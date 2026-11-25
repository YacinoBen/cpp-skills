# Architecture & Design Patterns Reference

## Overview
Guidelines for writing clean, modular, and maintainable modern C++ code, combining fundamental software engineering principles, multi-paradigm programming, and proven architectural patterns.

## Clean Code & Core Principles
- **Modern Standards**: Write clean, idiomatic C++ following modern standards (C++20/C++23), leveraging standard library facilities over custom workarounds.
- **Meaningful Naming**: Choose clear, self-documenting names for variables, functions, and types to minimize the need for redundant comments.
- **Composition Over Inheritance**: Favor assembling behavior through object composition and interfaces rather than deep, rigid inheritance hierarchies.
- **Small & Focused Functions**: Adhere to the Single Responsibility Principle at the function level—keep functions concise, readable, and dedicated to a single task.

## Software Engineering Principles
- **SOLID**:
  - **S**ingle Responsibility Principle
  - **O**pen/Closed Principle
  - **L**iskov Substitution Principle
  - **I**nterface Segregation Principle
  - **D**ependency Inversion Principle
- **DRY (Don't Repeat Yourself)**: Abstract shared logic into reusable templates, functions, or components to eliminate code duplication.
- **KISS (Keep It Simple, Stupid)**: Favor straightforward, readable solutions over unnecessary complexity.
- **YAGNI (You Aren't Gonna Need It)**: Implement features and abstractions only when actually required, avoiding speculative over-engineering.

## Programming Paradigms in C++
- **Object-Oriented Programming (OOP)**: Encapsulate state and behavior cleanly using RAII, access specifiers, and controlled polymorphism:
  - **Polymorphic Base Destructors & `override`**: Always declare a `virtual` destructor (e.g., `virtual ~Base() = default;`) in polymorphic base classes so deleting through a base pointer does not cause undefined behavior. Mark every overriding method in derived classes with `override` (and avoid repeating `virtual` or mixing `virtual` and `override` inconsistently; use `final` on classes or overrides where extension is not intended).
  - **Rule of Zero, Rule of Three, and Rule of Five**:
    - *Rule of Zero (Default)*: Prefer types composed of RAII members (`std::unique_ptr`, `std::vector`, `std::string`, custom RAII handles) that do not define custom copy/move constructors, copy/move assignment operators, or destructors.
    - *Rule of Three*: If a class requires a custom destructor, copy constructor, or copy assignment operator (typically for legacy resource management), define all three.
    - *Rule of Five*: If a class defines a custom destructor or copy operation and supports move semantics, explicitly declare or `= delete` all five special member functions (destructor, copy constructor, copy assignment, move constructor, move assignment) to avoid unintended copies or moved-from state bugs.
  - **Scope Guards & RAII (`scope_exit`)**: Tie resource release, lock handling, and rollback actions to object lifetimes via RAII. Use scope-guard idioms (`scope_exit` / `scope_fail` / `scope_success` or dedicated RAII guard types) to guarantee cleanup on all exit paths, including early returns and exceptions, without manual cleanup blocks.
  - **Dynamic vs. Static Polymorphism**:
    - *Dynamic Polymorphism*: Uses `virtual` dispatch (vtable indirection) or runtime type erasure (`std::function`, custom erased wrappers) when concrete types are selected at runtime or behind a stable ABI/plugin boundary.
    - *Static Polymorphism*: Uses templates, C++20 `concepts`, CRTP (Curiously Recurring Template Pattern), or `std::variant` + `std::visit` to resolve dispatch at compile time, enabling inlining, zero vtable overhead, and value semantics when the type set is known at compile time.
- **Generic Programming**: Use C++ templates and C++20 `concepts` to write type-safe, reusable algorithms and data structures without runtime overhead.
- **Metaprogramming**: Leverage `constexpr`, `consteval`, and `<type_traits>` for compile-time computation and static introspection.
- **Functional Programming**: Utilize pure functions, immutability (`const`), lambdas, and `<ranges>` pipelines to minimize side effects.
- **Data-Oriented Design (DOD)**: Organize data layouts around CPU cache lines and memory access patterns (e.g., Structure of Arrays) for high-throughput workloads.
- **Procedural & Recursion**: Use straightforward procedural flows for linear tasks and controlled recursion (or tail-recursive patterns) for naturally hierarchical problems.

## Architectural & Design Patterns
- **Behavioral Patterns**:
  - **Strategy**: Encapsulate interchangeable algorithms behind a common interface or template policy.
  - **Template Method**: Define the skeleton of an algorithm in a base class/template while delegating specific steps to subclasses or policy parameters.
- **Creational & Structural Patterns**:
  - **Factory**: Centralize and decouple object instantiation logic from client code.
  - **Registry**: Maintain dynamic lookup tables mapping identifiers to factories, handlers, or services.
- **Architectural Patterns**:
  - **MVC (Model-View-Controller)**: Separate core data/business logic (Model), presentation (View), and input/event handling (Controller) to decouple UI from domain logic.
