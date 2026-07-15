# Covariant-tetrad connection and integrability closure — 16 July 2026

## Purpose

Continue the projection-free UBT GR reframe by resolving the kinematic status
of the frame connection, proving the explicit flat/special-relativistic
representer, and isolating the exact obstruction to a generic curved
single-field representation.

The canonical route remains

```text
Theta(q,tau)
  -> E_mu = N0^(-1/2) D_mu Theta
  -> 1/2(E_mu^sharp E_nu + E_nu^sharp E_mu) = g_munu 1.
```

No trace, real-part projection, phase projector, embedding map, preferred
imaginary-time section, or compact-fiber average defines the local metric.

## Closed results

### GAP-10Omega-KIN — CLOSED [L1]

For every nondegenerate tetrad and specified torsion, the metric-compatible
Lorentz-frame connection is unique:

```text
omega(e,T) = omega_LC(e) + K(T),
K_abc = 1/2 (T_cab - T_abc - T_bca)
```

for the convention `T^a = de^a + omega^a_b wedge e^b`.  Local Lorentz gauge
changes transform the tetrad and connection together; they do not represent
an additional physical connection degree of freedom.

### GAP-10Omega-GR — CLOSED [L1]

In the torsion-free branch, `T=K=0`, so the frame connection is uniquely the
Levi-Civita spin connection of the tetrad.  The relation to Christoffel symbols
is the tetrad-compatibility equation, not `Gamma=Re(Omega)`.

### GAP-10L-CONN — CLOSED [L1]

A metric-compatible Lorentz connection preserves `eta_ab` and the real
Lorentz slice under parallel transport.  Preservation by the complete field
dynamics and sources remains `GAP-10L-DYN`.

### GAP-10I-SR — CLOSED [L1]

Every constant Lorentz tetrad has an affine single-field representer.  In
Cartesian inertial Minkowski gauge,

```text
Theta_SR = Theta_0 + sqrt(N0) (i x^0 1 + x^k e_k),
Gamma = omega = Omega = 0,
D_mu = partial_mu.
```

It generates `diag(-1,1,1,1)` and has zero second spacetime derivatives.

### GAP-10I-1S — CLOSED AS NO-GO [L1, conditional]

Under the explicitly stated assumptions — one-sided regular action,
invertible `Theta`, torsion-free tetrad compatibility, and the same induced
connection —

```text
D^L_mu Theta = partial_mu Theta + A_mu Theta
```

implies `F^L_mu_nu Theta=0`, hence `F^L=0`.  This route cannot represent a
generic curved GR sector.

## Narrowed result

### GAP-10I-2S — NARROWED [L1]

The algebra-native two-sided derivative

```text
D_mu Theta = partial_mu Theta + A_mu Theta - Theta B_mu
```

obeys the exact identity

```text
[D_mu,D_nu]Theta = F^A_mu_nu Theta - Theta F^B_mu_nu.
```

For invertible `Theta`, torsion-free integrability becomes

```text
F^A_mu_nu = Theta F^B_mu_nu Theta^(-1).
```

Thus nonzero curved left/right connections are not algebraically forbidden.
This removes the one-sided flatness obstruction but does not prove curved
existence, uniqueness, regularity, or action-level selection.

## Remaining exact gaps

- `GAP-10T-DYN`: derive zero or spin-sourced torsion from the canonical action.
- `GAP-10I-CURVED`: solve the implicit nonlinear curved-space system for
  `(Theta,E,A,B)` locally and globally.
- `GAP-10L-DYN`: preserve the Lorentz slice under full dynamics and sources.
- `GAP-10D`: derive Einstein dynamics from the canonical UBT action/master
  equation.
- `GAP-10psi`: derive classical stability or imaginary-time independence.
- `GAP-B-MASTER`: derive the perturbation bridge from original canonical
  dynamics.
- `GAP-U2Theta`: select the full Schwarzschild tetrad and lapse on shell.

## Implicit and transcendental character

After kinematic connection reconstruction, the curved field equation is a
self-consistency system of the schematic form

```text
E_mu = N0^(-1/2)
       [partial_mu Theta + A_mu[E,T] Theta - Theta B_mu[E,T]].
```

It is an implicit nonlinear first-order PDE/fixed-point system.  If `Theta` is
restricted to a Jacobi-theta or another nonalgebraic function class, the
concrete system may additionally be transcendental.  These are distinct
mathematical properties and are stated separately in formal documents.

## Student and agent documentation

Student material now explains:

- ordinary versus covariant derivatives;
- `Gamma`, `omega`, and `Omega`;
- torsion and contorsion;
- the torsion-free and flat limits;
- the explicit Minkowski field;
- the one-sided no-go and two-sided route;
- implicit versus transcendental self-consistency;
- exact closed, narrowed, and open gaps.

`AGENTS.md`, GitHub Copilot instructions, Copilot review files, contribution
rules, and the PR template lock the canonical tetrad route and reject
projection/fiber regressions.

## Verification

Exact checkers:

```text
python tools/verify_covariant_tetrad_rank.py
python tools/verify_gap_10omega_connection.py
python tools/verify_gap_10i_integrability.py
```

Targeted regression suite includes claim/status consistency, metric lock,
symbol consistency, connection reconstruction, integrability selection, and
student/agent guardrails.

The checkers verify only the algebraic and differential identities encoded in
them.  They do not test torsion dynamics, curved-space existence, the UBT
action, Einstein dynamics, or global continuation.
