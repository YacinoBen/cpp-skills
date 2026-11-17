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
- **Object-Oriented Programming (OOP)**: Encapsulate state and behavior cleanly using RAII, access specifiers, and polymorphism where appropriate.
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