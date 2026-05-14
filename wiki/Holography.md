<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Holography in UBT

## Physical Spacetime: de Sitter (not AdS)

The physical spacetime M⁴ (Re-sector of biquaternion metric) has Λ > 0 →
de Sitter geometry. This follows directly from GR recovery [L1 Proved] and
observational cosmology.

**Status: Proved [L1]** (follows from GR chain + Λ_obs > 0)
Source: `canonical/gr_limit/GR_limit_of_UBT.tex`

## ψ-Circle: Flat, Not AdS

The compact imaginary direction ψ ~ ψ + 2πR_ψ is a flat circle S¹(R_ψ)
with zero intrinsic curvature. It does NOT generate an AdS factor.

**Status: Proved [L0]** (standard differential geometry)
Source: `research_tracks/research/moduli_space_ads_vs_physical_ds.tex §3`

## Moduli Space: Hyperbolic (AdS-like)

The moduli space of the complex time torus T²(τ) = ℂ/(ℤ+τℤ) is the
upper half-plane ℍ with Poincaré metric (curvature K = −1). This is
mathematically analogous to AdS₂, but it is a parameter space,
NOT physical spacetime.

**Status: Proved [L0]** (standard modular forms theory)
Source: `research_tracks/research/moduli_space_ads_vs_physical_ds.tex §4`

## AdS/CFT Analogy (Informational Encoding)

UBT shares an informational encoding architecture with holographic theories:
Θ dynamics over complex time τ encodes physics observable in real 4D spacetime.
This is a structural analogy, NOT a literal AdS/CFT duality.

**Status: [O] Open Research Direction**
Source: `research_tracks/THEORY_COMPARISONS/ads_cft_like_encoding_in_ubt.md`

## Verlinde / de Sitter Holography

Holographic principle, Verlinde emergent gravity, and dS space connections
to UBT are developed in Appendix N.

**Status: [S] Speculative / Exploratory**
Source: `consolidation_project/appendix_N_holographic_verlinde_desitter.tex`

## Λ_eff from V_eff(Θ) — Investigated (v47)

Computing the effective cosmological constant from the minimum of the UBT
effective potential V_eff(Θ) was investigated in v47.

**V_eff(n*=137) = A·137² − B·137·ln(137) ≈ −12428** (dimensionless winding-sector potential,
A=1, B=46.284 calibrated to place minimum at n*=137).

The direct identification V_eff(n*) = Λ_eff is a **Dead End**: the winding-sector
potential is dimensionless and its value at the minimum differs from the observed
Λ_obs ≈ 10⁻¹²² (Planck units) by many orders of magnitude with no natural unit bridge.
A UV cut-off argument connecting the winding vacuum energy to Λ_eff is not currently
present in the UBT framework.

**Status: [O] Dead End [L2]** (v47 numerical investigation)
See: `DERIVATION_INDEX.md` §Holography and de Sitter Structure
