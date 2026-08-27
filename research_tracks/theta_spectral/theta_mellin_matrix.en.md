<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Joint Mellin analysis of the Jacobi theta sectors

**Date:** 2026-08-25  
**Status:** classical Mellin identities, a three-channel no-go result, and a rank-four characteristic extension modulo \(5\) established; a UBT-derived coupling remains open.

<a id="tmm-question"></a>
## 1. Question

Can the simultaneous Mellin transforms of all four Jacobi theta sectors impose a new condition on the nontrivial zeros of the Riemann zeta function beyond the functional equation?

The answer for the three nonzero theta constants is negative: their scalar Mellin channels contain only one zeta degree of freedom. This is useful because it identifies precisely where genuinely new input must enter.

<a id="tmm-definitions"></a>
## 2. Theta kernels

For \(t>0\), use

\[
\vartheta_2(it)=\sum_{n\in\mathbb Z}e^{-\pi(n+1/2)^2t},\qquad
\vartheta_3(it)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\qquad
\vartheta_4(it)=\sum_{n\in\mathbb Z}(-1)^n e^{-\pi n^2t}.
\]

Define convergent kernels

\[
K_2(t)=\frac{\vartheta_2(it)}2,\qquad
K_3(t)=\frac{\vartheta_3(it)-1}2,\qquad
K_4(t)=\frac{1-\vartheta_4(it)}2.
\]

The fourth theta constant satisfies 

\[
\vartheta_1(0,it)=0.
\]

Thus it supplies no scalar Mellin channel at \(z=0\). Its \(z\)-derivative is nonzero and belongs to the enlarged modular-form experiment, not to the three-channel theorem below.

<a id="tmm-transforms"></a>
## 3. Mellin transforms

Let

\[
A(s)=\pi^{-s/2}\Gamma\!\left(\frac s2\right).
\]

Termwise integration in the common half-plane 

\[
\Re s>1
\]

gives

\[
\mathcal M[K_3](s)=A(s)\zeta(s),
\]

\[
\mathcal M[K_4](s)=A(s)(1-2^{1-s})\zeta(s),
\]

\[
\mathcal M[K_2](s)=A(s)(2^s-1)\zeta(s).
\]

Equivalently,

\[
\mathbf M(s)
=A(s)\zeta(s)
\begin{pmatrix}
2^s-1\\[2pt]
1\\[2pt]
1-2^{1-s}
\end{pmatrix}.
\]

<a id="tmm-no-go"></a>
## 4. Theorem TMM-1: rank-one and zero-set result

**Theorem TMM-1 (standard consequences, proved here).** The joint scalar Mellin data of \(K_2,K_3,K_4\) have meromorphic rank one over the common factor \(A(s)\zeta(s)\). In the open critical strip

\[
0<\Re s<1,
\]

the three analytically continued channels vanish simultaneously exactly at the nontrivial zeros of 

\[
\zeta(s).
\]

**Proof.** The preceding factorization proves rank one. The gamma function has no zeros. The zeros of \(2^s-1\) lie on 

\[
\Re s=0,
\]

and the zeros of \(1-2^{1-s}\) lie on

\[
\Re s=1.
\]

Neither multiplier vanishes in the open strip. Hence none of the three channels adds an independent interior zero constraint. \(\square\)

This is a no-go result only for the three scalar theta constants. It does not exclude new information from derivatives, characteristics, products, higher-dimensional theta series, or a UBT-derived matrix kernel.

<a id="tmm-modular-matrix"></a>
## 5. Modular \(S\)-matrix

Under \(t\mapsto1/t\), the theta constants obey

\[
\begin{pmatrix}
\vartheta_2(i/t)\\
\vartheta_3(i/t)\\
\vartheta_4(i/t)
\end{pmatrix}
=\sqrt t\,
S
\begin{pmatrix}
\vartheta_2(it)\\
\vartheta_3(it)\\
\vartheta_4(it)
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix},
\qquad S^2=I.
\]

The eigenchannels are

\[
\vartheta_3,\qquad \vartheta_2+\vartheta_4,\qquad \vartheta_2-\vartheta_4,
\]

with eigenvalues \(+1,+1,-1\). This modular decomposition explains reflection symmetry, but rank one of the scalar Mellin data prevents it from locating all zeros on the symmetry axis.

<a id="tmm-new-information"></a>
## 6. Where new information could enter

