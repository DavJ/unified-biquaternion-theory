# UBT Copilot Reference — Canonical Covariant-Tetrad Geometry

This reference supersedes older AI notes that treated projection/fiber metrics
or fitted constants as established results.


## Architecture-before-repair and v10.x freeze

Before adding fields, modes, dimensions, fibers, projections, averaging,
embeddings, or new axioms to resolve an obstruction, first test whether the
obstruction is an artefact of the formulation in which it was derived. A
correct rank theorem for an embedding variation is not automatically a no-go
for the covariant tetrad.

The covariant-tetrad architecture is frozen for v10.x. Copilot and other agents
must not replace the anticommutator metric, the tetrad
`E_mu=N0^(-1/2)D_mu Theta`, or the two-sided curved candidate without explicit
human approval and a written comparative audit. Open gaps must be attacked
inside the current framework first.

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
`GAP-10L-CONN`, `GAP-10I-SR`, `GAP-10I-1S` (no-go),
`GAP-10I-PAIR-KIN`, `GAP-10I-PAIR-GR` (torsion-free no-go), and
`GAP-10I-TORSION-LOCAL` (closed locally).  `GAP-10I-2S` is optional for local
kinematics and remains a possible torsion-free auxiliary route.

Conditional/closed subgaps: `GAP-10T-PALATINI`, `GAP-10L-SYM`, `GAP-10I-PRESCRIBED`, `GAP-10D-PALATINI/UNIQUENESS`, and `GAP-10psi-KIN/SYM`.
Narrowed full gaps: `GAP-10T-DYN`, `GAP-10L-DYN`, the dynamical/global part of `GAP-10I-CURVED`, `GAP-10D`, `GAP-10psi`. Open bridges: `GAP-B-MASTER`, `GAP-U2Theta`.

Alpha is not derived. Schwarzschild is not yet selected on shell by canonical
Theta dynamics. Fiber/projection GR routes are historical or exploratory.


## Conditional-subclosure guardrail

Never promote a Palatini or Lovelock branch to an unconditional UBT derivation.
`GAP-10T-PALATINI`, `GAP-10L-SYM`, `GAP-10D-PALATINI`,
`GAP-10D-UNIQUENESS`, and `GAP-10psi-SYM` are conditional theorems.
`GAP-10I-PRESCRIBED` closes only the system with prescribed coefficients.
`GAP-10I-TORSION-LOCAL` closes only local kinematic representability through a
composite contortion; it does not prove action selection, physical torsion
admissibility, or global continuation.  The full-theory gaps remain narrowed
until the canonical UBT action selects the required hypotheses and
self-consistent fields.
