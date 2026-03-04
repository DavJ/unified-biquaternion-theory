#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
compute_B_KK_sum.py — Three independent approaches to deriving B_base = N_eff^{3/2}
from the compact ψ-circle Kaluza-Klein mode sum.

PURPOSE
-------
The fine-structure constant derivation in UBT requires B ≈ 46.3 in the effective
potential V_eff(n) = A·n² − B·n·ln(n).  The standard one-loop result is

    B₀ = 2π·N_eff/3   [DERIVED — flat spacetime one-loop β-function]

For N_eff = 12 this gives B₀ = 25.1, which is too small (n* = 67, not 137).
The phenomenological formula used in the derivation is

    B_base = N_eff^{3/2}   [OPEN PROBLEM A — no derivation]

This script tests THREE approaches to deriving B_base:

  Method 1 — KK mode sum (Euler-Maclaurin approach):
    The compact ψ-circle introduces a KK tower of virtual fermions in the
    one-loop vacuum polarization.  Summing over all KK modes and comparing
    to the flat-space result checks whether the ratio gives N_eff^{1/2}/(2π/3).

  Method 2 — Zeta-function regularization:
    The KK sum is regulated using Riemann zeta function ζ(-1) = -1/12.
    This gives an analytic correction to B₀ from the compact dimension.

  Method 3 — Gauge orbit volume (Weyl formula):
    Vol(SU(N)) = (2π)^{N(N+1)/2} / (1!·2!···(N-1)!)
    If B_base = C·Vol(SU(N_eff)), fitting C and checking the N^{3/2} scaling
    would provide a geometric derivation.

HONEST ACCOUNTING
-----------------
After running all three methods the script reports:
  - If any method gives B_base = N_eff^{3/2}: status → [DERIVED]
  - If none works: status → [HONEST GAP] with exact numerical values

NO CIRCULARITY: the computation uses only N_eff and geometric quantities;
it does NOT use the target n* = 137 or α = 1/137 as input.

USAGE
-----
    python tools/compute_B_KK_sum.py

REFERENCES
----------
  [1] Appelquist & Chodos, Phys. Rev. D 28 (1983) 772 — KK quantum corrections
  [2] Kaluza-Klein review: Overduin & Wesson, Phys. Rep. 283 (1997) 303
  [3] Weyl integration formula: Bröcker & tom Dieck, "Representations of Compact
      Lie Groups", Springer (1985)
