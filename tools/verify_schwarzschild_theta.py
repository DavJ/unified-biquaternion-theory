#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
verify_schwarzschild_theta.py — Legacy spatial-identity audit with a mandatory
canonical-boundary check.

PURPOSE
-------
This script verifies the limited algebraic fact that the legacy real-
quaternion ansatz

    Theta_0(r) = f(r) * 1 + g(r) * e_r

where
    g(r)  = r * (1 + M/(2r))^2                  [explicit solution]
    f'(r) = (1 + M/(2r)) * sqrt(2M/r)            [derived from ODE condition]

reproduces the positive-definite spatial isotropic Schwarzschild quadratic
form under the legacy scalar/Hermitian readout:

    g_ij(Theta_0) = Psi(r)^4 * delta_ij,   Psi(r) = 1 + M/(2r)

The computation uses the legacy quaternion-valued formula:

    g_munu = Sc( (d_mu Theta_0)^dagger * (d_nu Theta_0) )

where Sc extracts the scalar coefficient and dagger is quaternion conjugation.

This is NOT a verification of the active canonical UBT Schwarzschild claim.
At generic points the spatial derivatives have a nonzero real scalar
coefficient, whereas the canonical Lorentz slice requires the scalar
coefficient to be purely imaginary.  Moreover the static ansatz used here has
no time or psi dependence.  It therefore neither supplies the canonical
Lorentz tetrad nor the Schwarzschild lapse.

LIMITED RESULT
--------------
All spatial components g_ij = Psi^4 * delta_ij are verified exactly
(to floating-point precision) at every radius r > M/2.

CANONICAL VERDICT
-----------------
The full canonical claim remains GAP-U2Theta: OPEN.  Merely declaring complex
time does not turn a field with no psi dependence into one satisfying
partial_psi Theta = i Phi Theta.  The historical phase argument also omitted
the derivative of a radial phase.  See
``canonical/geometry/schwarzschild_claim_status.yaml`` and the paired GR-paper
correction for the exact boundary.

USAGE
-----
    python tools/verify_schwarzschild_theta.py [--mass M] [--r_values r1,r2,...]

HONEST ACCOUNTING
-----------------
  - Legacy spatial scalar identity: VERIFIED.
  - Membership of those derivatives in the canonical Lorentz slice: FAILS
    generically, as expected and explicitly checked here.
  - Temporal component and on-shell canonical selection: OPEN.

REFERENCES
----------
- research_tracks/research/schwarzschild_from_theta.tex (theory)
- canonical/gr_closure/step2_theta_only_closure.tex (metric formula)
- canonical/gr_closure/step3_signature_theorem.tex (Lorentzian signature)
"""

import argparse
import math
import numpy as np
from typing import List, Tuple


# ---------------------------------------------------------------------------
# 1. Quaternion algebra (real quaternions, represented as 4-vectors [a,b,c,d])
#    Convention: q = a*1 + b*i + c*j + d*k  (purely real quaternions)
# ---------------------------------------------------------------------------

def quat_product(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    """Product q1 * q2 of two real quaternions represented as [a,b,c,d]."""
    a1, b1, c1, d1 = q1
    a2, b2, c2, d2 = q2
    return np.array([
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2
    ])


def quat_conj(q: np.ndarray) -> np.ndarray:
    """Quaternion conjugate: [a,b,c,d] -> [a,-b,-c,-d]."""
    return np.array([q[0], -q[1], -q[2], -q[3]])


def Sc(q: np.ndarray) -> float:
    """Scalar part of quaternion: Sc([a,b,c,d]) = a."""
    return float(q[0])


def quat_metric_component(E_mu: np.ndarray, E_nu: np.ndarray) -> float:
    """
    Compute g_munu = Sc(E_mu^dagger * E_nu) = Sc(conj(E_mu) * E_nu).
    This is the legacy positive scalar readout for real-quaternion vectors.
    """
    return Sc(quat_product(quat_conj(E_mu), E_nu))


# ---------------------------------------------------------------------------
# 2. Schwarzschild metric (isotropic coordinates)
# ---------------------------------------------------------------------------

def Phi(r: float, M: float) -> float:
    """Temporal factor Phi(r) = (1 - M/2r) / (1 + M/2r)."""
    return (1.0 - M / (2.0 * r)) / (1.0 + M / (2.0 * r))


def Psi(r: float, M: float) -> float:
    """Spatial conformal factor Psi(r) = 1 + M/(2r)."""
    return 1.0 + M / (2.0 * r)


def schwarzschild_spatial(r: float, M: float) -> float:
    """Spatial metric component Psi(r)^4 (all three equal)."""
    return Psi(r, M) ** 4


# ---------------------------------------------------------------------------
# 3. Ansatz: Theta_0(r) = f(r)*1 + g(r)*e_r
#    Explicit solution: g(r) = r*Psi^2, f'(r) = Psi*sqrt(2M/r)
# ---------------------------------------------------------------------------

def g_func(r: float, M: float) -> float:
    """g(r) = r * Psi(r)^2 = r * (1 + M/(2r))^2."""
    return r * Psi(r, M) ** 2


def g_prime(r: float, M: float) -> float:
    """g'(r) = d/dr[r*(1+M/2r)^2] = (1+M/2r)(1-M/2r) = 1 - M^2/(4r^2)."""
    return 1.0 - M ** 2 / (4.0 * r ** 2)


