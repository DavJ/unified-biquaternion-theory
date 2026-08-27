<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Patch notes: two-sided renormalized Euler product

**Date:** 2026-08-28
**Scope:** active RH research track; no canonical claim changes.

<a id="tre-patch-summary"></a>
## Summary

This patch follows the adelic valuation audit with a two-sided treatment of the infinite product of local geometric sums. It establishes the standard result that the raw Euler product is nonzero in its trace domain and that a finite Maclaurin subtraction gives

\[
R_M(s)=\prod_p\frac{1}{1-p^{-s}}
\exp\left(-\sum_{m=1}^{M}\frac{p^{-ms}}m\right),
\qquad
\Re s>\frac1{M+1},
\]

where \(R_M\) is holomorphic and nonvanishing.

<a id="tre-patch-two-charts"></a>
## Two charts

For \(M=1\), the completed function is represented on the two open sides by

\[
\xi(s)=C(s)R_1(s)e^{P(s)},
\qquad
\xi(s)=C(1-s)R_1(1-s)e^{P(1-s)}.
\]

The second expression explicitly covers \(\Re s<1/2\). The common boundary is approached by \(s_\pm=1/2\pm\varepsilon+it\), for which

\[
\xi(s_-)=\overline{\xi(s_+)}.
\]

<a id="tre-patch-operator"></a>
## Operator result

All prime-power layers with \(m\geq2\) give a norm-convergent translation operator for every \(\varepsilon>0\). The uncentered first layer satisfies

\[
\left\|\sum_{p\leq X}p^{-1/2-\varepsilon}U_{\log p}\right\|
=\sum_{p\leq X}p^{-1/2-\varepsilon}
\]

and therefore diverges in operator norm for \(0<\varepsilon\leq1/2\). The next valid step must renormalize this first layer canonically; merely introducing a nonlocal operator does not cross the convergence barrier.

<a id="tre-patch-claim-control"></a>
## Claim control

The centered Chebyshev representation shows that a square-root bound for \(\psi(x)-x\) would supply the needed right-half-strip control, but that bound is RH-strength. The patch does not derive such a bound, does not construct a Hilbert--Pólya operator, and does not derive prime translations or their centering from UBT.

<a id="tre-patch-verification"></a>
## Verification

- `tools/verify_two_sided_renormalized_euler.py` checks finite complex Maclaurin factorizations, convergence signatures on both sides of selected thresholds, the exact reflection normalization \(\xi(2)=\xi(-1)=\pi/6\), finite translation norm bounds, and the von Mangoldt/prime-power identity.
- `tests/test_two_sided_renormalized_euler.py` provides six regression tests.
- The verifier uses only Python 3.12 standard-library facilities.
- Lean is unavailable in the runtime; exact formalization remains `LEAN-PENDING`.
- English was the translation source. The paired Czech edition has matching anchors, equations, status labels, numbers, citations, and caveats; human semantic-equivalence review is required before merge.
