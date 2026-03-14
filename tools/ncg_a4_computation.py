# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# NCG a₄ computation for the UBT spectral triple (A = ℂ⊗ℍ, H = ℂ⁴, D)
#
# Background (b_base_ncg_a4.tex / b_base_new_directions.tex §6):
#   Approach F1: A = ℂ⊗ℍ ≅ Mat(2,ℂ), H_F = ℂ⁴ (adjoint / left-regular rep).
#   If a₄(D) = N_eff^{3/2} = 41.57 then B_base is proved [L1] → upgrade.
#   If not → Dead End for this NCG route; document precisely.
#
# The Seeley–DeWitt coefficient a₄ (also written A₄ or a₄(1,D)) is:
#   a₄ = (1/16π²) Tr[a·(E² + R/6)] + gauge terms
# For flat space with zero scalar curvature (R=0) and a=1:
#   a₄^{gauge} = (1/16π²) · (1/3) · Tr_H[F_μν F^μν]
# where F_μν = [∇_μ, ∇_ν] is the curvature of the connection on H_F.
#
# For the adjoint representation of Mat(2,ℂ) acting on H_F = ℂ⁴:
#   Tr_H[F²] = dim(H_F) · Tr_{adj}[F²] / dim(adj) (schematically)
# We compute the ratio [a₄]_{ℂ⁴} / [a₄]_{ℂ²} and the resulting B estimate.

import math

# -----------------------------------------------------------------------
# Algebraic constants from ℂ⊗ℍ ≅ Mat(2,ℂ)
# -----------------------------------------------------------------------
dim_H_f = 4          # dim_ℂ(H_F) = dim of adjoint / left-regular rep of Mat(2,ℂ)
dim_H_fundamental = 2  # dim_ℂ of the fundamental (defining) rep of Mat(2,ℂ)
N_eff = 12           # from Theorem 1.4 in canonical/n_eff/ (N_phases×N_helicity×N_charge = 3×2×2)
B_base_target = N_eff ** 1.5  # = 12^{3/2} ≈ 41.569

# -----------------------------------------------------------------------
# a₄ ratio: adjoint (ℂ⁴) vs fundamental (ℂ²)
# For Mat(2,ℂ), the adjoint representation on itself has dim 4.
# The ratio a₄[adj]/a₄[fund] = dim(adj)/dim(fund) for the gauge trace,
# giving ratio = dim_H_f / dim_H_fundamental = 4/2 = 2.
# (cf. b_base_ncg_a4.tex F1: ratio = 4; note that F1 uses a different
# normalisation — here we use the standard Connes convention for a₄.)
# -----------------------------------------------------------------------
a4_ratio = dim_H_f / dim_H_fundamental  # = 2 (Connes normalisation)
a4_ratio_f1 = 4  # F1 convention (as in b_base_ncg_a4.tex)

# -----------------------------------------------------------------------
# B estimate from a₄ (approach F1, b_base_ncg_a4.tex)
# B_F1 = a4_ratio_f1 * B₀  where B₀ = 2π·N_eff/3 = 8π ≈ 25.13
# -----------------------------------------------------------------------
B0 = 2 * math.pi * N_eff / 3  # one-loop baseline (canonical/n_eff/step2_vacuum_polarization.tex)
B_F1 = a4_ratio_f1 * B0

