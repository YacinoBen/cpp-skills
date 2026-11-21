# C++ Skills Repository (`cpp-skills`)

Production-grade, modular C++ reference guidelines designed to configure LLMs and coding assistants (Claude Code, Cursor, Copilot, etc.) to generate clean, ISO-compliant, and documented modern C++ code.

---

## Core Philosophy: "Prompt-to-Code"

You write a precise technical prompt; your AI assistant follows the rules in `skills/` to generate modern, documented, and production-ready C++ code.

---

## Quick Integration

Only the **`skills/`** directory is required in your project workspace (the entry point is `skills/context.md`).

1. **Copy or clone only the `skills/` folder** into your C++ project root (or `.claude/skills/`).
2. **Point your assistant's configuration file** (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or Custom Instructions) to `skills/context.md`:

```markdown
# Project Instructions
Follow all behavioral, documentation, and technical rules defined in `skills/context.md`.
```

*(Note: `context.md` automatically routes the AI to `skills/skills.md` and the relevant domain files.)*

---

## Usage Examples

### 1. Asynchronous Server (C++20 Coroutines)
- **Prompt:** *"Write a C++20 coroutine-based TCP echo server that reads from a socket and echoes data back asynchronously."*
- **Result:** The AI loads `context.md` -> `skills.md` -> `core/`, and outputs Doxygen-documented coroutine code without lifetime bugs or conversational filler.

### 2. Lock-Free Queue (C++23 Concurrency)
- **Prompt:** *"Implement a low-contention thread-safe queue in C++23 with explicit memory ordering."*
- **Result:** The AI cross-references `performance/` and `versions/`, generating cache-aligned `std::atomic` code with `acquire`/`release` semantics and inline comments explaining the memory barriers.