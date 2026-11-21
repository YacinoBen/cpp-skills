# Algorithms, Ranges & Execution Policies Reference

## Overview

Guidelines for writing declarative, expressive, and high-performance data processing pipelines in modern C++23 using `<algorithm>`, `<ranges>`, lazy views (`std::views`), and parallel execution policies (`<execution>`).

## Standard Algorithms & Range-Based Equivalents

* **Prefer `std::ranges` Algorithms**: Favor constrained range algorithms (`std::ranges::sort`, `std::ranges::find_if`, `std::ranges::transform`) over legacy iterator-pair algorithms (`begin()`, `end()`) to prevent mismatched iterator bugs and support projections directly.
* **Projections**: Use projection callables in `std::ranges` algorithms to sort or search complex structs by a specific member without writing verbose custom comparators.
* **Numeric & Reduction Algorithms**: Prefer `std::reduce`, `std::transform_reduce`, and `std::inclusive_scan` over sequential `std::accumulate` when associative/commutative operations can benefit from parallelization or SIMD vectorization.
* **C++23 Range Algorithms**: Leverage modern additions such as `std::ranges::contains`, `std::ranges::fold_left`, `std::ranges::starts_with`, and `std::ranges::to` (for materializing views back into containers).

## Sorting & Partitioning Strategies

Choose the right sorting algorithm based on complexity, stability, and partial ordering needs:

* **`std::ranges::sort`**: Default $O(N \log N)$ unstable sort (typically Introsort) for general-purpose fast ordering.
* **`std::ranges::stable_sort`**: Preserves the relative order of equivalent elements when secondary ordering matters.
* **`std::ranges::partial_sort` & `std::ranges::nth_element`**: Use when only the top-$K$ elements or the median are required ($O(N \log K)$ and $O(N)$ average respectively), avoiding the cost of a full sort.
* **`std::ranges::partition`**: Group elements satisfying a predicate in $O(N)$ linear time without full sorting overhead.

## Lazy Evaluation with `std::views` (`<ranges>`)

* **Zero-Allocation Pipelines**: Chain view adaptors using the pipe operator (`|`) to compose transformations lazily without allocating intermediate temporary containers.
* **Common View Adaptors**:
  * Filtering & Transforming: `std::views::filter`, `std::views::transform`, `std::views::take`, `std::views::drop`.
  * C++23 Combinators: `std::views::zip`, `std::views::enumerate`, `std::views::chunk`, `std::views::slide`, `std::views::stride`, and `std::views::join_with`.
* **Materialization (`std::ranges::to`)**: Convert lazy view pipelines into concrete containers (`std::vector`, `std::flat_map`) cleanly in C++23 via `| std::ranges::to<std::vector>()`.
* **Lifetime Awareness**: Remember that views are lightweight, non-owning descriptors; never return a view referencing a local temporary container that goes out of scope.

## Parallel Execution Policies (`<execution>`)

Accelerate standard algorithms across multiple CPU cores and SIMD lanes by passing an execution policy:

* **`std::execution::seq`**: Strictly sequential execution on the calling thread.
* **`std::execution::par`**: Parallel execution across multiple worker threads (requires thread-safe, data-race-free element access).
* **`std::execution::par_unseq`**: Parallel and vectorized (SIMD) execution; operations must not acquire locks or rely on thread-local state to avoid deadlocks.
* **`std::execution::unseq`**: Single-threaded SIMD vectorized execution (C++20).

## Practical Examples

### 1. Declarative Pipeline with `std::views` & `std::ranges::to` (C++23)

```cpp
#include <algorithm>
#include <ranges>
#include <string>
#include <vector>

struct User {
    std::string name;
    int score{0};
    bool is_active{false};
};

[[nodiscard]] std::vector<std::string> getTopActiveUserNames(const std::vector<User>& users) {
    auto pipeline = users
        | std::views::filter([](const User& user) { return user.is_active && user.score >= 50; })
        | std::views::transform(&User::name)
        | std::views::take(5);

    return pipeline | std::ranges::to<std::vector>();
}
```

### 2. Sorting with Projections & Partial Sort

```cpp
#include <algorithm>
#include <vector>

void sortUsersByScoreDescending(std::vector<User>& users) {
    // Sort using a projection on User::score without a custom lambda comparator
    std::ranges::sort(users, std::ranges::greater{}, &User::score);
}

void getTopThreeUsers(std::vector<User>& users) {
    if (users.size() > 3) {
        std::ranges::partial_sort(users, users.begin() + 3, std::ranges::greater{}, &User::score);
    }
}
```

### 3. Parallel Sort & Transform-Reduce (`std::execution`)

```cpp
#include <algorithm>
#include <execution>
#include <numeric>
#include <vector>

double computeParallelNormSquared(std::vector<double>& values) {
    // Parallel sorting across CPU cores
    std::sort(std::execution::par, values.begin(), values.end());

    // Parallel + SIMD vectorized reduction
    return std::transform_reduce(
        std::execution::par_unseq,
        values.cbegin(),
        values.cend(),
        0.0,
        std::plus<>{},
        [](double val) noexcept { return val * val; }
    );
}
```