# -----------------------------------------------------------------------
# NCG a₄ via spectral action for H_F = ℂ⁴
# The spectral action coefficient for a₄ on a d=4 Riemannian manifold:
#   a₄ = (1/16π²) ∫ Tr_H[(R/6)² - R_μν²/2 + R_μνρσ²/20 + (F_μν)²/2 + ...]
# On flat ℝ⁴ (R=0, R_μν=0, R_μνρσ=0):
#   a₄^{flat} = (1/16π²) · (1/2) · Tr_H[F_μν F^μν]
# For H_F = ℂ⁴ in adjoint rep of SU(2) ⊂ Mat(2,ℂ):
#   tr_{adj}[T^a T^b] = 2δ^{ab} (standard normalisation, adjoint of SU(2))
#   Tr_H[F²] = Tr_{ℂ⁴}[F²] = 4 · (dimension weight)
# Ratio vs fundamental (ℂ²): Tr_{adj}[T^a T^b] / Tr_{fund}[T^a T^b] = 4 (for SU(2))
# This gives a₄[ℂ⁴] / a₄[ℂ²] = 4, consistent with F1.
# -----------------------------------------------------------------------
Tr_adj_over_fund = 4  # Dynkin index ratio: I(adj)/I(fund) = 2C_adj/1 = 4 for SU(2)

# B from a₄ spectral action (F4 approach: use a₄ as B directly)
# If a₄ = B_base directly (as in F4 motivated conjecture):
# Unique exact candidate: [dim_ℝ(ℍ) × dim_ℝ(Im ℍ)]^{3/2} = (4×3)^{3/2} = 41.57
dim_R_H = 4   # dim_ℝ(ℍ)
dim_R_ImH = 3  # dim_ℝ(Im ℍ) = N_phases
B_F4_candidate = (dim_R_H * dim_R_ImH) ** 1.5

# -----------------------------------------------------------------------
# Result summary
# -----------------------------------------------------------------------
print("=" * 60)
print("NCG a₄ computation for UBT spectral triple (A=ℂ⊗ℍ, H=ℂ⁴, D)")
print("=" * 60)
print()
print(f"  N_eff              = {N_eff}")
print(f"  B_base target      = N_eff^(3/2) = {B_base_target:.4f}")
print(f"  B₀ (one-loop base) = 2π·N_eff/3  = {B0:.4f}")
print()
print("--- Approach F1 (b_base_ncg_a4.tex) ---")
print(f"  a₄ ratio [ℂ⁴]/[ℂ²] = {a4_ratio_f1} (F1 convention)")
print(f"  B_F1 = a4_ratio × B₀ = {B_F1:.4f}")
print(f"  B_F1 / B_base_target = {B_F1/B_base_target:.4f}")
print(f"  → B_F1 ≈ {B_F1/B_base_target:.2f} × B_base  [NOT EQUAL → F1 is DEAD END]")
print()
print("--- Approach F4 (spectral invariant search) ---")
print(f"  [dim_ℝ(ℍ) × dim_ℝ(Im ℍ)]^(3/2) = ({dim_R_H}×{dim_R_ImH})^(3/2)")
print(f"  = {B_F4_candidate:.4f}")
print(f"  vs B_base_target = {B_base_target:.4f}")
print(f"  Match: {'EXACT' if abs(B_F4_candidate - B_base_target) < 1e-6 else 'NO'}")
print(f"  Note: This is an algebraic identity — restatement of N_eff=12 + exponent 3/2")
print(f"        No new derivation of 3/2 exponent. Gap (a) remains OPEN.")
print()
print("--- Conclusion ---")
print(f"  a₄[ℂ⁴] ≠ B_base via standard spectral action (F1 Dead End)")
print(f"  F4 candidate matches exactly but is algebraically equivalent to Hausdorff approach")
print(f"  Explicit a₄ = Tr(D⁴)/16π² for UBT Dirac operator not computed")
print(f"  → Status: PARTIAL (F4 algebraic coincidence noted; ab initio gap remains OPEN)")
print()
print("  DERIVATION_INDEX update: no upgrade; B_base remains Partially Proved [L1]")

# -----------------------------------------------------------------------
# Numerical cross-check: B_base formula
# -----------------------------------------------------------------------
assert abs(B_base_target - 12 * math.sqrt(12)) < 1e-9, "B_base formula mismatch"
assert abs(B_F4_candidate - B_base_target) < 1e-9, "F4 candidate mismatch"
print()
print("[OK] All numerical assertions passed.")
