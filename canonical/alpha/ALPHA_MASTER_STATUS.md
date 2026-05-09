<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# ALPHA_MASTER_STATUS.md — T3_ALPHA Canonical Master Status

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Single authoritative file consolidating all alpha-program status.
Supersedes and summarises: `reports/alpha_routes_ranked.md`, `reports/alpha_no_fit_progress.md`,
`reports/alpha_missing_lemma.md`, `canonical/alpha/prime_137_status.md`,
`reports/ew_mixing_status.md` (alpha perspective), `canonical/alpha/ew_mixing_gap_map.md`
(alpha routes only).  
**Truth anchor**: `STATUS_OF_UBT.md §T3_ALPHA`

---

## Objective

Derive α⁻¹_bare = 137 (integer) from UBT without fitting any parameter.  
Full derivation (137.036) requires solving Gap G137-B first.

**Acceptance criteria**:
1. No number is fitted to reproduce α or 137.
2. Every numerical input is derived from another UBT sector or from S[Θ].
3. Every step is reproducible from a cited proof file.

---

## Current Overall Status

| Item | Verdict |
|------|---------|
| α derivation: overall | **NOT DERIVED** — B-gap open |
| α⁻¹_bare = 137 (integer) | **CONDITIONAL ONLY** — no first-principles closure |
| α⁻¹ = 137.036 (full precision) | **NOT ACHIEVED** — requires Gap G137-B resolution |
| Active routes | 1 (A_PRIME) |
| Parked routes | 2 (A1, A2 — conditional on dead-end Weinberg angle) |
| Killed routes | 2 (A3, A4 — definitively failed) |

### Status sync (2026-05-09)

- Prime-stability set: **derived**
- B-gap: **open**
- eta(i) route: **best candidate, research/proposal only**
- Hecke path-integral route: **current no-go** (until O1–O3 or determinant-to-B insertion is solved)
- Canonical wording source: `reports/alpha_current_verdict.md`

---

## Route Ranking

### PRIMARY — A_PRIME: V_eff Prime Attractor

**Claim**: α⁻¹_bare = 137 (integer) from winding-mode spectrum V_eff minimum  
**Score**: 14/15  
**Status**: **PRIMARY ROUTE**

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 3/3 | N_eff = 12 is [L0]; V_eff structure forced by algebra |
| Independence from α | 3/3 | No α input; B derived from action (Gap G137-B pending) |
| Gap clarity | 3/3 | One gap: G137-B — derive B = B_phenom from S[Θ] |
| Corroborations | 3/3 | V_eff attractor + modular μ(Γ₀(137))/3 + Hecke lepton masses |
| Path to completion | 2/3 | Modular bootstrap; 4-week time-box |

**What is proved** (no fitting, zero free parameters):

| Claim | Level | Source |
|-------|-------|--------|
| N_eff = 12 from ℂ⊗ℍ algebra alone | [L0] | `canonical/algebra/` |
| V_eff(n) = n² − B·n·ln n structure | [L1] | `canonical/alpha/alpha_best_route.tex` |
| n*(B_phenom) = 137 for B_phenom ≈ 46.298 | [L1] (given B) | `canonical/alpha/alpha_best_route.tex` |
| 137 is prime — consistent with V_eff stability | [L0]+[STD] | Number theory |
| B₀ = 8π from S_kin[Θ] (one-loop) | [L1] | `canonical/t_munu/` |

**What is open** (Gap G137-B):  
- Derive B_phenom ≈ 46.298 from UBT action S[Θ] without using α as input.
- B₀ = 8π (proved, one-loop) gives n* ≈ 65, not 137.
- Missing factor ≈ 1.84 = Kac-Moody correction or higher-loop term.
- Source: `reports/alpha_missing_lemma.md`

**Corroborations** (not proofs, supporting evidence):

| Signal | Value | Significance |
|--------|-------|--------------|
| μ(Γ₀(137))/3 | ≈ 46.00 (0.64% from B_phenom) | Independent structural signal |
| Hecke eigenvalue → lepton mass ratios | 0.02–0.1% accuracy | Independent of V_eff |
| P¹(𝔽₁₃₇) cardinality = μ(Γ₀(137)) | Exact identity | Number-theoretic self-consistency |

**Kill condition**: A_PRIME would be killed only if N_eff = 12 fails (extremely
unlikely — this is an [L0] algebraic identity).

---

### PARKED — A1: Gauge Normalization

**Status**: PARKED — conditional on Gap EW-1 (Weinberg angle — **DEAD END**)  
**Score**: 7/15

**Blocker**: Requires sin²θ_W from algebra (Gap EW-1).  Gap EW-1 = DEAD END.  
**Revival condition**: Only if Gap EW-1 is somehow closed in T2_GAUGE track.  
**Active priority**: ZERO.

---

### PARKED — A2: Symmetry-Breaking Projection

