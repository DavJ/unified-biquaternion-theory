#!/usr/bin/env python3
"""Exact finite rank check for the split-jet Palatini variational lift.

The analytic theorem uses the explicit non-null right inverse already proved in
the GR split-jet track. This script checks the finite linear-algebra core at an
exact non-null witness: the Lorentz-jet plus relative-central variations span
all four tetrad directions, hence the transpose map on the tetrad Euler
gradient is injective.
"""

from __future__ import annotations

import sympy as sp

ETA = sp.diag(-1, 1, 1, 1)


def lorentz_generators() -> list[sp.Matrix]:
    """Six exact vector-representation generators of so(1,3)."""
    generators: list[sp.Matrix] = []
    for a in range(4):
        for b in range(a + 1, 4):
            matrix = sp.zeros(4)
            # Generator M^c_d = eta^{ca}(delta_b)_d - eta^{cb}(delta_a)_d.
            matrix[a, b] = ETA[a, a]
            matrix[b, a] = -ETA[b, b]
            assert matrix.T * ETA + ETA * matrix == sp.zeros(4)
            generators.append(matrix)
    return generators


def verify() -> None:
    generators = lorentz_generators()
    assert len(generators) == 6

    # Exact non-null witness X=(2,1,0,0), X^2=-3.
    x = sp.Matrix([2, 1, 0, 0])
    assert (x.T * ETA * x)[0] == -3

    # Columns are delta K_r X for the six Lorentz directions, plus delta w X.
    jet_map = sp.Matrix.hstack(*(generator * x for generator in generators), x)
    assert jet_map.shape == (4, 7)
    assert jet_map.rank() == 4

    # If E is the tetrad Euler gradient, auxiliary stationarity is J^T E=0.
    # Rank(J)=4 makes J^T injective, so there is no projected-equation loss.
    adjoint = jet_map.T
    assert adjoint.rank() == 4
    assert adjoint.nullspace() == []

    # Verify the analytic right-inverse formula on several exact target vectors.
    x_sq = (x.T * ETA * x)[0]
    for target in (
        sp.Matrix([1, 0, 0, 0]),
        sp.Matrix([0, 1, 0, 0]),
        sp.Matrix([0, 0, 1, 0]),
        sp.Matrix([0, 0, 0, 1]),
        sp.Matrix([3, -2, 5, 7]),
    ):
        w = (x.T * ETA * target)[0] / x_sq
        perpendicular = sp.simplify(target - w * x)
        # K_ab=(Z_perp_a X_b-X_a Z_perp_b)/X^2 with lowered vectors.
        x_low = ETA * x
        p_low = ETA * perpendicular
        k_low = (p_low * x_low.T - x_low * p_low.T) / x_sq
        k_mixed = ETA * k_low
        reconstructed = sp.simplify(k_mixed * x + w * x)
        assert reconstructed == target

    print("PASS: split-jet variation map rank = 4 at exact non-null witness")
    print("PASS: transpose map is injective on all tetrad Euler directions")
    print("PASS: explicit non-null right inverse reconstructs exact targets")


if __name__ == "__main__":
    verify()
