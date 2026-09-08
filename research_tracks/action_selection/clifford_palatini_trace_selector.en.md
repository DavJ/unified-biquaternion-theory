<!-- BILINGUAL-UNIT: clifford-palatini.provenance -->
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

# Canonical Clifford trace selector for the Palatini curvature form

<!-- BILINGUAL-UNIT: clifford-palatini.setup -->
## Setup from the existing UBT Clifford lift

On the canonical Lorentz basis let

\[
\frac12\{\Gamma_a,\Gamma_b\}=\eta_{ab}I_4,
\qquad
\eta=\operatorname{diag}(-1,1,1,1),
\]

with the exact `4 x 4` block matrices already obtained from the
biquaternionic tetrad. The same construction supplies the grading

\[
\Gamma_*^2=I_4,
\qquad
\{\Gamma_*,\Gamma_a\}=0.
\]

Let the Clifford-valued coframe and physical spin curvature be

\[
\mathbb E:=\Gamma_aE^a,
\qquad
\mathbb R:=\frac14R^{cd}\Gamma_c\Gamma_d.
\]

No new tetrad is introduced here: `E^a` is the same canonical UBT tetrad,
possibly represented through the split-jet architecture.

<!-- BILINGUAL-UNIT: clifford-palatini.trace -->
## Exact graded trace identity [L0]

For the canonical block representation,

\[
\boxed{
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=-4i\,\epsilon_{abcd},
\qquad \epsilon_{0123}=+1.}
\]

Therefore

\[
\begin{aligned}
\operatorname{Tr}(\Gamma_*\mathbb E\wedge\mathbb E\wedge\mathbb R)
&=\frac14
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
E^a\wedge E^b\wedge R^{cd}\\
&=-i\,\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}.
\end{aligned}
\]

Equivalently,

\[
\boxed{
\frac1{4\kappa}\int
\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
=
\frac{i}{4\kappa}\int
\operatorname{Tr}(\Gamma_*\mathbb E\wedge\mathbb E\wedge\mathbb R).}
\]

Thus the Hilbert--Palatini curvature contraction is **exactly the graded
Clifford trace of objects already present in the canonical UBT lift**. Its
`epsilon` tensor need not be introduced as an unrelated extra algebraic
structure.

`tools/verify_clifford_palatini_trace_selector.py` checks the identity for all
`4^4` index choices in exact symbolic arithmetic.

<!-- BILINGUAL-UNIT: clifford-palatini.grading -->
## The grading is unique up to scale [L0]

Let `Z` be an arbitrary complex `4 x 4` matrix satisfying

\[
\{Z,\Gamma_a\}=0
\qquad(a=0,1,2,3).
\]

The exact linear system has a one-complex-dimensional solution space. After
normalizing `Z^2=I_4`,

\[
\boxed{Z=\pm\Gamma_*.}
\]

Hence once a microscopic rule requires a single normalized Clifford grading
insertion, there is no continuous matrix ambiguity in that insertion.

This is a statement about the canonical representation. It does not yet
establish that the locked UBT dynamics requires a grading insertion in the
action.

<!-- BILINGUAL-UNIT: clifford-palatini.holst -->
## Why Lorentz invariance alone is still insufficient

The ungraded four-gamma trace is also exact:

\[
\boxed{
\operatorname{Tr}(\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=4(\eta_{ab}\eta_{cd}-\eta_{ac}\eta_{bd}+\eta_{ad}\eta_{bc}).}
\]

Because `E^a wedge E^b` and `R^{cd}` are antisymmetric in their index pairs,
this gives

\[
\boxed{
\operatorname{Tr}(\mathbb E\wedge\mathbb E\wedge\mathbb R)
=-2E^a\wedge E^b\wedge R_{ab},}
\]

which is the metric/Holst-type curvature channel rather than the oriented
Palatini channel.

More generally, exact Lie-algebra reduction on the six-dimensional Lorentz
bivector representation gives

\[
\boxed{
\dim\left[\operatorname{Sym}^2(\Lambda^2\mathbb R^{1,3})^*
\right]^{SO^+(1,3)}=2.}
\]

A basis is the bivector metric contraction and the epsilon/Hodge contraction.
The verifier solves the complete invariant bilinear-form system exactly and
finds dimension two.

Therefore Lorentz covariance and locality by themselves allow a two-channel
curvature-linear family, conventionally written as Palatini plus Holst. The
canonical grading identifies the Palatini direction inside that family, but a
further UBT-native grading/parity/chirality selection principle is required to
exclude an independent ungraded coefficient.

This is a question of action uniqueness. The
[dynamical equivalence theorem](curvature_channel_dynamical_equivalence.en.md)
shows that a constant real Holst coefficient does not obstruct local vacuum
GR when the Palatini coefficient is nonzero, the coframe is nondegenerate,
and the spin current vanishes. Its absence is therefore not a necessary
condition for that restricted classical recovery target. Spin sources and
field-dependent coefficients require separate treatment.

<!-- BILINGUAL-UNIT: clifford-palatini.conditional-uniqueness -->
## Conditional uniqueness of the curvature form

Suppose a future microscopic UBT theorem establishes all of the following:

1. the leading local gravitational term is linear in the physical Lorentz
   curvature and quadratic in the canonical tetrad;
2. it is formed through the canonical Clifford trace;
3. exactly one normalized matrix anticommuting with every `Gamma_a` must be
   inserted (for example because the physical `psi`/grading sector supplies a
   derived chirality or orientation rule).

Then the preceding uniqueness theorem forces that matrix to `+/- Gamma_*`, and
the curvature term is consequently the Hilbert--Palatini form, **up to its
overall real coefficient and orientation sign**.

This would derive the tensorial form of the GR curvature action rather than
postulate `epsilon E E R` independently. The present repository has not yet
derived premise 3 from complex-time dynamics, so this implication remains
conditional.

<!-- BILINGUAL-UNIT: clifford-palatini.normalization -->
## What remains after the trace identity

The Clifford trace fixes the relative numerical normalization inside the
identity (`-4 i`) once the canonical gamma basis is fixed. It does **not** fix
the physical coefficient `1/kappa`. The current `N0` is a global unit-setting
constant, not an already derived Newton/Planck scale, and the action audit
contains no theorem relating it uniquely to `kappa`.

Accordingly the remaining curvature-origin problem has now separated into two
smaller tasks:

- **gravitational channel:** derive a nonzero Palatini coefficient; fixing
  the independent Holst coefficient remains an action-uniqueness and
  matter/quantum question, but is not required by the stated classical
  vacuum-equivalence theorem;
- **overall normalization:** derive `kappa` (and separately `Lambda`) from UBT
  microscopic data.

<!-- BILINGUAL-UNIT: clifford-palatini.status -->
## Status

**PALATINI EPSILON CONTRACTION AS THE CANONICAL GRADED CLIFFORD TRACE:
PROVED [L0].**

**UNIQUENESS OF THE NORMALIZED CLIFFORD GRADING UP TO SIGN:
PROVED [L0].**

**LORENTZ-INVARIANT CURVATURE-LINEAR BIVECTOR CHANNEL SPACE:
EXACTLY TWO-DIMENSIONAL [L1].**

**UBT DYNAMICAL SELECTION OF THE GRADED CHANNEL AND NEWTON NORMALIZATION:
OPEN.**
