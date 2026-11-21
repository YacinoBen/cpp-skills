# Memory Management Reference

## Overview
Guidelines for safe, modern C++ memory management, emphasizing strict ownership models, RAII principles, and heap avoidance to ensure leak-free and exception-safe software.

## Smart Pointers
- **Exclusive Ownership**: Use `std::unique_ptr` as the default choice for managing dynamically allocated resources with single-owner semantics.
- **Shared Ownership**: Use `std::shared_ptr` strictly when shared, multi-owner lifetime management is explicitly required.
- **Circular Reference Prevention**: Use `std::weak_ptr` alongside `std::shared_ptr` to break ownership cycles and prevent memory leaks.
- **Owning Pointers**: Avoid raw owning pointers (`T*` that require manual `delete`); reserve raw pointers purely for non-owning observers or legacy interop.

## RAII (Resource Acquisition Is Initialization)
- **Universal Resource Management**: Bind the lifecycle of resources (memory, file descriptors, mutexes, sockets) directly to object scopes using RAII.
- **Custom Destructors**: Wrap complex resources in custom classes featuring robust destructors that clean up automatically upon scope exit.
- **Exception Safety**: Rely on RAII unwinding to guarantee that resources are safely released even when exceptions are thrown mid-execution.
- **Scope Guards**: Utilize scope guards or custom defer mechanisms to execute lightweight cleanup logic without writing redundant boilerplate.

## Best Practices & Heap Avoidance
- **Stack Allocation**: Prefer stack allocation over heap allocation whenever object sizes are known and lifetimes match local scopes to maximize performance and cache locality.
- **Safe Creation**: Use `std::make_unique` and `std::make_shared` for exception-safe, efficient pointer construction without explicit `new` calls.
- **Raw Allocation Ban**: Strictly avoid `new` and `delete` in application code; delegate all dynamic allocations to standard containers or smart pointers.
- **Container Usage**: Use standard containers instead of raw arrays or manual dynamic buffers to eliminate manual memory management overhead.