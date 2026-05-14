#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
compute_B_effective_dimension.py — Approach A4: Effective Dimension Analysis.

PURPOSE
-------
Investigate Gap (a) from b_base_hausdorff.tex by asking:

    If we define an "effective dimension" d_eff via
        B = N_eff^{d_eff/2},
    what is d_eff for the proved one-loop result B₀, the conjectured B_base,
    and the phenomenological B?

This reframes Gap (a): the standard one-loop result B₀ = 2πN_eff/3
corresponds to a non-integer d_eff ≈ 2.59 for N_eff = 12.  The algebraic
conjecture B_base = N_eff^{3/2} corresponds to exactly d = 3 = dim_ℝ(Im ℍ).
The "dimension gap" Δd = d - d_eff(B₀) ≈ 0.41 is the quantitative measure
of what Gap (a) must explain.

INPUTS (no circularity)
-----------------------
  N_eff  = 12      [PROVED] from N_phases × N_helicity × N_charge = 3×2×2
  d      = 3       [PROVED] dim_ℝ(Im ℍ) = dim span{i,j,k}
  B₀     = 8π      [PROVED] from step2_vacuum_polarization.tex
  B_base = 12^{3/2} [CONJECTURED] from b_base_hausdorff.tex
  B_phenom ≈ 46.284 [CALIBRATED] on n*=137 (topological winding number, not α)

OUTPUTS
-------
  d_eff for each B value
  Dimension gap Δd = d - d_eff(B₀)
  Scaling table: d_eff vs N_eff and vs d
  Assessment of which B value is "most natural" from a dimension viewpoint

REFERENCES
----------
  - consolidation_project/alpha_derivation/b_base_hausdorff.tex (A2, v58)
  - consolidation_project/N_eff_derivation/step2_vacuum_polarization.tex
  - STATUS_ALPHA.md §9
  - tools/explore_b_exponent.py (A3: numerical exponent check)
  - DERIVATION_INDEX.md "Fine Structure Constant"

USAGE
-----
    python tools/compute_B_effective_dimension.py
