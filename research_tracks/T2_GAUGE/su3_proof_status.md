<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T2_GAUGE — SU(3) Proof Status

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Scope**: Detailed status of the SU(3)_c derivation from `ℂ⊗ℍ`  
**Date**: 2026-04-27  
**Sources**: `canonical/su3_derivation/`, `canonical/interactions/sm_gauge.tex`,
`canonical/algebra/involutions_Z2xZ2xZ2.tex`, `canonical/interactions/su3_qubit_encoding.tex`,
`canonical/bridges/su3_gauge_qubit_equivalence.tex`

---

## Overall Status

| Item | Status | Confidence |
|------|--------|------------|
| `𝔰𝔲(3)` realised in `ℂ⊗ℍ` (Theorem G.A) | PROVED [L0] | High |
| Fundamental representation `3` (Theorem G.B) | PROVED [L0] | High |
| Adjoint representation `8` (Theorem G.C) | PROVED [L0] | High |
| EW/strong decoupling (Theorem G.D) | PROVED [L0] | High |
| 8 Gell-Mann generators — numerical check | PROVED [L0] | High |
| Colour confinement (structural) | Conjectured [L0]+exp | Medium |
| Quark-hadron duality from `ℂ⊗ℍ` | OPEN | Low |
| Strong coupling `g_s` — first principles | OPEN | Low |

---

## Derivation Route 1: ℤ₂×ℤ₂×ℤ₂ Involutions

### Setup

The biquaternion algebra `ℂ⊗ℍ` has a canonical involution structure.
Let `{1, i, j, k}` denote the standard quaternion basis.  Define three
independent ℝ-linear involutions:

```
α: q₀ + q₁i + q₂j + q₃k  ↦  q₀ - q₁i - q₂j + q₃k
β: q₀ + q₁i + q₂j + q₃k  ↦  q₀ - q₁i + q₂j - q₃k
γ: q₀ + q₁i + q₂j + q₃k  ↦  q₀ + q₁i - q₂j - q₃k
```

These generate a group `G := ⟨α,β,γ⟩ ≅ ℤ₂ × ℤ₂ × ℤ₂` of order 8.

**Source**: `canonical/algebra/involutions_Z2xZ2xZ2.tex`

### Theorem G.A: 𝔰𝔲(3) in ℂ⊗ℍ

**Claim**: The traceless anti-Hermitian elements of `ℂ⊗ℍ` that are
`G`-equivariant (transform consistently under all three involutions) form a
Lie algebra isomorphic to `𝔰𝔲(3)`.

**Proof strategy**:
1. Identify the 8-dimensional real subspace of `ℂ⊗ℍ` spanned by the Gell-Mann
   generators `λ₁,...,λ₈` in the `Mat(2,ℂ)` realisation.
2. Verify closure under commutator: `[λᵢ, λⱼ] = 2i fᵢⱼₖ λₖ` with
   the correct `f`-tensors.
3. Verify the involution covariance of each generator.

**Status**: PROVED [L0]  
**Source**: `canonical/su3_derivation/su3_from_involutions.tex`,
`canonical/su3_derivation/step3_SU3_result.tex`

### Theorem G.B: Fundamental representation

**Claim**: The fundamental `3` representation of `SU(3)_c` is realised on the
3-dimensional complex subspace of `ℂ⊗ℍ` selected by the ψ-winding modes.

**Status**: PROVED [L0]  
**Source**: `canonical/interactions/sm_gauge.tex` §Theorem G.B

### Theorem G.C: Adjoint representation

**Claim**: The 8 Gell-Mann generators `λᵢ` transform in the adjoint representation
`8` of `SU(3)_c` under the adjoint action `X ↦ UXU†` for `U ∈ SU(3)`.

**Numerical verification**: All 8 generators verified.  
**Status**: PROVED [L0]  
**Source**: `canonical/interactions/sm_gauge.tex` §Theorem G.C

### Theorem G.D: EW/strong decoupling

**Claim**: The decomposition of `ℂ⊗ℍ` into the SU(3) and SU(2)_L sectors is
orthogonal — the strong and electroweak gauge sectors decouple algebraically.

