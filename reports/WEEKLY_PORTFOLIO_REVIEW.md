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


# WEEKLY_PORTFOLIO_REVIEW.md — UBT Portfolio Review

**Date**: 2026-04-28 (Week 1 of 4)  
**Author**: Ing. David Jaroš  
**Review cycle**: 30-day sprint window  
**Framework**: UBT multi-track portfolio (T1_GR + T2_GAUGE + T3_ALPHA)

---

## Portfolio Progress by Track

### T1_GR — General Relativity Flagship Paper (65% allocation)

**This week**:

| Deliverable | Status |
|-------------|--------|
| `papers/UBT_GR_Flagship.tex` | ✅ DONE — paper-ready flagship created |
| `papers/UBT_GR_Abstract.md` | ✅ DONE — includes proof status table |
| `papers/UBT_GR_Figures/` | ✅ DONE — directory scaffolded |
| `reports/GR_final_gap_checklist.md` | ✅ DONE — all gaps mapped, GO for submission |
| `reports/GR_reviewer_objections_and_answers.md` | ✅ DONE — 9 objections answered |

**Proof status summary**: All mandatory results proved [L1]. Two [L2] gaps
(GAP-10: off-shell Θ-only closure; GAP-Z: Zerilli equation) stated explicitly.
Neither blocks submission.

**Blocker**: None.

**Next action**: Final proofreading pass (1–2 days) → arXiv submission.

---

### T3_ALPHA — Weinberg-Angle Program (20% allocation)

**This week**:

| Deliverable | Status |
|-------------|--------|
| `canonical/alpha/weinberg_angle_routes.md` | ✅ DONE — promoted to canonical |
| `canonical/alpha/ew_mixing_gap_map.md` | ✅ DONE — gap chain EW-1 through EW-4 mapped |
| `reports/alpha_no_fit_progress.md` | ✅ DONE — no-fit status updated |
| `report/polyhedral_weinberg_scan.md` | ✅ DONE — A4, S4, A5 evaluated |

**New finding**: Icosahedral group A5 gives sin²θ = (5−√5)/10 ≈ 0.276 from C₅–C₂
axis projection geometry — cleanest algebraic expression found to date; 19.5%
above sin²θ_W(M_Z) = 0.231. Physical anchor (A5 ⊂ Aut(ℂ⊗ℍ) acting on EW sector)
not yet established.

**Definitive bottleneck**: Gap EW-1 — derive tan θ_W = g'/g from UBT algebra.

**Route status**:
- A1 (algebra normalisation): BLOCKED — equal norms give 1/2 (excluded)
- A2 (SSB projection): BLOCKED at EW-2
- A3 (modular): FAILED
- A4 (coding): FAILED
- **A5-POL (polyhedral, icosahedral)**: NEW CANDIDATE — requires A5 ⊂ Aut(ℂ⊗ℍ)

**Next action**: Investigate A5 as subgroup of Aut(ℂ⊗ℍ) acting on the EW mixing plane.

---

### T2_GAUGE — Gauge Status Matrix (15% allocation)

**This week**:

| Deliverable | Status |
|-------------|--------|
| `reports/gauge_status_matrix.md` | ✅ DONE — promoted to reports |
| `reports/chirality_gap.md` | ✅ DONE — Gap C1 checklist promoted |
| `reports/anomaly_gap.md` | ✅ DONE — per-anomaly audit promoted |
| `reports/higgs_yukawa_dependency.md` | ✅ DONE — Higgs/Yukawa boundary mapped |

**Proved (and safe to claim)**:
- SU(3)_c from ℤ₂×ℤ₂×ℤ₂ involutions [L0]
- SU(2)_L from left-unitary action on Mat(2,ℂ) [L0]
- U(1)_Y from right scalar phase action [L0]
- N_gen = 3 from dim_ℝ(Im ℍ) = 3 [L0]
- Pure anomalies (SU(3)³, SU(2)³) cancel automatically [L0]
- Witten anomaly cancels for N_gen = 3 [L0 + MC]

**Cannot claim without further work**:
- Chirality: SU(2)_L not SU(2)_R (Gap C1: motivated, not proved)
- Mixed anomalies AN-3 to AN-6: motivated (need fermion Y assignments)
- Fermion masses, mixing, CP violation (outside gauge scope)

**Strongest emerging result**: SU(3)_c derivation (Theorems G.A–G.D) and
N_gen = 3 derivation are the most complete and cleanest gauge-sector results.

---

## Cross-Track Connections Found This Week