| Extension | Mellin image | Possible new content | Required gate |
|---|---|---|---|
| characteristics \([a,b]\) | Hurwitz zeta and Dirichlet \(L(s,\chi)\) | several arithmetic channels | prove a UBT-selected coupling rather than insert characters |
| \(\partial_z\vartheta_1(0,it)\) and theta products | modular-form \(L\)-functions | non-scalar modular sectors | control Mellin convolution and distinguish it from zeta repackaging |
| higher-dimensional theta series | Epstein/automorphic zeta functions | lattice geometry | derive the quadratic form from UBT |
| UBT matrix kernel | determinant or operator-valued transform | positivity or self-adjointness constraint | derive the kernel and inner product from the canonical action |

The decisive target is not another functional equation. It is an independently derived positivity, total-positivity, or self-adjointness statement strong enough to force real spectral parameters.

<a id="tmm-verification"></a>
## 7. Verification and next experiment

The artifact `tools/verify_theta_mellin_matrix.py` checks the multiplier zero lines, the exact \(S\)-matrix involution and eigenchannels, and independent numerical evaluations of the three Mellin Dirichlet series for real \(s>1\). Regression coverage is in `tests/test_theta_mellin_matrix.py`.

| Claim | Status |
|---|---|
| three Mellin identities | **[STD/PROVED]** |
| TMM-1 rank-one/no-new-interior-zero result | **[PROVED]** |
| modular \(S\)-matrix eigendecomposition | **[STD/PROVED]** |
| UBT selection of an enlarged theta kernel | **[OPEN]** |
| positivity or self-adjointness forcing RH | **[OPEN]** |
| Lean formalization | **LEAN-PENDING** |

<a id="tmm-characteristics"></a>
## 8. Characteristic extension modulo \(5\)

Let \(U_5=(\mathbb Z/5\mathbb Z)^\times\). Since \(2\) generates \(U_5\), write each unit as \(2^j\bmod5\) and define

\[
\chi_k(2^j)=e^{2\pi i k j/4},\qquad k=0,1,2,3.
\]

The character table is the four-point discrete Fourier matrix

\[
C_{kj}=\chi_k(2^j),
\qquad
CC^\dagger=4I,
\qquad
\operatorname{rank}C=4.
\]

The parity is

\[
\chi_k(-1)=(-1)^k.
\]

Set \(a_k=0\) for even \(k\) and \(a_k=1\) for odd \(k\), and define the character theta kernels

\[
\Theta_k(t)=
\sum_{n\in\mathbb Z}
\chi_k(n)n^{a_k}e^{-\pi n^2t/5}.
\]

For \(\Re s>1\), termwise integration gives

\[
\frac12\int_0^\infty
t^{(s+a_k)/2-1}\Theta_k(t)\,dt
=
\left(\frac5\pi\right)^{(s+a_k)/2}
\Gamma\!\left(\frac{s+a_k}{2}\right)L(s,\chi_k).
\]

Thus the characteristic extension has four independent coefficient channels. The principal channel satisfies

\[
L(s,\chi_0)=(1-5^{-s})\zeta(s),
\]

while \(\chi_1,\chi_2,\chi_3\) supply three nonprincipal Dirichlet \(L\)-functions.

**Result TMM-2.** Rational characteristics increase the finite character-channel rank from one to four. This is genuinely more arithmetic information, but it still imposes no new condition on the zeros of \(\zeta\) unless UBT derives a coupling, determinant, positivity form, or common spectral operator relating the four completed \(L\)-channels.

The next experiment must therefore derive, rather than choose, a matrix \(G_{\mathrm{UBT}}(s)\) acting on these channels and test whether

\[
\mathbf\Lambda(s)^\dagger G_{\mathrm{UBT}}(s)\mathbf\Lambda(s)
\]

has a canonical positivity or self-adjoint spectral representation.

<a id="tmm-ubt-metric"></a>
## 9. Symmetry-admissible coupling metrics

Write the four completed character channels as

\[
\mathbf\Lambda=(\Lambda_0,\Lambda_1,\Lambda_2,\Lambda_3)^T.
\]

Multiplication by the generator of \(U_5\) acts in the character basis through

\[
D=\operatorname{diag}(1,i,-1,-i).
\]

Complex conjugation exchanges \(\chi_1\leftrightarrow\chi_3\) and fixes \(\chi_0,\chi_2\). Let

\[
P=
\begin{pmatrix}
1&0&0&0\\
0&0&0&1\\
0&0&1&0\\
0&1&0&0
\end{pmatrix}.
\]

For a Hermitian coupling matrix \(G\), impose character-phase invariance and antiunitary conjugation compatibility,

