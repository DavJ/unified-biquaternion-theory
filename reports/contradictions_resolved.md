<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# contradictions_resolved.md — Internal Contradiction Audit

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Record every identified contradiction between active repository documents,
state the chosen truth, and mark the stale document.  
**Truth anchor**: `STATUS_OF_UBT.md`

---

## How to Read This Document

Each contradiction entry records:
- **Files in conflict**: the two (or more) documents making incompatible claims
- **The conflict**: what exactly is inconsistent
- **Current truth**: the authoritative verdict, with justification
- **Stale file action**: what should be done to the outdated file (added deprecation header,
  or preserved as historical record in `ARCHIVE/`)
- **Cross-link added**: whether a note pointing to the truth has been added to the stale file

---

## Contradiction C1 — Weinberg Angle: DEAD END vs. CRITICAL PRIORITY

**Discovered**: 2026-04-28  
**Severity**: HIGH — affects alpha program strategy and paper claims

### Files in Conflict

| File | Claim | Date |
|------|-------|------|
| `canonical/alpha/weinberg_angle_derivation.md` | **Priority: CRITICAL** — Weinberg angle derivation treated as live, active target | 2026-04-28 |
| `reports/ew_mixing_status.md` | **Priority: CRITICAL** — Weinberg angle as strategic conversion target | 2026-04-28 |
| `reports/gauge_truth_matrix.md` §6 | **DEAD END** — "algebra cannot fix g'/g"; no-go argument given | 2026-04-28 |
| `STATUS.md` | **DEAD END** — "Weinberg angle sin²θ_W ≈ 0.231 | DEAD END — algebra cannot fix g'/g" | 2026-04-28 |
| `WHAT_IS_PROVED.md` | "Weinberg angle sin²θ_W — Dead end — stated explicitly" | 2026-04-28 |
| `canonical/alpha/weinberg_angle_routes.md` | Defines "three-workstream attack plan" as if active | 2026-04-28 |

### The Conflict

`weinberg_angle_derivation.md`, `ew_mixing_status.md`, and `weinberg_angle_routes.md`
treat deriving sin²θ_W as a live critical priority.  `gauge_truth_matrix.md`, `STATUS.md`,
and `WHAT_IS_PROVED.md` declare it a DEAD END with an explicit no-go argument.

These cannot both be true simultaneously.

### Current Truth

**DEAD END.**

The no-go argument is decisive: SU(2)_L and U(1)_Y act on orthogonal sectors of
ℂ⊗ℍ (left vs right action).  The Killing form on su(2)_L ⊕ u(1)_Y has no mixed
term.  The relative normalization of the two sectors — i.e., the ratio g'/g — is
a continuous free parameter in the Lagrangian on ℂ⊗ℍ.  No purely algebraic
argument can fix it.

The Weinberg angle is a semi-empirical input in UBT at this stage.

Source for the no-go: `reports/gauge_truth_matrix.md §6`, dead-end statement paragraph.

### Resolution Actions

1. **`canonical/alpha/weinberg_angle_derivation.md`**: Add deprecation notice at top.
   Change "Priority: CRITICAL" to "Priority: CLOSED — DEAD END". Cross-link to
   `STATUS_OF_UBT.md §Deprecated Claims`.
2. **`reports/ew_mixing_status.md`**: Add deprecation notice at top.
   Change "Priority: CRITICAL" to "Priority: CLOSED — DEAD END". Note that the
   EW-mixing gap is preserved as an open problem (Gap EW-1) in the T2_GAUGE paper,
   but it is not an active pursuit.
3. **`canonical/alpha/weinberg_angle_routes.md`**: Add deprecation notice. The
   "three-workstream attack plan" is suspended; Weinberg route is not being pursued.

**Deprecation notices added**: ✅ (see below in this document for text)

---

## Contradiction C2 — Alpha Routes: "Four Active Routes" vs. Two Routes Killed

**Discovered**: 2026-04-28  
**Severity**: MEDIUM — creates wrong impression of active research breadth

### Files in Conflict

