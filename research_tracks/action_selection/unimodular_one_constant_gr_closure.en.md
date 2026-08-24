<!-- BILINGUAL-UNIT: unimodular-one-constant.provenance -->
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

# One-coupling split-jet GR with the cosmological constant as an integration constant

<!-- BILINGUAL-UNIT: unimodular-one-constant.scope -->
## Scope

The zero-`Lambda` Poincare contraction is too narrow for a complete local GR
closure: ordinary Einstein gravity contains the Einstein-`Lambda` family, and
positive `Lambda` gives the de Sitter branch relevant to accelerated expansion.
The parameter-economy requirement is instead that `Lambda` must not be a second
independent coupling of the action.

This note gives a diffeomorphism-invariant Henneaux--Teitelboim/unimodular
completion of the split-jet Palatini branch. It contains exactly one continuous
action parameter, `kappa`, while a constant `Lambda_0` arises on shell as
integration data.

<!-- BILINGUAL-UNIT: unimodular-one-constant.action -->
## Action

Define the tetrad volume four-form

\[
\nu_E:=\frac1{24}\epsilon_{abcd}
E^a\wedge E^b\wedge E^c\wedge E^d.
\]

With the same split-jet composite tetrad `E[Theta,omega,K_J,w]`, introduce an
auxiliary scalar `Lambda(x)` and an auxiliary three-form `C_3`. The gravity law
is

\[
\boxed{
S_{\rm UGR}
=\frac1{4\kappa}\int\epsilon_{abcd}
E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac1\kappa\int \Lambda(x)\left(\nu_E-dC_3\right),
\qquad \kappa>0.}
\]

`Lambda(x)` and `C_3` are variational auxiliaries, not coupling constants. The
three-form has no local propagating degree of freedom in four dimensions.
There is no independent tetrad field and no fixed background volume form.

<!-- BILINGUAL-UNIT: unimodular-one-constant.lambda -->
## Exact cosmological-constant mechanism [STD + L1 composition]

Variation of `C_3` gives

\[
\boxed{d\Lambda=0,}
\]

hence on every connected local patch

\[
\boxed{\Lambda(x)=\Lambda_0=\mathrm{constant}.}
\]

Variation of `Lambda` gives

\[
\boxed{\nu_E=dC_3.}
\]

Thus `Lambda_0` labels solutions but is absent from the list of action
couplings. This is the standard unimodular/Henneaux--Teitelboim mechanism.

<!-- BILINGUAL-UNIT: unimodular-one-constant.einstein -->
## Complete Einstein equation from split-jet variation

The tetrad variation of the action is proportional to

\[
\boxed{
\epsilon_{abcd}E^b\wedge
\left(R^{cd}-\frac{\Lambda}{3}E^c\wedge E^d\right)=0.}
\]

On every regular non-null split-jet patch the already proved map
`(delta K_J,delta w) -> delta E` is surjective onto all tetrad directions.
Therefore variation of the algebraic jet variables imposes this entire tetrad
Einstein equation, not merely an adjoint projection.

The `omega` variation equals the ordinary Palatini connection variation plus a
chain-rule contribution through the composite tetrad. The latter is
proportional to the tetrad equation and vanishes on that equation. The remaining
Cartan equation has the already verified pointwise invertible torsion map, so in
spinless vacuum

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

Consequently the metric equation is

\[
\boxed{G_{\mu\nu}+\Lambda_0g_{\mu\nu}=0.}
\]

<!-- BILINGUAL-UNIT: unimodular-one-constant.equivalence -->
## Local solution-set equivalence

Conversely, every regular local vacuum Einstein solution with any constant
`Lambda_0` has a split-jet lift by the existing right-inverse theorem. On a
contractible four-dimensional patch its volume four-form is locally exact, so a
three-form `C_3` satisfying `dC_3=nu_E` exists. Therefore

\[
\boxed{
\operatorname{Sol}_{\rm loc}(S_{\rm UGR})/\operatorname{Stab}_{\rm jet}
\longleftrightarrow
\bigcup_{\Lambda_0\in\mathbb R}
\operatorname{Sol}_{\rm loc}(\mathrm{GR},\Lambda_0).}
\]

The local branch therefore contains Schwarzschild, Kerr, de Sitter,
anti-de Sitter, Schwarzschild--de Sitter/Kottler and their ordinary classical
perturbation sectors wherever the split-jet patch is regular.

<!-- BILINGUAL-UNIT: unimodular-one-constant.parameters -->
## Constant budget

The action contains exactly one independent continuous physical coupling:

\[
\boxed{\{\text{action couplings}\}=\{\kappa\}.}
\]

`Lambda_0` is an integration constant/state datum, not a Lagrangian coupling,
just as mass or angular momentum can label a classical solution without being a
fundamental constant of the theory. A later UBT cosmology may attempt to select
or predict the observed value of `Lambda_0` from global, topological or quantum
state data; that stronger prediction is not required for local GR equivalence.

<!-- BILINGUAL-UNIT: unimodular-one-constant.limit -->
## What this does and does not solve

This mechanism solves the **one-coupling GR recovery problem** and removes the
incorrect need to set the cosmological constant to zero. It does not by itself
solve the cosmological-constant hierarchy or predict the observed tiny positive
value. The existing UBT vacuum-energy note explicitly finds no automatic
120-order suppression in its first-pass zeta estimate, so no such prediction is
claimed here.

<!-- BILINGUAL-UNIT: unimodular-one-constant.status -->
## Status

**ONE-COUPLING LOCAL EINSTEIN-`Lambda` SOLUTION-SET RECOVERY: DERIVED FROM THE
ADOPTED SPLIT-JET PALATINI POSTULATE PLUS THE STANDARD DIFFEOMORPHISM-INVARIANT
UNIMODULAR COMPLETION.**

**`Lambda_0` AS AN INTEGRATION CONSTANT RATHER THAN A SECOND ACTION COUPLING:
PROVED WITHIN THIS VARIATIONAL SYSTEM.**

**MICROSCOPIC PREDICTION OF THE NUMERICAL COSMOLOGICAL CONSTANT: OPEN.**
