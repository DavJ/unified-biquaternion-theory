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

# UBT differential correction — D-composite linearized: audit corrections

**Patch date:** 2026-07-26
**Base:** overlay_gap10t_dcomposite_linearized_2026-07-26 applied to commit `940f7c3`

Implements both substantive corrections from the independent (26)-audit and
its strengthening suggestions. Both corrected errors were mine.

## Correction 1 — sector lemma weakened (quantifier error)

The previous `GAP-10T-DCOMP-SECTOR: CLOSED` claimed Theta in W_L is
*necessary*. The proof quantified over ALL independently chosen
connections; on-shell only Omega = Omega[E] occurs. The audit's
counterexample (constant Hermitian shift at a constant tetrad, Omega[E]=0)
is verified as check L0b. Relabelled:
`GAP-10T-DCOMP-WL-SECTOR: CLOSED CONDITIONALLY` — consistent subsector;
necessity disproved. All linearized results are statements about the W_L
subsector.

## Correction 2 — resonance terminology (exponential vs Fourier symbol)

The symbol used the real-exponential ansatz d -> s (real s). For real
Fourier modes d -> ik, q = i lambda.k is imaginary, so q = 1 has no
real-frequency solution. The six-dimensional sector is an
exponential/evanescent symbol sector; its relation to real-frequency
propagation is OPEN. "Local uniqueness iff q != 1" replaced by "modewise
invertibility of the frozen full symbol". All documents, claims, and
ledgers reworded accordingly.

## Strengthenings added (per audit suggestions + confirmation of its finding)

- D2b: trace theorem tr A^k = 6 q^k (k=1,2,3) proved symbolically; with
  A^3 = qA^2 this pins char poly t^10 (t-q)^6 and det(I-A) = (1-q)^6 as a
  theorem rather than a sampled fact.
- D5b: resonant sector dim 6 + curl rank 6 verified at three exact
  resonant points (previously one).
- D5c: every resonant mode has a nonzero linearized Riemann image —
  independently confirming the audit's positive finding that the sector is
  not obviously pure gauge.

## Hygiene

- .pytest_cache/, __pycache__/, *.pyc removed from the tree and excluded
  from this overlay; .gitignore already covers them.
- layer2 shims and derive_fine_structure remain pending (not in this
  overlay's scope; still awaiting their own commit).

## Validation

- tools/verify_dcomposite_linearized.py — 16/16 exact checks PASS.
- pytest tests/test_dcomposite_linearized.py tests/test_claims_consistency.py — 11 passed.
- pdflatex on the corrected note — clean.
