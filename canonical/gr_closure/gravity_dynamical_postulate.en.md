<!-- BILINGUAL-UNIT: gr-dynamical-postulate.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT gravity-sector dynamical postulate: one-coupling Einstein-Lambda branch

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.role -->
## Role

The locked UBT axioms determine the field, complex-time and covariant-tetrad
kinematics, but kinematics alone does not determine a nonzero gravitational
action. A physical theory therefore needs one dynamical law in addition to its
kinematics.

The minimal gravity law adopted here has exactly one independent continuous
action coupling, `kappa`. The cosmological constant is not set to zero and is
not introduced as a second coupling: it arises on shell as an integration
constant by a diffeomorphism-invariant unimodular/Henneaux--Teitelboim
completion.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.field -->
## Composite tetrad and auxiliary geometry

On every regular non-null patch of the Lorentz-real projection `X` of `Theta`,
define

\[
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right),
\qquad X^2\ne0.
\]

`Theta` remains the only fundamental physical field. `omega` is the variational
Lorentz connection and `K_J,w` are algebraic split-jet variables. Introduce in
addition an auxiliary scalar `Lambda(x)` and an auxiliary three-form `C_3`.
Neither has local propagating degrees of freedom in the gravity sector. There
is no independently varied tetrad field and no fixed background volume form.

The split-jet variation map `(delta K_J,delta w) -> delta E` is pointwise
surjective onto all tetrad directions on the stated patch.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.action -->
## Dynamical postulate

Define

\[
\nu_E:=\frac1{24}\epsilon_{abcd}
E^a\wedge E^b\wedge E^c\wedge E^d.
\]

The canonical local classical gravity law is

\[
\boxed{
S_G[\Theta,\omega,K_J,w,\Lambda,C_3;\kappa]
=\frac1{4\kappa}\int_{M_4}
\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac1\kappa\int_{M_4}\Lambda(x)\left(\nu_E-dC_3\right),
\qquad \kappa>0.}
\]

The action contains exactly one independent continuous coupling, `kappa`.
`N0` is the locked global unit-setting normalization. `Lambda(x)` is a
Lagrange-multiplier field rather than a coupling constant.

The merged fifth-channel MacDowell--Mansouri construction remains the algebraic
motivation for why Palatini and cosmological structures belong to the same
extended Clifford curvature sector, but the earlier `ell -> infinity` choice
and `Lambda_bare=0` are not part of this postulate.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.selection -->
## Selection rationale: minimal low-energy principle

The postulate is not claimed to follow from kinematics alone. Its form is,
however, substantially narrower than an arbitrary choice of field equations.
Adopt the following gravity-sector low-energy requirements on the regular
Lorentz-real branch:

1. locality and diffeomorphism invariance;
2. local Lorentz invariance of the tetrad description;
3. metric equations of at most second differential order in the classical
   low-energy sector;
4. no additional light propagating geometric field beyond the composite metric
   degrees of freedom;
5. at most one independent continuous action coupling.

The existing four-dimensional Lovelock theorem recorded in
`canonical/gr_closure/gap_10d_low_energy_uniqueness.tex` then restricts every
natural symmetric divergence-free metric equation in this class to

\[
\boxed{\mathcal E_{\mu\nu}=aG_{\mu\nu}+bg_{\mu\nu}.}
\]

Thus the metric endpoint is Einstein--`Lambda` up to normalization; it is not
one arbitrary tensor equation among many. The Palatini term above is the
minimal first-order tetrad/connection representative of that endpoint, while
the HT sector realizes the cosmological term without a second action coupling.
Within the separately declared affine, background-free, first-order auxiliary
class, that HT completion is unique up to invertible linear auxiliary-field
redefinitions, sign/orientation and a boundary term.

