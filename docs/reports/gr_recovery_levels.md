<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# GR Recovery Levels — Three Notions of Einstein Gravity Recovery in UBT

**Path**: `reports/gr_recovery_levels.md`  
**Date**: 2026-03-11  
**Status**: Active reference document  
**Authority**: Canonical definition of GR recovery terminology for this repository

---

## Purpose

This document defines three distinct levels at which the Unified Biquaternion
Theory (UBT) can be said to "reproduce General Relativity".  Every GR-recovery
claim in the repository should be labelled with exactly one of these three levels.

**There is no contradiction between UBT and GR.**  UBT can reproduce GR on a
physical sector while still containing additional non-GR degrees of freedom.
The absence of a full exact Theta-only theorem does not contradict this;
it means GR recovery must be stated as sector/limit/projection recovery,
not unconditional full-theory recovery.

Using a common vocabulary prevents conflation of:
- what has been proved rigorously,
- what holds on a well-defined sector,
- what is expected in a low-energy limit,

and avoids the false impression of either over-claiming or under-claiming.

**Mandatory consistency rule**: README.md, CURRENT_STATUS.md, DERIVATION_INDEX.md,
docs/THEORY_STATUS.md, and all GR reports must use one of the labels
`exact_projected_recovery`, `constrained_sector_recovery`, or
`low_energy_limit_recovery` consistently for each specific claim.

---

## Level 1 — Exact Projected Recovery

**Label**: `exact_projected_recovery`

**Description**:  
There exists a mathematically clean projection, contraction, or subsector
theorem that maps the $\Theta$ Euler–Lagrange equation to the Einstein equation
$G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ exactly and unconditionally (without
additional assumptions beyond the UBT axioms).

This level requires:
- A surjective (or bijective on the relevant quotient) map from $\Theta$
  variations to metric variations.
- No additional regularity or gauge conditions beyond the defining axioms of UBT.
- An algebraic/analytic proof, not a perturbative argument.

**Current status**: `open_or_partial`

This level has NOT been established unconditionally.  The closest result
(Hilbert variation with $g$ as an independent variable) is a Level-1 result
for the metric+$\Theta$ formulation but not for the pure-$\Theta$ formulation.

**Where this matters**:  
Do NOT claim Level 1 for the pure-$\Theta$ variation unless the rank condition
on $J = \delta g / \delta\Theta$ is proved globally.  See
`consolidation_project/GR_closure/theta_vs_metric_variation_note.tex` §4.

**Permitted language** (when Level 1 is established):  
> "UBT exactly recovers Einstein's equations via a projection theorem."

**Forbidden language** (when only Level 2 or 3 is established):  
> "UBT derives Einstein's equations directly from the $\Theta$ field equation."

---

## Level 2 — Constrained Sector Recovery

**Label**: `constrained_sector_recovery`

**Description**:  
On an admissible configuration sector $\mathcal{A}_{\mathrm{UBT}} \subset
\mathcal{F}[\Theta]$ defined by explicit regularity and rank conditions
(see `consolidation_project/GR_closure/gr_sector_conditions.tex`), the
induced dynamics of $\Theta$ reproduces Einstein's equations.

This level requires:
- An explicitly defined admissible class $\mathcal{A}_{\mathrm{UBT}}$.
- Proof that $\mathcal{A}_{\mathrm{UBT}}$ is non-empty and physically
  relevant (contains at minimum flat space and linearised perturbations).
- Proof that on $\mathcal{A}_{\mathrm{UBT}}$, the combined
  Euler–Lagrange condition $\mathcal{E}_\Theta + J^*\mathcal{E}_g = 0$
  implies $\mathcal{E}_g = 0$.

**Current status**: `likely_current_best_description`

This level IS established for:
- Flat Minkowski space (trivial solution).
- Linearised perturbations around flat space.
- Metric+$\Theta$ formulation (where $g$ is varied independently):
  the Einstein equations follow unconditionally from the Hilbert variation.

It is NOT yet established for:
- Non-linear GR solutions (Schwarzschild, Kerr, FLRW) in the pure-$\Theta$
  formulation.
- Global (non-perturbative) configurations.

