<!-- BILINGUAL-UNIT: first-order-hessian.provenance -->
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

# Exact first-jet Hessian criterion for first-order Euler--Lagrange dynamics

<!-- BILINGUAL-UNIT: first-order-hessian.setup -->
## Setup

Let `Phi^A` be real field components and let a local Lagrangian depend on the
first jet only,

\[
L=L(\Phi,\partial_\mu\Phi).
\]

Define its velocity/first-jet Hessian

\[
W^{\mu\nu}{}_{AB}
:=\frac{\partial^2L}
{\partial(\partial_\mu\Phi^A)\,\partial(\partial_\nu\Phi^B)}.
\]

For a smooth scalar Lagrangian, equality of mixed partial derivatives gives

\[
\boxed{W^{\mu\nu}{}_{AB}=W^{\nu\mu}{}_{BA}.}
\]

<!-- BILINGUAL-UNIT: first-order-hessian.theorem -->
## Principal-order theorem [L0]

The principal second-jet part of the Euler--Lagrange equation is

\[
- W^{\mu\nu}{}_{AB}\,\partial_\mu\partial_\nu\Phi^B.
\]

Because the second jet is symmetric in `mu,nu`, this term vanishes identically
for arbitrary second jets if and only if

\[
\boxed{W^{(\mu\nu)}{}_{AB}=0.}
\]

Combining this condition with Hessian exchange symmetry yields

\[
\boxed{
W^{\mu\nu}{}_{AB}
=-W^{\nu\mu}{}_{AB}
=-W^{\mu\nu}{}_{BA}.}
\]

Therefore a nonzero first-jet Hessian can avoid a second-order
Euler--Lagrange principal part only in the doubly antisymmetric sector

\[
\boxed{W\in\Lambda^2T\otimes\Lambda^2F.}
\]

Conversely every Hessian with these algebraic symmetries annihilates the
symmetric second jet at principal order.

<!-- BILINGUAL-UNIT: first-order-hessian.standard -->
## Standard quadratic kinetic term is excluded

For the ordinary nondegenerate quadratic kinetic form

\[
L_{\rm kin}=\frac12g^{\mu\nu}H_{AB}
\partial_\mu\Phi^A\partial_\nu\Phi^B,
\]

with symmetric `g^{mu nu}` and symmetric field pairing `H_AB`,

\[
W^{\mu\nu}{}_{AB}=g^{\mu\nu}H_{AB}
\]

lies in the doubly symmetric sector, not in
`Lambda^2 T tensor Lambda^2 F`. It therefore gives a genuinely second-order
principal equation whenever the pairing is nonzero/nondegenerate, reproducing
and sharpening the existing action-order obstruction.

<!-- BILINGUAL-UNIT: first-order-hessian.ubt -->
## Consequence for a UBT-native first-order action

A no-extra-field degenerate UBT action capable of yielding genuinely
first-order equations must arrange the **total** first-jet Hessian so that its
symmetric spacetime-index part cancels exactly. Algebraically, any residual
nonzero Hessian must be doubly antisymmetric as above.

This sharply restricts the search. A successful action cannot be obtained by
merely changing the coefficient of the canonical symmetric quadratic pairing.
It must use a multisymplectic/Wess--Zumino-like antisymmetric structure, a null
Lagrangian plus nontrivial lower-order terms, or another mechanism whose full
Hessian satisfies the same cancellation criterion.

For the composite generalized-Dirac trial density, the fact that
`Gamma=Gamma(DTheta)` means its chain-rule Hessian must be computed in full.
Calling the displayed expression “Dirac-like” does not establish the required
double antisymmetry.

<!-- BILINGUAL-UNIT: first-order-hessian.verification -->
## Verification

`tools/verify_first_order_hessian_criterion.py` constructs exact symbolic
Hessians with the exchange symmetry, checks that only the `mu,nu` symmetric
part couples to a formal symmetric second jet, and verifies the induced field
antisymmetry when that part vanishes. The paired pytest keeps the finite-index
identity in CI.

The theorem is finite algebra. A Lean formalization is a high-priority
`LEAN-PENDING` target because it does not depend on unresolved physical
premises.

<!-- BILINGUAL-UNIT: first-order-hessian.status -->
## Status impact

**FIRST-ORDER VARIATIONAL CANCELLATION CRITERION: CLOSED [L0].**

**UBT DEGENERATE FIRST-ORDER ACTION: STILL OPEN, NOW RESTRICTED TO THE
DOUBLE-ANTISYMMETRIC/MULTISYMPLECTIC PRINCIPAL SECTOR.**