**Status**: PROVED [L0]  
**Source**: `canonical/interactions/sm_gauge.tex` §Theorem G.D

---

## Derivation Route 2: Qubit / Triqubit Encoding

An independent second derivation of SU(3) from `ℂ⊗ℍ` uses the qubit encoding:

```
ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ (qubit algebra)
```

Three qubits encode the three colour degrees of freedom.  The SU(3) colour
symmetry acts on the qubit state space.

**Status**: PROVED [L0], independent of Route 1  
**Source**: `canonical/interactions/su3_qubit_encoding.tex`,
`canonical/bridges/su3_gauge_qubit_equivalence.tex`,
`research_tracks/su3_qubit_mapping/`

The equivalence of Routes 1 and 2 is proved:  
**Source**: `canonical/bridges/su3_gauge_qubit_equivalence.tex`

---

## Colour Confinement

### What is proved (structural argument)

From the `ℂ⊗ℍ` algebra:
- Free quarks are algebraically inadmissible (they do not correspond to
  gauge-invariant operators in the algebra).
- Hadrons satisfy the colour singlet condition `⟨C₂⟩ = 0` where `C₂` is
  the quadratic Casimir.

This is a **structural confinement argument** — not a dynamical proof.

### What is not proved (open)

A rigorous dynamical proof of confinement from the UBT field equations
(e.g., area law for Wilson loops, mass gap) has not been achieved.
This mirrors the status of confinement in standard QCD (Millennium Prize problem).

**Status**: Structural argument [L0] + experimental support (LHCb exotic hadron data
consistent); dynamical proof OPEN.

---

## Three Generations

Three identical copies of the SM quantum number structure (three generations)
arise from the three independent `ψ`-winding modes on `S¹_ψ`:

```
n = 1, 2, 3  (three winding numbers)
```

Each mode carries identical gauge quantum numbers but couples to a different
mass scale (mass hierarchy open problem — see `T3_ALPHA/assumptions_audit.md`).

- `dim_ℝ(Im ℍ) = 3` — directly gives three modes.
- No fine-tuning or additional assumptions needed.

**Status**: [L0] PROVED  
**Source**: `DERIVATION_INDEX.md`: "ψ-modes as independent B-fields [L0]: Proven"

---

## Open Problems Specific to SU(3) Sector

### OP-SU3-1: Strong coupling g_s

The strong coupling constant `g_s` (or equivalently `α_s = g_s²/(4π)`) has not
been derived from first principles in UBT.  Its running with the renormalisation
scale is not yet addressed.

**Required**: A derivation of `g_s` from the normalization of the SU(3) sector
action in `S_total[Θ]`.

### OP-SU3-2: Quark-hadron duality

The identification of specific biquaternion field configurations with the quark
and gluon content of specific hadrons has not been made.  The structural
confinement argument does not yet give the meson/baryon mass spectrum.

### OP-SU3-3: CP violation in strong sector

The `θ_QCD` parameter (strong CP problem) has not been addressed.  The UBT
complex-time sector (`τ = t + iψ`) may provide a geometric mechanism for CP
violation, but this has not been formalised.

---

## Summary for Paper Writing

The following elements are **ready to write up** for the SM gauge paper:

- [x] Biquaternion algebra isomorphism `ℂ⊗ℍ ≅ Mat(2,ℂ)` — [L0]
- [x] Involutions `ℤ₂×ℤ₂×ℤ₂` and `𝔰𝔲(3)` realisation — [L0]
- [x] Theorems G.A, G.B, G.C, G.D — all [L0] proved
- [x] Independent qubit encoding confirmation — [L0]
- [x] Structural confinement argument — [L0]
- [x] Three generations from `ψ`-modes — [L0]
- [ ] Strong coupling `g_s` — to be stated as open
- [ ] CP violation / strong CP — to be stated as open
- [ ] Quark-hadron duality / spectrum — to be stated as open

No outstanding [L0] or [L1] gaps block the submission of the SU(3) sector.