This rationale does **not** prove that the deeper microscopic UBT uniquely
forces locality, second order or the no-extra-light-field hypothesis. Those are
part of the adopted classical dynamical principle. A future microscopic
derivation may explain them, but the current claim is deliberately the weaker
and defensible one: once these minimal low-energy principles are adopted, the
Einstein--`Lambda` endpoint and the one-coupling auxiliary realization are
strongly constrained.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.lambda -->
## Cosmological constant as integration data [STD]

Variation of `C_3` and `Lambda` gives

\[
\boxed{d\Lambda=0,}
\qquad
\boxed{\nu_E=dC_3.}
\]

Therefore on every connected local patch

\[
\boxed{\Lambda(x)=\Lambda_0=\mathrm{constant}.}
\]

`Lambda_0` is a solution/integration constant, not a second parameter of the
theory. Positive, zero and negative branches are all allowed.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.equations -->
## Local Euler--Lagrange consequence [L1]

The tetrad Euler equation is

\[
\boxed{
\epsilon_{abcd}E^b\wedge
\left(R^{cd}-\frac{\Lambda}{3}E^c\wedge E^d\right)=0.}
\]

Surjectivity of the split-jet variation implies that variation of `K_J,w`
imposes this complete tetrad equation, not an adjoint projection.

The connection variation is the ordinary Palatini connection variation plus a
chain-rule term through the composite tetrad. On the tetrad equation that term
vanishes. The remaining vacuum Cartan equation has the already verified
invertible 24-component torsion map, hence

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

The metric equation is therefore

\[
\boxed{G_{\mu\nu}+\Lambda_0g_{\mu\nu}=0.}
\]

The `Theta` variation is a differential consequence of the complete tetrad
equation. Conversely every regular local Einstein solution with any constant
`Lambda_0` has the existing non-null split-jet lift. On a contractible
four-dimensional patch `nu_E` is locally exact, so a `C_3` satisfying
`dC_3=nu_E` exists. Thus

\[
\boxed{
\operatorname{Sol}_{\rm loc}(S_G)/\operatorname{Stab}_{\rm jet}
\longleftrightarrow
\bigcup_{\Lambda_0\in\mathbb R}
\operatorname{Sol}_{\rm loc}(\mathrm{GR},\Lambda_0).}
\]

This includes the local Schwarzschild, Kerr, de Sitter, anti-de Sitter and
Schwarzschild--de Sitter/Kottler branches and their ordinary GR perturbations.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.source -->
## Meaning of the single constant

In pure vacuum the overall factor `1/kappa` cancels from the classical field
equations. `kappa` becomes the gravitational response constant relative to the
source normalization of the eventual unique UBT matter/gauge reduction.

`Lambda_0` is not counted as a fundamental constant of the theory, just as a
black-hole mass or angular momentum can label a solution without being a
Lagrangian coupling. A stronger future cosmological theory may select or
predict the observed value of `Lambda_0` from global, topological, vacuum or
quantum state data. That numerical selection is a cosmology problem, not a gap
in local Einstein-`Lambda` recovery.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.scope -->
## Scope of `CLOSED`

Adoption of this postulate closes the **local classical gravity-sector GR
recovery problem including arbitrary constant cosmological constant**. It does
not assert that the observed numerical value of dark energy has already been
predicted, that the full gauge/matter/quantum UBT action is finalized, that
global null-patch continuation is complete, or that UV `psi` stability is
proved.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.status -->
## Canonical status after adoption

```yaml
gravity_dynamical_postulate: ONE_COUPLING_UNIMODULAR_SPLIT_JET_PALATINI
independent_continuous_action_couplings: 1
constant: kappa
Lambda_role: INTEGRATION_CONSTANT
Lambda_allowed_signs: POSITIVE_ZERO_NEGATIVE
fundamental_physical_field: Theta
independent_tetrad: false
local_Einstein_Lambda_recovery: CLOSED
numerical_Lambda_prediction: OPEN_COSMOLOGY
full_single_ubt_action: NOT_FINALIZED
```

Merge of this document and the paired Czech edition is the repository action
that adopts the postulate. Until merge, it is a working canonicalization
proposal and must not be described as already adopted on `master`.
