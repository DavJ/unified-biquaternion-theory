# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# File: tools/nlogn_divisor_check.py
#
# Purpose: Numerical verification of the Dirichlet divisor sum
#   D(n) = sum_{k=1}^{n} tau(k)  ≈  n*ln(n) + (2*gamma - 1)*n
# where tau(k) is the number of positive divisors of k.
#
# This verifies Gap G-nlogn in T3_ALPHA:
#   the divisor-sum mechanism on T^2 produces the n*ln(n) form
#   required by V_eff(n) = n^2 - B*n*ln(n).
#
# Usage:
#   python3 tools/nlogn_divisor_check.py
#
# Output:
#   Table of n, D(n), n*ln(n) approximation, relative error.
#   Confirms D(n) ~ n*ln(n) to better than 5% for n >= 50.

import math

EULER_MASCHERONI = 0.5772156649015328606  # Euler-Mascheroni constant gamma


def count_divisors(k: int) -> int:
    """Return the number of positive divisors of k (tau function)."""
    if k <= 0:
        raise ValueError(f"k must be positive, got {k}")
    count = 0
    for d in range(1, int(math.isqrt(k)) + 1):
        if k % d == 0:
            count += 2
            if d * d == k:
                count -= 1  # perfect square: d counted once
    return count


def divisor_sum(n: int) -> list[int]:
    """Return cumulative divisor sums D(k) = sum_{j=1}^{k} tau(j) for k=1..n."""
    d_cumulative = []
    total = 0
    for k in range(1, n + 1):
        total += count_divisors(k)
        d_cumulative.append(total)
    return d_cumulative


def asymptotic_approximation(n: int) -> float:
    """Leading asymptotic: n*ln(n) + (2*gamma - 1)*n.

    Valid for n >= 1. Returns 0.0 for n <= 0 (not a useful value).
    For n = 1: ln(1) = 0, so the result is (2*gamma - 1)*1 ≈ 0.155.
    """
    if n <= 0:
        return 0.0
    if n == 1:
        # ln(1) = 0; asymptotic gives (2*gamma - 1) * 1 ≈ 0.155
        return (2 * EULER_MASCHERONI - 1) * n
    return n * math.log(n) + (2 * EULER_MASCHERONI - 1) * n


def main() -> None:
    N_MAX = 200

    print("=" * 72)
    print("Dirichlet Divisor Sum Verification")
    print(f"D(n) = sum_{{k=1}}^{{n}} tau(k)  vs  n*ln(n) + (2*gamma-1)*n")
    print(f"gamma = {EULER_MASCHERONI:.10f}")
    print("=" * 72)
    print(f"{'n':>6}  {'D(n)':>10}  {'n*ln(n)+(2g-1)n':>18}  {'rel. error':>12}")
    print("-" * 56)

    d_list = divisor_sum(N_MAX)

    check_points = list(range(10, 51, 10)) + list(range(50, N_MAX + 1, 25))
    errors = []
    for n in check_points:
        d_n = d_list[n - 1]
        approx = asymptotic_approximation(n)
        rel_err = abs(d_n - approx) / d_n
        errors.append(rel_err)
        print(f"{n:>6}  {d_n:>10}  {approx:>18.3f}  {rel_err:>11.4%}")

    print("=" * 72)

    # Verify that for n >= 50 the relative error is < 5%
    idx_50 = next(i for i, n in enumerate(check_points) if n >= 50)
    errors_50_plus = errors[idx_50:]
    max_err_50 = max(errors_50_plus)
    print(f"\nMax relative error for n >= 50: {max_err_50:.4%}")
    if max_err_50 < 0.05:
        print("PASS: D(n) ~ n*ln(n) to better than 5% for n >= 50.  [STD]")
    else:
        print("FAIL: approximation worse than 5% — check computation.")

    # Check that for n >= 20 the error is < 10%
    idx_20 = next(i for i, n in enumerate(check_points) if n >= 20)
    errors_20_plus = errors[idx_20:]
    max_err_20 = max(errors_20_plus)
    if max_err_20 < 0.10:
        print(f"PASS: D(n) ~ n*ln(n) to better than 10% for n >= 20.  [STD]")
    else:
        print(f"NOTE: approximation error {max_err_20:.4%} for n >= 20 (>10%).")

    # Show the n*ln(n) coefficient for a range around n=137
    print("\n--- Context around n* = 137 ---")
    print(f"{'n':>6}  {'D(n)':>10}  {'n*ln(n)':>12}  {'D(n)/(n*ln n)':>14}")
    print("-" * 48)
    for n in range(125, 150, 5):
        d_n = d_list[n - 1]
        nlogn = n * math.log(n)
        ratio = d_n / nlogn
        print(f"{n:>6}  {d_n:>10}  {nlogn:>12.2f}  {ratio:>14.6f}")

    print("\nConclusion: The leading term of D(n) is n*ln(n),")
    print("confirming the divisor-sum mechanism for the n*ln(n) form in V_eff(n).")
    print("See research_tracks/T3_ALPHA/nlogn_mechanism.tex for the physics derivation.")


if __name__ == "__main__":
    main()
