<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

## Immediate programme update — 2026-07-27

The active GR/quantum bridge is the canonical-relation generalized-Dirac route.
No second spinor-current tetrad is to be developed as a competing metric.

| Order | Proof target | Exit criterion |
|---|---|---|
| 1 | Derive the generalized-Dirac operator from one UBT action over `tau=t+i psi` | First-order Euler--Lagrange equation with all coefficients and involutions fixed; no independent metric/tetrad/connection inserted |
| 2 | Close the implicit local system `Theta -> E -> Gamma -> omega(E) -> D Theta` | Local existence theorem on a stated non-null/nondegenerate class, or a precise no-go theorem |
| 3 | Prove Lorentz-slice preservation and nondegeneracy | Constraint propagation theorem under the derived evolution |
| 4 | Prove on-shell rank 10 | Rank of admissible metric variations after equations, gauge and complex-time constraints is exactly 10 (or six physical directions modulo diffeomorphisms, with constraints handled explicitly) |
| 5 | Derive low-energy GR and quantum limits | Einstein branch and Dirac/Schrodinger limits obtained from the same action with assumptions isolated |

The exact kinematic Clifford lift, rank-ten tetrad theorem and fifth grading
channel are already closed.  The archived current-tetrad branch is historical
evidence only.

<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# ROADMAP.md — UBT Development Roadmap

**Author**: Ing. David Jaroš  
**Date**: 2026-05-14  
**Purpose**: Forward-looking plan for the next 21 days and beyond.
Based on current proof status; no aspirational items without a clear path.

---

## Current State (2026-05-13)

- T1_GR paper is submit-ready (`papers/UBT_GR_Submission.tex`)
- GAP-Z (Zerilli, even-parity graviton) is PROVED [L1]; the canonical proof is documented in `canonical/gr_closure/zerilli_derivation.tex` and matches the GR paper. All status files now list this as a closed gap.
- T2_GAUGE theorems are proved; paper not yet written
- T3_ALPHA integer-137 result is conditional on Gap G137-B

---

## Implemented Top-10 Priority/Gaps Program (Execution-Control Layer)

This section operationalizes the current top 10 priorities/gaps from the
authoritative status set:
`STATUS_OF_UBT.md`, `canonical/gauge/GAUGE_MASTER_STATUS.md`,
`canonical/alpha/ALPHA_MASTER_STATUS.md`.

**Execution order (locked):** **1 → 2 → (3,4 in parallel) → 5/6/7/8/9 → 10**

| # | Priority / Gap | Implementation instruction | Exit criterion |
|---|----------------|----------------------------|----------------|
| 1 | Publish T1_GR (submit-ready) | Finalize arXiv + journal submission package from `papers/UBT_GR_Submission.tex`; include canonical proof references; keep GAP-10 explicitly labeled open/non-blocking. | Submission confirmation IDs recorded; GAP-10 statement present in manuscript. |
| 2 | Complete and submit T2_GAUGE paper | Consolidate proved algebraic claims into one canonical manuscript; include explicit no-go statement that pure algebra cannot fix g'/g (Weinberg dead-end statement). | T2_GAUGE manuscript submitted with dead-end wording retained. |
| 3 | Close G137-B (alpha blocker) | Run one focused first-principles route only (modular bootstrap / equivalent strict path) to derive \(B_{\mathrm{phenom}}\) from \(S[\Theta]\) without alpha input; enforce hard go/no-go gate. | Either [L1] closure of G137-B or formal no-go/conditional downgrade memo. |
| 4 | Resolve N_eff loop-counting audit | Close multiplicity-factor audit in **loop-counting** branch (not SU(2) twist, which is [L1]). | `N_eff` status upgraded from OPEN/[MC] to proved, or frozen as explicitly unresolved with blocker proof note. |
| 5 | Close C2 hypercharge-assignment gap | Derive specific fermion hypercharge assignments from UBT structure, including uniqueness conditions and admissible-class boundaries. | C2 moved from OPEN to proved/conditional with full theorem assumptions stated. |
| 6 | Upgrade EW-1b (or kill) | Complete first-principles EW+RG closure including \(R_\psi\) origin from \(S[\Theta]\); if closure fails, formally downgrade/kill EW-1b route. | EW-1b reclassified to PROVED or KILLED (no ambiguous middle state). |
| 7 | Address EW-2 Higgs-VEV gap | Open Higgs-focused derivation track/paper; derive Higgs doublet VEV from \(S[\Theta]\) with assumptions isolated from gauge theorem claims. | EW-2 status moved from deferred/open to explicit proved/conditional theorem statement. |
| 8 | Address Y2 Yukawa/fermion-mass gap | Build first-principles fermion mass/coupling program while keeping KK-mismatch constraints explicit and non-negotiable. | Y2 status moved from OPEN to formally scoped theorem program with closed sub-lemmas or explicit impossibility statements. |
| 9 | Close anomaly first-principles gap | Derive anomaly cancellation from UBT-first principles (not assumed SM assignments), or mark exactly which anomalies remain conditional. | Anomaly section upgraded from conditional to proved or fully partitioned open items with blockers. |
| 10 | Produce one unique falsifiable prediction beyond ΛCDM+SM | Prioritize one parameter-controlled, discriminative observable (e.g., mirror-sector quantitative signature or robust cosmology discriminator) and define falsification protocol up front. | Public pre-registered prediction sheet with parameter bounds and fail/pass criterion. |

