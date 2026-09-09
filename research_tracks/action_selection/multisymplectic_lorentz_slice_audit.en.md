<!-- BILINGUAL-UNIT: multisymplectic-slice.provenance -->
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

# Lorentz-slice vanishing of the covariant multisymplectic action

<!-- BILINGUAL-UNIT: multisymplectic-slice.scope -->
## Scope and conventions

This note tests the already proposed action

\[
S_F=\frac12\int_U F(\Theta)\,Q\wedge Q,\qquad
P=D\Theta,\qquad Q=\frac12\omega_{AB}P^A\wedge P^B
\]

on the frozen canonical Lorentz branch. Here \(U\) is an oriented smooth
spacetime patch, the fields and coefficients are smooth, and variations have
compact support. The scalar \(F\) is a smooth real invariant on the field
values under consideration; singular coefficients are excluded.

The real field space is the realification of \(M_2(\mathbb C)\), ordered by
the real and then imaginary parts of \(z=(a,b,c,d)^T\), with matrix rows
\((a,b)\) and \((c,d)\). The previously classified pairing is

\[
h(u,v)=u^\dagger Gv,\qquad
G=\begin{pmatrix}
0&0&0&1\\0&-1&0&0\\0&0&-1&0\\1&0&0&0
\end{pmatrix},\qquad
\omega(u,v)=\operatorname{Im}h(u,v),\qquad
\Omega=\begin{pmatrix}0&G\\-G&0\end{pmatrix}.
\]

The imaginary part defines this previously proposed field-space symplectic
form. It is **not** a new projection defining the physical metric. The metric
continues to come from the canonical central sharp-anticommutator identity.

For the explicit spin representation below,

\[
D\Theta=d\Theta+\mathcal A\Theta+\Theta\mathcal A^\dagger
       =d\Theta+\mathcal A\Theta-\Theta\mathcal B,\qquad
\mathcal B=-\mathcal A^\dagger,\qquad
\mathcal A\in\mathfrak{sl}(2,\mathbb C).
\]

In real components this is \(D\Theta=d\Theta+\rho_*(\mathcal A)\Theta\).
The established symplectic connection can be held fixed, varied as an
auxiliary variable, or substituted as a differentiable composite functional.
These are different variational problems. The vanishing theorem below
applies to each when its stated slice condition holds; it does not infer
first-order composite equations from the fixed-connection calculation.

<!-- BILINGUAL-UNIT: multisymplectic-slice.lagrangian -->
## M1 — The canonical Lorentz slice is Lagrangian [L0]

Use the Pauli representation of the canonical quaternion basis,

\[
b_0=iI_2,\qquad b_k=-i\sigma_k,\qquad
W_L=\left\{b_a x^a:x^a\in\mathbb R\right\},\qquad
\eta=\operatorname{diag}(-1,1,1,1).
\]

The complex coordinate matrix whose columns are the four basis vectors is

\[
C=\begin{pmatrix}
i&0&0&-i\\
0&-i&-1&0\\
0&-i&1&0\\
i&0&0&i
\end{pmatrix},\qquad
C^\dagger GC=-2\eta.
\]

Thus \(h(Cx,Cy)=-2x^T\eta y\) is real whenever \(x,y\) are real, so

\[
\boxed{\omega|_{W_L\times W_L}=0.}
\]

The real inclusion

\[
J=\begin{pmatrix}\operatorname{Re}C\\\operatorname{Im}C\end{pmatrix}
\]

has rank four and obeys

\[
J^T\Omega J=0,\qquad
\dim_{\mathbb R}W_L=4=\frac12\dim_{\mathbb R}V.
\]

