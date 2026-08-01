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


# GR_final_red_team.md — T1_GR Final Red Team Report (post-RC2)

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T1_GR — General Relativity Recovery  
**Version assessed**: `papers/UBT_GR_RC2.tex`  
**Previous red team**: `reports/GR_hostile_review.md` (on RC1)  
**Verdict**: **SUBMIT** — all items from RC1 red team resolved or confirmed stable.

---

## Summary of Changes from RC1 to RC2

| Item | RC1 status | RC2 action | RC2 status |
|------|-----------|------------|------------|
| H2: AXIOM-B smuggles Lorentz | LOW–MED risk | Added Remark 2.2 explicitly distinguishing η (abstract Clifford bilinear) from g_μν(x) (dynamical field) | **RESOLVED** |
| H6: Missing twistor comparison | LOW risk | Added two sentences in §7.2: Penrose spinor formula g^{ab} = ε^{AB}ε^{A'B'}, key differences explained | **RESOLVED** |
| H7: G is a free parameter | LOW risk (already fixed in RC1) | Already in Theorem 3.5; confirmed in §7.3 | **CONFIRMED** |
| H9: 10⁻¹⁵ overclaim | MINOR | Tightened to < 5×10⁻¹⁵ in abstract, §4.1, Table 1, Appendix B | **RESOLVED** |
| H8: Canonical files not accessible | MINOR | Strategy: include as arXiv ancillary uploads on submission | **STRATEGY SET** |
| H1: Circular metric | LOW | No change needed; remark still adequate | **STABLE** |
| H3: Schwarzschild ansatz | LOW | No change needed; uniqueness proof in canonical file | **STABLE** |
| H4: Zerilli missing | LOW | GAP-Z stated; no change needed | **STABLE** |
| H5: GAP-10 is fatal | MEDIUM | On-shell claim stands; no change needed | **STABLE** |
| H10: Unfalsifiable | MINIMAL | Category confusion; no change needed | **STABLE** |

---

## Outsider Readability Assessment (new in RC2)

Added plain-language preamble at start of §1.1 for non-specialist readers.

| Aspect | RC1 | RC2 | Assessment |
|--------|-----|-----|------------|
| Entry point for non-specialist | Not present | Plain-language §1.1 preamble | **Improved** |
| Table of axioms | Present (Table 2) | Present; referenced in preamble | **Good** |
| Proof sketch vs full proof balance | Good | Good | **Stable** |
| Notation consistency | Good | Good + Remark 2.2 clarification | **Improved** |

---

## Residual Risks After RC2

| Attack | Residual risk | Mitigation status |
|--------|--------------|-------------------|
| H2 | MINIMAL | Remark 2.2 explicitly addresses it |
| H5 (GAP-10 framing) | LOW–MEDIUM | On-shell claim is explicitly bounded; §6 is clear |
| H8 (canonical files) | MINOR | Resolved on arXiv submission |
| Any remaining | LOW or MINIMAL | — |

**No FATAL or MAJOR unresolved issues.**

---

## RC2 Claim Strength Summary (unchanged from RC1, confirmed)

| Category | Count | Level | Verdict |
|----------|-------|-------|---------|
| Exact algebraic facts | 1 | [L0] | Iron-clad |
| Proved theorems | 6 | [L1] | Solid |
| Proved + numerically verified | 1 | [L1]+[NUM] | Strongest |
| Standard results | 1 | [STD] | Uncontroversial |
| Explicitly open gaps | 2 | [OPEN] | Honest |
| Free parameters | 1 | [AX] | Honest — G is input |

**All 9 non-trivial claims at [L1] or above. No overclaims.**

---

## Submission Checklist (Final)

- [x] H7: Newton's G explicitly stated as free parameter (§3.5, Theorem 3.5)
- [x] H9: Numerical claim tightened to < 5×10⁻¹⁵
- [x] H2: §2.2 Remark added — abstract Clifford bilinear vs. physical metric
- [x] H6: Penrose spinor formula comparison added (§7.2)
- [x] Outsider readability preamble (§1.1)
- [x] Both [L2] gaps stated and bounded (GAP-10, GAP-Z)
- [ ] arXiv submission: include canonical files as ancillary uploads

---

## Comparison to Success Criterion

> **Success condition**: release candidate stronger than previous version.

RC2 is stronger than RC1 on every targeted dimension:
- Resolves the two remaining LOW–MEDIUM reviewer risks (H2, H6)
- Improves outsider accessibility
- Tightens numerical claim
- Maintains all proved results unchanged

**Success criterion: MET.**

---

## Next Steps

1. Final editorial proofread (optional but recommended)
2. Submit to arXiv with canonical files as ancillary uploads
3. Submit to Journal of Mathematical Physics or Classical and Quantum Gravity

---

## References

- `papers/UBT_GR_RC2.tex` — assessed document
- `papers/UBT_GR_RC1.tex` — previous version
- `reports/GR_hostile_review.md` — original hostile review (RC1)
- `reports/GR_claim_strength_table.md` — full claim strength detail
- `reports/GR_exact_vs_conditional_table.md` — exact vs conditional table
