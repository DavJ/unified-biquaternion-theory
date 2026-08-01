# Hermitian support Gram for the tangential-null shell

**Status:** EXACT KINEMATIC RESULT / NON-CANONICAL ACTION ROUTE  
**Recorded:** 2026-08-01  
**Physical status:** the null shell has a nondegenerate internal support norm, but no Lorentz-covariant stabilising action has yet been derived

## 1. Why a second quadratic channel matters

The central visible metric is defined by the complex-bilinear sharp pairing,

\[
\gamma_{\mu\nu}\mathbf 1
=\left\langle\frac12
(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)\right\rangle_\psi.
\]

On the inner Whitney sphere its angular block vanishes exactly,

\[
\gamma_{AB}=0,\qquad A,B\in\{\theta,\phi\}.
\]

This gives zero visible area and a degenerate visible four-volume.  It does **not** imply that the full profile field has lost all rank or all possible measures.  The full Hermitian involution `ddagger` supplies a distinct real Gram tensor

\[
\boxed{
\mathsf h_{\mu\nu}
:=\left\langle
\operatorname{ReSc}(E_\mu^\ddagger E_\nu)
\right\rangle_\psi .
}
\]

`mathsf h` is not declared to be the physical spacetime metric.  It is an internal support Gram: a norm on the profile jets after a Hermitian profile frame has been chosen.

## 2. Null plane is not Hermitian-null

For

\[
q=\mathbf e_2+i\mathbf e_3,
\qquad
p=\mathbf 1-i\mathbf e_1,
\]

the sharp-bilinear plane is totally null,

\[
B(q,q)=B(p,p)=B(q,p)=0.
\]

Under the Hermitian scalar pairing one instead has

\[
\operatorname{ReSc}(q^\ddagger q)=2,
\qquad
\operatorname{ReSc}(p^\ddagger p)=2,
\qquad
\operatorname{ReSc}(q^\ddagger p)=0.
\]

Thus the same two directions that are invisible to the central sharp metric form an ordinary positive Hermitian two-plane.

## 3. Exact support metric of the Whitney sphere

For

\[
w_1=(1+i\cos\theta)\sin\theta\cos\phi,
\qquad
w_2=(1+i\cos\theta)\sin\theta\sin\phi,
\]

and

\[
\Theta_W=w_1e^{i\psi}q+w_2e^{-i\psi}p,
\]

the Hermitian angular Gram is

\[
\mathsf h_{AB}
=2\operatorname{Re}\!\left(
\partial_A\bar w_1\,\partial_Bw_1
+\partial_A\bar w_2\,\partial_Bw_2
\right).
\]

Writing `c=cos(theta)` and `s=sin(theta)`, direct calculation gives

\[
\boxed{
\begin{aligned}
\mathsf h_{\theta\theta}
&=2\left(4c^4-3c^2+1\right),\\
\mathsf h_{\theta\phi}&=0,\\
\mathsf h_{\phi\phi}
&=2(1+c^2)s^2.
\end{aligned}
}
\]

The coordinate determinant is

\[
\det\mathsf h_{AB}
=4s^2(1+c^2)(4c^4-3c^2+1).
\]

Both non-coordinate factors are strictly positive for `c in [-1,1]`:

\[
1+c^2>0,
\qquad
4c^4-3c^2+1>0
\]

(the latter quadratic in `c^2` has discriminant `-7`).  The factor `s^2` is only the usual degeneration of spherical coordinates at the poles.  Therefore `mathsf h_AB` is a smooth positive-definite metric on the tangent bundle of the sphere.

For the shell amplitude `chi_0`,

\[
\mathsf h_{AB}^{\rm shell}=\chi_0^2\mathsf h_{AB},
\]

and the invariant support-area density is

\[
\boxed{
 dA_{\mathsf h}
 =2\chi_0^2\sin\theta
 \sqrt{(1+\cos^2\theta)
 (4\cos^4\theta-3\cos^2\theta+1)}
 \,d\theta\,d\phi,
}
\]

which is regular and positive on `S^2`.

Hence the inner sphere simultaneously satisfies

\[
\boxed{dA_\gamma=0,\qquad dA_{\mathsf h}>0.}
\]

This is the precise sense in which the configuration is visible-metric-null but internally supported.

## 4. Four-dimensional support volume at the inner shell

At `r=R_1`, the Whitney ansatz has the orthogonal time and radial jets

\[
E_t=iP_t,\qquad E_r=P_r,
\]

with normalized profiles.  Therefore

