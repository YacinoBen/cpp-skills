import pathlib
import re
import sys

root = pathlib.Path(".")
errors = []

# 1. Verify SKILL.md and its minimal frontmatter
skill_files = list(root.glob("**/SKILL.md"))
if not skill_files:
    errors.append("No SKILL.md file found.")

for skill_file in skill_files:
    if ".git" in skill_file.parts:
        continue
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

# 3. Verify kebab-case naming in skill directories
kebab_re = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*(\.(md|ya?ml))?$")
allowed_exact = {"SKILL.md", ".clang-tidy"}

for folder_name in ("skills", "cpp-skills"):
    base = root / folder_name
    if base.exists():
        for p in base.rglob("*"):
            if ".git" in p.parts or p.name.startswith(".") and p.name not in allowed_exact:
                continue
            if p.name in allowed_exact:
                continue
            if not kebab_re.match(p.name):
                errors.append(f"Non-kebab-case name: {p}")

if errors:
    print("\n".join(f"[ERROR] {e}" for e in errors))
    sys.exit(1)

print("All checks passed.")
