<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# files_merged_deleted_redirected.md — Phase 3 File Cleanup Log

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Authoritative record of every file action taken during Phase 3
(Document Compression).  Records what was merged, what was deprecated/redirected,
what was preserved, and what remains as a candidate for future archival.  
**Truth anchor**: `STATUS_OF_UBT.md`

---

## Summary

| Action | Count | Notes |
|--------|-------|-------|
| New master files created | 4 | STATUS_OF_UBT, ALPHA_MASTER, GAUGE_MASTER, GR_REVIEW_MASTER |
| Files deprecated (notice added) | 5 | Weinberg-angle and alpha routes files |
| Files corrected (status updated) | 2 | chirality_gap, gauge_status_matrix |
| Files preserved unchanged | All GR core files | See GR_cleanup_nonimpact_confirmation.md |
| Files physically deleted | 0 | Archival policy: no deletion |
| Files archived | 0 | Recommended for future session |

---

## Phase 3a — Alpha Cluster

### Target (per task spec)

Merge into `canonical/alpha/ALPHA_MASTER_STATUS.md`:
- `reports/alpha_routes_ranked.md`
- `reports/alpha_no_fit_progress.md` (= `alpha_progress.md` in spec)
- `canonical/alpha/ew_mixing_gap_map.md`
- `reports/alpha_missing_lemma.md`
- `canonical/alpha/prime_137_status.md`

### Action Taken

**`canonical/alpha/ALPHA_MASTER_STATUS.md`** — CREATED (new master file).  
Synthesises and summarises all the above source files.  
The source files are **preserved** as detailed technical references.

| Source File | Action | Status |
|-------------|--------|--------|
| `reports/alpha_routes_ranked.md` | Summarised in master; preserved | PRESERVED |
| `reports/alpha_no_fit_progress.md` | Summarised in master; preserved | PRESERVED |
| `canonical/alpha/ew_mixing_gap_map.md` | Summarised in master; preserved | PRESERVED |
| `reports/alpha_missing_lemma.md` | Referenced from master; preserved | PRESERVED |
| `canonical/alpha/prime_137_status.md` | Summarised in master; preserved | PRESERVED |
| `canonical/alpha/alpha_derivation_routes.md` | Superseded notice added; preserved | SUPERSEDED |
| `canonical/alpha/weinberg_angle_derivation.md` | Deprecation notice added; preserved | DEPRECATED |
| `canonical/alpha/weinberg_angle_routes.md` | Deprecation notice added; preserved | DEPRECATED |
| `reports/ew_mixing_status.md` | Deprecation notice added; preserved | DEPRECATED |

**Redirects**:  
Anyone consulting `alpha_routes_ranked.md` or `alpha_derivation_routes.md` should
now consult `canonical/alpha/ALPHA_MASTER_STATUS.md` as the primary reference.

---

## Phase 3b — Gauge Cluster

### Target (per task spec)

Merge into `canonical/gauge/GAUGE_MASTER_STATUS.md`:
- `reports/gauge_status_matrix.md`
- `reports/gauge_truth_matrix.md`
- `reports/chirality_gap.md`
- `reports/anomaly_gap.md`
- `reports/higgs_yukawa_dependency.md`

### Action Taken

**`canonical/gauge/GAUGE_MASTER_STATUS.md`** — CREATED (new master file).  
New directory `canonical/gauge/` created.  
The source files are **preserved** as detailed technical references.

| Source File | Action | Status |
|-------------|--------|--------|
| `reports/gauge_status_matrix.md` | Summarised in master; chirality row corrected (C1 = [L1]); preserved | PRESERVED + CORRECTED |
| `reports/gauge_truth_matrix.md` | Summarised in master; preserved | PRESERVED |
| `reports/chirality_gap.md` | Status corrected: C1 = [L1] PROVED; C1b = [MC] OPEN; preserved | PRESERVED + CORRECTED |
| `reports/anomaly_gap.md` | Summarised in master; preserved | PRESERVED |
| `reports/higgs_yukawa_dependency.md` | Referenced from master; preserved | PRESERVED |

**Redirects**:  
Anyone consulting individual gauge report files should now consult
`canonical/gauge/GAUGE_MASTER_STATUS.md` as the primary overview.

---

## Phase 3c — GR Cluster

### Target (per task spec)

Preserve flagship paper; merge supporting notes into `reports/GR_REVIEW_MASTER.md`.

**Flagship paper preserved**: `papers/UBT_GR_Submission.tex` — UNCHANGED.

### Action Taken

**`reports/GR_REVIEW_MASTER.md`** — CREATED (consolidated review reference).  
Consolidates: GR_claim_to_proof_matrix, GR_claims_with_evidence_table,
GR_final_gap_checklist, GR_hostile_review, GR_reviewer_FAQ,
GR_reviewer_objections_and_answers.

