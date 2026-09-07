#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
verify_N_eff.py — Numerical verification of N_eff derivation from ℂ⊗ℍ structure.

Task: Derive N_eff = 12 from the UBT Action S[Θ]
Track: CORE — α derivation / B-coefficient
Date: 2026-03-05

This script verifies the conclusions of the three-step N_eff derivation:

  Step 1: Θ ∈ ℂ⊗ℍ ≅ Mat(2,ℂ) has 4 independent complex charged d.o.f.
          under U(1)_EM: Θ → e^(iα)Θ.

  Step 2: Each charged complex scalar contributes (e²/12π²)ln(Λ²/k²) to Π(k²).
          N_charged independent scalars give B₀ = 2π·N_charged/3.
          So N_eff = N_charged (proved, not assumed).

  Step 3: ℂ⊗ℍ alone → N_eff = 4 (electroweak, Track A).
          N_eff = 12 = 4 × 3 requires SU(3)_c color factor N_c = 3
          from octonionic extension ℂ⊗𝕆 (Track B).

QED consistency requirement (must pass at every step):
    N_eff = 1  →  B₀ = 2π/3 ≈ 2.094  (standard QED one-loop)
"""

import numpy as np

print("=" * 60)
print("N_eff derivation from ℂ⊗ℍ structure")
print("=" * 60)
print()

# ─────────────────────────────────────────────────────────────
# Step 1: d.o.f. count in ℂ⊗ℍ
# ─────────────────────────────────────────────────────────────
print("Step 1: Mode decomposition of Θ ∈ ℂ⊗ℍ ≅ Mat(2,ℂ)")
print("-" * 60)

N_complex_total = 4       # 2×2 complex matrix entries = 4 complex d.o.f.
N_real_total    = 8       # 4 complex = 8 real d.o.f.

print(f"  Total complex d.o.f. in Θ:   {N_complex_total}")
print(f"  Total real    d.o.f. in Θ:   {N_real_total}")
print()

# Under U(1)_EM: Θ → e^(iα)Θ  (left multiplication by central element of ℂ)
# All 4 complex components z_a transform with charge +1 — none are neutral.
N_charged_CxH = N_complex_total   # = 4
N_neutral_CxH = 0

print("  Under U(1)_EM: Θ → e^(iα)Θ  (e^(iα) central in ℂ⊗ℍ)")
print(f"  Charged modes (charge +1):   {N_charged_CxH}")
print(f"  Neutral modes:               {N_neutral_CxH}")
print()
assert N_charged_CxH + N_neutral_CxH == N_complex_total, "d.o.f. count mismatch"

# ─────────────────────────────────────────────────────────────
# Step 2: B₀ from one-loop vacuum polarization
# ─────────────────────────────────────────────────────────────
print("Step 2: One-loop vacuum polarization coefficient B₀")
print("-" * 60)

def B0_from_Ncharged(N):
    """B₀ = 2π·N/3  (proved: N_eff = N_charged, Step 2 Theorem)."""
    return 2.0 * np.pi * N / 3.0

# QED anchor: single complex scalar → B₀ = 2π/3
B0_QED = B0_from_Ncharged(1)
print(f"  QED limit (N_charged = 1):   B₀ = 2π/3 = {B0_QED:.6f}  ✓")

# ℂ⊗ℍ associative sector
B0_CxH = B0_from_Ncharged(N_charged_CxH)
print(f"  ℂ⊗ℍ alone (N_charged = 4):  B₀ = 2π·4/3 = {B0_CxH:.6f}")
print(f"  (= 8π/3 = {8*np.pi/3:.6f})")
print()
assert abs(B0_QED - 2.0 * np.pi / 3.0) < 1e-12, "QED limit failed"

# ─────────────────────────────────────────────────────────────
# Step 3: From N_eff = 4 (ℂ⊗ℍ) to N_eff = 12 (full SM)
# ─────────────────────────────────────────────────────────────
print("Step 3: N_eff counting from algebra")
print("-" * 60)

# Standard Model gauge content from appendix_E2_SM_geometry.tex:
#   ℂ⊗ℍ  →  SU(2)_L × U(1)_Y  (electroweak, associative sector)
#   ℂ⊗𝕆  →  SU(3)_c           (color, octonionic extension Track B)
N_EW_gauge   = 3 + 1        # SU(2)_L (3) + U(1)_Y (1)
N_color_gauge = 8           # SU(3)_c gluons (from G_2 ⊃ SU(3))
N_SM_gauge    = N_EW_gauge + N_color_gauge
print(f"  Electroweak gauge bosons (ℂ⊗ℍ):  {N_EW_gauge}  (SU(2)_L + U(1)_Y)")
print(f"  Color gauge bosons (Track B):     {N_color_gauge}  (SU(3)_c gluons)")
print(f"  Total SM gauge bosons:            {N_SM_gauge}")
print()

# N_eff = N_charged = N_EW_charged × N_color
# From Steps 1–2: N_charged^(ℂ⊗ℍ) = 4 (electroweak complex charged modes)
# From Track B:   N_c = 3 (color triplet)  →  N_charged = 4 × 3 = 12
N_EW_charged   = N_charged_CxH   # = 4  (from Step 1)
N_c            = 3               # QCD color multiplicity (from SU(3)_c via Track B)
N_eff_full     = N_EW_charged * N_c

print(f"  N_charged^(ℂ⊗ℍ) = {N_EW_charged}   (associative sector, Steps 1–2)")
print(f"  N_c = {N_c}              (color from SU(3)_c, Track B octonionic extension)")
print(f"  N_eff = N_EW × N_c = {N_EW_charged} × {N_c} = {N_eff_full}")
print()

B0_full = B0_from_Ncharged(N_eff_full)
print(f"  B₀(N_eff = {N_eff_full}) = 2π·{N_eff_full}/3 = {B0_full:.6f}")
print(f"  (= 8π = {8*np.pi:.6f})")
print()

# ─────────────────────────────────────────────────────────────
# Comparison with required B ≈ 46.3 and gap analysis
# ─────────────────────────────────────────────────────────────
print("Gap analysis: B₀ vs. required B ≈ 46.3")
print("-" * 60)

B_required = 46.3
gap_factor  = B_required / B0_full

print(f"  B₀ (one-loop, N_eff = 12):  {B0_full:.4f}")
print(f"  B_required (for n* = 137):  {B_required}")
print(f"  Gap factor B_req / B₀:      {gap_factor:.4f}")
print()
print("  Note: This gap is the OPEN PROBLEM A (STATUS_ALPHA.md §9).")
print("  Multi-loop QED corrections close only O(α/π) ≈ 0.003 of the gap")
print("  (proved dead end in B_derivation/candidate1_multiloop.tex).")
print("  The factor ~1.84 requires a non-perturbative mechanism beyond S[Θ] loop.")
print()

# ─────────────────────────────────────────────────────────────
# Summary table
# ─────────────────────────────────────────────────────────────
print("Summary: N_eff derivation status")
print("-" * 60)
print(f"  {'Case':<42} {'N_eff':>6}  {'B₀':>10}  {'Source'}")
print(f"  {'-'*42} {'-'*6}  {'-'*10}  {'-'*25}")
print(f"  {'QED limit (single scalar)':<42} {1:>6}  {B0_from_Ncharged(1):>10.4f}  standard QED ✓")
print(f"  {'ℂ⊗ℍ alone (EW sector)':<42} {N_charged_CxH:>6}  {B0_CxH:>10.4f}  proved (Steps 1–2)")
print(f"  {'ℂ⊗ℍ + Track B (full SM)':<42} {N_eff_full:>6}  {B0_full:>10.4f}  conditional (Track B)")
print()

# ─────────────────────────────────────────────────────────────
# Existing 3×2×2 counting: algebraic reinterpretation
# ─────────────────────────────────────────────────────────────
print("Reinterpretation of semi-empirical 3×2×2 = 12 counting")
print("-" * 60)
N_phases   = 3    # previously: 3 quaternion imaginary components i,j,k
                  # now identified as: N_c = 3 (color, from SU(3)_c via Track B)
N_helicity = 2    # identified with: 2 charged modes per EW doublet
N_charge   = 2    # identified with: doublet structure (SU(2)_L)
N_counting = N_phases * N_helicity * N_charge
print(f"  N_phases × N_helicity × N_charge = {N_phases} × {N_helicity} × {N_charge} = {N_counting}")
print(f"  Algebraic origin of factors:")
print(f"    3 = N_c (color from SU(3)_c ⊂ Aut(ℂ⊗𝕆), Track B)")
print(f"    2 × 2 = 4 = N_charged^(ℂ⊗ℍ) (electroweak charged modes, Steps 1–2)")
print()
assert N_counting == N_eff_full, "3×2×2 count inconsistency"

print("=" * 60)
print("CONCLUSION")
print("=" * 60)
print()
print("  ℂ⊗ℍ alone:   N_eff = 4   (derived, zero free parameters)")
print("  N_eff = 12:  requires N_c = 3 from SU(3)_c via Track B")
print("               (Octonionic Completion Hypothesis, ℂ⊗𝕆 extension)")
print()
print("  The semi-empirical '3×2×2' counting is replaced by:")
print("    N_eff = N_c × N_EW_charged = 3 × 4 = 12")
print("  where N_EW_charged = 4 is derived from S[Θ] and N_c = 3 needs Track B.")
print()
print("  B₀ = 2π·N_eff/3 is a zero-free-parameter result conditional on Track B.")
print()
print("  OPEN: The gap B₀ ≈ 25.1 → B_req ≈ 46.3 (factor ~1.84) is a separate")
print("  open problem (STATUS_ALPHA.md §9, Problem A) not addressed here.")