This is precisely a Lagrangian subspace: an isotropic subspace of half the
ambient dimension. The terminology and elementary criterion are standard;
see Ana Cannas da Silva, [Lectures on Symplectic Geometry, Homework 1](https://people.math.ethz.ch/~acannas/Papers/lsg.pdf).
The displayed UBT matrix restriction is calculated here.

Every represented symplectic transformation sends this plane to another
Lagrangian plane. In particular a common phase or a local spin transformation
of all four jet vectors cannot change the conclusion. No choice of a preferred
phase section is needed.

<!-- BILINGUAL-UNIT: multisymplectic-slice.vanishing -->
## M2 — Action and full first variation vanish on the slice [L1]

Assume the canonical tetrad condition throughout the patch:

\[
P_\mu=D_\mu\Theta=c_0 b_a e^a{}_\mu,\qquad
c_0=\sqrt{\mathcal N_0}>0,\qquad e^a{}_\mu\in\mathbb R.
\]

M1 gives the pointwise identity

\[
Q_{\mu\nu}=\omega(P_\mu,P_\nu)=0.
\]

This holds for every real coframe, including nondegenerate curved coframes;
neither a field equation nor a curvature restriction has been used.
It only restricts the covariant jet: the field value itself need not lie in
the Lorentz slice.

For arbitrary smooth variations of all the independent variables in the
chosen variational problem, differentiation before integration by parts gives

\[
\delta S_F
=\frac12\int_U\delta F\,Q\wedge Q
 +\int_U F\,\delta Q\wedge Q.
\]

Consequently, at every smooth slice configuration,

\[
\boxed{S_F=0,\qquad \delta S_F=0.}
\]

The variation is not required to preserve the slice. Each term already has a
factor of the background \(Q\). This also includes the induced variation of a
composite connection: the complete chain rule changes \(\delta Q\), but cannot
remove its multiplying factor \(Q\). Smooth dependence and an existing first
variation are required; singular substitutions are outside the theorem.

Thus every admissible smooth slice configuration is stationary for this
action sector. It cannot by itself distinguish Einstein coframes from
noneinsteinian coframes. Adding another action sector can change that
conclusion, but its dynamics must be derived separately.

<!-- BILINGUAL-UNIT: multisymplectic-slice.hessian -->
## M3 — What follows for the Hessian [L1]

At a background with \(Q=0\), the mixed second variation is

\[
\boxed{\delta_1\delta_2 S_F
=\int_U F\,\delta_1Q\wedge\delta_2Q.}
\]

Terms containing a variation of \(F\) or a second variation of \(Q\) vanish
because they still multiply the background \(Q\). If one variation is tangent
to a smooth family of slice configurations, then \(\delta_1Q=0\), so its
mixed pairing with every other variation vanishes. If the slice condition is
imposed for the whole configuration space before variation, the restricted
functional is identically zero and all its variations vanish.

The unrestricted Hessian must not be declared zero. A finite jet witness
illustrates the distinction. Let

\[
H=-2\eta,\qquad
Z=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
\qquad B=\frac12H^{-1}Z,\qquad
P_\mu(\varepsilon)=b_\mu+\varepsilon i b_aB^a{}_\mu.
\]

Direct polarization gives

\[
Q(\varepsilon)=\varepsilon
(dx^0\wedge dx^1+dx^2\wedge dx^3),\qquad
\frac12FQ(\varepsilon)\wedge Q(\varepsilon)
=F\varepsilon^2\,d^4x.
\]

For a nonzero coefficient the pointwise density has a nonzero second
derivative in this direction. This is **not** a demonstration of propagating
bulk modes: compatible field perturbations, integrations by parts, boundary
terms and the physical mode quotient still have to be accounted for. For
example, with a flat fixed connection and constant coefficient the original
pullback action is a boundary term. Its bulk Hessian vanishes even though a
pointwise jet-density Hessian can be nonzero.

<!-- BILINGUAL-UNIT: multisymplectic-slice.witness -->
## M4 — Explicit stationary coframe that is not Einstein [L1]

On a patch with \(t>0\), use dimensionless local coordinates and set

\[
e^0=dt,\qquad e^i=t^2dx^i,\qquad
\Theta=c_0t\,b_0,\qquad
g=-dt^2+t^4\sum_{i=1}^3(dx^i)^2.
\]

Let the Lorentz jet connection have the only nonzero frame components

\[
\widehat\omega^i{}_0=\widehat\omega^0{}_i=t\,dx^i,
\qquad
\mathcal A_{\rm jet}=-\frac t2\sum_{i=1}^3\sigma_i\,dx^i.
\]

The explicit two-sided action in the setup then gives

\[
D_{\rm jet}\Theta
=c_0 b_0\,dt+c_0t^2\sum_{i=1}^3 b_i\,dx^i
=c_0b_a e^a.
\]

The coframe is nondegenerate and the field representative is non-null:

\[
\det(e^a{}_\mu)=t^6,\qquad X^a=(c_0t,0,0,0),\qquad
\eta_{ab}X^aX^b=-c_0^2t^2.
\]

The physical torsion-free Lorentz connection is different:

\[
\omega_{\rm LC}^i{}_0=\omega_{\rm LC}^0{}_i=2t\,dx^i,\qquad
K^i{}_0=K^0{}_i=-t\,dx^i,\qquad
\widehat\omega=\omega_{\rm LC}+K,\qquad w=0.
\]

These are explicit composites in the already established split-jet
architecture. The displayed jet connection has torsion; it is not being
identified with the torsion-free physical connection. No second propagating
connection is postulated. The example represents the fields and coframe; it
does not derive a separate law selecting these composites.

Using
\(R^\rho{}_{\sigma\mu\nu}
=\partial_\mu\Gamma^\rho_{\nu\sigma}
-\partial_\nu\Gamma^\rho_{\mu\sigma}
+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}
-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}\)
and \(R_{\sigma\nu}=R^\rho{}_{\sigma\rho\nu}\), the physical metric has

