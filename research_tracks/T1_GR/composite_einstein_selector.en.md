<!-- BILINGUAL-UNIT: composite-selector.provenance -->
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

# Composite Einstein selector: canonical-core decision candidate

<!-- BILINGUAL-UNIT: composite-selector.definition -->
## Candidate

Keep the frozen covariant tetrad and define, on every regular rank-ten patch,

\[
S_{\rm comp}[\Theta]
=c\int d^4x\,\sqrt{-g[\Theta]}\,(R[g[\Theta]]-2\Lambda),
\qquad c\ne0.
\]

The displayed equation is the exact definition of the candidate considered
here for the local pure-gravity GR sector: $S_{\rm comp}$ contains no further
terms. This is not, however, a proof that the complete microscopic UBT action
contains no higher-derivative, $\psi$-sector, or matter terms. An additional
term preserves the exact Einstein--$\Lambda$ equation only if its first
variation vanishes in this sector (for example, if it is a boundary or
topological term), or if one explicitly works only in an approximate infrared
limit in which that term is suppressed. Deriving precisely this selection
from the microscopic dynamics therefore remains a separate condition.

This contains no independent metric field after composition: $g[\Theta]$ is
the central Gram metric of the covariant tetrad. It is non-surjective as a
dynamical selector because its stationary configurations must satisfy a metric
Euler--Lagrange equation; it is not the already rejected surjective split-jet
constraint.

<!-- BILINGUAL-UNIT: composite-selector.variation -->
## Exact variational bridge

Let $J=d g_\Theta$ be the differential from admissible $\Theta$ variations to
symmetric metric variations and let $\mathcal E_g$ be the metric
Euler--Lagrange covector of the Einstein--Hilbert functional. The composite
first variation is

\[
\delta S_{\rm comp}[\Theta]=c\,\mathcal E_g(J\,\delta\Theta).
\]

The canonical tetrad-to-metric rank theorem supplies surjectivity onto the ten
metric directions at every nondegenerate tetrad. Hence stationarity for every
admissible $\delta\Theta$ implies $\mathcal E_g=0$. For $c\ne0$, this is the
Einstein--$\Lambda$ equation. Lean theorem
`metricEquationOfCompositeStationarity` kernel-checks the exact surjective
pullback implication, and `nonzeroCoefficientPreservesEquation` checks removal
of the nonzero overall coefficient.

This argument is local and assumes that the already proved algebraic rank-ten
map extends to the declared admissible variation space with the required
boundary conditions. It does not compute the nonlinear composite Hessian.

<!-- BILINGUAL-UNIT: composite-selector.decision -->
## Decision boundary

The candidate closes the **classical composite variation bridge** once adopted:
it does not derive its own adoption. Diffeomorphism covariance, local Lorentz
symmetry, two-derivative locality, and absence of additional light geometric
fields restrict the infrared metric functional to Einstein--$\Lambda$ up to
coefficients, but the current kinematic axioms allow both $c=0$ and $c\ne0$.

Therefore unconditional `CLOSED` requires one of two honest inputs:

1. promote the nonzero composite Einstein functional to a canonical dynamical
   axiom; or
2. derive it from a separately finalized microscopic measure/Hessian.

Without one of these, changing the status would be circular. Even after option
1, quantum prediction of $G$, the constrained Hessian/measure, and physical
$\psi$-sector stability remain separate UV-completion questions unless the
scope of `CLOSED` is explicitly limited to classical local GR recovery.
