# UBT Copilot Reference — Canonical Covariant-Tetrad Geometry

This reference supersedes older AI notes that treated projection/fiber metrics
or fitted constants as established results.

## Canonical geometry

\[
\Theta(q,\tau)\in\mathbb C\otimes\mathbb H,
\qquad \tau=t+i\psi,
\]
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,
\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g_{\mu\nu}\mathbf1.
\]

On the Lorentz slice
\[
E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k,
\]
this gives \(g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}\). No trace,
real-part projector, compact-fiber average, preferred section, or embedding map
belongs to the canonical metric definition.

## Coordinate and frame connections

`Gamma` acts on coordinate indices, `omega` on Lorentz-frame indices, and
`Omega=rho_*(omega)` in the chosen spin/biquaternionic representation. They
are related by tetrad compatibility, not by `Gamma=Re(Omega)`.

For specified tetrad and torsion,
\[
\omega=\mathring\omega(e)+K(T),
\qquad
K_{abc}=\tfrac12(T_{cab}-T_{abc}-T_{bca}).
\]
The torsion-free GR branch therefore has the unique Levi-Civita spin
connection. The full UBT action must still select torsion and the exact action
on \(\Theta\).

## Integrability selection

Every constant Lorentz tetrad has the affine representer
\[
\Theta_{\rm aff}=\Theta_0+\sqrt{\mathcal N_0}\,\bar E_\mu x^\mu.
\]
For \(\bar E_0=i\mathbf1\), \(\bar E_k=\mathbf e_k\), this explicitly gives
Minkowski spacetime with \(\Omega=0\) in inertial gauge.

A naive one-sided regular connection is a conditional no-go for generic
invertible torsion-free curved geometry. The active candidate is
\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu,
\]
\[
[D_\mu,D_\nu]\Theta=F^A_{\mu\nu}\Theta-\Theta F^B_{\mu\nu}.
\]
This narrows, but does not close, curved-space integrability.

## Status guardrails

Closed/narrowed: `GAP-10K`, `GAP-10Omega-KIN`, `GAP-10Omega-GR`,
`GAP-10L-CONN`, `GAP-10I-SR`, `GAP-10I-1S` (no-go), `GAP-10I-2S`
(narrowed).

Open: `GAP-10T-DYN`, `GAP-10L-DYN`, `GAP-10I-CURVED`, `GAP-10D`,
`GAP-10psi`, `GAP-B-MASTER`, `GAP-U2Theta`.

Alpha is not derived. Schwarzschild is not yet selected on shell by canonical
Theta dynamics. Fiber/projection GR routes are historical or exploratory.