| File | Claim | Date |
|------|-------|------|
| `canonical/alpha/alpha_derivation_routes.md` | "four active routes catalogued"; all four listed as live | 2026-04-27 |
| `reports/alpha_routes_ranked.md` | Routes A3 and A4 **DEFINITIVELY FAILED**; KILLED | 2026-04-28 |
| `canonical/alpha/PRIMARY_ROUTE.md` | A3 and A4 **closed**; one primary route only | 2026-04-28 |

### The Conflict

`alpha_derivation_routes.md` was authored one day before the route-ranking audit and
still refers to four active routes including A3 (Theta/modular) and A4 (Layer 2 coding),
both of which were definitively killed on 2026-04-28.

### Current Truth

**Two routes are KILLED**: A3 (exhaustive search found no modular invariant = 137.036)
and A4 (proved impossible: coding fixes spectrum, not coupling magnitude).

**One primary route**: A_PRIME (V_eff prime attractor), conditional on Gap G137-B.

**Two parked routes**: A1 and A2 (conditional on Weinberg angle — which is itself a dead end).

Source: `reports/alpha_routes_ranked.md`, `canonical/alpha/PRIMARY_ROUTE.md`.

### Resolution Actions

1. **`canonical/alpha/alpha_derivation_routes.md`**: Add notice at top that this file
   is superseded by `canonical/alpha/ALPHA_MASTER_STATUS.md` and
   `reports/alpha_routes_ranked.md`.  Routes A3 and A4 are killed; file is kept as
   historical survey.

---

## Contradiction C3 — Chirality Gap C1: [MC] Motivated vs. [L1] Proved

**Discovered**: 2026-04-28  
**Severity**: MEDIUM — affects what can be stated as a theorem in T2_GAUGE paper

### Files in Conflict

| File | Claim | Date |
|------|-------|------|
| `reports/gauge_status_matrix.md` line 70 | C1 status: **[MC]** — "close before submission (1–2 wk); if not: explicit open statement" | 2026-04-28 |
| `reports/chirality_gap.md` | C1 current status: **MOTIVATED [SE]** — "physical argument given, no formal theorem" | 2026-04-28 |
| `STATUS.md` | C1: **✅ PROVED [L1]** — "Chirality: SU(2)_L not SU(2)_R (Gap C1 closed)" | 2026-04-28 |
| `WHAT_IS_PROVED.md` claim E2 | **[L1]** — "SU(2)_L acts on left-chiral doublets (chirality gap C1 closed)" | 2026-04-28 |

### The Conflict

`gauge_status_matrix.md` and `chirality_gap.md` treat C1 as an open motivated conjecture.
`STATUS.md` and `WHAT_IS_PROVED.md` declare it [L1] proved.

### Current Truth

**[L1] PROVED.**  

The formal proof exists in `canonical/chirality/step3_gap_C1_resolution.tex`.
`STATUS.md` and `WHAT_IS_PROVED.md` are the more recent assessment.

However: note the nuance between Gap C1 (SU(2)_L acts on left-chiral doublets — PROVED)
and Gap C1b (dynamical exclusion of SU(2)_R — CONDITIONAL [MC]).  The partial confusion
in `gauge_status_matrix.md` may stem from conflating C1 with C1b.

**C1 (SU(2)_L acts on L doublets)**: [L1] PROVED  
**C1b (dynamical SU(2)_R exclusion)**: [MC] OPEN — not required for T2_GAUGE paper

### Resolution Actions

1. **`reports/gauge_status_matrix.md`**: Add note clarifying C1 vs C1b distinction.
   Update C1 line to reflect [L1] PROVED status; retain C1b as [MC] open.
2. **`reports/chirality_gap.md`**: Add note at top that C1 is now [L1] proved;
   file documents the proof steps; C1b remains open.

---

## Contradiction C4 — T3_ALPHA Confidence: 15% vs. "ACHIEVABLE"

**Discovered**: 2026-04-28  
**Severity**: LOW — language inconsistency, not a factual conflict

### Files in Conflict

| File | Claim | Date |
|------|-------|------|
| `FLAGSHIP_SELECTION.md` | T3_ALPHA: **"15% confidence"** of submission; ">20 weeks to arXiv if ever" | 2026-04-28 |
| `ALPHA_PROGRESS_REPORT.md` | α⁻¹_bare = 137: **"ACHIEVABLE — if and only if k=1 is proved"** | 2026-04-28 |

