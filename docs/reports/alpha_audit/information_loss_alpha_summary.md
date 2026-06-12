<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Information-loss alpha self-consistency: summary

**Status:** research-track hypothesis, not canonical.

This patch adds a new T3_ALPHA paper:

- `research_tracks/T3_ALPHA/information_loss_alpha_self_consistency.tex`

and a reproduction script:

- `experiments/alpha_information_loss/reproduce_info_loss_alpha.py`

## Core equation

The effective quasi-periodic theta modulus is modeled as

\[
\rho = e^{-\Delta I_Q},
\qquad
\Delta I_Q(n)=\frac{C_Q}{2\pi n}.
\]

The eta-winding coefficient is

\[
B(\rho)=12^{3/2}\left(2\eta(i\rho)\right)^{1/4}.
\]

Together with the stationary winding condition

\[
\frac{2n}{\ln n+1}=B(\rho),
\]

this gives the closed self-consistency equation

\[
\frac{2n}{\ln n+1}
=
12^{3/2}
\left[
2\eta\left(i\exp\left[-\frac{C_Q}{2\pi n}\right]\right)
\right]^{1/4}.
\]

For the minimal four-channel ansatz \(C_Q=4\), this yields

\[
\alpha^{-1}_{\rm UBT,1loop}=137.0368227057.
\]

The observed Thomson-limit value \(\alpha^{-1}\approx137.035999084\) would
correspond to

\[
C_Q\approx3.9307485957,
\]

a \(1.73\%\) correction to the minimal four-channel estimate.

## Open gap

Derive \(C_Q\) from the UBT action, the biquaternionic transport operator, and
the observable projection map \(\Pi\). Until this is done, the result remains a
research-track self-consistency mechanism rather than a canonical derivation.
