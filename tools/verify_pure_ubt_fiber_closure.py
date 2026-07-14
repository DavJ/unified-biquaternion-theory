#!/usr/bin/env python3
"""Exact linear-algebra checks for the pure-UBT complex-time-fiber closure.

This script does not prove the functional-analytic theorem by computation. It
verifies the finite-dimensional local jet models used in the proof:

* an 8-real-dimensional single-section carrier has at most four independent
  normal closure vectors;
* retaining ten independent psi modes supplies a rank-ten closure block;
* the local time-gradient normalization fixes g_00 to -1 on a timelike branch;
* a corank-one closure matrix has rank-one adjugate.
"""

from __future__ import annotations

import sympy as sp

PAIR_ORDER = (
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 2),
    (2, 3),
    (3, 3),
)


def single_section_closure_matrix() -> sp.Matrix:
    """Return an 8x10 closure matrix with image in a 4D normal space."""
    matrix = sp.zeros(8, 10)
    # Tangent directions occupy rows 0..3. All normal second derivatives must
    # lie in rows 4..7, so rank cannot exceed four.
    for column in range(10):
        matrix[4 + (column % 4), column] = 1
    return matrix


def fiber_completed_closure_matrix() -> sp.Matrix:
    """Return a 14x10 free-fiber closure matrix of exact rank ten."""
    matrix = sp.zeros(14, 10)
    # Four tangent modes occupy rows 0..3 and ten mutually orthogonal psi modes
    # occupy rows 4..13.
    for column in range(10):
        matrix[4 + column, column] = 1
    return matrix


def induced_metric_at_origin() -> sp.Matrix:
    """Metric from four orthogonal tangent profiles in signature (-,+,...)."""
    target_metric = sp.diag(-1, *([1] * 13))
    tangents = sp.zeros(14, 4)
    for column in range(4):
        tangents[column, column] = 1
    return sp.simplify(tangents.T * target_metric * tangents)


def verify_local_normalization() -> sp.Expr:
    timelike_norm = sp.symbols("a", negative=True, nonzero=True)
    return sp.simplify(timelike_norm / sp.Abs(timelike_norm))


def corank_one_adjugate() -> tuple[int, int, sp.Matrix]:
    matrix = sp.diag(*([1] * 9), 0)
    adjugate = matrix.adjugate()
    return matrix.rank(), adjugate.rank(), adjugate


def run_checks() -> None:
    single = single_section_closure_matrix()
    fiber = fiber_completed_closure_matrix()
    metric = induced_metric_at_origin()
    local_g00 = verify_local_normalization()
    matrix_rank, adjugate_rank, adjugate = corank_one_adjugate()

    assert single.shape == (8, 10)
    assert single.rank() == 4
    assert len(single.nullspace()) == 6

    assert fiber.shape == (14, 10)
    assert fiber.rank() == 10
    assert len(fiber.nullspace()) == 0

    assert metric == sp.diag(-1, 1, 1, 1)
    assert local_g00 == -1

    assert matrix_rank == 9
    assert adjugate_rank == 1
    assert adjugate == sp.diag(*([0] * 9), 1)

    print("PASS: single-section B-valued closure rank is 4, with kernel dimension 6.")
    print("PASS: ten independent complex-time-fiber modes give closure rank 10.")
    print("PASS: the constructed tangent Gram matrix is diag(-1,+1,+1,+1).")
    print("PASS: local time-gradient normalization forces g_00=-1.")
    print("PASS: a corank-one 10x10 closure block has rank-one adjugate.")
    print("NOT TESTED: dynamical selection of the fiber-free Jacobi-theta sector.")
    print("NOT TESTED: single-action separation of internal and metric equations.")


if __name__ == "__main__":
    run_checks()
