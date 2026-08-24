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

# UBT gravity-sector dynamical postulate: one-constant Poincare branch

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.role -->
## Role

The locked UBT axioms determine the field, complex-time and covariant-tetrad
kinematics, but kinematics alone does not determine a nonzero gravitational
action. The action-selection audit established an explicit underdetermination:
the same kinematics is compatible with different curvature coefficients,
including zero.

A physical theory therefore needs one dynamical law in addition to its
kinematics. This document states the minimal UBT **gravity-sector dynamical
postulate**. It does not redefine the locked field or metric axioms and it does
not introduce a second fundamental physical field.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.field -->
## Composite tetrad and auxiliary geometry

On every regular non-null patch of the Lorentz-real projection `X` of `Theta`,
define

\[
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right),
\qquad X^2\ne0.
\]

Here:

- `Theta` remains the only fundamental physical field;
- `omega` is the variational Lorentz connection;
- `K_J` and `w` are algebraic split-jet variables with no derivative terms;
- there is no independently varied tetrad field;
- physical curvature is `R(omega)` and does not use `K_J`.

The split-jet variation map `(delta K_J, delta w) -> delta E` is pointwise
surjective onto all four tetrad directions on the stated patch.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.action -->
## Dynamical postulate

The canonical local classical gravity law is

\[
\boxed{
S_G[\Theta,\omega,K_J,w;\kappa]
=\frac1{4\kappa}\int_{M_4}
\epsilon_{abcd}\,E^a\wedge E^b\wedge R^{cd}(\omega),
\qquad \kappa>0.}
\]

This is the finite local Poincare-contracted limit of the merged canonical
fifth-channel graded curvature-square candidate after removal of the Euler
topological density. Equivalently it is the `ell -> infinity` branch for which

\[
\boxed{\Lambda_{\rm bare}=0.}
\]

The action has exactly one continuous gravitational constant, `kappa`. The
locked `N0` is a global unit-setting normalization and is not a second physical
coupling.

No independent bare cosmological constant is permitted in this branch. A
nonzero effective cosmological term must be derived from the `Theta`
vacuum/quantum state, boundary data, or another reduction of the same eventual
single UBT action; it is not an additional gravity parameter.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.equations -->
## Local Euler--Lagrange consequence [L1]

Let `E_a` denote the ordinary Palatini tetrad Euler three-form. Variation of
`K_J,w` gives

\[
0=\int E_a\wedge\delta E^a.
\]

Surjectivity of the split-jet variation implies

\[
\boxed{E_a=0.}
\]

Thus the complete tetrad Einstein equation is imposed, not an adjoint
projection.

The connection variation is the standard Palatini connection variation plus a
chain-rule term proportional to `E_a`. On the jet equation that term vanishes.
The remaining vacuum Cartan equation has the already verified invertible
24-component torsion map, hence

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

The `Theta` variation is a differential consequence of `E_a=0`. Conversely,
every local zero-bare-`Lambda` Palatini solution admits the explicit non-null
split-jet lift. Therefore, modulo the algebraic jet stabilizer and standard
boundary/topology data,

\[
\boxed{
\operatorname{Sol}_{\rm loc}(S_G)/\operatorname{Stab}_{\rm jet}
\longleftrightarrow
\operatorname{Sol}_{\rm loc}(\mathrm{GR},\Lambda_{\rm bare}=0).}
\]

Schwarzschild, Kerr and the linearized gravitational-wave sector are included
through the ordinary local GR solution set wherever the split-jet patch is
regular.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.source -->
## Sources and the meaning of the single constant

In pure vacuum the overall factor `1/kappa` cancels from the classical field
equations. `kappa` becomes the gravitational response constant only relative
to a source normalization.

UBT's single-action rule forbids adding a separately normalized fundamental
matter action merely to define that ratio. When the gauge/matter reduction of
the unique UBT action is finalized, its stress tensor must enter the same
variational system and `kappa` is the sole allowed gravitational response
constant. Deriving the microscopic Standard-Model/matter reduction is a
non-gravitational completion task and is not replaced by this postulate.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.scope -->
## Scope of `CLOSED`

Adoption of this postulate closes the **local classical gravity-sector GR
recovery problem**. It does not assert all of the following stronger statements:

- that the older kinetic/potential family forced this action without a
  dynamical postulate;
- that an observed effective dark-energy density has already been derived;
- that the full gauge/matter/quantum UBT action has been finalized;
- that null-patch and global topological continuation is complete;
- that UV `psi` stability has been proved.

Those are separate full-theory, cosmological or global-completion problems.
They must not be relabeled as failures of the local Einstein gravity theorem.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.status -->
## Canonical status after adoption

```yaml
gravity_dynamical_postulate: POINCARE_CONTRACTED_FIFTH_CHANNEL_SPLIT_JET_PALATINI
continuous_gravity_constants: 1
constant: kappa
bare_cosmological_constant: 0
fundamental_physical_field: Theta
independent_tetrad: false
local_gr_recovery: CLOSED
full_single_ubt_action: NOT_FINALIZED
```

Merge of this document and the paired Czech edition is the repository action
that adopts the postulate. Until merge, it is a working canonicalization
proposal and must not be described as already adopted on `master`.