\[
R_{00}=-\frac6{t^2},\qquad
R_{ii}=10t^2,\qquad R_{\mu\nu}=0\;(\mu\ne\nu),\qquad
R=\frac{36}{t^2}.
\]

In particular,

\[
\frac{R_{00}}{g_{00}}=\frac6{t^2}
\ne\frac{10}{t^2}=\frac{R_{ii}}{g_{ii}}.
\]

The metric does not satisfy \(R_{\mu\nu}=\Lambda g_{\mu\nu}\), even if a
point-dependent proportionality factor is allowed. Nevertheless \(Q=0\) and
M2 makes it stationary for every smooth member of the specified action
family. This is a concrete counterexample to vacuum Einstein selection by
that family alone; no claim of satisfying additional matter equations is made.

<!-- BILINGUAL-UNIT: multisymplectic-slice.previous -->
## Relation to the earlier auxiliary-connection obstruction

The [previous gauging theorem](theta_covariant_multisymplectic_gauging.en.md)
assumed both \(F\ne0\) and \(Q\wedge Q\ne0\) before using the symplectic wedge
isomorphism and generic orbit rank to collapse the tetrad rank.
M1 shows that its second assumption is never satisfied by the canonical
Lorentz jet. The theorem remains a valid conditional statement on the larger
real field space, but it does not analyze this canonical sector.

The missing sector is now covered directly: its problem is that the entire
action and its first variation vanish, so the pure auxiliary connection
equation also vanishes. It supplies no coframe-selection equation there.
This is stronger for the specified Lorentz branch than a generic rank
argument, and it does not depend on the orbit stratum or on \(F\ne0\).

The result concerns exactly the family displayed in the setup. It does not
eliminate the bivector/Clifford curvature actions, independently added
curvature sectors, or a genuinely derived quantum effective action.

<!-- BILINGUAL-UNIT: multisymplectic-slice.verification -->
## Verification and status

Run `tools/verify_multisymplectic_lorentz_slice.py`. The companion record is
`reports/multisymplectic_lorentz_slice_2026_09_08.json`.

The verifier supplies seven groups: the exact slice Gram identity; unrestricted
jet-density differentiation; tangent and normal variation checks; the generated
coframe and physical torsion check; a full coordinate Ricci calculation;
independent complex matrix checks under spin and phase transformations; and
independent finite differences of the density. Exact checks use SymPy;
independent numerical checks use NumPy and SciPy. Versions and source hashes
are recorded in the report.

The functional differentiation and smooth composite chain-rule argument are
analytic proofs, not consequences of finite sampling. Formal status is
`LEAN-PENDING`: Lean and Lake are absent in the inspected runtime, and no
compiled formalization is supplied.

**RESTRICTED ACTION-SELECTION OBSTRUCTION: PROVED [L1].**

**UNCONDITIONAL UBT GRAVITY, QUANTUM HESSIAN AND RH: OPEN.**

The canonical claim ledger is unchanged. The new result closes this precise
test of an existing action family; it does not introduce a new dynamical axiom.