def f_prime(r: float, M: float) -> float:
    """
    f'(r) from the isotropy ODE condition f'^2 + g'^2 = Psi^4:
        f'(r) = Psi(r) * sqrt(2M/r)

    Derivation: Psi^4 - g'^2 = Psi^4 - Psi^2*Phi^2 = Psi^2*(Psi^2 - Phi^2)
                             = Psi^2 * 2M/r   [since Psi^2-Phi^2 = 2*M/r]
    Hence f'(r) = sqrt(Psi^2 * 2M/r) = Psi * sqrt(2M/r).
    """
    if M <= 0:
        return 0.0
    return Psi(r, M) * math.sqrt(2.0 * M / r)


# ---------------------------------------------------------------------------
# 4. Spatial tetrad derivatives of Theta_0
# ---------------------------------------------------------------------------

def d_Theta_spatial(r: float, M: float,
                    x: float, y: float, z: float,
                    coord_idx: int) -> np.ndarray:
    """
    Compute partial_{x_i} Theta_0 for spatial coordinate i=1(x),2(y),3(z).

    Formula:
        d_i Theta_0 = (f'*x_i/r)*1 + (g'*x_i/r - g*x_i/r^2)*e_r + (g/r)*Q_i

    where Q_1=i, Q_2=j, Q_3=k are the quaternion imaginary basis elements.
    """
    xi = [x, y, z][coord_idx - 1]
    gv = g_func(r, M)
    gp = g_prime(r, M)
    fp = f_prime(r, M)

    # e_r as quaternion: [0, x/r, y/r, z/r]
    er = np.array([0.0, x / r, y / r, z / r])

    # Q_i (i-th quaternion imaginary basis element)
    Qi = np.zeros(4)
    Qi[coord_idx] = 1.0  # Q_1=[0,1,0,0], Q_2=[0,0,1,0], Q_3=[0,0,0,1]

    # d_i Theta_0
    one = np.array([1.0, 0.0, 0.0, 0.0])
    result = (fp * xi / r) * one
    result += ((gp * xi / r) - (gv * xi / r**2)) * er
    result += (gv / r) * Qi
    return result


# ---------------------------------------------------------------------------
# 5. Metric computation
# ---------------------------------------------------------------------------

def compute_spatial_metric(r: float, M: float,
                            x: float, y: float, z: float) -> np.ndarray:
    """
    Compute the 3x3 spatial metric g_ij at (x,y,z) from the UBT ansatz.
    Returns g[i][j] for i,j = 0,1,2 (corresponding to x,y,z).
    """
    g = np.zeros((3, 3))
    for i in range(1, 4):
        Ei = d_Theta_spatial(r, M, x, y, z, i)
        for j in range(1, 4):
            Ej = d_Theta_spatial(r, M, x, y, z, j)
            g[i - 1, j - 1] = quat_metric_component(Ei, Ej)
    return g


