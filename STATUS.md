<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# STATUS.md — Current Theory Status Dashboard

**Author**: Ing. David Jaroš  
**Date**: 2026-05-11  
**Update frequency**: Per milestone  
**Purpose**: Single-glance status of every major track.

---

## Overall Status: First External Release Preparation

| Track | Status | Paper | Verdict |
|-------|--------|-------|---------|
| **T1_GR** — GR Recovery | ✅ COMPLETE | `papers/UBT_GR_Submission_v2.tex` | **SUBMIT READY (arXiv upload pending)** |
| **T2_GAUGE** — Gauge Sector | 🔶 NEAR SUBMISSION | `papers/UBT_Gauge_Submission.tex` | Draft complete (2026-05-10) |
| **T3_ALPHA** — Fine Structure Constant | 🔴 CONDITIONAL-WEAK | No paper yet | Blocked on Gap G137-B + N_eff audit gap |
| **Repo public face** | ✅ DONE | This file, README, ROADMAP | Live |

---

## T1_GR — General Relativity Recovery

**Status**: SUBMIT READY

The five-step chain from the fundamental UBT field Θ to Einstein's equations
is complete at proof level [L1].  All known reviewer attacks are preempted.

| Item | Status |
|------|--------|
| Metric derived from Θ | ✅ Proved [L1] |
| Non-degeneracy det(g) ≠ 0 | ✅ Proved [L1] |
| Lorentzian signature (−,+,+,+) from AXIOM-B | ✅ Proved [L1] |
| Einstein equations from Hilbert variation | ✅ Proved [L1] |
| T_μν symmetric, ∇^μT_μν = 0 | ✅ Proved [L1] |
| Schwarzschild metric (spatial, < 10⁻¹⁵ error) | ✅ Proved + verified |
| Regge-Wheeler equation (odd-parity graviton) | ✅ Proved [L1] |
| Zerilli equation (even-parity graviton) | ✅ Proved [L1] — GAP-Z closed (2026-05-10) |
| Off-shell Θ-only closure | ⚪ Open [L2] — GAP-10; stated in paper |

**Submission file**: `papers/UBT_GR_Submission_v2.tex`  
**Pre-submission fix**: ✅ Done — Newton's G clarification added as Remark in §3.5 (2026-05-10)  
**arXiv upload**: Ready — checklist prepared  
**arXiv ID**: Pending assignment

---

## T2_GAUGE — Standard Model Gauge Structure

**Status**: NEAR READY (85% — needs write-up, not new proofs)

Algebraic SU(3) × SU(2)_L × U(1)_Y emergence from ℂ⊗ℍ is proved at [L0].
Chirality gap (C1) is resolved.  Weinberg angle is an honest dead end.

| Item | Status |
|------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) = algebraic foundation | ✅ Proved [L0] |
| SU(3)_c from ℤ₂×ℤ₂×ℤ₂ involutions | ✅ Proved [L0] |
| Quarks in 3, gluons in 8, EW/strong decoupling | ✅ Proved [L0] |
| SU(2)_L from left action | ✅ Proved [L0] |
| U(1)_Y from right phase | ✅ Proved [L0] |
| U(1)_EM from ψ-cycle | ✅ Proved [L0] |
| Three generations from ψ-winding | ✅ Proved [L0] |
| Chirality: SU(2)_L not SU(2)_R (Gap C1 closed) | ✅ Proved [L1] |
| Hypercharge quantisation | ✅ Proved [L0] |
| Weinberg angle sin²θ_W ≈ 0.231 | 🔴 DEAD END — algebra cannot fix g'/g |
| W/Z masses from SSB | ⚪ Deferred to Higgs paper |
| Fermion masses | ⚪ Deferred |
| Dynamical confinement | ⚪ Clay Millennium Problem |

**Submission plan**: Draft LaTeX paper after T1_GR submission.  Target: 2026-06-08 (4 weeks from 2026-05-11).  
**Paper draft**: ✅ `papers/UBT_Gauge_Submission.tex` created and updated (2026-05-10)

---

## T3_ALPHA — Fine Structure Constant

**Status**: CONDITIONAL (integer-137 result; full derivation blocked)

| Item | Status |
|------|--------|
| N_eff = 12 from ℂ⊗ℍ | ⚠ Under critical audit (not promoted) |
| α⁻¹_bare = 137 given B = B_phenom | ⚠ CONDITIONAL-WEAK (depends on unresolved N_eff and B-bridge audits) |
| 137 is structurally selected (prime attractor) | ✅ Structural [L1] |
| B_phenom ≈ 46.298 from UBT action | 🔴 OPEN — Gap G137-B |
| All competing alpha routes | 🔴 KILLED or conditional (see `reports/alpha_routes_ranked.md`) |

**Current plan**: 4-week modular bootstrap on Gap G137-B.
If fails: publish conditional integer-137 result as companion note.

---

## Repository Public Face

| Document | Status |
|----------|--------|
| `README.md` | ✅ Rewritten — 5-minute entry point |
| `STATUS.md` | ✅ This file |
| `WHAT_IS_PROVED.md` | ✅ Complete |
| `ROADMAP.md` | ✅ Complete |

---

## Key Numbers (as of 2026-04-28)

| Metric | Value |
|--------|-------|
| Core proved theorems (T1_GR) | 8 [L1] theorems + 5 [L0] identities |
| Core proved theorems (T2_GAUGE) | 10 [L0] + 1 [L1] |
| Hard open problems | 1 ([L2]: GAP-10; GAP-Z closed 2026-05-10) |
| Dead-end routes | 3 (A3, A4 alpha; Weinberg angle) |
| Tracks ready for submission | 1 (T1_GR) |
| Tracks 6–8 weeks from submission | 1 (T2_GAUGE) |
| Tracks blocked on critical gap | 1 (T3_ALPHA) |
