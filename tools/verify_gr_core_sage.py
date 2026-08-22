#!/usr/bin/env -S sage -python
"""Independent SageMath checks for theorem-critical UBT GR algebra.

This file intentionally uses Sage native exact matrices and its GSL-backed
quadrature rather than importing the SymPy verifier implementation.  It checks
finite-dimensional algebra and a numerical heat-trace constant only.  It does
not derive the UBT action, prove PDE existence, or close GAP-U2Theta/GAP-10D.
"""

from itertools import combinations
import math

from sage.all import I, QQ, PolynomialRing, exp, function, matrix, numerical_integral, var


def metric_rank_check():
    """Rank of de -> de*eta + eta*de^T at the identity tetrad."""
    eta = [-1, 1, 1, 1]
    rows = []
    for mu in range(4):
        for nu in range(mu, 4):
            row = [QQ(0)] * 16
            row[4 * mu + nu] += eta[nu]
            row[4 * nu + mu] += eta[mu]
            rows.append(row)
    jacobian = matrix(QQ, rows)
    assert jacobian.rank() == 10
    assert jacobian.right_kernel().dimension() == 6


def contortion_rank_check():
    """Exact rank of the metric-compatible contortion-to-torsion map."""
    pairs = list(combinations(range(4), 2))
    domain = [(a, b, c) for a, b in pairs for c in range(4)]
    codomain = [(a, c, d) for a in range(4) for c, d in pairs]
    index = {entry: i for i, entry in enumerate(domain)}

    def coefficient(a, b, c):
        if a == b:
            return None, 0
        if a < b:
            return index[(a, b, c)], 1
        return index[(b, a, c)], -1

    transform = matrix(QQ, 24, 24)
    for row, (a, c, d) in enumerate(codomain):
        column, sign = coefficient(a, d, c)
        if column is not None:
            transform[row, column] += sign
        column, sign = coefficient(a, c, d)
        if column is not None:
            transform[row, column] -= sign
    assert transform.rank() == 24


def legacy_schwarzschild_boundary_check():
    """Exact witnesses invalidating the old full-Schwarzschild promotion."""
    ring = PolynomialRing(QQ, names=("r", "M"))
    r, mass = ring.gens()
    field = ring.fraction_field()
    r, mass = field(r), field(mass)
    psi_factor = 1 + mass / (2 * r)
    g_prime = 1 - mass**2 / (4 * r**2)
    f_prime_squared = psi_factor**2 * 2 * mass / r
    assert f_prime_squared + g_prime**2 == psi_factor**4

    # At M=1, r=2M on the positive x-axis, the scalar coefficient of
    # partial_x Theta is f'=5/4: real and nonzero, hence outside W_L.
    assert psi_factor(M=1, r=2) == QQ(5) / 4
    assert f_prime_squared(M=1, r=2) == (QQ(5) / 4) ** 2

    # The claimed unit norm is already impossible because the vector
    # coefficient g=r*Psi^2 alone exceeds one at the same exact point.
    radial_g = r * psi_factor**2
    assert radial_g(M=1, r=2) == QQ(25) / 8
    assert radial_g(M=1, r=2) ** 2 > 1


def legacy_phase_derivative_check():
    """Symbolically expose the missing psi and radial-phase derivatives."""
    rho, psi = var("rho psi")
    alpha = function("alpha")(rho)
    radial_field = function("X")(rho)
    theta = exp(I * alpha) * radial_field

    # The displayed historical ansatz has no psi argument.
    assert theta.diff(psi) == 0

    # A nonconstant radial phase contributes the second product-rule term.
    expected = exp(I * alpha) * (
        radial_field.diff(rho) + I * alpha.diff(rho) * radial_field
    )
    assert (theta.diff(rho) - expected).simplify_full() == 0


def cpsi_gsl_quadrature_check():
    """Independent GSL quadrature for the self-dual KK heat-trace factor."""
    def integrand(u):
        theta3 = 1.0 + 2.0 * sum(math.exp(-(n * n) * u) for n in range(1, 13))
        return theta3 / (u * u)

    # Integrate to 50 and add the exact zero-mode tail int_50^inf u^-2 du.
    # The omitted nonzero-mode tail is below 1e-23.
    value, error = numerical_integral(integrand, 1.0, 50.0)
    value += 1.0 / 50.0
    expected = 1.3034102518592793083762365147875847838216766094408744
    assert abs(value - expected) < 2e-9
    assert error < 2e-9


def main():
    metric_rank_check()
    contortion_rank_check()
    legacy_schwarzschild_boundary_check()
    legacy_phase_derivative_check()
    cpsi_gsl_quadrature_check()
    print("SAGEMATH GR CORE AUDIT: ALL CHECKS PASSED")
    print("  exact metric differential: rank 10, kernel 6")
    print("  exact K-to-T map: rank 24")
    print("  legacy Schwarzschild ansatz: missing psi/phase terms exposed exactly")
    print("  legacy Schwarzschild identity: spatial-only and outside canonical W_L")
    print("  self-dual KK factor: independent Sage/GSL quadrature")
    print("  NOT TESTED: action selection, PDE/global existence, or unconditional GR")


main()
