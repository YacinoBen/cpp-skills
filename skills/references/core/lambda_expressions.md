# Modern C++ Lambda Expressions

## Overview

Guidelines and patterns for writing concise, type-safe, and zero-overhead anonymous function objects (closures) in modern C++23, covering capture semantics, generic template lambdas, C++23 deducing `this` recursion, and performance considerations.

---

## 1. Basic Syntax & Anatomy

```cpp
[capture_clause](parameters) specifiers -> return_type {
    // Function body
};
```

- **`[capture_clause]`**: Defines which variables from the enclosing scope are accessible inside the lambda and how they are captured (by value or by reference).
- **`(parameters)`**: Function parameter list (optional in C++23 if empty and no specifiers like `mutable` or `noexcept` are used).
- **`specifiers`**: Optional qualifiers such as `mutable`, `constexpr`, `consteval`, `noexcept`, or `static` (C++23).
- **`-> return_type`**: Trailing return type (optional; deduced automatically in most cases).

---

## 2. Capture Modes & Lifetime Safety

| Capture Syntax | Behavior | Best Practice |
| :--- | :--- | :--- |
| `[]` | Stateless lambda (captures nothing). Convertible to a raw function pointer. | **Preferred** whenever no external state is needed. |
| `[x, &y]` | Captures `x` by value (copy) and `y` by reference. | **Recommended** for explicit, auditable dependencies. |
| `[=]` | Default capture all used variables by value. | **Avoid** in non-trivial scopes (can cause unintended copies or implicit `this` capture). |
| `[&]` | Default capture all used variables by reference. | **Use with caution**: only safe when the lambda does not outlive the current scope (e.g., synchronous `std::ranges` algorithms). |
| `[this]` / `[*this]` | Captures the current object pointer (`[this]`) or a full copy of the object (`[*this]`). | Prefer `[*this]` in asynchronous callbacks to prevent dangling `this` pointers. |
| `[ptr = std::move(p)]` | **Init-Capture (C++14)**: Moves or initializes a member variable directly inside the closure. | **Ideal** for move-only types (`std::unique_ptr`, `std::jthread`). |

### Example: Move-Only Init-Capture

```cpp
#include <memory>

auto createWorker() {
    auto resource = std::make_unique<int>(42);
    return [ptr = std::move(resource)]() noexcept -> int {
        return *ptr;
    };
}
```

---

## 3. Modern C++20 / C++23 Lambda Features

### A. Template / Generic Lambdas (C++20)
Use explicit template parameter lists on lambdas to enforce type constraints with `concepts` and avoid unintended type conversions:

```cpp
#include <concepts>
#include <iostream>

auto printIntegral = []<std::integral T>(T value) {
    std::cout << value << '\n';
};
```

### B. Recursive Lambdas via Deducing `this` (C++23)
C++23 allows an explicit object parameter (`this auto&& self`) inside the parameter list, enabling clean, zero-overhead recursion without `std::function`:

```cpp
auto factorial = [](this auto&& self, int n) noexcept -> int {
    return (n <= 1) ? 1 : n * self(n - 1);
};

static_assert(factorial(5) == 120);
```

### C. `static` Operator() Lambdas (C++23)
Stateless lambdas can be marked `static` in C++23 to eliminate the unused implicit `this` pointer in the generated call operator, improving ABI and register efficiency:

```cpp
auto add = [](int a, int b) static noexcept -> int {
    return a + b;
};
```

### D. `constexpr` & `consteval` Lambdas
Lambdas are implicitly `constexpr` whenever their body satisfies `constexpr` requirements, and can be explicitly marked `consteval` (C++20) to guarantee compile-time evaluation:

```cpp
constexpr auto square = [](int x) noexcept { return x * x; };
static_assert(square(6) == 36);
```

---

## 4. Performance & Best Practices

- **Prefer `auto` or Template Parameters Over `std::function`**:
  - Storing a lambda in `auto` or passing it to a constrained template preserves its unique closure type, enabling full compiler **inlining** and zero heap allocation.
  - `std::function` introduces type erasure, indirect virtual-like calls, and potential dynamic heap allocation if the closure exceeds Small Buffer Optimization (SBO).

```cpp
// Fast: Zero overhead, fully inlinable
template <typename Func>
void executeFast(Func&& fn) {
    fn();
}

// Slower: Type erasure & potential heap allocation
void executeErased(const std::function<void()>& fn) {
    fn();
}
```

- **Avoid Dangling References in Asynchronous Scopes**: Never pass a lambda capturing local variables by reference (`[&]`) to a background thread, detached task, or stored callback.
- **Use `mutable` Sparingly**: By default, a lambda's `operator()` is `const`, meaning value-captured variables cannot be modified. Add `mutable` only when maintaining internal state across invocations is explicitly intended.
- **Mark `noexcept` When Applicable**: Annotating non-throwing lambdas with `noexcept` allows standard containers and algorithms to select optimal move/execution paths.