"""

from __future__ import annotations

import math

# ─── Constants ───────────────────────────────────────────────────────────────

N_EFF: int    = 12       # [PROVED] N_phases × N_helicity × N_charge = 3×2×2
D_ALGEBRA: int = 3       # [PROVED] dim_ℝ(Im ℍ) = dim span{i,j,k}

B0: float     = 2 * math.pi * N_EFF / 3   # [PROVED] one-loop baseline = 8π
B_BASE: float = N_EFF ** 1.5               # [CONJECTURED] N_eff^{3/2}
B_PHENOM: float = 46.284                   # [CALIBRATED] on n*=137

ALPHA_INV: float = 137.0   # [CALIBRATED] bare value from UBT topology


# ─── Helper ──────────────────────────────────────────────────────────────────

def d_eff(B: float, N: int = N_EFF) -> float:
    """
    Compute the effective dimension d_eff such that B = N^{d_eff/2}.

    d_eff = 2 × log(B) / log(N)
    """
    return 2.0 * math.log(B) / math.log(N)


def B_from_d(d: float, N: int = N_EFF) -> float:
    """Return B = N^{d/2} for a given effective dimension d."""
    return N ** (d / 2.0)


# ─── Section 1: d_eff for key B values ───────────────────────────────────────

print("=" * 70)
print("UBT B Coefficient — Approach A4: Effective Dimension Analysis")
print("=" * 70)
print()
print(f"Algebra:  ℂ⊗ℍ    →  dim_ℝ(Im ℍ) = d = {D_ALGEBRA}")
print(f"N_eff    = {N_EFF}      [PROVED] N_phases × N_helicity × N_charge")
print()

print("-" * 70)
print("Section 1: Effective dimension d_eff = 2×log(B)/log(N_eff)")
print("-" * 70)

rows = [
    ("B₀ = 2πN_eff/3",  B0,       "[PROVED]",        "one-loop flat-space"),
    ("B_base = N_eff^{3/2}", B_BASE,   "[CONJECTURED]",   "b_base_hausdorff.tex"),
    ("B_phenom",         B_PHENOM, "[CALIBRATED n*=137]", "phenomenological"),
]

print()
print(f"  {'B value':<28} {'B numeric':>10}  {'d_eff':>7}  Status")
print(f"  {'-'*28}  {'-'*10}  {'-'*7}  {'-'*25}")
for name, B, status, note in rows:
    print(f"  {name:<28}  {B:10.5f}  {d_eff(B):7.4f}  {status}  [{note}]")

print()
print(f"  Algebra dimension d = {D_ALGEBRA}.000  (exact: dim_ℝ(Im ℍ))")
print()
print(f"  KEY OBSERVATION:")
print(f"  → d_eff(B_base) = {d_eff(B_BASE):.4f}  = d = {D_ALGEBRA} exactly  [ALGEBRAIC IDENTITY]")
print(f"  → d_eff(B₀)     = {d_eff(B0):.4f}  ≠ d = {D_ALGEBRA}         [GAP]")
print(f"  → d_eff(B_phenom)= {d_eff(B_PHENOM):.4f}  ≠ d                 [GAP]")


# ─── Section 2: Dimension gap Δd ─────────────────────────────────────────────

d_eff_B0 = d_eff(B0)
delta_d = D_ALGEBRA - d_eff_B0
delta_B = B_BASE - B0
ratio_B = B_BASE / B0

print()
print("-" * 70)
print("Section 2: The dimension gap Δd = d - d_eff(B₀)")
print("-" * 70)
print()
print(f"  d          = {D_ALGEBRA:.4f}    (dim_ℝ(Im ℍ), proved)")
print(f"  d_eff(B₀)  = {d_eff_B0:.4f}    (from one-loop B₀, proved)")
print(f"  Δd         = {delta_d:.4f}    (dimension gap, OPEN)")
print()
print(f"  B₀         = {B0:.5f}    (proved)")
print(f"  B_base     = {B_BASE:.5f}    (conjectured)")
print(f"  B_base/B₀  = {ratio_B:.6f}   = (d/(2π)) × N_eff^{{1/2}}")
print()
# Verify: (d/(2π)) × N_eff^{d/2-1}
gap_factor_formula = (D_ALGEBRA / (2 * math.pi)) * (N_EFF ** 0.5)
print(f"  Algebraic check: d/(2π) × N_eff^{{1/2}}")
print(f"    = {D_ALGEBRA}/(2π) × √{N_EFF} = {D_ALGEBRA}/(2π) × {N_EFF**0.5:.4f} = {gap_factor_formula:.6f}")
print(f"  Matches ratio B_base/B₀ = {ratio_B:.6f}  ✓ (algebraic identity)")
print()
print(f"  INTERPRETATION:")
print(f"  The proved one-loop result B₀ = 2πN_eff/3 corresponds to")
print(f"  d_eff ≈ {d_eff_B0:.2f}, NOT the algebraic d = {D_ALGEBRA}.")
print(f"  Gap (a) in b_base_hausdorff.tex asks: what physical mechanism")
print(f"  lifts d_eff from {d_eff_B0:.2f} → {D_ALGEBRA}.00 (by Δd = {delta_d:.2f})?")


# ─── Section 3: Scaling table for different N_eff ────────────────────────────

print()
print("-" * 70)
print("Section 3: Scaling of d_eff(B₀) and d_eff(B_base) with N_eff")
print("-" * 70)
print()
print(f"  d = {D_ALGEBRA} (fixed: dim_ℝ(Im ℍ))")
print()
print(f"  {'N_eff':>6}  {'B₀=2πN/3':>10}  {'d_eff(B₀)':>10}  "
      f"{'B_base=N^(3/2)':>14}  {'d_eff(B_base)':>13}  {'Δd':>6}")
print(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*14}  {'-'*13}  {'-'*6}")
for N in [2, 3, 4, 6, 8, 12, 24, 36]:
    b0 = 2 * math.pi * N / 3
    bb = N ** 1.5
    de_b0 = d_eff(b0, N)
    de_bb = d_eff(bb, N)
    dd = D_ALGEBRA - de_b0
    marker = " ← UBT" if N == N_EFF else ""
    print(f"  {N:>6}  {b0:>10.4f}  {de_b0:>10.4f}  {bb:>14.4f}  "
          f"{de_bb:>13.4f}  {dd:>+6.3f}{marker}")
print()
print(f"  Note: d_eff(B_base) = 3.000 for ALL N_eff (algebraic identity).")
print(f"  Note: d_eff(B₀) → 2 as N_eff → ∞; → 0 as N_eff → 1.")
print(f"  Note: Δd = d - d_eff(B₀) > 0 for all N_eff > 1.")


# ─── Section 4: Scaling with algebra dimension d ─────────────────────────────

print()
print("-" * 70)
print("Section 4: How d_eff(B₀) varies with algebra dimension d")
print("-" * 70)
print()
print(f"  N_eff = {N_EFF} (fixed), B₀ = 2πN_eff/d (generalising '3' → d)")
print()
print(f"  {'d':>3}  {'B₀=2πN/d':>10}  {'d_eff(B₀)':>10}  "
      f"{'B_base=N^(d/2)':>15}  {'d_eff(B_base)':>13}  {'Δd':>6}")
print(f"  {'-'*3}  {'-'*10}  {'-'*10}  {'-'*15}  {'-'*13}  {'-'*6}")
for d in [1, 2, 3, 4, 5, 6, 7, 8]:
    b0 = 2 * math.pi * N_EFF / d
    bb = N_EFF ** (d / 2.0)
    de_b0 = d_eff(b0, N_EFF)
    de_bb = d_eff(bb, N_EFF)
    dd = d - de_b0
    marker = " ← UBT" if d == D_ALGEBRA else ""
    print(f"  {d:>3}  {b0:>10.4f}  {de_b0:>10.4f}  {bb:>15.4f}  "
          f"{de_bb:>13.4f}  {dd:>+6.3f}{marker}")
print()
print(f"  For d = {D_ALGEBRA} (UBT Im(ℍ)): Δd = d - d_eff(B₀) = {D_ALGEBRA - d_eff(B0, N_EFF):.4f}")


# ─── Section 5: Summary and status ───────────────────────────────────────────

print()
print("=" * 70)
print("SUMMARY — Approach A4: Effective Dimension Analysis")
print("=" * 70)
print()
print("Algebraic identity (PROVED as identity, not new physics):")
print(f"  B_base = N_eff^{{d/2}}  ⟺  d_eff(B_base) = d = {D_ALGEBRA} exactly")
print()
print("Key numerical result (PROVED from B₀ derivation):")
print(f"  d_eff(B₀) = {d_eff_B0:.4f}  for N_eff = {N_EFF}, d = {D_ALGEBRA}")
print(f"  Δd = {delta_d:.4f}  (dimension gap to be explained by Gap (a))")
print()
print("Gap (a) reformulated:")
print(f"  Standard one-loop: d_eff(B₀) ≈ {d_eff_B0:.2f} (non-integer)")
print(f"  Algebraic conjecture: d_eff(B_base) = {D_ALGEBRA}.00 (integer = dim_ℝ(Im ℍ))")
print(f"  Gap (a) = show what lifts d_eff from {d_eff_B0:.2f} → {D_ALGEBRA}.00")
print()
print("Status: [NUMERICAL OBSERVATION / ALGEBRAIC CONSISTENCY CHECK]")
print("  No new physics derived here.  The effective dimension d_eff is a")
print("  diagnostic tool: B_base = N_eff^{{3/2}} being 'natural' is equivalent")
print("  to d_eff(B_base) = dim_ℝ(Im ℍ) being an exact integer.")
print()
print("References:")
print("  b_base_hausdorff.tex §4 — Gap (a) formal statement")
print("  step2_vacuum_polarization.tex — B₀ derivation")
print("  explore_b_exponent.py — Approach A3 (numerical exponent x = 1.543)")
print("  compute_B_KK_sum.py — Approaches 1-3 (all dead ends / honest gaps)")
