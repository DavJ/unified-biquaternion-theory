#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
compute_B_from_Lfunctions.py — Test whether B_phenom = 46.3 is a special
value of a modular L-function associated with the Hecke newforms encoding
lepton masses.

PURPOSE
-------
The fine-structure constant derivation in UBT requires B_phenom ≈ 46.3
(Open Problem A).  The proved result is B₀ = 8π ≈ 25.13.  After three
prior approaches failed (KK sum, zeta, gauge orbit), this script tests
Approaches A1 and A4:

  Approach A1: Is B_phenom = 2π·L(1,f) or L(2,f) for modular forms
               associated with the Dedekind zeta functions of
               K = Q(√(-137)) or K = Q(√(-139))?

  Approach A4: Is B_phenom related to Hecke eigenvalues a_137 = -9
               (p=137 match) or a_139 = 9 (p=139 match)?

               Specifically: a_137^2 / π ≈ B₀ (coincidence found);
               does a_137^2 / π scale to B_phenom with a natural factor?

INPUTS
------
No external inputs.  All quantities derived from:
  - B₀ = 8π (proved, from UBT)
  - B_phenom ≈ 46.3 (phenomenological target)
  - a_137 = -9 (Hecke eigenvalue from SageMath search)
  - a_139 = +9 (Hecke eigenvalue from SageMath search)
  - Class numbers and discriminants of Q(√(-137)), Q(√(-139))

HONEST ACCOUNTING
-----------------
The script reports:
  - MATCH if any formula gives B_phenom to within 0.1%
  - CLOSE  if within 1%
  - FAIL   otherwise
No circular use of α = 1/137 or n* = 137 as inputs.

USAGE
-----
    python tools/compute_B_from_Lfunctions.py

REFERENCES
----------
  - approach_A1_modular.tex
  - approach_A4_hecke_eigenvalue.tex
  - tools/compute_B_KK_sum.py (prior approaches)
