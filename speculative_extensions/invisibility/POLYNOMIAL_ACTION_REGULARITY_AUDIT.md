# Polynomial-action regularity audit for the null-shell branch

**Status:** EXACT STRUCTURAL RESULT / NON-CANONICAL SPECULATIVE TRACK  
**Recorded:** 2026-08-01  
**Physical status:** a regular topological action exists, but no action is yet known that dynamically selects or stabilises the shell

## 1. Question

The Whitney shell has a degenerate central metric at the inner surface,

\[
\gamma_{AB}=0,\qquad A,B\in\{\theta,\phi\},
\]

so an action using `gamma^{-1}` or the ordinary Levi--Civita scalar is not
available there.  The first action-level question is therefore narrower than
full invisibility:

> Does a local polynomial four-form built from the original field remain
> well-defined when the central metric degenerates?

The answer is yes, but the simplest answer is topological and therefore does
not select the shell.

Throughout, `d_4` denotes the exterior derivative on ordinary spacetime.  The
compact `psi` profile is retained as an internal label and may be averaged only
after the four-form has been constructed.

## 2. Exact metric-free four-form

Define the ordered biquaternion-valued two-form

\[
\mathcal K_\Theta(\psi)
:=d_4\Theta^\sharp\wedge d_4\Theta.
\]

It contains no inverse metric, determinant, Hodge star, or Levi--Civita
connection.  It is therefore algebraically regular on the tangential-null
surface and even on a fully metric-degenerate configuration.

Let

\[
\alpha_\Theta:=\Theta^\sharp d_4\Theta.
\]

Because `d_4^2=0`, one has the exact identities

\[
\boxed{\mathcal K_\Theta=d_4\alpha_\Theta,\qquad
       d_4\mathcal K_\Theta=0.}
\]

Consequently,

\[
\boxed{
\mathcal K_\Theta\wedge\mathcal K_\Theta
=d_4\!\left(\alpha_\Theta\wedge\mathcal K_\Theta\right).
}
\]

The statement is algebra-valued and therefore remains true after applying any
fixed linear scalar/reality functional `ell` and after Haar averaging over
`psi`.

## 3. Regular but non-selective topological action

The quartic action

\[
\boxed{
S_{\rm top}[\Theta]
=\lambda\int_M
\left\langle
\ell\!\left(\mathcal K_\Theta\wedge\mathcal K_\Theta\right)
\right\rangle_\psi
}
\]

is:

- polynomial in first spacetime derivatives of the one field `Theta`;
- generally covariant as the integral of a four-form;
- independent of `gamma^{-1}`, `det(gamma)`, and a Hodge star;
- regular at `gamma_AB=0`;
- a pure boundary term.

For compactly supported variations its bulk Euler--Lagrange equation vanishes
identically.  The Whitney shell is therefore admitted by this action, but so
is every sufficiently smooth `Theta`.  It does not select the shell.  This is not a dynamical closure,
finite-energy theorem, or stability mechanism.

Thus the weak statement

\[
\text{``a polynomial action can remain defined at the null surface''}
\]

is closed, while the physically relevant statement

\[
\text{``the UBT action selects and stabilises the null shell''}
\]

remains open.

## 4. Constant-coefficient first-jet obstruction

More generally, a first-derivative four-form of the schematic form

\[
C_{ABCD}\,
 d_4\Theta^A\wedge d_4\Theta^B\wedge
 d_4\Theta^C\wedge d_4\Theta^D,
\]

with a field-independent internal tensor `C_ABCD`, is locally the pullback of
a constant target-space four-form and is exact.  It cannot supply local bulk
dynamics by itself.

Therefore merely writing a more complicated constant contraction of four
`dTheta` factors does not solve the action problem.  A nontrivial pure-Theta
action must introduce at least one of:

1. a field-dependent coefficient or target-space form;
2. an inequivalent `psi`-spectral/profile operator;
3. an auxiliary first-order connection or multiplier;
4. an independently justified background/constitutive structure.

The fourth option belongs to an analogue-material model rather than a
fundamental emergent-spacetime closure.

## 5. Minimal live pure-Theta deformation class

For a central zero-form `Xi` built covariantly from the original field and its
internal profile data, consider

\[
S_\Xi[\Theta]
=\lambda\int_M\left\langle
\ell\!\left(
\Xi(\Theta,D_\psi\Theta,\ldots)\,
\mathcal K_\Theta\wedge\mathcal K_\Theta
\right)\right\rangle_\psi.
\]

Now

\[
\Xi\,\mathcal K_\Theta\wedge\mathcal K_\Theta
=d_4\!\left(\Xi\alpha_\Theta\wedge\mathcal K_\Theta\right)
-d_4\Xi\wedge\alpha_\Theta\wedge\mathcal K_\Theta.
\]

The second term is a genuine bulk term whenever `d_4 Xi` is nonzero.  This is
the smallest metric-free way to evade the constant-coefficient topological
obstruction without adding a new propagating spacetime field.

No particular `Xi` is promoted here.  It must be derived from UBT involutions,
profile symmetry, reality, and the same action principle.  In particular it
must:

- be invariant under the allowed local frame/gauge action;
- avoid explicit dependence on coordinate origin or the affine representative
  of `Theta`;
- produce a real action on the physical branch;
- remain finite at the inner null surface;
- yield the Whitney radial/angular profiles as an actual solution rather than
  fitting them after the fact;
- have a bounded quadratic fluctuation operator in the physical sector.

A profile projector onto selected winding sectors followed by a Hermitian
central norm is one candidate source of `Xi`, but its canonical status and
translation properties are open.

## 6. Auxiliary first-order fallback

A BF/Plebanski-type action using the composite two-form
`mathcal K_Theta` and an auxiliary connection is also polynomial and regular at
metric degeneracy.  Pure BF theory, however, is topological and admits the
shell non-selectively.  Simplicity or potential terms would have to be derived,
and the auxiliary variables shown not to introduce unwanted propagating
modes.  This route is therefore a fallback, not a completed solution.

## 7. Updated action ledger

Closed exactly:

1. a pure-Theta metric-free polynomial four-form exists;
2. it is regular at the null surface;
3. the constant sharp-quartic action is a boundary term and cannot select the
   shell;
4. constant-coefficient first-jet four-forms are insufficient for local
   dynamics.

Still open:

1. select an admissible nonconstant profile scalar/operator `Xi` or another
   non-topological invariant;
2. derive the full Euler--Lagrange equations;
3. reduce them on the spherical ansatz to radial equations for `H`, `chi`, and
   the interior continuation;
4. prove a finite-action on-shell shell and analyse its perturbations;
5. derive visible-sector constitutive equations and exterior scattering.

The next calculational target is therefore not another kinematic ansatz.  It is
an action-classification and radial-reduction calculation.
