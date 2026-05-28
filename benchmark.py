"""
Benchmark: 4 strategies for building the result string in big number addition.

  1. PREPEND      result = digit + result                  O(n²)
  2. APPEND+REV   list.append → "".join(reversed(...))     O(n)
  3. APPEND+SLICE list.append → list.reverse() → join      O(n)
  4. PRE-ALLOC    pre-allocate list, fill right-to-left    O(n)  ★
"""

import time
import sys


# ── 1. PREPEND ───────────────────────────────────────────────────────────────

def sum_prepend(stn1: str, stn2: str) -> str:
    result = ""
    carry = 0
    i, j = len(stn1) - 1, len(stn2) - 1
    while i >= 0 or j >= 0 or carry:
        d1 = int(stn1[i]) if i >= 0 else 0
        d2 = int(stn2[j]) if j >= 0 else 0
        total = d1 + d2 + carry
        carry = total // 10
        result = str(total % 10) + result
        i -= 1; j -= 1
    return result


# ── 2. APPEND + JOIN(REVERSED) ──────────────────────────────────────────────

def sum_append_reversed(stn1: str, stn2: str) -> str:
    digits = []
    carry = 0
    i, j = len(stn1) - 1, len(stn2) - 1
    while i >= 0 or j >= 0 or carry:
        d1 = int(stn1[i]) if i >= 0 else 0
        d2 = int(stn2[j]) if j >= 0 else 0
        total = d1 + d2 + carry
        carry = total // 10
        digits.append(str(total % 10))
        i -= 1; j -= 1
    return "".join(reversed(digits))


# ── 3. APPEND + IN-PLACE REVERSE ────────────────────────────────────────────

def sum_append_slice(stn1: str, stn2: str) -> str:
    digits = []
    carry = 0
    i, j = len(stn1) - 1, len(stn2) - 1
    while i >= 0 or j >= 0 or carry:
        d1 = int(stn1[i]) if i >= 0 else 0
        d2 = int(stn2[j]) if j >= 0 else 0
        total = d1 + d2 + carry
        carry = total // 10
        digits.append(str(total % 10))
        i -= 1; j -= 1
    digits.reverse()
    return "".join(digits)


# ── 4. PRE-ALLOCATE ─────────────────────────────────────────────────────────

def sum_prealloc(stn1: str, stn2: str) -> str:
    len1, len2 = len(stn1), len(stn2)
    max_len = max(len1, len2) + 1
    result = ['0'] * max_len

    carry = 0
    k = max_len - 1
    i, j = len1 - 1, len2 - 1
    while i >= 0 or j >= 0 or carry:
        d1 = int(stn1[i]) if i >= 0 else 0
        d2 = int(stn2[j]) if j >= 0 else 0
        total = d1 + d2 + carry
        carry = total // 10
        result[k] = str(total % 10)
        k -= 1; i -= 1; j -= 1
    return "".join(result) if result[0] != '0' else "".join(result[1:])


# ── Benchmark ───────────────────────────────────────────────────────────────

def bench(func, stn1, stn2, iterations):
    start = time.perf_counter()
    for _ in range(iterations):
        func(stn1, stn2)
    return time.perf_counter() - start


def main():
    print("=" * 90)
    print("  BENCHMARK:  Prepend  vs  Append+Rev  vs  Append+Slice  vs  Pre-Alloc ★")
    print("  Test: add N-digit number (all 9s) + '1'")
    print("=" * 90)
    print()

    # Correctness
    a, b = "9999999", "1"
    results = [f(a, b) for f in (sum_prepend, sum_append_reversed, sum_append_slice, sum_prealloc)]
    assert all(r == "10000000" for r in results), f"Mismatch! {results}"
    a2, b2 = "0", "0"
    results2 = [f(a2, b2) for f in (sum_prepend, sum_append_reversed, sum_append_slice, sum_prealloc)]
    assert all(r == "0" for r in results2), f"Mismatch on 0+0! {results2}"
    print("  ✅ Correctness check passed\n")

    strategies = [
        ("Prepend",      sum_prepend),
        ("Append+Rev",   sum_append_reversed),
        ("Append+Slice", sum_append_slice),
        ("Pre-Alloc ★",  sum_prealloc),
    ]

    test_cases = [
        (      1_000,  1_000),
        (     10_000,    100),
        (    100_000,     10),
        (  1_000_000,      1),
    ]

    # Header
    cols = "  {:>12} | {:>6}".format("N digits", "Iters")
    for name, _ in strategies:
        cols += " | {:>14}".format(name)
    print(cols)
    print("-" * len(cols))

    for n_digits, iterations in test_cases:
        stn1 = "9" * n_digits
        stn2 = "1"

        row = "  {:>12,} | {:>6,}".format(n_digits, iterations)
        for name, func in strategies:
            t = bench(func, stn1, stn2, iterations)
            row += " | {:>13.4f}s".format(t)
        print(row)
        sys.stdout.flush()

    print()
    print("=" * 90)
    print("  PHÂN TÍCH")
    print("=" * 90)
    print("""
  ┌─────────────────┬────────────┬──────────────────────────────────────────┐
  │    Phương pháp   │ Độ phức tạp │          Ghi chú                       │
  ├─────────────────┼────────────┼──────────────────────────────────────────┤
  │ Prepend          │   O(n²)    │ Chậm nhất, copy chuỗi liên tục        │
  ├─────────────────┼────────────┼──────────────────────────────────────────┤
  │ Append+Rev       │   O(n)     │ Nhanh                                  │
  ├─────────────────┼────────────┼──────────────────────────────────────────┤
  │ Append+Slice     │   O(n)     │ Nhanh                                  │
  ├─────────────────┼────────────┼──────────────────────────────────────────┤
  │ Pre-Alloc ★      │   O(n)     │ Nhanh, ghi thẳng vào đúng vị trí      │
  └─────────────────┴────────────┴──────────────────────────────────────────┘
""")


if __name__ == "__main__":
    main()
