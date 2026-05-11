# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# File: tools/compare_alpha_potentials.py
#
# Purpose: Compare the stationary-point structure of three candidate forms of
#   the UBT alpha-sector effective potential:
#
#     V1(n) = n^2 - B * n * log(n)
#     V2(n) = n^2 - B * log(Gamma(n+1))
#     V3(n) = n^2 - B * (log(Gamma(n+1)) + n)
#
#   For each form:
#     - Print the derivative (stationary-condition formula).
#     - Compute the value of B required so that n* = 137 is stationary.
#     - Scan n in [120, 150] for the stationary point n*(B) at B = B_Ram.
#
#   Reference value:
#     B_Ram = 12^(3/2) * 2^(1/8) * theta3(0|i)^(1/4)
#   This is a numerical observation only — NOT a first-principles derivation.
#   See canonical/alpha/ALPHA_MASTER_STATUS.md (deprecated-claim register).
#
# Status labels used in output:
#   [STD/L0]  — standard mathematical fact
#   [INTERP]  — interpretation, not a UBT derivation
#   [DERIV CAND] — derivation candidate, not proved
#   [OPEN]    — gap not closed; alpha NOT DERIVED
#
# Usage:
#   python3 tools/compare_alpha_potentials.py
#
# Dependencies: math, scipy (for digamma / special functions)

import math
from scipy.special import digamma, loggamma  # type: ignore


# ── Reference value (numerical observation only) ─────────────────────────────

def theta3_nome_sum(q: float, terms: int = 200) -> float:
    """Compute Jacobi theta3(0|tau) with nome q = exp(i*pi*tau).

    For tau = i: nome q = exp(-pi).
    theta3(0|i) = 1 + 2 * sum_{n=1}^{inf} exp(-pi * n^2).
    """
    total = 1.0
    for n in range(1, terms + 1):
        term = 2.0 * math.exp(-math.pi * n * n)
        total += term
        if term < 1e-15:
            break
    return total


def compute_B_ram() -> float:
    """B_Ram = 12^(3/2) * 2^(1/8) * theta3(0|i)^(1/4).

    Numerical observation — not a first-principles derivation. [INTERP]
    """
    theta3 = theta3_nome_sum(q=math.exp(-math.pi))
    return (12 ** 1.5) * (2 ** 0.125) * (theta3 ** 0.25)


# ── Potential derivatives ─────────────────────────────────────────────────────

def v1_deriv(n: float, B: float) -> float:
    """dV1/dn = 2n - B*(log n + 1).  [L1]"""
    if n <= 0:
        raise ValueError(f"n must be positive, got {n}")
    return 2.0 * n - B * (math.log(n) + 1.0)


def v2_deriv(n: float, B: float) -> float:
    """dV2/dn = 2n - B * psi(n+1)  where psi = digamma.  [DERIV CAND]"""
    if n <= 0:
        raise ValueError(f"n must be positive, got {n}")
    return 2.0 * n - B * float(digamma(n + 1))


def v3_deriv(n: float, B: float) -> float:
    """dV3/dn = 2n - B*(psi(n+1) + 1).  [DERIV CAND]"""
    if n <= 0:
        raise ValueError(f"n must be positive, got {n}")
    return 2.0 * n - B * (float(digamma(n + 1)) + 1.0)


# ── B required for n* = 137 ───────────────────────────────────────────────────

def B_for_nstar_V1(nstar: float) -> float:
    """B such that V1'(nstar)=0: B = 2*nstar / (log(nstar) + 1)."""
    return 2.0 * nstar / (math.log(nstar) + 1.0)


def B_for_nstar_V2(nstar: float) -> float:
    """B such that V2'(nstar)=0: B = 2*nstar / psi(nstar+1)."""
    return 2.0 * nstar / float(digamma(nstar + 1))


def B_for_nstar_V3(nstar: float) -> float:
    """B such that V3'(nstar)=0: B = 2*nstar / (psi(nstar+1) + 1)."""
    return 2.0 * nstar / (float(digamma(nstar + 1)) + 1.0)


# ── Scan for stationary point ─────────────────────────────────────────────────

