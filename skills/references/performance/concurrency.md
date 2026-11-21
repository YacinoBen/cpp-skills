# Multithreading and Concurrency Reference

## Overview
Guidelines for safe, modern C++ concurrent programming, covering thread management, synchronization primitives, lock-free operations, and asynchronous task execution.

## Thread Management
- **`std::jthread` (C++20)**: Use `std::jthread` for automatic RAII-based joining upon destruction and built-in cooperative cancellation via `std::stop_token`. Note that depending on target platform toolchains (such as older Apple Clang/macOS SDKs), `std::jthread` support may require updated runtime environments.
- **`std::thread`**: Standard thread primitive available since C++11, requiring explicit manual lifecycle management (`join()` or `detach()`) to prevent `std::terminate` upon destruction.

## Synchronization and Mutual Exclusion
- **RAII Locks**: Prefer **`std::scoped_lock` (C++17)** as the default choice for locking one or more mutexes simultaneously, preventing deadlocks via deadlock-avoidance algorithms. Use `std::unique_lock` or `std::shared_lock` when advanced ownership transfer or shared locking is needed.
- **Mutexes**: Use `std::mutex` for exclusive synchronization and `std::shared_mutex` (C++17) for reader-writer concurrency patterns.

## Semaphores and Thread Coordination
- **Semaphores (C++20)**: Use `std::counting_semaphore` and `std::binary_semaphore` for lightweight signaling and resource counting across concurrent threads.
- **Condition Variables**: Use `std::condition_variable` alongside a `std::unique_lock<std::mutex>` for efficient blocking and thread notification patterns.

## Asynchronous Tasks and Futures
- **Futures & Promises**: Use `std::async` for launching simple asynchronous task execution, and combine `std::future`, `std::promise`, and `std::packaged_task` to retrieve results and propagate exceptions across thread boundaries.

## Lock-Free Programming and Atomics
- **`std::atomic`**: Use for lock-free thread-safe operations on fundamental types, ensuring correct memory ordering semantics when designing high-performance concurrent data structures.

## Optimization
Use if possible False Sharing and True Sharing