#!/usr/bin/env python3
"""Exact checks for the biquaternionic induced-gravity decision boundary.

The checks keep the canonical variable Theta in C tensor H and its covariant
tetrad.  They do not introduce an independent tetrad, a spinor carrier, or an
auxiliary geometric sector.  The script verifies finite algebra and two independent
evaluations of the periodic-psi heat factor; it does not construct the missing
composite gauge-fixed Hessian or prove a quantum UBT completion.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import shutil
from itertools import permutations
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CHECKS: list[dict[str, object]] = []


def record(identifier: str, channel: str, scope: str, **details: object) -> None:
    CHECKS.append(
        {"id": identifier, "channel": channel, "scope": scope,
         "result": "PASS", **details}
    )


def pairing_signatures() -> None:
    # Coordinates are (Re a, Im a, Re d, Im d, Re b, Im b, Re c, Im c).
    k = sp.zeros(8)
    k[0, 2] = k[2, 0] = 1
    k[1, 3] = k[3, 1] = 1
    for index in range(4, 8):
        k[index, index] = -1

    eigenvalues = k.eigenvals()
    assert eigenvalues == {sp.Integer(-1): 6, sp.Integer(1): 2}

    # X = i*x0*I - i*xk*sigma_k, real x.  This is the canonical W_L slice.
    # Realification in the coordinate order above gives the following map.
    j = sp.Matrix([
        [0, 0, 0, 0],       # Re a
        [1, 0, 0, -1],      # Im a
        [0, 0, 0, 0],       # Re d
        [1, 0, 0, 1],       # Im d
        [0, 0, -1, 0],      # Re b
        [0, -1, 0, 0],      # Im b
        [0, 0, 1, 0],       # Re c
        [0, -1, 0, 0],      # Im c
    ])
    restricted = sp.simplify(j.T * k * j)
    assert restricted == sp.diag(2, -2, -2, -2)
    record(
        "B1", "SymPy exact quadratic-form algebra",
        "Connected-symmetry pairing on generic biquaternions and its Lorentz-real restriction",
        generic_signature=[2, 6], lorentz_slice_signature=[1, 3],
        restricted_matrix=str(restricted.tolist()),
    )


def determinant_hessian() -> None:
    entries = sp.symbols("e0:16")
    e = sp.Matrix(4, 4, entries)  # row mu, column a
    determinant = sp.expand(e.det())
    # W[mu,a,nu,b] is the first-jet Hessian of det(E).
    for mu in range(4):
        for a in range(4):
            for nu in range(4):
                for b in range(4):
                    w = sp.diff(determinant, e[mu, a], e[nu, b])
                    assert sp.simplify(
                        w + sp.diff(determinant, e[nu, a], e[mu, b])
                    ) == 0
                    assert sp.simplify(
                        w + sp.diff(determinant, e[mu, b], e[nu, a])
                    ) == 0

    k = sp.Matrix(sp.symbols("k0:4", real=True))
    for a in range(4):
        for b in range(4):
            principal = sum(
                sp.diff(determinant, e[mu, a], e[nu, b]) * k[mu] * k[nu]
                for mu in range(4) for nu in range(4)
            )
            assert sp.simplify(principal) == 0
    record(
        "B2", "SymPy exact 4D Hessian",
        "Metric-locked volume determinant has doubly antisymmetric first-jet Hessian and zero second-order symbol",
        components_checked=4**4, field_blocks_checked=4**2,
    )


def lorentz_generators() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    boost01 = sp.zeros(4)
    boost01[0, 1] = boost01[1, 0] = 1
    rotation12 = sp.zeros(4)
    rotation12[1, 2], rotation12[2, 1] = 1, -1
    boost02 = sp.zeros(4)
    boost02[0, 2] = boost02[2, 0] = 1
    eta = sp.diag(-1, 1, 1, 1)
    for generator in (boost01, rotation12, boost02):
        assert generator.T * eta + eta * generator == sp.zeros(4)
    return boost01, rotation12, boost02


def covariant_volume_variations() -> None:
    """Compare exterior-curvature formulas with coordinate determinant calculus.

    This nonflat example tests signs, normalization and first/second variations.
    The general result is proved analytically in the paired notes.
    """
    q = sp.symbols("q0:4", real=True)
    c0 = sp.symbols("c0", positive=True)
    x = sp.Matrix([1 + q[0], q[1], q[2], q[3]])
    v = sp.Matrix([q[0]*q[1], q[2]**2 + q[0], q[0]*q[3], q[1] + q[3]**2])
    b01, r12, b02 = lorentz_generators()
    connection = [q[1]*b01, r12, q[0]*b02, sp.zeros(4)]
    e = sp.Matrix(4, 4, lambda mu, a:
                  (sp.diff(x[a], q[mu]) + (connection[mu]*x)[a])/c0)
    dv = sp.Matrix(4, 4, lambda mu, a:
                   sp.diff(v[a], q[mu]) + (connection[mu]*v)[a])
    assert e.det().subs(dict.fromkeys(q, 0)) == c0**(-4)

    # Coordinate channel: differentiate the determinant, then its Euler form.
    cof = e.cofactor_matrix()
    coordinate_euler = sp.Matrix([
        sp.expand(sum(cof[mu, b]*connection[mu][b, a]
                      for mu in range(4) for b in range(4))/c0
                  - sum(sp.diff(cof[mu, a], q[mu]) for mu in range(4))/c0)
        for a in range(4)
    ])
    t = sp.symbols("t")
    varied_cof = (e + t*dv/c0).cofactor_matrix()
    delta_cof = varied_cof.diff(t).subs(t, 0)
    coordinate_jacobi = sp.Matrix([
        sp.expand(sum(delta_cof[mu, b]*connection[mu][b, a]
                      for mu in range(4) for b in range(4))/c0
                  - sum(sp.diff(delta_cof[mu, a], q[mu]) for mu in range(4))/c0)
        for a in range(4)
    ])

    # Independent exterior channel: compute F, then the 2-form wedge 1-form
    # wedge 1-form coefficients.  A 2-form carries the explicit factor 1/2.
    curvature = {
        (mu, nu): connection[nu].diff(q[mu]) - connection[mu].diff(q[nu])
        + connection[mu]*connection[nu] - connection[nu]*connection[mu]
        for mu in range(4) for nu in range(4)
    }
    assert any(f != sp.zeros(4) for f in curvature.values())
    fx = {indices: f*x for indices, f in curvature.items()}
    fv = {indices: f*v for indices, f in curvature.items()}
    exterior_euler = [sp.S.Zero]*4
    exterior_jacobi = [sp.S.Zero]*4
    signed = [(p, sp.LeviCivita(*p)) for p in permutations(range(4))]
    for (a, b, c, d), internal_sign in signed:
        for (mu, nu, rho, sigma), coordinate_sign in signed:
            sign = internal_sign*coordinate_sign
            ee = e[rho, c]*e[sigma, d]
            exterior_euler[a] -= sign*fx[mu, nu][b]*ee/(4*c0**2)
            exterior_jacobi[a] -= (
                sign*fv[mu, nu][b]*ee/(4*c0**2)
                + sign*fx[mu, nu][b]*dv[rho, c]*e[sigma, d]/(2*c0**3)
            )
    for a in range(4):
        assert sp.expand(coordinate_euler[a] - exterior_euler[a]) == 0
        assert sp.expand(coordinate_jacobi[a] - exterior_jacobi[a]) == 0
    assert any(component != 0 for component in coordinate_euler)
    assert any(component != 0 for component in coordinate_jacobi)
    record(
        "B5", "Independent coordinate determinant and exterior-curvature calculations in SymPy",
        "Euler and complete Jacobi formulas on a nonflat Lorentz connection with symbolic c0",
        euler_components=4, jacobi_components=4,
        nondegenerate_origin_determinant=str(c0**(-4)),
        limitation="A polynomial example cross-checks the general analytic proof; it is not a universal formal proof.",
    )


def value_dependent_connection() -> None:
    x = sp.Matrix(sp.symbols("X0:4", real=True))
    p = sp.Matrix(4, 4, sp.symbols("p0:16", real=True))
    b01, r12, b02 = lorentz_generators()
    connection = [x[1]*b01, x[0]*r12, x[2]**2*b02, sp.zeros(4)]
    c0 = sp.Integer(2)
    e = sp.Matrix(4, 4, lambda mu, a:
                  (p[mu, a] + (connection[mu]*x)[a])/c0)
    f = 2 + x.dot(x)
    density = sp.expand(f*e.det(method="domain-ge"))

    # Differentiate the actual composite density, with generic independent
    # first jets, rather than treating C as constant during field variation.
    momentum = [sp.diff(density, entry) for entry in p]
    for a in range(4):
        for b in range(4):
            for mu in range(4):
                for nu in range(mu, 4):
                    second = sp.diff(momentum[4*mu+a], p[nu, b])
                    if mu != nu:
                        second += sp.diff(momentum[4*nu+a], p[mu, b])
                    assert sp.expand(second) == 0

    # A nonzero discrepancy from the frozen-connection derivative confirms
    # that this example genuinely includes a field-dependent connection.
    values = {x[a]: a+1 for a in range(4)}
    values.update({p[mu, a]: int(mu == a)
                   for mu in range(4) for a in range(4)})
    a = 1
    full = sp.diff(density, x[a]).subs(values)
    frozen = sp.diff(f, x[a])*e.det(method="domain-ge") + sum(
        momentum[4*mu+b]*connection[mu][b, a]
        for mu in range(4) for b in range(4)
    )
    discrepancy = sp.simplify(full - frozen.subs(values))
    assert discrepancy != 0
    record(
        "B6", "SymPy differentiation of a nonlinear value-dependent Lorentz connection",
        "All symmetric second-jet coefficients vanish with induced C variations and an algebraic prefactor",
        symmetric_second_jet_blocks=16*10,
        full_minus_frozen_field_derivative=str(discrepancy),
        limitation="The unrestricted proof for every smooth C(x,X) and f(x,X) is in Lemma B-VAL.",
    )


def composite_chain_rule() -> None:
    # A 2x2 block in a 4x4 tetrad with the other diagonal entries fixed to 1.
    # This is an algebraic diagnostic, not a proposed UBT connection.
    s, t = sp.symbols("s t", real=True)
    z = sp.Matrix(sp.symbols("z0:4"))
    determinant = z[0]*z[3] - z[1]*z[2]
    substitution = sp.Matrix([1+s**2, s*t, s, 1+t])
    mapping = dict(zip(z, substitution))
    jacobian = substitution.jacobian([s, t])
    first = jacobian.T*sp.hessian(determinant, z)*jacobian
    second = sp.zeros(2)
    for i in range(4):
        second += sp.diff(determinant, z[i]).subs(mapping)*sp.hessian(substitution[i], [s, t])
    direct = sp.hessian(determinant.subs(mapping), [s, t])
    assert sp.simplify(direct - first - second) == sp.zeros(2)
    assert sp.simplify(second) != sp.zeros(2)
    record(
        "B7", "Direct composite determinant versus two-term Hessian chain rule",
        "Omitting the tetrad second-variation term changes the Hessian",
        direct_hessian=str(direct.tolist()),
        limitation="An algebraic first-jet example; no canonical connection or elliptic UBT operator is selected.",
    )


def heat_factor_and_coefficients() -> None:
    mp.mp.dps = 60

    def theta_integrand(u: mp.mpf) -> mp.mpf:
        return mp.jtheta(3, 0, mp.e**(-u)) / (u*u)

    integral = mp.quad(theta_integrand, [1, mp.inf])
    series = mp.mpf(1)
    for n in range(1, 40):
        nn = mp.mpf(n*n)
        series += 2 * (mp.e**(-nn) - nn * mp.e1(nn))
    assert abs(integral - series) < mp.mpf("1e-50")
    nmax = 39
    tail_bound = (2*mp.exp(-(nmax+1)**2) /
                  ((nmax+1)**2*(1-mp.exp(-(2*nmax+3)))))
    assert 0 < tail_bound < mp.mpf("1e-690")

    expected = mp.mpf("1.303410251859279308")
    assert abs(integral - expected) < mp.mpf("5e-19")

    ratio8 = mp.sqrt(8 * integral / (96 * mp.pi**2))
    ratio4 = mp.sqrt(4 * integral / (96 * mp.pi**2))
    assert abs(ratio8 / ratio4 - mp.sqrt(2)) < mp.mpf("1e-50")

    xi = sp.symbols("xi", real=True)
    weight = 1 - 6 * xi
    assert weight.subs(xi, sp.Rational(1, 6)) == 0
    assert weight.subs(xi, 0) == 1
    record(
        "B3", "mpmath quadrature plus independent convergent series",
        "Periodic-psi self-dual heat factor and conditional Planck ratios",
        C_psi=mp.nstr(integral, 35),
        planck_ratio_N8=mp.nstr(ratio8, 20),
        planck_ratio_N4=mp.nstr(ratio4, 20),
        absolute_difference=mp.nstr(abs(integral-series), 8),
        analytic_series_tail_bound=mp.nstr(tail_bound, 8),
        numerical_note="The tail bound does not certify floating-point quadrature error.",
    )
    record(
        "B4", "SymPy exact coefficient algebra",
        "Scalar-like induced Einstein coefficient need not be nonzero",
        minimal_weight="1", conformal_weight="0",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    pairing_signatures()
    determinant_hessian()
    heat_factor_and_coefficients()
    covariant_volume_variations()
    value_dependent_connection()
    composite_chain_rule()

    paths = [
        "tools/verify_biquaternionic_induced_gravity_boundary.py",
        "canonical/gr_closure/gap_10d_induced_gravity_endgame.tex",
        "canonical/gr_closure/gap_10d_theta_hessian_principal_symbol.tex",
        "research_tracks/action_selection/biquaternionic_induced_gravity_boundary.en.md",
        "research_tracks/action_selection/biquaternionic_induced_gravity_boundary.cs.md",
        "tests/test_biquaternionic_induced_gravity_boundary.py",
    ]
    report = {
        "schema": "ubt-verification/v1",
        "date": "2026-09-09",
        "base_commit": "98fbc114f8dfcd88d8dbc24614b555f80f04ffeb",
        "result": "PASS",
        "check_groups": len(CHECKS),
        "checks": CHECKS,
        "tools": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
        },
        "lean": {
            "status": "LEAN-PENDING",
            "lean_available": bool(shutil.which("lean")),
            "lake_available": bool(shutil.which("lake")),
            "reason": "No compiled Lean proof; Lean and Lake are absent in the inspected runtime.",
        },
        "source_sha256": {
            path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            for path in paths
        },
        "limitations": [
            "The finite checks do not construct the full composite gauge-fixed Theta Hessian or its functional measure.",
            "The heat coefficient applies only to the stated scalar-like bosonic Laplace operators and proper-time prescription.",
            "The signature calculation does not choose a Euclidean integration contour or identify physical and gauge modes.",
            "The Lorentz-real four-component volume lemmas do not classify all eight real biquaternionic fluctuation directions.",
            "No Newton constant, microscopic gravitational action, full UBT closure, or RH theorem is claimed.",
        ],
        "canonical_claim_status_changes": [],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    for check in CHECKS:
        print(f"PASS {check['id']}: {check['scope']}")
    print(f"{len(CHECKS)} groups passed; LEAN-PENDING.")


if __name__ == "__main__":
    main()