\[
D^\dagger G D=G,
\qquad
P^\dagger G P=\overline G.
\]

**Theorem TMM-3.** These conditions are equivalent to

\[
G=\operatorname{diag}(g_0,g_1,g_2,g_1),
\qquad g_0,g_1,g_2\in\mathbb R.
\]

The form is positive definite exactly when

\[
g_0>0,\qquad g_1>0,\qquad g_2>0.
\]

Hence phase and conjugation symmetry leave three independent real weights and do not select a canonical metric.

If one additionally postulates cyclic channel symmetry

\[
X(\Lambda_0,\Lambda_1,\Lambda_2,\Lambda_3)^T
=(\Lambda_3,\Lambda_0,\Lambda_1,\Lambda_2)^T,
\qquad X^\dagger G X=G,
\]

then

\[
G=cI.
\]

This stronger conclusion is conditional because the repository does not derive the action of \(X\) on the Mellin-character channels from the canonical UBT field.

Even the maximally symmetric positive candidate gives only

\[
Q(s)=c\sum_{k=0}^3|\Lambda_k(s)|^2.
\]

Its positivity says that \(Q(s)=0\) only when all four channels vanish. RH concerns the zeros of the principal channel alone, so positivity of \(Q\) does not locate those zeros without an additional identity forcing simultaneous vanishing or a self-adjoint operator whose characteristic determinant is the principal completed zeta channel.

This limitation matches the repository action audit: the real biquaternionic pairing, sign and scale are not finalized; the positive Hermitian quantity \(\operatorname{Tr}(X^\dagger X)\) is not Lorentz invariant for a generic field under nonunitary boosts; and the canonical sesquilinear form needed for antiunitary time reversal remains open. Therefore TMM-3 is a classification of admissible candidates, not a UBT derivation.

| Gate | Status |
|---|---|
| phase-plus-conjugation classification | **[PROVED]** |
| scalar metric under additional cyclic symmetry | **[PROVED, CONDITIONAL ON \(X\)]** |
| derive the channel symmetries from canonical UBT | **[OPEN]** |
| reconcile positive channel metric with Lorentz-invariant field pairing | **[OPEN]** |
| obtain an RH-strength self-adjoint determinant | **[OPEN]** |

Repository grounding: `canonical/ACTION.en.md:50-98`, `canonical/symmetry/discrete_symmetries.tex:311-317`, and `canonical/symmetry/discrete_symmetries.tex:449-454`.

<a id="tmm-functional-equations"></a>
## 10. Gauss sums and the functional-equation no-go result

For the three nonprincipal characters \(\chi_k\), \(k=1,2,3\), set \(a_k=k\bmod2\) and

\[
\tau_k=\sum_{r=1}^{4}\chi_k(r)e^{2\pi i r/5},
\qquad
\varepsilon_k=\frac{\tau_k}{i^{a_k}\sqrt5}.
\]

All three characters are primitive. Their completed functions

\[
\Lambda_k(s)=
\left(\frac5\pi\right)^{(s+a_k)/2}
\Gamma\!\left(\frac{s+a_k}{2}\right)L(s,\chi_k)
\]

satisfy

\[
\Lambda_k(s)=\varepsilon_k\Lambda_{4-k}(1-s).
\]

Direct Gauss-sum evaluation gives

\[
|\tau_k|=\sqrt5,
\qquad
\varepsilon_2=1,
\qquad
\varepsilon_3=\overline{\varepsilon_1},
\qquad
\varepsilon_1\varepsilon_3=1.
\]

Thus, on \(\mathbf\Lambda_{\mathrm{prim}}=(\Lambda_1,\Lambda_2,\Lambda_3)^T\), the functional equation is

\[
\mathbf\Lambda_{\mathrm{prim}}(s)
=R\mathbf\Lambda_{\mathrm{prim}}(1-s),
\qquad
R=
\begin{pmatrix}
0&0&\varepsilon_1\\
0&1&0\\
\varepsilon_3&0&0
\end{pmatrix},
\qquad
R^\dagger R=R^2=I.
\]

The restriction of the TMM-3 metric to these channels is

\[
G_{\mathrm{prim}}=\operatorname{diag}(g_1,g_2,g_1).
\]

For every real \(g_1,g_2\), not only when they are equal,

\[
R^\dagger G_{\mathrm{prim}}R=G_{\mathrm{prim}}.
\]

The functional equation therefore adds no relation between the odd-character weight \(g_1\) and the quadratic-character weight \(g_2\).

