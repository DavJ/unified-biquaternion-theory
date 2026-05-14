<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T2_GAUGE — Missing Axioms and Open Gaps

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Scope**: Inventory of axioms that are assumed (not derived) in the gauge sector,
and open gaps that must be addressed before a complete first-principles SM derivation  
**Date**: 2026-04-27  
**Sources**: `canonical/bridges/gauge_emergence_bridge.tex`,
`canonical/THEORY/axioms/core_assumptions.tex`, `DERIVATION_INDEX.md`,
`PRIORITIES_2026.md`

---

## Classification

| Type | Meaning |
|------|---------|
| **AXIOM** | Postulated input — used but not derived from more fundamental structure |
| **MOTIVATED** | Justified by physical/algebraic reasoning but not proved as theorem |
| **OPEN HARD** | Important derivation that has resisted many approaches |
| **OPEN** | Missing piece with a plausible path to proof |
| **SEMI-EMPIRICAL** | Value or relation fixed by experiment, not predicted |

---

## Core Axioms (Used in Gauge Sector)

### AXIOM-A: Fundamental algebra is ℂ⊗ℍ

**Statement**: The fundamental algebraic structure of UBT is the biquaternion
algebra `ℂ⊗ℍ`.

**Status**: AXIOM — foundational postulate of UBT  
**Justification**: `ℂ⊗ℍ ≅ Mat(2,ℂ)` is the minimal algebra that contains both
complex structure (for quantum phases) and quaternionic structure (for spinors
and 4D Lorentzian geometry).  It is uniquely determined by these requirements up
to isomorphism among the normed division algebras.  
**Source**: `canonical/THEORY/axioms/core_assumptions.tex`

**Gap**: A derivation of why `ℂ⊗ℍ` rather than, e.g., `ℝ⊗ℍ` or `ℂ⊗ℂ`,
from a yet more fundamental principle (e.g., information-theoretic or
categorical) would strengthen the theory.

---

### AXIOM-B: Complex time τ = t + iψ

**Statement**: Physical time is complex: `τ = t + iψ` where `t` is real time
and `ψ` is the imaginary time component.

**Status**: AXIOM — foundational  
**Role in gauge sector**: The imaginary time circle `S¹_ψ` provides the three
winding modes that give rise to three generations.  `ψ`-parity motivates
chirality selection `SU(2)_L` not `SU(2)_R`.  
**Source**: `canonical/THEORY/axioms/core_assumptions.tex`

---

### AXIOM-F: Field equation (T-shirt equation)

**Statement**: The fundamental field `Θ(q,τ)` satisfies
`∇†∇Θ(q,τ) = κ 𝒯(q,τ)`.

**Status**: AXIOM — dynamical postulate  
**Role in gauge sector**: The covariant derivative `∇ = ∂ + A` with gauge
connection `A` is defined by this equation; gauge invariance follows from the
structure of the biquaternion-valued connection.  
**Source**: `canonical/fields/theta_field.tex`

---

## Motivated but Not Proved (Gaps C1–C3)

### Gap C1: Chirality — why SU(2)_L and not SU(2)_R

**Statement needed**: A formal theorem that the complex-time structure
`τ = t + iψ` selects left-handed couplings (`SU(2)_L`) over right-handed
(`SU(2)_R`).

**Current status**: MOTIVATED [SE]  
The physical argument (ψ-parity breaks L↔R symmetry) is given in
`canonical/chirality/` but has not been elevated to a theorem.

**What would close it**: Define the parity operation `P_ψ: ψ → -ψ` formally
in the UBT action.  Show that the action `S[Θ]` is invariant under `P_ψ`
only for left-handed couplings.  Equivalently, show that the Θ-field
decomposition under `P_ψ` projects onto `SU(2)_L` representations, not `SU(2)_R`.

**Priority**: HIGH — required for the SM paper to be complete on parity violation  
**Source**: `canonical/chirality/step3_gap_C1_resolution.tex`,
`canonical/symmetry/chirality_and_parity_breaking.tex`

---

### Gap C2: Weinberg Angle θ_W

**Statement needed**: A first-principles derivation of `sin²θ_W ≈ 0.23122`.

**Current status**: SEMI-EMPIRICAL (confirmed Dead End from `ℂ⊗ℍ` algebra alone)

