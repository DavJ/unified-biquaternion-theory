<!-- BILINGUAL-UNIT: gradient-null.provenance -->
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

# Pure-gradient metric-lock kinetic term is a null Lagrangian

<!-- BILINGUAL-UNIT: gradient-null.scope -->
## Scope

This note tests the simplest Lorentz-real branch of the currently declared
quadratic kinetic family. Let

\[
E_\mu{}^a=\mathcal N_0^{-1/2}\partial_\mu X^a,
\qquad
g_{\mu\nu}=E_\mu{}^aE_\nu{}^b\eta_{ab},
\]

on a nondegenerate patch with fixed orientation. No connection or torsion term
is included in this test. The result is therefore a branch-specific exact
obstruction, not a theorem about every possible covariant completion.

<!-- BILINGUAL-UNIT: gradient-null.collapse -->
## Metric-lock collapse

The canonical sharp/Minkowski contraction obeys the already proved identity

\[
g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=4\mathcal N_0.
\]

Hence the quadratic kinetic action on this branch is proportional to

\[
S_{\rm kin}=2\mathcal N_0\int d^4x\sqrt{-g}.
\]

Since `g=E eta E^T` and `det eta=-1`,

\[
\sqrt{-g}=|\det E|
=\mathcal N_0^{-2}|\det(\partial_\mu X^a)|.
\]

On a fixed-orientation patch the absolute-value sign is a fixed overall sign,
so the local variational problem is the Jacobian determinant.

<!-- BILINGUAL-UNIT: gradient-null.theorem -->
## Null-Lagrangian theorem [L0]

Write `J_mu^a=partial_mu X^a`. In four dimensions,

\[
\det J
=\frac1{4!}\epsilon^{\mu\nu\rho\sigma}\epsilon_{abcd}
 J_\mu{}^aJ_\nu{}^bJ_\rho{}^cJ_\sigma{}^d.
\]

Its derivative with respect to `J_mu^a` is the cofactor,

\[
\frac{\partial\det J}{\partial J_\mu{}^a}
=\frac1{3!}\epsilon^{\mu\nu\rho\sigma}\epsilon_{abcd}
 J_\nu{}^bJ_\rho{}^cJ_\sigma{}^d.
\]

The Euler--Lagrange equation is therefore

\[
\partial_\mu\left(\frac{\partial\det J}{\partial J_\mu{}^a}\right)=0.
\]

Each differentiated term contains a Hessian
`partial_mu partial_nu X^b`, symmetric in `mu,nu`, contracted with the
antisymmetric spacetime epsilon tensor. The terms vanish pairwise. Thus

\[
\boxed{\frac{\delta}{\delta X^a}\int d^4x\det(\partial X)=0}
\]

identically in the bulk. Equivalently, the cofactor of a gradient satisfies
the Piola identity

\[
\partial_\mu\operatorname{Cof}(\partial X)_\mu{}^a=0.
\]

Therefore the metric-locked quadratic kinetic term supplies no local bulk
field equation on this pure-gradient branch.

<!-- BILINGUAL-UNIT: gradient-null.hessian -->
## Hessian consequence

Because the first variation is a boundary term, the bulk quadratic fluctuation
operator of this branch is variationally degenerate. In particular it cannot
be identified, on this branch, with an assumed nondegenerate collection of
Laplace-type bosonic operators solely from the displayed quadratic canonical
kinetic term.

This does not disprove induced gravity from a **different finalized covariant
Theta action**. It does show that the Laplace-type Hessian used in the existing
conditional induced-gravity formula is not derived by simply taking the
metric-locked pure-gradient quadratic kinetic term at face value.

<!-- BILINGUAL-UNIT: gradient-null.verification -->
## Verification

`tools/verify_gradient_null_lagrangian.py` performs an exact symbolic
four-dimensional Piola-identity check by contracting a symmetric formal
Hessian with the antisymmetric Levi-Civita tensors. The corresponding pytest
keeps the cancellation in CI.

The epsilon-tensor proof above is exact. A Lean formalization of the Piola
identity in this UBT notation is `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: gradient-null.status -->
## Status impact

**PURE-GRADIENT QUADRATIC KINETIC SELECTOR: CLOSED AS NO-GO [L0].**

The current quadratic metric-lock term cannot be used as the missing
microscopic propagating Hessian on the pure-gradient branch. A successful
single-action completion must obtain its nondegenerate fluctuation operator
from additional covariant derivative/connection structure, a higher-jet term,
or another explicitly selected mechanism. GR recovery remains
`CLOSED_CONDITIONALLY` until that structure is derived.