The principal character is different. It is induced from the conductor-one trivial character and

\[
L(s,\chi_0)=(1-5^{-s})\zeta(s).
\]

If \(\Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\), its conductor-five normalization is

\[
\Lambda_0^{(5)}(s)
=\left(5^{s/2}-5^{-s/2}\right)\Lambda_\zeta(s).
\]

Since \(\Lambda_\zeta(s)=\Lambda_\zeta(1-s)\), one obtains the nonconstant multiplier

\[
\Lambda_0^{(5)}(s)
=\frac{5^{s/2}-5^{-s/2}}
{5^{(1-s)/2}-5^{-(1-s)/2}}
\Lambda_0^{(5)}(1-s).
\]

Consequently the four channels do not form a constant unitary \(4\times4\) functional-equation representation: the three primitive channels form a closed block, while the principal zeta channel remains separate.

**Theorem TMM-4.** The exact mod-5 Gauss sums and Dirichlet functional equations do not reduce the three-parameter metric family of TMM-3 and do not mix the principal zeta channel with the primitive channels. Hence they impose no additional condition on the nontrivial zeros of \(\zeta\).

This is a second no-go result, not a failure of the calculation. Any stronger coupling must come from an enlarged additive-residue theta representation, a UBT-derived operator, or another identity not contained in the separate Dirichlet functional equations.

| Gate | Status |
|---|---|
| primitive Gauss sums and root numbers | **[PROVED]** |
| unitary involution on the primitive block | **[PROVED]** |
| principal channel has a constant conductor-five root number | **[DISPROVED]** |
| functional equations force \(g_1=g_2\) | **[DISPROVED]** |
| UBT-derived mixing with the principal channel | **[OPEN]** |

<a id="tmm-additive-residues"></a>
## 11. Additive residue channels and the finite Weil representation

For \(r\in\mathbb Z/5\mathbb Z\), define

\[
\Theta_r(t)=
\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
e^{-\pi n^2t/5},
\qquad t>0.
\]

Poisson summation gives the vector transformation

\[
\mathbf\Theta(t)=t^{-1/2}\mathcal S\mathbf\Theta(1/t),
\qquad
\mathcal S_{rs}=\frac1{\sqrt5}e^{2\pi i rs/5}.
\]

For the holomorphic version, translation by two modular units acts through

\[
\Theta_r(\tau+2)=e^{2\pi i r^2/5}\Theta_r(\tau),
\qquad
\mathcal T=\operatorname{diag}
\left(e^{2\pi i r^2/5}\right)_{r=0}^{4}.
\]

Let \(\mathcal P\) reflect residues, \((\mathcal Pv)_r=v_{-r}\). Direct calculation yields

\[
\mathcal S^\dagger\mathcal S=I,
\qquad
\mathcal S^2=\mathcal P,
\qquad
\mathcal S^4=I,
\qquad
[\mathcal T,\mathcal P]=0.
\]

The full coefficient space decomposes into residue-parity sectors

\[
\mathbb C^5=V_+\oplus V_-,
\qquad
\dim V_+=3,
\qquad
\dim V_-=2,
\qquad
\Pi_\pm=\frac12(I\pm\mathcal P).
\]

Solving the complete commutant equations

\[
[G,\mathcal S]=[G,\mathcal T]=0
\]

gives

\[
G=a\Pi_+ + b\Pi_-.
\]

For Hermitian \(G\), the coefficients \(a,b\) are real, and positivity requires \(a,b>0\). Thus the full five-dimensional representation has two independent invariant weights.

However, the scalar theta constants satisfy

\[
\Theta_r(t)=\Theta_{-r}(t).
\]

They therefore occupy only

\[
V_+=\operatorname{span}
\left\{e_0,\frac{e_1+e_4}{\sqrt2},
\frac{e_2+e_3}{\sqrt2}\right\}.
\]

The restricted commutant of \(\mathcal S\) and \(\mathcal T\) on this three-dimensional sector has dimension one. Consequently its invariant Hermitian metric is

\[
G_+=aI_3.
\]

The two odd channels are absent at \(z=0\); they can be supplied by derivatives with respect to the elliptic variable, analogously to the missing scalar \(\vartheta_1\) channel.

The principal zeta function is now genuinely contained in the additive system because

\[
\frac12\sum_{r=0}^{4}
\left(\Theta_r(t)-\delta_{r0}\right)
=\sum_{n=1}^{\infty}e^{-\pi n^2t/5},
\]

and hence, for \(\Re s>1\),