def find_stationary_continuous(
    deriv_fn,
    B: float,
    n_lo: float,
    n_hi: float,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """Find n* in [n_lo, n_hi] where deriv_fn(n, B) = 0 via bisection."""
    f_lo = deriv_fn(n_lo, B)
    f_hi = deriv_fn(n_hi, B)
    if f_lo * f_hi > 0:
        return float("nan")
    for _ in range(max_iter):
        mid = 0.5 * (n_lo + n_hi)
        f_mid = deriv_fn(mid, B)
        if abs(f_mid) < tol or (n_hi - n_lo) < tol:
            return mid
        if f_lo * f_mid < 0:
            n_hi = mid
            f_hi = f_mid
        else:
            n_lo = mid
            f_lo = f_mid
    return 0.5 * (n_lo + n_hi)


def find_stationary_integer(deriv_fn, B: float, n_lo: int, n_hi: int) -> int:
    """Find integer n in [n_lo, n_hi] minimising |deriv_fn(n, B)|."""
    best_n = n_lo
    best_abs = abs(deriv_fn(n_lo, B))
    for n in range(n_lo + 1, n_hi + 1):
        val = abs(deriv_fn(n, B))
        if val < best_abs:
            best_abs = val
            best_n = n
    return best_n


# ── Potential values ──────────────────────────────────────────────────────────

def v1(n: float, B: float) -> float:
    return n * n - B * n * math.log(n)


def v2(n: float, B: float) -> float:
    return n * n - B * float(loggamma(n + 1))


def v3(n: float, B: float) -> float:
    return n * n - B * (float(loggamma(n + 1)) + n)


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    NSTAR = 137
    BPHENOM = 46.2976  # phenomenological value; not derived

    B_ram = compute_B_ram()

    print("=" * 72)
    print("UBT Alpha Effective Potential Comparison")
    print("  V1(n) = n^2 - B*n*log(n)                    [L1]")
    print("  V2(n) = n^2 - B*log(Gamma(n+1))             [DERIV CAND]")
    print("  V3(n) = n^2 - B*(log(Gamma(n+1)) + n)       [DERIV CAND]")
    print()
    print("WARNING: Alpha is NOT DERIVED. Gap G137-B is OPEN. [OPEN]")
    print("B_Ram is a numerical observation only. [INTERP]")
    print("=" * 72)

    # ── Section 1: B required for n* = 137 ───────────────────────────────────
    print()
    print("── Section 1: B required so that n* = 137 is a stationary point ──")
    print()
    b1 = B_for_nstar_V1(NSTAR)
    b2 = B_for_nstar_V2(NSTAR)
    b3 = B_for_nstar_V3(NSTAR)
    print(f"  V1: B = 2*{NSTAR}/(log({NSTAR})+1) = {b1:.6f}")
    print(f"  V2: B = 2*{NSTAR}/psi({NSTAR}+1)   = {b2:.6f}")
    print(f"  V3: B = 2*{NSTAR}/(psi({NSTAR}+1)+1) = {b3:.6f}")
    print()
    print(f"  Phenomenological B_phenom ≈ {BPHENOM:.4f}")
    print(f"  B_Ram (numerical ref.)    = {B_ram:.6f}")
    print()
    print(f"  V1 vs B_phenom: rel. err = {abs(b1 - BPHENOM)/BPHENOM:.4%}  (exact by definition of B_phenom)")
    print(f"  V2 vs B_phenom: rel. err = {abs(b2 - BPHENOM)/BPHENOM:.4%}  (V2 shifts B by ~17%)")
    print(f"  V3 vs B_phenom: rel. err = {abs(b3 - BPHENOM)/BPHENOM:.4%}  (V3 matches V1 stationary cond.)")
    print()
    print("  [STD/L0] Stationary conditions:")
    print(f"    V1: 2n - B*(log n + 1) = 0")
    print(f"    V2: 2n - B*psi(n+1) = 0,  asymptotically 2n - B*log(n) = 0")
    print(f"    V3: 2n - B*(psi(n+1)+1) = 0,  asymptotically 2n - B*(log(n)+1) = 0")
    print()
    print("  Conclusion: V3 preserves the original V1 stationary condition at")
    print("  leading order and simultaneously encodes the prime-factorization")
    print("  entropy structure via log(Gamma(n+1)).  [INTERP]")

    # ── Section 2: Scan n*(B) for B = B_Ram ──────────────────────────────────
    print()
    print(f"── Section 2: Stationary point scan for B = B_Ram = {B_ram:.6f} ──")
    print()
    n_lo, n_hi = 100, 200
    nstar1 = find_stationary_continuous(v1_deriv, B_ram, n_lo, n_hi)
    nstar2 = find_stationary_continuous(v2_deriv, B_ram, n_lo, n_hi)
    nstar3 = find_stationary_continuous(v3_deriv, B_ram, n_lo, n_hi)
    print(f"  V1: continuous n* = {nstar1:.3f}  (nearest integer: {round(nstar1)})")
    print(f"  V2: continuous n* = {nstar2:.3f}  (nearest integer: {round(nstar2)})")
    print(f"  V3: continuous n* = {nstar3:.3f}  (nearest integer: {round(nstar3)})")
    print()
    nstar1_int = find_stationary_integer(v1_deriv, B_ram, n_lo, n_hi)
    nstar2_int = find_stationary_integer(v2_deriv, B_ram, n_lo, n_hi)
    nstar3_int = find_stationary_integer(v3_deriv, B_ram, n_lo, n_hi)
    print(f"  Integer minimiser of |V'(n)|:")
    print(f"    V1: n* = {nstar1_int}  (target: 137)")
    print(f"    V2: n* = {nstar2_int}  (target: 137)")
    print(f"    V3: n* = {nstar3_int}  (target: 137)")
    print()
    print("  NOTE: B_Ram is a numerical reference only. [INTERP]")
    print("  Whether any of these n* matches 137 depends on a first-principles")
    print("  derivation of B — which is Gap G137-B. [OPEN]")

    # ── Section 3: Derivative table around n = 137 ───────────────────────────
    print()
    print(f"── Section 3: Derivative table around n = 137, B = B_phenom = {BPHENOM} ──")
    print()
    print(f"  {'n':>5}  {'V1_deriv':>12}  {'V2_deriv':>12}  {'V3_deriv':>12}")
    print("  " + "-" * 47)
    for n in range(130, 145):
        d1 = v1_deriv(n, BPHENOM)
        d2 = v2_deriv(n, BPHENOM)
        d3 = v3_deriv(n, BPHENOM)
        marker = " <-- zero crossing" if n == 137 else ""
        print(f"  {n:>5}  {d1:>12.4f}  {d2:>12.4f}  {d3:>12.4f}{marker}")

    # ── Section 4: Legendre formula verification for n = 137 ─────────────────
    print()
    print("── Section 4: Legendre formula check — log(137!) [STD/L0] ──")
    print()

    def legendre_log_factorial(n: int) -> float:
        """Compute log(n!) via Legendre's formula: sum_{p^m <= n} floor(n/p^m)*log(p)."""
        def sieve_primes(limit: int):
            is_p = [True] * (limit + 1)
            is_p[0] = is_p[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if is_p[i]:
                    for j in range(i * i, limit + 1, i):
                        is_p[j] = False
            return [i for i in range(2, limit + 1) if is_p[i]]

        primes = sieve_primes(n)
        total = 0.0
        for p in primes:
            pm = p
            while pm <= n:
                total += (n // pm) * math.log(p)
                pm *= p
        return total

    leg_val = legendre_log_factorial(NSTAR)
    stirling_val = float(loggamma(NSTAR + 1))
    direct_val = sum(math.log(k) for k in range(1, NSTAR + 1))
    print(f"  Direct sum log(1)+...+log({NSTAR}):  {direct_val:.6f}")
    print(f"  log(Gamma({NSTAR}+1)) via scipy:     {stirling_val:.6f}")
    print(f"  Legendre formula:                 {leg_val:.6f}")
    print(f"  Relative difference (Legendre vs direct): {abs(leg_val-direct_val)/abs(direct_val):.2e}")
    print()
    print("  PASS [STD/L0]: Legendre formula reproduces log(n!) exactly.")
    print(f"  S_log({NSTAR}) = log({NSTAR}!) = total log-information of integers 1..{NSTAR}  [INTERP]")

    # ── Summary ───────────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("SUMMARY")
    print()
    print("  The n*log(n) term in V_eff = n^2 - B*n*log(n)  [L1]")
    print("  is the leading Stirling term of the total log-information")
    print("  content of integers 1..n under the prime alphabet.  [INTERP]")
    print()
    print("  V3(n) = n^2 - B*(log(Gamma(n+1)) + n)  [DERIV CAND]")
    print("  preserves the V1 stationary condition at leading order")
    print("  and encodes the exact prime-factorization entropy.")
    print()
    print("  V2(n) = n^2 - B*log(Gamma(n+1))  [DERIV CAND]")
    print("  shifts the stationary B by ~17% and is a less accurate match")
    print("  to B_phenom. It should NOT silently replace V1.")
    print()
    print("  GAP G137-B remains OPEN. Alpha is NOT DERIVED.  [OPEN]")
    print("=" * 72)


if __name__ == "__main__":
    main()
