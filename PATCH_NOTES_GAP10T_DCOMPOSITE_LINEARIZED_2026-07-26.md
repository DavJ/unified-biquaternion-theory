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

# UBT differential patch — linearized self-consistent D-composite analysis

**Patch date:** 2026-07-26
**Base commit marker:** `940f7c3b49dcc54d97f92dc497c43c2eb205cf84`

Root-relative overlay; extract from the repository root.

## Results (frozen-coefficient linearization at the affine point)

1. **GAP-10T-DCOMP-SECTOR: CLOSED [L0].** Lorentz-real D-composite sector
   forces Theta into W_L identically (Hermitian part solved to zero).
2. **Symbol identity [L1, symbolic]:** A^3 = (lambda.s) A^2 in all eight
   variables; spectrum {0^10, q^6}, rank A = 9, rank A^2 = 6,
   det(I-A) = (1-q)^6; unique solvability iff q != 1.
3. **GAP-10T-DCOMP-LIN-OFFRES: CLOSED CONDITIONALLY [L1].** The linearized
   Levi-Civita connection annihilates exact gradients, so off resonance the
   unique delta-Theta-driven solution is the exact gradient: holonomic,
   pullback-flat at linear order.
4. **GAP-10T-DCOMP-RES: OPEN.** At q = 1 the resonant eigenspace is exactly
   six-dimensional (= dim so(1,3)); every mode is anholonomic with linearly
   independent curls. All linearized anholonomy (hence candidate curvature)
   is confined there, on the moving hyperplane (x0 + theta0).s = 1.

Answers to the six audit questions at this level are in the note
(canonical/gr_closure/gap_10t_dcomposite_linearized.tex, section 4):
Q1 solved (unique iff q != 1), Q2 solved (driven solutions holonomic;
anholonomy only resonant), Q3 narrowed to the resonant sector, Q4-Q5 not
yet computed, Q6 answered off-resonance (degenerates to flat, but not
identically - the resonant remainder is irreducible).

## Bug found and fixed during this work

An index transposition in the linearized Levi-Civita t3 term
(delta e_{sigma mu} vs delta e_{mu sigma}) leaked the symmetric tetrad
part into omega^1. It was caught by the structural test "A must annihilate
gradients" and is now a permanent regression check (D1). All results
computed with the faulty formula (an earlier {0^4, q^9, (q/2)^3} spectrum
and its resonances q in {1,2}) are void and superseded. The same formula
in tools/verify_canonical_spin_current.py (C7) was corrected; the C7
conclusion is unaffected because its exactness argument holds for any
delta-omega, and the C7 checks still pass after the fix.

## Files

- canonical/gr_closure/gap_10t_dcomposite_linearized.tex (new)
- docs/pdfs/gap_10t_dcomposite_linearized.pdf (new)
- tools/verify_dcomposite_linearized.py (new; 11 exact checks)
- tests/test_dcomposite_linearized.py (new; 6 tests, symbolic identity slow-marked)
- tools/verify_canonical_spin_current.py (C7 t3 formula corrected)
- CLAIMS.yaml, CLAIMS_MATRIX.md, STATUS.md, STATUS_OF_UBT.md, WHAT_IS_PROVED.md

## Validation

- python tools/verify_dcomposite_linearized.py - 11/11 exact checks PASS.
- pytest tests/test_dcomposite_linearized.py tests/test_claims_consistency.py - 8 passed.
- pytest tests/test_canonical_spin_current.py (incl. slow) - passes after C7 fix.
- pdflatex on the note - compiles cleanly.

## Still pending from earlier audits

layer2 shims and derive_fine_structure archive branch (three uploads and
counting); shim scan should grep the module string.
