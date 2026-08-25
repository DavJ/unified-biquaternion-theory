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

# Residues, the argument principle, and the Möbius route to RH

**Date:** 2026-08-25  
**Status:** working mathematical synthesis; no proof of the Riemann hypothesis and no upgrade of any UBT claim.  
**Scope:** classical analytic number theory plus an explicit interface to the current UBT theta–Mellin/RH working route.

<a id="scope-and-notation"></a>
## 0. Scope and notation

Write

\[
\zeta(s)=\sum_{n\ge 1}n^{-s}=\prod_p(1-p^{-s})^{-1},
\qquad \Re s>1,
\]

and let \(\mu\) be the Möbius function, \(\Lambda\) the von Mangoldt function, and

\[
M(x):=\sum_{n\le x}\mu(n)
\]

the Mertens summatory function. Unless analytic continuation is stated explicitly, series and Euler-product manipulations are made first in their half-plane of absolute convergence.

The four parts below separate established mathematics from the UBT-specific bridge. The conclusions are deliberately negative where a proposed shortcut is insufficient.

<a id="part-a"></a>
## A. Residues and holomorphicity

<a id="a1-local-data"></a>
### A.1 Local meromorphic data

The zeta function has a simple pole at \(s=1\) with residue \(1\). If \(\rho\) is a zero of multiplicity \(m_\rho\), then locally

\[
\zeta(s)=(s-\rho)^{m_\rho}g(s),\qquad g(\rho)\ne0.
\]

Consequently,

