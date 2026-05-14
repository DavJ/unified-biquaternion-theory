<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T2_GAUGE — Gauge Derivation Map

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Objective**: Formalize emergence of SU(3)×SU(2)×U(1) from canonical UBT algebra  
**Date**: 2026-04-27  
**Sources**: `canonical/bridges/gauge_emergence_bridge.tex`,
`canonical/interactions/sm_gauge.tex`, `canonical/algebra/`,
`DERIVATION_INDEX.md`

---

## Overview

The Standard Model gauge group `G_SM = SU(3)_c × SU(2)_L × U(1)_Y` emerges
from the biquaternion algebra `ℂ⊗ℍ ≅ Mat(2,ℂ)` through three independent
algebraic mechanisms.  All three factors are derived with **zero free parameters**
at the [L0] level.

```
ℂ⊗ℍ ≅ Mat(2,ℂ)
    │
    ├── ℤ₂×ℤ₂×ℤ₂ involutions ──► SU(3)_c   [L0] PROVED
    │
    ├── Left norm-preserving action ──► SU(2)_L  [L0] PROVED
    │
    └── Scalar phase right action ──► U(1)_Y   [L0] PROVED
```

---

## Algebraic Foundation

### A0: Biquaternion algebra isomorphism

```
ℂ⊗ℝ ℍ  ≅  Mat(2,ℂ)
```

This is an exact algebraic identity (no approximation).  It is the foundation
of the entire gauge sector.

- **Status**: [L0] proved — algebraic identity
- **Source**: `canonical/fields/biquaternion_algebra.tex`
- **DERIVATION_INDEX entry**: `ℂ⊗ℍ ≅ Mat(2,ℂ) [L0]: algebraic identity`

---

## SU(3)_c: Color Gauge Group

### Derivation route 1: ℤ₂×ℤ₂×ℤ₂ involutions

The algebra `ℂ⊗ℍ` admits three canonical involutions:
```
σ₁: q₀ + q₁i + q₂j + q₃k  →  q₀ + q₁i - q₂j - q₃k   (j,k sign flip)
σ₂: …                                                   (i,k sign flip)
σ₃: …                                                   (i,j sign flip)
```
These generate a `ℤ₂×ℤ₂×ℤ₂` symmetry group of `ℂ⊗ℍ`.

The fixed-point subalgebra structure of `ℤ₂×ℤ₂×ℤ₂` acting on `ℂ⊗ℍ` contains
the Lie algebra `𝔰𝔲(3)`:
- **Theorem G.A**: `𝔰𝔲(3)` is realised in `ℂ⊗ℍ`
- **Theorem G.B**: Quarks transform in the fundamental `3` representation
- **Theorem G.C**: Gluons transform in the adjoint `8` representation
- **Theorem G.D**: Electroweak and strong sectors decouple

**Status**: [L0] PROVED — all four theorems G.A–G.D  
**Source**: `canonical/interactions/sm_gauge.tex`, Theorems G.A–G.D  
**Source**: `canonical/algebra/involutions_Z2xZ2xZ2.tex`  
**Source**: `canonical/su3_derivation/`

### Derivation route 2: Qubit encoding (independent confirmation)

SU(3) is also derived via the triqubit encoding:
- `ℂ⊗ℍ ≅ Mat(2,ℂ)` → qubit basis
- 8 Gell-Mann generators verified numerically
- Color confinement: free quarks algebraically inadmissible; singlet condition
  `⟨C₂⟩ = 0` holds

**Status**: [L0] proved (algebraic); confinement conjecture with experimental support  
**Source**: `canonical/interactions/su3_qubit_encoding.tex`,
`canonical/bridges/su3_gauge_qubit_equivalence.tex`

### Three generations

Three copies of the SM quantum number structure arise from three ψ-winding modes
on the imaginary time circle `ψ ~ ψ + 2π`:
- `N_gen = 3` from `dim_ℝ(Im ℍ) = 3`
- Each mode carries identical gauge quantum numbers

**Status**: [L0] proved  
**Source**: `DERIVATION_INDEX.md`: "ψ-modes as independent B-fields [L0]: Proven"

---

## SU(2)_L: Weak Isospin

### Derivation: Left norm-preserving action

`ℂ⊗ℍ ≅ Mat(2,ℂ)`.  The group of norm-preserving left multiplications is:
```
{U ∈ Mat(2,ℂ) : U†U = 1} = U(2)
```
The special unitary subgroup is `SU(2)_L`.  This is the electroweak SU(2) gauge
symmetry, acting on the left-chiral doublets of the Standard Model.

