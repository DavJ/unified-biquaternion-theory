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

# GR endgame audit — 26 July 2026

## Scope

This patch completes every GR statement that follows from the current UBT
architecture without silently importing a UV completion.  It separates three
logically different results:

1. local representation of arbitrary GR tetrads;
2. action-level nonpropagation of the split-jet auxiliaries;
3. origin and normalization of the Einstein curvature term.

## Exact closures

- `GAP-10T-JET-AUX: CLOSED [L1]`.
- `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`.
- `GAP-10D-UNDERDETERMINATION: CLOSED AS NO-GO [L1]`.
- `GAP-10D-A2-FORM: CLOSED CONDITIONALLY [L1]`.
- `GAP-10D-SPECTRAL-IR: CLOSED CONDITIONALLY [L1]`.

The combined action gives the full local torsion-free Einstein--Lambda
equations through two derivatives once a gauge-fixed Laplace-type Hessian and
renormalization prescription are specified.  The auxiliary jet sector carries
no propagator and vanishes from the physical equations on shell.

## Irreducible boundary

The present axioms do not determine a numerical Newton constant.  Adding
`c int sqrt(g) R` leaves every established kinematic theorem unchanged for any
real `c`.  Equivalently, the one-loop coefficient depends on the physical mode
count, curvature endomorphism/nonminimal coupling, compactification scale, and
UV subtraction prescription.  These data require a finalized constrained
path-integral measure or a separate UV principle.

This is not an unfinished heat-kernel calculation.  It is a proved
underdetermination of the current axioms.

## Publication wording

Allowed:

> UBT admits a complete conditional local GR effective branch, with generic
> Levi--Civita kinematics, nonpropagating split-jet auxiliaries, and an induced
> Einstein--Lambda action whose coefficient is explicit for a specified
> fluctuation operator and regulator.

Forbidden:

> UBT predicts Newton's constant from the current kinematic axioms.

> The single locked first-jet term classically derives the Einstein action.
