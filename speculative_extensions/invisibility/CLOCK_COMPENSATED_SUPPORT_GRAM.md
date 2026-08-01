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

# Clock-compensated covariant support Gram

**Status:** EXACT CONDITIONAL KINEMATIC THEOREM / MODEL-SPECIFIC CLOCK MODE  
**Recorded:** 2026-08-01  
**Physical status:** the Whitney shell support norm can be made invariant under the standard local `SL(2,C)` paravector congruence without adding a new field; uniqueness of the clock-mode projector, dynamics, stability, and invisibility remain open

## 1. Problem addressed

The positive Hermitian support Gram

\[
\mathsf h_{\mu\nu}
=\left\langle\operatorname{ReSc}(E_\mu^\ddagger E_\nu)\right\rangle_\psi
\]

is regular on the central-metric-null Whitney sphere, but the unweighted
Hermitian product selects a preferred internal frame.  It is therefore not
invariant under a general local Lorentz congruence

\[
E_\mu\longmapsto S E_\mu S^\ddagger,
\qquad S(x)\in SL(2,\mathbb C).
\]

This note gives a `Theta`-only compensator for the explicit shell model.  It
uses the already present clock Fourier profile

\[
P_t(\psi)=\sqrt2\cos(3\psi),
\qquad \langle P_t^2\rangle_\psi=1,
\]

which is orthogonal to the radial, exterior-angular, and Whitney-null profile
sectors of the construction.

The result is conditional on retaining this distinguished clock-mode
projector.  The projector has not yet been derived uniquely from the UBT
master action, so the result is not a canonical promotion of the invisibility
track.

## 2. Composite clock matrix and compensator

Define the Hermitian clock coefficient

\[
\boxed{
\mathcal C_\Theta
:=-\frac{i}{2}\left\langle
P_t\left(\Theta-\Theta^\ddagger\right)
\right\rangle_\psi
}
\]

and its clock-jet derivative

\[
\boxed{
\mathcal N_\Theta
:=-\frac{i}{2}\left\langle
P_t\left(E_t-E_t^\ddagger\right)
\right\rangle_\psi,
\qquad E_t=\mathbb D_t\Theta.
}
\]

Both matrices are Hermitian.  On a branch where `mathcal N_Theta` is positive
definite, set

\[
\widehat{\mathcal N}_\Theta
:=\frac{\mathcal N_\Theta}
{\sqrt{\det\mathcal N_\Theta}},
\qquad
\det\widehat{\mathcal N}_\Theta=1.
\]

Under the standard paravector congruence

\[
\Theta\mapsto S\Theta S^\ddagger,
\qquad
E_\mu\mapsto S E_\mu S^\ddagger,
\]

with `S` independent of the internal coordinate `psi`, one has

\[
\mathcal C_\Theta\mapsto
S\mathcal C_\Theta S^\ddagger,
\qquad
\widehat{\mathcal N}_\Theta\mapsto
S\widehat{\mathcal N}_\Theta S^\ddagger.
\]

The determinant normalization is invariant because `det S=1`.

## 3. Covariant positive support Gram

Define

\[
\boxed{
\mathsf h^{\rm clk}_{\mu\nu}
:=\frac12\left\langle
\operatorname{ReTr}\!\left(
E_\mu^\ddagger
\widehat{\mathcal N}_\Theta^{-1}
E_\nu
\widehat{\mathcal N}_\Theta^{-1}
\right)
\right\rangle_\psi.
}
\]

This is real and symmetric.  For every real spacetime vector `v^mu`, writing
`X=v^mu E_mu`,

\[
v^\mu v^\nu\mathsf h^{\rm clk}_{\mu\nu}
=\frac12\left\langle
\operatorname{Tr}\!\left[
\left(\widehat{\mathcal N}_\Theta^{-1/2}
X\widehat{\mathcal N}_\Theta^{-1/2}\right)^\ddagger
\left(\widehat{\mathcal N}_\Theta^{-1/2}
X\widehat{\mathcal N}_\Theta^{-1/2}\right)
\right]
\right\rangle_\psi\ge0.
\]

It is positive definite whenever the four profile jets are independent in
this norm.

### Invariance theorem

The clock-compensated Gram is invariant under local `SL(2,C)` congruence.
Indeed,

\[
\widehat{\mathcal N}'^{-1}
=(S^\ddagger)^{-1}\widehat{\mathcal N}^{-1}S^{-1},
\]

so the matrix inside the trace transforms by similarity:

\[
E_\mu'^\ddagger\widehat{\mathcal N}'^{-1}
E_\nu'\widehat{\mathcal N}'^{-1}
=
S\left(
E_\mu^\ddagger\widehat{\mathcal N}^{-1}
E_\nu\widehat{\mathcal N}^{-1}
\right)S^{-1}.
\]

Cyclicity of the trace proves invariance.  Since `E_mu` is a spacetime
covector, `mathsf h_clk` is also a spacetime rank-two tensor.