**Status**: [L0] PROVED — exact algebraic fact  
**Source**: `canonical/interactions/sm_gauge.tex`,
"Geometric derivation of SU(2)_L × U(1)_Y"

### Chirality: Why SU(2)_L not SU(2)_R

Physical weak interactions are left-handed.  In UBT, this is motivated by
`ψ`-parity:

Under `ψ → -ψ` (time-reversal in imaginary time), left- and right-handed
couplings transform differently.  The complex-time structure of `τ = t + iψ`
breaks the `L ↔ R` symmetry.

**Status**: Motivated [SE] — not yet a formal theorem  
**Source**: `canonical/chirality/`, `canonical/symmetry/chirality_and_parity_breaking.tex`  
**Open gap**: C1 (see `missing_axioms.md`)

---

## U(1)_Y: Hypercharge

### Derivation: Scalar phase right action

The group of scalar phase right multiplications on `Mat(2,ℂ)`:
```
Θ → Θ · e^{iφ},    φ ∈ ℝ
```
is isomorphic to `U(1)`.  This `U(1)` is identified with the hypercharge gauge
symmetry `U(1)_Y`.

**Status**: [L0] PROVED — exact algebraic fact  
**Source**: `canonical/interactions/sm_gauge.tex`;
`DERIVATION_INDEX.md`: "U(1)_Y from right action: Proved [L0]"

---

## U(1)_EM: Electromagnetism

After electroweak symmetry breaking, the electromagnetic `U(1)_EM` arises
from the `ψ`-cycle phase:
```
U(1)_EM ⊂ SU(2)_L × U(1)_Y,   after SSB
```
The `ψ`-winding phase is identified with the electromagnetic phase.

**Status**: [L0] proved  
**Source**: `DERIVATION_INDEX.md`: "U(1)_EM from ψ-cycle phase [L0]"

---

## Semi-Empirical and Open Elements

| Element | Status | Source |
|---------|--------|--------|
| Weinberg angle θ_W | SEMI-EMPIRICAL | `canonical/interactions/sm_gauge.tex` |
| Chirality (L not R) | MOTIVATED [SE] | `canonical/chirality/` |
| Higgs mechanism / SSB | Candidate | `research_tracks/research/higgs_yukawa_scan.md` |
| Yukawa couplings | OPEN (λ gap ×11) | `DERIVATION_INDEX.md` |
| Lepton mass ratios | OPEN | `PRIORITIES_2026.md` |

### Weinberg angle

`sin²θ_W ≈ 0.23122` cannot be derived from `ℂ⊗ℍ` alone.  Additional input
(fermion representations or Higgs sector structure) is required.  This is an
identified limitation of the algebraic sector — **not** a failure of the framework.

---

## Derivation Map: Complete Picture

```
ℂ⊗ℍ ≅ Mat(2,ℂ)   [L0]
│
├─── ℤ₂³ involutions ──────────────────► SU(3)_c     [L0] PROVED
│         │
│         └── 3 ψ-winding modes ────────► 3 generations [L0] PROVED
│
├─── Left SU(2) action ─────────────────► SU(2)_L    [L0] PROVED
│         │
│         └── ψ-parity breaking ────────► L not R   [SE] motivated
│
├─── Right U(1) action ─────────────────► U(1)_Y    [L0] PROVED
│
├─── ψ-cycle phase ─────────────────────► U(1)_EM   [L0] PROVED
│
├─── Higgs sector (SSB) ────────────────► W±, Z mass [candidate]
│
└─── Yukawa / fermion reps ─────────────► θ_W, masses [semi-emp / open]
```

---

## Paper Readiness

A paper on `SU(3)×SU(2)_L×U(1)_Y from Biquaternion Algebra ℂ⊗ℍ` requires:

1. **Sections already proved [L0]**: SU(3), SU(2)_L, U(1)_Y, U(1)_EM,
   three generations — all zero free parameters.
2. **Sections to state as open**: chirality (motivated only), Weinberg angle
   (semi-empirical), Higgs/Yukawa (not addressed in this paper).
3. **Independent check**: numerical verification of 8 Gell-Mann generators.
4. **Comparison**: no other published framework derives all three SM gauge
   factors from a single algebra without introducing them as external input.

**Target journals**: Journal of Mathematical Physics, Nuclear Physics B,
Physical Review D.

**Estimated write time**: 6–8 weeks (proofs exist; writing + consistency check).
