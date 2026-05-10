# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# File: tools/vcw_minimum_scan.py
#
# Purpose: Determine where the minimum of the exact Coleman-Weinberg potential
#   V_CW(n) = n^2 - N_eff * ln(2*sinh(pi*n))
#   and its variants fall, for various N_eff values.
#
# Background (from research_tracks/T3_ALPHA/cw_determinant_full_derivation.tex
#             and research_tracks/T3_ALPHA/nlogn_mechanism.tex):
#   V_CW is the exact one-loop determinant on S^1_psi.
#   For large n: ln(2*sinh(pi*n)) ~ pi*n + ln2, giving linear correction.
#   The n*ln(n) form in V_eff arises from a different mechanism.
#   Minimum of V_CW: dV/dn = 0 => 2n = N_eff * pi * coth(pi*n)
#   For large n: coth(pi*n) ~ 1, so n* ~ N_eff*pi/2.
#   For n*=137: N_eff_needed = 2*137/pi ~ 87.2.
#
# Classification: [L1] for the formula; [OPEN] for the mechanism bridging gap.

import math


# ── helpers ─────────────────────────────────────────────────────────────────

def is_prime(n: int) -> bool:
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


def coth(x: float) -> float:
    """Hyperbolic cotangent."""
    if x > 100:
        return 1.0
    return math.cosh(x) / math.sinh(x)


# ── potentials ───────────────────────────────────────────────────────────────

def V_CW(n: float, Neff: float) -> float:
    """
    Exact Coleman-Weinberg potential on S^1_psi:
        V_CW(n) = n^2 - N_eff * ln(2*sinh(pi*n))
    """
    arg = math.pi * n
    if arg > 500:
        # asymptotic: ln(2*sinh(pi*n)) ~ pi*n + ln2
        log_sinh = arg + math.log(2)
    else:
        log_sinh = math.log(2 * math.sinh(arg))
    return n**2 - Neff * log_sinh


def dV_CW(n: float, Neff: float) -> float:
    """
    Derivative: dV_CW/dn = 2n - N_eff * pi * coth(pi*n)
    """
    return 2.0 * n - Neff * math.pi * coth(math.pi * n)


def find_minimum_VCW(Neff: float, n_start: float = 2.0, n_end: float = 300.0,
                     step: float = 0.5) -> tuple:
    """
    Find the minimum of V_CW by scanning and refining via bisection.
    Returns (n_min, V_min).
    """
    # Coarse scan
    best_n = n_start
    best_v = V_CW(n_start, Neff)
    n = n_start + step
    while n <= n_end:
        v = V_CW(n, Neff)
        if v < best_v:
            best_v = v
            best_n = n
        n += step

    # Bisection refinement on dV=0 around best_n
    lo = max(1.0, best_n - step)
    hi = min(n_end, best_n + step)
    # Check sign change
    if dV_CW(lo, Neff) * dV_CW(hi, Neff) > 0:
        return best_n, best_v

    for _ in range(100):
        mid = (lo + hi) / 2.0
        if dV_CW(lo, Neff) * dV_CW(mid, Neff) <= 0:
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-10:
            break
    n_min = (lo + hi) / 2.0
    return n_min, V_CW(n_min, Neff)


def V_Veff_nlogn(n: float, B: float) -> float:
    """
    Simplified V_eff = n^2 - B*n*ln(n), the n*ln(n) potential.
    """
    if n <= 0:
        return float('inf')
    return n**2 - B * n * math.log(n)


def V_divisor(n: int, Neff: float, f_bar: float) -> float:
    """
    Divisor-sum correction (from nlogn_mechanism.tex, Cesta A):
        V_div(n) = -N_eff * f_bar * D(n)
    where D(n) = sum_{k=1}^{n} tau(k),  tau(k) = number of divisors of k.
    Combined potential: V_CW(n) + V_div(n).
    """
    D = sum(sum(1 for d in range(1, k + 1) if k % d == 0) for k in range(1, n + 1))
    return n**2 - Neff * math.log(2 * math.sinh(math.pi * n)) - Neff * f_bar * D


