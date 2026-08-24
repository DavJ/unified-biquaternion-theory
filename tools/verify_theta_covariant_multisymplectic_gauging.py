#!/usr/bin/env python3
"""Exact finite checks for local gauging of the Theta multisymplectic family.

This verifies theorem-critical algebraic facts:

1. the connected spin+phase generators preserving the quadratic invariant H
   also preserve the induced real symplectic form Omega;
2. H and |det X|^2 are functionally independent at an explicit field value;
3. at that value the infinitesimal group orbit has real dimension six, hence
   rank six on a nonempty open generic stratum;
4. the moment-map constraints produced by a purely auxiliary symplectic
   connection then leave only a two-dimensional symplectic-orthogonal subspace
   for D_mu Theta.

The exterior-calculus implication that alpha wedge Q = 0 implies alpha = 0 on
four-dimensional branches with Q wedge Q != 0 is analytic and recorded in the
paired theorem note.
"""

from __future__ import annotations

import sympy as sp

I = sp.I

G = sp.Matrix(
    [
        [0, 0, 0, 1],
        [0, -1, 0, 0],
        [0, 0, -1, 0],
        [1, 0, 0, 0],
    ]
)


def pauli_generators() -> list[sp.Matrix]:
    sigma = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -I], [I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    return [entry / 2 for entry in sigma] + [I * entry / 2 for entry in sigma]


def complex_spin_generator(generator: sp.Matrix) -> sp.Matrix:
    """Complex 4x4 generator on z=(a,b,c,d) for delta X=A X+X A^dagger."""
    out = sp.zeros(4)
    for column in range(4):
        values = [sp.Integer(0)] * 4
        values[column] = sp.Integer(1)
        x = sp.Matrix([[values[0], values[1]], [values[2], values[3]]])
        delta = generator * x + x * generator.conjugate().T
        flat = [delta[0, 0], delta[0, 1], delta[1, 0], delta[1, 1]]
        for row, value in enumerate(flat):
            out[row, column] = sp.simplify(value)
    return out


def complex_generators() -> list[sp.Matrix]:
    # The final generator is the central phase delta z=i z.
    return [complex_spin_generator(a) for a in pauli_generators()] + [I * sp.eye(4)]


def realify(generator: sp.Matrix) -> sp.Matrix:
    """Realification in ordering (Re z_1..Re z_4, Im z_1..Im z_4)."""
    re = generator.applyfunc(sp.re)
    im = generator.applyfunc(sp.im)
    return re.row_join(-im).col_join(im.row_join(re))


def symplectic_matrix() -> sp.Matrix:
    zero = sp.zeros(4)
    return zero.row_join(G).col_join((-G).row_join(zero))


def invariant_gradients_at(theta: sp.Matrix) -> sp.Matrix:
    """Rows dH and d|det X|^2 evaluated at theta in all-real/all-imag order."""
    x = sp.symbols("x0:4", real=True)
    y = sp.symbols("y0:4", real=True)
    z = [x[i] + I * y[i] for i in range(4)]
    vector = sp.Matrix(z)
    h = sp.expand((vector.conjugate().T * G * vector)[0])
    matrix = sp.Matrix([[z[0], z[1]], [z[2], z[3]]])
    determinant = sp.expand(matrix.det())
    determinant_norm = sp.expand(determinant * sp.conjugate(determinant))
    coordinates = list(x) + list(y)
    substitution = {coordinates[i]: theta[i] for i in range(8)}
    grad_h = [sp.diff(h, q).subs(substitution) for q in coordinates]
    grad_d = [sp.diff(determinant_norm, q).subs(substitution) for q in coordinates]
    return sp.Matrix([grad_h, grad_d])


def verify() -> None:
    omega = symplectic_matrix()
    assert G.det() == -1
    assert omega.T == -omega
    assert omega.det() == 1

    complex_gens = complex_generators()
    real_gens = [realify(generator) for generator in complex_gens]

    # H-invariance is the infinitesimal pseudo-unitarity condition. It implies
    # preservation of both Re h and Im h; check the symplectic condition too.
    for complex_generator, real_generator in zip(complex_gens, real_gens, strict=True):
        assert sp.simplify(complex_generator.conjugate().T * G + G * complex_generator) == sp.zeros(4)
        assert sp.simplify(real_generator.T * omega + omega * real_generator) == sp.zeros(8)

    # Explicit rational/complex field value z=(1+i, 2+3i, 4+5i, 6+7i).
    theta = sp.Matrix([1, 2, 4, 6, 1, 3, 5, 7])
    orbit = sp.Matrix.hstack(*(generator * theta for generator in real_gens))

    # H and D=|det X|^2 are two independent invariant functions here. Their
    # gradients annihilate the orbit, so the orbit rank is at most six on the
    # open stratum where the gradients remain independent. The exact witness
    # reaches rank six, fixing the generic rank on a nonempty open set.
    invariant_gradients = invariant_gradients_at(theta)
    assert invariant_gradients.rank() == 2
    assert sp.simplify(invariant_gradients * orbit) == sp.zeros(2, 7)
    assert orbit.rank() == 6

    # Auxiliary-connection moment-map equations on a nondegenerate Q branch
    # impose omega(T_r Theta, v)=0 for every generator. Since omega is
    # invertible, the constraint matrix has the same rank as the orbit.
    constraints = orbit.T * omega
    assert constraints.rank() == 6
    assert len(constraints.nullspace()) == 2

    print("PASS: all seven connected spin+phase generators preserve Omega")
    print("PASS: dH and d|det X|^2 are independent at the exact witness")
    print("PASS: generic-stratum orbit rank = 6")
    print("PASS: auxiliary moment-map allowed subspace dimension = 2")


if __name__ == "__main__":
    verify()
