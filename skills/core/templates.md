# Templates & Concepts Reference

## Overview

Guidelines for writing expressive, type-safe, and maintainable generic C++23 code using function and class templates, variadic parameter packs, and C++20/23 `concepts` for compile-time interface constraints.

## Function & Class Templates

* **Function Templates**: Prefer concise function templates (and C++20 abbreviated function templates using `auto` parameters when constrained by concepts) for generic algorithms without runtime polymorphism overhead.
* **Class Templates & CTAD**: Design class templates with clear type invariants and leverage Class Template Argument Deduction (CTAD) alongside custom deduction guides where appropriate.
* **Header Organization**: Keep template definitions visible in headers (or `.tpp`/`.inl` files included at the bottom of headers) so the compiler can instantiate them across translation units.
* **Explicit Instantiation**: Use explicit template instantiation (`extern template`) in large projects to reduce compilation times and binary bloat for commonly used concrete types.

## Variadic Templates & Fold Expressions

* **Parameter Packs (`typename... Args`)**: Use variadic templates to accept arbitrary numbers of type-safe arguments, forwarding them efficiently with `std::forward<Args>(args)...`.
* **Fold Expressions (C++17)**: Prefer C++17 unary and binary fold expressions (`(args + ...)`, `(process(args), ...)`) over recursive template instantiation to keep compile times fast and code readable.
* **Pack Indexing (C++26) & `std::tuple`**: Use `std::forward_as_tuple`, `std::apply`, or `sizeof...(Args)` to inspect and manipulate parameter packs cleanly at compile time.

## Concepts & Compile-Time Constraints (C++20/23)

* **Prefer Concepts Over SFINAE**: Replace complex `std::enable_if` and SFINAE idioms with readable `concept` definitions and `requires` clauses to produce clear, human-readable compiler diagnostics.
* **Standard Library Concepts**: Leverage built-in concepts from `<concepts>` and `<ranges>` (e.g., `std::integral`, `std::floating_point`, `std::invocable`, `std::ranges::range`) before defining custom ones.
* **Custom Domain Concepts**: Define cohesive, semantic concepts (`template <typename T> concept Serializable = requires(T a) { ... };`) to document and enforce structural and behavioral requirements on template parameters.
* **Subsumption & Overloading**: Order constrained template overloads from most specific to least specific concept so the compiler resolves dispatch unambiguously via concept subsumption.