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
