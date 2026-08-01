<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Layer2 kernel refinement to alpha information-loss route

**Status:** research-track hypothesis, not canonical.

This patch upgrades the alpha information-loss route from a sharp Layer2 rank
projection to a first eta-kernel readout refinement.

## Core equation

\[
\rho = \exp(-\Delta I_Q),
\qquad
\Delta I_Q(n)=\frac{C_Q(n)}{2\pi n}.
\]

\[
B(\rho)=12^{3/2}(2\eta(i\rho))^{1/4},
\qquad
\frac{2n}{\ln n+1}=B(\rho).
\]

## Eta spectral subtraction

\[
\Omega_\eta(1)
=
\sum_{m=1}^{\infty}\frac{m}{e^{2\pi m}-1}
=
\frac{1}{24}-\frac{1}{8\pi}.
\]

\[
\varepsilon_\eta
=
12\pi\Omega_\eta(1)
=
\frac{\pi-3}{2}.
\]

## Layer2 effective rank

General model:

\[
C_Q(n)
=
4-\varepsilon_\eta\frac{n-r_{\rm L2}}{n}.
\]

Sharp Layer2 projection:

\[
r_{\rm L2}^{(0)}=3.
\]

First eta-kernel refinement:

\[
r_{\rm L2}^{(1)}
=
3(1+\Omega_\eta(1)).
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
4-\frac{\pi-3}{2}\frac{n-r_{\rm L2}^{(1)}}{n}
\right)
\right]
\right)
\right]^{1/4}.
\]

Numerically:

\[
n_{\rm UBT}=137.035999177549\ldots .
\]

Compared with CODATA/NIST 2022,

\[
\alpha^{-1}=137.035999177(21),
\]

this is approximately \(+0.026\sigma\).

## Open gap

\[
G137\text{-L2K}:
\quad
\text{derive }
r_{\rm L2}=3(1+\Omega_\eta(1))
\text{ from the canonical Layer2 readout kernel.}
\]

Until this is done, the result remains a very strong research-track prediction,
not a canonical derivation of alpha.
