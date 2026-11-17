# Diagnostics et Sanitizers Reference

## Overview
Recommended diagnostic tools and sanitizers cross-referenced by operating system to detect memory leaks, race conditions, and undefined behavior at runtime.

## Linux
- **Memory & Leak Detection**: Use Valgrind (Memcheck) with GCC or Clang builds for deep leak analysis and uninitialized memory tracking.
- **Address Sanitizer**: Use ASan (`-fsanitize=address`) with either GCC or Clang for fast detection of out-of-bounds accesses and use-after-free bugs.
- **Thread Sanitizer**: Use TSan (`-fsanitize=thread`) with either GCC or Clang for detecting data races in multi-threaded code.

## Windows
- **Address Sanitizer**: Use MSVC ASan (`/fsanitize=address`) for detecting heap, stack, and global buffer overflows.

## macOS
- **Address & Undefined Behavior**: Use Apple Clang with ASan (`-fsanitize=address`) and UBSan (`-fsanitize=undefined`) for memory safety and undefined behavior checks.
- **Thread Sanitizer**: Use TSan (`-fsanitize=thread`) for concurrent execution safety and data race detection.
