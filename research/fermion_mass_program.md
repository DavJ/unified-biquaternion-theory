# Fermion Mass Generation Program

**Author**: Ing. David Jaroš  
**Date**: 2025  
**Status**: SEMI-EMPIRICAL — formula reproduces masses; parameters fitted, not derived

---

## Overview

A complete unified theory must generate fermion masses from its first-principles
structure. The Unified Biquaternion Theory (UBT) proposes a mechanism for
fermion mass generation rooted in the biquaternionic field structure and complex
time. This document describes the current state of the program accurately,
distinguishing what is proved from what is semi-empirical or open.

---

## Mechanism

In UBT, fermion masses arise from the potential term V(Θ) in the action:

```
S[Θ] = ∫ d⁴x √(-g) [ (1/2κ) R + Tr[(D_μΘ)†(D^μΘ)] - (1/4) F_μν F^μν - V(Θ) ]
```

The potential V(Θ) encodes symmetry breaking and mass generation. In the
spinor decomposition Θ = ψ₊ ⊗ u₊ + ψ₋ ⊗ u₋, the mass term
`m ψ̄ ψ` appears as the real projection of the biquaternionic potential.

The mass scale is set by the imaginary curvature of the Θ field through
the complex-time component τ = t + iψ. Physically, the mass parameter m
measures the coupling strength between the real and imaginary sectors of
the biquaternionic field.

---

## Current Results

### Electron Mass

The UBT formula predicts:
```
m_e ≈ 0.511 MeV    (0.22% accuracy relative to experimental value)
```

- **Status**: SEMI-EMPIRICAL [SE] — the formula reproduces m_e with 0.22%
  accuracy, but the mass scale parameter B_m ≈ −14.099 MeV is fitted to
  experimental data, not derived independently.
- **Source**: `consolidation_project/electron_mass/`

### The Mass Formula

The fermion mass formula of UBT for the n-th excitation of the Θ field:
```
m(n) = A · n^p − B_m · n · ln(n)
```
where A is a scale factor and B_m ≈ −14.099 MeV is a logarithmic correction.

- **Status**: SEMI-EMPIRICAL [SE] — formula present; parameters fitted
- **Source**: `unified_biquaternion_theory/fermion_mass_derivation_complete.tex`

### Note on B_m vs B_base

The parameter **B_m ≈ −14.099 MeV** (fermion mass sector, dimension MeV) is
distinct from **B_base ≈ 41.57** (α derivation, dimensionless). These should
not be confused. See `canonical/bridges/QED_limit_bridge.tex`, Notation section.

---

## Derivation Status Table

| Result | Status | Source |
|--------|--------|--------|
| Fermion mass formula (general) | **[SE]** — formula present, params fitted | `fermion_mass_derivation_complete.tex` |
| Electron mass m_e ≈ 0.511 MeV | **[SE]** — 0.22% accuracy | `consolidation_project/electron_mass/` |
| Mass hierarchy framework | **[P]** — framework present, not complete | `consolidation_project/masses/` |
| Theta-particle model (P2) | **[P]** — motivating model present | `solution_theta_particle_model_P2/` |
| Quark masses (partial) | **[P]** — partial treatment only | `appendix_QA2_quarks_CKM.tex` |
| Three-generation structure | **PROVED [L0]** — from ψ-winding modes | `DERIVATION_INDEX.md` |

---

## Open Problems

### Open Problem 1: B_m from First Principles

The mass-scale parameter B_m ≈ −14.099 MeV appears in the fermion mass
formula but is fitted to the electron mass rather than derived from the
biquaternion algebra or complex-time structure.

Deriving B_m would constitute a complete first-principles fermion mass
derivation for the electron.

**Status**: OPEN [O]  
**Source**: `consolidation_project/masses/`

### Open Problem 2: Lepton Mass Ratios

The ratios m_μ/m_e ≈ 207 and m_τ/m_μ ≈ 17 are not derived from first
principles. The three-generation structure is proved (from ψ-winding modes),
but the mass ratios between generations are not.

**Status**: OPEN [O]

### Open Problem 3: CKM Matrix

The quark mixing angles (CKM matrix elements) have not been derived from
first principles. A partial treatment exists.

**Status**: PARTIAL [P]  
**Source**: `consolidation_project/appendix_QA2_quarks_CKM.tex`

### Open Problem 4: Neutrino Masses and PMNS Matrix

Neutrino masses and the PMNS mixing matrix are not treated in the repository.
The neutrino sector is referenced in some appendices but without a complete
mass derivation.

**Status**: PARTIAL [P]  
**Source**: Various consolidation_project appendices on neutrinos

### Open Problem 5: Second and Third Generation Masses

While first-generation (u, d, e) masses are treated semi-empirically, the
second-generation (c, s, μ) and third-generation (t, b, τ) masses require
additional parameters not yet derived.

**Status**: PARTIAL [P]  
**Source**: `consolidation_project/masses/`

---

## Three-Generation Structure (PROVED [L0])

One result that is fully proved is the origin of three fermion generations.

Three identical copies of the SM quantum number structure arise from the three
ψ-winding modes on the imaginary time circle ψ ~ ψ + 2π.

- **Status**: PROVED [L0] — algebraic identity
- **Source**: `DERIVATION_INDEX.md`: "ψ-modes as independent B-fields [L0]: Proven";
  `STATUS_THEORY_ASSESSMENT.md` v61 proved results.

This means UBT explains *why there are three generations* even if the
mass ratios between generations remain open.

---

## Assessment

The fermion mass program shows promising results:
- Electron mass is reproduced with 0.22% accuracy (scientifically significant)
- Three-generation structure is explained (fully proved)

However, the current state does not constitute a complete first-principles
derivation because:
1. Mass parameters are fitted rather than derived
2. Lepton mass ratios are not explained
3. Quark masses and mixing are incomplete
4. Neutrino sector is not treated

The situation is analogous to the Koide formula in the Standard Model: a
numerically accurate relation whose geometric origin is not fully understood.

**For a referee**: The electron mass result and three-generation derivation
are interesting and publication-worthy. Claims of a complete fermion mass
derivation should not be made until the mass parameters are derived from
first principles.

---

## Repository Sources

| File | Content |
|------|---------|
| `unified_biquaternion_theory/fermion_mass_derivation_complete.tex` | Full mass derivation attempt |
| `consolidation_project/electron_mass/` | m_e specific derivation |
| `consolidation_project/masses/` | All fermion masses framework |
| `unified_biquaternion_theory/solution_theta_particle_model_P2/` | Theta-particle motivating model |
| `unified_biquaternion_theory/priority_P2_electron_model/` | P2 priority documentation |
| `consolidation_project/appendix_QA2_quarks_CKM.tex` | Quark sector |
| `unified_biquaternion_theory/solution_P5_dark_matter/ThetaM_MassHierarchy.tex` | Hopfion mass model |

---

*Cross-reference: `research/fermion_mass_status.md` (earlier status document).*  
*Cross-reference: `research/alpha_derivation_status.md` for the related α program.*  
*Cross-reference: `AUDITS/claim_evidence_matrix.md` row `fermion_sector`.*
