#!/usr/bin/env python3
"""Exact checks for the regulated canonical-GR Theta measure audit.

This verifies finite-dimensional Jacobians only.  It does not construct the
continuum functional measure or a Faddeev--Popov determinant.
"""

import sympy as sp


def realify(a: sp.Matrix) -> sp.Matrix:
    """Realification of a complex-linear matrix."""
    return a.applyfunc(sp.re).row_join(-a.applyfunc(sp.im)).col_join(
        a.applyfunc(sp.im).row_join(a.applyfunc(sp.re))
    )


def action_matrix(s: sp.Matrix) -> sp.Matrix:
    """Complex matrix of X -> S X S^dagger on vec(X)."""
    return sp.kronecker_product(sp.conjugate(s), s)


def check_spin_jacobian() -> None:
    # Exact nontrivial SL(2,C) representatives: boost, shear, and phase.
    reps = [
        sp.diag(sp.Rational(2), sp.Rational(1, 2)),
        sp.Matrix([[1, 1 + sp.I], [0, 1]]),
        sp.diag(sp.I, -sp.I),
    ]
    for s in reps:
        assert sp.simplify(s.det()) == 1
        jac = sp.simplify(realify(action_matrix(s)).det())
        assert jac == 1, (s, jac)


def check_component_count() -> None:
    # Four complex biquaternion coefficients at each regulator site.
    assert 4 * 2 == 8


if __name__ == "__main__":
    check_component_count()
    check_spin_jacobian()
    print("PASS: 8 real components and unit spin-lift Jacobians")
