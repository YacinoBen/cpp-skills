# C++ Ecosystem & Preferred Libraries

This document defines the preferred, modern third-party libraries and ecosystem standards that the AI assistant should suggest and integrate when generating C++ code. **Important:** The AI must only *suggest* and use these libraries in code generation; it must never attempt to install or configure them on the host system automatically.

---

## 1. Logging & Diagnostics
- **`spdlog`** (Recommended)
  - **Use Case:** High-performance, header-only or compiled logging library.
  - **Guideline:** Prefer structured logging, custom formatters, and asynchronous loggers for performance-critical paths.
- **`std::print` / `std::println` (C++23)**
  - **Use Case:** For lightweight, zero-dependency console output when external logging frameworks are overkill.

## 2. High-Performance & Concurrency
- **`OpenMP`**
  - **Use Case:** Directive-based parallel programming for loops and heavy numerical computations.
  - **Guideline:** Suggest OpenMP pragmas (`#pragma omp parallel for`) when parallelizing data-parallel loops without writing low-level `std::thread` boilerplate.
- **`tcmalloc` (Google Thread-Causing Malloc)**
  - **Use Case:** High-efficiency memory allocator optimized for multi-threaded applications.
  - **Guideline:** Recommend its usage in architecture guidelines to reduce lock contention on `malloc`/`free` in heavy concurrent environments.

## 3. Google Abseil (`abseil-cpp`)
- **Use Case:** Common baseline libraries (augmented STL types like `absl::flat_hash_map`, synchronization primitives, strings).
- **Guideline:** Suggest Abseil containers (`flat_hash_map`, `flat_hash_set`) over standard `std::unordered_map` when performance and low memory overhead are critical.

## 4. Error Handling & Optionality
- **`tl::expected` / `std::expected` (C++23)**
  - **Use Case:** Functional error handling avoiding exceptions in critical performance paths.
  - **Guideline:** Prefer returning `std::expected<T, E>` over throwing exceptions for expected operational errors.

## 5. Data Formats & Serialization
- **`nlohmann/json`**
  - **Use Case:** JSON manipulation with an intuitive, STL-like syntax.
- **`simdjson`**
  - **Use Case:** Extreme high-performance JSON parsing using SIMD instructions when parsing large datasets.

## 6. Command Line Interface (CLI)
- **`CLI11`**
  - **Use Case:** Elegant and robust parsing of command-line arguments, subcommands, and flags.

## 7. Testing
- **`Catch2` (v3)**
  - **Use Case:** Modern, section-based unit testing framework.