**Permitted language**:  
> "GR-compatible sector recovered."  
> "Einstein's equations hold on the admissible sector $\mathcal{A}_{\mathrm{UBT}}$."  
> "Variational embedding: standard Einstein-sector recovery."

**Forbidden language**:  
> "Full exact $\Theta$-only Einstein derivation completed."  
> "UBT proves Einstein's equations for all $\Theta$."

---

## Level 3 — Low-Energy or Effective Limit Recovery

**Label**: `low_energy_limit_recovery`

**Description**:  
After freezing or suppressing additional $\Theta$ degrees of freedom
(imaginary-time modes, $\psi$-circle winding modes, non-metric biquaternionic
polarisations) that decouple at macroscopic scales, the theory reduces to
General Relativity in the classical/low-energy limit.

This level requires:
- An identification of which $\Theta$ modes correspond to "extra" UBT degrees
  of freedom beyond the metric sector.
- A decoupling argument showing these modes are suppressed at the relevant scales.
- Reduction of the UBT equations to the Einstein equations after decoupling.

**Current status**: `plausible_if_supported`

This is the physically expected behaviour and is consistent with all known
results, but a complete formal argument has not been given.  The partial result
in `consolidation_project/FPE_verification/step4_fpe_equivalence.tex` (FPE ↔
Euler–Lagrange equivalence) supports this picture.

**Permitted language**:  
> "UBT reduces to GR in the low-energy / classical limit."  
> "After freezing extra $\Theta$ modes, the macroscopic theory is GR."

**Forbidden language**:  
> "UBT reduces exactly to GR" (without specifying the limit).

---

## Comparison Table

| Property | Level 1 | Level 2 | Level 3 |
|----------|---------|---------|---------|
| Label | `exact_projected_recovery` | `constrained_sector_recovery` | `low_energy_limit_recovery` |
| Conditions | None beyond UBT axioms | Explicit sector conditions C1–C6 | Decoupling of extra modes |
| Scope | All $\Theta$ | $\Theta \in \mathcal{A}_{\mathrm{UBT}}$ | Classical / low-energy regime |
| Flatspace | ✅ | ✅ | ✅ |
| Linearised GR | ✅ (if proved) | ✅ | ✅ |
| Non-linear GR | ✅ (if proved) | ⚠️ open | ⚠️ plausible |
| Current best status | Open | **Established (partial)** | Plausible |

---

## Current Repository Claim Inventory

The following table records which level applies to each GR-related claim
currently made in the repository.

| Claim | Location | Applicable level | Status |
|-------|----------|-----------------|--------|
| $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ from Hilbert variation ($g$ independent) | `consolidation_project/T_munu_derivation/step3_einstein_with_matter.tex` | Level 1 | ✅ Proved |
| Linearised GR recovery from $\delta\Theta$ | `canonical/geometry/gr_completion_attempt.tex` | Level 2 | ✅ Proved |
| Non-linear GR recovery | `reports/gr_recovery_final_status.md` | Level 2–3 | ⚠️ Partial |
| $\Theta$-only closure (pure-$\Theta$ action) | `consolidation_project/GR_closure/step2_theta_only_closure.tex` | Level 2 | 🔶 On-shell + rank condition |
| GR as low-energy limit of full UBT | — | Level 3 | ⚠️ Plausible, not proved |

---

## Instructions for Future Claims

When adding a new GR-related result to the repository:

1. Determine which level applies (1, 2, or 3).
2. State the level explicitly in the document.
3. Use the permitted language for that level; do not use forbidden language.
4. If the level changes (e.g.\ a Level-2 result is upgraded to Level 1), update
   this file and all files referencing the claim.
5. If only Level 2 or 3 is available, do not imply Level 1.

---

## References

- `consolidation_project/GR_closure/theta_vs_metric_variation_note.tex` — combined variation analysis
- `consolidation_project/GR_closure/gr_sector_conditions.tex` — explicit conditions for Level 2
- `reports/gr_recovery_final_status.md` — current status summary
- `DERIVATION_INDEX.md §GR Recovery Status` — derivation-level tracking
- `AUDITS/followup_gap_backlog_2026_03.md` — open problems
