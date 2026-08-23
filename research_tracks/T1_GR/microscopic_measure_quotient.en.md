<!-- BILINGUAL-UNIT: microscopic-measure.provenance -->
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

# Microscopic configuration space and measure: canonical GR sector

<!-- BILINGUAL-UNIT: microscopic-measure.configuration -->
## Regulated configuration space

For the GR calculation, interpret complex time without double counting:
$x^0=t$ belongs to $M^4$ and $psi$ is the periodic internal coordinate. Thus

\[
 \Theta:M^4\times S^1_\psi\longrightarrow
 \mathbb B\simeq\mathbb C^4\simeq\mathbb R^8,
 \qquad \Theta(x,\psi+2\pi R_\psi)=\Theta(x,\psi).
\]

On a finite regulator with $N$ sites the unconstrained field-value space is
$\mathcal C_N=(\mathbb R^8)^N$. Smooth nondegenerate Lorentz-real tetrad
backgrounds form the classical GR sector. The condition
$D_\mu\Theta\in W_L$ is not silently imposed on every quantum fluctuation;
doing so would require a declared constraint determinant.

<!-- BILINGUAL-UNIT: microscopic-measure.spin -->
## Spin-gauge Jacobian

The pure gravitational spin lift acts on the matrix realization by

\[
 \Theta\longmapsto S\Theta S^\dagger,
 \qquad S\in SL(2,\mathbb C).
\]

Vectorization gives the complex-linear matrix $\bar S\otimes S$. Its complex
determinant is
$\overline{\det S}^{,2}(\det S)^2=1$, and the determinant of its realification
is the squared modulus, also one. Therefore the regulated flat measure

\[
 d\mu_{0,N}=\prod_{p=1}^{N}\prod_{A=1}^{8}d\theta_A(p)
\]

is invariant under the pointwise spin lift. The exact checker
`tools/verify_gr_microscopic_measure.py` verifies nontrivial rational/complex
$SL(2,\mathbb C)$ representatives independently. A general Lean proof of the
realified Kronecker determinant is `LEAN-PENDING`; no formal-proof claim is
made for this determinant yet.

<!-- BILINGUAL-UNIT: microscopic-measure.nonuniqueness -->
## Why this is not yet the physical functional measure

Spin invariance does not select a unique continuum measure. If $d\mu$ is
invariant and $F[\Theta]$ is any invariant functional, then
$e^{-F[\Theta]}d\mu$ is invariant as well. Diffeomorphism covariance requires
a density or a field-space metric. The natural DeWitt candidate

\[
 \|\delta\Theta\|^2_\Theta=
 \int_{M^4\times S^1_\psi}\sqrt{|g[\Theta]|}\,
 \langle\delta\Theta,\delta\Theta\rangle_E
\]

already depends on the composite metric and produces a nontrivial determinant.
The current axioms neither select this field-space metric nor exclude other
local invariant weights. Consequently symmetry alone derives an invariant
bare regulator measure, but not the constrained physical measure needed to
predict the Einstein--Hilbert coefficient.

<!-- BILINGUAL-UNIT: microscopic-measure.quotient -->
## Gauge quotient boundary

For the GR sector, local Lorentz transformations account for the six kernel
directions of the tetrad-to-metric map, while diffeomorphisms account for four
metric gauge directions. A Faddeev--Popov operator requires gauge conditions
and the infinitesimal action on every independent integration variable.
Canonical UBT fixes the transformation of the tetrad and reconstructed spin
connection, but it does not yet finalize whether the path integral integrates
only over $\Theta$, over the algebraic split-jet variables as auxiliaries, or
over a constrained first-jet space. These formulations have different
Jacobians even though their on-shell classical metrics agree.

<!-- BILINGUAL-UNIT: microscopic-measure.verdict -->
## Step verdict

- Step 1, regulated field-value configuration: **CLOSED for the declared GR
  audit regulator**.
- Step 2, spin-invariant bare measure: **CLOSED at finite regulator**.
- Step 2, continuum constrained physical measure: **OPEN**.
- Step 3, full gauge/ghost quotient: **OPEN**, narrowed to selecting and
  deriving one off-shell integration-variable formulation.

No canonical GR status changes follow yet.
