<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# GAP-U2/GAP-B/GAP-10a derivation notes (restricted scope)

Date: 2026-07-14

## U2a — Equation for `A_psi`

From the existing action ingredients in repository files,

- `papers/UBT_GR_Submission.tex` (matter kinetic term in `S_Theta`),
- `canonical/interactions/sm_gauge.tex` (gauge kinetic term),

Euler–Lagrange variation with respect to `A_mu` gives

\[
\nabla_\nu F^{\nu\mu}=J^\mu.
\]

- This is **Outcome B** in the problem statement.
- The harmonic equation `Delta_g A_psi = 0` is recovered only after imposing the extra physical condition `J^psi=0`.

**Status:** PROVED (for Maxwell-type equation), CONDITIONAL (for harmonic reduction).

## U2b — Is `C=M` necessary?

From

\[
\partial_r\big(r^2\Psi^2 A_\psi'\big)=0,
\quad
A_\psi(r)=1-\frac{C}{r+M/2},
\]

`C` is an integration constant. Field equations alone do not force `C=M`.

`C=M` follows only if one imposes asymptotic physical matching to Schwarzschild lapse/ADM mass:

\[
A_\psi(r)=1-\frac{C}{r}+O(r^{-2}),\qquad
\Phi(r)=1-\frac{M}{r}+O(r^{-2}).
\]

Matching the `1/r` coefficient gives `C=M`.

**Status:** CONDITIONAL.

Missing physical condition if not imposed: asymptotic mass normalization (or equivalent boundary/charge condition fixing the integration constant).

## GAP-B (restricted odd-parity request)

Using

\[
g_{\mu\nu}[\Theta]=\frac{\langle\partial_\mu\Theta,\partial_\nu\Theta\rangle}{\mathcal N},
\quad
\Theta=\Theta_0+\varepsilon\,\delta\Theta,
\]

first variation is

\[
\delta g_{\mu\nu}=
\frac{\langle\partial_\mu\delta\Theta,\partial_\nu\Theta_0\rangle+\langle\partial_\mu\Theta_0,\partial_\nu\delta\Theta\rangle}{\mathcal N_0}
-\frac{g^{(0)}_{\mu\nu}}{\mathcal N_0}\,\delta\mathcal N,
\]

with

\[
\delta\mathcal N=\operatorname{sgn}\!\big(\langle\partial_0\Theta_0,\partial_0\Theta_0\rangle\big)
\left(\langle\partial_0\delta\Theta,\partial_0\Theta_0\rangle+\langle\partial_0\Theta_0,\partial_0\delta\Theta\rangle\right).
\]

For odd parity, this gives explicit metric perturbation components once a concrete odd-parity basis for `delta Theta` is fixed. The Regge–Wheeler equation still requires the unresolved map

\[
\delta(\nabla^\dagger\nabla\Theta)\to\delta G_{\mu\nu},
\]

so the bridge remains missing at that step.

**Status:** CONDITIONAL (explicit `delta g` formula derived; RW reduction still open at bridge map).

## GAP-10a (restricted Jacobian request)

Linearized Jacobian operator:

\[
(J_\Theta\cdot\delta\Theta)_{\mu\nu}=\delta g_{\mu\nu}
\]

with `delta g_{mu nu}` as above.

- **Kernel contains** at least:
  - constant shifts `delta Theta = const` (all derivatives vanish),
  - gauge-orbit tangents that leave all bilinear derivative pairings invariant at first order.
- **Gauge directions:** local right-phase variations and isotropy directions acting trivially on the bilinear pairings.
- **Rank/surjectivity:** no complete global rank proof provided here.

**Status:** OPEN (full rank/kernel classification not closed); PROVED (explicit operator formula).
