# Phase-charge stabilisation of the Whitney null shell

**Status:** EXACT REDUCED-MODEL THEOREM / NONCANONICAL DYNAMICAL CANDIDATE  
**Recorded:** 2026-08-01  
**Physical status:** a conserved relative profile phase gives a strict finite minimum of the reduced support-scale energy; derivation from the UBT master action, locking to the externally measured shell radius, full perturbative stability, and invisibility remain open

## 1. Purpose

The clock-compensated support-volume route is regular on the visible-metric-null
Whitney sphere, but a positive tension term alone favours contraction.  This
note identifies the smallest `Theta`-only collective mode that can oppose that
contraction without changing the central visible metric.

The mechanism is a common time-dependent phase of the Whitney `psi=+/-1`
profile block.  It is not an additional fundamental field: it is a collective
coordinate of an already present component of `Theta`.

## 2. Phase-rotated Whitney sector

Write

\[
W(\theta,\phi,\psi)
=w_1e^{i\psi}q+w_2e^{-i\psi}p
\]

and replace the shell contribution by

\[
\boxed{
\Theta_W^{(\alpha)}
=\chi\,e^{i\alpha(t)}W.
}
\]

Here `alpha` is independent of `psi`.  Because the complex unit is central and
`span_C{q,p}` is totally null for the sharp-bilinear form,

\[
\gamma_{AB}^{(\alpha)}
=e^{2i\alpha}\gamma_{AB}^{(0)}=0,
\qquad A,B\in\{\theta,\phi\}.
\]

The additional time jet

\[
\partial_t\Theta_W^{(\alpha)}
=i\dot\alpha\,\Theta_W^{(\alpha)}
\]

also lies in the same totally null plane.  Consequently all of its central
sharp pairings with the Whitney angular and radial jets vanish.  The collective
phase therefore does not reopen the visible central metric channel at the
kinematic level.

The ordered area channel rotates but does not disappear:

\[
\mathcal B_W^{(\alpha)}=e^{2i\alpha}\mathcal B_W^{(0)}\ne0.
\]

By contrast, the clock-compensated Hermitian support Gram is invariant under
the common phase, and therefore supplies a positive kinetic norm for `alpha`.

## 3. Exact Whitney support coefficients

Let `c=cos(theta)` and

\[
P(c)=4c^4-3c^2+1.
\]

For unit Whitney amplitude, the support-area density is

\[
\sqrt{\det \mathsf h^W_{AB}}
=2\sin\theta\sqrt{(1+c^2)P(c)}.
\]

Define the positive dimensionless constants

\[
\boxed{
 a_W
 =4\pi\int_{-1}^{1}
 \sqrt{(1+c^2)P(c)}\,dc
}
\]

and

\[
\boxed{
 i_W
 =8\pi\int_{-1}^{1}
 (1-c^4)\sqrt{(1+c^2)P(c)}\,dc.
}
\]

Numerically,

\[
 a_W\simeq25.47135740784,
 \qquad
 i_W\simeq37.47809073013.
\]

For amplitude `chi`,

\[
A_W(\chi)=a_W\chi^2.
\]

Moreover,

\[
\left\langle
\operatorname{ReSc}
\bigl[(\partial_\alpha\Theta_W)^\ddagger
      (\partial_\alpha\Theta_W)\bigr]
\right\rangle_\psi
=2\chi^2(1-c^4),
\]

so the phase moment of inertia obtained by integrating this norm over the
support area is

\[
\boxed{I_\alpha(\chi)=\kappa_\alpha i_W\chi^4,}
\]

where `kappa_alpha>0` is the coefficient of the reduced Hermitian phase-kinetic
term.

## 4. Reduced action and conserved charge

The minimal low-frequency collective-coordinate Lagrangian is

\[
\boxed{
L_{\rm red}
=\frac12\kappa_\alpha i_W\chi^4\dot\alpha^2
-\sigma a_W\chi^2,
}
\]

with support tension `sigma>0`.

This expression is a reduced effective action, not yet a term derived from the
canonical UBT master action.  It is invariant under

\[
\alpha\mapsto\alpha+\alpha_0,
\]

and therefore has conserved charge

\[
\boxed{
Q_\alpha
=\kappa_\alpha i_W\chi^4\dot\alpha.
}
\]

At fixed charge, the static effective energy is

\[
\boxed{
E_Q(\chi)
=\sigma a_W\chi^2
+\frac{Q_\alpha^2}
       {2\kappa_\alpha i_W\chi^4}.
}
\]

The first term contracts the support sphere.  The fixed-charge term diverges
when `chi -> 0` and opposes collapse.

## 5. Exact finite-scale minimum

For nonzero `Q_alpha`, the energy has one and only one positive stationary
point:

\[
\boxed{
\chi_*^6
=\frac{Q_\alpha^2}
       {\sigma a_W\kappa_\alpha i_W}.
}
\]

At this point,

\[
\left.\frac{d^2E_Q}{d\chi^2}\right|_{\chi_*}
=12\sigma a_W>0,
\]

so it is a strict radial minimum in the reduced one-modulus model.  Its energy
is

\[
\boxed{
E_*=\frac32\sigma a_W\chi_*^2.
}
\]

For `Q_alpha=0`, no positive minimum exists and the tension term drives
`chi -> 0`.  Fixing the phase frequency rather than its conserved charge also
does not stabilise the scale.  Conservation of the internal relative-phase
charge is therefore the essential ingredient in this reduced mechanism.

## 6. Relation to the physical shell radius

The exact theorem above stabilises the **internal Whitney support scale**
`chi`.  The present off-shell shell ansatz treats `chi_0`, `R_1`, and `R_2` as
independent parameters.  It therefore does not yet prove that the externally
measured cloak radius is stabilised.

For a self-similar one-parameter shell family satisfying a dynamical matching
condition

\[
\chi=\zeta R,
\qquad \zeta>0,
\]

where all shell radii and the Whitney amplitude dilate together, the same
reduced theorem gives

\[
\boxed{
R_*^6
=\frac{Q_\alpha^2}
       {\sigma a_W\kappa_\alpha i_W\zeta^6}.
}
\]

This is a conditional finite-physical-radius result.  The matching relation
must be derived from a radial bulk action or a regular transition-layer term;
it may not be imposed as a canonical UBT axiom.

## 7. What is and is not closed

Closed in the reduced candidate model:

1. the phase mode is a collective coordinate of the existing Whitney block;
2. it leaves the central visible metric null exactly;
3. the clock-compensated support norm gives it positive inertia;
4. an exact conserved-charge energy has a unique strict finite support-scale
   minimum for `Q_alpha != 0`;
5. under a self-similar scale-lock hypothesis, the physical shell radius also
   has a unique strict minimum.

Still open:

1. derivation of the phase kinetic term and exact `U(1)` symmetry from the UBT
   master action;
2. proof that profile mixing and the full paired connection preserve
   `Q_alpha`;
3. a dynamical relation between `chi` and the exterior radii `R_1,R_2`;
4. full fluctuation analysis beyond the single radial modulus;
5. finite total bulk energy and absence of singular boundary stress;
6. electromagnetic and gravitational zero-scattering theorems.

The result is therefore a genuine stabilisation mechanism in a controlled
reduced model, not yet a completed machine or an on-shell solution of the full
UBT equations.
