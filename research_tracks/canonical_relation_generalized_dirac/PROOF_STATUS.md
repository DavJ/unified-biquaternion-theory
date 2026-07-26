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

## Open theorem H — holomorphic on-shell rank and existence

Prove that solutions of the complete implicit field equations retain a
nondegenerate Lorentz tetrad and enough admissible variations for metric rank
ten after gauge and complex-time constraints.

**Status:** open; this is the decisive next rank theorem.