**Governance constraints**
- No speculative track expansion while items 1–4 are unresolved.
- No new alpha routes outside the active portfolio gate process.
- Every status change above must be mirrored same-day in `STATUS_OF_UBT.md`.

---

## Phase 1: First Public Release (Weeks 1–3)

### Week 1

| Task | Owner | Status |
|------|-------|--------|
| Fix Newton's G clarification in §3.5 of UBT_GR_Submission.tex | DJ | ✅ Done (2026-05-10) |
| Include canonical files as arXiv ancillary material | DJ | Prepare on submission |
| Submit T1_GR to arXiv (gr-qc or math-ph) | DJ | Target: end of week 1 |
| Submit T1_GR to Classical and Quantum Gravity or JMP | DJ | Simultaneous with arXiv |

### Week 2

| Task | Owner | Status |
|------|-------|--------|
| Begin T2_GAUGE paper draft (§1–§3: algebra + SU(3) + SU(2)_L) | DJ | 8-week paper |
| Start modular bootstrap on Gap G137-B (4-week time-box begins) | DJ | Research |
| Status update: `STATUS.md` reflecting arXiv submission | DJ | Maintenance |

### Week 3

| Task | Owner | Status |
|------|-------|--------|
| Continue T2_GAUGE draft (§4: U(1)_Y, §5: three generations) | DJ | — |
| Midpoint assessment of Gap G137-B progress | DJ | Go/no-go at week 4 |

---

## Phase 2: T2_GAUGE Submission (Weeks 4–10)

### Weeks 4–6: Paper core

| Task | Notes |
|------|-------|
| T2_GAUGE §6: electroweak sector with honest dead-end statement on θ_W | Critical |
| T2_GAUGE §7: chirality result (Gap C1 closed) | Theorem write-up |
| T2_GAUGE §8: open problems (C2, EW-2, Y2, confinement) | Honest accounting |
| Gap G137-B: complete modular bootstrap attempt | Go/no-go by week 4 |

### Weeks 7–8: T2_GAUGE completion

| Task | Notes |
|------|-------|
| Internal review pass | — |
| arXiv submission of T2_GAUGE | Target: week 8 |
| Journal submission | Simultaneous |

---

## Phase 3: T3_ALPHA Decision Point (Week 4)

**Go/no-go decision on Gap G137-B at week 4.**

### Scenario A: Gap G137-B solved

| Task | Notes |
|------|-------|
| Write T3_ALPHA paper: integer-137 result with full proof | 4-week write-up |
| Paper claim: "α⁻¹_bare = 137 from UBT structural argument" | Level [L1] |
| Submit as companion note to T1_GR | Target: week 10–12 |

### Scenario B: Gap G137-B not solved (more likely — 70%)

| Task | Notes |
|------|-------|
| Write short companion note: conditional integer-137 with gap stated | 1–2 weeks |
| Downgrade T3_ALPHA track from flagship to "structural evidence" | Honest status |
| Redirect effort fully to T2_GAUGE and T1_GR revisions | — |

---

## Phase 4: Long-Term Open Problems (Beyond Week 21)

These are not active targets in the 21-day window.

| Problem | Why deferred | Priority |
|---------|-------------|----------|
| Zerilli equation (GAP-Z) | **PROVED [L1]**; canonical proof in `canonical/gr_closure/zerilli_derivation.tex` and GR paper. Both graviton polarisation sectors are now closed at [L1]. | — |
| Chirality C1b (dynamical SU(2)_R exclusion) | Enhances T2_GAUGE but not required | Medium |
| Fermion masses | KK-mismatch theorem — needs new approach | Low |
| Higgs mechanism / W-Z masses | Separate paper | Low |
| Anomaly cancellation from first principles | Requires fermion hypercharge assignments first | Low |
| Quantum UBT / path integral (GAP-Q) | Long-term foundational work | Very long term |
| Cosmological solutions (GAP-C) | FRW Θ ansatz | Low |
| Dynamical confinement | Clay Millennium Problem | Not in scope |

---

## Success Criteria for 21-Day Window

| Criterion | Target | How measured |
|-----------|--------|-------------|
| GR paper on arXiv | ✅ | arXiv submission number |
| GR paper submitted to journal | ✅ | Submission confirmation |
| Repo understandable in 5 minutes | ✅ | README, STATUS, WHAT_IS_PROVED, ROADMAP in place |
| Alpha route decision made | ✅ | PRIMARY_ROUTE.md + weak routes killed |
| Gauge status honest | ✅ | gauge_truth_matrix.md with dead-ends stated |
| T2_GAUGE paper draft started | ✅ | First 3 sections exist |

---

## What Is Not On The Roadmap

The following are explicitly excluded from the 21-day window and the near-term plan:

- New speculative branches (CTC, psychons, consciousness)
- New top-level theory roots
- Consciousness/CCT development
- Papers claiming more than what is proved

---

## Document Update Policy

This roadmap is updated when:
1. A track changes status (submitted/blocked/killed)
2. A gap is solved or declared dead
3. A new critical finding changes priorities

Previous roadmap versions are not deleted — see git history.
