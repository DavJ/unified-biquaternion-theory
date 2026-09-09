<!-- BILINGUAL-UNIT: biquat-induced.provenance -->
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

# Biquaternionic tetrad route to induced gravity

<!-- BILINGUAL-UNIT: biquat-induced.scope -->
## Scope correction

This audit keeps the frozen UBT architecture:

\[
\Theta\in\mathbb C\otimes\mathbb H,\qquad
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g_{\mu\nu}\mathbf1.
\]

The covariant tetrad is the geometric bridge. No independent tetrad, spinor
replacement for `Theta`, or an additional physical geometric sector
is introduced. The periodic `psi` direction below is used only under the
explicit spectral-domain assumption already stated in the induced-gravity
calculation; it does not define or average the canonical metric.

The question is whether quantum fluctuations of the same biquaternionic field
can induce the Einstein term and its coefficient.

<!-- BILINGUAL-UNIT: biquat-induced.questions -->
## Two logically distinct gravitational inputs

In the Euclidean effective metric theory, consider
\[
S_{\rm EH}[g]=-\frac1{16\pi G}\int d^4x\sqrt g\,R.
\]
There are two separate questions: why this term is present, and what its
renormalized coefficient is. With unrestricted compactly supported metric
variations, adopting this action with any nonzero constant coefficient gives
the vacuum Einstein equation; the magnitude cancels. With matter it becomes
observable as `G`. This statement assumes the effective metric variational
principle. It does not establish that varying a composite metric through
`Theta` realizes all those variations. The cosmological term also needs its
own derivation or input.

Thus inserting a measured `G` completes a specified effective gravitational
action. It does not supply the missing microscopic action or prove its
variational reduction from the biquaternionic axioms.

<!-- BILINGUAL-UNIT: biquat-induced.formula -->
## Conditional Sakharov coefficient

Assume a smooth four-dimensional Euclidean background without a boundary,
a well-defined bosonic Gaussian measure, and scalar Laplace operators
\[
P_{j,n}=-\nabla^2+m_j^2+\frac{n^2}{R_\psi^2}+\xi_jR,
\qquad n\in\mathbb Z,\qquad m_j^2\geq0.
\]
The periodic modes, their multiplicities, constant masses and curvature
couplings are assumptions here. Any additional endomorphism, gauge or ghost
operator must be derived and included before applying this scalar formula.
Use a suitable infrared prescription if the full determinant has zero modes.

The local heat expansion and proper-time prescription give
\[
\operatorname{Tr}e^{-sP_j}\sim
\frac{e^{-m_j^2s}\vartheta_3(0,e^{-s/R_\psi^2})}{(4\pi s)^2}
\int\sqrt g\,\bigl[1+s(1/6-\xi_j)R+\cdots\bigr],
\qquad
\Gamma_1=-\frac12\sum_j\int_{M_{\rm UV}^{-2}}^\infty
\frac{ds}{s}\operatorname{Tr}e^{-sP_j}.
\]
Here the omitted terms include higher curvature and derivative terms.
Define
\[
\mathcal I_1(M_{\rm UV},R_\psi,m)
:=\int_{M_{\rm UV}^{-2}}^\infty ds\,s^{-2}e^{-m^2s}
\vartheta_3(0,e^{-s/R_\psi^2}).
\]
Matching the local term linear in curvature to the displayed Einstein action
yields
\[
\Gamma_{1,R}=-\frac1{192\pi^2}
\sum_j(1-6\xi_j)\mathcal I_1\int\sqrt g\,R,
\qquad
\boxed{\frac1{G_{\rm ind}}=
\frac1{12\pi}\sum_j(1-6\xi_j)\mathcal I_1(M_{\rm UV},R_\psi,m_j).}
\]
This determines the coefficient in the stated local expansion and regulator
prescription. It is not an exact full determinant at arbitrary curvature, a
control of its infrared part, or a derivation of the UBT fluctuation operator.