## 4. Exact evaluation on the Whitney shell

For

\[
\Theta=itP_t+F(r)P_r+\rho(r)V
+\chi(r)\left[w_1e^{i\psi}q+w_2e^{-i\psi}p\right],
\]

profile orthogonality gives

\[
\boxed{
\mathcal C_\Theta=t\mathbf1,
\qquad
\mathcal N_\Theta=\mathbf1,
\qquad
\widehat{\mathcal N}_\Theta=\mathbf1.
}
\]

Therefore

\[
\boxed{
\mathsf h^{\rm clk}_{\mu\nu}
=\mathsf h_{\mu\nu}
}
\]

on the complete explicit shell ansatz.  All previously proved support results
are preserved exactly:

\[
dA_\gamma=0,
\qquad
dA_{\mathsf h^{\rm clk}}>0,
\qquad
\det\mathsf h^{\rm clk}>0
\]

on the inner sphere in every regular angular chart.

Thus the positive support area is not an artefact of one local Lorentz frame.
It has a `Theta`-only clock-compensated expression for the stated shell model.

## 5. Composite scalar clock and Lorentzian support tensor

A congruence-invariant scalar clock is

\[
\boxed{
T_\Theta
:=\frac12\operatorname{Tr}\!\left(
\widehat{\mathcal N}_\Theta^{-1}\mathcal C_\Theta
\right).
}
\]

The product transforms by similarity, so its trace is invariant.  On the
Whitney shell,

\[
\boxed{T_\Theta=t.}
\]

Where `mathsf h_clk` is nondegenerate and `dT_Theta` is nonzero, define

\[
u_\mu
:=\frac{\partial_\mu T_\Theta}
{\sqrt{(\mathsf h^{\rm clk})^{\alpha\beta}
\partial_\alpha T_\Theta\partial_\beta T_\Theta}}
\]

and

\[
\boxed{
\widehat h_{\mu\nu}
:=\mathsf h^{\rm clk}_{\mu\nu}-2u_\mu u_\nu.
}
\]

Then `u` has unit norm in the positive support Gram and `widehat h` has one
negative and three positive directions.  On the inner shell,

\[
\widehat h_{\mu\nu}
=\operatorname{diag}
\left(-1,1,\mathsf h_{\theta\theta},\mathsf h_{\phi\phi}\right)
\]

in the orthogonal spherical chart.  Hence the shell possesses a regular
Lorentzian internal support tensor even though the visible central metric has
zero angular area.

`widehat h` is an internal support geometry, not a replacement for the visible
metric `gamma`.

## 6. Action consequence

The previously proposed support-volume route can now be written in a locally
Lorentz-frame-invariant form,

\[
S_{\rm supp}^{\rm clk}
=T_{\rm supp}\int d^4x\,
\sqrt{\det\mathsf h^{\rm clk}},
\]

or, after selecting the composite clock foliation, as the static energy

\[
E_{\rm supp}^{\rm clk}
=T_{\rm supp}\int_{T_\Theta={\rm const}}d^3x\,
\sqrt{\det\mathsf h^{\rm clk}_{ij}}.
\]

These expressions remain regular at the visible-metric-null sphere.  A pure
positive volume/tension term favours contraction.  The smallest reduced
mechanism currently known to oppose it is the conserved relative phase charge
of the Whitney `psi=+/-1` block, derived in
`PHASE_CHARGE_FINITE_SCALE_STABILIZATION.md`.  That mechanism stabilises the
internal support scale exactly in the reduced model, but does not yet derive
the physical shell radius from the master action.

## 7. Exact closure and remaining limitations

Closed under the stated assumptions:

1. a composite Hermitian clock coefficient and positive compensator are built
   from the same `Theta`;
2. the compensated support Gram is positive and invariant under standard local
   `SL(2,C)` paravector congruence;
3. the explicit Whitney shell has `N_Theta=1`, so all previous support-area and
   support-volume calculations remain exact;
4. a congruence-invariant scalar clock satisfies `T_Theta=t` on the ansatz;
5. a regular Lorentzian internal support tensor can be formed without a new
   independent field.

Still open:

1. derivation and uniqueness of the distinguished clock Fourier projector from
   the UBT master action rather than from the shell ansatz;
2. covariance under more general `psi`-dependent ambient profile-frame changes;
3. compatibility with the full paired left/right UBT connection rather than
   only the standard paravector congruence sector;
4. a non-topological action whose Euler--Lagrange equations select the shell;
5. master-action derivation of the reduced conserved phase charge and a
   dynamical lock between the finite support scale and the exterior radius;
6. full perturbative stability, visible-sector decoupling, and zero exterior
   scattering.

The covariance obstruction of the raw Hermitian Gram is therefore narrowed to
clock-mode selection and full bimodule covariance.  It is not eliminated at the
canonical theory level, and zero exterior scattering remains unproved.