\[
\frac12\int_0^\infty t^{s/2-1}
\sum_{r=0}^{4}\left(\Theta_r(t)-\delta_{r0}\right)dt
=\left(\frac5\pi\right)^{s/2}
\Gamma\!\left(\frac s2\right)\zeta(s).
\]

**Theorem TMM-5.** The additive residue representation does mix the zero residue class with the four nonzero classes. Modular invariance fixes the scalar even-sector metric uniquely up to an overall scale. Nevertheless, the zeta channel is a linear functional of the three theta components, whereas positivity of \(aI_3\) controls their simultaneous vanishing. It therefore does not imply that zeros of this linear functional lie on \(\Re s=1/2\).

This experiment supplies canonical modular mixing and a scalar metric on the realized sector, but not an RH-strength spectral operator. The remaining missing ingredient is a UBT-derived self-adjoint operator whose determinant or distinguished eigenchannel equals the completed zeta function.

| Gate | Status |
|---|---|
| five-residue Fourier transformation | **[PROVED]** |
| full commutant \(a\Pi_++b\Pi_-\) | **[PROVED]** |
| scalar metric on the realized even sector | **[PROVED]** |
| additive system contains the zeta Mellin channel | **[PROVED]** |
| positivity locates the zeros of that linear channel | **[DISPROVED]** |
| UBT-derived self-adjoint zeta operator | **[OPEN]** |

<a id="tmm-elliptic-derivatives"></a>
## 12. Elliptic derivatives and the odd sector

Introduce the elliptic residue kernels

\[
\Theta_r(z,\tau)=
\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
\exp\!\left(\frac{\pi i\tau n^2}{5}
+\frac{2\pi i n z}{5}\right)
\]

and their first derivatives at \(z=0\), normalized as

\[
\Phi_r(t)=
\frac5{2\pi i}
\left.\frac{\partial}{\partial z}\Theta_r(z,it)\right|_{z=0}
=\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
n e^{-\pi n^2t/5}.
\]

They have odd residue parity,

\[
\Phi_0(t)=0,
\qquad
\Phi_{-r}(t)=-\Phi_r(t),
\qquad
\sum_{r=0}^{4}\Phi_r(t)=0.
\]

Thus the derivative vector lies in

\[
V_-=\operatorname{span}
\left\{\frac{e_1-e_4}{\sqrt2},
\frac{e_2-e_3}{\sqrt2}\right\}.
\]

Differentiating the Poisson transformation, or transforming the weighted Gaussian directly, gives

\[
\mathbf\Phi(t)
=-i\,t^{-3/2}\mathcal S\mathbf\Phi(1/t).
\]

The power changes from \(t^{-1/2}\) to \(t^{-3/2}\): the derivative sector has modular weight higher by one. Translation by two still acts through \(\mathcal T\).

The restricted commutant on \(V_-\) has dimension one, so its invariant Hermitian metric is

\[
G_-=bI_2.
\]

The complete scalar-plus-derivative metric is consequently

\[
G=aI_3\oplus bI_2
=a\Pi_+ + b\Pi_-.
\]

One might hope that the derivative operation forces \(a=b\). It does not. Solving all constant intertwiner equations

\[
Q\mathcal S_+=(-i\mathcal S_-)Q,
\qquad
Q\mathcal T_+=\mathcal T_-Q,
\qquad
Q:V_+\longrightarrow V_-
\]

gives only

\[
Q=0.
\]

This is consistent with the unequal dimensions and modular weights of the two irreducible sectors. Differentiation relates the underlying functions but is not a constant endomorphism of the finite coefficient representation.

**Theorem TMM-6.** First elliptic derivatives realize the two missing odd residue channels and give them a scalar invariant metric. The combined Jacobi data retain two independent positive scales \(a,b\); modular covariance supplies no nonzero constant even-to-odd intertwiner and therefore does not enforce \(a=b\).

The even/odd split may be used as a carefully limited bosonic/fermionic analogy: scalar theta values are even and derivative channels are odd, with pairwise cancellation in the latter. It is not a derivation of physical particles, spin-statistics, or particle-antiparticle states. Such an interpretation would require a UBT-derived graded Hilbert space and a weight-changing Dirac or supercharge operator.

| Gate | Status |
|---|---|
| odd derivative kernels and their Poisson law | **[PROVED]** |
| scalar invariant metric \(bI_2\) | **[PROVED]** |
| nonzero constant modular intertwiner \(V_+\to V_-\) | **[DISPROVED]** |
| modular covariance forces \(a=b\) | **[DISPROVED]** |
| UBT-derived Dirac or supercharge coupling | **[OPEN]** |
| physical fermion interpretation | **[OPEN]** |

