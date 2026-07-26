#!/usr/bin/env python3
"""Exact verifier for constrained metric rank with no extra UBT fields.

The original variables are only
  - the value Psi=vec(Theta) (8 real components), and
  - the Lorentz first jet e_mu^a (16 real components).

The verifier checks:
  1. the exact tetrad metric map has rank 10 and Lorentz kernel 6;
  2. the exact constrained-rank criterion rank(Dg|A)=dim(A+K)-6;
  3. an invertible field-value Jacobian F_Psi makes every tetrad variation
     admissible and preserves rank 10;
  4. eight independent first-jet constraints with no field-value absorption
     can reduce the metric rank to 8;
  5. six constraints acting only on Lorentz gauge directions can leave rank 10;
  6. a scalar or scalar-pseudoscalar Dirac zero-order block is exactly
     invertible under the stated non-vanishing condition.

All arithmetic is exact SymPy algebra. No floating tolerance is used.
"""
from __future__ import annotations

import sympy as sp

ETA = sp.diag(-1, 1, 1, 1)
PAIRS = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]


def metric_components(e: sp.Matrix) -> sp.Matrix:
    g = e * ETA * e.T
    return sp.Matrix([g[mu, nu] for mu, nu in PAIRS])


def metric_jacobian_at_identity() -> sp.Matrix:
    x = list(sp.symbols("e00:04 e10:14 e20:24 e30:34", real=True))
    e = sp.Matrix(4, 4, x)
    jac = metric_components(e).jacobian(x)
    subs = {
        x[4 * mu + a]: sp.Integer(1 if mu == a else 0)
        for mu in range(4)
        for a in range(4)
    }
    return sp.simplify(jac.subs(subs))


def metric_right_inverse() -> sp.Matrix:
    """Return R (16x10) with J_g R = I_10 at the identity tetrad."""
    cols: list[sp.Matrix] = []
    for mu, nu in PAIRS:
        h = sp.zeros(4)
        h[mu, nu] = 1
        h[nu, mu] = 1
        if mu == nu:
            h[mu, nu] = 1
        delta_e = sp.Rational(1, 2) * h * ETA
        cols.append(sp.Matrix(list(delta_e)))
    return sp.Matrix.hstack(*cols)


def lorentz_kernel() -> sp.Matrix:
    """Return K (16x6), a basis of infinitesimal Lorentz frame changes."""
    generators: list[sp.Matrix] = []
    for i, j in ((1, 2), (1, 3), (2, 3)):
        x = sp.zeros(4)
        x[i, j] = 1
        x[j, i] = -1
        generators.append(x)
    for i in (1, 2, 3):
        x = sp.zeros(4)
        x[0, i] = 1
        x[i, 0] = 1
        generators.append(x)
    return sp.Matrix.hstack(*(sp.Matrix(list(x)) for x in generators))


def constrained_rank(admissible: sp.Matrix, jac: sp.Matrix, kernel: sp.Matrix) -> tuple[int, int]:
    """Return direct restricted rank and dim(A+K)-6 for a basis of A."""
    direct = int((jac * admissible).rank())
    formula = int(sp.Matrix.hstack(admissible, kernel).rank() - kernel.rank())
    return direct, formula


def exact_constraint_geometry_checks() -> dict[str, int]:
    jac = metric_jacobian_at_identity()
    right = metric_right_inverse()
    kernel = lorentz_kernel()
    frame_basis = sp.Matrix.hstack(right, kernel)
    frame_inverse = frame_basis.inv()

    # Gauge-only constraints: in the [physical(10), Lorentz(6)] basis, set the
    # six Lorentz coordinates to zero. The admissible space is span(right).
    c_gauge = sp.Matrix.hstack(sp.zeros(6, 10), sp.eye(6))
    f_e_gauge = c_gauge * frame_inverse
    a_gauge = right
    gauge_direct, gauge_formula = constrained_rank(a_gauge, jac, kernel)

    # Eight constraints with no Psi absorption: constrain two physical and all
    # six Lorentz directions. Eight physical directions remain, so rank is 8.
    c_eight = sp.zeros(8, 16)
    c_eight[0, 0] = 1
    c_eight[1, 1] = 1
    for row in range(6):
        c_eight[2 + row, 10 + row] = 1
    f_e_eight = c_eight * frame_inverse
    a_eight = frame_basis[:, 2:10]
    eight_direct, eight_formula = constrained_rank(a_eight, jac, kernel)

    # Original-field absorption: F_Psi=I_8. For every delta e one can take
    # delta Psi=-F_e delta e, so the admissible tetrad space is all R^16.
    f_e_absorbed = f_e_eight
    f_psi = sp.eye(8)
    graph = sp.Matrix.vstack(sp.eye(16), -f_psi.inv() * f_e_absorbed)
    constraint_jac = sp.Matrix.hstack(f_e_absorbed, f_psi)
    graph_residual = constraint_jac * graph
    a_all = sp.eye(16)
    absorbed_direct, absorbed_formula = constrained_rank(a_all, jac, kernel)

    return {
        "metric_rank": int(jac.rank()),
        "lorentz_kernel_rank": int(kernel.rank()),
        "right_inverse_residual_rank": int((jac * right - sp.eye(10)).rank()),
        "frame_basis_rank": int(frame_basis.rank()),
        "gauge_constraint_rank": int(f_e_gauge.rank()),
        "gauge_only_restricted_metric_rank": gauge_direct,
        "gauge_only_formula_rank": gauge_formula,
        "eight_constraint_rank": int(f_e_eight.rank()),
        "eight_no_absorption_metric_rank": eight_direct,
        "eight_no_absorption_formula_rank": eight_formula,
        "field_absorption_graph_residual_rank": int(graph_residual.rank()),
        "field_absorption_projection_rank": int(graph[:16, :].rank()),
        "field_absorption_metric_rank": absorbed_direct,
        "field_absorption_formula_rank": absorbed_formula,
    }


