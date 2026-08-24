#!/usr/bin/env python3
"""Exact rank certificate for the scalar equivariant-symplectic curvature coupling.

For the closed equivariant two-form Qhat = Q - <mu,F>, the term linear in the
Lorentz curvature has coefficients B_r proportional to mu_r Q.  Therefore the
six Lorentz-labelled spacetime two-forms span at most one dimension.  This
script compares that structural bound with the rank-six Palatini bivector map
for an exact nondegenerate tetrad.
"""

from __future__ import annotations

import sympy as sp


def two_form_basis() -> list[tuple[int, int]]:
    return [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def levi_civita4(a: int, b: int, c: int, d: int) -> int:
    if len({a, b, c, d}) < 4:
        return 0
    permutation = [a, b, c, d]
    inversions = sum(permutation[i] > permutation[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inversions % 2 else 1


def palatini_b_matrix(e: sp.Matrix) -> sp.Matrix:
    """Rows B_ab in coordinate two-form basis for B_ab=1/2 eps_abcd e^c wedge e^d."""
    lorentz_pairs = two_form_basis()
    coord_pairs = two_form_basis()
    rows = []
    for a, b in lorentz_pairs:
        coefficients = []
        for mu, nu in coord_pairs:
            coefficient = sp.Integer(0)
            for c in range(4):
                for d in range(4):
                    coefficient += sp.Rational(1, 2) * levi_civita4(a, b, c, d) * (
                        e[mu, c] * e[nu, d] - e[nu, c] * e[mu, d]
                    )
            coefficients.append(sp.simplify(coefficient))
        rows.append(coefficients)
    return sp.Matrix(rows)


def scalar_equivariant_b_matrix(mu: sp.Matrix, q: sp.Matrix) -> sp.Matrix:
    """Six Lorentz-labelled B_r=mu_r Q rows in the same two-form basis."""
    assert mu.shape == (6, 1)
    assert q.shape == (1, 6)
    return mu * q


def verify() -> None:
    # Exact nondegenerate tetrad. Identity already suffices, but use a simple
    # upper-triangular witness to show the claim is not tied to orthonormal coordinates.
    e = sp.Matrix(
        [
            [1, 1, 0, 0],
            [0, 2, 1, 0],
            [0, 0, 3, 1],
            [0, 0, 0, 4],
        ]
    )
    assert e.det() == 24
    palatini = palatini_b_matrix(e)
    assert palatini.shape == (6, 6)
    assert palatini.rank() == 6
    assert palatini.det() != 0

    # An arbitrary exact nonzero moment-map vector and spacetime two-form.
    # The rank-one factorization is structural and independent of their values.
    mu = sp.Matrix([1, 2, -1, 3, 5, -2])
    q = sp.Matrix([[2, -3, 1, 4, 0, 7]])
    scalar_b = scalar_equivariant_b_matrix(mu, q)
    assert scalar_b.rank() == 1

    # Symbolic outer-product structure gives rank <= 1 for every mu,Q.
    assert all(
        scalar_b.row(i)[a] * scalar_b.row(j)[b] - scalar_b.row(i)[b] * scalar_b.row(j)[a] == 0
        for i in range(6)
        for j in range(6)
        for a in range(6)
        for b in range(6)
    )

    print("PASS: nondegenerate Palatini bivector map rank = 6")
    print("PASS: scalar equivariant-symplectic curvature coefficient rank <= 1")
    print("PASS: the scalar completion cannot equal the Palatini bivector coupling")


if __name__ == "__main__":
    verify()