def V_modular(n: int, Neff: float, C: float) -> float:
    """
    Combined potential with modular correction for prime n:
        V_mod(n) = V_CW(n) - C*(n+1)/3    [only for prime n]
    The modular correction -C*(n+1)/3 encodes the normalised volume of X_0(n).
    """
    vcw = V_CW(n, Neff)
    if is_prime(n):
        return vcw - C * (n + 1) / 3.0
    return vcw


# ── main analysis ────────────────────────────────────────────────────────────

def run_vcw_scan():
    print("=" * 80)
    print("V_CW MINIMUM SCAN")
    print("V_CW(n) = n^2 - N_eff * ln(2*sinh(pi*n))")
    print("=" * 80)

    neff_values = [3, 6, 12, 24, 48, 87, 88]

    print(f"{'N_eff':>8}  {'n*(V_CW)':>10}  {'V_CW(n*)':>12}  {'prime?':>7}  {'N_eff*pi/2':>12}")
    print("-" * 65)
    for Neff in neff_values:
        n_min, v_min = find_minimum_VCW(Neff)
        approx = Neff * math.pi / 2.0
        print(f"{Neff:>8.1f}  {n_min:>10.2f}  {v_min:>12.4f}  {str(is_prime(round(n_min))):>7}  {approx:>12.2f}")

    # Find exact N_eff needed for n*=137
    print()
    print("Exact N_eff required for n*(V_CW) = 137:")
    print("  From dV/dn=0: 2*137 = N_eff*pi*coth(pi*137)")
    Neff_exact = 2 * 137 / (math.pi * coth(math.pi * 137))
    print(f"  N_eff_needed = 2*137 / (pi*coth(pi*137)) = {Neff_exact:.4f}")
    print(f"  coth(pi*137) ≈ {coth(math.pi*137):.10f}  (essentially 1 for large n)")
    print(f"  Large-n approx: N_eff_needed ≈ 2*137/pi = {2*137/math.pi:.4f}")
    print(f"  UBT has N_eff in {{3, 12}}. Gap: 87.2 / 12 = {87.2/12:.2f}")

    print()
    print("=" * 80)
    print("V_CW SCAN FOR n=1..200, N_eff=12 (detailed)")
    print("=" * 80)
    Neff = 12
    print(f"{'n':>5}  {'V_CW':>12}  {'prime?':>7}  {'local min?':>11}")
    print("-" * 42)
    prev_v = V_CW(1, Neff)
    prev2_v = None
    min_n = None
    min_v = float('inf')
    for n in range(1, 201):
        v = V_CW(n, Neff)
        is_local_min = False
        if prev2_v is not None and prev_v < prev2_v and prev_v < v:
            is_local_min = True
        if v < min_v:
            min_v = v
            min_n = n
        if n <= 30 or (120 <= n <= 145) or is_local_min:
            print(f"{n:>5}  {v:>12.4f}  {str(is_prime(n)):>7}  {str(is_local_min):>11}")
        prev2_v = prev_v
        prev_v = v
    print()
    print(f"  Global minimum of V_CW (N_eff=12, n in [1,200]): n={min_n}, V={min_v:.4f}")
    print(f"  n={min_n} is prime: {is_prime(min_n)}")

    print()
    print("=" * 80)
    print("COMBINED POTENTIAL: V_CW + V_modular correction")
    print("Searching for C that places minimum at n=137 (prime)")
    print("=" * 80)
    Neff = 12

    # We need V_mod(137) < V_mod(n) for all other n (especially near minima)
    # V_mod(137, C) = V_CW(137) - C*(137+1)/3
    # Competitor: n_min_CW from V_CW alone
    n_cw_min, v_cw_min = find_minimum_VCW(Neff)
    n_comp = round(n_cw_min)   # main competitor
    v_comp_cw = V_CW(n_comp, Neff)
    v_137_cw = V_CW(137, Neff)

    print(f"  V_CW(n={n_comp}, N_eff=12) = {v_comp_cw:.4f}  (main competitor)")
    print(f"  V_CW(n=137,  N_eff=12) = {v_137_cw:.4f}")
    print(f"  Gap to overcome: V_CW(137) - V_CW({n_comp}) = {v_137_cw - v_comp_cw:.4f}")
    print()

    # Find C such that V_mod(137) < V_mod(n_comp)
    # V_CW(137) - C*(138/3) < V_CW(n_comp) - C*(n_comp+1)/3 [if n_comp is prime]
    # C*(138/3 - (n_comp+1)/3) > V_CW(137) - V_CW(n_comp)
    if is_prime(n_comp):
        denom = (138 / 3.0) - ((n_comp + 1) / 3.0)
        if denom > 0:
            C_min = (v_137_cw - v_comp_cw) / denom
            print(f"  For modular correction to flip minimum from n={n_comp} to n=137:")
            print(f"  C_min = {C_min:.4f}")
            print(f"  (assuming n={n_comp} is also prime and gets modular correction)")
        else:
            C_min = None
            print(f"  n={n_comp} is prime but has larger modular volume -> correction doesn't help")
    else:
        # If n_comp is not prime, no modular correction there
        denom = 138 / 3.0
        C_min = (v_137_cw - v_comp_cw) / denom
        print(f"  n={n_comp} is NOT prime -> no modular correction at competitor.")
        print(f"  C_min to flip minimum: {C_min:.4f}  (from C*46 > gap)")

    if C_min is not None:
        print()
        # Check if C has a natural UBT value
        # V_modular was derived from B_modular ~ (p+1)/3; C ~ N_eff * pi?
        c_natural = Neff * math.pi / 3
        print(f"  Natural candidate C = N_eff*pi/3 = {c_natural:.4f}")
        print(f"  Is C_min achievable from UBT? C_min/C_natural = {C_min/c_natural:.4f}")
        print(f"  Verdict: {'YES (within factor 2)' if C_min/c_natural < 2 else 'NO (too large by factor ' + f'{C_min/c_natural:.1f})'}")

    print()
    print("=" * 80)
    print("COMBINED V_CW + V_modular: scan n=1..200, N_eff=12, C=C_min or 0")
    print("=" * 80)
    if C_min is not None and C_min > 0:
        C = C_min
    else:
        C = 50.0   # test value

    print(f"  Using C = {C:.4f}")
    min_n2 = None
    min_v2 = float('inf')
    for n in range(1, 201):
        v = V_modular(n, Neff, C)
        if v < min_v2:
            min_v2 = v
            min_n2 = n

    print(f"  Global minimum of V_combined (N_eff=12, C={C:.2f}): n={min_n2}, V={min_v2:.4f}")
    print(f"  n={min_n2} is prime: {is_prime(min_n2)}")

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    n_veff_12, v_veff_12 = find_minimum_VCW(12)
    n_veff_3, v_veff_3   = find_minimum_VCW(3)
    print(f"  V_CW minimum (N_eff=3):   n* = {n_veff_3:.2f}")
    print(f"  V_CW minimum (N_eff=12):  n* = {n_veff_12:.2f}")
    print(f"  N_eff needed for n*=137:  {Neff_exact:.1f}")
    print(f"  Gap factor:               {Neff_exact/12:.2f}")
    print()
    if C_min is not None and C_min > 0:
        c_natural = Neff * math.pi / 3
        print(f"  V_combined minimum with C={C:.2f}: n* = {min_n2}")
        print(f"  C_min needed:              {C_min:.4f}")
        print(f"  Natural C candidate:       {c_natural:.4f}")
        ratio = C_min / c_natural
        print(f"  Ratio C_min/C_natural:     {ratio:.4f}")
        if ratio < 1.5:
            verdict = "PROMISING — within natural scale"
        elif ratio < 3.0:
            verdict = "POSSIBLE — requires additional factor"
        else:
            verdict = "UNLIKELY — C_min >> natural scale"
        print(f"  Verdict:                   {verdict}")
    print()
    print("  Conclusion: V_CW alone CANNOT produce n*=137 with N_eff=12 or N_eff=3.")
    print("  A supplementary mechanism (modular, divisor, or higher-loop) is required.")
    print("  The modular correction V_mod = -C*(n+1)/3 can in principle shift the")
    print("  minimum to n=137 if C has the right magnitude from UBT.")
    print("  Whether C is derivable from S[Theta] is [OPEN].")


if __name__ == "__main__":
    run_vcw_scan()