1. **T1_GR ↔ T2_GAUGE**: The chirality gap C1 (ψ-parity theorem) is related to
   the complex-time structure that is central to the GR derivation. Proving C1
   from the complex-time axiom AXIOM-B would be a unified result spanning both tracks.

2. **T2_GAUGE ↔ T3_ALPHA**: The gauge paper's scope boundary (Higgs sector deferred)
   is exactly where T3_ALPHA begins. The critical dependency: sin²θ_W is the
   first Higgs-sector quantity needed for α derivation.

3. **T3_ALPHA new lead**: The A5 polyhedral result (5−√5)/10 could connect the
   icosahedral symmetry of the biquaternion algebra to the EW mixing sector. If
   this is valid, it would be a cross-track result (algebra structure → EW physics).

---

## Blockers

| Blocker | Affects | Severity | Resolution path |
|---------|---------|----------|-----------------|
| Gap C1: chirality | T2_GAUGE paper claim | HIGH | Formalise ψ-parity theorem (1–2 wk) |
| Gap EW-1: tan θ_W | T3_ALPHA derivation | CRITICAL | Investigate A5 ⊂ Aut(ℂ⊗ℍ) |
| GAP-Z: Zerilli equation | T1_GR completeness | LOW (stated) | Chandrasekhar transformation (2–4 wk) |
| arXiv submission | T1_GR reputation shift | MEDIUM | 1–2 days proofreading |

---

## Strongest Emerging Results

**#1 (T1_GR)**: The GR flagship paper is submission-ready. The five-step chain
Θ → g_μν → Γ → R → G_μν = 8πGT_μν is complete at [L1]. Schwarzschild metric
reproduced numerically to < 10⁻¹⁵. This is the first undeniable public result.

**#2 (T2_GAUGE)**: SU(3)_c derivation from ℤ₂×ℤ₂×ℤ₂ involutions of ℂ⊗ℍ (Theorems
G.A–G.D) is the cleanest gauge result. Three independent derivations (involution,
qubit, commutator table) give the same answer.

**#3 (T3_ALPHA, NEW)**: The icosahedral prediction sin²θ = (5−√5)/10 ≈ 0.276 from
A5 projection geometry is the most precise parameter-free expression for the Weinberg
angle found in UBT to date. Worth investigating further.

---

## Reallocation Recommendation

| Recommendation | Rationale |
|----------------|-----------|
| **Maintain T1_GR at 65%** | One proofreading pass + arXiv is days away. Do not fragment this. |
| **Raise T3_ALPHA slightly (20% → 25%)** | The A5 lead is new and time-sensitive; needs 1–2 week investigation. |
| **Lower T2_GAUGE slightly (15% → 10%)** | All T2_GAUGE deliverables are done for this sprint. |
| **Pause: do NOT start any new tracks** | Anti-entropy rule. No new tracks for 30 days. |

**If A5 lead breaks through** (A5 ⊂ Aut(ℂ⊗ℍ) confirmed):
Temporarily reallocate T3_ALPHA to 35% for 1 week; do not abandon T1_GR.

---

## Anti-Entropy Status

| Rule | Status |
|------|--------|
| No new tracks for 30 days | ✅ Compliant — polyhedral scan is within T3_ALPHA |
| No repo-wide reorganizations | ✅ Compliant — only new files created in designated directories |
| No duplicate status docs | ✅ Compliant — each deliverable serves a unique purpose |
| Every claim links to source proof file | ✅ All claims in new documents cite source files |

---

## 30-Day Remaining Plan

| Week | T1_GR focus | T3_ALPHA focus | T2_GAUGE focus |
|------|------------|---------------|---------------|
| Week 2 | Proofread + arXiv submission | A5 ⊂ Aut(ℂ⊗ℍ) investigation | Chirality gap C1 formalisation |
| Week 3 | Post-submission: respond to feedback | If A5 valid: anchor (5−√5)/10 | Mixed anomaly derivation (EW-2) |
| Week 4 | GAP-Z (Zerilli): start Chandrasekhar | Weinberg angle paper outline | Gauge paper outline |

---

## Success Metric Check (end of 30 days)

| Metric | Current forecast |
|--------|-----------------|
| T1_GR final public-quality draft | ✅ Achieved — submission pending |
| T3_ALPHA exact Weinberg-angle roadmap | ✅ Achieved — Gap EW-1 mapped; A5 lead identified |
| T2_GAUGE brutally honest status matrix | ✅ Achieved — proved/open/deferred clearly separated |
| Repo reputation: "shipping framework" | IN PROGRESS — arXiv submission will trigger this |
