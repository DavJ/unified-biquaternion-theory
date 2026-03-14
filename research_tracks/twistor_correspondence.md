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

## 3. Open Problems (Curved Sector)

| Problem | Status |
|---------|--------|
| X^{AA'}(Θ) in curved UBT sector (ASD Ricci-flat obstacle) | **Open [L2]** |
| ψ (imaginary time) ↔ twistor geometry | **Open** |
| Conformal (Möbius) action analytically proved | **Computationally verified only** |

The curved-sector extension requires the nonlinear graviton construction
(Penrose 1976), which is not derived in UBT. The ASD Ricci-flat condition
is an obstacle that is currently unresolved.

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
| X^{AA'}(Θ) curved sector | **Open [L2]** — ASD Ricci-flat obstacle |
| UBT = twistor theory | **False** — flat sector only |