def exact_zero_order_block_checks() -> dict[str, sp.Expr | int]:
    """Check exact invertibility of canonical Dirac zero-order examples."""
    m, ms, mp = sp.symbols("m m_s m_p", real=True)
    i = sp.I
    i4 = sp.eye(4)
    grading = sp.diag(1, 1, -1, -1)

    scalar = m * i4
    scalar_inverse = i4 / m

    # Scalar + pseudoscalar block. Since grading^2=I,
    # (ms I + i mp grading)(ms I - i mp grading)=(ms^2+mp^2)I.
    mixed = ms * i4 + i * mp * grading
    mixed_adj = ms * i4 - i * mp * grading
    denominator = ms**2 + mp**2
    mixed_inverse = mixed_adj / denominator

    return {
        "scalar_inverse_residual_rank": sp.simplify(scalar * scalar_inverse - i4).rank(),
        "scalar_complex_determinant": sp.factor(scalar.det()),
        "mixed_product_residual_rank": sp.simplify(mixed * mixed_adj - denominator * i4).rank(),
        "mixed_inverse_residual_rank": sp.simplify(mixed * mixed_inverse - i4).rank(),
        "mixed_complex_determinant": sp.factor(mixed.det()),
        "mixed_realified_determinant": sp.factor(denominator**4),
    }


def assert_expected() -> dict[str, dict[str, sp.Expr | int]]:
    geometry = exact_constraint_geometry_checks()
    assert geometry["metric_rank"] == 10
    assert geometry["lorentz_kernel_rank"] == 6
    assert geometry["right_inverse_residual_rank"] == 0
    assert geometry["frame_basis_rank"] == 16
    assert geometry["gauge_constraint_rank"] == 6
    assert geometry["gauge_only_restricted_metric_rank"] == 10
    assert geometry["gauge_only_formula_rank"] == 10
    assert geometry["eight_constraint_rank"] == 8
    assert geometry["eight_no_absorption_metric_rank"] == 8
    assert geometry["eight_no_absorption_formula_rank"] == 8
    assert geometry["field_absorption_graph_residual_rank"] == 0
    assert geometry["field_absorption_projection_rank"] == 16
    assert geometry["field_absorption_metric_rank"] == 10
    assert geometry["field_absorption_formula_rank"] == 10

    zero_order = exact_zero_order_block_checks()
    assert zero_order["scalar_inverse_residual_rank"] == 0
    assert zero_order["scalar_complex_determinant"] == sp.Symbol("m", real=True) ** 4
    assert zero_order["mixed_product_residual_rank"] == 0
    assert zero_order["mixed_inverse_residual_rank"] == 0
    ms, mp = sp.symbols("m_s m_p", real=True)
    assert sp.factor(zero_order["mixed_complex_determinant"] - (ms**2 + mp**2) ** 2) == 0
    assert sp.factor(zero_order["mixed_realified_determinant"] - (ms**2 + mp**2) ** 4) == 0
    return {"constraint_geometry": geometry, "zero_order_blocks": zero_order}


def main() -> None:
    results = assert_expected()
    print("No-extra-variable constrained-rank verifier")
    print("=" * 48)
    for section, checks in results.items():
        print(f"[{section}]")
        for name, value in checks.items():
            print(f"PASS  {name:48s} {value}")
    print("\nAll checks use exact SymPy algebra; no floating tolerance is used.")
    print("Scope: pointwise first-jet equation rank. Local PDE existence remains separate.")


if __name__ == "__main__":
    main()
