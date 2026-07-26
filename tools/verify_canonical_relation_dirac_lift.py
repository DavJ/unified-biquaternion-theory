#!/usr/bin/env python3
"""Exact verifier for the canonical UBT relation and its Clifford/Dirac lift.

Scope:
- exact Lorentz-slice central metric identity;
- exact injective 4x4 block Clifford lift;
- exact tetrad-to-metric rank 10 and six-dimensional Lorentz kernel;
- exact fifth/grading channel anticommutation;
- exact four- and five-channel principal-symbol factorisation;
- exact conditional psi-normal-form solvability;
- exact constrained-rank projection criterion and rank-budget no-go.

This does not prove the generalized UBT equation of motion, curved implicit
existence, the actual holomorphic on-shell Jacobian, or Einstein dynamics.
"""
from __future__ import annotations

import sympy as sp

I = sp.I
I2 = sp.eye(2)
I4 = sp.eye(4)
Z2 = sp.zeros(2)
ETA = sp.diag(-1, 1, 1, 1)
PAIRS = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]

SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
QUNIT = tuple(-I * sigma for sigma in SIGMA)


def lorentz_biquaternion(v: sp.Matrix) -> sp.Matrix:
    """Return i*v0*1 + vk*e_k in the Pauli representation."""
    if v.shape != (4, 1):
        raise ValueError("v must be a 4x1 column")
    return I * v[0] * I2 + sum((v[k + 1] * QUNIT[k] for k in range(3)), sp.zeros(2))


def sharp(q: sp.Matrix) -> sp.Matrix:
    """Quaternion conjugation on Mat(2,C): q^sharp = Tr(q) I - q."""
    if q.shape != (2, 2):
        raise ValueError("q must be 2x2")
    return sp.trace(q) * I2 - q


def clifford_lift(q: sp.Matrix) -> sp.Matrix:
    """Injective off-diagonal lift C(q) into Mat(4,C)."""
    return sp.Matrix.vstack(
        sp.Matrix.hstack(Z2, q),
        sp.Matrix.hstack(sharp(q), Z2),
    )


def exact_lorentz_and_clifford_checks() -> dict[str, sp.Expr | int]:
    e0, e1, e2, e3, f0, f1, f2, f3 = sp.symbols(
        "e0 e1 e2 e3 f0 f1 f2 f3", real=True
    )
    ev = sp.Matrix([e0, e1, e2, e3])
    fv = sp.Matrix([f0, f1, f2, f3])
    e = lorentz_biquaternion(ev)
    f = lorentz_biquaternion(fv)
    h = (ev.T * ETA * fv)[0]

    central_lower = sp.simplify((sharp(e) * f + sharp(f) * e) / 2 - h * I2)
    central_upper = sp.simplify((e * sharp(f) + f * sharp(e)) / 2 - h * I2)
    ge = clifford_lift(e)
    gf = clifford_lift(f)
    clifford = sp.simplify((ge * gf + gf * ge) / 2 - h * I4)

    grading = sp.diag(1, 1, -1, -1)
    grading_anti_e = sp.simplify(grading * ge + ge * grading)
    grading_anti_f = sp.simplify(grading * gf + gf * grading)

    # Injectivity is visible from the upper-right block. Check it exactly for a
    # symbolic Lorentz vector by recovering the original matrix.
    recovered = ge[:2, 2:4]

    return {
        "lower_central_residual_rank": central_lower.rank(),
        "upper_central_residual_rank": central_upper.rank(),
        "clifford_residual_rank": clifford.rank(),
        "grading_anticommutator_e_rank": grading_anti_e.rank(),
        "grading_anticommutator_f_rank": grading_anti_f.rank(),
        "grading_square_residual_rank": (grading * grading - I4).rank(),
        "timelike_fifth_square_residual_rank": ((I * grading) ** 2 + I4).rank(),
        "lift_recovery_residual_rank": sp.simplify(recovered - e).rank(),
    }



def canonical_basis_gammas() -> tuple[sp.Matrix, ...]:
    """Return the four exact lower-index Clifford generators."""
    basis = []
    for a in range(4):
        v = sp.zeros(4, 1)
        v[a] = 1
        basis.append(clifford_lift(lorentz_biquaternion(v)))
    return tuple(basis)


