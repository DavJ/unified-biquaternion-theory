# Proof status: canonical relation and generalized Dirac lift

## Theorem A — central metric identity

For

\[
E_\mu=i_{\rm c}e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k\in W_L,
\]

\[
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=e_\mu{}^a e_\nu{}^b\eta_{ab}\mathbf1.
\]

**Status:** proved algebraically `[L0]`.

## Theorem B — exact Clifford lift

For

\[
\mathcal C(E)=\begin{pmatrix}0&E\\E^\sharp&0\end{pmatrix},
\]

\[
\frac12\{\mathcal C(E),\mathcal C(F)\}
=H_L(E,F)I_4.
\]

Thus `Gamma_mu = C(E_mu)` satisfies the curved Clifford relation for exactly
the same metric defined by the canonical UBT relation.

**Status:** proved algebraically `[L0]`; exact symbolic verifier included.

A fixed complex-linear map `vec: B -> C^4` writes the same biquaternionic
field as `Psi=vec(Theta)`.  Similarity changes of this carrier conjugate all
`Gamma_mu` and leave the metric and characteristic determinant invariant.
No second fundamental field is introduced.

## Theorem C — metric rank

For every invertible tetrad `e`,

\[
g=e\eta e^T
\]

has differential of rank ten. For arbitrary symmetric `h`,

\[
\delta e=\tfrac12h g^{-1}e
\]

gives `delta g = h`. The kernel is

\[
\delta e=eX,\qquad X\eta+\eta X^T=0,
\]

and has dimension six.

**Status:** proved for every nondegenerate tetrad `[L1]`.

## Theorem D — fifth algebraic channel

The grading matrix

\[
\Gamma_*=\operatorname{diag}(I_2,-I_2)
\]

anticommutes with every lifted `Gamma_mu`. Hence either `Gamma_*` or
`i_c Gamma_*` supplies an exact fifth Clifford channel with square `+I` or
`-I`, respectively.

**Status:** algebraically proved `[L0]`.

This does not yet prove that `psi` is a macroscopic fifth spacetime coordinate.

## Theorem E — exact principal symbol and causal cone

For

\[
\sigma_4(\xi)=\Gamma^\mu\xi_\mu,
\]

the Clifford relation implies

\[
\sigma_4(\xi)^2=g^{\mu\nu}\xi_\mu\xi_\nu I_4,
\qquad
\det\sigma_4(\xi)=\left(g^{\mu\nu}\xi_\mu\xi_\nu\right)^2.
\]

Thus the generalized-Dirac lift has exactly the causal cone of the metric
already induced by the canonical UBT relation.  With an anticommuting fifth
channel satisfying `Gamma_psi^2 = epsilon I`,

\[
\sigma_5^2=\left(g^{\mu\nu}\xi_\mu\xi_\nu
+\varepsilon\xi_\psi^2\right)I_4.
\]

**Status:** proved algebraically `[L0]`; exact polynomial verifier included.

## Theorem F — conditional psi-normal first-jet projection

For an equation

\[
\Gamma_\psi D_\psi\Psi+\mathcal F(\Psi,E_\mu)=0
\]

with `Gamma_psi^2 = epsilon I` and no `D_psi Psi` inside `F`, the unique
pointwise solution is

\[
D_\psi\Psi=-\varepsilon\Gamma_\psi\mathcal F.
\]

Hence, while `D_psi Psi` is an independent first-jet slot, the equation
manifold projects surjectively onto all Lorentz-admissible `E_mu` and does not
reduce the rank-ten map `E -> g`.

**Status:** exactly proved as a conditional algebraic theorem `[L0-C]`.
It is not yet the canonical holomorphic on-shell theorem, because strict
holomorphy in `tau=t+i psi` relates the `t` and `psi` derivatives.

## Holomorphic on-shell rank boundary and constrained-rank projection criterion

The conditional psi-normal theorem must not be mistaken for a proof of
**holomorphic on-shell rank**.  Under strict covariant holomorphy,

\[
D_\psi\Psi=i_{\rm c}D_t\Psi,
\]

so `D_psi Psi` is not an independent auxiliary first-jet slot.  The correct
general pointwise question is therefore the following.  Let

\[
F(e,z)=0
\]

