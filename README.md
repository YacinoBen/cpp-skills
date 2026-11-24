# C++ Skills Repository (`cpp-skills`)

Modular C++ reference guidelines designed to configure LLMs and coding assistants (Claude Code, Cursor, Copilot, etc.) to generate clean, ISO-compliant, and documented modern C++ code.

# Project Instructions
Follow all behavioral, documentation, and technical rules defined in `cpp-skills/context.md`.


*(Note: `context.md` automatically routes the AI to `cpp-skills/SKILL.md` and the relevant domain files.)*

# Installation
## Quick Integration

Only the **`cpp-skills/`** directory is required in your project workspace (the entry point is `cpp-skills/context.md`).

1. **Copy or clone only the `cpp-skills/` folder** into your C++ project root (or `.claude/skills/`).
2. **Point your assistant's configuration file** (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or Custom Instructions) to `cpp-skills/context.md`:

```markdown
claude.md
```

## Claude Code & Agent Installation

### Claude Code Plugin / Marketplace

Add the repository as a marketplace and install the plugin directly inside Claude Code:

```bash
/plugin marketplace add YacinoBen/cpp-skills
/plugin install cpp-skills@yacinoben-cpp-skills
```

## Usage Examples

### 1. Asynchronous Server (C++20 Coroutines)
- **Prompt:** *"Write a C++20 coroutine-based TCP echo server that reads from a socket and echoes data back asynchronously."*

### 2. Lock-Free Queue (C++23 Concurrency)
- **Prompt:** *"Implement a low-contention thread-safe queue in C++23 with explicit memory ordering."*
- 

# Test the documentation

Before push, run this python file:

```bash
python scripts/check.py
```

# Attribution & License

Standard feature lists and language version summaries in this section are adapted from [cppreference.com](https://en.cppreference.com/) (licensed under **CC BY-SA**). All custom guidelines, examples, configurations, and repository structure are governed by the repository's `LICENSE` file.