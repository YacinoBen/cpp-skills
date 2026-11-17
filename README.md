# C++ Skills Repository (`cpp-skills`)

Production-grade, modular C++ reference guidelines and skills designed to feed LLMs and coding assistants (such as Claude Code) with clean, ISO-compliant, developer-first documentation.

---

## 🎯 Core Philosophy: The "Prompt-to-Code" Workflow

This repository is built around a **Prompt-to-Code** workflow. The goal is simple: **you never write the C++ code yourself; you write a precise technical prompt**, and your assistant reads the modular documentation in this repository to generate clean, modern, and production-ready C++ code.

---

## 📂 Repository Structure

- `versions/` : Language specifications and compiler support matrices (C++11, C++14, C++17, C++20, C++23, C++26, C++29, and general index).
- `architecture/` : Patterns, design principles, and algorithms.
- `core/` : Core language features (coroutines, lambdas, templates, safety, error handling).
- `standards/` : Naming conventions, style guides, and ISO Core Guidelines enforcement.
- `performance/` : Memory management, containers, concurrency, and optimization techniques.
- `hardware/` : Low-level compute, hardware acceleration, and SIMD data-parallel types.
- `build/` : Build system management, CMake best practices, and presets.
- `quality/` : Testing strategies, diagnostics, static analysis, and documentation guidelines.

---

## 🚀 How to Use It (With or Without Claude)

You don't *have* to use Claude. Any modern LLM or AI assistant can leverage these skills as long as your workspace points to them.

### Option 1: Integrating with Claude Code (or any AI assistant)

1. Clone or copy this repository into your project (e.g., inside a `skills/` folder or at your workspace root).
2. Create or update a `CLAUDE.md` file (or your assistant's system prompt configuration) at your project root to reference these files:

```markdown
# Project Instructions

You are an expert modern C++ developer (C++20/C++23). 
Always refer to the modular documentation inside the `skills/` directory to ensure compliance with our architecture, memory safety standards, and modern syntax guidelines:
- Versions & Features: `skills/versions/`
- Core Mechanics (Coroutines, etc.): `skills/core/`
- Performance & Concurrency: `skills/performance/`
```

---

## 💡 Practical Examples: Prompt-to-Code in Action

Instead of writing boilerplate or searching documentation, you interact with your assistant using high-level technical prompts.

### Example 1: Asynchronous Task with Coroutines (C++20)
* **Your Prompt:**
  > *"Write a C++20 coroutine-based TCP echo server that reads from a socket and echoes back data asynchronously, using our `cpp-skills` coroutines guidelines."*
* **What the Assistant Does:** It loads `skills/core/coroutines.md`, checks signature and suspension requirements, and outputs the correct `co_await` / `co_return` boilerplate safely without use-after-free parameter bugs.

### Example 2: High-Performance Concurrent Queue (C++20/C++23)
* **Your Prompt:**
  > *"Implement a lock-free or low-contention thread-safe queue for high-frequency trading in C++23, utilizing memory order constraints specified in our performance guidelines."*
* **What the Assistant Does:** It cross-references `skills/performance/` and `skills/versions/cpp-23.md` to write a robust, cache-aligned implementation using `std::atomic` and proper acquire-release semantics.

---

## 🛠️ Requirements & Contribution
- **Language:** English (mandatory for all skill modules).
- **Style:** Developer-first, ISO-compliant, free of external paper noise and ISO boilerplate.
- **CI/CD:** Optional at this stage; focus remains entirely on documentation quality and modularity.