<!-- BILINGUAL-UNIT: multisymplectic-dirac.provenance -->
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

# Euler--Lagrange system and generalized-Dirac obstruction for the covariant multisymplectic family

<!-- BILINGUAL-UNIT: multisymplectic-dirac.setup -->
## Setup

Let `V` be the eight-dimensional real field space with constant symplectic
form `omega`, let `D` be a symplectic connection, and set

\[
 P:=D\Theta,\qquad Q:=\frac12\omega(P\wedge P),\qquad
 S_F^{\rm cov}=\frac12\int_{M_4}F(\Theta)Q\wedge Q.
\]

The connection is held fixed in the `Theta` variation. Write
`RTheta:=D^2 Theta` and use `omega_{AB}` for the matrix of `omega`.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.el -->
## Full Theta Euler--Lagrange system [L1]

The covariant variation gives the following eight four-form equations:

\[
\boxed{
 \begin{aligned}
 \mathcal E_A={}&\frac12F_{,A}Q\wedge Q
 -\omega_{AB}\,dF\wedge P^B\wedge Q\\
 &+F\omega_{AB}P^B\wedge dQ
 -F\omega_{AB}(\mathcal R\Theta)^B\wedge Q=0,
 \end{aligned}}
\]

where

\[
 dQ=\omega(\mathcal R\Theta,P).
\]

This is the complete bulk equation for a connection independent of `Theta`
and its jets during the variation. Boundary data must make
`F omega(delta Theta,P) wedge Q` vanish on the boundary.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.hessian -->
## Principal Hessian and second-jet cancellation [L0/L1]

In local coordinates the density is

\[
 L=F\,\operatorname{Pf}(Q_{\mu\nu}),\qquad
 Q_{\mu\nu}=\omega_{AB}P_\mu^AP_\nu^B.
\]

Its first-jet Hessian satisfies exactly

\[
 W^{\mu\nu}{}_{AB}
 =-W^{\nu\mu}{}_{AB}
 =-W^{\mu\nu}{}_{BA}.
\]

Therefore

\[
 W^{\mu\nu}{}_{AB}D_{(\mu}D_{\nu)}\Theta^B=0.
\]

All symmetric second jets cancel. The appearances of `D^2 Theta` in the full
equation above are only the antisymmetric commutator
`R Theta`; for a fixed connection they are zeroth order in `Theta`. Hence the
equation is first order in `Theta`. This conclusion does **not** survive an
unproved substitution `A=A[Theta,DTheta,...]`: the chain rule must then be
recomputed, and a Levi--Civita/composite connection normally introduces
higher jets.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.flat-identities -->
## Exact flat-branch differential identities [L0]

On a flat patch with `A=0`, the action is the pullback of the target-space
four-form `F omega^2/2`. Put `P_mu=partial_mu Theta`. Cartan's formula gives

\[
 \mathcal E_A\,\delta\Theta^A
 =\Theta^*\!\left(\iota_{\delta\Theta}
   (dF\wedge\omega^2/2)\right).
\]

Choosing a tangent variation `delta Theta=P_mu xi^mu` contracts a five-form
with five vectors lying in the four-dimensional image of `P`, and therefore
vanishes identically. Thus

\[
\boxed{P_\mu^A\mathcal E_A\equiv0\quad(\mu=0,1,2,3).}
\]

At every rank-four jet these are four independent Noether identities. The
eight displayed component equations have rank at most four. In particular,
their Jacobian with respect to the field value cannot be invertible on this
branch. For `F=H`, the exact rational witness used by the verifier reaches
rank exactly four, so the bound is sharp on a nonempty open set.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.dirac -->
## Obstruction to the canonical generalized-Dirac equation [L1]

The canonical generalized-Dirac candidate is an eight-real-component
first-order system with a nonzero linear principal symbol. Its established
sufficient rank-ten mechanism requires an invertible `8 x 8` original-field
block `F_Psi`, for example a nonzero scalar or scalar--pseudoscalar mass block.

The flat multisymplectic Euler--Lagrange system cannot be identical to that
system under an invertible recombination of equations:

1. it has the four identities `P_mu^A E_A=0` and hence at most four
   independent equations at a rank-four jet;
2. its first-derivative dependence is homogeneous of degree four, whereas a
   generalized-Dirac principal part is homogeneous of degree one;
3. its field-value Jacobian is singular and therefore does not realize the
   currently proved invertible-block sufficient condition for rank ten.

The third statement does not establish failure of the more general condition
`A+K=R^16`; it establishes only that the easy invertible-block route is unavailable.
Nor does pointwise rank alone establish local jet integrability. Curvature or
a composite connection may change the lower-order equations, but then the
fixed-connection/pullback proof no longer establishes equivalence and the
full composite variation is a separate higher-jet problem.

Together with the auxiliary-connection rank-collapse theorem, this leaves no
proved no-new-propagating-field completion of this family that is both a
nondegenerate UBT tetrad theory and the canonical generalized-Dirac equation.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.verification -->
## Verification

`tools/verify_multisymplectic_dirac_transversality.py` uses exact SymPy
arithmetic to:

- construct the eight Euler--Lagrange components as contractions of
  `dH wedge omega^2/2`;
- verify all four identities `P^T E=0` symbolically;
- verify a rank-four (and therefore singular) field-value Jacobian at an exact
  rank-four rational jet;
- differentiate the Pfaffian density and verify exact double antisymmetry of
  the full first-jet Hessian and zero contraction with arbitrary symmetric
  second jets at several exact witnesses.

The exterior-calculus proof is analytic. Lean status is `LEAN-PENDING`: the
repository has no compiled formalization of differential forms with the
required pullback/contraction identities for this theorem.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.status -->
## Status

**FIXED-CONNECTION COVARIANT THETA EQUATION AND SECOND-JET CANCELLATION:
PROVED [L1].**

**DIRECT EQUIVALENCE OF THE FLAT MULTISYMPLECTIC EQUATIONS TO THE CANONICAL
GENERALIZED-DIRAC SYSTEM: CLOSED AS NO-GO [L1].**

**GENERAL RANK-TEN TRANSVERSALITY FOR A COMPOSITE/HIGHER-JET COMPLETION:
OPEN.**
