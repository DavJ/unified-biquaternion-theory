<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# ROADMAP.md — UBT Development Roadmap

**Author**: Ing. David Jaroš  
**Date**: 2026-05-13  
**Purpose**: Forward-looking plan for the next 21 days and beyond.
Based on current proof status; no aspirational items without a clear path.

---

## Current State (2026-05-13)

- T1_GR paper is submit-ready (`papers/UBT_GR_Submission.tex`)
- GAP-Z (Zerilli, even-parity graviton) is closed at [L1] via `canonical/gr_closure/zerilli_derivation.tex`
- T2_GAUGE theorems are proved; paper not yet written
- T3_ALPHA integer-137 result is conditional on Gap G137-B

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
| Zerilli equation (GAP-Z) | **Closed [L1] on 2026-05-10**; documented in `canonical/gr_closure/zerilli_derivation.tex` | — |
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