# ---------------------------------------------------------------------------
# 6. Verification
# ---------------------------------------------------------------------------

def verify_schwarzschild(M: float = 1.0,
                          r_values: List[float] = None,
                          tolerance: float = 1e-8) -> bool:
    """
    Verify that the UBT ansatz spatial metric equals Schwarzschild at each r.
    Tests at multiple spatial directions for each radius.
    Returns True if all components agree within tolerance.
    """
    if r_values is None:
        r_values = [2.0 * M, 5.0 * M, 10.0 * M, 50.0 * M, 100.0 * M]

    # Test directions: avoid z-axis degeneracy, use several points on sphere
    test_angles = [
        (0.0, 0.0),           # z-axis
        (math.pi / 2, 0.0),   # x-axis
        (math.pi / 4, math.pi / 4),  # diagonal
        (math.pi / 3, math.pi / 6),  # general
    ]

    print("=" * 70)
    print(f"Legacy Schwarzschild spatial-identity audit (M = {M})")
    print("=" * 70)
    print("Verifying: g_ij[Θ₀] = Psi(r)^4 * delta_ij")
    print("  where g(r) = r*Psi^2, f'(r) = Psi*sqrt(2M/r)")
    print()
    print(f"{'r/M':>6}  {'Psi^4':>10}  {'g_xx':>10}  {'g_yy':>10}  "
          f"{'g_zz':>10}  {'max|g_off|':>12}  {'Status':>8}")
    print("-" * 70)

    all_pass = True

    for r in r_values:
        if r <= M / 2.0:
            print(f"  r = {r:.3f}M: inside horizon — skipped")
            continue

        expected = schwarzschild_spatial(r, M)
        row_ok = True

        for theta, phi_angle in test_angles:
            # Convert spherical to Cartesian
            xp = r * math.sin(theta) * math.cos(phi_angle)
            yp = r * math.sin(theta) * math.sin(phi_angle)
            zp = r * math.cos(theta)
            # Avoid exact zero coordinates (causes division by zero in e_r)
            eps = 1e-10
            xp = xp if abs(xp) > eps else eps
            yp = yp if abs(yp) > eps else eps
            zp = zp if abs(zp) > eps else eps
            r_actual = math.sqrt(xp**2 + yp**2 + zp**2)

            g_spatial = compute_spatial_metric(r_actual, M, xp, yp, zp)
            g_xx = g_spatial[0, 0]
            g_yy = g_spatial[1, 1]
            g_zz = g_spatial[2, 2]
            g_off = max(abs(g_spatial[i, j]) for i in range(3)
                        for j in range(3) if i != j)

            err_xx = abs(g_xx - expected) / (abs(expected) + 1e-30)
            err_yy = abs(g_yy - expected) / (abs(expected) + 1e-30)
            err_zz = abs(g_zz - expected) / (abs(expected) + 1e-30)
            err_off = g_off / (abs(expected) + 1e-30)

            if max(err_xx, err_yy, err_zz, err_off) > tolerance:
                row_ok = False

        # Report for this radius (using last test direction for display)
        status = "OK" if row_ok else "FAIL"
        if not row_ok:
            all_pass = False
        print(f"  {r/M:>4.1f}  {expected:>10.6f}  {g_xx:>10.6f}  {g_yy:>10.6f}  "
              f"{g_zz:>10.6f}  {g_off:>12.2e}  {status:>8}")

    print()
    print("Canonical status:")
    print("  g_tt = 0 for static ansatz (d_t Theta_0 = 0).")
    print("  The spatial derivatives are generically outside the Lorentz slice W_L.")
    print("  Status: GAP-U2Theta OPEN; this is not a canonical Schwarzschild derivation.")
    print()
    print("=" * 70)
    if all_pass:
        print("LEGACY SPATIAL IDENTITY: [VERIFIED] — g_ij = Psi^4*delta_ij "
              "under the noncanonical real-quaternion readout.")
    else:
        print("SPATIAL METRIC RESULT: [DISCREPANCY] — See above for details.")
    print("=" * 70)
    return all_pass


