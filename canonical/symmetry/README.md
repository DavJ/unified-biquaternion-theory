<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# canonical/symmetry — UBT Discrete Symmetry Architecture

© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0

**Overall confidence: Strong Partial** — CPT invariance and parity violation are substantially
derived; CP-violation phase terms and full non-perturbative T-asymmetry remain at Candidate level.

This directory contains the canonical discrete-symmetry formalization of
Unified Biquaternion Theory (UBT).  It covers charge conjugation $C$, spatial
parity $P$, time reversal $T$, and their composites $CP$, $CPT$, as well as
chirality structure, CP violation, and the distinction between fundamental and
effective symmetry breaking.

---

## File Index

Confidence labels: **Strong** | **Strong Partial** | **Candidate** | **Experimental** | **Open** | **Deprecated**

| File | Content | Confidence |
|------|---------|-----------|
| `discrete_symmetries.tex` | Formal involutions on $\mathcal{B}$; canonical definitions of $C$, $P$, $T$, $CPT$; operator table | **Strong** |
| `cpt_audit_table.md` | Term-by-term $C/P/T/CP/CPT$ audit of the UBT action | **Strong** |
| `chirality_and_parity_breaking.tex` | Left/right field decomposition; parity-violating weak coupling; conditional derivation that $P$ is broken (assuming no-$SU(2)_R$ in $S[\Theta]$) while $CPT$ is preserved | **Strong Partial** |
| `cp_phase_sector.tex` | CP-violating phase terms: $\theta_{\rm eff}F\tilde F$, complex Yukawa, vacuum misalignment | **Candidate** |
| `effective_vs_fundamental_breaking.tex` | Diffusion sector as effective coarse-grained dynamics; two-layer microscopic/macroscopic interpretation | **Strong** |
| `open_problems.md` | Honest list of unresolved discrete-symmetry problems in UBT | Reference |
| `examples_matrix_representation.tex` | $2\times2$ complex and $4\times4$ real matrix realizations of $C$, $P$, $T$ operators | **Strong** |
| `step1_CPT_definitions.tex` | Earlier detailed derivation of $C$, $P$, $T_{\rm UBT}$, $CPT$ | **Deprecated** (superseded by `discrete_symmetries.tex`) |
| `step2_action_analysis.tex` | Sector-by-sector $C/P/T$ analysis of the UBT action | Reference |
| `step3_breaking_catalogue.tex` | Symmetry breaking catalogue; physical vs.\ effective/dissipative | Reference |

---

## Theory Position

UBT adopts the following baseline:

1. **CPT invariance** is preserved at the microscopic (fundamental action) level.
2. **Parity violation** is present and desirable in the minimal UBT action
   (conditional on the no-$SU(2)_R$ selection rule): the weak-like sector
   couples only to left-chiral biquaternionic modes under this assumption.
3. **CP violation** is allowed through identified phase terms (see `cp_phase_sector.tex`).
4. **T asymmetry** in the diffusion sector is emergent/effective, not fundamental
   (see `effective_vs_fundamental_breaking.tex`).

---

## Dependencies

| This file | Depends on |
|-----------|-----------|
| `discrete_symmetries.tex` | `canonical/algebra/involutions_Z2xZ2xZ2.tex` |
| `chirality_and_parity_breaking.tex` | `discrete_symmetries.tex`, `canonical/chirality/` |
| `cp_phase_sector.tex` | `discrete_symmetries.tex`, `cpt_audit_table.md` |
| `effective_vs_fundamental_breaking.tex` | `discrete_symmetries.tex`, `step3_breaking_catalogue.tex` |
| `examples_matrix_representation.tex` | `discrete_symmetries.tex`, `canonical/fields/biquaternion_algebra.tex` |

---

## Notation Conventions

| Symbol | Meaning |
|--------|---------|
| $\mathcal{B} = \mathbb{C}\otimes\mathbb{H}$ | Biquaternion algebra |
| $\Theta(q,\tau)$ | Fundamental UBT field |
| $\tau = t + i\psi$ | Complex time ($t$ real, $\psi$ phase variable) |
| $P_1$ | Complex conjugation involution on $\mathcal{B}$ |
| $P_2$ | Quaternion conjugation involution on $\mathcal{B}$ |
| $P_3$ | Axis-flip (inner automorphism by $\mathbf{I}$) |
| $\widehat{C}, \widehat{P}, \widehat{T}$ | Physical symmetry operators |
| $\Theta_L, \Theta_R$ | Left/right chiral projections |

---

## Style Policy

- No mystical wording.
- The phase variable $\psi$ is an **auxiliary imaginary-time coordinate**.
  It is not referred to as a consciousness variable in these files.
- Claims are labelled **Theorem**, **Proposition**, **Conjecture**, or
  **Open Problem** — never presented without qualification.
- Every strong claim carries an equation or derivation sketch.
