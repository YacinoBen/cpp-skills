# Error Handling & Exception Safety
## Overview

Guidelines for robust error handling in modern C++23, balancing value-based expected return types (`std::expected`) for recoverable errors with structured exception handling and strict exception safety guarantees for exceptional conditions.

## Modern Value-Based Error Handling (C++23)

- **`std::expected` & `std::unexpected`**: Prefer `std::expected<T, E>` (from `<expected>`) over raw error codes, `std::optional` (when failure reasons matter), or output parameters for recoverable, expected failure paths (e.g., parsing, I/O, network validation).
- **Monadic Composition**: Leverage C++23 monadic operations (`.and_then()`, `.transform()`, `.or_else()`, `.transform_error()`) to chain error-prone operations cleanly without deeply nested `if` checks.
- **Domain Error Enums**: Pair `std::expected` with strongly typed `enum class` error descriptors or lightweight error structs to make failure states explicit in function signatures.

## Exception Handling Strategy

- **Exceptional Conditions Only**: Use C++ exceptions for truly exceptional, unrecoverable, or constructor-level failures where invariants cannot be established.
- **Custom Exception Hierarchies**: Define custom exception classes inheriting from standard library types (such as `std::runtime_error` or `std::logic_error`) to represent domain-specific errors clearly.
- **Catch by Const Reference**: Always catch exceptions by `const` reference (`catch (const CustomException& e)`) to prevent object slicing and avoid unnecessary copies.
- **Preserve Original Exceptions**: Rethrow active exceptions using bare `throw;` rather than `throw e;` to preserve the dynamic type and stack context of the original exception.

## `noexcept` & Exception Safety Guarantees

- **`noexcept` Specifier**: Mark non-throwing functions—especially move constructors, move assignment operators, swap functions, and destructors—with `noexcept` to enable standard library container optimizations and prevent unexpected `std::terminate` calls.
- **Strong Exception Guarantee**: Design operations to provide the **Strong Exception Guarantee** (commit-or-rollback semantics) wherever possible, ensuring program state remains completely unchanged if an error occurs.
- **Basic & No-Throw Guarantees**: At a minimum, uphold the **Basic Exception Guarantee** (no resource leaks and valid object invariants) via RAII, and reserve the **No-Throw Guarantee** for critical cleanup and state-swap paths.