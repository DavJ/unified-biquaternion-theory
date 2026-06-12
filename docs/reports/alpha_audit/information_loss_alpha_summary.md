<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Layer2 projection correction to alpha information-loss route

**Status:** research-track hypothesis, not canonical.

This patch updates the alpha information-loss route by tying the finite
correction to the Layer2 observable-sector coding/projection layer.

## Core equation

The effective quasi-periodic theta modulus is

\[
\rho = \exp(-\Delta I_Q),
\qquad
\Delta I_Q(n)=\frac{C_Q(n)}{2\pi n}.
\]

The eta-winding coefficient is

\[
B(\rho)=12^{3/2}(2\eta(i\rho))^{1/4}.
\]

The stationary winding equation is

\[
\frac{2n}{\ln n+1}=B(\rho).
\]

## Layer1 eta-spectral subtraction

\[
\varepsilon_\eta
=
12\pi
\sum_{m=1}^{\infty}
\frac{m}{e^{2\pi m}-1}
=
\frac{\pi-3}{2}.
\]

## Layer2 projection-rank factor

Layer2 supplies a protected three-dimensional SU(3)/color-code subspace.
In a finite winding sector of effective dimension \(n\), the eta-loss acts on
the complement, giving

\[
\frac{n-3}{n}.
\]

Thus

\[
C_Q(n)
=
4-\frac{\pi-3}{2}\frac{n-3}{n}.
\]

## Result

\[
\frac{2n}{\ln n+1}
=
12^{3/2}
\left[
2\eta\left(
i\exp\left[
-\frac{1}{2\pi n}
\left(
4-\frac{\pi-3}{2}\frac{n-3}{n}
\right)
\right]
\right)
\right]^{1/4}.
\]

Numerically:

\[
n_{\rm UBT}=137.035999142931\ldots .
\]

Compared with CODATA/NIST 2022,

\[
\alpha^{-1}=137.035999177(21),
\]

this is approximately \(-1.62\sigma\).

## Open gap

\[
G137\text{-L2}:
\quad
\text{derive the projection-rank factor }
\frac{n-3}{n}
\text{ from canonical Layer2 UBT.}
\]

Until this is done, the result remains a systematic research-track derivation
with one Layer2 projection theorem remaining.
