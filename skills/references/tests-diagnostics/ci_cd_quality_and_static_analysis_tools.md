# CI/CD Quality and Static Analysis Tools

Guidelines for automated code formatting, static analysis, and continuous quality checks in modern C++ projects.

---

## Clang-Format

- **Automated Formatting:** Enforce consistent formatting across C++ source and header files using the `.clang-format` configuration.
- **Reference Configuration:** See [`.clang-format`](./.clang-format).

---

## Clang-Tidy

- **Static Analysis:** Run static analysis checks to detect modern C++ anti-patterns, potential bugs, and optimization opportunities using a compilation database (`compile_commands.json`).
- **Reference Configuration:** See [`.clang-tidy`](./.clang-tidy).

---

## SonarQube / Quality Gates

- **Centralized Quality Tracking:** Centralize code quality metrics, vulnerability tracking, and maintainability scores across branches and pull requests.
- **New Code Focus:** Enforce quality gates primarily on newly added or modified code rather than blocking on legacy technical debt.
- **Complementary Checks:** Pair static analysis tools with strict compiler warnings and runtime sanitizers rather than treating them as a replacement.