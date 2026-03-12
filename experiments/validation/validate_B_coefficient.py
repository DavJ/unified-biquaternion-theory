#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
No-circularity test for the B coefficient in the UBT alpha derivation.

PURPOSE
-------
The fine structure constant is derived from the effective potential
    V_eff(n) = A·n² − B·n·ln(n)
whose minimum over prime n gives n* ≈ 137.

The B coefficient must be computed FROM FIRST PRINCIPLES without knowing
the answer is 137. This script computes B and n* for multiple gauge-group
sizes N_eff, then reports n* as a genuine prediction.

The derivation is non-circular only if:
  (a) N_eff=12 (Standard Model) gives n* = 137
  (b) Other N_eff values give DIFFERENT primes (not always 137)

CURRENT STATUS (see STATUS_ALPHA.md §9)
-----------------------------------------
Two separate problems exist:

  Problem A: B_base = N_eff^{3/2} = 41.57 has NO geometric derivation.
             The standard one-loop β-function gives B₀ = 2π·N_eff/3 = 25.1.
             Factor N_eff^{1/2}/(2π/3) ≈ 1.66 is unexplained.

  Problem B: R ≈ 1.114 (B_base × R = B) has NO geometric derivation.

This script tests BOTH the standard formula (B₀) and the phenomenological
formula (B_base·R) for all N_eff values, to show which gives n*=137.

USAGE
-----
    python validation/validate_B_coefficient.py

OUTPUT
------
For each N_eff:
  - B₀ = 2π·N_eff/3         (rigorously derived, one-loop flat spacetime)
  - B_base = N_eff^{3/2}    (phenomenological; origin is OPEN PROBLEM A)
  - B = B_base × R           (requires R; origin is OPEN PROBLEM B)
  - n* from B₀, B_base, B   (nearest prime to true minimum)
  - Compare n*(N_eff=12) to 137
"""

import math
import sys

# ──────────────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────────────

# Kinetic coefficient (normalised)
A_COEFF = 1.0

# Correction factor R (OPEN PROBLEM B — no derivation)
R_FACTOR = 1.114

# Gauge group sizes to test:
#   4  — Electroweak SU(2)×U(1) only
#   8  — SU(3) colour only
#   12 — Standard Model SU(3)×SU(2)×U(1)
#   24 — Grand Unified SU(5)
N_EFF_CASES = [4, 8, 12, 24]

# Labels for each case
N_EFF_LABELS = {
    4:  "EW only (SU(2)×U(1))",
    8:  "colour only (SU(3))",
    12: "Standard Model (SU(3)×SU(2)×U(1))",
    24: "GUT SU(5)",
}

# Maximum prime to check
MAX_PRIME = 600


# ──────────────────────────────────────────────────────────────────────────────
# Prime sieve
# ──────────────────────────────────────────────────────────────────────────────

def sieve(n: int) -> list:
    """Return sorted list of primes up to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


PRIMES = sieve(MAX_PRIME)


# ──────────────────────────────────────────────────────────────────────────────
# Effective potential and minimum finder
# ──────────────────────────────────────────────────────────────────────────────

def v_eff(n: int, A: float, B: float) -> float:
    """Effective potential V_eff(n) = A·n² − B·n·ln(n)."""
    if n <= 1:
        return float('inf')
    return A * n * n - B * n * math.log(n)


def continuous_minimum(A: float, B: float) -> float:
    """Continuous minimum of V_eff: dV/dn = 0 → n* = exp(A/B − 1/(2B))."""
    if B <= 0:
        return float('inf')
    return math.exp(A / B - 1.0 / (2.0 * B))


def nearest_prime(x: float) -> int:
    """Return the prime nearest to x (by absolute value of difference)."""
    if not PRIMES:
        return -1
    return min(PRIMES, key=lambda p: abs(p - x))


def prime_minimum(A: float, B: float) -> int:
    """Return the prime n that minimises V_eff(n) among primes."""
    if B <= 0:
        return PRIMES[0]
    best_n = PRIMES[0]
    best_v = v_eff(PRIMES[0], A, B)
    for p in PRIMES:
        v = v_eff(p, A, B)
        if v < best_v:
            best_v = v
            best_n = p
    return best_n


# ──────────────────────────────────────────────────────────────────────────────
# B coefficient formulas
# ──────────────────────────────────────────────────────────────────────────────

def b_one_loop(N_eff: int) -> float:
    """Standard one-loop B coefficient (flat spacetime, fully derived).

    From the one-loop photon vacuum polarisation with N_eff gauge bosons:
        B₀ = 2π·N_eff/3
    This is the rigorously derived result.
    """
    return 2.0 * math.pi * N_eff / 3.0


def b_base(N_eff: int) -> float:
    """Phenomenological B_base = N_eff^{3/2}.

    This formula has no geometric derivation (OPEN PROBLEM A).
    It is used in the UBT alpha derivation but its origin is unexplained.
    """
    return N_eff ** 1.5