**Why it cannot be derived from ℂ⊗ℍ alone**:
The Weinberg angle parametrises the mixing between `SU(2)_L` and `U(1)_Y`.
The mixing ratio depends on the fermion hypercharge assignments, which are not
fixed by the abstract algebra `ℂ⊗ℍ` — they depend on the representation theory
of the full gauge group including the Higgs sector.

**Implication for the paper**: State explicitly that `θ_W` is semi-empirical
in UBT at the current level of development.  This is not a failure — no other
published framework derives `θ_W` from a single algebra either.

**What might close it**: A derivation of the fermion hypercharge assignments from
UBT representation theory, combined with the Glashow-Salam-Weinberg (GSW) formula
`tan θ_W = g'/g`.  This would require formalizing the Higgs sector in UBT.

**Priority**: MEDIUM — desirable but not blocking the gauge paper  
**Source**: `canonical/interactions/sm_gauge.tex`,
`canonical/bridges/gauge_emergence_bridge.tex`

---

### Gap C3: Higgs Mechanism and Electroweak Symmetry Breaking

**Statement needed**: Derive the Higgs potential, its vacuum expectation value
`⟨H⟩ = v = 246 GeV`, and the gauge boson masses `m_W, m_Z` from UBT.

**Current status**: CANDIDATE — incomplete  
Radiative Hosotani mechanism for spontaneous symmetry breaking is partially
explored.  The quartic coupling `λ` is off by a factor of ~11 from the observed
value.

**Known gap (λ ×11)**: The quartic Higgs coupling derived from UBT gives
`λ_UBT ≈ 11 λ_SM`.  This is the "λ gap ×11" in `DERIVATION_INDEX.md`.

**What would close it**: Either:
1. Identify an additional contribution to the effective potential that cancels
   the ×11 discrepancy.
2. Show that the ×11 factor is a renormalisation effect that disappears at
   the correct energy scale.
3. Accept as a limitation and state it explicitly.

**Priority**: LOW — not blocking the gauge structure paper  
**Source**: `research_tracks/research/higgs_yukawa_scan.md`, `PRIORITIES_2026.md`

---

## Open Problems in Yukawa/Mass Sector

### Gap Y1: Fermion mass spectrum

**Statement needed**: Derive the electron, muon, tau, and quark masses from UBT.

**Current status**: OPEN  
The KK mismatch theorem *proves* that the simple torus winding formula cannot
reproduce the factor-207 mass ratio between muon and electron.
No mechanism found.

**Priority**: LOW for current paper, HIGH for future work  
**Source**: `PRIORITIES_2026.md` §Bottlenecks

### Gap Y2: Yukawa coupling derivation

**Statement needed**: Derive the Yukawa coupling matrix `y_{ij}` from the UBT
interaction sector.

**Current status**: OPEN  
**Priority**: LOW  
**Source**: `research_tracks/research/higgs_yukawa_scan.md`

---

## What the Gauge Paper Can Claim (Without These Gaps)

The SM gauge structure paper can be submitted with the following scope:

### Proved claims (zero free parameters)

1. `𝔰𝔲(3)` realised in `ℂ⊗ℍ` — [L0]
2. Quarks in fundamental `3` — [L0]
3. Gluons in adjoint `8` — [L0]
4. EW/strong decoupling — [L0]
5. `SU(2)_L` from left action — [L0]
6. `U(1)_Y` from right action — [L0]
7. `U(1)_EM` from `ψ`-cycle phase — [L0]
8. Three generations from `ψ`-modes — [L0]
9. Structural colour confinement — [L0] + experimental support

### Stated as open/semi-empirical

- Chirality selection (SU(2)_L not SU(2)_R) — motivated only [SE]
- Weinberg angle `θ_W` — semi-empirical
- Higgs mechanism / `λ` — open
- Fermion masses — open

### Paper impact

This scope is publishable and significant: **no other framework derives all three
SM gauge factors from a single 8-dimensional real algebra without introducing
the gauge group as external input.**

---

## Priority Ranking for Gap Closure

| Gap | Importance for paper | Difficulty | Recommended action |
|-----|---------------------|------------|-------------------|
| C1 (chirality) | HIGH | Medium | Formalize ψ-parity theorem before submission |
| C2 (θ_W) | Medium | Hard (Dead End) | State as limitation in paper |
| C3 (Higgs λ) | Low | Hard | Defer to separate paper |
| Y1 (masses) | Low | Very Hard | Defer, not blocking |
| Y2 (Yukawa) | Low | Very Hard | Defer, not blocking |
