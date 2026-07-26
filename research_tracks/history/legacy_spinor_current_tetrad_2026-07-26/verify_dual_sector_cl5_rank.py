#!/usr/bin/env python3
"""Exact/algebraic verifier for the UBT dual-sector Clifford-5 research track.

This script proves only the explicitly stated algebraic and off-shell first-jet
claims. It does not impose the UBT equations of motion, complex-time
holomorphy, gauge constraints, or Einstein dynamics.
"""
from __future__ import annotations

from itertools import combinations
from typing import Iterable

import numpy as np
import sympy as sp


SINGLE_WITNESS = np.array([
    -2, 1, -2, 2, 2, 0, -2, 1, 0, 1, -2, 0, 1, 1, -1, 0, 0, -1, 0, 1,
    -2, 1, 2, 0, -2, 1, -2, -2, -1, -1, 2, 1, 2, -2, -2, -1, 2, 1, -2, -1,
], dtype=int)

DUAL_WITNESS = np.array([
    -2, 1, 1, 0, 0, 2, -2, 1, -1, -2, 0, 2, 1, 1, 1, 1, 0, -2, 2, 0,
    0, -1, -2, 2, 1, 1, 0, 2, 0, 0, 0, -1, -2, 0, 2, -2, 2, 2, -1, 1,
    -2, 1, 1, 0, 0, 2, -2, 1, -1, -2, 0, 2, 1, 1, 1, 1, 0, -2, 2, 0,
    0, -1, -2, 2, 1, 1, 0, 2, 0, 0, 0, -1, -2, 0, 2, -2, 2, 2, -1, 1,
], dtype=int)

# The dual witness is overwritten below by the exact witness used to obtain the
# published determinant values. Keeping the assignment explicit makes the
# packing convention reviewable.
DUAL_WITNESS = np.array([
    -2, 1, 1, 0, 0, 2, -2, 1, -1, -2, 0, 2, 1, 1, 1, 1, 0, -2, 2, 0,
    0, -1, -2, 2, 1, 1, 0, 2, 0, 0, 0, -1, -2, 0, 2, -2, 2, 2, -1, 1,
    -2, 1, 1, -1, -2, 2, 0, 2, 1, 1, 1, -2, -1, 0, 0, -2, 0, -2, 1, 1,
    2, 1, -1, 2, 0, -1, 2, -1, -2, 0, 1, -2, 0, -2, 1, 0, -1, -1, 0, 1,
], dtype=int)

# Expected exact invariants.
EXPECTED_SINGLE_E_DET = 4452
EXPECTED_SINGLE_MINOR_DET = 9016261632000
EXPECTED_DUAL_E_DET = 327
EXPECTED_DUAL_MINOR_DET = 68394848345664


def np_gammas() -> tuple[list[np.ndarray], np.ndarray]:
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    pauli = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    gamma0 = np.block([[i2, z2], [z2, -i2]])
    gamma = [gamma0]
    gamma.extend(np.block([[z2, s], [-s, z2]]) for s in pauli)
    eta = np.diag([1, -1, -1, -1]).astype(complex)
    return gamma, eta


def block_diag(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    z_ab = np.zeros((a.shape[0], b.shape[1]), dtype=complex)
    z_ba = np.zeros((b.shape[0], a.shape[1]), dtype=complex)
    return np.block([[a, z_ab], [z_ba, b]])


def cl5_two_branch_checks(tol: float = 1e-12) -> dict[str, float | int]:
    gamma4d, _ = np_gammas()
    gamma5 = 1j * gamma4d[0] @ gamma4d[1] @ gamma4d[2] @ gamma4d[3]
    fifth_plus = 1j * gamma5  # spacelike fifth generator: square -I
    plus = gamma4d + [fifth_plus]
    minus = gamma4d + [-fifth_plus]
    big = [block_diag(plus[a], minus[a]) for a in range(5)]
    eta5 = np.diag([1, -1, -1, -1, -1]).astype(complex)
    identity8 = np.eye(8, dtype=complex)

    clifford_residual = max(
        np.linalg.norm(big[a] @ big[b] + big[b] @ big[a] - 2 * eta5[a, b] * identity8)
        for a in range(5)
        for b in range(5)
    )

    omega = identity8.copy()
    for generator in big:
        omega = omega @ generator
    p_plus = (identity8 + omega) / 2
    p_minus = (identity8 - omega) / 2

    monomials: list[np.ndarray] = []
    for grade in range(6):
        for subset in combinations(range(5), grade):
            product = identity8.copy()
            for index in subset:
                product = product @ big[index]
            monomials.append(product)
    span_matrix = np.stack([m.reshape(-1) for m in monomials], axis=1)

    result = {
        "clifford_residual": float(clifford_residual),
        "monomial_count": len(monomials),
        "faithful_complex_span_rank": int(np.linalg.matrix_rank(span_matrix, tol=tol)),
        "omega_square_residual": float(np.linalg.norm(omega @ omega - identity8)),
        "projector_plus_rank": int(np.linalg.matrix_rank(p_plus, tol=tol)),
        "projector_minus_rank": int(np.linalg.matrix_rank(p_minus, tol=tol)),
        "projector_orthogonality_residual": float(np.linalg.norm(p_plus @ p_minus)),
    }
    return result


def sp_data() -> tuple[list[sp.Matrix], sp.Matrix]:
    i = sp.I
    z2 = sp.zeros(2)
    pauli = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -i], [i, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    gamma0 = sp.diag(1, 1, -1, -1)
    gamma = [gamma0]
    gamma.extend(
        sp.Matrix.vstack(sp.Matrix.hstack(z2, s), sp.Matrix.hstack(-s, z2))
        for s in pauli
    )
    eta = sp.diag(1, -1, -1, -1)
    return gamma, eta


GAMMA_SP, ETA_SP = sp_data()
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]