def b_full(N_eff: int) -> float:
    """Full B = B_base × R (requires OPEN PROBLEM A + OPEN PROBLEM B to resolve)."""
    return b_base(N_eff) * R_FACTOR


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def main() -> int:
    print("=" * 72)
    print("UBT B-Coefficient No-Circularity Test")
    print("=" * 72)
    print()
    print("PURPOSE: Compute n* = arg min_{prime p} V_eff(p) for each N_eff,")
    print("         WITHOUT knowing the target is 137.")
    print()
    print("KEY POINT: B must be derived from first principles.")
    print("  Problem A: B_base = N_eff^{3/2} has no derivation (OPEN PROBLEM)")
    print("  Problem B: R = 1.114 has no derivation (OPEN PROBLEM)")
    print()
    print(f"  A = {A_COEFF} (normalised)")
    print(f"  R = {R_FACTOR} (OPEN PROBLEM B — fitted, not derived)")
    print()

    target_n_star = 137
    sm_n_star_b0 = None
    sm_n_star_bbase = None
    sm_n_star_bfull = None

    for N_eff in N_EFF_CASES:
        label = N_EFF_LABELS.get(N_eff, f"N_eff={N_eff}")
        B0 = b_one_loop(N_eff)
        Bbase = b_base(N_eff)
        Bfull = b_full(N_eff)

        n_cont_b0 = continuous_minimum(A_COEFF, B0)
        n_cont_bbase = continuous_minimum(A_COEFF, Bbase)
        n_cont_bfull = continuous_minimum(A_COEFF, Bfull)

        n_star_b0 = prime_minimum(A_COEFF, B0)
        n_star_bbase = prime_minimum(A_COEFF, Bbase)
        n_star_bfull = prime_minimum(A_COEFF, Bfull)

        if N_eff == 12:
            sm_n_star_b0 = n_star_b0
            sm_n_star_bbase = n_star_bbase
            sm_n_star_bfull = n_star_bfull

        print(f"N_eff = {N_eff:3d}  [{label}]")
        print(f"  B₀ (one-loop, DERIVED)    = {B0:.4f}  → n*_continuous = {n_cont_b0:.1f}"
              f"  → n*_prime = {n_star_b0}")
        print(f"  B_base (N^3/2, PHENOM.)   = {Bbase:.4f}  → n*_continuous = {n_cont_bbase:.1f}"
              f"  → n*_prime = {n_star_bbase}")
        print(f"  B_full (B_base·R, FITTED) = {Bfull:.4f}  → n*_continuous = {n_cont_bfull:.1f}"
              f"  → n*_prime = {n_star_bfull}")
        print()

    print("=" * 72)
    print("CIRCULARITY ANALYSIS")
    print("=" * 72)
    print()

    # Test 1: Does the rigorously derived B₀ give n*=137 for N_eff=12?
    print(f"Test 1 — Rigorously derived B₀ (one-loop, flat spacetime):")
    print(f"  SM (N_eff=12):  n* = {sm_n_star_b0}")
    if sm_n_star_b0 == target_n_star:
        print(f"  PASS: B₀ alone gives n* = {target_n_star}.")
        print(f"  The B_base = N_eff^{{3/2}} formula is NOT needed.")
        result_b0 = True
    else:
        print(f"  FAIL: B₀ = {b_one_loop(12):.4f} gives n* = {sm_n_star_b0}, not {target_n_star}.")
        print(f"  CONCLUSION: The rigorously derived one-loop B coefficient does NOT")
        print(f"  reproduce α⁻¹ = 137. B_base = N_eff^{{3/2}} (OPEN PROBLEM A) is")
        print(f"  essential to the derivation.")
        result_b0 = False

    print()

    # Test 2: Does B_base (no R factor) give n*=137 for N_eff=12?
    print(f"Test 2 — Phenomenological B_base = N_eff^{{3/2}} (no R factor):")
    print(f"  SM (N_eff=12):  n* = {sm_n_star_bbase}")
    if sm_n_star_bbase == target_n_star:
        print(f"  PASS: B_base alone gives n* = {target_n_star}. R factor not needed.")
        result_bbase = True
    else:
        print(f"  FAIL: B_base = {b_base(12):.4f} gives n* = {sm_n_star_bbase}, not {target_n_star}.")
        print(f"  CONCLUSION: R ≈ {R_FACTOR} (OPEN PROBLEM B) is also essential.")
        result_bbase = False

    print()

    # Test 3: Does B_full = B_base·R give n*=137 for N_eff=12?
    print(f"Test 3 — Fitted B_full = B_base × R (both open problems used):")
    print(f"  SM (N_eff=12):  n* = {sm_n_star_bfull}")
    if sm_n_star_bfull == target_n_star:
        print(f"  PASS: B_full = {b_full(12):.4f} gives n* = {target_n_star} for N_eff=12.")
        result_bfull = True
    else:
        print(f"  PARTIAL FAIL: B_full = {b_full(12):.4f} gives n* = {sm_n_star_bfull}.")
        result_bfull = False

    print()

    # Non-circularity check: different N_eff should give different n*
    print(f"Non-circularity check (B_full):")
    n_stars = {N: prime_minimum(A_COEFF, b_full(N)) for N in N_EFF_CASES}
    all_different = len(set(n_stars.values())) == len(N_EFF_CASES)
    print(f"  n* values: {n_stars}")
    if all_different:
        print(f"  PASS: All N_eff values give different n* — derivation is non-circular.")
        result_noncircular = True
    else:
        print(f"  WARNING: Some N_eff values give the same n* — check for circularity.")
        result_noncircular = False

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    if result_b0:
        print("STATUS: PROVEN — one-loop B₀ suffices; no open problems required.")
        return 0
    elif result_bfull and result_noncircular:
        print("STATUS: SEMI-EMPIRICAL — B_full gives n*=137 and is non-circular,")
        print("        but requires B_base (OPEN PROBLEM A) and R (OPEN PROBLEM B).")
        print("        The derivation is not yet fully rigorous.")
        return 1
    else:
        print("STATUS: OPEN PROBLEM — B coefficient derivation is incomplete.")
        print("        The B_base = N_eff^{3/2} and R ≈ 1.114 formulas are both")
        print("        phenomenological. See STATUS_ALPHA.md §9 for derivation strategy.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