"""

import math
import sys

import numpy as np
from scipy import integrate

# ─────────────────────────────────────────────────────────────────────────────
# Global parameters  [POSTULATE — R_psi = 1 in natural units]
# ─────────────────────────────────────────────────────────────────────────────

R_PSI = 1.0    # compactification radius (natural units)
LAMBDA = 1.0   # UV cutoff Λ = 1/R_psi = 1

N_EFF_VALUES = [4, 8, 12, 24]  # gauge group sizes to test


# ─────────────────────────────────────────────────────────────────────────────
# Reference: flat-space one-loop result  [DERIVED]
# ─────────────────────────────────────────────────────────────────────────────

def B_flat(N_eff: int) -> float:
    """Standard flat-spacetime one-loop B coefficient.

    B₀ = 2π·N_eff / 3   [DERIVED — standard one-loop β-function]

    For N_eff = 12 this gives B₀ ≈ 25.13.
    """
    return 2.0 * math.pi * N_eff / 3.0


# ─────────────────────────────────────────────────────────────────────────────
# Method 1 — KK mode sum (Euler-Maclaurin)
# ─────────────────────────────────────────────────────────────────────────────

def _f_integrand_kk(z: float, k: int) -> float:
    """Feynman-parameter integrand for the k-th KK mode contribution.

    f(z, k) = z(1-z) ln[1 + z(1-z)/k²]   for k ≠ 0

    This is the standard Feynman-parameter form of the vacuum polarization
    contribution from a Dirac fermion of mass m_k = |k|/R_psi (massless limit).

    [SKETCH — applies standard vacuum polarization integral mode-by-mode to the
     KK tower; justified by Appelquist-Chodos 1983 for compact extra dimensions]
    """
    if k == 0:
        return 0.0
    m_k_sq = float(k * k)
    return z * (1.0 - z) * math.log(1.0 + z * (1.0 - z) / m_k_sq)


def _S_single_mode(k: int) -> float:
    """Feynman-parameter integral for a single KK mode k.

    S_k = ∫₀¹ dz z(1-z) ln[1 + z(1-z)/k²]
    """
    if k == 0:
        return 0.0
    val, _ = integrate.quad(
        lambda z: _f_integrand_kk(z, k), 0.0, 1.0, limit=100
    )
    return val


def S_KK(N_eff: int, K_max: int = 100) -> float:
    """KK mode sum for N_eff species, truncated at |k| ≤ K_max.

    S(N_eff, K_max) = (N_eff / (3π)) · Σ_{k=-K_max, k≠0}^{K_max} S_k

    The factor N_eff/(3π) matches the standard vacuum polarisation normalization
    for N_eff charged scalar modes (factor from spinor trace included in N_eff).

    [SKETCH — derivation follows Appelquist-Chodos 1983 Appendix B]
    """
    total = 0.0
    for k in range(-K_max, K_max + 1):
        if k == 0:
            continue
        total += _S_single_mode(k)
    return (N_eff * total) / (3.0 * math.pi)


def convergence_check(N_eff: int = 12) -> None:
    """Check convergence of S_KK(N_eff, K_max) as K_max increases."""
    print("  Convergence check (N_eff=12):")
    print(f"  {'K_max':>8}  {'S_KK':>12}  {'B_flat':>12}  {'ratio':>10}")
    B0 = B_flat(N_eff)
    for K_max in [5, 10, 20, 50, 100]:
        S = S_KK(N_eff, K_max=K_max)
        ratio = S / B0 if B0 > 0 else float("nan")
        print(f"  {K_max:>8}  {S:>12.5f}  {B0:>12.5f}  {ratio:>10.5f}")
    print()


def method1_KK_sum() -> None:
    """Method 1: KK mode sum approach.

    If the ratio S_KK(N_eff) / B_flat(N_eff) ≈ N_eff^{1/2} / (2π/3),
    then B_base = N_eff^{3/2} follows from the KK mode sum.  [DERIVED]
    Otherwise, document the actual ratio.  [HONEST GAP]
    """
    print("=" * 70)
    print("METHOD 1 — KK Mode Sum (Euler-Maclaurin approach)")
    print("=" * 70)
    print()
    print("Starting point  [DERIVED]:")
    print("  B₀ = 2π·N_eff/3  (flat-spacetime one-loop β-function)")
    print()
    print("Setup  [POSTULATE — R_psi = 1, Λ = 1/R_psi]:")
    print("  Compact ψ-circle S¹ with KK masses m_k = k/R_psi = k")
    print("  One-loop vacuum polarization summed over k ∈ ℤ\\{0}")
    print()

    convergence_check(N_eff=12)

    print(f"  {'N_eff':>6}  {'S_KK':>10}  {'B_flat':>10}  {'ratio':>10}  "
          f"{'N^0.5/(2π/3)':>14}  {'match?':>8}")
    print(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*14}  {'-'*8}")

    matches = []
    for N_eff in N_EFF_VALUES:
        S = S_KK(N_eff, K_max=100)
        B0 = B_flat(N_eff)
        ratio = S / B0 if B0 > 0 else float("nan")
        expected_ratio = N_eff ** 0.5 / (2.0 * math.pi / 3.0)
        rel_err = abs(ratio - expected_ratio) / expected_ratio if expected_ratio > 0 else float("nan")
        match = rel_err < 0.02  # 2% tolerance
        matches.append(match)
        flag = "YES" if match else "NO"
        print(f"  {N_eff:>6}  {S:>10.4f}  {B0:>10.4f}  {ratio:>10.4f}  "
              f"{expected_ratio:>14.4f}  {flag:>8}")

    print()
    if all(matches):
        print("  RESULT [DERIVED]: Ratio S_KK/B_flat ≈ N_eff^{1/2}/(2π/3) for all N_eff.")
        print("  → B_base = N_eff^{3/2} is derived from the compact KK mode sum.")
        verdict = "DERIVED"
    else:
        S12 = S_KK(12, K_max=100)
        B0_12 = B_flat(12)
        actual_ratio = S12 / B0_12
        required_ratio = 12 ** 0.5 / (2.0 * math.pi / 3.0)
        print("  RESULT [HONEST GAP]: Ratio S_KK/B_flat does NOT match N_eff^{1/2}/(2π/3).")
        print(f"  For N_eff=12: actual ratio = {actual_ratio:.4f}, "
              f"required = {required_ratio:.4f}.")
        print(f"  Actual S_KK(12) = {S12:.4f};  B_flat(12) = {B0_12:.4f}.")
        print()
        print("  NOTE: The KK sum with massless fermion modes (m_k = k/R_psi)")
        print("  does NOT reproduce the N_eff^{3/2} scaling.")
        print("  This is an HONEST GAP.  B_base = N_eff^{3/2} is NOT derived")
        print("  from this mode sum structure.")
        verdict = "HONEST GAP"
    print()
    return verdict


# ─────────────────────────────────────────────────────────────────────────────
# Method 2 — Zeta-function regularization
# ─────────────────────────────────────────────────────────────────────────────

def B_zeta(N_eff: int, R_psi: float = 1.0, Lambda: float = 1.0) -> float:
    """Zeta-function regularized KK contribution.

    Using Riemann zeta regularization:
        ΔB = (N_eff/3) · 2·ζ(-1) · (2π/(R_psi·Λ))²
    where ζ(-1) = -1/12.

    [SKETCH — zeta regularization of Σ_{k=1}^∞ k applies to the KK tower;
     physical meaning requires careful treatment of boundary conditions]
    """
    zeta_minus1 = -1.0 / 12.0  # ζ(-1) = −1/12 (Riemann zeta)
    B_0 = 2.0 * math.pi * N_eff / 3.0
    # Correction from compact dimension (zeta-regularized KK sum)
    Delta = (N_eff / 3.0) * 2.0 * zeta_minus1 * (2.0 * math.pi / (R_psi * Lambda)) ** 2
    return B_0 + Delta


def method2_zeta() -> None:
    """Method 2: Zeta-function regularization of the KK sum."""
    print("=" * 70)
    print("METHOD 2 — Zeta-function regularization of KK sum")
    print("=" * 70)
    print()
    print("Using ζ(-1) = −1/12 (Riemann zeta regularization of Σ_{k=1}^∞ k)")
    print("  ΔB = (N_eff/3) · 2·ζ(-1) · (2π/R_psi·Λ)²   [SKETCH]")
    print()
    print(f"  {'N_eff':>6}  {'B_zeta':>10}  {'B_flat':>10}  {'B_base=N^1.5':>14}  {'match B_base?':>14}")
    print(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*14}  {'-'*14}")

    matches = []
    for N_eff in N_EFF_VALUES:
        Bz = B_zeta(N_eff)
        B0 = B_flat(N_eff)
        B_required = float(N_eff) ** 1.5
        rel_err = abs(Bz - B_required) / B_required
        match = rel_err < 0.05
        matches.append(match)
        flag = "YES" if match else "NO"
        print(f"  {N_eff:>6}  {Bz:>10.4f}  {B0:>10.4f}  {B_required:>14.4f}  {flag:>14}")

    print()
    if all(matches):
        print("  RESULT [DERIVED]: Zeta regularization gives B ≈ N_eff^{3/2}.")
        verdict = "DERIVED"
    else:
        # Detailed analysis for N_eff=12
        Bz12 = B_zeta(12)
        B0_12 = B_flat(12)
        B_req = 12.0 ** 1.5
        print("  RESULT [HONEST GAP]: Zeta-regularized KK correction gives")
        print(f"  B_zeta(12) = {Bz12:.4f}")
        print(f"  B_flat(12) = {B0_12:.4f}  (one-loop, derived)")
        print(f"  B_base     = {B_req:.4f}  (required)")
        print()
        print("  Analysis:")
        print(f"    ΔB (zeta correction) = {Bz12 - B0_12:.4f}")
        print(f"    Sign: {'+' if Bz12 > B0_12 else '−'} → zeta correction moves B "
              f"{'away from' if Bz12 < B0_12 else 'toward'} the required value.")
        print()
        print("  NOTE: The (2π/R_psi·Λ)² = (2π)² ≈ 39.5 factor in ΔB is a")
        print("  large number that overwhelms the ζ(-1)=-1/12 coefficient.")
        print("  The correction goes in the wrong direction (decreases B below B₀).")
        print("  This approach does NOT reproduce B_base = N_eff^{3/2}.")
        verdict = "HONEST GAP"
    print()
    return verdict


# ─────────────────────────────────────────────────────────────────────────────
# Method 3 — Gauge orbit volume (Weyl formula)
# ─────────────────────────────────────────────────────────────────────────────

def vol_SUN(N: int) -> float:
    """Volume of SU(N) via the Weyl integration formula.

    Vol(SU(N)) = (2π)^{N(N+1)/2} / ∏_{k=1}^{N-1} k!

    Reference: Bröcker & tom Dieck (1985), Eq. (7.3.1)
    Note: this is the volume with respect to the round bi-invariant metric
    normalized so that the long root has length √2.  An overall normalization
    constant is convention-dependent; here we use the Weyl formula directly.
    """
    exponent = N * (N + 1) / 2.0
    numerator = (2.0 * math.pi) ** exponent
    denominator = 1.0
    for k in range(1, N):
        denominator *= math.factorial(k)
    return numerator / denominator


def method3_gauge_orbit_volume() -> None:
    """Method 3: Gauge orbit volume from Weyl integration formula.

    If Vol(SU(N)) ~ C·N^{3/2} for large N, and B_base = C_B·Vol(SU(N_eff))
    for some constant C_B, then B_base = N_eff^{3/2} is derivable from the
    gauge orbit volume.  [CONJECTURE — check literature]
    """
    print("=" * 70)
    print("METHOD 3 — Gauge orbit volume (Weyl integration formula)")
    print("=" * 70)
    print()
    print("  Vol(SU(N)) = (2π)^{N(N+1)/2} / ∏_{k=1}^{N-1} k!")
    print()
    print(f"  {'N':>4}  {'Vol(SU(N))':>14}  {'N^1.5':>10}  {'Vol/N^1.5':>12}")
    print(f"  {'-'*4}  {'-'*14}  {'-'*10}  {'-'*12}")

    vols = {}
    for N in [2, 3, 4, 5, 6, 8, 10, 12]:
        v = vol_SUN(N)
        n15 = float(N) ** 1.5
        ratio = v / n15
        vols[N] = (v, ratio)
        print(f"  {N:>4}  {v:>14.4e}  {n15:>10.4f}  {ratio:>12.4e}")

    print()
    # Check power-law scaling: fit α in Vol(SU(N)) = C·N^α
    # Use N=4..12 (large-N limit)
    ns = [4, 5, 6, 8, 10, 12]
    log_v = [math.log(vols[N][0]) for N in ns]
    log_n = [math.log(N) for N in ns]
    # Linear fit: log(V) = log(C) + α·log(N)
    n_pts = len(ns)
    mean_ln = sum(log_n) / n_pts
    mean_lv = sum(log_v) / n_pts
    cov = sum((log_n[i] - mean_ln) * (log_v[i] - mean_lv) for i in range(n_pts))
    var = sum((log_n[i] - mean_ln) ** 2 for i in range(n_pts))
    alpha_fit = cov / var if var > 0 else float("nan")
    C_fit = math.exp(mean_lv - alpha_fit * mean_ln)
    print(f"  Power-law fit Vol(SU(N)) = C·N^α (using N = {ns}):")
    print(f"    α = {alpha_fit:.3f}  (required: 1.5 for N_eff^{{3/2}} to hold)")
    print(f"    C = {C_fit:.4e}")
    print()

    # Check at N_eff = 12
    V12 = vol_SUN(12)
    B_from_vol = C_fit * (12.0 ** 1.5) if abs(alpha_fit - 1.5) < 0.1 else None
    B_required = 12.0 ** 1.5  # = 41.57

    if abs(alpha_fit - 1.5) < 0.5:
        print(f"  α ≈ {alpha_fit:.3f}: power-law is approximately N^α scaling.")
        if B_from_vol is not None:
            print(f"  But C = {C_fit:.4e} ≫ 1, so B_base = C·N_eff^{{3/2}} = "
                  f"{C_fit * 12**1.5:.3e} ≠ {B_required:.2f}.")
    else:
        print(f"  α ≈ {alpha_fit:.3f} ≠ 1.5: the N^{{3/2}} scaling does NOT hold for")
        print(f"  Vol(SU(N)) in this range.  The growth is much faster than N^{{3/2}}.")
    print()
    print("  RESULT [HONEST GAP]:")
    print("  Vol(SU(N)) grows as N^α with α ≫ 3/2 (due to factorial in denominator).")
    print("  The Weyl formula gives Vol(SU(N)) ~ (2πe/N)^{N²/2} (Stirling approx.),")
    print("  which is SUPER-EXPONENTIAL in N, not N^{3/2}.")
    print("  The gauge orbit volume hypothesis is therefore [DEAD END] as a direct")
    print("  derivation of B_base = N_eff^{3/2}.")
    print()
    print("  HOWEVER: if B_base is proportional to ln(Vol(SU(N_eff))) / N_eff^{1/2},")
    print("  or to some other reduced functional of the volume, then the scaling")
    print("  might still work.  This requires further investigation.")
    print()
    return "HONEST GAP"


# ─────────────────────────────────────────────────────────────────────────────
# Summary and honest accounting
# ─────────────────────────────────────────────────────────────────────────────

def final_summary(v1: str, v2: str, v3: str) -> None:
    """Print the honest accounting summary of all three methods."""
    print("=" * 70)
    print("FINAL HONEST ACCOUNTING")
    print("=" * 70)
    print()
    print(f"  Method 1 (KK sum, Euler-Maclaurin):    {v1}")
    print(f"  Method 2 (Zeta-function regularization): {v2}")
    print(f"  Method 3 (Gauge orbit volume):           {v3}")
    print()

    any_derived = any(v == "DERIVED" for v in [v1, v2, v3])

    if any_derived:
        print("  STATUS: [DERIVED] — at least one approach gives B_base = N_eff^{3/2}.")
        print("  See above for the specific mechanism.")
        print()
        print("  ACTION: Update STATUS_ALPHA.md §9 'OPEN PROBLEM A' → RESOLVED.")
        print("          Remove B̃ from FITTED_PARAMETERS.md.")
        print("          Update DERIVATION_INDEX.md: B coefficient → Proven.")
    else:
        print("  STATUS: [HONEST GAP] — NONE of the three approaches gives N_eff^{3/2} scaling.")
        print()
        print("  WHAT EACH APPROACH GIVES:")
        print()

        # Report actual values
        S12 = S_KK(12, K_max=100)
        B0_12 = B_flat(12)
        Bz12 = B_zeta(12)
        B_req = 12.0 ** 1.5

        print(f"    B_flat (one-loop, derived):        {B0_12:.4f}  → n* = 67")
        print(f"    S_KK   (KK mode sum):              {S12:.4f}  → n* = {_n_star(B0_12, S12)}")
        print(f"    B_zeta (zeta regularization):      {Bz12:.4f}  → n* = {_n_star(B0_12, Bz12)}")
        print(f"    B_required (N_eff^{{3/2}}):          {B_req:.4f}  → n* = 127")
        print(f"    B_full (B_base × R=1.114):         {B_req * 1.114:.4f}  → n* = 137")
        print()
        print("  CONCLUSION:")
        print("  None of the three approaches gives N_eff^{3/2} scaling.")
        print("  The formula B_base = N_eff^{3/2} = 41.57 remains PHENOMENOLOGICAL.")
        print()
        print("  The correct one-loop value B₀ = 25.1 predicts n*(B₀) = 67 ≠ 137.")
        print("  This is an OPEN HARD PROBLEM.")
        print()
        print("  The α derivation at bare level requires B_base to be treated as")
        print("  a fitted parameter until a geometric derivation is found.")
        print()
        print("  ACTION: Keep STATUS_ALPHA.md §9 'OPEN PROBLEM A' as OPEN.")
        print("          Keep B̃ in FITTED_PARAMETERS.md.")
        print("          Update DERIVATION_INDEX.md: B coefficient → Open Hard Problem")
        print("          (precisely restated, not hidden).")
    print()


def _n_star(B0: float, B_test: float) -> int:
    """Return the prime minimizing V_eff(n) = n² - B_test·n·ln(n)."""
    # Use the same prime sieve and V_eff computation as validate_B_coefficient.py
    primes = _sieve(600)

    def v_eff(n):
        if n <= 1:
            return float("inf")
        return n * n - B_test * n * math.log(n)

    best_p = primes[0]
    best_v = v_eff(best_p)
    for p in primes:
        v = v_eff(p)
        if v < best_v:
            best_v = v
            best_p = p
    return best_p


def _sieve(n: int):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main() -> int:
    print()
    print("=" * 70)
    print("UBT — B_base = N_eff^{3/2}: Three Derivation Approaches")
    print("=" * 70)
    print()
    print("No-circularity constraint: this script does NOT use n* = 137 or")
    print("α = 1/137 as input.  The only inputs are N_eff and geometry.")
    print()

    v1 = method1_KK_sum()
    v2 = method2_zeta()
    v3 = method3_gauge_orbit_volume()
    final_summary(v1, v2, v3)

    # Return 0 if at least one method derives B_base = N_eff^{3/2}; 1 otherwise
    if any(v == "DERIVED" for v in [v1, v2, v3]):
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
