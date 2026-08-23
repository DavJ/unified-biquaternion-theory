#!/usr/bin/env python3
"""Exact invariant-space audit for the local Theta potential.

Scope
-----
The field value is represented by a generic matrix X in Mat(2,C).  The tested
connected group is

    X -> exp(i alpha) S X S^dagger,       S in SL(2,C).

The script classifies real homogeneous polynomial invariants of total degrees
two and four.  It does not select their coefficients, include derivatives,
classify additional internal-carrier actions, or prove stability.

The quadratic rank is computed exactly over Q with SymPy.  The quartic rank is
certified over two finite fields.  Because the infinitesimal constraint matrix
has integer entries after multiplication by two, rank 328 modulo either prime
exhibits a nonzero integer 328-minor.  Two explicit rational kernel vectors
give the opposite bound over Q, so the characteristic-zero rank is exactly
328.
"""

from __future__ import annotations

from collections.abc import Iterable

import sympy as sp


N_REAL = 8
I = sp.I


def pauli_generators() -> list[sp.Matrix]:
    sigma = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -I], [I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    # Hermitian generators are boosts; anti-Hermitian generators are rotations.
    return [entry / 2 for entry in sigma] + [I * entry / 2 for entry in sigma]


def realified_spin_generator(generator: sp.Matrix) -> sp.Matrix:
    """Real 8x8 generator of delta X = A X + X A^dagger."""
    result = sp.zeros(N_REAL)
    for column in range(N_REAL):
        entries: list[sp.Expr] = [sp.Integer(0)] * 4
        entries[column // 2] = 1 if column % 2 == 0 else I
        x = sp.Matrix([[entries[0], entries[1]], [entries[2], entries[3]]])
        delta = generator * x + x * generator.conjugate().T
        flat = [delta[0, 0], delta[0, 1], delta[1, 0], delta[1, 1]]
        for row, value in enumerate(flat):
            result[2 * row, column] = sp.re(value)
            result[2 * row + 1, column] = sp.im(value)
    return result


def phase_generator() -> sp.Matrix:
    """Real generator of delta X = i X."""
    result = sp.zeros(N_REAL)
    for entry in range(4):
        result[2 * entry, 2 * entry + 1] = -1
        result[2 * entry + 1, 2 * entry] = 1
    return result


def generators() -> list[sp.Matrix]:
    return [realified_spin_generator(a) for a in pauli_generators()] + [phase_generator()]


def monomial_exponents(variables: int, degree: int) -> list[tuple[int, ...]]:
    if variables == 1:
        return [(degree,)]
    return [
        (head,) + tail
        for head in range(degree + 1)
        for tail in monomial_exponents(variables - 1, degree - head)
    ]


def derivative_rows(generator: sp.Matrix, degree: int) -> list[dict[int, int]]:
    """Rows of twice the infinitesimal action on degree-d monomials.

    All Lie generators have half-integral entries, hence the factor two makes
    this an integer matrix without changing its rank in characteristic zero.
    """
    basis = monomial_exponents(N_REAL, degree)
    index = {exponent: position for position, exponent in enumerate(basis)}
    rows: list[dict[int, int]] = [{} for _ in basis]
    for column, exponent in enumerate(basis):
        for output_coordinate, power in enumerate(exponent):
            if power == 0:
                continue
            for input_coordinate in range(N_REAL):
                coefficient = generator[output_coordinate, input_coordinate]
                if coefficient == 0:
                    continue
                shifted = list(exponent)
                shifted[output_coordinate] -= 1
                shifted[input_coordinate] += 1
                row = index[tuple(shifted)]
                integer_coefficient = int(2 * coefficient) * power
                rows[row][column] = rows[row].get(column, 0) + integer_coefficient
    return rows


def stacked_rows(degree: int) -> list[dict[int, int]]:
    return [row for generator in generators() for row in derivative_rows(generator, degree)]


def sparse_rank_mod_prime(rows: Iterable[dict[int, int]], prime: int) -> int:
    """Exact sparse Gaussian rank over F_prime, implemented independently."""
    echelon: dict[int, dict[int, int]] = {}
    for source in rows:
        row = {column: value % prime for column, value in source.items() if value % prime}
        while row:
            pivot = min(row)
            known = echelon.get(pivot)
            if known is None:
                inverse = pow(row[pivot], prime - 2, prime)
                echelon[pivot] = {
                    column: (value * inverse) % prime
                    for column, value in row.items()
                    if value % prime
                }
                break
            factor = row[pivot]
            for column, value in known.items():
                reduced = (row.get(column, 0) - factor * value) % prime
                if reduced:
                    row[column] = reduced
                else:
                    row.pop(column, None)
    return len(echelon)


def coordinate_polynomials() -> tuple[tuple[sp.Symbol, ...], sp.Expr, sp.Expr, sp.Expr]:
    coordinates = sp.symbols("x0:8", real=True)
    a = coordinates[0] + I * coordinates[1]
    b = coordinates[2] + I * coordinates[3]
    c = coordinates[4] + I * coordinates[5]
    d = coordinates[6] + I * coordinates[7]
    x = sp.Matrix([[a, b], [c, d]])
    sharp = sp.Matrix([[d, -b], [-c, a]])
    h = sp.expand(sp.trace(sharp * x.conjugate().T))
    determinant = sp.expand(x.det())
    determinant_norm = sp.expand(determinant * sp.conjugate(determinant))
    hilbert_schmidt = sp.expand(sp.trace(x.conjugate().T * x))
    return coordinates, h, determinant_norm, hilbert_schmidt


def lie_derivative(polynomial: sp.Expr, generator: sp.Matrix, coordinates: tuple[sp.Symbol, ...]) -> sp.Expr:
    vector = generator * sp.Matrix(coordinates)
    return sp.expand(sum(vector[row] * sp.diff(polynomial, coordinates[row]) for row in range(N_REAL)))


def check_candidate_invariants() -> None:
    coordinates, h, determinant_norm, _ = coordinate_polynomials()
    expected_h = (
        2 * (coordinates[0] * coordinates[6] + coordinates[1] * coordinates[7])
        - coordinates[2] ** 2
        - coordinates[3] ** 2
        - coordinates[4] ** 2
        - coordinates[5] ** 2
    )
    assert sp.expand(h - expected_h) == 0
    for generator in generators():
        assert lie_derivative(h, generator, coordinates) == 0
        assert lie_derivative(h**2, generator, coordinates) == 0
        assert lie_derivative(determinant_norm, generator, coordinates) == 0

    # H^2 and |det X|^2 are independent: their evaluation vectors at these
    # two field values have nonzero determinant.
    identity = {coordinates[i]: value for i, value in enumerate([1, 0, 0, 0, 0, 0, 1, 0])}
    nilpotent = {coordinates[i]: value for i, value in enumerate([0, 0, 1, 0, 0, 0, 0, 0])}
    evaluation = sp.Matrix(
        [
            [h.subs(identity) ** 2, determinant_norm.subs(identity)],
            [h.subs(nilpotent) ** 2, determinant_norm.subs(nilpotent)],
        ]
    )
    assert evaluation.det() != 0


def check_quadratic_rank() -> None:
    basis = monomial_exponents(N_REAL, 2)
    rows = stacked_rows(2)
    matrix = sp.MutableSparseMatrix(len(rows), len(basis), {})
    for row, entries in enumerate(rows):
        for column, value in entries.items():
            matrix[row, column] = value
    rank = sp.SparseMatrix(matrix).rank()
    assert len(basis) == 36
    assert rank == 35


def check_quartic_rank() -> None:
    basis = monomial_exponents(N_REAL, 4)
    rows = stacked_rows(4)
    assert len(basis) == 330
    for prime in (1_000_003, 1_000_033):
        assert sparse_rank_mod_prime(rows, prime) == 328


def check_hilbert_schmidt_counterexample() -> None:
    # S=diag(2,1/2), X=I: SXS^dagger=diag(4,1/4).
    before = sp.Integer(2)
    after = sp.Integer(16) + sp.Rational(1, 16)
    assert after != before


def main() -> None:
    check_candidate_invariants()
    check_quadratic_rank()
    check_quartic_rank()
    check_hilbert_schmidt_counterexample()
    print("PASS: quadratic invariant space dimension = 1 (36 - rank 35)")
    print("PASS: quartic invariant space dimension = 2 (330 - rank 328)")
    print("PASS: basis is H, then H^2 and |det X|^2; Hilbert-Schmidt mass term fails")
    print("NOT TESTED: coefficient selection, boundedness, derivatives, measure, Hessian, psi stability")
    print("LEAN-PENDING: the 330-monomial completeness/rank certificate")


if __name__ == "__main__":
    main()
