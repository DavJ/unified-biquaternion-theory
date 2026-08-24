#!/usr/bin/env python3
"""Exact symbolic Piola-identity check for a 4D gradient Jacobian."""

import itertools
import sympy as sp


def eps4(indices):
    if len(set(indices)) < 4:
        return 0
    inv = sum(indices[i] > indices[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inv % 2 else 1


def verify():
    # J[mu,a] = partial_mu X^a; Q[mu,nu,a] is a formal Hessian symmetric in mu,nu.
    J = [[sp.Symbol(f"J{mu}{a}") for a in range(4)] for mu in range(4)]
    q_symbols = {}
    def Q(mu, nu, a):
        key = (min(mu, nu), max(mu, nu), a)
        if key not in q_symbols:
            q_symbols[key] = sp.Symbol(f"Q{key[0]}{key[1]}{a}")
        return q_symbols[key]

    # Divergence of cofactor column a. Differentiate the epsilon expression
    # formally: each of the three J factors is hit once.
    for a in range(4):
        expr = 0
        for mu, nu, rho, sig in itertools.product(range(4), repeat=4):
            e1 = eps4((mu, nu, rho, sig))
            if not e1:
                continue
            for b, c, d in itertools.product(range(4), repeat=3):
                e2 = eps4((a, b, c, d))
                if not e2:
                    continue
                expr += sp.Rational(1, 6) * e1 * e2 * (
                    Q(mu, nu, b) * J[rho][c] * J[sig][d]
                    + J[nu][b] * Q(mu, rho, c) * J[sig][d]
                    + J[nu][b] * J[rho][c] * Q(mu, sig, d)
                )
        assert sp.expand(expr) == 0

    print("4D Piola identity for gradient Jacobian: PASS")


if __name__ == "__main__":
    verify()