\[
\mathsf h_{tt}=1,\qquad
\mathsf h_{rr}=1,
\qquad
\mathsf h_{tA}=\mathsf h_{rA}=0.
\]

The full support Gram is nondegenerate:

\[
\det\mathsf h_{\mu\nu}
=4\chi_0^4\sin^2\theta
(1+\cos^2\theta)
(4\cos^4\theta-3\cos^2\theta+1).
\]

Thus

\[
\boxed{
\det\gamma\big|_{R_1}=0,
\qquad
\det\mathsf h\big|_{R_1}>0
}
\]

in every regular angular chart.  A vanishing visible volume does not force the underlying one-field configuration to have zero internal volume.

## 5. Consequence for the action problem

The previous sharp-quartic four-form is regular but topological.  The Hermitian support Gram supplies a different route: a Nambu--Goto/DBI-type support-volume functional

\[
S_{\rm supp}[\Theta]
=T_{\rm supp}\int d^4x\,\sqrt{\det\mathsf h[\Theta]}
\]

is non-topological and remains finite where `det(gamma)=0`, provided `mathsf h` stays nondegenerate.  On a preferred UBT time slice, the corresponding static energy

\[
E_{\rm supp}
=T_{\rm supp}\int_{\Sigma_t}d^3x\,
\sqrt{\det\mathsf h_{ij}}
\]

is also well-defined at the null sphere.

These formulas are **candidate action routes**, not a completed fundamental action.  A pure support-volume term generally favours minimal volume and does not by itself guarantee a stable finite radius.  Winding/profile potentials or rigidity terms would still be required.

## 6. Covariance obstruction

The sharp pairing is preserved by the complex Lorentz/profile isometries used in the GR construction.  A positive Hermitian norm is preserved only by the corresponding unitary subgroup.  Therefore `mathsf h` cannot yet be inserted as a second canonical spacetime metric without one of the following:

1. a composite clock/timelike compensator that covariantises the Hermitian norm;
2. a proof that the invisibility phase dynamically reduces the frame symmetry to a unitary subgroup;
3. interpretation as a constitutive/analogue support metric rather than fundamental spacetime geometry;
4. an auxiliary first-order formulation whose extra field is nonpropagating and whose elimination reproduces the support action.

A possible covariant completion is to derive an `mathsf h`-unit one-form `u_mu[Theta]` from the UBT clock sector and define

\[
\widehat h_{\mu\nu}
=\mathsf h_{\mu\nu}-2u_\mu u_\nu,
\]

which has Lorentzian signature if `u` is normalized.  The existence, uniqueness, and gauge transformation of such a composite clock remain open.

## 6.5 Conditional clock-compensated completion

The model-specific covariance obstruction is narrowed in
`CLOCK_COMPENSATED_SUPPORT_GRAM.md`.  Projecting the same `Theta` onto its
dedicated clock Fourier profile produces a positive Hermitian compensator
`mathcal N_Theta`.  The weighted trace Gram

\[
\mathsf h^{\rm clk}_{\mu\nu}
=\frac12\left\langle\operatorname{ReTr}
\left(E_\mu^\ddagger\widehat{\mathcal N}_\Theta^{-1}
E_\nu\widehat{\mathcal N}_\Theta^{-1}\right)
\right\rangle_\psi
\]

is invariant under the standard local `SL(2,C)` paravector congruence.  On the
explicit Whitney shell `mathcal N_Theta=1`, so this is exactly the support Gram
computed above.  The same construction yields a scalar clock `T_Theta=t` and a
regular Lorentzian internal support tensor.

This is an exact conditional result for the selected shell clock mode, not a
canonical derivation of a unique clock projector or full paired-connection
covariance.

## 7. Updated ledger

Closed exactly:

1. the Whitney tangential-null plane is positive under the Hermitian scalar pairing;
2. its induced support Gram on `S^2` is smooth and positive definite;
3. the inner shell has zero visible area but nonzero support area;
4. the full inner-shell support Gram is nondegenerate;
5. a support-volume functional is regular where the visible metric degenerates.

Still open:

1. Lorentz/gauge-covariant promotion of the support Gram;
2. a derived clock or compensator rather than a preferred frame;
3. a potential/rigidity term selecting finite `R_1,R_2` and the Whitney profile;
4. finite conserved energy and perturbative stability;
5. proof that visible matter couples to `gamma` but not directly to `mathsf h` in the exterior;
6. Maxwell and gravitational scattering.

This route therefore resolves the immediate "zero visible volume implies zero action" concern, but not the dynamical or invisibility closure.