At \(M_{\rm UV}R_\psi=1\) and \(m_j=0\),
\[
C_\psi:=\int_1^\infty\frac{du}{u^2}\vartheta_3(0,e^{-u})
=1.303410251859279308\ldots,
\]
\[
\boxed{\frac1{G_{\rm ind}}=
\frac{C_\psi M_{\rm UV}^2}{12\pi}N_{\rm ind},
\qquad N_{\rm ind}:=\sum_j(1-6\xi_j).}
\]
For an independent evaluation, positivity permits termwise integration
(Tonelli's theorem); one integration by parts gives
\[
C_\psi=1+2\sum_{n=1}^\infty
\bigl[e^{-n^2}-n^2 E_1(n^2)\bigr],
\qquad E_1(z)=\int_z^\infty\frac{e^{-t}}t\,dt.
\]
The remainder after \(N\) terms satisfies
\[
0<r_N\leq
\frac{2e^{-(N+1)^2}}{(N+1)^2[1-e^{-(2N+3)}]}.
\]
Indeed each omitted integral is bounded by \(e^{-n^2}/n^2\), and successive
squares differ by at least \(2N+3\). This controls the series truncation;
floating-point quadrature still has its own numerical error.

Identical conformally coupled scalar modes, \(\xi_j=1/6\), contribute zero
to this Einstein coefficient. In the massless equal-radius specialization,
a positive induced Newton coefficient requires \(N_{\rm ind}>0\).
Other sectors require their own heat coefficients.

<!-- BILINGUAL-UNIT: biquat-induced.count -->
## The biquaternion dimension is not yet the physical mode count

Write

\[
X=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
H(X)=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2.
\]

In real coordinates, the connected-symmetry invariant quadratic form has
signature

\[
\boxed{\operatorname{sig}_{\mathbb R}H=(2,6).}
\]

On the canonical Lorentz-real subspace

\[
X=i x^0I-i x^k\sigma_k,\qquad x^a\in\mathbb R,
\]

it restricts to

\[
\boxed{H(X)=2\left[(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2\right],}
\]

with signature \((1,3)\). Hence neither “eight real coordinates of one
biquaternion” nor “four Lorentz-real coordinates” is by itself a count of
healthy Euclidean bosonic modes. The physical count requires the constraints,
gauge directions, statistics and an admissible Euclidean contour.

Define \(\bar M_{\rm Pl}^2=(8\pi G_{\rm ind})^{-1}\) in units
\(\hbar=c=1\). For orientation only, the two naive minimal-coupling
substitutions at the preceding massless equal-scale point give

\[
\left.\frac{\bar M_{\rm Pl}}{M_{\rm UV}}\right|_{N_{\rm ind}=8}
=0.1049059378244545\ldots,
\qquad
\left.\frac{\bar M_{\rm Pl}}{M_{\rm UV}}\right|_{N_{\rm ind}=4}
=0.0741797000224061\ldots.
\]

The factor \(\sqrt2\) between them is already enough to show that component
counting cannot be silently used as a prediction of `G`.

<!-- BILINGUAL-UNIT: biquat-induced.locked -->
## Complete volume variation for a fixed connection

The metric lock gives the exact four-dimensional identity
\[
\frac12\sqrt{|g|}\,g^{\mu\nu}
\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp
=2\mathcal N_0\sqrt{|g|}.
\]
The pairing here denotes the central sharp anticommutator coefficient.
The involution \(\sharp\) is quaternionic conjugation (the matrix adjugate),
not complex conjugation. Set \(c_0=\sqrt{\mathcal N_0}>0\).

**Lemma B-VAR [L1].** Work on an oriented coordinate patch with a smooth
Lorentz-real field and a fixed smooth Lorentz connection \(C\):
\[
\Theta=b_aX^a,\quad X^a\in\mathbb R,\quad
b_0=iI,\quad b_k=-i\sigma_k,\quad
\eta=\operatorname{diag}(-1,1,1,1),\quad
C^T\eta+\eta C=0.
\]
The two-sided action is
\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu,
\qquad A_\mu=\Omega_\mu,\quad B_\mu=-\Omega_\mu^\dagger,
\]
where \(\Omega\) represents \(C\) on these biquaternions. Thus
\[
E^a=c_0^{-1}(dX^a+C^a{}_bX^b),\quad
F=dC+C\wedge C,\quad DE^a=c_0^{-1}F^a{}_bX^b.
\]
Fix the local frame for the variation; \(C\) is prescribed, not an additional
varied field. Assume \(X,C\) are smooth, \(\det E>0\), and the variations
\(u,v\) are smooth with compact support, small enough to preserve
nondegeneracy. The four real components are a restriction of the same
`Theta`, not a replacement field. Define
\[
J[X]=\int\operatorname{vol}_E,\qquad
\operatorname{vol}_E=\frac1{4!}\epsilon_{abcd}
E^a\wedge E^b\wedge E^c\wedge E^d,\qquad \epsilon_{0123}=1.
\]
Then the Euler four-form and its complete linearization are
\[
\boxed{\delta J[v]=\int v^a\mathcal A_a,\qquad
\mathcal A_a=-\frac1{2c_0^2}\epsilon_{abcd}
(F^b{}_eX^e)\wedge E^c\wedge E^d,}
\]
\[
\boxed{(\mathcal L v)_a=
-\frac1{2c_0^2}\epsilon_{abcd}(F^b{}_ev^e)\wedge E^c\wedge E^d
-\frac1{c_0^3}\epsilon_{abcd}(F^b{}_eX^e)\wedge Dv^c\wedge E^d.}
\]
In particular,
\[
\delta^2J[u,v]=\int u^a(\mathcal L v)_a
=\delta^2J[v,u].
\]

**Proof.** The determinant variation gives
\[
\delta J[v]=\frac1{6c_0}\int\epsilon_{abcd}
Dv^a\wedge E^b\wedge E^c\wedge E^d.
\]
Since \(D\epsilon=0\), the exterior derivative of
\(\epsilon_{abcd}v^a E^b\wedge E^c\wedge E^d\) is the displayed
integrand without its prefactor plus
\(3\epsilon_{abcd}v^a DE^b\wedge E^c\wedge E^d\).
Its integral vanishes by compact support. Substitution of
\(DE=c_0^{-1}FX\) proves the first formula. Differentiate that formula with
\(C,F\) fixed, using \(\delta E=c_0^{-1}Dv\). The two tetrad variations
are equal after relabeling the antisymmetric indices, giving the displayed
\(\mathcal L\). Equality of mixed variations of the smooth determinant
functional proves formal symmetry; no field equation was assumed.

For \(F=0\), both Euler form and linearization vanish: the local Piola
null-Lagrangian result. For curved fixed \(C\), the Euler form can be nonzero,
but its linearization has order at most one. It is therefore not the
second-order scalar Laplace operator assumed in the preceding coefficient
calculation. This is a result about this Lorentz-real restricted action,
not a classification of all eight real biquaternionic fluctuation directions.

<!-- BILINGUAL-UNIT: biquat-induced.value-connection -->
## Including all variations of a value-dependent connection

**Lemma B-VAL [L1].** Let \(C_\mu=C_\mu(x,X)\) be any prescribed smooth
Lorentz connection functional depending on the field values, with no
derivatives of \(X\). Include its induced variation. For any smooth scalar
\(f(x,X)\), consider
\[
S_f[X]=\int d^4x\,f(x,X)\det E,\qquad
p_\mu^a:=\partial_\mu X^a,\qquad
E_\mu^a=c_0^{-1}[p_\mu^a+C_\mu{}^a{}_b(x,X)X^b].
\]
Use the same patch and compact-support assumptions as B-VAR. Then the full
Euler equation and its linearization have order at most one.

**Proof.** Holding \(x,X\) fixed when differentiating the first-jet density,
\[
\frac{\partial E_\rho^c}{\partial p_\mu^a}
=c_0^{-1}\delta_\rho^\mu\delta_a^c,\qquad
W_{ab}^{\mu\nu}:=
\frac{\partial^2(f\det E)}{\partial p_\mu^a\partial p_\nu^b}
=\frac{f}{2c_0^2}\epsilon^{\mu\nu\rho\sigma}
\epsilon_{abcd}E_\rho^cE_\sigma^d.
\]
The upper epsilon is the coordinate permutation symbol, not a metric-raised
Lorentz tensor. Hence
\[
W_{ab}^{\mu\nu}=-W_{ab}^{\nu\mu},\qquad
W_{ab}^{\mu\nu}k_\mu k_\nu=0.
\]
The only second derivatives in
\(\partial L/\partial X^a-\partial_\mu(\partial L/\partial p_\mu^a)\)
have coefficient \(-W_{ab}^{\mu\nu}\); commuting coordinate derivatives
cancel them. All derivatives of \(C(x,X)\) and \(f(x,X)\) are included in
the remaining zeroth- and first-order terms. Linearizing that expression
cannot reintroduce second derivatives.

This includes an algebraic potential multiplied by the same volume density.
It closes the value-only connection loophole for this family. It does not
justify using the fixed-\(C\) Euler formula when \(C\) varies.

<!-- BILINGUAL-UNIT: biquat-induced.jet-connection -->
## Exact remaining chain rule for derivative dependence

For a specified smooth local first-jet tetrad functional
\(E_\alpha=E_\alpha(x,X,p)\), let \(\alpha\) label a tetrad component and
\(I,J\) first-jet components. Define
\[
Q_\alpha=\frac{\partial\det E}{\partial E_\alpha},\quad
H_{\alpha\beta}=\frac{\partial^2\det E}
{\partial E_\alpha\partial E_\beta},\quad
J_{\alpha I}=\frac{\partial E_\alpha}{\partial p_I}.
\]
The full first-jet Hessian is exactly
\[
\boxed{W_{IJ}=f\left(
J_{\alpha I}H_{\alpha\beta}J_{\beta J}
+Q_\alpha\frac{\partial^2E_\alpha}{\partial p_I\partial p_J}
\right).}
\]
This is the twice-applied chain rule, including the second derivative of
the composite tetrad. It can change the cancellation above; it does not
guarantee a nonzero or elliptic principal symbol. If the connection depends
implicitly on \(E,\partial E\), first establish a differentiable solution map;
the first-jet formula alone does not cover that differential problem.
Computing the operator for the actual selected action and connection remains
`GAP-10D-HESS-COMP`.

<!-- BILINGUAL-UNIT: biquat-induced.renormalization -->
## Bare term, regulator and the simultaneous vacuum term

Allowing a bare Einstein term gives, within the same local prescription,
\[
\boxed{\frac1{G_{\rm ren}}=\frac1{G_{\rm bare}}
+\frac1{12\pi}\sum_j(1-6\xi_j)\mathcal I_1(M_{\rm UV},R_\psi,m_j)
+\kappa_{\rm other,ct}.}
\]
Here \(\kappa_{\rm other,ct}\) contains other sectors and counterterms.
Pure Sakharov induction therefore requires a reason for
\(G_{\rm bare}^{-1}=0\), together with a renormalization condition.
A prediction also needs a derived UV scale or a UV completion controlling
regulator dependence. Setting the cutoff equal to a measured Planck scale
would make a purported prediction of `G` circular.

The same heat expansion produces a volume term and higher curvature terms.
At fixed \(M_{\rm UV}R_\psi\) and fixed mass-to-cutoff ratios, the leading
volume coefficient scales as \(M_{\rm UV}^4\). If \(R_\psi\) is fixed instead
and \(M_{\rm UV}R_\psi\gg1\), the tower changes the leading scaling to
\(R_\psi M_{\rm UV}^5\). Its renormalization or cancellation is part of the
same calculation.

For the induced-gravity proposal see
[Sakharov](https://www.mathnet.ru/eng/dan33444). The proper-time prescription
and local heat coefficients used here are given in equations (1.20) and
(4.26)–(4.27) of
[Vassilevich](https://arxiv.org/abs/hep-th/0306138).

<!-- BILINGUAL-UNIT: biquat-induced.program -->
## Correct biquaternionic programme for route B

The shortest direct route is now:

1. finalize one microscopic action of the original `Theta` whose tetrad is
   \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\);
2. compute its complete second variation, including
   \(\delta E,\delta g,\delta\Omega\) and every constraint;
3. determine the gauge-fixed physical/ghost operator and a valid Euclidean
   contour, rather than setting the mode count equal to 8 by inspection;
4. evaluate the full heat supertrace and prove that its Einstein coefficient
   is nonzero with the physical sign;
5. derive \(M_{\rm UV}\) from the UBT scale data and state the renormalization
   condition, while treating the simultaneous volume term;
6. only then compare the resulting dimensionless ratio
   \(G\sqrt{\mathcal N_0}\) with experiment.

No Clifford spinor carrier or auxiliary geometric sector is needed for these steps.
The current blocker precedes the long numerical sum: the complete
biquaternionic composite Hessian is not yet fixed.

<!-- BILINGUAL-UNIT: biquat-induced.verification -->
## Verification

`tools/verify_biquaternionic_induced_gravity_boundary.py` checks:

- the exact signatures \((2,6)\) and \((1,3)\);
- all \(4^4\) determinant-Hessian components and the vanishing second-order
  symbol;
- the covariant Euler and Jacobi formulas against a separately differentiated
  coordinate determinant on a nonflat Lorentz-connection example;
- the value-dependent connection cancellation with an algebraic prefactor;
- both terms of the composite first-jet chain rule on a nonlinear example;
- \(C_\psi\) by quadrature and the independently truncated positive series,
  its tail bound, the two conditional Planck ratios, and \(\xi=1/6\).

The analytic proofs establish the general statements from their displayed
assumptions. The examples and numerical calculations check conventions and
implementation; they do not replace those proofs. The companion record is
`reports/biquaternionic_induced_gravity_boundary_2026_09_08.json` and records
the actual verification date, versions, hashes and limits. The regression
gate exercises these scientific identities.

Formalization is `LEAN-PENDING`: Lean and Lake are absent in the inspected
runtime, and no compiled Lean proof is supplied. The full quantum Hessian,
physical measure, and semantic equivalence of the translation still require
their respective verification.

<!-- BILINGUAL-UNIT: biquat-induced.status -->
## Status

- B-VAR, B-VAL: `CLOSED [L1]` for the displayed restricted action families.
- Derivative-dependent chain rule: `CLOSED [L1]` as an identity for a specified
  local first-jet map; no ellipticity result follows.
- Biquaternionic induced-gravity programme: `OPEN`.
- `GAP-10D-HESS-COMP`, physical modes/contour, nonzero Einstein coefficient,
  UV scale and renormalization: `OPEN`.
- Full UBT derivation and RH: `OPEN`. No canonical claim status is promoted.
