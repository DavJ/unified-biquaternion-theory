# Biquaternionic metric nullity and invisibility program

**Author:** Ing. David Jaroš  
**Status:** SPECULATIVE RESEARCH DIRECTION — NOT CANONICAL, NOT AN ENGINEERING CLAIM  
**Recorded:** 2026-08-01

## 1. Research motivation

The historical UBT intuition was that geometric invisibility may be easier in
a genuinely biquaternionic geometry than in a purely real pseudo-Riemannian
one. The modern covariant-tetrad formulation solved the GR metric problem by
selecting a central symmetric anticommutator. That was useful for GR, but it
also obscured the original larger object.

This program restores the larger object as an explicit research variable
without changing the canonical GR metric.

## 2. Full geometric bilinear versus GR projection

Let

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in\mathbb C\otimes\mathbb H.
\]

Define the full ordered bilinear

\[
\boxed{\mathfrak G_{\mu\nu}:=E_\mu^\sharp E_\nu.}
\]

It decomposes uniquely as

\[
\mathfrak G_{\mu\nu}
=\gamma_{\mu\nu}\mathbf1+\Sigma_{\mu\nu},
\]

with

\[
\gamma_{\mu\nu}\mathbf1
=\frac12\left(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu\right),
\qquad
\Sigma_{\mu\nu}
=\frac12\left(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu\right).
\]

For arbitrary biquaternionic tetrad components, `gamma_mu_nu` is a central
complex symmetric tensor. On the Lorentz-real branch,

\[
\gamma_{\mu\nu}=g_{\mu\nu}\in\mathbb R.
\]

The canonical GR metric is therefore a projection/channel of the full
biquaternionic bilinear, not the whole algebra-valued geometry.

Terminology used in this track:

- **full biquaternionic geometric tensor:** `mathfrak G_mu_nu`;
- **central complex metric channel:** `gamma_mu_nu`;
- **classical metric:** `g_mu_nu = Re(gamma_mu_nu)` on an admissible real branch;
- **bivector channel:** `Sigma_mu_nu`.

The phrase **biquaternionic metric** may be used historically or as a candidate
interpretation of `mathfrak G`, but it is not yet a metric in the standard
symmetric, central, invertible sense.

## 3. Exact reason the quaternionic metric disappeared from `ds^2`

For commuting coordinate increments,

\[
\begin{aligned}
d\mathfrak S^2
&:=\mathfrak G_{\mu\nu}\,dx^\mu dx^\nu\\
&=\gamma_{\mu\nu}\,dx^\mu dx^\nu\,\mathbf1
 +\Sigma_{\mu\nu}\,dx^\mu dx^\nu\\
&=\gamma_{\mu\nu}\,dx^\mu dx^\nu\,\mathbf1,
\end{aligned}
\]

because

\[
\Sigma_{\mu\nu}=-\Sigma_{\nu\mu},
\qquad
 dx^\mu dx^\nu=dx^\nu dx^\mu.
\]

Thus `Sigma` is not removed from the full product; it is annihilated by the
ordinary symmetric line-element contraction.

This gives a precise fork:

### Route Q1 — central degeneracy

Keep commuting coordinates and study

\[
\det\gamma=0
\quad\text{or}\quad
\gamma_{\mu\nu}=0,
\]

while allowing `Sigma != 0`.

### Route Q2 — area/two-form geometry

Retain the ordinary line element but introduce the oriented biquaternionic
area observable

\[
\mathcal B
=\frac12\Sigma_{\mu\nu}\,dx^\mu\wedge dx^\nu.
\]

A sector may be line-metrically null yet carry nonzero area/spin/flux data.

### Route Q3 — ordered or noncommutative increments

For increments `dQ^mu` with nonzero commutator,

\[
\begin{aligned}
d\mathfrak S^2
={}&\frac12\gamma_{\mu\nu}
\{dQ^\mu,dQ^\nu\}\mathbf1\\
&+\frac12\Sigma_{\mu\nu}
[dQ^\mu,dQ^\nu].
\end{aligned}
\]

Then the genuinely biquaternionic part can contribute to an interval-like
object. This route requires a new covariant differential calculus and is not
part of current canonical UBT.

### Route Q4 — noncentral symmetric Hermitian form

Investigate a candidate such as

\[
H_{\mu\nu}
=\frac12\left(E_\mu^\ddagger E_\nu+E_\nu^\ddagger E_\mu\right),
\]

which need not be central. Before it can be called a metric one must derive:

- its transformation law;
- a suitable determinant (for example through a faithful complex matrix
  representation, or a Study/Moore-type determinant where applicable);
