<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# STATUS_OF_UBT.md — Single Source of Truth

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Authoritative one-file description of the real current state of every
major UBT track.  All other status files are subordinate to this document.
When in conflict, this file governs.

> **Governance rule**: This file is updated only when a track changes status,
> a gap is solved or killed, or a paper is submitted.  Date every significant change.

---

## Executive Summary

UBT has one submission-ready result (T1_GR), one near-ready result (T2_GAUGE),
and one blocked result (T3_ALPHA).

| Track | Status | Paper | Verdict |
|-------|--------|-------|---------|
| **T1_GR** — GR Recovery | ✅ SUBMIT READY | `papers/UBT_GR_Submission.tex` | Submit to arXiv within 2 weeks |
| **T2_GAUGE** — Gauge Sector | 🔶 NEAR READY | Draft needed | Submit 6–8 weeks after T1_GR |
| **T3_ALPHA** — Fine Structure Constant | 🔴 CONDITIONAL | No paper yet | Blocked on Gap G137-B |

**No speculative tracks are active.**  Consciousness/CTC content is frozen in
`speculative_extensions/`.  No new branches are being opened during the cleanup window.

---

## T1_GR — General Relativity Recovery

**Status**: SUBMIT READY  
**Confidence**: HIGH — all core chain steps proved at [L1]  
**Paper file**: `papers/UBT_GR_Submission.tex`

### Exact Achievements

The five-step chain Θ → g → Γ → R → G_μν = 8πGT_μν is complete at proof level [L1].

