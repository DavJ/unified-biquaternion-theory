# Fermion Mass Generation Program Status

**Author**: Ing. David Jaroš  
**Date**: 2026-03-10  
**Status**: SEMI-EMPIRICAL — formula reproduces masses; parameters fitted, not derived

---

## Overview

One of the key predictions of any unified theory is the generation of fermion
masses from a single framework. UBT proposes a mechanism for fermion mass
generation rooted in the biquaternionic field structure. This document
summarizes the current state of the fermion mass program without inventing
new formulas or claiming more than the repository evidence supports.

---

## Current Results

### Electron Mass

The UBT formula for the electron mass predicts:
```
m_e ≈ 0.511 MeV    (0.22% accuracy relative to experimental value)
```

**Status**: SEMI-EMPIRICAL [SE] — the formula reproduces m_e with 0.22%
accuracy, but the parameters in the formula are fitted to experimental data
rather than derived independently.

**Primary source**: `consolidation_project/electron_mass/`

### General Fermion Mass Formula

A fermion mass formula is present that covers the first-generation fermions
with reasonable accuracy.

**Status**: SEMI-EMPIRICAL [SE]  
**Primary source**: `unified_biquaternion_theory/fermion_mass_derivation_complete.tex`

---

## What Is Present

| Result | Status | Source |
|--------|--------|--------|
| Fermion mass formula (general) | **[SE]** — formula present, params fitted | `fermion_mass_derivation_complete.tex` |
| Electron mass m_e ≈ 0.511 MeV | **[SE]** — 0.22% accuracy | `consolidation_project/electron_mass/` |
| Mass hierarchy framework | **[P]** — framework present | `consolidation_project/masses/` |
| Theta-particle model (P2) | **[P]** — motivating model | `solution_theta_particle_model_P2/` |
| Quark masses (partial) | **[P]** — partial only | `appendix_QA2_quarks_CKM.tex` |

---

## Open Problems

### Open Problem 1: First-Principles Mass Parameters

**Problem**: The mass formula contains parameters (related to B_m ≈ −14.099 MeV)
that are fitted to experimental data, not derived from the biquaternion algebra
or complex-time structure.

**Note on Notation**: B_m (≈ −14.099 MeV, fermion mass parameter) is distinct
from B_base (≈ 41.57, dimensionless, used in α derivation). These should not
be confused. See `canonical/bridges/QED_limit_bridge.tex`, Notation §.

**Status**: OPEN [O]  
**Source**: `consolidation_project/masses/`

### Open Problem 2: Lepton Mass Ratios

**Problem**: The ratios m_μ/m_e and m_τ/m_μ (approximately 207 and 17)
are not derived from first principles. No complete derivation of these
ratios from the biquaternionic framework has been found in the repository.

**Status**: OPEN [O]

### Open Problem 3: CKM Matrix

**Problem**: The quark mixing angles (CKM matrix elements) have not been
derived from first principles. A partial treatment exists but does not
produce the full CKM matrix.

**Status**: PARTIAL [P]  
**Source**: `consolidation_project/appendix_QA2_quarks_CKM.tex`

### Open Problem 4: Neutrino Masses

**Problem**: Neutrino masses and the PMNS mixing matrix are not yet
treated in the repository. The neutrino sector is referenced in some
appendices but without a complete mass derivation.

**Status**: PARTIAL [P]  
**Source**: Various consolidation_project appendices on neutrinos

### Open Problem 5: Second and Third Generation Masses

**Problem**: While the first-generation (u, d, e) masses are treated with
a semi-empirical formula, the second-generation (c, s, μ) and third-generation
(t, b, τ) masses require additional parameters.

**Status**: PARTIAL [P]  
**Source**: `consolidation_project/masses/`

---

## Repository Sources for Fermion Mass Derivations

| File | Content | Location |
|------|---------|----------|
| Fermion mass main | Full mass derivation attempt | `unified_biquaternion_theory/fermion_mass_derivation_complete.tex` |
| Electron mass | m_e specific derivation | `consolidation_project/electron_mass/` |
| Mass hierarchy | All fermion masses | `consolidation_project/masses/` |
| P2 particle model | Theta-particle motivating model | `unified_biquaternion_theory/solution_theta_particle_model_P2/` |
| P2 priority claim | Priority documentation | `unified_biquaternion_theory/priority_P2_electron_model/` |
| Quarks and CKM | Quark sector | `consolidation_project/appendix_QA2_quarks_CKM.tex` |
| Hopfion mass model | Dark sector mass model | `unified_biquaternion_theory/solution_P5_dark_matter/ThetaM_MassHierarchy.tex` |
| Electron mass prediction | Final prediction | `unified_biquaternion_theory/solution_P5_dark_matter/electron_mass_prediction_final.tex` |

---

## The B_m Parameter

The fermion mass sector uses a parameter **B_m ≈ −14.099 MeV** which sets
the overall scale of fermion masses. This is distinct from the B_base parameter
in the fine structure constant formula.

**Status**: Semi-empirical — numerical value fitted to m_e.  
**Source**: `canonical/bridges/QED_limit_bridge.tex`, Notation section.

---

## Assessment

The fermion mass program shows promising results — the electron mass is
reproduced with 0.22% accuracy, which is scientifically significant.
However, the current state does not constitute a complete first-principles
derivation because:

1. Mass parameters are fitted rather than derived
2. Lepton mass ratios are not explained
3. Quark masses and mixing are incomplete
4. Neutrino sector is not treated

**For a referee**: The electron mass result is interesting and warrants
investigation. Claims of a complete fermion mass derivation should not be
made until the mass parameters are derived from first principles.

The situation is analogous to the Koide formula in the Standard Model —
a numerically accurate relation whose origin is not fully understood.

---

*See `AUDITS/claim_evidence_matrix.md` row `fermion_sector` for cross-references.*  
*See `research/alpha_program_status.md` for the related α program status.*
