<!-- BILINGUAL-UNIT: holomorphy-factor.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Holomorphy alone does not select one Dirac factor

<!-- BILINGUAL-UNIT: holomorphy-factor.scope -->
## Scope

The canonical generalized-Dirac programme leaves open a possible route in
which a second-order master operator factorizes and complex-time analyticity
selects one first-order factor. This note tests the selection power of
holomorphy itself, independently of any additional positivity, chirality,
boundary, or spectral condition.

Let

\[
\tau=t+i\psi
\]

be the canonical complex-time variable.

<!-- BILINGUAL-UNIT: holomorphy-factor.counterexample -->
## Exact counterexample [L0]

Consider the factorized scalar model

\[
(\partial_\tau-m)(\partial_\tau+m)f=0,
\qquad m\ne0.
\]

Both functions

\[
\boxed{f_+(\tau)=e^{m\tau},\qquad f_-(\tau)=e^{-m\tau}}
\]

are entire holomorphic functions of `tau`. They satisfy

\[
(\partial_\tau-m)f_+=0,
\qquad
(\partial_\tau+m)f_-=0,
\]

and hence both solve the same second-order equation. Therefore

\[
\boxed{\text{holomorphy alone does not distinguish the two factors}.}
\]

The statement is independent of the sign convention used to name the two
first-order factors.

<!-- BILINGUAL-UNIT: holomorphy-factor.periodic -->
## Compact `psi` does not remove the sign degeneracy by itself

Suppose the imaginary-time direction is compact with period `2 pi R_psi`.
Along fixed real `t`,

\[
f_\pm(t+i(\psi+2\pi R_\psi))
=f_\pm(t+i\psi)e^{\pm i2\pi mR_\psi}.
\]

Whenever periodicity is satisfied by the usual integer condition

\[
mR_\psi\in\mathbb Z,
\]

**both signs** obey it simultaneously because
`exp(+i 2 pi n)=exp(-i 2 pi n)=1`. Thus holomorphy plus ordinary compact
`psi` periodicity still does not select a unique first-order factor.

More general twisted boundary conditions can distinguish sectors only after
the twist itself is independently selected. Such a twist is additional
physical data, not a consequence of holomorphy alone.

<!-- BILINGUAL-UNIT: holomorphy-factor.consequence -->
## Consequence for the UBT action-origin programme

An exact factorization of a second-order UBT master equation would still need
an additional theorem to pick one generalized-Dirac branch. The canonical
holomorphy condition by itself cannot play that role.

A viable selector must contain information beyond analyticity, for example a
derived positivity/energy condition, chirality projection, oriented spectral
condition, nontrivial boundary/twist datum, or a genuinely degenerate
first-order variational principle. Each such proposal must be derived from the
same UBT structure rather than chosen after the desired factor is known.

<!-- BILINGUAL-UNIT: holomorphy-factor.verification -->
## Verification

`tools/verify_holomorphy_factor_no_go.py` checks the two factor equations and
the compact-`psi` periodicity identity symbolically with SymPy.
`tests/test_holomorphy_factor_no_go.py` keeps the counterexample in CI.

The counterexample is elementary and exact. A Lean formalization is
`LEAN-PENDING`.

<!-- BILINGUAL-UNIT: holomorphy-factor.status -->
## Status impact

**HOLOMORPHY-ONLY DIRAC FACTOR SELECTION: CLOSED AS NO-GO [L0].**

This closes one proposed subroute of the generalized-Dirac action-origin gap.
It does not rule out holomorphy as one ingredient of a stronger selector; it
rules out using analyticity alone as the missing branch-selection theorem.