| Source File | Action | Status |
|-------------|--------|--------|
| `papers/UBT_GR_Submission.tex` | Untouched | PRESERVED — primary deliverable |
| `papers/UBT_GR_Flagship.tex` | Untouched | PRESERVED |
| `reports/GR_claim_to_proof_matrix.md` | Summarised in master; preserved | PRESERVED |
| `reports/GR_claims_with_evidence_table.md` | Summarised in master; preserved | PRESERVED |
| `reports/GR_final_gap_checklist.md` | Summarised in master; preserved | PRESERVED |
| `reports/GR_hostile_review.md` | Summarised in master; preserved | PRESERVED |
| `reports/GR_reviewer_FAQ.md` | Summarised in master; preserved | PRESERVED |
| `reports/GR_reviewer_objections_and_answers.md` | Summarised in master; preserved | PRESERVED |

---

## New Files Created This Phase

| File | Purpose | Supersedes |
|------|---------|------------|
| `STATUS_OF_UBT.md` | Master truth anchor | `STATUS.md` (still active) |
| `reports/contradictions_resolved.md` | Contradiction audit log | — |
| `canonical/alpha/ALPHA_MASTER_STATUS.md` | Alpha master status | `reports/alpha_routes_ranked.md` (primary) |
| `canonical/gauge/GAUGE_MASTER_STATUS.md` | Gauge master status | `reports/gauge_truth_matrix.md` (primary) |
| `reports/GR_REVIEW_MASTER.md` | GR review consolidation | `reports/GR_hostile_review.md` (primary) |
| `reports/GR_cleanup_nonimpact_confirmation.md` | GR track protection confirmation | — |
| `reports/files_merged_deleted_redirected.md` | This file — cleanup log | — |

---

## Recommended Future Archival (Not Done Now)

The following root-level files have overlapping or lower-fidelity content now that
master files exist.  They are **not deleted** (archival policy forbids deletion).
They are candidates for future consolidation into `ARCHIVE/` or for a single
redirect notice.

### Alpha / Strategy root-level files

| File | Relationship to master |
|------|------------------------|
| `ALPHA_BREAKTHROUGH_REPORT.md` | Historical progress report; superseded by `ALPHA_MASTER_STATUS.md` |
| `ALPHA_FINAL_OFFENSIVE.md` | Historical strategy doc; superseded |
| `ALPHA_PROGRESS_REPORT.md` | Superseded by `ALPHA_MASTER_STATUS.md` |
| `ALPHA_STRUCTURAL_ORIGINS.md` | Useful structural context; consider absorbing into `ALPHA_MASTER_STATUS.md` |
| `MODULAR_BOOTSTRAP_K1_PLAN.md` | Relevant to Gap G137-B — preserve as working doc |
| `alpha_routes_scorecard.md` | Earlier version of route ranking; superseded by `alpha_routes_ranked.md` |
| `accepted_vs_rejected_routes.md` | Route history; subsumes into `failed_routes_graveyard.md` |

### Governance / Status root-level files

| File | Relationship to master |
|------|------------------------|
| `STATUS.md` | Per-track dashboard; remains useful alongside `STATUS_OF_UBT.md` |
| `PRIORITIES_2026.md` | Still relevant for time ordering; cross-check with `ROADMAP.md` |
| `ROADMAP.md` | Forward plan; consistent with `STATUS_OF_UBT.md` |
| `FLAGSHIP_SELECTION.md` | Selection rationale; historical — GR is already selected |
| `MILESTONE_REVIEW.md` | Historical milestone record; archive candidate |
| `STEERING_MEMO_AFTER_PRIORITIES_PR.md` | Governance memo; historical |
| `PAPER_OUTLINE.md` | Paper planning; superseded by actual paper `papers/UBT_GR_Submission.tex` |
| `REPRODUCE_TOP_RESULTS.md` | Reproduction guide; useful — keep active |
| `REVIEWER_ATTACK_REPORT.md` | Reviewer analysis; absorbed into `reports/GR_REVIEW_MASTER.md` |
| `PROOF_GAP_CLOSURE.md` | Gap closure tracking; cross-check with `reports/GR_final_gap_checklist.md` |
| `DERIVATION_INDEX.md` | Index of all derivations; keep active as navigation aid |
| `SM_CLOSURE_MATRIX.md` | SM gauge sector matrix; cross-check with `GAUGE_MASTER_STATUS.md` |

**Recommendation**: In a future cleanup session, move `ALPHA_BREAKTHROUGH_REPORT.md`,
`ALPHA_FINAL_OFFENSIVE.md`, `ALPHA_PROGRESS_REPORT.md`, `MILESTONE_REVIEW.md`,
`STEERING_MEMO_AFTER_PRIORITIES_PR.md`, `PAPER_OUTLINE.md`, `FLAGSHIP_SELECTION.md`
to `ARCHIVE/` with a redirect stub left at the root level.

---

## Files NOT Touched (Core Theory)

All LaTeX source files in `canonical/`, `papers/`, and `canonical/gr_closure/`
were not modified.  See `reports/GR_cleanup_nonimpact_confirmation.md` for the
full GR verification.
