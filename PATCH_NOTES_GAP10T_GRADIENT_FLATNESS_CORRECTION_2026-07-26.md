# UBT differential correction — exact-gradient flatness no-go

**Patch date:** 2026-07-26  
**Base:** `unified-biquaternion-theory-master(24).zip`

## Audit verdict

The version-(24) affine-stationarity calculation is mathematically correct,
but its interpretation as the “surviving minimal composite branch” is not.
The branch used there replaces the canonical covariant jet

`E_mu = N0^(-1/2) D_mu Theta`

by the auxiliary exact-gradient restriction

`e^a = N0^(-1/2) dY^a`.

For nondegenerate Jacobian, `Y^a` are local coordinates and

`g = N0^(-1) Y^* eta`.

Therefore the Riemann tensor and Hilbert-Palatini density vanish identically
for every configuration in this restriction.  The locked kinetic and
cosmological terms reduce to a Jacobian null Lagrangian.  Affine stationarity
for all coefficients is consequently true, but it is a corollary of a
flatness no-go, not evidence for a curved dynamical branch.

## Correct status

- `GAP-10T-GRADIENT-FLATNESS: CLOSED AS NO-GO [L1]`.
- Gradient-affine stationarity: closed as an auxiliary corollary.
- `GAP-10T-DYN`: still narrowed; the canonical self-consistent
  `D`-composite variation and curved dynamics remain open.
- `GAP-10D`: still narrowed; the origin and coefficient of the curvature term
  remain open.

## Validation

- Generic determinant identity:
  `det(J^T eta J / N0) = -det(J)^2/N0^4`.
- Exact nonlinear coordinate pullback example: all Riemann components vanish.
- Existing affine first-variation verifier retained but relabelled as an
  auxiliary corollary check.
- Claim ledgers and GR submission synchronized to remove the overclaim.
