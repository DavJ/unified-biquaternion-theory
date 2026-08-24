#!/usr/bin/env python3
"""Finite-index exact check of the double-antisymmetry cancellation criterion."""

from fractions import Fraction as Q


def verify():
    # Use two spacetime and two field indices. Let W^{mu nu}_{AB}
    # be generated from one doubly antisymmetric component k.
    k = Q(7, 5)

    def W(mu, nu, A, B):
        if mu == nu or A == B:
            return Q(0)
        s_mu = Q(1) if (mu, nu) == (0, 1) else Q(-1)
        s_ab = Q(1) if (A, B) == (0, 1) else Q(-1)
        return k * s_mu * s_ab

    # Hessian pair-exchange symmetry W^{mu nu}_{AB}=W^{nu mu}_{BA}.
    for mu in range(2):
        for nu in range(2):
            for A in range(2):
                for B in range(2):
                    assert W(mu, nu, A, B) == W(nu, mu, B, A)
                    assert W(mu, nu, A, B) == -W(nu, mu, A, B)
                    assert W(mu, nu, A, B) == -W(mu, nu, B, A)

    # Contract with an arbitrary symmetric formal second jet S_{mu nu}^B.
    S = {
        (0, 0, 0): Q(2), (0, 1, 0): Q(3), (1, 0, 0): Q(3), (1, 1, 0): Q(5),
        (0, 0, 1): Q(7), (0, 1, 1): Q(11), (1, 0, 1): Q(11), (1, 1, 1): Q(13),
    }
    for A in range(2):
        contraction = sum(
            W(mu, nu, A, B) * S[(mu, nu, B)]
            for mu in range(2) for nu in range(2) for B in range(2)
        )
        assert contraction == 0

    # Standard symmetric metric x symmetric field pairing does not cancel.
    g = [[Q(1), Q(0)], [Q(0), Q(2)]]
    h = [[Q(3), Q(0)], [Q(0), Q(5)]]
    nonzero = sum(g[mu][nu] * h[0][0] * S[(mu, nu, 0)] for mu in range(2) for nu in range(2))
    assert nonzero != 0

    print("Double-antisymmetric Hessian cancellation criterion: PASS")


if __name__ == "__main__":
    verify()
