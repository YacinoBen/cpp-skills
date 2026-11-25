import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys


def check_repo(root: pathlib.Path) -> list[str]:
    errors: list[str] = []

    # 1. Verify SKILL.md and its minimal frontmatter
    skill_files = [p for p in root.rglob("SKILL.md") if ".git" not in p.parts]
    if not skill_files:
        errors.append("No SKILL.md file found.")

    for skill_file in skill_files:
        content = skill_file.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match:
            errors.append(f"{skill_file}: missing or malformed YAML frontmatter.")
            continue

        frontmatter = match.group(1)
        name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.MULTILINE)
        desc_match = re.search(r"^description:\s*.+$", frontmatter, re.MULTILINE)

        if not name_match or not desc_match:
            errors.append(f"{skill_file}: missing or invalid 'name' or 'description' in frontmatter.")
        elif name_match.group(1) != skill_file.parent.name:
            errors.append(
                f"{skill_file}: 'name' ({name_match.group(1)}) does not match parent directory ({skill_file.parent.name})."
            )

    # 2. Verify relative Markdown links (ignoring fenced and inline code)
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for md_file in root.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        text = md_file.read_text(encoding="utf-8")
        text_no_fences = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        text_clean = re.sub(r"`[^`\n]+`", "", text_no_fences)

        for target in link_pattern.findall(text_clean):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{md_file}: broken link -> {target}")

    # 3. Verify kebab-case naming inside cpp-skills/ (and skills/ if present)
    kebab_re = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*(\.(md|ya?ml))?$")
    allowed_exact = {"SKILL.md", ".clang-tidy", ".clang-format", "BuildOptimization.cmake"}

    for dir_name in ("cpp-skills", "skills"):
        base = root / dir_name
        if base.exists():
            for p in base.rglob("*"):
                if ".git" in p.parts:
                    continue
                if p.name in allowed_exact:
                    continue
                if p.name.startswith("."):
                    continue
                if not kebab_re.match(p.name):
                    errors.append(f"Non-kebab-case name: {p}")

    # 4. Verify JSON manifests (.claude-plugin/plugin.json, .codex-plugin/plugin.json,
    #    marketplace.json files, gemini-extension.json, and .claude/settings.json)
    loaded_manifests: dict[str, dict] = {}

    for json_file in root.rglob("*.json"):
        if ".git" in json_file.parts:
            continue
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{json_file}: invalid JSON -> {exc}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{json_file}: top-level JSON must be an object.")
            continue

        rel_key = str(json_file.relative_to(root).as_posix())
        loaded_manifests[rel_key] = data

        if json_file.name == "gemini-extension.json":
            for field in ("name", "version", "description"):
                if not isinstance(data.get(field), str) or not data[field].strip():
                    errors.append(f"{json_file}: missing or empty '{field}'.")

        elif json_file.name == "plugin.json":
            for field in ("name", "version", "description"):
                if not isinstance(data.get(field), str) or not data[field].strip():
                    errors.append(f"{json_file}: missing or empty '{field}'.")

            skills_path = data.get("skills")
            if skills_path is not None:
                if not isinstance(skills_path, str) or not skills_path.strip():
                    errors.append(f"{json_file}: 'skills' must be a non-empty string path.")
                else:
                    resolved_skills = (json_file.parent / skills_path).resolve()
                    if not resolved_skills.exists():
                        errors.append(f"{json_file}: 'skills' path does not exist -> {skills_path}")

            if json_file.parent.name == ".codex-plugin" or "interface" in data:
                iface = data.get("interface")
                if not isinstance(iface, dict):
                    errors.append(f"{json_file}: missing or invalid 'interface' object.")
                else:
                    for ifield in ("displayName", "shortDescription", "longDescription", "category"):
                        if not isinstance(iface.get(ifield), str) or not iface[ifield].strip():
                            errors.append(f"{json_file}: interface missing or empty '{ifield}'.")
                    if not isinstance(iface.get("capabilities"), list) or not iface["capabilities"]:
                        errors.append(f"{json_file}: interface 'capabilities' must be a non-empty list.")

        elif json_file.name == "marketplace.json":
            for field in ("name", "owner", "plugins"):
                if field not in data:
                    errors.append(f"{json_file}: missing '{field}'.")
            if not isinstance(data.get("plugins"), list) or not data["plugins"]:
                errors.append(f"{json_file}: 'plugins' must be a non-empty list.")
            else:
                for idx, entry in enumerate(data["plugins"]):
                    if not isinstance(entry, dict):
                        errors.append(f"{json_file}: plugins[{idx}] must be an object.")
                        continue
                    if not isinstance(entry.get("name"), str) or not entry["name"].strip():
                        errors.append(f"{json_file}: plugins[{idx}] missing or empty 'name'.")
                    if "source" not in entry:
                        errors.append(f"{json_file}: plugins[{idx}] missing 'source'.")

        elif rel_key == ".claude/settings.json":
            extra = data.get("extraKnownMarketplaces")
            if extra is not None:
                if not isinstance(extra, dict) or not extra:
                    errors.append(f"{json_file}: 'extraKnownMarketplaces' must be a non-empty object.")
                else:
                    for m_name, m_cfg in extra.items():
                        if not isinstance(m_cfg, dict) or "source" not in m_cfg:
                            errors.append(f"{json_file}: extraKnownMarketplaces['{m_name}'] missing 'source'.")

    required_manifests = [
        "gemini-extension.json",
        ".claude-plugin/plugin.json",
        ".codex-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        ".agent/plugins/marketplace.json",
        ".claude/settings.json",
    ]
    for req in required_manifests:
        if req not in loaded_manifests:
            errors.append(f"Missing expected manifest: {req}")

    # Version consistency across plugin.json files and gemini-extension.json
    versions: dict[str, str] = {}
    for key, data in loaded_manifests.items():
        if key.endswith("plugin.json") or key == "gemini-extension.json":
            ver = data.get("version")
            if isinstance(ver, str) and ver.strip():
                versions[key] = ver.strip()

    unique_versions = set(versions.values())
    if len(unique_versions) > 1:
        details = ", ".join(f"{k}={v}" for k, v in versions.items())
        errors.append(f"Version mismatch across manifests: {details}")

    return errors


def check_claude_environment() -> list[str]:
    notes: list[str] = []
    claude_bin = shutil.which("claude")
    if not claude_bin:
        notes.append("[WARN] 'claude' CLI not found in PATH.")
    else:
        try:
            proc = subprocess.run(
                [claude_bin, "--version"],
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            version_out = (proc.stdout or proc.stderr).strip()
            notes.append(f"[INFO] Claude CLI: {version_out or claude_bin}")
        except OSError as exc:
            notes.append(f"[WARN] Could not run 'claude --version': {exc}")

    home_claude = pathlib.Path.home() / ".claude"
    plugins_dir = home_claude / "plugins"
    notes.append(
        f"[INFO] ~/.claude exists: {home_claude.exists()} | ~/.claude/plugins exists: {plugins_dir.exists()}"
    )
    return notes


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate cpp-skills repository structure and manifests.")
    parser.add_argument("--root", default=".", help="Repository root path to validate.")
    parser.add_argument(
        "--check-claude",
        action="store_true",
        help="Inspect local Claude Code CLI and ~/.claude/plugins directory.",
    )
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    errors = check_repo(root)

    if args.check_claude:
        for line in check_claude_environment():
            print(line)

    if errors:
        print("\n".join(f"[ERROR] {e}" for e in errors))
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