\[
\operatorname*{Res}_{s=\rho}\frac{\zeta'(s)}{\zeta(s)}=m_\rho,
\qquad
\operatorname*{Res}_{s=\rho}\left(-\frac{\zeta'(s)}{\zeta(s)}\right)=-m_\rho,
\]

whereas at the pole \(s=1\),

\[
\operatorname*{Res}_{s=1}\left(-\frac{\zeta'(s)}{\zeta(s)}\right)=1.
\]

Thus \(-\zeta'/\zeta\) records zeros with negative multiplicity and the pole of \(\zeta\) with positive multiplicity. The reciprocal \(1/\zeta\) has a zero at \(s=1\) and poles exactly at the zeros of \(\zeta\), with matching orders.

<a id="a2-rh-holomorphicity"></a>
### A.2 The zero-free formulation of RH

Using the functional equation and the known location of the trivial zeros, RH is equivalent to the statement that \(\zeta(s)\ne0\) for \(\Re s>1/2\). Equivalently,

\[
\boxed{\;1/\zeta\in\mathcal O\!\left(\{s\in\mathbb C:\Re s>1/2\}\right).\;}
\]

The point \(s=1\) causes no exception because \(1/\zeta\) has a zero there. This equivalence does not say that the Dirichlet series \(\sum\mu(n)n^{-s}\) already converges throughout that half-plane; extending that series requires estimates on its partial sums.

<a id="part-b"></a>
## B. Argument principle and winding number

<a id="b1-principle"></a>
### B.1 Exact counting statement

Let \(f\) be meromorphic inside and on a positively oriented contour \(C\), with no zeros or poles on \(C\). Then

\[
\frac{1}{2\pi i}\oint_C\frac{f'(s)}{f(s)}\,ds
=N_Z(C)-N_P(C),
\]

where zeros and poles are counted with multiplicity. The same integer is the winding number of the closed curve \(f(C)\) about the origin:

\[
\operatorname{wind}(f(C),0)=\frac{1}{2\pi}\Delta_C\arg f.
\]

For \(f=\zeta\), a contour enclosing \(s=1\) returns the number of enclosed zeta zeros minus one. For the completed entire xi function

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

the same integral counts nontrivial zeros without a pole subtraction.

<a id="b2-what-winding-cannot-do"></a>
### B.2 What winding does not prove

The argument principle counts zeros in a region; it does not, by itself, force them onto its symmetry axis. A contour split around the critical line can prove RH only if an additional estimate shows zero count zero in \(\Re s>1/2\), or if another theorem forces all counted zeros to lie on \(\Re s=1/2\). Functional-equation symmetry alone permits pairs \(\rho\) and \(1-\rho\) off the line.

Therefore a UBT winding or phase construction must supply a new analytic ingredient—such as positivity, monotonicity, a zero-free estimate, or a genuinely self-adjoint spectral identification—not merely reproduce the classical counting integral.

<a id="part-c"></a>
## C. Möbius/Mertens equivalence and the Dirichlet-algebra bridge

<a id="c1-dirichlet-series"></a>
### C.1 Reciprocal zeta and partial summation

Absolute convergence for \(\Re s>1\) gives

\[
\frac1{\zeta(s)}=\sum_{n\ge1}\frac{\mu(n)}{n^s}.
\]

Abel partial summation yields, initially for \(\Re s>1\),

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}
=s\int_1^\infty M(x)x^{-s-1}\,dx,
\]

provided the boundary term \(M(X)X^{-s}\) tends to zero. More precisely, at finite \(X\),

\[
\sum_{n\le X}\frac{\mu(n)}{n^s}
=M(X)X^{-s}+s\int_1^X M(x)x^{-s-1}\,dx.
\]

The classical Mertens formulation is

\[
\boxed{\;\mathrm{RH}\iff
(\forall\varepsilon>0)\quad
M(x)=O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).\;}
\]

The forward and reverse implications use analytic continuation and standard contour/Perron arguments; the displayed integral explains the exponent threshold but is not, alone, a complete proof of both directions.

<a id="c2-formal-dirichlet-algebra"></a>
### C.2 Formal operator notation

Introduce formal basis elements \(D_n\) with

\[
D_mD_n=D_{mn},\qquad D_1=1.
\]

Multiplication of coefficient series is then Dirichlet convolution. In the completed formal Dirichlet algebra, where every coefficient receives only finitely many divisor contributions, define

\[
\mathcal Z:=\sum_{n\ge1}D_n.
\]

Since \(1*\mu=\varepsilon\),

\[
\boxed{\;\mathcal Z^{-1}=\sum_{n\ge1}\mu(n)D_n.\;}
\]

Let the derivation \(\delta\) be defined by \(\delta D_n=(\log n)D_n\). Then

\[
\mathcal Z^{-1}\delta\mathcal Z
=\sum_{n\ge1}(\mu*\log)(n)D_n
=\sum_{n\ge1}\Lambda(n)D_n,
\]

because

\[
\boxed{\;\Lambda=\mu*\log.\;}
\]

Under the Mellin character \(D_n\mapsto n^{-s}\), valid analytically for \(\Re s>1\), these formal identities become

\[
\mathcal Z\mapsto\zeta(s),\qquad
\delta\mathcal Z\mapsto-\zeta'(s),\qquad
\mathcal Z^{-1}\delta\mathcal Z\mapsto-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s}.
\]

The inverse above is a formal Dirichlet-convolution inverse. It is not automatically an inverse of a bounded operator on a UBT Hilbert space. Any operator interpretation must separately specify the space, domain, closure, convergence, and spectrum.

<a id="part-d"></a>
## D. Relation to the current UBT RH/theta–Mellin route

<a id="d1-variable-map"></a>
### D.1 Exact variable map

The current reduced bridge uses

\[
S(t,\psi)=\sum_{n\ge1}a_ne^{-\pi\psi n^2}e^{i\pi t n^2}
\]

and, at \(t=0\) with unit weights,

\[
\int_0^\infty \psi^{w-1}S(0,\psi)\,d\psi
=\Gamma(w)\pi^{-w}\zeta(2w).
\]

Hence the classical zeta variable in Parts A–C is

\[
s=2w.
\]

The RH critical line \(\Re s=1/2\) therefore maps to \(\Re w=1/4\), not \(\Re w=1/2\). Likewise,

\[
-\frac{d}{dw}\log\zeta(2w)
=-2\frac{\zeta'(2w)}{\zeta(2w)}
=2\sum_{n\ge1}\frac{\Lambda(n)}{n^{2w}},
\qquad \Re w>1/2.
\]

If the prime-power series is written without the factor \(2\), the prime denotes differentiation with respect to the zeta argument \(s=2w\), not differentiation with respect to \(w\).

<a id="d2-admissible-bridge"></a>
### D.2 What would constitute a noncircular UBT bridge

The identities above suggest two precise, non-equivalent targets:

1. derive from canonical UBT dynamics an object whose Dirichlet coefficients are \(\mu(n)\), then prove the bound \(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\); or
2. derive an operator or determinant whose logarithmic derivative has \(\Lambda(n)\) coefficients and whose analyticity, positivity, or self-adjointness excludes zeros in \(\Re s>1/2\).

Defining the formal \(D_n\) algebra, inserting \(\mu\) or \(\Lambda\) by hand, or applying Mellin inversion to a known zeta identity is not a UBT derivation. The coefficients must arise from the canonical action, a proved theta/revival mechanism, or a derived trace/orbit structure without using zeta zeros as input.

<a id="d3-current-verdict"></a>
### D.3 Current verdict and open gap

The residue, winding, Möbius, Mertens, and logarithmic-derivative statements are established classical mathematics. They sharpen the target but do not close the current UBT gaps `GAP-THETA-PROP` and `GAP-THETA-PRIME-1`.

**GAP-RH-MOEBIUS-UBT:** derive, from the canonical UBT field equations or action, a non-post-selected mechanism producing the Möbius cancellation bound or an equivalent zero-free/spectral statement. Until this gap is closed, the route is a research programme, not a proof of RH.

<a id="verification"></a>
## Verification

| Claim / equation | Analytic status | Tool and artifact | Result and scope | Limitation | Lean status |
|---|---|---|---|---|---|
| \(\mathcal Z^{-1}=\sum\mu(n)D_n\) | classical exact identity | Python exact-integer checker, `tools/verify_residue_moebius_argument_principle.py` | verifies \(1*\mu=\varepsilon\) through a configurable finite cutoff | finite coefficient check is not a proof of the infinite formal-algebra statement | `LEAN-PENDING` — no repository formalization of the completed Dirichlet algebra |
| \(\Lambda=\mu*\log\) | classical exact identity | dependency-free Python checker, same artifact | verifies coefficients exactly as prime-exponent vectors through a configurable cutoff | a finite coefficient check is not an infinite proof | `LEAN-PENDING` — the exact arithmetic-function theorem is not yet formalized here |
| finite Abel-summation identity | classical exact identity | dependency-free Python complex-arithmetic checker, same artifact | compares both finite expressions at nonreal \(s\) | sampled numerical evaluation only | `LEAN-PENDING` — analytic formalization not present in the repository |
| residue/winding signs | classical complex analysis | dependency-free Hasse-series diagnostic, same artifact | checks small contours around \(s=1\) and the first nontrivial zero | uses finite-precision zeta evaluation and a known zero approximation | `LEAN-PENDING` — complex-analytic zeta formalization not present in the repository |

This note does not call any UBT-specific bridge verified. The checker tests only selected classical consequences encoded in it.

<a id="references"></a>
## References

1. T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.
2. E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford University Press, 1986.
3. `research_tracks/theta_spectral/theta_mellin_feynman_prime_synthesis_2026-08-19.md`.
4. `research_tracks/rh_trace_formula/README.md`.