### The Conflict

These are not strictly contradictory (15% is a low probability of success, not zero), but
the word "ACHIEVABLE" in the progress report creates an impression of optimism inconsistent
with the honest probability in `FLAGSHIP_SELECTION.md`.

### Current Truth

**Conditionally achievable with low (20–30%) probability** of resolution within
the 4-week time-box.  The word ACHIEVABLE is accurate but should be read as "technically
possible, not likely".

### Resolution Actions

No file changes required.  This is flagged as a language calibration issue.
The probability range 20–30% from `canonical/alpha/PRIMARY_ROUTE.md` is the authoritative
confidence estimate.

---

## Contradiction C5 — T2_GAUGE Chirality Reference: [L0] vs. [L1]

**Discovered**: 2026-04-28  
**Severity**: LOW — affects paper proof-level labelling

### Files in Conflict

| File | Claim | Date |
|------|-------|------|
| `reports/gauge_status_matrix.md` line 68 | "SU(2)_L acts on left-chiral doublets — **[L0]**" | 2026-04-28 |
| `WHAT_IS_PROVED.md` claim E2 | "SU(2)_L acts on left-chiral doublets — **[L1]**" | 2026-04-28 |
| `reports/gauge_truth_matrix.md` | Same claim at **[L1]** | 2026-04-28 |

### Current Truth

**[L1]** — this result requires the ψ-parity axiom (AXIOM-B) in addition to the
algebraic structure; it is not a purely algebraic identity.  [L0] is incorrect here.

### Resolution Actions

1. **`reports/gauge_status_matrix.md`** line 68: Update [L0] → [L1] for the chirality claim.

---

## Summary Table

| ID | Topic | Truth | Stale Files |
|----|-------|-------|-------------|
| C1 | Weinberg angle | **DEAD END** | `weinberg_angle_derivation.md`, `ew_mixing_status.md`, `weinberg_angle_routes.md` |
| C2 | Alpha routes count | **2 killed; 1 primary** | `alpha_derivation_routes.md` |
| C3 | Chirality C1 | **[L1] PROVED** | `gauge_status_matrix.md`, `chirality_gap.md` |
| C4 | T3_ALPHA confidence | **20–30% in 4-week box** | Language in `ALPHA_PROGRESS_REPORT.md` |
| C5 | Chirality proof level | **[L1] not [L0]** | `gauge_status_matrix.md` |

---

## Deprecation Notices (Text to Add to Stale Files)

### For `canonical/alpha/weinberg_angle_derivation.md`

```
> **DEPRECATION NOTICE (2026-04-28)**: This file treated the Weinberg angle
> derivation as a critical priority. That assessment is superseded.
> The Weinberg angle route is a DEAD END: the biquaternion algebra cannot fix
> the ratio g'/g (no-go argument in `reports/gauge_truth_matrix.md §6`).
> This file is preserved as historical record.
> **Truth anchor**: `STATUS_OF_UBT.md §Deprecated Claims`
```

### For `reports/ew_mixing_status.md`

```
> **DEPRECATION NOTICE (2026-04-28)**: This file was written when the Weinberg
> angle route was considered a live priority. The route is now classified as a
> DEAD END. Gap EW-1 is preserved as an honest open problem in the T2_GAUGE paper
> but is not being actively pursued.
> **Truth anchor**: `STATUS_OF_UBT.md §Deprecated Claims`
```

### For `canonical/alpha/weinberg_angle_routes.md`

```
> **DEPRECATION NOTICE (2026-04-28)**: The three-workstream attack plan in this
> file is suspended. The Weinberg angle route is a DEAD END.
> See `reports/gauge_truth_matrix.md §6` for the no-go argument.
> **Truth anchor**: `STATUS_OF_UBT.md §Deprecated Claims`
```

### For `canonical/alpha/alpha_derivation_routes.md`

```
> **SUPERSEDED NOTICE (2026-04-28)**: This survey (dated 2026-04-27) listed
> four active routes. Routes A3 and A4 have since been definitively killed.
> See `canonical/alpha/ALPHA_MASTER_STATUS.md` for current route status.
> This file is preserved as a historical survey.
```
