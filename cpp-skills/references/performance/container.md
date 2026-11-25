# Containers and Memory Safety Reference

## Overview
Guidelines for safe buffer management, standard sequence and associative containers, string handling, and modern C++ extensions (C++11 through C++23) designed for performance and cache-friendliness.

---

## Container Selection by Workload

| Workload / Need | Container Choice |
|---|---|
| Default sequential storage | `std::vector` (C++11 move/emplace, C++17 CTAD, C++20 `std::erase` / `std::erase_if`) |
| Compile-time fixed capacity | `std::array` (C++11, C++17 CTAD) |
| Front/back growth with stable element addresses | `std::deque` (C++11 move/emplace, C++20 `std::erase` / `std::erase_if`) |
| Element and iterator stability across mutations, or node splicing | `std::list`, `std::forward_list` (C++11 `splice` / `merge`, C++14 heterogeneous lookup on associative, C++20 `std::erase` / `std::erase_if`) |
| Sorted keys, ordered traversal, or range lookups | `std::map`, `std::set` (C++11 `emplace`, C++17 `try_emplace` / `insert_or_assign` / `extract` / `merge`) |
| Average constant-time lookup without ordering | `std::unordered_map`, `std::unordered_set` (C++11, C++17 `try_emplace` / `insert_or_assign` / `extract` / `merge`, C++20 `contains`) |
| Read-heavy lookups, rare insertions, cache locality | Sorted `std::vector`, or `std::flat_map` / `std::flat_set` (C++23) |
| Small, bounded capacity on hot paths | Fixed `std::array` with an explicit count, or a small-buffer container |

---

## Buffer and Memory Safety
- **Fixed-Size Arrays**: Use `std::array` (C++11) instead of raw C-style arrays for compile-time size safety and bounds management.
- **Dynamic Sequences**: Use `std::vector` as the default dynamic container; prefer `.at()` when out-of-range indices are possible and reserve `operator[]` for proven in-range hot paths.
- **`std::vector<bool>` Caveat**: Avoid `std::vector<bool>` when standard element references (`bool&`) or direct byte semantics are required, as it packs bits via proxy references; prefer `std::vector<char>` or `std::bitset`.
- **Contiguous Views**: Use `std::span` (C++20) for safe, non-owning views over contiguous sequences of objects.
- **Multidimensional Views (C++23)**: Use `std::mdspan` (C++23) for non-owning multidimensional array views, ideal for matrix and tensor computations without heap allocation overhead.

---

## Strings, Formatting & Number Conversions
- **Ownership vs. Observation**: `std::string` owns its characters, whereas `std::string_view` (C++17) is a non-owning view and is **not** guaranteed to be null-terminated.
- **Parameter Passing**: Accept `std::string_view` (C++17) when a function only reads text, and take `std::string` by value when the function needs to store or sink an owned copy.
- **Loop Construction**: Pre-allocate with `reserve()` and append in loops rather than concatenating with `+`, avoiding repeated reallocations and temporary string copies.
- **Formatting & Output**: Prefer `std::format` (C++20) and `std::print` (C++23) over type-unsafe `printf` or heavy stream chains; fall back to `fmt` (if already in the project) or iostreams on older standards (C++11–C++17).
- **Custom Formatters (C++20)**: Specialize `std::formatter` (C++20) for custom project types by implementing `parse()` (throwing `std::format_error` on invalid format specifiers) and `format()`.
- **Locale-Free Conversions (`<charconv>`)**: Prefer `std::from_chars` and `std::to_chars` (C++17) for fast, allocation-free, locale-independent conversions over `stoi` / `to_string` (C++11), `atoi`, or `std::stringstream`. For exact floating-point round-trips, format with `max_digits10` precision, parse with `from_chars`, and verify that the returned pointer consumed the full token.
- **Line Breaks & Locales**: Emit `'\n'` instead of `std::endl` to avoid unnecessary buffer flushes, and explicitly specify or avoid locale-dependent operations during data processing.

---

## Standard Sequence Containers
- **`std::vector`**: Default choice for dynamic arrays with contiguous memory layout and hardware prefetch locality, often outperforming node-based containers even on iteration-heavy workloads.
- **`std::deque`**: Double-ended queue providing amortized constant-time insertions and deletions at both ends plus random access, at the cost of an extra pointer indirection per lookup.
- **`std::list` / `std::forward_list`**: Doubly (`std::list`, C++11 improvements) and singly (`std::forward_list`, C++11) linked lists for constant-time insertions/removals anywhere when pointer/iterator stability or node splicing is strictly required; profile first due to per-node heap allocations.

---

## Associative & Unordered Containers
- **Ordered (`std::map`, `std::set`)**: Balanced binary search trees maintaining sorted element order with logarithmic lookup times and per-node allocations (`std::map::try_emplace` / `insert_or_assign` in C++17, `contains` in C++20).
- **Unordered (`std::unordered_map`, `std::unordered_set`, C++11)**: Hash-based tables providing average constant-time complexity for insertions, deletions, and lookups; benchmark default hashers on hot paths.
- **Deterministic Output**: Never rely on the iteration order of unordered containers when output must be deterministic—sort with a strict total order across all relevant fields and test with shuffled inputs to catch hidden order dependencies:

```cpp
#include <algorithm>
#include <iostream>
#include <random>
#include <ranges>
#include <vector>

int main()
{
    std::vector<int> numbers{8, 3, 10, 1, 7, 4, 9, 2, 6, 5};

    std::random_device rd{};
    std::mt19937 generator{rd()};
    std::ranges::shuffle(numbers, generator);
    std::ranges::sort(numbers);

    const auto sorted_view{numbers | std::views::all};
    for (const auto& value : sorted_view)
    {
        std::cout << value << ' ';
    }
    std::cout << '\n';
}
