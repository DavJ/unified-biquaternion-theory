#!/usr/bin/env python3
"""Exact finite-algebra checks for the UBT field-space symplectic construction."""

from fractions import Fraction as Q
from itertools import combinations

import sympy as sp


def wedge(a, b):
    """Wedge sparse forms represented by sorted index tuples -> coefficients."""
    out = {}
    for ia, ca in a.items():
        for ib, cb in b.items():
            if set(ia) & set(ib):
                continue
            inv = sum(i > j for i in ia for j in ib)
            key = tuple(sorted(ia + ib))
            coeff = ca * cb * (-1 if inv % 2 else 1)
            out[key] = out.get(key, Q(0)) + coeff
    return {k: v for k, v in out.items() if v != 0}


def verify():
    G = sp.Matrix([
        [0, 0, 0, 1],
        [0, -1, 0, 0],
        [0, 0, -1, 0],
        [1, 0, 0, 0],
    ])
    Z = sp.zeros(4)
    Omega = Z.row_join(G).col_join((-G).row_join(Z))

    assert G.det() == -1
    assert Omega.T == -Omega
    assert Omega.det() == 1

    # omega = sum_{i<j} Omega_ij dq_i wedge dq_j.
    omega = {}
    for i, j in combinations(range(8), 2):
        c = Q(int(Omega[i, j]))
        if c:
            omega[(i, j)] = c
    omega2 = wedge(omega, omega)
    assert omega2

    # At x_a=1, all other real coordinates zero, H=x^T G x+y^T G y
    # has dH=2 dx_d, i.e. coordinate index 3 in (x_a,x_b,x_c,x_d,y_a,...).
    dH = {(3,): Q(2)}
    five_form = wedge(dH, omega2)
    assert five_form

    # Record a deterministic nonzero component as an exact witness.
    key = sorted(five_form)[0]
    assert five_form[key] != 0
    print("Invariant field-space symplectic matrix: PASS")
    print(f"nonzero dH wedge omega^2 component {key} = {five_form[key]}")


if __name__ == "__main__":
    verify()