<a id="tmm-jacobi-dirac"></a>
## 13. Jacobi Dirac factorization and its spectral limit

Work on the Hilbert space of (5)-periodic functions of the elliptic variable,

\[
\mathcal H_z=L^2(\mathbb R/5\mathbb Z),
\qquad
\langle f,g\rangle_z=\frac15\int_0^5\overline{f(z)}g(z)\,dz,
\]

with dense domain (H^1(\mathbb R/5\mathbb Z)).  The normalized elliptic derivative

\[
\mathscr D_z:=\frac5{2\pi i}\frac{\partial}{\partial z}
\]

is self-adjoint on the periodic domain and obeys

\[
\mathscr D_z e^{2\pi i n z/5}=n e^{2\pi i n z/5}.
\]

Let ((\mathcal Pf)(z)=f(-z)).  Then

\[
\mathcal P\mathscr D_z\mathcal P=-\mathscr D_z.
\]

Thus (mathscr D_z) is an odd operator for the parity grading and exchanges the even and odd function spaces.  Applied to the residue theta kernels, it gives exactly the channels of TMM-6,

\[
\left.\mathscr D_z\Theta_r(z,it)\right|_{z=0}=\Phi_r(t).
\]

It also factors the free theta heat generator.  If

\[
H_0 e^{2\pi i n z/5}=\frac{\pi n^2}{5}e^{2\pi i n z/5},
\]

then

\[
\boxed{H_0=\frac\pi5\mathscr D_z^2},
\qquad
e^{-tH_0}e^{2\pi i n z/5}=e^{-\pi n^2t/5}e^{2\pi i n z/5}.
\]

Relative to (mathcal H_z=\mathcal H_+\oplus\mathcal H_-), the operator has Dirac form

\[
\mathscr D_z=
\begin{pmatrix}
0&\mathscr D_-\\
\mathscr D_+&0
\end{pmatrix},
\qquad
\mathscr D_- = \mathscr D_+^\dagger.
\]

This is a genuine weight-changing differential operator, not the constant intertwiner excluded by TMM-6.  However, it does not identify the two finite-sector metric scales.  For the graded metric (aI_3\oplus bI_2), the adjoint of a map (D:V_+\to V_-) is (D^{\dagger_{a,b}}=(b/a)D^\dagger); self-adjoint block completion is therefore possible for every (a,b>0).  Requiring the same unrescaled differential expression in both off-diagonal blocks would impose (a=b), but that is an additional normalization choice, not a consequence of modular covariance.

**Theorem TMM-7.** The Jacobi derivative gives a canonical parity-odd self-adjoint square root of the free theta Hamiltonian on the periodic elliptic Hilbert space.  Its spectrum is

\[
\operatorname{spec}(\mathscr D_z)=\mathbb Z,
\qquad
\operatorname{spec}(H_0)=\left\{\frac{\pi n^2}{5}:n\in\mathbb Z\right\}.
\]

Consequently this operator does not have the nontrivial zeta ordinates as eigenvalues, and its spectral determinant is not the completed zeta function.  The repository also does not derive an identification of the auxiliary Jacobi coordinate (z) with a canonical biquaternionic spacetime or complex-time direction.  Hence (mathscr D_z) closes the local graded-factorization problem but does not close the UBT or Hilbert--Pólya bridge.

| Gate | Status |
|---|---|
| self-adjoint elliptic derivative on the periodic domain | **[PROVED]** |
| parity-odd map and (H_0=(\pi/5)\mathscr D_z^2) | **[PROVED]** |
| same block normalization follows from modular symmetry | **[DISPROVED]** |
| spectrum equals the nontrivial zeta ordinates | **[DISPROVED]** |
| (z) identified with a canonical UBT direction | **[OPEN]** |
| Hilbert--Pólya operator derived from UBT | **[OPEN]** |

Verification: `tools/verify_theta_mellin_matrix.py` checks the Fourier eigenvalues, parity anticommutation, heat-generator factorization, and metric-adjoint scaling on finite invariant mode truncations; `tests/test_theta_mellin_matrix.py` provides the regression entry point.  These finite exact/numerical checks do not prove an unbounded-operator domain theorem or a UBT identification.  **LEAN-PENDING:** the theorem uses Fourier/Sobolev operator-domain facts not yet represented in the repository's Lean environment.
