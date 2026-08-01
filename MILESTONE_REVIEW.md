<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# MILESTONE_REVIEW.md — Flagship UBT Priorities

> **DEPRECATED / SUPERSEDED STATUS: This document contains pre-audit alpha claims. Current alpha status is given by STATUS_OF_UBT.md and canonical/alpha/ALPHA_MASTER_STATUS.md.**
> Audit references: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`, `reports/gamma_entropy_alpha_interpolation_audit.md`.


**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Scope**: Tracks T1_GR, T2_GAUGE, T3_ALPHA  
**Purpose**: Evidence-based assessment of current status; inform resource reallocation decisions.

---

## 1. Summary Table

| Track | Objective | Confidence | Blocker severity | Breakthrough probability | Recommended action |
|-------|-----------|-----------|-----------------|-------------------------|--------------------|
| T1_GR | Paper-grade GR recovery | **HIGH (85%)** | Low | High | Begin draft immediately |
| T2_GAUGE | SM gauge structure paper | **HIGH (80%)** | Low–Medium | High | Begin draft; formalise chirality gap |
| T3_ALPHA | Closed first-principles α | **LOW (15%)** | Critical | Low | Time-box 4 weeks; activate Layer2 fallback |

---

## 2. T1_GR — General Relativity Recovery

### 2.1 Current Confidence: HIGH (85%)

The GR recovery chain is essentially complete at the proved level:

| Result | Status | Source |
|--------|--------|--------|
| Steps 1–5 (metric emergence through Einstein eqs) | [L1] PROVED | `canonical/gr_closure/` |
| Schwarzschild metric from Θ | [L1] PROVED | `canonical/geometry/biquaternionic_vacuum_solutions.tex` |
| Linearised gravity (graviton propagation) | [L1] PROVED | `canonical/geometry/` |
| Regge-Wheeler (odd-parity perturbations) | [L1] PROVED | `canonical/gr_closure/` |
| ASD / twistor correspondence | [L1] PROVED | `research_tracks/T1_GR/theorem_chain.tex` |

The five remaining gaps (GAP-10, GAP-Z, GAP-M, GAP-Q, GAP-C) are all [L2]
or [L3] and **do not block paper submission**.  They are documented in
`research_tracks/T1_GR/proof_gap_list.md` and will be stated as open problems.

### 2.2 Blockers

| Blocker | Severity | Notes |
|---------|----------|-------|
| Zerilli equation (even-parity perturbations) | **Low** — not required for paper | Regge-Wheeler (odd-parity) already proved |
| Off-shell Θ-only closure (GAP-10) | **Low** — on-shell result sufficient | On-shell non-degeneracy proved |
| Notation unification across canonical/ files | **Medium** — affects readability | Planned in paper writeup phase |

**No hard technical blocker prevents submission** of a rigorous GR recovery paper.

### 2.3 Breakthrough Probability

| Scenario | Probability |
|----------|------------|
| Paper draft complete within 9 weeks | 85% |
| arXiv submission within 12 weeks | 75% |
| Zerilli closed before submission | 25% |
| Off-shell closure before submission | 15% |

### 2.4 Recommended Action

**Begin paper draft now.**  
Priority order for writeup:

1. Notation unification pass across `canonical/gr_closure/`
2. Draft Sections 2–5 (metric, non-degeneracy, signature, GR geometry, Einstein eqs)
3. Draft Schwarzschild + Regge-Wheeler sections
4. Known-solution numerical checks (Schwarzschild, linearised limit)
5. State gaps honestly in discussion section
6. Internal review → arXiv

**Target**: arXiv preprint within 12 weeks.

---

## 3. T2_GAUGE — Standard Model Gauge Structure

### 3.1 Current Confidence: HIGH (80%)

All three SM gauge factors are derived with zero free parameters at [L0]:

| Result | Status | Source |
|--------|--------|--------|
| `ℂ⊗ℍ ≅ Mat(2,ℂ)` isomorphism | [L0] PROVED | `canonical/algebra/` |
| SU(3)_c from ℤ₂×ℤ₂×ℤ₂ involutions (two independent routes) | [L0] PROVED | `canonical/interactions/sm_gauge.tex` |
| Quarks in fundamental 3, gluons in adjoint 8 | [L0] PROVED | `canonical/su3_derivation/` |
| SU(2)_L from left norm-preserving action | [L0] PROVED | `canonical/interactions/` |
| U(1)_Y from scalar phase right action | [L0] PROVED | `canonical/interactions/` |
| U(1)_EM from ψ-cycle phase | [L0] PROVED | `canonical/interactions/` |
| Three generations from ψ-winding modes | [L0] PROVED | `canonical/fields/` |
| EW/strong decoupling | [L0] PROVED | `canonical/interactions/` |
| Structural colour confinement | [L0] + experimental support | `canonical/su3_derivation/` |

**No other framework derives all three SM gauge factors from a single 8-dimensional
real algebra with zero free parameters.**  The paper's core claim is solid.

### 3.2 Blockers

| Blocker | Severity | Notes |
|---------|----------|-------|
| Chirality gap (SU(2)_L vs SU(2)_R) | **Medium** — must be addressed before submission | ψ-parity theorem exists but needs formalisation; see `T2_GAUGE/missing_axioms.md §C1` |
| Weinberg angle θ_W | **Low (stated limitation)** — confirmed dead end from ℂ⊗ℍ alone | State as limitation in paper |
| Higgs mechanism / λ gap ×11 | **Low for this paper** — defer to separate Higgs paper | |
| Fermion mass spectrum | **Low for this paper** — defer | |
| Strong coupling g_s | **Low (open problem)** — state as open | |

**Only one medium blocker**: chirality gap C1.  Formalising the ψ-parity theorem
is estimated at 1–2 weeks and must precede submission.

### 3.3 Breakthrough Probability

| Scenario | Probability |
|----------|------------|
| Chirality gap C1 formalised within 2 weeks | 70% |
| Paper draft complete within 8 weeks | 75% |
| arXiv submission within 10 weeks | 65% |
| Weinberg angle closed from algebra alone | 5% (dead end confirmed) |
| Higgs λ gap closed | 20% (separate track needed) |

### 3.4 Recommended Action

**Immediate step**: Formalise the ψ-parity chirality theorem (GAP C1).  
**Then**: Begin paper draft.

Priority order:

1. Formalise ψ-parity theorem → close C1 (1–2 weeks)
2. Draft algebraic foundation sections (isomorphism, involutions)
3. Draft SU(3), SU(2)_L, U(1)_Y, U(1)_EM sections
4. Anomaly checks and consistency section
5. Draft Higgs/Yukawa dependency map (open problems section)
6. Internal review → arXiv

**Target**: arXiv preprint within 10 weeks (after C1 formalisation).

---

## 4. T3_ALPHA — Fine Structure Constant Derivation

### 4.1 Current Confidence: LOW (15%)

The α derivation is **structurally incomplete** due to three unresolved assumptions:

| Item | Status | Notes |
|------|--------|-------|
| N_eff = 12 from ℂ⊗ℍ modes | [L0] PROVED — clean | Zero free parameters |
| B₀ = 8π one-loop coefficient | [L1] PROVED — clean | |
| V_eff minimum gives n* = 137 | [L1] PROVED given B_base | Conditional on B_base |
| **B_base = N_eff^{3/2} = 41.57** | **[MC] MOTIVATED CONJECTURE** | **k=1 Kac-Moody not proved** |
| Correction δ = 0.036 | [SE] SEMI-EMPIRICAL | Uses α and m_e as input — circular |
| R_ψ in physical units | [OPEN HARD] | Requires m_e derivation |

### 4.2 Blockers

| Blocker | Severity | Notes |
|---------|----------|-------|
| k=1 (Kac-Moody level) | **CRITICAL** | 27+ approaches exhausted; modular bootstrap is the last viable route |
| δ = 0.036 correction | **CRITICAL** | Currently uses α as input — directly circular; not acceptable for first-principles claim |
| R_ψ physical calibration | **CRITICAL** | Requires m_e derivation — out of scope of α track alone |

All three critical blockers must be resolved to claim a first-principles derivation.
The **minimum viable claim** — "UBT predicts α⁻¹_bare = 137" — requires only the k=1
proof and accepting the bare value.

### 4.3 Breakthrough Probability

| Scenario | Probability |
|----------|------------|
| k=1 proved via modular bootstrap within 4 weeks | 20% |
| Minimal claim (α⁻¹_bare = 137) published | 30% (requires k=1 proof) |
| Full first-principles α derivation (δ included) | 8% |
| Blocking breakthrough within 6 months | 15% |

**The Layer2 coding paper (see `T3_ALPHA/fallback_layer2_outline.md`) has a
much higher breakthrough probability (~85%) and is independent of the B_base gap.**

### 4.4 Recommended Action

**Time-box the α track to 4 weeks** for a single focused attempt:

1. Attempt modular bootstrap approach (compute partition function Ẑ(τ) = ϑ₃³(τ),
   apply crossing symmetry, attempt to fix k from consistency conditions).
2. If k=1 follows: draft the minimal "α⁻¹_bare = 137" paper.
3. If modular bootstrap is blocked after 4 weeks: **activate Layer2 fallback immediately**.

**Do not** continue variants of approaches H2–H27.  They are documented and exhausted.

**Activate Layer2 paper in parallel now** — it does not compete with the α attempt
and can be submitted independently.  See `T3_ALPHA/fallback_layer2_outline.md` for
the full outline.

---

## 5. Recommended Resource Reallocation

### 5.1 Current resource distribution (estimated)

| Track | Current effort share |
|-------|---------------------|
| T1_GR | 35% |
| T2_GAUGE | 30% |
| T3_ALPHA | 35% |

### 5.2 Recommended distribution

| Track | Recommended effort share | Rationale |
|-------|--------------------------|-----------|
| T1_GR | **40%** | Highest readiness; paper can be submitted in 12 weeks |
| T2_GAUGE | **35%** | High readiness; one medium blocker (C1) to close first |
| T3_ALPHA (modular bootstrap attempt) | **15%** | Time-boxed; single focused route |
| T3_ALPHA (Layer2 coding paper) | **10%** | Activate immediately; independent of B_base |

### 5.3 Publication priority order

| Priority | Paper | Estimated submission |
|----------|-------|---------------------|
| 1 | T2_GAUGE — SM gauge structure from ℂ⊗ℍ | +10 weeks |
| 2 | T1_GR — GR recovery from UBT | +12 weeks |
| 3 | T3_ALPHA Layer2 — Gray code / SU(3) coding paper | +8 weeks (if activated now) |
| 4 | T3_ALPHA minimal — α⁻¹_bare = 137 | +16 weeks (conditional on k=1 proof) |

**The Layer2 coding paper (Priority 3) could be the first published UBT output**
if activated now — it is the lowest-risk, highest-visibility near-term deliverable.

### 5.4 Decision gates

| Date (from now) | Decision |
|-----------------|----------|
| +4 weeks | Evaluate modular bootstrap progress.  If no k=1 proof: drop α attempt, redirect 15% to T1+T2 writing |
| +8 weeks | Layer2 paper first draft complete |
| +10 weeks | T2_GAUGE paper submitted to arXiv |
| +12 weeks | T1_GR paper submitted to arXiv |
| +16 weeks | Full milestone review: assess α track vs. other open problems |

---

## 6. Cross-Track Dependencies

| Dependency | Impact |
|------------|--------|
| B_base gap (T3_ALPHA) → stated as open in T1_GR and T2_GAUGE papers | Low — does not block either paper |
| Chirality gap C1 (T2_GAUGE) → independent of T1_GR and T3_ALPHA | None |
| R_ψ physical calibration (T3_ALPHA) → required for full α but not for GR or gauge paper | None for T1/T2 |
| Notation unification (T1_GR) → shared notation needed in T2_GAUGE paper | Low — coordinate during writeup phase |

**The three tracks are largely independent.**  T1_GR and T2_GAUGE can be written
up in parallel without waiting for T3_ALPHA.

---

## 7. Intellectual Honesty Statement

This review records open problems alongside proved results.  The following
must be stated explicitly in any submitted paper:

- **T1_GR**: GAP-10 (off-shell closure) and GAP-Z (Zerilli) are open; they do not
  invalidate the proved results.
- **T2_GAUGE**: Weinberg angle θ_W and fermion masses are not derived; they are
  known limitations, not mistakes.
- **T3_ALPHA**: The B_base exponent (k=1) is a motivated conjecture; the full
  first-principles derivation of α is not yet complete.

Reporting the theory's scope honestly is a scientific strength, not a weakness.

---

## 8. References

| File | Content |
|------|---------|
| `research_tracks/T1_GR/proof_gap_list.md` | Full gap inventory for GR recovery |
| `research_tracks/T1_GR/GR_PAPER_OUTLINE.md` | Paper structure and section plan |
| `research_tracks/T1_GR/theorem_chain.tex` | LaTeX theorem chain |
| `research_tracks/T2_GAUGE/gauge_derivation_map.md` | Full derivation map for SM gauge |
| `research_tracks/T2_GAUGE/missing_axioms.md` | Gap inventory for gauge sector |
| `research_tracks/T2_GAUGE/su3_proof_status.md` | SU(3) proof readiness |
| `research_tracks/T3_ALPHA/alpha_status_report.md` | α derivation status |
| `research_tracks/T3_ALPHA/assumptions_audit.md` | Circularity and assumption map |
| `research_tracks/T3_ALPHA/fallback_layer2_outline.md` | Layer2 coding paper outline |
| `PRIORITIES_2026.md` | Full strategic priorities document |
| `DERIVATION_INDEX.md` | Canonical proof status index |

---

*End of MILESTONE_REVIEW.md*
