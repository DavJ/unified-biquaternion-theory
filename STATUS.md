> **GR geometry update (16 July 2026):** Projection-free covariant-tetrad kinematics now closes rank ten, reconstruction of the compatible connection from tetrad and specified torsion, the torsion-free Levi--Civita branch, and the affine Minkowski representer.  Curved two-sided integrability, torsion dynamics, and Einstein dynamics remain open.

<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# STATUS.md — Current Theory Status Dashboard

> **DEPRECATED as status source — see `CLAIMS_MATRIX.md` and `CLAIMS.yaml` (authoritative).**

**Author**: Ing. David Jaroš  
**Date**: 2026-07-16  
**Update frequency**: Per milestone  
**Purpose**: Single-glance status of every major track.

---

## Overall Status: Rigorous GR Closure Revision

| Track | Status | Paper | Verdict |
|-------|--------|-------|---------|
| **T1_GR** — GR Recovery | 🔶 LOCAL CLOSURE PROVED / GLOBAL GAPS OPEN | `papers/UBT_GR_Submission.tex` | **NOT YET SUBMIT READY** |
| **T2_GAUGE** — Gauge Sector | 🔶 NEAR SUBMISSION | `papers/UBT_Gauge_Submission.tex` | Draft complete (2026-05-10) |
| **T3_ALPHA** — Fine Structure Constant | 🔴 CONDITIONAL-WEAK | No paper yet | Blocked on Gap G137-B + N_eff audit gap |
| **Repo public face** | ✅ DONE | This file, README, ROADMAP | Live |

---

## T1_GR — General Relativity Recovery

**Status**: COVARIANT-TETRAD KINEMATICS PARTLY CLOSED; DYNAMICAL BRIDGE OPEN

The active metric is
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,
\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1.
\]
Compact-\(\psi\) fiber averaging is noncanonical. The connection is not an
arbitrary extra field: for specified tetrad and torsion it is uniquely
\(\omega=\mathring\omega(e)+K(T)\); the torsion-free branch is Levi--Civita.
Every constant Lorentz tetrad, including Minkowski spacetime, has an explicit
affine single-\(\Theta\) representer. A naive one-sided invertible torsion-free
curved route is a proved conditional no-go. The two-sided bimodule derivative
removes that obstruction but does not yet prove curved-space existence or
Einstein dynamics.

| Item | Status |
|------|--------|
| Central anticommutator metric | ✅ Proved [L0] |
| Nondegenerate tetrad-to-metric rank | ✅ Rank 10, kernel 6 [L1] |
| Connection from specified tetrad + torsion | ✅ Unique [L1] |
| Torsion-free classical GR connection | ✅ Levi--Civita [L1] |
| Lorentz-slice preservation by compatible transport | ✅ [L1] |
| Constant-tetrad / Minkowski representer | ✅ Explicit [L1] |
| One-sided invertible torsion-free curved route | ⛔ NO-GO [L1, conditional] |
| Two-sided curvature identity/intertwiner | ✅ Identity; route narrowed [L1] |
| Torsion selected by canonical UBT action | ⚪ `GAP-10T-DYN` OPEN |
| Curved single-Θ existence/uniqueness | ⚪ `GAP-10I-CURVED` OPEN |
| Einstein equations from canonical master/action | ⚪ `GAP-10D` OPEN |
| Schwarzschild tetrad/lapse selected on shell | ⚪ `GAP-U2Theta` OPEN |

**Submission file**: `papers/UBT_GR_Submission.tex`  
**Verdict**: not submission-ready until the curved dynamical bridge is closed.

---

## T2_GAUGE — Standard Model Gauge Structure

**Status**: NEAR READY (85% — needs write-up, not new proofs)

Algebraic SU(3) × SU(2)_L × U(1)_Y emergence from ℂ⊗ℍ is proved at [L0].
Chirality gap (C1) is resolved.  Weinberg angle is a dead end for pure algebra,
with a conditional EW-1b (EW1+RG) branch still tracked.

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
| Weinberg angle sin²θ_W ≈ 0.231 | 🟠 CONDITIONAL OPEN — pure algebra is dead end; EW-1b (EW1+RG) remains conditional |
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

## Key Numbers (as of 2026-05-13)

| Metric | Value |
|--------|-------|
| Core proved theorems (T1_GR) | 8 [L1] theorems + 5 [L0] identities |
| Core proved theorems (T2_GAUGE) | 10 [L0] + 1 [L1] |
| Hard open problems | GAP-10T-DYN, GAP-10I-CURVED, GAP-10L-DYN, GAP-10D, GAP-10ψ, GAP-U2Theta, GAP-B-MASTER |
| Dead-end routes | 3 (A3, A4 alpha; Weinberg pure-algebra route EW-1) |
| Tracks ready for submission | 0 pending GR closure audit |
| Tracks 6–8 weeks from submission | 1 (T2_GAUGE) |
| Tracks blocked on critical gap | 1 (T3_ALPHA) |
