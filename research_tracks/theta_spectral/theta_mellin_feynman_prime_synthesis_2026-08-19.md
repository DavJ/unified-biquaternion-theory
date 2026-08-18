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

# Theta ↔ Mellin/zeta ↔ Feynman ↔ prime structure: consolidated UBT working note

**Date:** 2026-08-19  
**Status:** working synthesis; not a canonical UBT result.  
**Purpose:** preserve the full reasoning thread, including classical mathematics, numerical observations, failed shortcuts, and UBT-specific questions.

## 1. Reference reduced kernel

The bridge object is

\[
S(t,\psi)=\sum_{n\ge1}a_n e^{-\pi\psi n^2}e^{i\pi t n^2}.
\]

Formal operator reading:

\[
H_0|n\rangle=\pi n^2|n\rangle,\qquad
U_0(t,\psi)=e^{-\psi H_0}e^{+itH_0}.
\]

This is a **reduced bridge model**. Canonical UBT uses the master field \(\Theta(q,\tau)\), \(\tau=t+i\psi\); the canonical GR paper explicitly does not assume that \(\Theta\) itself is a Jacobi theta function.

**Sign convention note.** An earlier RH scratch thread used the positive heat variable \(y=-\psi\), i.e. the theta parameter was written as \(t-i\psi=t+iy\). The formulas below use a directly positive damping coordinate \(\psi>0\). They are mapped into the earlier convention by \(y=-\psi\). This convention issue must be kept separate from any physical claim about the direction of UBT imaginary time.

## 2. Template non-orthogonality and the Gram kernel

With the normalized period-two inner product,

\[
G(\psi,\phi)=\langle S_\psi,S_\phi\rangle
=\sum_{n\ge1}|a_n|^2e^{-\pi(\psi+\phi)n^2}.
\]

For \(a_n=1\),

\[
G(\psi,\phi)=\frac{\vartheta_3(0|i(\psi+\phi))-1}{2}.
\]

Therefore the non-orthogonality kernel of a theta-template bank is itself a theta/heat kernel. This is classical mathematics applied to the reduced UBT bridge, not a novel UBT theorem.

For detection, use a matched filter

\[
\rho(\psi,\Delta)=
\frac{|\langle f,S_\psi(\cdot-\Delta)\rangle|^2}
{\|f\|^2\|S_\psi\|^2}.
\]

Orthogonality is unnecessary for selecting one best template. It matters for simultaneous decomposition, where the Gram matrix can be ill-conditioned and should be regularized.

## 3. Spectral triangle

For the same \(n^2\) spectrum:

- Fourier in real time \(t\): delta lines \(\omega=\pi n^2\).
- Laplace in \(\psi\): resolvent poles \(z=-\pi n^2\).
- Mellin in \(\psi\): \(\Gamma(s)\pi^{-s}n^{-2s}\).

For the unit-weight heat trace,

\[
\int_0^\infty u^{s-1}\sum_{n\ge1}e^{-\pi u n^2}\,du
=\Gamma(s)\pi^{-s}\zeta(2s).
\]

Mellin becomes ordinary Fourier after \(x=e^u\):

\[
M_f(\sigma+i\omega)
=\int_{-\infty}^{\infty}f(e^u)e^{\sigma u}e^{i\omega u}\,du.
\]

Thus \(\Im s\) is a frequency conjugate to logarithmic scale.

## 4. The important extension: ordinary zeta is the t=0 slice

In the working UBT coordinate convention used in this thread, the present slice is \(t=0\). Define

\[
Z_\Theta(s;t)=\sum_{n\ge1}\frac{e^{i\pi t n^2}}{n^{2s}}.
\]

Then

\[
\mathcal M_\psi[S](s;t)=\Gamma(s)\pi^{-s}Z_\Theta(s;t)
\]

for unit weights. In particular,

\[
Z_\Theta(s;0)=\zeta(2s).
\]

