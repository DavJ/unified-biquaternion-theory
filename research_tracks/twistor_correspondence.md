<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT ↔ Twistor Correspondence: Summary

**Date**: 2026-03-14  
**Hard rule**: UBT is **not** twistor theory. This file summarises the
structural overlap and divergence. Canonical source:
`THEORY_COMPARISONS/penrose_twistor/STATUS.md`.

---

## 1. Exact Common Substructure (Proved [L0])

Both UBT and Penrose twistor theory share a spinor-Hermitian-matrix
representation of flat Minkowski space.

| Result | Status |
|--------|--------|
| σ_μ derived from ℂ⊗ℍ biquaternion basis | **Proved [L0]** |
| det(X) = Minkowski interval for X = x^μ σ_μ | **Proved [L0]** |
| Bijection x ↔ X^{AA'} (flat Minkowski) | **Proved [L0]** |
| Incidence relation ω^A = i X^{AA'} π_{A'} (flat sector only) | **Proved [L0]** |
| Null vectors ↔ rank-1 Hermitian matrices | **Proved [L0]** |
| SU(2,2) Hermitian form preserved | **Proved [L0]** |

Key point: the σ_μ matrices are **derived** from the biquaternion basis
{**1**, **i**, **j**, **k**}; no external import of Pauli matrices is needed.
Scope is **flat Minkowski only** (ψ = 0 slice).

---

## 2. Compatible Sector (Flat Limit)

The UBT fundamental matrix X^{AA'}(Θ) in the flat limit (ψ → 0, real
spacetime) equals the twistor-theoretic x^μ σ_μ. This is **Proved [L0]**
for the scalar sector of the biquaternion field at real time.

---

## 3. Curved Sector Results

| Result | Status |
|--------|--------|
| ASD condition C⁺=0 for Θ ∈ SU(2)₋ (linearised) | ✅ **Proved [L1]** |
| ASD condition C⁺=0 for Θ ∈ SU(2)₋ (non-perturbative) | ✅ **Proved [L1]** |
| Curved twistor space via Penrose nonlinear graviton (SU(2)₋) | ✅ **Proved [L1]** |
| Full Schwarzschild metric from explicit Θ₀ | ✅ **Proved [L1]** |
| X^{AA'}(Θ) for general curved Θ (outside SU(2)₋) | **Open [L2]** |
| ψ (imaginary time) ↔ twistor geometry | **Open** |

For Θ ∈ SU(2)₋ ⊂ ℂ⊗ℍ with vacuum UBT equation ∇†∇Θ = 0:
holonomy ⊂ Sp(1) → C⁺ = 0 (ASD) and R_μν = 0 (Ricci-flat) →
**Penrose nonlinear graviton theorem applies**. UBT has a curved
twistor space description in this sector.
Source: `research_tracks/research/asd_condition_ubt.tex §5`

Note: Schwarzschild metric (Petrov type D) lies outside the SU(2)₋ ASD sector.

---

## 4. Where UBT Diverges from Twistor Theory

- **Complex time τ = t + iψ**: UBT has a dynamical imaginary-time
  coordinate ψ with no counterpart in standard twistor theory.
- **Non-conformal dynamics**: UBT field equations include mass terms and
  a running α; twistor theory is most natural for conformally invariant
  (massless) fields.
- **Standard Model gauge group**: UBT derives SU(3)×SU(2)×U(1) from
  ℂ⊗ℍ independently; this derivation does not pass through SU(2,2).

---

## 5. Classification Summary

| Sector | Status |
|--------|--------|
| σ_μ from ℂ⊗ℍ; bijection x↔X; incidence (flat) | **Proved [L0]** |
| X^{AA'}(Θ) flat limit = x^μ σ_μ | **Proved [L0]** |
| ASD condition C⁺=0 for Θ ∈ SU(2)₋ (non-perturbative) | **Proved [L1]** |
| Curved twistor space via Penrose nonlinear graviton (SU(2)₋) | **Proved [L1]** |
| X^{AA'}(Θ) curved sector (general Θ, outside SU(2)₋) | **Open [L2]** |
| UBT = twistor theory | **False** — flat sector and SU(2)₋ instanton sector only |