def adjoint(v: sp.Matrix) -> sp.Matrix:
    return sp.conjugate(v).T * GAMMA_SP[0]


def real_exact(z: sp.Expr) -> sp.Expr:
    return sp.simplify((z + sp.conjugate(z)) / 2)


def unpack_complex(values: np.ndarray, complex_count: int) -> list[sp.Expr]:
    if len(values) != 2 * complex_count:
        raise ValueError(f"expected {2 * complex_count} real entries, got {len(values)}")
    return [
        sp.Integer(int(values[k])) + sp.I * sp.Integer(int(values[complex_count + k]))
        for k in range(complex_count)
    ]


def single_parts(values: np.ndarray) -> tuple[sp.Matrix, list[sp.Matrix]]:
    c = unpack_complex(values, 20)
    theta = sp.Matrix(c[:4])
    dtheta = [sp.Matrix(c[4 + 4 * mu: 4 + 4 * (mu + 1)]) for mu in range(4)]
    return theta, dtheta


def single_delta(index: int) -> tuple[sp.Matrix, list[sp.Matrix]]:
    values = np.zeros(40, dtype=int)
    values[index] = 1
    return single_parts(values)


def single_tetrad(theta: sp.Matrix, dtheta: list[sp.Matrix]) -> sp.Matrix:
    result = sp.zeros(4, 4)
    for mu in range(4):
        for a in range(4):
            forward = (adjoint(theta) * GAMMA_SP[a] * dtheta[mu])[0]
            backward = (adjoint(dtheta[mu]) * GAMMA_SP[a] * theta)[0]
            result[mu, a] = real_exact(sp.I * (forward - backward) / 2)
    return result


def single_tetrad_variation(
    theta: sp.Matrix,
    dtheta: list[sp.Matrix],
    delta_theta: sp.Matrix,
    delta_dtheta: list[sp.Matrix],
) -> sp.Matrix:
    result = sp.zeros(4, 4)
    for mu in range(4):
        for a in range(4):
            variation = (
                (adjoint(delta_theta) * GAMMA_SP[a] * dtheta[mu])[0]
                + (adjoint(theta) * GAMMA_SP[a] * delta_dtheta[mu])[0]
                - (adjoint(delta_dtheta[mu]) * GAMMA_SP[a] * theta)[0]
                - (adjoint(dtheta[mu]) * GAMMA_SP[a] * delta_theta)[0]
            )
            result[mu, a] = real_exact(sp.I * variation / 2)
    return result


def exact_single_witness() -> dict[str, int]:
    theta, dtheta = single_parts(SINGLE_WITNESS)
    tetrad = single_tetrad(theta, dtheta)
    metric = tetrad * ETA_SP * tetrad.T
    columns: list[sp.Matrix] = []
    for index in range(10):
        delta_theta, delta_dtheta = single_delta(index)
        delta_e = single_tetrad_variation(theta, dtheta, delta_theta, delta_dtheta)
        delta_g = delta_e * ETA_SP * tetrad.T + tetrad * ETA_SP * delta_e.T
        columns.append(sp.Matrix([delta_g[i, j] for i, j in PAIRS]))
    minor = sp.Matrix.hstack(*columns)
    return {
        "tetrad_det": int(tetrad.det()),
        "metric_det": int(metric.det()),
        "selected_10x10_minor_det": int(minor.det()),
        "selected_minor_rank": int(minor.rank()),
    }


def dual_parts(
    values: np.ndarray,
) -> tuple[sp.Matrix, sp.Matrix, list[sp.Matrix], list[sp.Matrix]]:
    c = unpack_complex(values, 40)
    plus = sp.Matrix(c[:4])
    minus = sp.Matrix(c[4:8])
    dplus = [sp.Matrix(c[8 + 4 * mu: 8 + 4 * (mu + 1)]) for mu in range(4)]
    dminus = [sp.Matrix(c[24 + 4 * mu: 24 + 4 * (mu + 1)]) for mu in range(4)]
    return plus, minus, dplus, dminus