**Status**: PARKED — same blocker as A1 (EW-1 + EW-2)  
**Score**: 7/15

**Blocker**: EW-1 (DEAD END) and EW-2 (OPEN).  
**Active priority**: ZERO.

---

### KILLED — A3: Theta/Modular Route

**Status**: **DEFINITIVELY FAILED**  
**Score**: 3/15

**Failure**: Exhaustive search over modular invariants, Hecke eigenvalues, j-invariants,
and eta functions found no expression equal to α⁻¹ = 137.036.  
**Archive**: `reports/failed_routes_graveyard.md`  
**Active priority**: ZERO — closed permanently.

---

### KILLED — A4: Layer 2 Coding Constraint

**Status**: **DEFINITIVELY FAILED**  
**Score**: 2/15

**Failure**: Proved impossible — coding constraints fix charge spectrum (integer or
half-integer multiples of a unit charge), not the magnitude of the unit charge.
α = e²/(4π) requires coupling magnitude, which depends on UV cutoff and renormalization
scheme — neither determined by coding constraints.  
**Archive**: `reports/failed_routes_graveyard.md`  
**Active priority**: ZERO — closed permanently.

---

### SUPPORTING (Not a Bare-α Route) — A5: One-Loop QED Running

**Status**: SUPPORTING RESULT only  
**Score**: 8/15

**Value**: Validates QED sector of UBT; reproduces SM one-loop running α(μ₂) from α(μ₁).  
**Limitation**: Uses α as input; cannot determine bare α from first principles.  
**Source**: `canonical/interactions/qed.tex`

---

## Summary Ranking Table

| Rank | Route | Score | Status | Claim |
|------|-------|-------|--------|-------|
| 1 | **A_PRIME**: V_eff prime attractor | **14/15** | **PRIMARY** | α⁻¹_bare = 137 (integer), conditional on G137-B |
| 2 | A5: One-loop running | 8/15 | SUPPORTING (not bare-α) | α(μ₂) from α(μ₁) |
| 3 | A1: Gauge normalization | 7/15 | PARKED (EW-1 dead end) | α after θ_W fixed |
| 4 | A2: Symmetry-breaking projection | 7/15 | PARKED (EW-1+EW-2) | α after SSB |
| 5 | A3: Theta/modular | 3/15 | **KILLED** | Failed |
| 6 | A4: Layer 2 coding | 2/15 | **KILLED** | Failed (proved impossible) |

---

## Next 30-Day Attack Plan

### Week 1–4: Modular Bootstrap on Gap G137-B

**Target**: Derive B = μ(Γ₀(n*))/3 from S[Θ] evaluated at n* = 137.

**Approach**:
1. Compute S[Θ] for the winding-mode ansatz at n = 137.
2. Evaluate the Kac-Moody level k from the WZW boundary term.
3. Check if k = 1 follows from the boundary structure of S[Θ].
4. Alternatively: evaluate one-loop correction beyond B₀ = 8π using
   heat-kernel on S¹_ψ × M⁴.

**Resources**:
- `reports/alpha_missing_lemma.md` — exact formulation of G137-B
- `canonical/t_munu/` — B₀ = 8π derivation (starting point)
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation chain
- `reports/prime_137_structural_audit.md` — corroborations

**Go/no-go at Week 4**:
- **If solved** → write T3_ALPHA paper; claim α⁻¹_bare = 137 at [L1]; submit as
  companion note to T1_GR.
- **If not solved** (70–80% probability) → publish conditional integer-137 note
  with Gap G137-B explicitly stated; downgrade T3_ALPHA from flagship to
  STRUCTURAL EVIDENCE status; redirect effort fully to T2_GAUGE.

---

## What Is Not Being Pursued

| Route | Reason |
|-------|--------|
| Weinberg angle derivation | DEAD END — algebra cannot fix g'/g |
| Route A3 (modular direct) | KILLED — exhaustive search failed |
| Route A4 (coding) | KILLED — proved impossible |
| δ = 0.036 correction without α | CIRCULAR — uses α as input |
| R_ψ calibration from m_e | SEMI-EMPIRICAL — breaks unit-free derivation |
| New speculative routes | FORBIDDEN — no new branches in cleanup window |

---

## Source Files

| Purpose | File |
|---------|------|
| Full route ranking with scores | `reports/alpha_routes_ranked.md` |
| Primary route detail | `canonical/alpha/PRIMARY_ROUTE.md` |
| Gap G137-B exact statement | `reports/alpha_missing_lemma.md` |
| Prime 137 structural roles | `canonical/alpha/prime_137_status.md` |
| Failed routes archive | `reports/failed_routes_graveyard.md` |
| V_eff derivation chain | `canonical/alpha/alpha_best_route.tex` |
| No-fit audit | `reports/alpha_no_fit_audit.md` |
| No-fit progress | `reports/alpha_no_fit_progress.md` |
