# GR completion decision after the minimal one-connection no-go

## Decision

The current minimal interpretation is not retained as the exact-GR endpoint.
The same Lorentz connection cannot simultaneously:

1. sit inside `DTheta` and locally represent arbitrary tetrads through a
   composite contortion, and
2. be the torsion-free physical Levi-Civita connection of generic GR.

This is now an exact architecture-level no-go, not an open numerical question.

## Preferred exact-GR completion

Use two roles, not two freely propagating gauge fields:

- **physical connection**: `Omega_phys = Omega_LC(E)`, used for physical
  curvature and ordinary matter transport;
- **jet connection**: `Omega_hat = Omega_LC(E) + K_J[E,Theta]`, used only in
  `E_mu = N0^(-1/2) D_mu^{Omega_hat} Theta`.

`K_J` and the required relative central jet one-form now have an explicit
local covariant right-inverse formula for every non-null Lorentz-real `X`; see
`canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`. This closes
representability, but the formula uses the prescribed tetrad and therefore does
not dynamically select `E[Theta]` or follow from the canonical action.

## Alternative completion

Keep one connection and accept physical torsion. Then the endpoint is an
Einstein-Cartan/modified-gravity theory rather than exact ordinary GR. This
route needs a canonical torsion action, matter coupling, propagation analysis,
and observational bounds.

## Exact remaining proof obligations

1. **Jet dynamics lemma** — derive action-level selection of the explicit
   split-jet representative and of `E[Theta]`, and prove that its extra jet
   components do not propagate.
2. **Curvature-action lemma** — derive the Hilbert-Palatini term, sign, and
   Newton coefficient from canonical UBT. The locked quadratic kinetic term is
   only a volume term and cannot generate curvature dynamics.
3. **Constraint/degree-of-freedom audit** — prove that the jet completion adds
   no ghost or physical propagating mode.
4. **On-shell solution theorem** — prove that Schwarzschild/Kerr/FRW tetrads
   solve the final equations and that perturbations reduce to two graviton
   polarizations.

Only after all four items are proved may the repository say that GR is derived
unconditionally from UBT.