def dual_delta(
    index: int,
) -> tuple[sp.Matrix, sp.Matrix, list[sp.Matrix], list[sp.Matrix]]:
    values = np.zeros(80, dtype=int)
    values[index] = 1
    return dual_parts(values)


def dual_tetrad(
    plus: sp.Matrix,
    minus: sp.Matrix,
    dplus: list[sp.Matrix],
    dminus: list[sp.Matrix],
) -> sp.Matrix:
    result = sp.zeros(4, 4)
    for mu in range(4):
        for a in range(4):
            expression = (
                (adjoint(minus) * GAMMA_SP[a] * dplus[mu])[0]
                - (adjoint(dminus[mu]) * GAMMA_SP[a] * plus)[0]
                + (adjoint(plus) * GAMMA_SP[a] * dminus[mu])[0]
                - (adjoint(dplus[mu]) * GAMMA_SP[a] * minus)[0]
            )
            result[mu, a] = real_exact(sp.I * expression / 2)
    return result


def dual_tetrad_variation(
    plus: sp.Matrix,
    minus: sp.Matrix,
    dplus: list[sp.Matrix],
    dminus: list[sp.Matrix],
    delta_plus: sp.Matrix,
    delta_minus: sp.Matrix,
    delta_dplus: list[sp.Matrix],
    delta_dminus: list[sp.Matrix],
) -> sp.Matrix:
    result = sp.zeros(4, 4)
    for mu in range(4):
        for a in range(4):
            expression = (
                (adjoint(delta_minus) * GAMMA_SP[a] * dplus[mu])[0]
                + (adjoint(minus) * GAMMA_SP[a] * delta_dplus[mu])[0]
                - (adjoint(delta_dminus[mu]) * GAMMA_SP[a] * plus)[0]
                - (adjoint(dminus[mu]) * GAMMA_SP[a] * delta_plus)[0]
                + (adjoint(delta_plus) * GAMMA_SP[a] * dminus[mu])[0]
                + (adjoint(plus) * GAMMA_SP[a] * delta_dminus[mu])[0]
                - (adjoint(delta_dplus[mu]) * GAMMA_SP[a] * minus)[0]
                - (adjoint(dplus[mu]) * GAMMA_SP[a] * delta_minus)[0]
            )
            result[mu, a] = real_exact(sp.I * expression / 2)
    return result


def exact_dual_witness() -> dict[str, int]:
    plus, minus, dplus, dminus = dual_parts(DUAL_WITNESS)
    tetrad = dual_tetrad(plus, minus, dplus, dminus)
    metric = tetrad * ETA_SP * tetrad.T
    columns: list[sp.Matrix] = []
    for index in range(10):
        dp, dm, ddp, ddm = dual_delta(index)
        delta_e = dual_tetrad_variation(
            plus, minus, dplus, dminus, dp, dm, ddp, ddm
        )
        delta_g = delta_e * ETA_SP * tetrad.T + tetrad * ETA_SP * delta_e.T
        columns.append(sp.Matrix([delta_g[i, j] for i, j in PAIRS]))
    minor = sp.Matrix.hstack(*columns)
    return {
        "tetrad_det": int(tetrad.det()),
        "metric_det": int(metric.det()),
        "selected_10x10_minor_det": int(minor.det()),
        "selected_minor_rank": int(minor.rank()),
    }


def assert_expected() -> dict[str, dict[str, float | int]]:
    cl5 = cl5_two_branch_checks()
    assert cl5["clifford_residual"] < 1e-12
    assert cl5["monomial_count"] == 32
    assert cl5["faithful_complex_span_rank"] == 32
    assert cl5["omega_square_residual"] < 1e-12
    assert cl5["projector_plus_rank"] == 4
    assert cl5["projector_minus_rank"] == 4
    assert cl5["projector_orthogonality_residual"] < 1e-12

    single = exact_single_witness()
    assert single["tetrad_det"] == EXPECTED_SINGLE_E_DET
    assert single["selected_10x10_minor_det"] == EXPECTED_SINGLE_MINOR_DET
    assert single["selected_minor_rank"] == 10

    dual = exact_dual_witness()
    assert dual["tetrad_det"] == EXPECTED_DUAL_E_DET
    assert dual["selected_10x10_minor_det"] == EXPECTED_DUAL_MINOR_DET
    assert dual["selected_minor_rank"] == 10
    return {"cl5": cl5, "single": single, "dual": dual}


def main() -> None:
    results = assert_expected()
    print("UBT dual-sector Clifford-5 verifier")
    print("=" * 42)
    for section, checks in results.items():
        print(f"[{section}]")
        for name, value in checks.items():
            print(f"PASS  {name:38s} {value}")
    print("\nScope: algebraic and off-shell first-jet claims only.")
    print("On-shell UBT/complex-time/Einstein closure remains open.")


if __name__ == "__main__":
    main()
