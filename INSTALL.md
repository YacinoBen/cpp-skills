# Installation Guide — `cpp-skills`

This guide covers installing and enabling **C++ Skills (`cpp-skills`)** guidelines across supported AI assistants (**Claude Code**, **Codex**, and **Gemini CLI**), starting with a standalone **Manual Copy** step that uses only the `cpp-skills/` directory.

## Step 1: Manual Copy (`cpp-skills/` Only)

Only the `cpp-skills/` directory (`SKILL.md` and `references/`) is required to get the Modern C++ (`C++11` to `C++23`) guidelines and reference sheets. Repository manifest files (`.claude-plugin/`, `.codex-plugin/`, `.agent/`, `gemini-extension.json`, `.claude/settings.json`, `scripts/`) are not needed for a standalone copy.

Download the `cpp-skills/` directory directly from the repository (`https://github.com/YacinoBen/cpp-skills`) and place it in your target project or skills path.

Once `cpp-skills/` is in place, you can wire it into your assistant instructions (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or equivalent) as needed:

```
Read and apply `cpp-skills/SKILL.md` and the relevant files in `cpp-skills/references/` before writing, refactoring, or reviewing C++ code.
```

## Step 2: Claude Code

Add the repository as a marketplace and install the plugin in Claude Code:

```
/plugin marketplace add YacinoBen/cpp-skills
/plugin install cpp-skills@yacinoben-cpp-skills
/reload-plugins
```

To install for a specific scope (`user` by default, `project`, or `local`):

```
claude plugin install cpp-skills@yacinoben-cpp-skills --scope project
```

## Step 3: Codex

Use the repository manifest in `.codex-plugin/plugin.json` alongside `cpp-skills/SKILL.md` and `cpp-skills/references/`, or reference `cpp-skills/SKILL.md` from `AGENTS.md` in your workspace.

## Step 4: Gemini CLI

Use `gemini-extension.json` alongside `cpp-skills/SKILL.md` and `cpp-skills/references/`, or reference `cpp-skills/SKILL.md` in `GEMINI.md` / your system instructions.

## Step 5: Repository Validation

From the root of the `cpp-skills` repository, verify manifests, relative links, and naming rules with:

```
python scripts/check.py
```