def verify_canonical_boundary(M: float = 1.0) -> bool:
    """Confirm that the legacy ansatz does not satisfy the canonical claim.

    At the exact sample r=2M on the positive x-axis, the scalar coefficient of
    partial_x Theta is f'(2M)=5/4 for M>0.  A canonical Lorentz-slice element
    has scalar coefficient i e^0 with real e^0, so a nonzero real scalar
    coefficient is outside W_L.  The implemented ansatz is also independent
    of both t and psi, hence it cannot generate a nonzero lapse.
    """
    if M <= 0:
        raise ValueError("M must be positive for the Schwarzschild boundary audit")

    r = 2.0 * M
    spatial_derivative = d_Theta_spatial(r, M, r, 0.0, 0.0, 1)
    real_scalar_nonzero = abs(spatial_derivative[0] - 1.25) < 1e-12
    outside_lorentz_slice = abs(spatial_derivative[0]) > 1e-12
    temporal_derivative_zero = True  # Theta_0(r) in this script has no t or psi argument.
    detected = real_scalar_nonzero and outside_lorentz_slice and temporal_derivative_zero

    print()
    print("Canonical-boundary guard:")
    print(f"  scalar(partial_x Theta) at r=2M, x=r: {spatial_derivative[0]:.12g}")
    print("  required by W_L: purely imaginary scalar coefficient")
    print(f"  outside W_L detected: {'YES' if outside_lorentz_slice else 'NO'}")
    print(f"  missing t/psi dependence detected: {'YES' if temporal_derivative_zero else 'NO'}")
    print("  canonical full-Schwarzschild status: GAP-U2Theta OPEN")
    return detected


# ---------------------------------------------------------------------------
# 7. Analytical verification: f'^2 + g'^2 = Psi^4
# ---------------------------------------------------------------------------

def verify_ode_condition(M: float = 1.0,
                          r_values: List[float] = None) -> None:
    """Print verification of the ODE condition f'^2 + g'^2 = Psi^4."""
    if r_values is None:
        r_values = [2.0*M, 5.0*M, 10.0*M, 100.0*M]
    print()
    print("ODE condition: f'(r)^2 + g'(r)^2 = Psi(r)^4")
    print(f"  f'(r) = Psi(r)*sqrt(2M/r),  g'(r) = 1 - M^2/(4r^2)")
    print(f"{'r/M':>6}  {'f_prime':>10}  {'g_prime':>10}  "
          f"{'f^2+g^2':>12}  {'Psi^4':>12}  {'error':>10}")
    print("-" * 65)
    for r in r_values:
        fp = f_prime(r, M)
        gp = g_prime(r, M)
        lhs = fp**2 + gp**2
        rhs = schwarzschild_spatial(r, M)
        err = abs(lhs - rhs) / (rhs + 1e-30)
        print(f"  {r/M:>4.1f}  {fp:>10.6f}  {gp:>10.6f}  "
              f"{lhs:>12.6f}  {rhs:>12.6f}  {err:>10.2e}")


# ---------------------------------------------------------------------------
# 8. Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Audit a legacy spatial identity and its canonical boundary."
    )
    parser.add_argument("--mass", type=float, default=1.0,
                        help="Schwarzschild mass M (default: 1.0)")
    parser.add_argument("--r_values", type=str, default=None,
                        help="Comma-separated test radii in units of M "
                             "(default: 2,5,10,50,100)")
    parser.add_argument("--tolerance", type=float, default=1e-8,
                        help="Relative error tolerance (default: 1e-8)")
    args = parser.parse_args()

    M = args.mass
    r_vals = None
    if args.r_values:
        r_vals = [float(x) * M for x in args.r_values.split(",")]

    verify_ode_condition(M=M, r_values=r_vals)
    spatial_success = verify_schwarzschild(
        M=M, r_values=r_vals, tolerance=args.tolerance
    )
    boundary_success = verify_canonical_boundary(M=M)
    success = spatial_success and boundary_success
    raise SystemExit(0 if success else 1)
