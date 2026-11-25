# C++ Skills Repository (`cpp-skills`)

Modular modern C++ (C++11 to C++23) reference guidelines and coding standards for AI coding assistants (Claude Code, Codex, Gemini CLI, Cursor, and Copilot). Designed for deterministic memory management, zero-cost abstractions, MISRA C++:2023 alignment, and consistent API documentation.

## Repository Structure

- `SKILL.md`: Primary entry point containing behavioral rules, documentation standards, and domain routing to `references/`.
- `references/`: Modular reference sheets organized by domain (`versions/`, `architecture/`, `core/`, `standards/`, `performance/`, `hardware/`, `build/`, and `quality/`).
- `scripts/check.py`: Validation script checking repository structure, links, and reference consistency.

## Installation

### Claude Code Plugin & Marketplace (Recommended)

Add the repository as a marketplace and install the plugin in Claude Code:

```bash
/plugin marketplace add YacinoBen/cpp-skills
/plugin install cpp-skills@yacinoben-cpp-skills
/reload-plugins
```

To install for a specific scope (`user` by default, `project`, or `local`):

```bash
claude plugin install cpp-skills@yacinoben-cpp-skills --scope project
```

### Manual / Local Copy

Only the `cpp-skills/` directory is needed in a target repository or agent skill path.

1. Place `cpp-skills/` in your project root or under your assistant's skills directory (for example, `.claude/skills/cpp-skills`).
2. Point `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or system instructions to `SKILL.md`:

```markdown
Read and apply `cpp-skills/SKILL.md` and the relevant files in `cpp-skills/references/` before writing, refactoring, or reviewing C++ code.
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

## Reference Sources & Inspiration

The guidelines and conventions in `cpp-skills` draw conceptual inspiration from established C++ references and engineering guides:

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) — core design, safety, resource management, and modern C++ rules.
- Herb Sutter's [Elements of Modern C++ Style](https://herbsutter.com/elements-of-modern-c-style/) and [GotW (Guru of the Week)](https://herbsutter.com/gotw/) — idiomatic style, lifetime clarity, and subtle language edge cases.
- Jason Turner's [C++ Best Practices](https://github.com/cpp-best-practices/cppbestpractices) — practical habits, tooling discipline, and defensive coding.
- Björn Andrist and Viktor Sehr's [C++ High Performance, 2nd edition](https://www.oreilly.com/library/view/c-high-performance/9781839216541/) — data layout, memory hierarchy, allocators, and performance engineering.
- OpenSSF [Compiler Options Hardening Guide](https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.html) — compiler security flags and hardening practices.
- [cppreference](https://en.cppreference.com/) — ISO C++ standard specifications, library behavior, and feature details.

## Attribution & License

Inspired by the modular skill-routing architecture of [`DiamonDinoia/skill-cpp`](https://github.com/DiamonDinoia/skill-cpp) (`skills/cpp`), adapted to the `cpp-skills` directory layout and workflow. Language feature lists and standard summaries are adapted from [cppreference.com](https://en.cppreference.com/) under **CC BY-SA**. Repository structure, reference guides, scripts, and examples follow the terms in `LICENSE`.