def exact_principal_symbol_checks() -> dict[str, sp.Expr | int]:
    """Verify the metric and fifth-channel symbols by exact polynomial algebra."""
    p0, p1, p2, p3, ppsi = sp.symbols(
        "p0 p1 p2 p3 ppsi", real=True
    )
    momenta = (p0, p1, p2, p3)
    gammas = canonical_basis_gammas()
    symbol4 = sum(
        (momenta[a] * gammas[a] for a in range(4)),
        sp.zeros(4),
    )
    q4 = -p0**2 + p1**2 + p2**2 + p3**2
    grading = sp.diag(1, 1, -1, -1)
    symbol5_space = symbol4 + ppsi * grading
    symbol5_time = symbol4 + ppsi * I * grading

    return {
        "flat_basis_clifford_residual_rank": max(
            (
                (gammas[a] * gammas[b] + gammas[b] * gammas[a]
                 - 2 * ETA[a, b] * I4).rank()
                for a in range(4)
                for b in range(4)
            ),
            default=0,
        ),
        "four_symbol_square_residual_rank": sp.simplify(
            symbol4 * symbol4 - q4 * I4
        ).rank(),
        "four_symbol_determinant_residual": sp.factor(
            symbol4.det() - q4**2
        ),
        "five_space_symbol_square_residual_rank": sp.simplify(
            symbol5_space * symbol5_space - (q4 + ppsi**2) * I4
        ).rank(),
        "five_time_symbol_square_residual_rank": sp.simplify(
            symbol5_time * symbol5_time - (q4 - ppsi**2) * I4
        ).rank(),
        "five_space_symbol_determinant_residual": sp.factor(
            symbol5_space.det() - (q4 + ppsi**2) ** 2
        ),
        "five_time_symbol_determinant_residual": sp.factor(
            symbol5_time.det() - (q4 - ppsi**2) ** 2
        ),
    }


def exact_psi_normal_form_checks() -> dict[str, sp.Expr | int]:
    """Verify exact pointwise solvability in the independent psi derivative."""
    f = sp.Matrix(sp.symbols("f0:4"))
    grading = sp.diag(1, 1, -1, -1)
    checks: dict[str, sp.Expr | int] = {}
    for name, gamma_psi, epsilon in (
        ("space", grading, sp.Integer(1)),
        ("time", I * grading, sp.Integer(-1)),
    ):
        inverse = epsilon * gamma_psi
        solution = -inverse * f
        checks[f"{name}_inverse_left_residual_rank"] = (
            inverse * gamma_psi - I4
        ).rank()
        checks[f"{name}_inverse_right_residual_rank"] = (
            gamma_psi * inverse - I4
        ).rank()
        checks[f"{name}_normal_solution_residual_rank"] = sp.simplify(
            gamma_psi * solution + f
        ).rank()
    return checks

def metric_components(e: sp.Matrix) -> sp.Matrix:
    g = e * ETA * e.T
    return sp.Matrix([g[mu, nu] for mu, nu in PAIRS])


def tetrad_jacobian_at_identity() -> tuple[sp.Matrix, list[sp.Symbol]]:
    symbols = list(sp.symbols("e00:04 e10:14 e20:24 e30:34", real=True))
    # SymPy's compact naming above produces 16 variables in row order.
    if len(symbols) != 16:
        raise RuntimeError(f"unexpected symbol count: {len(symbols)}")
    e = sp.Matrix(4, 4, symbols)
    jac = metric_components(e).jacobian(symbols)
    identity_subs = {
        symbols[4 * mu + a]: sp.Integer(1 if mu == a else 0)
        for mu in range(4)
        for a in range(4)
    }
    return sp.simplify(jac.subs(identity_subs)), symbols


def lorentz_generators() -> list[sp.Matrix]:
    generators: list[sp.Matrix] = []
    # Spatial rotations: X^i_j = +1, X^j_i = -1.
    for i, j in ((1, 2), (1, 3), (2, 3)):
        x = sp.zeros(4)
        x[i, j] = 1
        x[j, i] = -1
        generators.append(x)
    # Boosts for eta=(-,+,+,+): X^0_i = X^i_0 = 1.
    for i in (1, 2, 3):
        x = sp.zeros(4)
        x[0, i] = 1
        x[i, 0] = 1
        generators.append(x)
    return generators


def exact_rank_checks() -> dict[str, int]:
    jac, _ = tetrad_jacobian_at_identity()
    generators = lorentz_generators()
    kernel_columns = [sp.Matrix(list(x)) for x in generators]
    kernel = sp.Matrix.hstack(*kernel_columns)

    lorentz_condition_residual = max(
        (x * ETA + ETA * x.T).rank() for x in generators
    )
    jac_kernel_residual = (jac * kernel).rank()

    # Verify a right inverse for all ten symmetric metric basis variations at
    # the identity tetrad. Formula: delta e = 1/2 h g^{-1} e = 1/2 h eta.
    right_inverse_residual = 0
    for column, (mu, nu) in enumerate(PAIRS):
        h = sp.zeros(4)
        h[mu, nu] = 1
        h[nu, mu] = 1
        if mu == nu:
            h[mu, nu] = 1
        delta_e = sp.Rational(1, 2) * h * ETA
        produced = jac * sp.Matrix(list(delta_e))
        target = sp.zeros(10, 1)
        target[column] = 1
        right_inverse_residual = max(
            right_inverse_residual, (produced - target).rank()
        )

    return {
        "metric_jacobian_rank": int(jac.rank()),
        "metric_jacobian_nullity": int(16 - jac.rank()),
        "lorentz_kernel_rank": int(kernel.rank()),
        "lorentz_condition_residual_rank": int(lorentz_condition_residual),
        "jacobian_on_lorentz_kernel_residual_rank": int(jac_kernel_residual),
        "right_inverse_residual_rank": int(right_inverse_residual),
    }



