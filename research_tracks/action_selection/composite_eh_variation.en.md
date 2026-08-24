<!-- BILINGUAL-UNIT: composite-eh.provenance -->
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

# Chain-rule criterion for a composite Einstein--Hilbert Theta action

<!-- BILINGUAL-UNIT: composite-eh.question -->
## Question

A direct higher-jet candidate for the single-field programme is

\[
S_{\rm cEH}[\Theta]
 =c\int d^4x\sqrt{-g[\Theta]}\,(R[g[\Theta]]-2\Lambda).
\]

It is formally a `Theta`-only functional once the complete covariant map
`Theta -> g[Theta]` has been defined. This note records the exact condition
under which varying this composed functional is equivalent to the Einstein
equation. Merely writing the composition is not yet that proof.

<!-- BILINGUAL-UNIT: composite-eh.chain -->
## Exact chain-rule theorem [L0]

Let `Phi` denote the field-to-metric map and let `L_Theta=D Phi_Theta` be its
linearization,

\[
\delta g=L_\Theta\,\delta\Theta.
\]

After the standard Einstein--Hilbert boundary term is removed or fixed, write

\[
\delta S_{\rm EH}
 =c\int d^4x\sqrt{-g}\,\mathcal E^{\mu\nu}\delta g_{\mu\nu},
\qquad
\mathcal E^{\mu\nu}=G^{\mu\nu}+\Lambda g^{\mu\nu}
\]

in vacuum. Substitution of the composite variation and integration by parts
give

\[
\boxed{\frac{\delta S_{\rm cEH}}{\delta\Theta}
       =c\,L_\Theta^*\mathcal E.}
\]

Therefore

\[
\mathcal E=0\Longrightarrow \frac{\delta S_{\rm cEH}}{\delta\Theta}=0,
\]

but the converse holds only if the formal adjoint `L_Theta^*` has trivial
kernel on the physical symmetric-tensor sector under consideration:

\[
\boxed{\ker L_\Theta^*\big|_{\rm phys}=\{0\}.}
\]

Pointwise rank ten of the tetrad-to-metric algebraic map does not prove this
differential-operator injectivity. The latter includes integrability,
boundary, connection, gauge, and differential-symbol information.

<!-- BILINGUAL-UNIT: composite-eh.gradient -->
## Exact pure-gradient obstruction [L0]

The distinction is visible already in the simplest four-real-component branch
with a pure derivative tetrad,

\[
e_\mu{}^a=\partial_\mu X^a.
\]

On a nondegenerate patch `X` is a local coordinate map and

\[
g_{\mu\nu}=\eta_{ab}\partial_\mu X^a\partial_\nu X^b=X^*\eta.
\]

Thus the metric is locally flat. Around an affine background
`X^a=E_\mu{}^a x^\mu`, define

\[
\xi_\nu:=\eta_{ab}E_\nu{}^a\delta X^b.
\]

Then exactly

\[
\boxed{\delta g_{\mu\nu}
 =\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,}
\]

a pure infinitesimal diffeomorphism. Consequently

\[
\int \mathcal E^{\mu\nu}\delta g_{\mu\nu}
 =-2\int (\partial_\mu\mathcal E^{\mu\nu})\xi_\nu
 +\text{boundary},
\]

which vanishes identically for the Einstein tensor by the Bianchi identity.
The composed EH action therefore supplies no independent `X` equation on this
pure-gradient branch. This is the variational counterpart of the known flat
integrability obstruction.

<!-- BILINGUAL-UNIT: composite-eh.split -->
## Consequence for the split-jet branch

The split-jet right inverse avoids the pure-gradient obstruction by allowing an
arbitrary tetrad while reconstructing a composite jet connection. However,
the existing right inverse uses the tetrad as input. If `e` is then varied as
an independent field in an Einstein--Hilbert or Palatini action, GR follows,
but the microscopic theory contains an independently varied geometric
variable unless an additional theorem eliminates it as a functional of the
single fundamental `Theta`.

The auxiliary split-jet multiplier proves nonpropagation of the jet variables;
it does not make the Einstein tetrad a unique local functional of `Theta`.
Its surjectivity is precisely why the pure constraint cannot select the metric.

<!-- BILINGUAL-UNIT: composite-eh.target -->
## New minimal closure target

A direct microscopic higher-jet closure must provide **both**:

1. a local covariant `Theta -> g[Theta]` map capable of nonzero generic
   curvature without an independently propagating tetrad/connection; and
2. a proof that `L_Theta^*` is injective on the physical Einstein-equation
   sector (or an equivalent theorem showing that the `Theta` Euler--Lagrange
   equation is exactly Einstein's equation modulo gauge identities).

Only after that theorem is proved does a composed Einstein--Hilbert functional
close the dynamical implication. Its overall coefficient `c` remains a
separate selection/normalization problem unless fixed by the same microscopic
principle.

<!-- BILINGUAL-UNIT: composite-eh.status -->
## Status

**COMPOSITE EH FORM: ADMISSIBLE CANDIDATE; DYNAMICAL EQUIVALENCE OPEN.**

The exact chain-rule criterion closes a logical ambiguity but does not upgrade
`UBT-FUND-GR-ACTION`. It rules out the inference
“`S_EH[g(Theta)]` is Theta-only, therefore varying Theta gives all Einstein
equations” unless the adjoint-injectivity theorem is supplied.
