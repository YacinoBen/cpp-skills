# C++ Skills Repository (`cpp-skills`)

Modular modern C++ (C++11–C++23) reference guidelines and coding standards for AI coding assistants (Claude Code, Codex, Gemini CLI, Cursor, and Copilot). Designed for deterministic memory management, zero-cost abstractions, MISRA C++:2023 alignment, and consistent API documentation.

## Repository Structure

- `SKILL.md`: Primary entry point containing behavioral rules, documentation standards, and domain routing to `references/`.
- `references/`: Modular reference sheets organized by domain (`versions/`, `architecture/`, `core/`, `standards/`, `performance/`, `hardware/`, `build/`, and `quality/`).
- `scripts/check.py`: Validation script checking repository structure, links, and reference consistency.

## Installation

Only the `cpp-skills/` directory is needed in a target repository or agent skill path.

### 1. Copy or Clone into Your Workspace
Place `cpp-skills/` in your project root or under your assistant's skills directory (for example, `.claude/skills/cpp-skills`).

### 2. Wire Your Assistant Configuration
Point `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or system instructions to `SKILL.md`:

```markdown
Read and apply `cpp-skills/SKILL.md` and the relevant files in `cpp-skills/references/` before writing, refactoring, or reviewing C++ code.
```

### 3. Claude Code Marketplace
Add the repository and install the plugin directly from Claude Code:

```bash
/plugin marketplace add YacinoBen/cpp-skills
/plugin install cpp-skills@yacinoben-cpp-skills
```

## Usage Examples

- **Async Networking (C++20):** *"Write a C++20 coroutine-based TCP echo server that reads from a socket and echoes data back asynchronously."*
- **Lock-Free Data Structures (C++23):** *"Implement a low-contention thread-safe queue in C++23 with explicit memory ordering and RAII ownership."*
- **Compile-Time & Range Pipelines (C++23):** *"Filter, transform, and materialize sensor samples with `std::views` and `std::ranges::to` without intermediate heap allocations."*

## Validation

Run the verification script before committing or pushing changes:

```bash
python scripts/check.py
```

## Attribution & License

Language feature lists and standard summaries are adapted from [cppreference.com](https://en.cppreference.com/) under **CC BY-SA**. Repository structure, reference guides, scripts, and examples follow the terms in `LICENSE`.