| Claim | Level | Source |
|-------|-------|--------|
| Metric g_μν derived from Θ | [L1] | `canonical/gr_closure/step1_metric_bridge.tex` |
| Non-degeneracy det(g) ≠ 0 | [L1] | `canonical/gr_closure/step2_nondegeneracy.tex` |
| Lorentzian signature (−,+,+,+) from AXIOM-B | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` |
| Einstein equations from Hilbert variation | [L1] | Paper §3 |
| T_μν symmetric, ∇^μT_μν = 0 | [L1] | `canonical/geometry/stress_energy.tex` |
| Schwarzschild metric (spatial, < 10⁻¹⁵ error) | [L1]+[NUM] | `tools/verify_schwarzschild_theta.py` |
| Regge-Wheeler equation (odd-parity graviton) | [L1] | Paper §5 |

Comprehensive proof audit: `reports/GR_claim_to_proof_matrix.md`  
Reviewer FAQ: `reports/GR_reviewer_FAQ.md`

### Remaining Blockers

None that prevent submission.

| Gap | Level | Impact |
|-----|-------|--------|
| GAP-Z — Zerilli equation (even-parity graviton) | [L2] Open | Does not block; stated in paper |
| GAP-10 — Off-shell Θ-only closure | [L2] Open | Does not block; stated in paper |

### Pre-Submission Fix Required

Add one sentence clarifying Newton's G = input parameter (§3.5 of paper).

### Next Action

Submit `papers/UBT_GR_Submission.tex` to arXiv (gr-qc or math-ph) and simultaneously
to *Classical and Quantum Gravity* or *Journal of Mathematical Physics*.

---

## T2_GAUGE — Standard Model Gauge Structure

**Status**: NEAR READY — algebraic results proved; paper not yet written  
**Confidence**: HIGH for algebraic sector; MEDIUM for chirality claim  
**Paper**: Draft needed (6–8 week write-up)

### Solved Algebra Pieces (Zero New Work Needed)

All claims below are [L0] algebraic identities or [L1] proved theorems.

| Claim | Level | Source |
|-------|-------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) | [L0] | `canonical/algebra/biquaternion_algebra.tex` |
| 𝔰𝔲(3) from ℤ₂×ℤ₂×ℤ₂ involutions | [L0] | `canonical/su3_derivation/su3_from_involutions.tex` |
| Quarks in **3**, gluons in **8**, EW/strong decoupling | [L0] | `canonical/interactions/sm_gauge.tex` |
| SU(2)_L from left norm-preserving action | [L0] | `canonical/interactions/sm_gauge.tex §SU2` |
| SU(2)_L acts on left-chiral doublets (Gap C1 closed) | [L1] | `canonical/chirality/step3_gap_C1_resolution.tex` |
| U(1)_Y from right scalar phase | [L0] | `canonical/interactions/sm_gauge.tex §U1` |
| U(1)_EM from ψ-cycle phase | [L0] | `canonical/interactions/qed.tex` |
| Three generations from ψ-winding | [L0] | `canonical/n_eff/` |
| Hypercharge quantisation from Dirac condition | [L0] | `canonical/qed_phi_const/appendix_alpha_geometry.tex §1` |

### Open Physical Gaps

| Gap | Description | Priority |
|-----|-------------|----------|
| EW-1 | Weinberg angle sin²θ_W — **DEAD END** (algebra cannot fix g'/g) | Do not pursue; state as dead end in paper |
| EW-2 | Higgs doublet VEV from S[Θ] | Deferred to separate Higgs paper |
| C2 | Specific fermion hypercharge assignments | Open |
| Y2 | Yukawa couplings | Open |
| Dynamical confinement | Wilson loop area law | Clay Millennium Problem |

### Confidence

**Overall**: 85% submit-ready now; 90% after verifying anomaly cancellation.

**Honest dead end to state in paper**: The Weinberg angle sin²θ_W ≈ 0.231 cannot
be derived from algebra alone.  The ratio g'/g is a free parameter in the SU(2)_L × U(1)_Y
kinetic term and cannot be fixed by any continuous deformation of the algebra.
It is a semi-empirical input in UBT.

### Next Action

Begin T2_GAUGE paper draft immediately after T1_GR submission. Target sections 1–3
(algebra, SU(3), SU(2)_L) in weeks 2–3. Target arXiv at week 8–10.

Master status file: `canonical/gauge/GAUGE_MASTER_STATUS.md`

---

## T3_ALPHA — Fine Structure Constant

**Global Objective**: Derive α⁻¹_bare = 137 (integer) without fitting.
Full derivation (137.036) requires solving Gap G137-B first.

**Status**: CONDITIONAL — integer-137 result proved given B = B_phenom; gap remains

### Active Routes

| Route | Status | Confidence | Blocker | Continue? |
|-------|--------|------------|---------|-----------|
| **A_PRIME: V_eff Prime Attractor** | **PRIMARY** | HIGH (conditional) | Gap G137-B | YES — 4-week time-box |

**What is proved in A_PRIME**:
- N_eff = 12 from ℂ⊗ℍ algebra alone [L0]
- V_eff(n) = n² − B·n·ln n structure forced by winding-mode spectrum [L1]
- n*(B_phenom) = 137 for B_phenom ≈ 46.298 [L1] (conditional on B)
- Prime stability of n* is a structural property [L0]

**What remains open in A_PRIME** (Gap G137-B):
- Derive B_phenom ≈ 46.298 from S[Θ] without using α as input.
- B₀ = 8π (one-loop, proved) gives n* ≈ 65, not 137.
- The missing factor ≈ 1.84 corresponds to a Kac-Moody level or higher-loop correction.

### Parked Routes

| Route | Reason | Revival condition |
|-------|--------|-------------------|
| A1: Gauge Normalization | Conditional on Gap EW-1 (Weinberg angle — DEAD END) | Only if EW-1 is somehow solved in T2_GAUGE |
| A2: Symmetry-Breaking Projection | Same blocker as A1 (EW-1 + EW-2) | Same |

### Dead-End Routes

| Route | Verdict | Evidence |
|-------|---------|----------|
| **A3: Theta/Modular Route** | **DEFINITIVELY FAILED** | Exhaustive search — no modular invariant = 137.036 |
| **A4: Layer 2 Coding Constraint** | **DEFINITIVELY FAILED** | Proved impossible: coding fixes spectrum, not coupling magnitude |

Archive: `reports/failed_routes_graveyard.md`

### Strongest Next Move (30-Day Attack Plan)

**Week 1–4**: Modular bootstrap on Gap G137-B.
- Target: derive B = μ(Γ₀(n*))/3 from S[Θ] evaluated at n*.
- Evidence: μ(Γ₀(137))/3 ≈ 46.00 (0.64% from B_phenom); non-trivial structural signal.
- Success = route becomes [L1]; publish integer-137 paper.

**Week 4 decision gate** (go/no-go):
- If G137-B solved → write T3_ALPHA paper; submit as companion to T1_GR.
- If G137-B not solved (70–80% probability) → publish conditional integer-137 note,
  downgrade T3_ALPHA to STRUCTURAL EVIDENCE status, redirect effort to T2_GAUGE.

**Do not pursue** A1, A2, A3, A4.  Dead routes receive zero active priority.

Master status file: `canonical/alpha/ALPHA_MASTER_STATUS.md`

---

## Exploratory Tracks

### Side Ideas Worth Preserving

| Topic | Location | Status | Note |
|-------|----------|--------|------|
| ΔN_eff ≈ 0.046 (CMB-S4 prediction) | `research_tracks/` | OPEN | Above CMB-S4 threshold; publishable as prediction |
| Structural colour confinement (algebraic) | `canonical/su3_derivation/` | PROVED [L0] | Distinct from dynamical confinement; include in T2_GAUGE |
| ASD Weyl condition and twistor correspondence | `canonical/geometry/` | PROVED [L1] | Include in T1_GR appendix or follow-on paper |
| Hecke eigenvalue lepton mass ratios | `research_tracks/hecke_bridge/` | [MC] — strong (0.02%) | Corroborates A_PRIME; preserve, do not publicise as proved |

### Frozen Items

| Topic | Location | Reason frozen |
|-------|----------|---------------|
| Complex Consciousness Theory / Psychons | `speculative_extensions/complex_consciousness/` | No mathematical closure; frozen indefinitely |
| Closed Timelike Curves | `speculative_extensions/appendices/` | Speculative; no experimental anchor |
| p-adic dark sector | `research_tracks/p_universes/` | Interesting; deferred beyond 21-day window |
| Cosmological solutions (GAP-C) | `research_tracks/` | Open; no active effort |

---

## Deprecated Claims

| Old Claim | Where It Appeared | Why Deprecated | Replacement |
|-----------|-------------------|----------------|-------------|
| Weinberg angle derivation is a CRITICAL PRIORITY | `canonical/alpha/weinberg_angle_derivation.md`, `reports/ew_mixing_status.md` | No-go argument proves the algebra cannot fix g'/g; continuous deformations of the SU(2)_L × U(1)_Y embedding change tan θ_W continuously | State as DEAD END in T2_GAUGE paper §6 |
| "Four active α routes" | `canonical/alpha/alpha_derivation_routes.md` (dated 2026-04-27) | Routes A3 and A4 are definitively killed (exhaustive scan + proved impossibility) | One primary route (A_PRIME), two parked, two killed |
| Chirality Gap C1 as merely MOTIVATED [SE] | `reports/gauge_status_matrix.md` (line 70), `reports/chirality_gap.md` | Formal proof exists: `canonical/chirality/step3_gap_C1_resolution.tex` | C1 is [L1] PROVED — SU(2)_L acts on left-chiral doublets |
| α⁻¹ = 137.036 claimed derivable via B_base/k=1 Kac-Moody route | Multiple early α documents | 27+ approaches exhausted; k=1 has not been proved; this specific number is not the claim | Claim is α⁻¹_bare = 137 (integer), conditional on Gap G137-B |

---

## Key Source Files

| Purpose | File |
|---------|------|
| What is proved (complete map) | `WHAT_IS_PROVED.md` |
| GR claim-to-proof matrix | `reports/GR_claim_to_proof_matrix.md` |
| Alpha route ranking | `canonical/alpha/ALPHA_MASTER_STATUS.md` |
| Gauge sector truth | `canonical/gauge/GAUGE_MASTER_STATUS.md` |
| GR flagship paper | `papers/UBT_GR_Submission.tex` |
| Forward plan | `ROADMAP.md` |
| Contradictions resolved | `reports/contradictions_resolved.md` |
| File cleanup log | `reports/files_merged_deleted_redirected.md` |
