# C++ Skills Repository (`cpp-skills`)

Production-grade, modular C++ reference guidelines and skills designed to feed LLMs and coding assistants (such as Claude Code) with clean, ISO-compliant, developer-first documentation.

---

## 🎯 Core Philosophy: The "Prompt-to-Code" Workflow

This repository is built around a **Prompt-to-Code** workflow. The goal is simple: **you never write the C++ code yourself; you write a precise technical prompt**, and your assistant reads the modular documentation in this repository to clean, modern, and production-ready C++ code.

---

## 📂 Repository & Skills Structure

To avoid downloading unnecessary repository files (like root licenses or meta files), ensure you only download or include the **`skills/`** folder inside your project. 

Inside `skills/`, the entry point is **`skills.md`**:

```markdown
# C++ Development Guidelines
You are an expert in modern C++ development with deep knowledge of C++ standards, memory management, and high-performance programming.

## C++ Versions
- **C++ modern & Legacy Standards**: See the [versions/](versions/) directory

## Architecture & Design
- **Patterns & Algorithms**: See the [architecture/](architecture/) directory

## Core Development
- **Best Practices, Templates, Safety & Errors**: See the [core/](core/) directory

## Naming Conventions & Standards
- **Naming & Code Style**: See the [standards/](standards/) directory

## Performance & Memory
- **Memory, Containers, Concurrency & Optimization**: See the [performance/](performance/) directory

## Hardware Acceleration
- **Low-level Compute & SIMD**: See the [hardware/](hardware/) directory

## Build & Package Management
- **CMake & Presets**: See the [build/](build/) directory

## Quality & Diagnostics
- **Testing, CI/CD, Diagnostics & Documentation**: See the [quality/](quality/) directory
```

---

## 🚀 How to Integrate the `skills/` Folder

1. **Extract or Copy only the `skills/` directory** into your target C++ project workspace (e.g., at your project root or under `.claude/skills/`).
2. Point your AI assistant or configure your workspace instructions (like a `CLAUDE.md` file at your project root) to use `skills/skills.md` as the core system prompt reference:

```markdown
# Project Instructions

You are an expert modern C++ developer (C++20/C++23). 
Always refer to the guidelines and documentation inside the `skills/` directory:
- Main Entry Point: `skills/skills.md`
- Core Features: `skills/core/`
- Versions: `skills/versions/`
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