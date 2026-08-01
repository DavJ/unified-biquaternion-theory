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


# FLAGSHIP_SELECTION.md

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Evidence-based selection of one track for the first flagship publication.  
**Sources**: `research_tracks/T1_GR/`, `research_tracks/T2_GAUGE/`,
`research_tracks/T3_ALPHA/`, `MILESTONE_REVIEW.md`

---

## Decision

**Selected track**: **T1_GR — General Relativity Recovery**

**Flagship paper title**: *General Relativity as a Real-Projected Limit of Unified
Biquaternion Theory*

---

## Selection Rationale

### Readiness comparison

| Criterion | T1_GR | T2_GAUGE | T3_ALPHA |
|-----------|-------|----------|----------|
| Proved steps (no outstanding caveats) | 9/9 core steps [L1] | 9/9 core steps [L0]; C1 open | 3/7 clean steps; k=1 open |
| Remaining blockers | 0 hard; 2 open [L2] (stated as open) | 1 medium (C1 chirality, ~2 wk) | 3 critical (B_base, δ, R_ψ) |
| Paper outline exists | Yes — fully mapped | Partial | No coherent path |
| Theorem chain exists | Yes — LaTeX draft (`theorem_chain.tex`) | No | No |
| Numerical verification | Yes — Schwarzschild, error < 10⁻⁸ | Yes — 8 Gell-Mann generators | Partial — V_eff only |
| Confidence of submission | 85% | 65% (after C1) | 15% |
| Estimated weeks to arXiv | 12 | 10 (if C1 closed) | >20 (if ever) |

### Why T1_GR is chosen

1. **Zero hard blockers.** All nine steps in the chain
   Θ → g → Γ → R → G_μν = 8πG T_μν are proved at [L1].  The two remaining
   open problems (GAP-10 off-shell closure, GAP-Z Zerilli equation) are [L2]
   and do not affect the validity of the classical GR recovery result.

2. **LaTeX draft already exists.** `research_tracks/T1_GR/theorem_chain.tex`
   contains the complete theorem chain in publishable form.
   `research_tracks/T1_GR/GR_PAPER_OUTLINE.md` maps every section with
   canonical source files.  This work does not need to be created — it needs
   to be compiled into a paper.

3. **Narrowest, cleanest claim.** The theorem is precisely stated:
   *In the real-sector limit, UBT field equations reduce to Einstein's
   equations.*  This claim is specific, falsifiable, and self-contained.
   Reviewers can verify it without knowing the rest of UBT.

4. **Numerical verification included.** `tools/verify_schwarzschild_theta.py`
   demonstrates the Schwarzschild metric recovery to relative error < 10⁻⁸.
   Independent numerical confirmation is a standard requirement for claims of
   this type.

5. **Regge-Wheeler included.** Deriving the odd-parity graviton equation without
   additional input is a non-trivial independent result that strengthens the paper.

6. **Credibility pathway is clear.** The target journals (Journal of Mathematical
   Physics, Classical and Quantum Gravity) have published exact GR recovery
   results from alternative algebraic frameworks.  The novelty — metric
   *derived* rather than postulated, Lorentzian signature proved not assumed —
   is immediately recognisable to reviewers.

---

## Why T2_GAUGE Is Postponed

T2_GAUGE is the second-strongest track and will be submitted within two weeks
of T1_GR.  It is not discarded — it is sequenced.

Reasons for not making it the first flagship:

- **Gap C1 (chirality) is unresolved.** SU(2)_L versus SU(2)_R selection is a
  central claim of the paper and is currently motivated but not proved as a theorem.
  Submitting without this proof would invite immediate rejection or demands for
  major revision.  Formalising the ψ-parity theorem is estimated at 1–2 weeks
  and must precede submission.

- **The derived theorem chain is less advanced.** No LaTeX theorem chain
  equivalent to `theorem_chain.tex` exists for the gauge sector.  More
  write-up work remains.

- **The claim is broader and harder to defend.** Deriving SU(3) × SU(2)_L × U(1)_Y
  from one algebra is a larger result.  Larger claims require proportionally stronger
  write-ups and invite proportionally harder scrutiny.  T1_GR, being narrower, is
  lower-risk as a first publication.

**Action**: While T1_GR is being drafted, close Gap C1 in parallel.  Activate
T2_GAUGE draft immediately after T1_GR draft is complete.

---

## Why T3_ALPHA Is Postponed

T3_ALPHA is not ready for submission.  Three critical assumptions remain unresolved:

| Gap | Type | Impact |
|-----|------|--------|
| B_base exponent (k=1, Kac-Moody level) | MC — motivated conjecture; 27+ approaches exhausted | Blocks the bare α⁻¹ = 137 claim |
| δ = 0.036 correction | Circular — uses α as input | Invalidates first-principles claim |
| R_ψ physical calibration | Semi-empirical — uses m_e | Breaks unit-free derivation |

A paper claiming a first-principles derivation of α without resolving these
gaps would not survive peer review.  A minimal paper claiming only
"α⁻¹_bare = 137 from UBT" is possible *if and only if* k=1 is proved —
which remains unachieved after 27+ attempts.

**Action**: Time-box one more attempt (modular bootstrap, 4 weeks).
If no progress, drop the α claim and redirect effort to T1 + T2 writing.

---

## Remaining Blockers for T1_GR

| Blocker | Type | Action |
|---------|------|--------|
| Zerilli equation (even-parity graviton) | [L2] open — does not block | State explicitly as open problem in paper |
| Off-shell Θ-only closure (GAP-10) | [L2] open — does not block | State explicitly with full obstruction map |
| Notation unification across canonical/ | Editorial | Complete during Sections 2–5 draft |
| Regge-Wheeler source (canonical file) | Write-up gap | Located in linearised GR analysis; needs clean write-up |

**No remaining blocker prevents submission.**

---

## Estimated Time to Paper-Ready

| Milestone | Weeks from now |
|-----------|---------------|
| Notation unification pass | 1 |
| Draft Sections 2–5 (foundations + GR chain) | 4 |
| Draft Section 6 (Schwarzschild + Regge-Wheeler) | 6 |
| Draft Sections 1, 7, 8, appendices | 8 |
| Internal consistency and completeness check | 9 |
| arXiv submission | 12 |

These estimates assume one person working primarily on this paper.

---

## Success Criteria

A successful submission achieves the following:

1. Complete, self-contained proof of the five-step GR chain (Theorems 1–5).
2. Schwarzschild metric recovered with explicit Θ ansatz and numerical verification.
3. Regge-Wheeler equation derived without additional input.
4. GAP-10 and GAP-Z stated as open problems with precise obstruction maps.
5. No claim exceeds what is proved.
6. Submitted to arXiv and a peer-reviewed journal within 12 weeks.
