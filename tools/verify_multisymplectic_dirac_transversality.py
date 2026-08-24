#!/usr/bin/env python3
"""Exact checks for the multisymplectic EL, Hessian and Dirac obstruction."""

from __future__ import annotations

from itertools import combinations

import sympy as sp


def wedge(left, right):
    out = {}
    for ia, ca in left.items():
        for ib, cb in right.items():
            if set(ia) & set(ib):
                continue
            inversions = sum(i > j for i in ia for j in ib)
            key = tuple(sorted(ia + ib))
            out[key] = sp.expand(out.get(key, 0) + (-1) ** inversions * ca * cb)
    return {key: value for key, value in out.items() if value != 0}


def contract(form, vector):
    out = {}
    for indices, coefficient in form.items():
        for position, index in enumerate(indices):
            reduced = indices[:position] + indices[position + 1 :]
            out[reduced] = sp.expand(
                out.get(reduced, 0) + (-1) ** position * vector[index] * coefficient
            )
    return {key: value for key, value in out.items() if value != 0}


def evaluate_four_form(form, columns):
    value = form
    for column in columns:
        value = contract(value, column)
    return sp.expand(value.get((), 0))


def matrices():
    g = sp.Matrix(
        [[0, 0, 0, 1], [0, -1, 0, 0], [0, 0, -1, 0], [1, 0, 0, 0]]
    )
    zero = sp.zeros(4)
    omega = zero.row_join(g).col_join((-g).row_join(zero))
    hessian_h = g.row_join(zero).col_join(zero.row_join(g))
    return omega, hessian_h


def theta_el_and_jacobian(p):
    omega, hessian_h = matrices()
    theta = sp.Matrix(sp.symbols("theta0:8", real=True))
    d_h = 2 * hessian_h * theta
    one_form = {(index,): d_h[index] for index in range(8) if d_h[index] != 0}
    omega_form = {
        (i, j): omega[i, j]
        for i, j in combinations(range(8), 2)
        if omega[i, j] != 0
    }
    five_form = wedge(one_form, wedge(omega_form, omega_form))
    columns = [list(p[:, mu]) for mu in range(4)]
    equations = []
    for field_index in range(8):
        basis = [sp.Integer(0)] * 8
        basis[field_index] = sp.Integer(1)
        equations.append(evaluate_four_form(contract(five_form, basis), columns))
    equation_vector = sp.Matrix(equations)
    return theta, equation_vector, equation_vector.jacobian(theta)


def pfaffian_density(theta, p_symbols):
    omega, hessian_h = matrices()
    p = sp.Matrix(8, 4, p_symbols)
    q = p.T * omega * p
    pfaffian = q[0, 1] * q[2, 3] - q[0, 2] * q[1, 3] + q[0, 3] * q[1, 2]
    h = (theta.T * hessian_h * theta)[0]
    return sp.expand(h * pfaffian)


def verify():
    # Exact rank-four rational jet with nondegenerate pulled-back Q.
    p = sp.Matrix(
        [
            [1, 0, 0, 2], [0, 1, 3, 0], [2, 0, 1, 1], [0, 2, 0, 1],
            [1, 1, 0, 0], [0, 1, 1, 2], [2, 1, 0, 1], [1, 0, 2, 1],
        ]
    )
    omega, _ = matrices()
    assert p.rank() == 4
    assert (p.T * omega * p).det() != 0

    theta, equations, jacobian = theta_el_and_jacobian(p)
    # Four tangent/reparametrization identities, valid symbolically in theta.
    assert sp.simplify(p.T * equations) == sp.zeros(4, 1)
    # The upper bound is sharp at this exact witness, so F_Psi is singular.
    assert jacobian.rank() == 4
    assert jacobian.det() == 0

    # Exact Hessian checks at deterministic rational witnesses. Differentiating
    # the full 32-variable Pfaffian density checks all cross terms, not a toy
    # truncation. Substitute only after taking both derivatives.
    variables = sp.symbols("p0:32", real=True)
    theta_witness = sp.Matrix([1, 2, -1, 3, 0, 1, 2, -2])
    density = pfaffian_density(theta_witness, variables)
    velocity_hessian = sp.hessian(density, variables)
    substitution = {variables[4 * a + mu]: p[a, mu] for a in range(8) for mu in range(4)}
    w = velocity_hessian.subs(substitution)

    def index(a, mu):
        return 4 * a + mu

    for a in range(8):
        for b in range(8):
            for mu in range(4):
                for nu in range(4):
                    value = w[index(a, mu), index(b, nu)]
                    assert value == -w[index(a, nu), index(b, mu)]
                    assert value == -w[index(b, mu), index(a, nu)]

    symmetric_second_jet = [
        [[sp.Integer((a + 1) * (mu + nu + 1)) for nu in range(4)] for mu in range(4)]
        for a in range(8)
    ]
    for a in range(8):
        contraction_value = sum(
            w[index(a, mu), index(b, nu)] * symmetric_second_jet[b][mu][nu]
            for b in range(8) for mu in range(4) for nu in range(4)
        )
        assert sp.expand(contraction_value) == 0

    print("PASS: four exact tangent identities P^T E = 0")
    print("PASS: exact field-value Jacobian rank = 4 < 8")
    print("PASS: full first-jet Hessian is doubly antisymmetric")
    print("PASS: all symmetric second-jet contractions vanish")


if __name__ == "__main__":
    verify()