be the real action-derived constraints, where `e in R^16` denotes the Lorentz
tetrad coefficients and `z` collects every genuinely nonmetric variable that
remains independent after the holomorphy condition is imposed.  The admissible
tetrad variations are

\[
\mathcal A=\{\delta e:\;F_e\delta e\in\operatorname{im}F_z\}.
\]

The exact **constrained-rank projection criterion** is that the metric rank on
the equation manifold equals the rank of `D_e g` restricted to `A`.  If `F_z`
is surjective, every tetrad variation lifts and metric rank ten is retained.
If instead eight independent real equations act only on the sixteen tetrad
coefficients, the **rank-budget** leaves an admissible tangent space of
dimension eight and the metric rank is at most eight.

**Status:** the projection criterion and rank-budget no-go are proved exactly
`[L1]`.  The real Jacobian `(F_e,F_z)` of the finalized action-derived,
strictly holomorphic UBT equation has not yet been computed.  Therefore the
canonical holomorphic on-shell rank theorem remains open.

## Open theorem G — canonical generalized-Dirac dynamics

Derive from one UBT action an operator of the form

\[
\mathscr D_{\rm UBT}
=i_{\rm c}\Gamma^\mu[D\Theta]\nabla_\mu
+i_{\rm c}\Gamma_\psi D_\psi
-\mathcal M[\Theta,D\Theta]
\]

with no independent metric, tetrad or arbitrary connection.

**Status:** open.

## Theorem H — holomorphic constrained-rank criterion and remaining existence problem

The exact pointwise rank question is solved by Theorem I below: the admissible
tetrad tangent space must satisfy `A+K=R^16`, and invertible `F_Psi` is an
explicit no-extra-field sufficient condition, including after strict
holomorphy.

**Status:** pointwise first-jet rank criterion proved `[L1]`; derivation of the
required transversality from the canonical action and local existence of
solutions of the complete implicit PDE remain open.

## Theorem I — exact no-extra-variable constrained rank

Let the real form of the four-complex-component generalized-Dirac equation be

\[
F(\Psi,e)=0\in\mathbb R^8,
\]

where `Psi=vec(Theta)` is the value of the original UBT field and
`e=(e_mu^a)` is its Lorentz first jet.  Define

\[
\mathcal A=\{\delta e:\ F_e\delta e\in\operatorname{im}F_\Psi\},
\qquad
K=\ker D_eg.
\]

Then

\[
\boxed{\operatorname{rank}(D_eg|_{\mathcal A})
=\dim(\mathcal A+K)-6.}
\]

Hence full metric rank ten is retained exactly when

\[
\boxed{\mathcal A+K=\mathbb R^{16}.}
\]

**Status:** proved exactly `[L1]`; no auxiliary or additional field is used.

## Corollary I.1 — original-field absorption

If the real Jacobian `F_Psi` is invertible, every tetrad variation can be
cancelled by a variation of the value of the same original field,

\[
\delta\Psi=-F_\Psi^{-1}F_e\delta e.
\]

Therefore the constrained pointwise first-jet metric rank is ten.

For the strictly holomorphic generalized-Dirac candidate, a nonzero scalar
zero-order block `M=m I_4` gives `det_C M=m^4` and real rank eight.  More
generally,

\[
M=m_sI_4+i m_p\Gamma_*,
\qquad
\det_C M=(m_s^2+m_p^2)^2,
\]

so rank ten is retained whenever `(m_s,m_p)!=(0,0)`.

**Status:** proved conditionally `[L1-C]` on the finalized UBT equation having
such an invertible original-field Jacobian.  This condition introduces no new
variable; deriving the zero-order block from the canonical action remains
open.

## Corollary I.2 — first-order eight-constraint no-go

If `F_Psi=0` and the equation imposes eight independent real constraints only
on the tetrad, then the admissible tetrad tangent space has dimension eight
and the metric rank is at most eight.

**Status:** proved `[L1]`.

## Revised decisive open task

The rank count itself is no longer vague.  The canonical action must now prove
one of the following without extra fields:

1. the finalized holomorphic generalized-Dirac equation has invertible
   `F_Psi`; or
2. its admissible tetrad tangent space satisfies
   `A + K = R^16` by a more special gauge-transverse mechanism.

Local existence and integrability of the resulting implicit PDE remain
separate from this pointwise first-jet rank theorem.