So the standard Riemann zeta is the untwisted/present member of a quadratic-phase family. This does **not** mean zeta itself intrinsically contains a physical present; the interpretation comes from the chosen UBT coordinate convention.

The family is periodic in \(t\) with period 2. At \(t=1\),

\[
Z_\Theta(s;1)=-\eta(2s)
=-(1-2^{1-2s})\zeta(2s).
\]

For rational \(t=a/q\), choose \(M=2q\). Since \(e^{i\pi a n^2/q}\) is periodic modulo \(M\),

\[
Z_\Theta(s;a/q)
=M^{-2s}\sum_{r=1}^{M}
 e^{i\pi a r^2/q}\zeta(2s,r/M).
\]

Hence the exponential time twist naturally produces finite linear combinations of Hurwitz zeta functions. The same rational quadratic phases are the phases appearing in quadratic Gauss sums and quantum revivals.

## 5. Theta ↔ Feynman in the controlled S1 example

For a free particle on a circle of circumference \(L\),

\[
K(x,x';T)=\frac1L\sum_{n\in\mathbb Z}
\exp\left[\frac{2\pi in(x-x')}{L}-\frac{iE_nT}{\hbar}\right],
\qquad
E_n=\frac{\hbar^2}{2m}\left(\frac{2\pi n}{L}\right)^2.
\]

Poisson summation yields the exactly equivalent winding representation

\[
K(x,x';T)=\sqrt{\frac{m}{2\pi i\hbar T}}
\sum_{w\in\mathbb Z}
\exp\left[\frac{im(x-x'+wL)^2}{2\hbar T}\right].
\]

Thus theta/momentum modes and Feynman winding histories are two representations of the same propagator in this controlled quadratic system.

Stationary action means \(\delta S=0\), not necessarily minimum action. Multiple stationary paths do not by themselves imply a multiverse.

## 6. Prime structure: what is exact and what is not

At \(t=0\),

\[
\zeta(2s)=\prod_p(1-p^{-2s})^{-1},\qquad \Re s>1/2.
\]

This is classical arithmetic. Mellin is invertible and does not create new information; the Euler product reflects the multiplicative structure of the positive integers. Therefore the chain theta → Mellin → Euler product does **not by itself** dynamically derive UBT prime sectors.

For general weights \(|a_n|^2\), the Dirichlet series \(\sum|a_n|^2n^{-2s}\) need not have an Euler product. Multiplicative coefficients are required.

### 6.1 Local Euler-factor poles

For a single local factor,

\[
(1-p^{-2s})^{-1},
\]

formal poles occur at

\[
s=i\pi k/\ln p.
\]

Nonzero pole lattices for distinct primes do not coincide: equality would imply \(p^\ell=q^k\). These are **local-factor poles outside the Euler-product convergence region**, not poles of the analytically continued global \(\zeta(2s)\).

Counting positive local-factor poles up to height \(T\) for primes \(p\le P\) gives

\[
N(T;P)=\sum_{p\le P}\left\lfloor\frac{T\ln p}{\pi}\right\rfloor
=\frac{T}{\pi}\vartheta(P)+O(\pi(P)),
\]

with Chebyshev \(\vartheta(P)=\sum_{p\le P}\ln p\). PNT gives \(\vartheta(P)\sim P\).

### 6.2 Vertical Fourier spectrum

At fixed \(\sigma>1/2\),

\[
\zeta(2(\sigma+i\omega))
=\sum_{n\ge1}n^{-2\sigma}e^{-i2\omega\ln n}.
\]

The Fourier lines are at \(2\ln n\). The logarithmic derivative isolates prime powers:

\[
-\frac{\zeta'(2s)}{\zeta(2s)}
=\sum_{p,k\ge1}(\ln p)p^{-2ks},
\]

so the prime-power frequency comb lies at

\[
\xi_{p,k}=2k\ln p.
\]

Distinct prime-power lines are nondegenerate except when the prime powers are identical.

The classical explicit formula makes the complementary statement: zeta zeros \(\rho=\beta+i\gamma\) generate oscillations \(e^{\beta u}e^{i\gamma u}\) in the logarithmic counting variable \(u=\ln x\).

## 7. Better dynamical prime lead: rational revivals

At rational times the quadratic theta phase is periodic and amplitudes are organized by Gauss sums

\[
g(a,q)=\sum_{r\bmod q}e^{2\pi i a r^2/q}.
\]

For the convention \(g(a,q)=\sum_{r=0}^{q-1}e^{2\pi i a r^2/q}\), the CRT identity is

\[
g(a,q_1q_2)=g(aq_2,q_1)g(aq_1,q_2),\qquad \gcd(q_1,q_2)=1.
\]

Thus prime powers are irreducible arithmetic building blocks of the revival structure. Unlike the bare Euler-product observation, this multiplicativity is carried by the quadratic theta dynamics itself.

**GAP-THETA-PRIME-2:** determine whether the existing UBT alpha prime-sector construction, when re-expressed in winding/revival variables, lands on rational denominators \(q\) and their Gauss-sum factorization.

## 8. Trace/orbit prime route

The existing `trace_formula_connections.tex` already records the classical analogy between primes and primitive orbit lengths \(\ln p\). For ordinary \(H_0\propto n^2\) on \(S^1\), the classical orbit lengths are not \(\ln p\).

**GAP-THETA-PRIME-1:** derive a genuine UBT operator/flow with primitive spectral or orbit data naturally equal to \(\ln p\), or do not claim a dynamical derivation of prime sectors from the Euler product.

## 9. The central physics gap

**GAP-THETA-PROP:** derive from the canonical UBT action/field equations an operator \(H_\Theta\) whose kernel or matrix element produces the reduced theta evolution. Until then, all exact theta/Feynman/zeta/Gauss relations are rigorous mathematics of a bridge model.

## 10. Relation to alpha

The existing alpha programme contains prime-stability sectors. This note does not upgrade them. It supplies two mechanisms to test:

1. primitive orbit / trace-formula route;
2. rational revival / Gauss-sum route.

Only if one of these reproduces the alpha-sector selection without post-selection should it be promoted into an alpha derivation.

## 11. Numerical status and reproducibility

`theta_zeta_probe.py` reproduces the standard identities used here. Current checks include:

- Mellin(theta) = \(\Gamma(s)\pi^{-s}\zeta(2s)\) at \(s=1,1.5,2\), agreeing to numerical precision;
- \(Z_\Theta(s;0)=\zeta(2s)\) and \(Z_\Theta(s;1)=-\eta(2s)\);
- rational-time Hurwitz-zeta decompositions for several \(a/q\);
- finite noncollision checks for the prime-power frequencies \(2k\ln p\), with the exact proof supplied by unique factorization;
- Gauss-sum CRT factorization for several coprime pairs;
- the 12-template Gram matrix on \(\psi\in[0.02,0.40]\), which is numerically nearly singular (condition scale about \(10^{17}\)); a ridge \(\lambda/\lambda_{\max}=10^{-8}\) reduces the condition scale to about \(10^8\);
- a deterministic noisy matched-filter demonstration recovering test values \(\psi_0=0.05,0.12,0.30\) to the grid scale.

These are verification tests of the bridge mathematics and estimation method, not tests of UBT physical truth. A future price-series experiment must establish the null distribution of the maximized score under phase-randomized or otherwise appropriate surrogates before interpreting any apparent predictive match.

## 12. Preservation rule for this thread

Classical mathematics belongs in the UBT student textbook when it is needed to understand the programme. It must be labelled as classical rather than omitted. Research notes should preserve successful identities, caveats, counterarguments, failed shortcuts, and open gaps, because the value of the programme is the synthesis and the explicit map from established mathematics to UBT-specific questions.