- left/right inverse conventions;
- a compatible connection and curvature;
- the real Lorentzian limit and causal interpretation.

## 4. Three inequivalent nullity conditions

### 4.1 Curve-null

\[
\gamma_{\mu\nu}v^\mu v^\nu=0.
\]

This is the ordinary null-cone condition. It is coordinate invariant, but it
does not imply invisibility: photons are null and still interact.

### 4.2 Volume-null

For the central complex channel,

\[
\boxed{\det\gamma=0.}
\]

The associated standard volume density

\[
dV_\gamma=\sqrt{-\det\gamma}\,d^4x
\]

vanishes formally, but inverse-metric actions may become undefined rather than
zero. A viable branch needs a polynomial/first-order action that remains
well-defined at degeneracy.

A purely imaginary nondegenerate metric is not volume-null in four dimensions:

\[
\gamma_{\mu\nu}=i h_{\mu\nu}
\quad\Longrightarrow\quad
\det\gamma=i^4\det h=\det h.
\]

### 4.3 Metric-null but biquaternionically active

\[
\boxed{\gamma_{\mu\nu}=0,
\qquad \Sigma_{\mu\nu}\neq0.}
\]

This is the sharpest algebraic form of the original intuition: no ordinary
quadratic metric channel, but a nonzero full biquaternionic product.

An explicit pointwise witness exists. Let

\[
q=\mathbf e_2+i\mathbf e_3,
\qquad
r=\mathbf1-i\mathbf e_1.
\]

With the bilinear scalar channel

\[
B(q,r)\mathbf1
=\frac12(q^\sharp r+r^\sharp q),
\]

one has

\[
B(q,q)=B(r,r)=B(q,r)=0,
\]

while

\[
q^\sharp r=-2\mathbf e_2-2i\mathbf e_3\neq0,
\qquad
r^\sharp q=-q^\sharp r.
\]

Thus a two-direction jet can be metric-null in the central channel while its
antisymmetric biquaternionic channel is nonzero. This is only an algebraic
witness, not yet a spacetime solution or physical object.

### 4.4 Pointwise rank obstruction

The pointwise space `C tensor H` is four-dimensional over `C`, and the central
bilinear `B` is nondegenerate and symmetric. If a subspace `U` is totally
isotropic, then `U` is contained in its orthogonal complement `U^perp`.
Nondegeneracy gives

\[
\dim U+\dim U^\perp=4,
\]

and therefore

\[
\boxed{\dim U\le 2.}
\]

Consequently, if four pointwise jets satisfy

\[
B(E_\mu,E_\nu)=0\qquad\hbox{for every }\mu,\nu,
\]

their span has rank at most two. A pointwise branch with
`gamma_mu_nu=0` therefore cannot simultaneously be an invertible ordinary
four-dimensional tetrad. It must be interpreted as a degenerate phase,
defect, boundary configuration, or lower-rank sector unless additional
profile structure is retained.

### 4.5 UBT profile-space escape and a rank-four witness

The obstruction above applies to one copy of `C tensor H` at a fixed `psi`.
It does not apply to the full UBT profile space. Let `psi` have period
`2 pi`, retain the null pair `q,r` above, and define

\[
\begin{aligned}
E_0(\psi)&=e^{ i\psi}q,&
E_1(\psi)&=e^{-i\psi}r,\\
E_2(\psi)&=e^{2i\psi}q,&
E_3(\psi)&=e^{-2i\psi}r.
\end{aligned}
\]

These four profiles are linearly independent as functions of `psi`. With the
translation-invariant profile average

\[
\langle f\rangle_\psi
=\frac1{2\pi}\int_0^{2\pi}f(\psi)\,d\psi,
\]

the central profile metric vanishes:

\[
\boxed{
\gamma^{\rm prof}_{\mu\nu}\mathbf1
=\left\langle
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
\right\rangle_\psi=0.
}
\]

However, the averaged ordered tensor remains nonzero. In particular,

\[
\Sigma^{\rm prof}_{01}=q^\sharp r\ne0,
\qquad
\Sigma^{\rm prof}_{23}=q^\sharp r\ne0.
\]

Thus the full UBT profile space admits a rank-four family of jets that is
central-metric-null but biquaternionically active. This is an exact algebraic
profile witness. It still does not provide an inverse metric, a nonzero
standard four-volume, an on-shell solution, stability, or invisibility.

The distinction is essential:

- pointwise metric-null jets have rank at most two;
- profile-valued metric-null jets may have functional rank four;
- neither statement by itself supplies a regular physical spacetime action.

A detailed statement and verifier are recorded in
`PROFILE_METRIC_NULL_WITNESS.md`.

