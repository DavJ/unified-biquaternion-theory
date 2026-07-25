#!/usr/bin/env python3
"""Verification for the non-canonical GEM compact-mode research track.

The script checks:
  1. averaged (+n,-n) compact current and gradient energy;
  2. balanced-pair zero-current / positive-pressure identity;
  3. pure infinitesimal Lorentz rotations leave the metric unchanged;
  4. the standard Gödel coframe has nonzero g_ty and d(theta^0).

No UBT dynamical closure or enhanced gravity claim is tested.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import json
import math
from typing import Sequence


@dataclass(frozen=True)
class ModeAverages:
    current_psi: float
    flux_t_psi: float
    compact_gradient: float
    time_gradient: float


def mode_averages(
    weight_plus: float,
    weight_minus: float,
    omega: float,
    k: float,
) -> ModeAverages:
    """Return circle-averaged quadratic quantities for a (+k,-k) pair.

    The weights include the squared amplitudes and internal polarization norms.
    The flux sign follows T_{t psi}=Re[(partial_t Theta)^* partial_psi Theta]
    for the exp(-i omega t) convention.
    """
    if weight_plus < 0 or weight_minus < 0:
        raise ValueError("mode weights must be non-negative")
    current = k * (weight_plus - weight_minus)
    flux = -omega * current
    compact_gradient = k * k * (weight_plus + weight_minus)
    time_gradient = omega * omega * (weight_plus + weight_minus)
    return ModeAverages(current, flux, compact_gradient, time_gradient)


def matmul(a: Sequence[Sequence[Fraction]], b: Sequence[Sequence[Fraction]]):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: Sequence[Sequence[Fraction]]):
    return [list(row) for row in zip(*a)]


def add(a: Sequence[Sequence[Fraction]], b: Sequence[Sequence[Fraction]]):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def lorentz_rotation_metric_variation():
    """Exact first-order metric variation for a nontrivial tetrad and generator."""
    eta = [
        [Fraction(-1), 0, 0, 0],
        [0, Fraction(1), 0, 0],
        [0, 0, Fraction(1), 0],
        [0, 0, 0, Fraction(1)],
    ]
    # e_mu^a: invertible but non-diagonal, to avoid testing only the identity frame.
    e = [
        [Fraction(2), Fraction(1), 0, 0],
        [0, Fraction(1), Fraction(1, 3), 0],
        [0, 0, Fraction(3, 2), Fraction(1, 5)],
        [0, 0, 0, Fraction(4, 3)],
    ]
    # Lorentz-algebra generator lambda^a_b.  Lowered lambda_ab=eta_ac lambda^c_b
    # is antisymmetric: one boost (01) and one spatial rotation (23).
    lam = [
        [0, Fraction(2), 0, 0],
        [Fraction(2), 0, 0, 0],
        [0, 0, 0, Fraction(3)],
        [0, 0, Fraction(-3), 0],
    ]
    delta_e = matmul(e, transpose(lam))
    # g=e eta e^T, so delta g=delta_e eta e^T + e eta delta_e^T.
    delta_g = add(
        matmul(matmul(delta_e, eta), transpose(e)),
        matmul(matmul(e, eta), transpose(delta_e)),
    )
    return delta_g


def godel_kinematics(a: float, x: float) -> dict[str, float]:
    if a <= 0:
        raise ValueError("a must be positive")
    ex = math.exp(x)
    g_ty = -(a * a) * ex
    g_yy = -0.5 * (a * a) * ex * ex
    dtheta0_xy = a * ex
    determinant = -0.5 * (a ** 8) * ex * ex
    return {
        "g_ty": g_ty,
        "g_yy": g_yy,
        "dtheta0_xy": dtheta0_xy,
        "determinant": determinant,
    }


def run_checks() -> dict[str, object]:
    unbalanced = mode_averages(3.0, 1.0, omega=5.0, k=2.0)
    balanced = mode_averages(2.5, 2.5, omega=5.0, k=2.0)

    assert unbalanced.current_psi == 4.0
    assert unbalanced.flux_t_psi == -20.0
    assert balanced.current_psi == 0.0
    assert balanced.flux_t_psi == 0.0
    assert balanced.compact_gradient == 20.0
    assert balanced.time_gradient == 125.0

    delta_g = lorentz_rotation_metric_variation()
    assert all(value == 0 for row in delta_g for value in row)

    godel = godel_kinematics(a=2.0, x=0.3)
    assert godel["g_ty"] != 0.0
    assert godel["dtheta0_xy"] != 0.0
    assert godel["determinant"] < 0.0

    return {
        "track": "GEM compact modes",
        "status": "PASS",
        "unbalanced": asdict(unbalanced),
        "balanced": asdict(balanced),
        "lorentz_delta_g": [[str(v) for v in row] for row in delta_g],
        "godel_kinematics": godel,
        "not_tested": [
            "nonzero balanced bivector/spin observable",
            "canonical action coupling",
            "nonzero metric response",
            "enhancement beyond standard stress-energy",
            "Gödel-type UBT solution or CTCs",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify GEM compact-mode kinematics and no-go identities."
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    result = run_checks()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("PASS: balanced (+n,-n) pair has zero compact current and positive gradient energy")
        print("PASS: a common infinitesimal Lorentz rotation gives delta g = 0")
        print("PASS: Gödel coframe target has nonzero g_ty and d(theta^0)")
        print("NOT TESTED: action-derived source, metric response, enhancement, or CTCs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