def exact_constraint_projection_checks() -> dict[str, int]:
    """Verify the linear-algebra projection criterion for constrained rank.

    Let e contain the 16 real tetrad coefficients, z auxiliary/non-metric
    first-jet variables, and F(e,z)=0 the real constraint system.  If the
    Jacobian with respect to z is surjective, every tetrad variation can be
    lifted to a tangent variation of the constraint surface, so the metric
    rank remains ten.  Conversely, eight independent constraints acting only
    on e leave an at-most-eight-dimensional tangent space and cannot support
    metric rank ten.

    The universal statements are proved in the accompanying text.  The exact
    matrices below verify the block construction and the rank budget without
    floating arithmetic.
    """
    metric_jac, _ = tetrad_jacobian_at_identity()

    # Eight real equations, with eight auxiliary variables.  B=I_8 is
    # surjective, so for every delta e one may choose delta z=-A delta e.
    a = sp.Matrix(8, 16, lambda i, j: ((i + 2 * j + 1) % 5) - 2)
    b = sp.eye(8)
    constraint = a.row_join(b)
    tangent_lift = sp.Matrix.vstack(sp.eye(16), -a)  # (delta e, delta z)
    metric_on_lift = metric_jac * tangent_lift[:16, :]

    # Eight independent real constraints on tetrad variables alone.  Their
    # tangent space has dimension eight, hence any restricted metric map has
    # rank at most eight.  The chosen coordinate model makes the bound exact
    # and readily checkable.
    tetrad_only = sp.eye(8).row_join(sp.zeros(8, 8))
    tetrad_only_tangent = sp.Matrix.vstack(sp.zeros(8, 8), sp.eye(8))
    restricted_metric = metric_jac * tetrad_only_tangent

    return {
        "auxiliary_constraint_rank": int(constraint.rank()),
        "auxiliary_block_rank": int(b.rank()),
        "lifted_tangent_rank": int(tangent_lift.rank()),
        "constraint_on_lift_residual_rank": int((constraint * tangent_lift).rank()),
        "metric_rank_on_lift": int(metric_on_lift.rank()),
        "tetrad_only_constraint_rank": int(tetrad_only.rank()),
        "tetrad_only_tangent_rank": int(tetrad_only_tangent.rank()),
        "tetrad_only_residual_rank": int((tetrad_only * tetrad_only_tangent).rank()),
        "tetrad_only_metric_rank": int(restricted_metric.rank()),
    }

def assert_expected() -> dict[str, dict[str, sp.Expr | int]]:
    algebra = exact_lorentz_and_clifford_checks()
    assert all(value == 0 for value in algebra.values())

    principal = exact_principal_symbol_checks()
    assert all(value == 0 for value in principal.values())

    psi_normal = exact_psi_normal_form_checks()
    assert all(value == 0 for value in psi_normal.values())

    projection = exact_constraint_projection_checks()
    assert projection["auxiliary_constraint_rank"] == 8
    assert projection["auxiliary_block_rank"] == 8
    assert projection["lifted_tangent_rank"] == 16
    assert projection["constraint_on_lift_residual_rank"] == 0
    assert projection["metric_rank_on_lift"] == 10
    assert projection["tetrad_only_constraint_rank"] == 8
    assert projection["tetrad_only_tangent_rank"] == 8
    assert projection["tetrad_only_residual_rank"] == 0
    assert projection["tetrad_only_metric_rank"] <= 8

    rank = exact_rank_checks()
    assert rank["metric_jacobian_rank"] == 10
    assert rank["metric_jacobian_nullity"] == 6
    assert rank["lorentz_kernel_rank"] == 6
    assert rank["lorentz_condition_residual_rank"] == 0
    assert rank["jacobian_on_lorentz_kernel_residual_rank"] == 0
    assert rank["right_inverse_residual_rank"] == 0
    return {
        "algebra": algebra,
        "principal_symbol": principal,
        "psi_normal_form": psi_normal,
        "constraint_projection": projection,
        "rank": rank,
    }


def main() -> None:
    results = assert_expected()
    print("Canonical UBT relation -> Clifford/Dirac lift verifier")
    print("=" * 58)
    for section, checks in results.items():
        print(f"[{section}]")
        for name, value in checks.items():
            print(f"PASS  {name:48s} {value}")
    print("\nAll checks are exact SymPy algebra; no floating tolerance is used.")
    print(
        "Scope: exact kinematic algebra, causal symbol, conditional psi-normal "
        "form, constrained-rank projection criterion, and E->g rank. The "
        "actual holomorphic/full on-shell Jacobian remains open."
    )


if __name__ == "__main__":
    main()