### 4.6 Spherical tangential-null shell candidate

For a spherical invisibility candidate it is not necessary to make all four
spacetime directions metric-null. A spatial sphere has a two-dimensional
tangent plane, so the pointwise bound `dim U <= 2` is exactly large enough for
its angular directions.

In spherical coordinates let `A,B` range over `theta,phi`. The proposed inner
boundary condition at `r=R_1` is

\[
\boxed{
\gamma_{AB}\big|_{R_1}=0,
\qquad
\mathcal B_{S^2}\big|_{R_1}\ne0.
}
\]

Thus the central induced area density vanishes while the full ordered
biquaternionic geometry retains a nonzero oriented-area channel. For a static
spherically symmetric central metric

\[
ds_\gamma^2=-A(r)dt^2+B(r)dr^2
+C(r)\left(d\theta^2+\sin^2\theta\,d\phi^2\right),
\]

the inner condition is `C(R_1)=0`. Then

\[
dA_\gamma=C(R_1)\sin\theta\,d\theta\,d\phi=0,
\]

and, when `A(R_1)` and `B(R_1)` remain finite,

\[
\det\gamma\big|_{R_1}
=-A(R_1)B(R_1)C(R_1)^2\sin^2\theta=0.
\]

The shell `R_1<r<R_2` must interpolate to the ordinary exterior geometry and
must satisfy at least

\[
C(R_2)=R_2^2,
\qquad
\mathcal B_{S^2}(R_2)=0,
\]

with the appropriate exterior values of `A` and `B`. These are only geometric
boundary targets. Physical invisibility additionally requires vacuum exterior
Maxwell/gravitational scattering data, finite action, stability, and absence
of singular surface sources.

The coordinate tangent-frame obstruction does not require a patchwise `Theta`.
The global Whitney-type construction in
`WHITNEY_SPHERICAL_NULL_SHELL_THETA.md` uses Cartesian sphere functions and
closes angular integrability off shell. The remaining action and scattering
gates are recorded in `SPHERICAL_TANGENTIAL_NULL_SHELL.md`.

## 5. Action and volume questions

The statement “zero volume implies zero action” is true only for action terms
that are regular polynomial top forms proportional to the vanishing volume
form. It is not automatic for actions containing `gamma^{-1}`, boundary terms,
or metric-independent topological densities.

The track must compare at least three action classes:

1. **inverse-metric actions** — generally singular at `det(gamma)=0`;
2. **first-order tetrad/Cartan polynomial actions** — may admit degenerate
   tetrads without algebraic divergence;
3. **full-biquaternionic actions** built from `mathfrak G`, `Sigma`, curvature,
   and wedge products — determinant and reality conditions remain open.

For a full noncommutative matrix `mathfrak G_mu_nu`, writing
`det(mathfrak G)` is not innocent. The determinant prescription, ordering, and
covariance must be specified and shown to reduce to `det(g)` in the GR sector.

The exact audit `POLYNOMIAL_ACTION_REGULARITY_AUDIT.md` now closes one narrow
subquestion.  The metric-free sharp-quartic four-form

\[
\mathcal K_\Theta=d_4\Theta^\sharp\wedge d_4\Theta,
\qquad
S_{\rm top}\propto\int\langle\ell(\mathcal K_\Theta\wedge\mathcal K_\Theta)\rangle_\psi
\]

is polynomial and regular at degeneracy, but it is an exact boundary term.
Thus regularity alone is possible; dynamical selection is not obtained from a
constant-coefficient first-jet four-form.  The next live class requires a
field-dependent profile coefficient/operator or an auxiliary first-order
structure.

## 6. Operational definition of invisibility

A null or degenerate metric is not sufficient. A candidate configuration is
**electromagnetically invisible** only if its exterior Maxwell scattering data
match vacuum, including phase, amplitude, and polarisation. It is
**gravitationally invisible** only if the exterior real-sector metric and
stress-energy response match vacuum to the stated precision.

A complete criterion is schematically

\[
\mathcal S_{\rm exterior}^{\rm visible}
[\Theta_{\rm candidate}]
=\mathcal S_{\rm exterior}^{\rm vacuum},
\]

and

\[
S_{\rm mix}[\gamma,\Sigma,\Theta,\Psi_{\rm visible}]=0
\]

on the candidate branch, not merely `ds^2=0`.

## 6.5 Hermitian support-volume route

The central sharp metric can be null while the same profile jets remain
nondegenerate under the full Hermitian scalar pairing.  Define the real support
Gram

\[
\mathsf h_{\mu\nu}
=\left\langle\operatorname{ReSc}
(E_\mu^\ddagger E_\nu)\right\rangle_\psi.
\]

