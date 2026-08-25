<!-- BILINGUAL-UNIT: rpsi-scale-audit.provenance -->
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

# Audit of the absolute `R_psi` scale claim

<!-- BILINGUAL-UNIT: rpsi-scale-audit.scope -->
## Scope

The canonical geometry corpus contains a historical claim that the one-loop
moduli potential fixes the compact imaginary-time radius at the self-dual point
`R_psi = R_t`. Before using `R_psi` to set the length scale `ell` of the
fifth-channel gravitational connection, the actual stationarity statement must
be checked directly.

The displayed one-loop potential in `canonical/geometry/Rpsi_dynamical_fix.tex`
is

\[
V_{\rm mod}(R_\psi)
=-\frac32\ln(2\pi R_\psi)-E_3'(0).
\]

<!-- BILINGUAL-UNIT: rpsi-scale-audit.derivative -->
## Exact derivative check [L0]

For every finite `R_psi > 0`,

\[
\boxed{
\frac{dV_{\rm mod}}{dR_\psi}
=-\frac{3}{2R_\psi}\ne0.}
\]

Therefore the displayed potential has **no finite stationary point**. In
particular it does not, by itself, have a minimum at `R_psi = R_t`.

This is an internal consistency correction: it does not reject modular
self-duality as a structural condition; it rejects only the stronger claim that
the displayed logarithmic determinant already supplies a dynamical absolute
minimum.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.modular -->
## What modular self-duality can fix

Let

\[
x:=\frac{R_\psi}{R_t}>0.
\]

The modular inversion acts as `x -> 1/x`. Its unique positive fixed point is

\[
\boxed{x=1,\qquad R_\psi=R_t.}
\]

If a differentiable completed effective potential is genuinely invariant,

\[
V(x)=V(1/x),
\]

then differentiation gives

\[
V'(x)=-\frac1{x^2}V'(1/x),
\]

and at the fixed point

\[
\boxed{V'(1)=0.}
\]

Thus exact modular invariance can select the **dimensionless ratio**
`R_psi/R_t = 1` as a stationary point of a completed invariant potential. It
does not determine the common absolute length without one additional physical
scale or a scale-generating mechanism.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.n0 -->
## Why `N0` does not add a second physical scale

The locked UBT axioms define `N0 > 0` as a fixed global **unit-setting
constant** in

\[
E_\mu=N_0^{-1/2}D_\mu\Theta.
\]

It is not registered as an independently predicted dynamical observable. A
rescaling convention carried only by `N0` therefore must not be counted as a
second physical coupling, and it must not be used to manufacture an absolute
prediction for `R_psi` unless a separate observable relation is derived.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.impact -->
## Status impact

**ABSOLUTE `R_psi` MINIMUM FROM THE DISPLAYED LOGARITHMIC ONE-LOOP POTENTIAL:
CLOSED AS NO-GO [L0].**

**MODULAR FIXED-POINT RATIO `R_psi/R_t = 1`:
EXACT [L0].**

**ABSOLUTE COMMON LENGTH SCALE FROM THE CURRENT MODULAR ARGUMENT:
OPEN.**

Consequently the fifth-channel gravity scale `ell` must not be declared derived
from the old `R_psi` minimum claim. A one-constant gravitational completion
must either retain one genuine length/coupling constant, or derive an absolute
scale by a separate mechanism.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.verification -->
## Verification

`tools/verify_one_constant_gr_closure.py` checks the derivative of the displayed
potential and the fixed-point derivative identity symbolically. The statements
about the locked role of `N0` are grounded in `canonical/AXIOMS.md` and
`canonical/CANONICAL_DEFINITIONS.md`.
