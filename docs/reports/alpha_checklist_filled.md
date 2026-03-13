# Alpha Derivation Checklist

This checklist verifies the assumptions and derivations required for a rigorous, fit-free prediction of the fine-structure constant α within UBT.

## A1: Geometric Fixation of R_ψ and N_eff

### Question: Is R_ψ derived within UBT without external input?
**Answer:** YES (See: appendix_CT_two_loop_baseline.tex:112, test_scheme_independence.py:113, geometric_inputs_proof.tex:19)

**Evidence:**
<!-- Reference to relevant equations, theorems, or derivations -->

### Question: Is N_eff topologically determined (no adjustable parameters)?
**Answer:** <!-- TODO: Fill with yes/no + file:line reference -->

**Evidence:**
<!-- Reference to mode counting derivation -->

## A2: Ward-Takahashi Identity in CT Scheme

### Question: Is the Ward identity Z1 = Z2 proven in the CT scheme?
**Answer:** <!-- TODO: Fill with yes/no + file:line reference -->

**Evidence:**
<!-- Reference to theorem/proof -->

### Question: Is BRST invariance maintained under CT continuation?
**Answer:** <!-- TODO: Fill with yes/no + file:line reference -->

**Evidence:**
<!-- Reference to proof of BRST preservation -->

## A3: QED Limit and Thomson Normalization

### Question: Is the QED limit (ψ → 0) rigorously established?
**Answer:** <!-- TODO: Fill with yes/no + file:line reference -->

**Evidence:**
<!-- Reference to lemma/proof of continuity -->

### Question: Is the Thomson limit normalization explicitly defined?
**Answer:** <!-- TODO: Fill with yes/no + file:line reference -->

**Evidence:**
<!-- Reference to observable definition -->

## Closed Derivation Chain

### Question: Does a closed derivation chain exist: UBT axioms ⇒ α = numerical constant (no fit)?
**Answer:** <!-- TODO: Fill with yes/no + complete chain reference -->

**Evidence:**
<!-- Trace the full derivation path:
1. UBT field equations → ...
2. ... → B = (2π N_eff)/(3 R_ψ)
3. B → α via pipeline function F
4. No free parameters in any step
-->

## Two-Loop Baseline R_UBT

### Question: Is R_UBT = 1 proven at two-loop order under baseline assumptions?
**Answer:** <!-- TODO: Fill with yes/no + theorem reference -->

**Evidence:**
<!-- Reference to Theorem proving R_UBT = 1 -->

### Question: Are deviations from R_UBT = 1 explicitly calculated (not assumed)?
**Answer:** <!-- TODO: Fill with yes/no + calculation reference -->

**Evidence:**
<!-- Any CT-specific corrections beyond baseline -->

## Renormalization Group Consistency

### Question: Are Ward identities and gauge invariance respected?
**Answer:** <!-- TODO: Fill with yes/no + verification reference -->

**Evidence:**
<!-- Tests, checks, or proofs of Ward identity -->

### Question: Is the Thomson limit properly handled?
**Answer:** <!-- TODO: Fill with yes/no + reference -->

**Evidence:**
<!-- Treatment of q² → 0 limit -->

## Overall Assessment

### Summary: Is α rigorously and unambiguously derived without fitted parameters?
**Verdict:** <!-- TODO: Fill with YES / NO / UNCLEAR -->

**Justification:**
<!-- Brief summary (≤ 200 words) with specific file:line references -->

---

P25-11-09 01:10:57
**Source Data:** <!-- reports/alpha_hits.json, reports/alpha_equations.json -->


## Auto-Filled Evidence Summary


**A1 - Geometric Fixation:**
- appendix_CT_two_loop_baseline.tex:112
- test_scheme_independence.py:113
- geometric_inputs_proof.tex:19
- appendix_CT_two_loop_baseline.tex:110
- appendix_ALPHA_one_loop_biquat.tex:56

**A2 - Ward Identity:**
- Theorem at appendix_CT_two_loop_baseline.tex:217

**A3 - QED Limit:**
- Lemma at appendix_CT_two_loop_baseline.tex:284

**R_UBT Baseline:**
- Theorem at appendix_CT_two_loop_baseline.tex:179

**N_eff Mode Counting:**
- FIT_FREE_ALPHA_README.md:116
- ALPHA_SYMBOLIC_B_DERIVATION.md:839
- IMPLEMENTATION_SUMMARY.md:266
- UBT_HARDENING_COMPLETE_REPORT.md:213
- CHANGELOG.md:98

