# Spherical tangential-null shell candidate

**Status:** SPECULATIVE / NON-CANONICAL / GEOMETRIC TARGET ONLY  
**Recorded:** 2026-08-01  
**Origin:** David Jaroš's proposed spherical invisibility geometry

## 1. Core idea

The candidate object is a spherical shell with inner radius `R_1` and outer
radius `R_2`. The intended nullity is not a collapse of all four spacetime
directions. It is a collapse of the two-dimensional tangent metric of the
inner sphere.

This matches the exact pointwise algebraic limit: the central symmetric
bilinear on one biquaternionic fibre has Witt index two, and the tangent plane
of `S^2` also has dimension two.

Let

\[
\mathfrak G_{\mu\nu}=E_\mu^\sharp E_\nu
=\gamma_{\mu\nu}\mathbf1+\Sigma_{\mu\nu}.
\]

At the inner spherical boundary the target is

\[
\boxed{
\gamma_{AB}\big|_{r=R_1}=0,
\qquad
\Sigma_{\theta\phi}\big|_{r=R_1}\ne0,
\qquad A,B\in\{\theta,\phi\}.
}
\]

The central metric channel assigns zero area to the inner sphere, while the
full ordered biquaternionic tensor retains nonzero oriented-area information.

## 2. Central spherical ansatz

For a static spherically symmetric central channel use

\[
ds_\gamma^2=-A(r)dt^2+B(r)dr^2
+C(r)\left(d\theta^2+\sin^2\theta\,d\phi^2\right).
\]

The induced metric on `r=constant` is

\[
\gamma_{AB}=C(r)
\begin{pmatrix}
1&0\\
0&\sin^2\theta
\end{pmatrix}.
\]

Hence

\[
\sqrt{\det\gamma_{AB}}=C(r)\sin\theta
\]

on a chosen real-positive branch, and the total central area is

\[
\mathcal A_\gamma(r)=4\pi C(r).
\]

The tangential-null boundary condition is therefore

\[
\boxed{C(R_1)=0.}
\]

For the block-diagonal spherical ansatz,

\[
\det\gamma=-A(r)B(r)C(r)^2\sin^2\theta,
\]

so the inner sphere is also a volume-degenerate boundary when `A` and `B` are
finite. This does not by itself imply that the full UBT action vanishes or
that the boundary is physically invisible.

## 3. Biquaternionically active surface

Choose two angular jets spanning a totally isotropic biquaternionic plane. A
local algebraic model is

\[
E_\theta\propto q=\mathbf e_2+i\mathbf e_3,
\qquad
E_\phi\propto r=\mathbf1-i\mathbf e_1,
\]

for which

\[
B(q,q)=B(r,r)=B(q,r)=0,
\qquad
q^\sharp r\ne0.
\]

Thus locally

\[
\gamma_{\theta\theta}
=\gamma_{\phi\phi}
=\gamma_{\theta\phi}=0,
\qquad
\Sigma_{\theta\phi}\ne0.
\]

This is the precise sense in which the surface may be central-metrically null
without being empty in the full biquaternionic geometry.

## 4. Shell and exterior matching

The annulus

\[
R_1<r<R_2
\]

must interpolate between the null inner boundary and an ordinary exterior.
Necessary boundary targets include

\[
C(R_1)=0,
\qquad
C(R_2)=R_2^2,
\]

and

\[
\Sigma_{\theta\phi}(R_1)\ne0,
\qquad
\Sigma_{\theta\phi}(R_2)=0,
\]

with `A(R_2),B(R_2)` matching the chosen vacuum exterior. Smoothness order and
junction conditions must be derived from the eventual polynomial UBT action;
they cannot be imposed only by analogy with GR.

## 5. Global patching on the sphere

No smooth nonvanishing tangent frame exists globally on `S^2`. Therefore the
pair `(E_theta,E_phi)` cannot be treated as one globally regular coordinate
frame. A valid construction requires at least northern and southern patches,
with overlap transformations preserving

\[
\gamma_{AB}=0
\]

and the covariant meaning of the two-form

\[
\mathcal B_{S^2}
=\Sigma_{\theta\phi}\,d\theta\wedge d\phi.
\]

The patch transition may carry topological information. It must not create an
uncontrolled string singularity at either pole.

## 6. What would count as invisibility

Zero central area is a geometric prerequisite, not the final observable.
The shell is electromagnetically invisible only if the complete exterior
boundary/scattering map equals that of vacuum, including amplitude, phase,
polarisation, and all incidence directions. It is gravitationally invisible
only if the exterior real metric and stress-energy response equal the chosen
vacuum solution.

The target conditions are schematically

\[
\mathcal S_{\rm EM}^{\rm exterior}[\Theta_{\rm shell}]
=\mathcal S_{\rm EM}^{\rm vacuum},
\]

\[
\mathcal S_{\rm grav}^{\rm exterior}[\Theta_{\rm shell}]
=\mathcal S_{\rm grav}^{\rm vacuum}.
\]

## 7. Required proofs

1. Construct an integrable field `Theta(t,r,theta,phi,psi)` realising the
   angular null pair in two spherical patches.
2. Derive a first-order or polynomial action regular at `C(R_1)=0`.
3. Prove finite energy and absence of singular surface stress/current.
4. Determine the dynamics and stability of the nonzero
   `Sigma_theta_phi` surface channel.
5. Solve Maxwell and gravitational matching across the shell.
6. Show zero exterior scattering rather than merely zero induced area.

## 8. Falsification gates

This route fails if any of the following holds:

- the angular null pair cannot be integrated to a global patched `Theta`;
- every regular action forces `Sigma_theta_phi=0` when `C=0`;
- the null boundary necessarily carries divergent energy or surface current;
- matching to a regular exterior necessarily produces nonzero scattering;
- the shell is unstable under arbitrarily small perturbations;
- the required constitutive response violates the admissible reality or
  causality conditions of the visible sector.

## 9. Claim discipline

Recorded here is a mathematically motivated spherical candidate geometry. It
is not an on-shell UBT solution, a proof of invisibility, or an engineering
blueprint.
