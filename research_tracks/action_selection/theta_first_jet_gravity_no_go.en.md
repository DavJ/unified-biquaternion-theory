<!-- BILINGUAL-UNIT: first-jet-gravity.provenance -->
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

# First-jet no-go for a pure-gravity UBT selector

<!-- BILINGUAL-UNIT: first-jet-gravity.scope -->
## Scope

Let the nondegenerate Lorentz-real first jet of the single field define the
physical tetrad and metric,

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,
\qquad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}.
\]

Consider a **pure-gravity** local action density which is constructed
algebraically from `E` (equivalently `g`) at one point, is invariant under
local Lorentz frame changes and spacetime coordinate changes, contains no
fixed background tensor, and contains no derivative of `E` or `g`. Explicit
`Theta`-value invariants such as the potential are excluded from this theorem;
they were classified separately and behave as matter/potential terms.

<!-- BILINGUAL-UNIT: first-jet-gravity.orbit -->
## Pointwise orbit theorem [L0]

All nondegenerate Lorentz metrics of a fixed signature at one point form one
`GL(4,R)` congruence orbit. If

\[
g_1=e_1\eta e_1^T,
\qquad
g_2=e_2\eta e_2^T,
\]

then with `A=e_2 e_1^{-1}`,

\[
\boxed{g_2=A g_1 A^T.}
\]

Therefore a scalar function of the metric alone which is natural under all
coordinate changes has the same value on every nondegenerate Lorentz metric:
it is a constant on that orbit. Local Lorentz invariance removes the choice of
tetrad representative inside each metric.

Consequently the most general value-independent pure-gravity density at
zeroth derivative order in `g` is

\[
\boxed{\mathcal L_{\rm grav}^{(0)}=c_0\sqrt{-g}.}
\]

It is only a cosmological-volume term. This generalizes the previously proved
collapse of the direct quadratic composite first-jet scalar to
`4 N0 sqrt(-g)`.

<!-- BILINGUAL-UNIT: first-jet-gravity.order -->
## Differential-order consequence [L0]

An algebraic metric density has no curvature and its independent metric
variation is algebraic in `g`. It therefore cannot produce the Einstein tensor

\[
G_{\mu\nu}=R_{\mu\nu}-\frac12Rg_{\mu\nu},
\]

which contains second derivatives of the metric before the usual boundary-term
cancellations. In the composite description `g=g(D Theta)`, a first-jet
functional can of course produce second-order Euler--Lagrange equations for
`Theta`; that fact does **not** turn its algebraic metric dependence into the
Einstein curvature operator. The already proved quadratic-action order result
is consistent with this distinction.

Hence an unconditional microscopic GR derivation cannot be obtained by
searching for another value-independent pure-gravity scalar made only from the
same first jet `D Theta`.

<!-- BILINGUAL-UNIT: first-jet-gravity.routes -->
## Surviving routes

At least one of the following must occur in the single UBT action programme:

1. a local higher-jet invariant whose reduction contains the curvature scalar
   (second derivatives of `Theta` are unavoidable in the direct composite
   description);
2. a first-order formulation with an independently varied but ultimately
   constrained/composite connection, together with a derivation proving that
   no new physical propagating field was introduced;
3. quantum/functional integration of the finalized `Theta` dynamics which
   induces the Einstein--Hilbert term and fixes the required Hessian, measure,
   and physical mode content.

The first and second routes are direct microscopic selector routes; the third
is an induced-gravity route. Merely changing the first-jet pairing or tuning
the derivative-free potential is no longer an admissible unresolved mechanism.

<!-- BILINGUAL-UNIT: first-jet-gravity.verification -->
## Verification

`tools/verify_first_jet_gravity_orbit.py` verifies the congruence identity over
exact rational nondegenerate tetrads and checks that determinant densities
transform with the expected squared Jacobian. The theorem itself is the
pointwise transitivity argument above; the script is an independent exact
regression check, not its proof.

A Lean formalization of the full `GL(4,R)` Lorentz-signature orbit statement is
`LEAN-PENDING`. No Lean completion is claimed here.

<!-- BILINGUAL-UNIT: first-jet-gravity.status -->
## Status impact

**FIRST-JET PURE-GRAVITY SELECTOR: CLOSED AS NO-GO [L0].**

This narrows `UBT-FUND-GR-ACTION`: the missing selector must now be sought in a
higher-jet/curvature, constrained first-order, or genuinely induced effective
mechanism. It does not by itself choose among those mechanisms and therefore
does not upgrade GR recovery from `CLOSED_CONDITIONALLY`.