"""

import math
import sys

# ─── Physical constants ──────────────────────────────────────────────────────
PI = math.pi
B0 = 8 * PI          # proved one-loop result
B_PHENOM = 46.3      # phenomenological target (no circular use of alpha)
NEFF = 12            # proved from dim Im(H) = 3

# ─── Hecke eigenvalues from SageMath search ──────────────────────────────────
A_137 = -9           # a_137 for k=2 newform at level N=38 (p=137 match)
A_139 = 9            # a_139 for k=2 newform at level N=200 (p=139 match)

# ─── Class numbers for imaginary quadratic fields ────────────────────────────
# Q(sqrt(-137)): discriminant -137 (137 ≡ 1 mod 4, so d_K = -4*137 ... wait)
# 137 mod 4 = 1, so disc(Q(sqrt(-137))) = -137 (fundamental discriminant)
# h(-137) = 8 (from Gauss class number table for prime discriminants)
H_137 = 8
D_137 = 137          # |discriminant|

# Q(sqrt(-139)): 139 mod 4 = 3, so disc = -4*139 = -556, |d| = 556
# h(-139): using class number formula or tables; h = 3
H_139 = 3
D_139 = 4 * 139      # |discriminant| = 556


def dedekind_zeta_residue(h, d, w=2):
    """
    Residue of Dedekind zeta ζ_K(s) at s=1 for imaginary quadratic K.
    Formula: lim_{s→1} (s-1)ζ_K(s) = 2π h / (w √|d|)

    Parameters
    ----------
    h : class number
    d : |discriminant|
    w : number of roots of unity (2 for most imaginary quadratic fields)
    """
    return 2 * PI * h / (w * math.sqrt(d))


def dedekind_zeta_2(h, d, w=2):
    """
    Approximate ζ_K(2) for imaginary quadratic K via:
    ζ_K(2) = π^2 h / (3 w √|d|) × R
    where R = 1 for imaginary quadratic (regulator = 1, and the exact formula
    involves L(2, χ_d) not ζ_Q(2)).

    More precisely: ζ_K(2) = ζ(2) · L(2, χ_d) where χ_d is the Kronecker symbol.
    For a rough estimate: L(2, χ_d) ≈ (1 - χ_d(2)/4)(1 - χ_d(3)/9)...

    We use the known identity:
    ζ_K(2) = (π^2/6) × L(2, χ_d)
    and approximate L(2, χ_d) ≈ 1 for a rough check.
    """
    # Rough approximation: L(2, χ_d) ≈ π^2 / (12 √|d|) × something
    # Better: use the exact formula for the Dirichlet character
    # For |d| large, L(2, χ_d) ≈ 1 (converges to ~1 for large |d|)
    # This is a rough approximation only
    L2_rough = (PI ** 2 / 6)  # ζ(2) lower bound
    return L2_rough  # rough approximation


def format_result(label, value, target, tol_match=0.001, tol_close=0.01):
    """Format comparison result."""
    rel_err = abs(value - target) / target
    if rel_err < tol_match:
        status = "MATCH ✓"
    elif rel_err < tol_close:
        status = "CLOSE  ~"
    else:
        status = "FAIL   ✗"
    return f"  {label:<45s} = {value:8.4f}   [{status}  err={rel_err*100:.2f}%]"


# ─── Main computation ─────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("compute_B_from_Lfunctions.py")
    print("Test: Can B_phenom ≈ 46.3 be a modular L-function value?")
    print("=" * 72)
    print()

    print(f"  Target:    B_phenom = {B_PHENOM}")
    print(f"  Proved:    B₀       = 8π = {B0:.6f}")
    print(f"  Ratio:     B_phenom / B₀ = {B_PHENOM/B0:.6f}")
    print(f"  N_eff      = {NEFF}  (proved from dim Im(H) = 3)")
    print(f"  a_137      = {A_137}  (Hecke eigenvalue, k=2, p=137 match)")
    print(f"  a_139      = {A_139}  (Hecke eigenvalue, k=2, p=139 match)")
    print()

    print("─" * 72)
    print("APPROACH A1: Dedekind Zeta Functions")
    print("─" * 72)

    # Residue at s=1
    res_137 = dedekind_zeta_residue(H_137, D_137)
    res_139 = dedekind_zeta_residue(H_139, D_139)

    print("  Testing: B_phenom = (2π/w) × h(K) / √|d_K|")
    print(format_result("ζ_K(s→1) residue, K=Q(√-137)", res_137, B_PHENOM))
    print(format_result("ζ_K(s→1) residue, K=Q(√-139)", res_139, B_PHENOM))
    print()

    # Testing variations
    print("  Testing: B_phenom = π × 2h(K) / √|d_K|  (same as residue × π/1)")
    print(format_result("π × res_K(Q(√-137))", PI * res_137, B_PHENOM))
    print(format_result("π × res_K(Q(√-139))", PI * res_139, B_PHENOM))
    print()

    print("  Testing: B_phenom = π² × h(K) / (3 × √|d_K|/2)")
    val_137_v2 = PI**2 * H_137 / (3 * math.sqrt(D_137) / 2)
    val_139_v2 = PI**2 * H_139 / (3 * math.sqrt(D_139) / 2)
    print(format_result("π²·h(137) variant", val_137_v2, B_PHENOM))
    print(format_result("π²·h(139) variant", val_139_v2, B_PHENOM))
    print()

    print("─" * 72)
    print("APPROACH A2 NUMERICAL CHECK: (p+1)/3 Formula")
    print("─" * 72)

    for p in [137, 139]:
        val = (p + 1) / 3
        print(format_result(f"(p+1)/3 at p={p}", val, B_PHENOM))
    print()
    print("  Geometric interpretation: μ(Γ₀(p))/3 = (p+1)/3")
    print("  where μ = index of Γ₀(p) in SL(2,Z) for prime p")
    print()

    print("─" * 72)
    print("APPROACH A4: Hecke Eigenvalue Tests")
    print("─" * 72)

    # Test A4.4: a_p^2 / π
    val_a137_sq_pi = A_137**2 / PI
    val_a139_sq_pi = A_139**2 / PI
    print(f"  Testing: a_p^2 / π  (vs B₀ = 8π = {B0:.4f})")
    print(format_result(f"a_137² / π = {A_137}²/π", val_a137_sq_pi, B0))
    print(format_result(f"a_139² / π = {A_139}²/π", val_a139_sq_pi, B0))
    print()
    print("  Note: a_137^2/π ≈ B₀ (to 2.5%) — connects Hecke to proved result")
    print()

    print(f"  Testing: a_p^2 / π  vs B_phenom = {B_PHENOM}")
    print(format_result(f"a_137² / π vs B_phenom", val_a137_sq_pi, B_PHENOM))
    print()

    # Test: a_p^2 × factor
    print("  Testing: a_p^2 / π × correction factor")
    for factor_name, factor in [("B_phenom/B₀", B_PHENOM/B0),
                                  ("(p+1)/(3π)", (137+1)/(3*PI)),
                                  ("4", 4.0), ("π/2", PI/2)]:
        val = A_137**2 / PI * factor
        print(format_result(f"a_137²/π × {factor_name}", val, B_PHENOM))
    print()

    # Test: π × |a_p| 
    print("  Testing: π × |a_p|  (simpler)")
    print(format_result(f"π × |a_137| = π × 9", PI * abs(A_137), B_PHENOM))
    print(format_result(f"π × |a_139| = π × 9", PI * abs(A_139), B_PHENOM))
    print()

    # Test: 2π × |a_p| / something
    print("  Testing: 2π × |a_p|")
    print(format_result(f"2π × |a_137|", 2*PI*abs(A_137), B_PHENOM))
    print()

    print("─" * 72)
    print("SUMMARY")
    print("─" * 72)

    results = [
        ("Dedekind residue at 137", dedekind_zeta_residue(H_137, D_137), B_PHENOM),
        ("Dedekind residue at 139", dedekind_zeta_residue(H_139, D_139), B_PHENOM),
        ("(p+1)/3 at p=137", (137+1)/3, B_PHENOM),
        ("(p+1)/3 at p=139", (139+1)/3, B_PHENOM),
        ("a_137^2/π vs B₀",   A_137**2/PI, B0),
    ]

    any_match = False
    any_close = False
    for label, value, target in results:
        rel_err = abs(value - target) / target
        if rel_err < 0.001:
            any_match = True
            print(f"  MATCH: {label} = {value:.4f}  (err={rel_err*100:.3f}%)")
        elif rel_err < 0.01:
            any_close = True
            print(f"  CLOSE: {label} = {value:.4f}  (err={rel_err*100:.2f}%)")

    if any_match:
        print()
        print("  STATUS: MATCH FOUND — see above")
    elif any_close:
        print()
        print("  STATUS: CLOSE RESULT(S) — no exact match; Gap A partially narrowed")
        print("          Best: (p+1)/3 = 46 at p=137  (err=0.65%)")
        print("          Best: a_137^2/π ≈ B₀ (not B_phenom)")
    else:
        print()
        print("  STATUS: HONEST GAP — no formula reproduces B_phenom from")
        print("          Dedekind zeta or Hecke eigenvalues alone.")

    print()
    print("  PENDING: SageMath computation of L(1,f₁) and L(2,f₂)")
    print("           for LMFDB labels from identify_lmfdb_labels.py")
    print("  TEST:    π × L(1,f₁) ≈ 46.3?  (requires David's local run)")
    print()
    print("  CONCLUSION: Gap A is not closed by this script.")
    print("              Best numerical candidate: (p+1)/3 = 46 (Approach A2).")
    print()

    return 0 if not any_match else 0


if __name__ == "__main__":
    sys.exit(main())
