# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# File: tools/self_consistency_scan.py
#
# Purpose: Scan primes p in [50, 500] for the self-consistent fixed-point
#   condition n*(B_modular(p)) = p, where B_modular(p) = (p+1)/3.
#
# Background (from reports/prime_137_structural_audit.md §1.2):
#   The modular volume X₀(p)/π = (p+1)/3 gives B(p) = (p+1)/3.
#   The stationarity condition of V_eff gives n*(B) as the implicit solution of
#       2n = B(ln n + 1)   =>   n*(B) = B(ln n* + 1)/2   [transcendental]
#   Self-consistency: n*((p+1)/3) = p
#   Exact algebraic form: (5p-1)/(p+1) = ln p
#
# Refined formula (§3.3, including elliptic correction):
#   B_refined(p) = (p+1)/3 + nu2(p)/4
#   where nu2(p) = 1 + kronecker(-4, p) counts elliptic points of order 2.
#
# Classification of each step follows [L0]/[L1]/[MC]/[OPEN] protocol.

import math


# ── helpers ─────────────────────────────────────────────────────────────────

def is_prime(n: int) -> bool:
    """Trial-division primality test."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_in_range(lo: int, hi: int):
    """Return list of primes p with lo <= p <= hi."""
    return [p for p in range(lo, hi + 1) if is_prime(p)]


def kronecker_symbol(a: int, n: int) -> int:
    """
    Compute the Kronecker symbol (a|n) for n odd prime.
    Uses Euler's criterion: a^((p-1)/2) mod p == 1 => +1, else -1 (for a not div by p).
    """
    if n == 2:
        if a % 2 == 0:
            return 0
        return 1 if a % 8 in (1, 7) else -1
    a = a % n
    if a == 0:
        return 0
    # Euler criterion for odd prime n
    val = pow(a, (n - 1) // 2, n)
    return 1 if val == 1 else -1


def nu2(p: int) -> int:
    """
    Number of elliptic points of order 2 of Gamma_0(p) for prime p.
    Formula: nu2 = 1 + kronecker(-4, p)
    """
    return 1 + kronecker_symbol(-4, p)


def B_modular(p: int) -> float:
    """B from normalised modular volume: B = (p+1)/3.  [MC] candidate."""
    return (p + 1) / 3.0


def B_refined(p: int) -> float:
    """Refined B including elliptic-point correction: B = (p+1)/3 + nu2(p)/4.  [MC]."""
    return (p + 1) / 3.0 + nu2(p) / 4.0


def n_star(B: float, tol: float = 1e-12, max_iter: int = 100_000) -> float:
    """
    Iterative solution of the transcendental fixed-point equation
        n = B * (ln(n) + 1) / 2
    which is the stationarity condition dV_eff/dn = 0 for
        V_eff(n) = n² - B·n·ln n.
    Uses dampened fixed-point iteration starting from n = max(B, 2).
    """
    n = max(B, 2.0)
    for _ in range(max_iter):
        n_new = B * (math.log(n) + 1) / 2.0
        if abs(n_new - n) < tol:
            return n_new
        n = 0.5 * n + 0.5 * n_new   # dampened update
    return n


def self_consistency_gap(p: int) -> float:
    """Gap delta(p) = n*(B_modular(p)) - p."""
    return n_star(B_modular(p)) - p


def self_consistency_gap_refined(p: int) -> float:
    """Gap delta_refined(p) = n*(B_refined(p)) - p."""
    return n_star(B_refined(p)) - p


# ── exact algebraic condition ────────────────────────────────────────────────

def algebraic_gap(p: int) -> float:
    """
    From the self-consistency equation n*(B_modular(p)) = p:
        p = (p+1)/3 * (ln p + 1) / 2
    Rearranges to:
        (5p-1)/(p+1) = ln p
    Gap: lhs - rhs.
    """
    lhs = (5 * p - 1) / (p + 1)
    rhs = math.log(p)
    return lhs - rhs


def algebraic_gap_refined(p: int) -> float:
    """
    Self-consistency with refined B = (p+1)/3 + nu2(p)/4:
        p = B_refined(p) * (ln p + 1) / 2
    Gap: B_refined(p)*(ln p + 1)/2 - p.
    """
    return B_refined(p) * (math.log(p) + 1) / 2.0 - p


# ── main scan ────────────────────────────────────────────────────────────────

def run_scan():
    primes = primes_in_range(50, 500)

    print("=" * 90)
    print("SELF-CONSISTENCY SCAN: n*(B_modular(p)) vs p, for primes p in [50, 500]")
    print("B_modular(p) = (p+1)/3  [MC candidate from modular volume of X_0(p)]")
    print("=" * 90)
    print(f"{'p':>5}  {'B_mod':>8}  {'n*(B_mod)':>11}  {'delta':>10}  {'|delta|':>9}  {'prime?':>6}")
    print("-" * 90)

    results = []
    for p in primes:
        B = B_modular(p)
        ns = n_star(B)
        delta = ns - p
        results.append((abs(delta), p, B, ns, delta))

    results.sort()   # sort by |delta|
    for abs_d, p, B, ns, delta in results:
        marker = " <--" if abs_d < 5 else ""
        print(f"{p:>5}  {B:>8.4f}  {ns:>11.4f}  {delta:>10.4f}  {abs_d:>9.4f}{marker}")

    print()
    print("=" * 90)
    print("REFINED SCAN: B_refined(p) = (p+1)/3 + nu2(p)/4")
    print("=" * 90)
    print(f"{'p':>5}  {'nu2':>4}  {'B_ref':>8}  {'n*(B_ref)':>11}  {'delta_r':>10}  {'|dr|':>9}")
    print("-" * 90)

    results_r = []
    for p in primes:
        n2 = nu2(p)
        B = B_refined(p)
        ns = n_star(B)
        delta = ns - p
        results_r.append((abs(delta), p, n2, B, ns, delta))

    results_r.sort()
    for abs_d, p, n2, B, ns, delta in results_r:
        marker = " <--" if abs_d < 5 else ""
        print(f"{p:>5}  {n2:>4}  {B:>8.4f}  {ns:>11.4f}  {delta:>10.4f}  {abs_d:>9.4f}{marker}")

    print()
    print("=" * 90)
    print("EXACT ALGEBRAIC CONDITION: (5p-1)/(p+1) vs ln(p)")
    print("Self-consistency equation: (5p-1)/(p+1) = ln p")
    print("=" * 90)
    print(f"{'p':>5}  {'lhs':>9}  {'rhs=lnp':>9}  {'gap_alg':>10}  {'|gap|':>9}")
    print("-" * 90)

    alg_results = []
    for p in primes:
        lhs = (5 * p - 1) / (p + 1)
        rhs = math.log(p)
        gap = lhs - rhs
        alg_results.append((abs(gap), p, lhs, rhs, gap))

    alg_results.sort()
    for abs_g, p, lhs, rhs, gap in alg_results[:20]:
        marker = " <-- top-20" if abs_g < 0.5 else ""
        print(f"{p:>5}  {lhs:>9.6f}  {rhs:>9.6f}  {gap:>10.6f}  {abs_g:>9.6f}{marker}")

    print()
    print("=" * 90)
    print("EXACT ALGEBRAIC CONDITION (REFINED): B_refined*(ln p+1)/2 = p")
    print("=" * 90)
    print(f"{'p':>5}  {'nu2':>4}  {'B_ref':>8}  {'B*(lnp+1)/2':>13}  {'gap_r':>10}  {'|gr|':>9}")
    print("-" * 90)

    alg_r_results = []
    for p in primes:
        n2 = nu2(p)
        B = B_refined(p)
        val = B * (math.log(p) + 1) / 2.0
        gap = val - p
        alg_r_results.append((abs(gap), p, n2, B, val, gap))

    alg_r_results.sort()
    for abs_g, p, n2, B, val, gap in alg_r_results[:20]:
        marker = " <-- top-20" if True else ""
        print(f"{p:>5}  {n2:>4}  {B:>8.4f}  {val:>13.4f}  {gap:>10.4f}  {abs_g:>9.4f}{marker}")

    print()
    # --- special focus on p=137
    print("=" * 90)
    print("FOCUS ON p = 137")
    print("=" * 90)
    p = 137
    n2 = nu2(p)
    B1 = B_modular(p)
    B2 = B_refined(p)
    ns1 = n_star(B1)
    ns2 = n_star(B2)
    d1 = ns1 - p
    d2 = ns2 - p
    lhs = (5 * p - 1) / (p + 1)
    rhs = math.log(p)
    alg_gap = lhs - rhs
    alg_r_gap = algebraic_gap_refined(p)

    print(f"  nu2(137)         = {n2}")
    print(f"  B_modular(137)   = (137+1)/3 = {B1:.6f}")
    print(f"  B_refined(137)   = (137+1)/3 + {n2}/4 = {B2:.6f}")
    print(f"  B_phenom (target)= 46.298  (from dV/dn=0 at n=137)")
    print(f"  n*(B_modular)    = {ns1:.6f}   delta = {d1:+.6f}  ({100*d1/p:+.3f}%)")
    print(f"  n*(B_refined)    = {ns2:.6f}   delta = {d2:+.6f}  ({100*d2/p:+.3f}%)")
    print(f"  Algebraic LHS    = (5*137-1)/(137+1) = {lhs:.6f}")
    print(f"  Algebraic RHS    = ln(137)            = {rhs:.6f}")
    print(f"  Algebraic gap    = LHS - RHS          = {alg_gap:+.6f}  ({100*alg_gap/rhs:+.3f}% of ln p)")
    print(f"  Refined alg gap  = B_ref*(lnp+1)/2-p  = {alg_r_gap:+.6f}")
    print()
    print("  Is p=137 a fixed point?")
    print(f"    Basic  (|delta|<1.37 i.e. 1%): {'YES' if abs(d1) < 1.37 else 'NO'} (|delta|={abs(d1):.3f})")
    print(f"    Refined(|delta|<1.37 i.e. 1%): {'YES' if abs(d2) < 1.37 else 'NO'} (|delta|={abs(d2):.3f})")


if __name__ == "__main__":
    run_scan()