For the global Whitney sphere, `gamma_AB=0` but `mathsf h_AB` is smooth and
positive definite.  Consequently the inner sphere has zero visible area and a
nonzero internal support area.  The full support Gram is also nondegenerate at
`R_1`, so a support-volume/Nambu--Goto-type functional can remain regular
without using `gamma^{-1}`.

This does not yet provide a canonical action.  The positive Hermitian pairing
is invariant under a unitary profile-frame subgroup, not automatically under
the full complex Lorentz/profile isometry used by the GR metric.  Promotion
therefore requires a composite clock/compensator, a derived symmetry reduction,
or an explicit constitutive interpretation.  See
`HERMITIAN_SUPPORT_GRAM_ROUTE.md`.
A model-specific `Theta`-only clock compensator and locally Lorentz-congruence-invariant support Gram are derived in `CLOCK_COMPENSATED_SUPPORT_GRAM.md`; uniqueness of the clock projector and full bimodule covariance remain open.

## 6.6 Conserved relative-phase stabilisation

The Whitney `psi=+/-1` block admits a common collective phase

\[
\Theta_W\mapsto e^{i\alpha(t)}\Theta_W.
\]

Because the whole block lies in a totally sharp-null plane, this motion leaves
the central visible metric null.  The clock-compensated Hermitian support Gram,
however, assigns it positive inertia.  In the minimal reduced model, fixed
relative-phase charge produces

\[
E_Q(\chi)=\sigma a_W\chi^2+
\frac{Q_\alpha^2}{2\kappa_\alpha i_W\chi^4},
\]

with a unique strict finite minimum.  This closes a reduced support-scale
stabilisation theorem, not the full shell dynamics.  The master-action origin
of the phase symmetry and a dynamical relation between the support amplitude
and the exterior shell radius remain open.  See
`PHASE_CHARGE_FINITE_SCALE_STABILIZATION.md`.

## 7. Research stages

### I-0 — algebraic classification

- classify isotropic subspaces of the central bilinear `B`;
- classify cases `gamma=0, Sigma!=0` and `det(gamma)=0`;
- determine which are invariant under allowed frame transformations.

### I-1 — covariant field realisation

- construct smooth `Theta(x,psi)` jets realising a nullity class;
- check integrability and connection compatibility;
- distinguish isolated points, hypersurfaces, and open regions.

### I-2 — regular action at degeneracy

- **weak regularity closed:** a pure-Theta polynomial top form exists without
  `gamma^{-1}`, but the simplest constant-coefficient term is topological;
- classify admissible non-topological profile-weighted or auxiliary
  first-order actions;
- derive equations of motion and constraints;
- derive the reduced phase-charge term from the master action and determine
  whether its exact conserved charge survives full profile mixing;
- lock the finite support scale to the exterior shell radius;
- prove nontrivial finite-energy solutions and full stability.

### I-3 — coupling and visibility theorem

- derive visible-matter coupling from the same UBT action;
- calculate mixing between `gamma` and `Sigma` sectors;
- determine whether an algebra-active metric-null branch can remain dark.

### I-4 — exterior and boundary problem

- solve the matching problem between a null/degenerate interior and a
  nondegenerate exterior;
- calculate electromagnetic and gravitational scattering;
- exclude singular shells and uncontrolled energy requirements.

### I-5 — analogue experiment

Only after I-0--I-4 should a laboratory analogue be proposed. A metamaterial or
wave-system analogue would test the mathematics of nullity and boundary
matching; it would not by itself prove spacetime invisibility.

## 8. Falsification criteria

The proposed route fails if any of the following is proved:

- every covariant `gamma=0, Sigma!=0` jet is pure gauge or non-integrable;
- every open metric-null region forces the full `Theta` curvature/product to
  vanish;
- no regular bounded action exists at the required degeneracy;
- visible-sector mixing is unavoidable and nonzero;
- boundary matching necessarily creates detectable scattering or singular
  stress-energy;
- the noncommutative metric route has no invariant determinant/causal limit.

## 9. Claim discipline

What is currently established:

- the full bilinear `mathfrak G` exists;
- its symmetric channel is central complex;
- its antisymmetric channel is genuinely biquaternionic;
- commuting line-element contraction removes the antisymmetric channel;
- algebraic metric-null but biquaternionically nonzero witnesses exist.

What is not established:

- an on-shell invisible object;
- a fully stable degenerate spacetime region beyond the reduced charged-scale mode;
- a full biquaternionic determinant or volume;
- electromagnetic or gravitational decoupling;
- an invisibility machine or engineering design.
