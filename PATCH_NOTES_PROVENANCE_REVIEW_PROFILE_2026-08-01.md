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

# Patch notes: orthogonal provenance review profiles

## Purpose

Preserve the existing A/B/C/D release tiers while representing the common UBT
case more accurately: strong machine verification of named claims, partial but
real human review, and conscious author approval.

## Changes

- adds `PROVENANCE_REVIEW.yaml` as the source of truth for independent review
  axes;
- adds a machine-verifiable source block for profiled Markdown/LaTeX files;
- adds `tools/verify_provenance_review.py` and regression tests;
- extends `tex/ubtprovenance.sty` with `\UBTReviewProfile{...}{...}{...}`;
- extends PDF provenance verification to require matching visible text and
  metadata for registered curated publications;
- records the first narrowly scoped profile for
  `gap_10d_theta_hessian_principal_symbol.tex`;
- keeps that document in Tier B: the whole paper is not represented as fully
  human-reviewed, while selected claims are explicitly human-reviewed and the
  document is author-approved;
- adds the review-profile verifier to the LaTeX publication gate.

## First recorded human-review scope

The author reviewed and approved the following selected claims:

1. `rank(I-A)=10` on a 16-dimensional frozen system implies
   `dim ker(I-A)=6`;
2. the exponent six in `det(I-A)=(1-q)^6` is an algebraic multiplicity and
   does not by itself establish kernel dimension;
3. `q=1` is a spectral resonance condition, and exponential modes correspond
   to complex frequency or wave number rather than being intrinsically
   unphysical.

The profile explicitly does not claim line-by-line manual recomputation, the
full composite gauge-fixed Hessian, or an inter-sector transition mechanism.

## Compatibility

No existing tier is renamed.  No Tier-A path, claim status, equation, action or
scientific conclusion is changed.  Files without a registered review profile
retain their previous source marker, PDF notice and metadata behaviour.
