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
