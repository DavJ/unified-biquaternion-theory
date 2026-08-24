<!-- BILINGUAL-UNIT: theta-multisymplectic.provenance -->
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

# Canonical invariant multisymplectic action family from the Theta quadratic form

<!-- BILINGUAL-UNIT: theta-multisymplectic.hermitian -->
## Invariant Hermitian form from the proved quadratic invariant

Write the generic field value as

\[
z=(a,b,c,d)^T\in\mathbb C^4,
\]

so that the already classified quadratic invariant is

\[
H(z)=z^\dagger Gz,
\qquad
G=\begin{pmatrix}
0&0&0&1\\
0&-1&0&0\\
0&0&-1&0\\
1&0&0&0
\end{pmatrix}.
\]

The connected constant field representation used in the invariant
classification is complex linear and preserves `H`. By complex polarization,
it therefore preserves the full Hermitian form

\[
\boxed{h(u,v)=u^\dagger Gv.}
\]

The matrix `G` is real, Hermitian and invertible (`det G=-1`). Thus `h` is
nondegenerate.

<!-- BILINGUAL-UNIT: theta-multisymplectic.symplectic -->
## Canonical invariant real symplectic form [L0]

On the underlying eight-dimensional real field space define

\[
\boxed{\omega(u,v):=\operatorname{Im}h(u,v).}
\]

With `z=x+iy`, its real matrix is

\[
\Omega=\begin{pmatrix}0&G\\-G&0\end{pmatrix}.
\]

Hence

\[
\det\Omega=(\det G)^2=1,
\]

so `omega` is nondegenerate. It is antisymmetric because `h` is Hermitian, and
it is invariant under the same constant connected field representation because
`h` is invariant. Its coefficients are constant in the linear field
coordinates, hence

\[
\boxed{d\omega=0.}
\]

The current UBT field representation therefore carries a canonical invariant
pseudo-Kaehler/symplectic structure without introducing a second physical
field. This is a field-space statement; local gauge covariance of a spacetime
action requires a separate covariantization theorem.

<!-- BILINGUAL-UNIT: theta-multisymplectic.action -->
## A no-extra-field first-order variational family [L1]

Let

\[
\Omega_4:=\frac12\omega\wedge\omega
\]

and let `F` be any real scalar invariant of the field value, for example a
function of the already classified invariants `H` and `D=|det X|^2`. For a
four-dimensional spacetime map `Theta:M_4 -> R^8`, define the ordinary-pullback
functional

\[
\boxed{S_F[\Theta]=\int_{M_4}\Theta^*(F\,\Omega_4).}
\]

This functional:

- uses only `Theta` and its ordinary first derivatives;
- is invariant under spacetime coordinate changes because it integrates a
  pulled-back four-form;
- is invariant under the constant/global connected field action when `F` is
  invariant;
- contains no independent tetrad, metric or connection;
- has a first-jet Hessian in the double-antisymmetric sector required by the
  exact first-order Hessian criterion.

Using Cartan's variation formula and `d Omega_4=0`, its bulk variation is

\[
\boxed{
\delta S_F
=\int_{M_4}\Theta^*\!\left(
\iota_{\delta\Theta}(dF\wedge\Omega_4)
\right)
+\text{boundary}.}
\]

The Euler--Lagrange equation therefore contains only first derivatives of
`Theta`. For constant `F`, `dF=0` and the action is a null/topological
Lagrangian. For nonconstant invariant `F`, the five-form
`dF wedge Omega_4` is generically nonzero and the variational principle is not
identically a boundary term.

This ordinary-pullback construction is **not yet a locally gauge-covariant UBT
action**. Under an `x`-dependent spin/gauge transformation, `dTheta` acquires a
derivative of the transformation. Replacing it by `DTheta` is not a literal
pullback of the target-space form, so the Cartan argument and first-order
cancellation must be rederived for the covariantized functional. That is a
separate open theorem.

<!-- BILINGUAL-UNIT: theta-multisymplectic.witness -->
## Nontriviality witness

Take `F=H`. At a point with `x_a=1` and all other real components zero,
`dH=2 dx_d` is nonzero. Because `omega` is symplectic on an eight-dimensional
space, the Lefschetz map

\[
\alpha\longmapsto\alpha\wedge\omega^2
\]

is injective on one-forms. Therefore

\[
\boxed{dH\wedge\omega^2\ne0}
\]

at that point. Thus `S_H` is an explicit globally field-symmetry-invariant
member of the ordinary-pullback family whose bulk first-order
Euler--Lagrange form is not identically zero.

<!-- BILINGUAL-UNIT: theta-multisymplectic.limit -->
## What this does and does not solve

This closes a restricted but important existence question left by the
generalized-Dirac action-order obstruction: **the canonical UBT field
representation admits nontrivial, no-extra-field, globally symmetry-invariant
first-jet functionals whose Euler--Lagrange equations are genuinely first
order.** The obstruction from the ordinary symmetric quadratic kinetic term is
therefore not a universal algebraic no-go against first-order field dynamics.

However, a locally gauge-covariant completion has not been proved. The family
`S_F` is not yet the desired unique fundamental action: `F` is not selected;
local spin/gauge covariance after replacing ordinary derivatives by covariant
ones is open; equivalence to the canonical generalized-Dirac equation is open;
and rank-ten transversality, curved GR recovery, the physical `psi` sector and
the quantum Hessian remain to be tested. Existence of this family must not be
reported as closure of `UBT-FUND-GR-ACTION`.

<!-- BILINGUAL-UNIT: theta-multisymplectic.verification -->
## Verification

`tools/verify_theta_multisymplectic_action.py` checks exactly that the real
symplectic matrix is antisymmetric and nondegenerate and constructs a nonzero
component of `dH wedge omega wedge omega`. The paired pytest keeps these finite
algebraic claims in CI.

The polarization and ordinary-pullback Cartan-variation arguments are
analytic. Lean formalization of the finite matrix/symplectic claims is
`LEAN-PENDING`. Local gauge covariantization is explicitly not included in the
proved claim.

<!-- BILINGUAL-UNIT: theta-multisymplectic.status -->
## Status impact

**EXISTENCE OF AN INVARIANT FIELD-SPACE SYMPLECTIC FORM AND A NONTRIVIAL
GLOBAL-SYMMETRY FIRST-ORDER PULLBACK FAMILY: PROVED [L1].**

**LOCAL GAUGE-COVARIANT COMPLETION, UNIQUE SELECTION AND EQUIVALENCE TO
GENERALIZED-DIRAC/GR DYNAMICS: OPEN.**
