# Containers and Memory Safety Reference

## Overview
Guidelines for safe buffer management, standard sequence and associative containers, and modern C++23 container extensions designed for performance and cache-friendliness.

## Buffer and Memory Safety
- **Fixed-Size Arrays**: Use `std::array` instead of raw C-style arrays for compile-time size safety and bounds management.
- **Dynamic Sequences**: Use `std::vector` as the default dynamic container; prefer `.at()` for bounds-checked access when safety outweighs raw performance.
- **Strings**: Prefer `std::string` and `std::string_view` over C-style null-terminated strings (`char*`).
- **Contiguous Views**: Use `std::span` for safe, non-owning views over contiguous sequences of objects.
- **Multidimensional Views (C++23)**: Use `std::mdspan` for non-owning multidimensional array views, ideal for matrix and tensor computations without heap allocation overhead.

## Standard Sequence Containers
- **`std::vector`**: Default choice for dynamic arrays with contiguous memory layout and cache locality.
- **`std::deque`**: Double-ended queue for efficient insertions and deletions at both ends.
- **`std::list` / `std::forward_list`**: Doubly and singly linked lists for constant-time insertions/removals anywhere when pointer stability or frequent mid-sequence modifications are strictly required.

## Associative & Unordered Containers
- **Ordered (`std::map`, `std::set`)**: Balanced binary search trees maintaining sorted element order with logarithmic lookup times.
- **Unordered (`std::unordered_map`, `std::unordered_set`)**: Hash-based tables providing average constant-time complexity for insertions, deletions, and lookups.

## Flat Containers (C++23)
- **`std::flat_map` & `std::flat_set`**: Container adaptors providing associative container interfaces backed by sorted contiguous containers (like `std::vector`), ensuring superior cache locality and memory density at the cost of linear insertion/deletion performance.