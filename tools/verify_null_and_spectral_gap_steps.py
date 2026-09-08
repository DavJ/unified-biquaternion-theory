#!/usr/bin/env python3
"""Exact algebra plus independent numerical checks, not an infinite-dimensional proof.

Run with Python, SymPy, NumPy and SciPy. Optional --output writes a JSON record.
The analytic smooth/PDE/spectral proofs and their hypotheses are in the paired
research notes. No result here proves Einstein dynamics, RH or a UBT action.
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import platform
import shutil
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.special import erf
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
ETA = sp.diag(-1, 1, 1, 1)
ETA_NP = np.diag([-1.0, 1.0, 1.0, 1.0])
CHECKS: list[dict] = []


def record(identifier: str, channel: str, scope: str, **details) -> None:
    CHECKS.append(dict(id=identifier, result="PASS", channel=channel,
                       scope=scope, **details))


def symbolic_zero(matrix) -> None:
    for value in matrix:
        if sp.cancel(value) != 0:
            raise AssertionError(f"Nonzero exact residual: {value}")


def lorentz_basis():
    basis = []
    for a in range(4):
        for b in range(a + 1, 4):
            lower = sp.zeros(4)
            lower[a, b], lower[b, a] = 1, -1
            basis.append(ETA * lower)
    return basis


def exact_null_checks() -> None:
    x0 = sp.Symbol("x0", real=True, nonzero=True)
    x1, x2, x3, w = sp.symbols("x1 x2 x3 w", real=True)
    x = sp.Matrix([x0, x1, x2, x3])
    basis = lorentz_basis()
    coeffs = sp.symbols("k0:6", real=True)
    original = sum((c * b for c, b in zip(coeffs, basis)), sp.zeros(4))
    z = original * x + w * x
    chi = (x.T * ETA * x)[0]
    r = (x.T * ETA * z)[0]
    assert sp.expand(r - w * chi) == 0
    y = sp.Matrix([-1 / x0, 0, 0, 0])
    u = z - w * x
    candidate = u * (ETA * y).T - y * (ETA * u).T
    symbolic_zero(candidate.T * ETA + ETA * candidate)
    symbolic_zero(candidate * x + w * x - z)
    # This representative only needs a nonzero local component, not chi != 0.
    for value in candidate:
        denominator = sp.denom(sp.cancel(value))
        assert not denominator.has(x1, x2, x3)
    record("N1", "SymPy exact rational functions",
           "General Lorentz tensor, contraction, antisymmetry and dual-vector reconstruction in x0 != 0 chart")

    cases = [(sp.Matrix([2, 0, 0, 0]), 4),
             (sp.Matrix([0, 2, 1, 0]), 4),
             (sp.Matrix([1, 1, 0, 0]), 3),
             (sp.zeros(4, 1), 0)]
    for vector, rank in cases:
        linear_map = sp.Matrix.hstack(*(b * vector for b in basis), vector)
        assert linear_map.rank() == rank
        if rank == 3:
            symbolic_zero(linear_map.T * ETA * vector)
            assert len(linear_map.T.nullspace()) == 1
    record("N3", "SymPy exact linear algebra",
           "Timelike, spacelike, nonzero-null and zero witnesses; null multiplier direction",
           ranks=[4, 4, 3, 0])

    v = sp.Symbol("v", real=True)
    x_bad, z_bad = sp.Matrix([1, 1, v, 0]), sp.Matrix([0, 0, 1, 0])
    chi_bad = (x_bad.T * ETA * x_bad)[0]
    r_bad = (x_bad.T * ETA * z_bad)[0]
    assert chi_bad == v ** 2 and r_bad == v
    assert r_bad.subs(v, 0) == 0
    assert sp.cancel(r_bad / chi_bad) == 1 / v
    record("N2-counterexample", "SymPy exact polynomial arithmetic",
           "Vanishing on a nonregular zero set is not smooth divisibility")

    t, a, b, c = sp.symbols("t a b c", real=True)
    coords = sp.Matrix([t, a, b, c])
    chi_affine = (coords.T * ETA * coords)[0]
    dchi = sp.Matrix([sp.diff(chi_affine, q) for q in coords])
    symbolic_zero(dchi - 2 * ETA * coords)
    assert sp.expand((dchi.T * ETA * dchi)[0] - 4 * chi_affine) == 0
    constant_null = sp.Matrix([1, 1, 0, 0])
    assert (constant_null.T * ETA * sp.eye(4)[:, 0])[0] == -1
    record("N2-affine", "SymPy exact differentiation",
           "Flat affine smooth cone crossing and incompatible constant null representative")


def numerical_null_checks() -> None:
    # Independent numerical formulation: a full 4-by-7 linear system, solved by SVD.
    generators = []
    for i in range(4):
        for j in range(i + 1, 4):
            generator = np.zeros((4, 4))
            generator[i, j] = 1
            generator[j, i] = -ETA_NP[i, i] / ETA_NP[j, j]
            generators.append(generator)
    rng = np.random.default_rng(20260908)
    residuals = []
    compatibility = []
    for v in [-0.1, -1e-5, 0.0, 1e-5, 0.1]:
        x = np.array([1.0, 1.0 + v, 0.0, 0.0])
        linear_map = np.column_stack([b @ x for b in generators] + [x])
        original_coeffs = rng.normal(size=7)
        z = linear_map @ original_coeffs
        solved, *_ = np.linalg.lstsq(linear_map, z, rcond=None)
        residuals.append(float(np.linalg.norm(linear_map @ solved - z)))
        w = original_coeffs[-1]
        u = z - w * x
        y = np.array([-1.0, 0.0, 0.0, 0.0])
        reconstructed = np.outer(u, ETA_NP @ y) - np.outer(y, ETA_NP @ u)
        residuals.append(float(np.linalg.norm(reconstructed @ x + w * x - z)))
        compatibility.append(abs(float(x @ ETA_NP @ z - (x @ ETA_NP @ x) * w)))
    null_x = np.array([1.0, 1.0, 0.0, 0.0])
    null_map = np.column_stack([b @ null_x for b in generators] + [null_x])
    incompatible = np.array([1.0, 0.0, 0.0, 0.0])
    solved, *_ = np.linalg.lstsq(null_map, incompatible, rcond=None)
    incompatible_residual = float(np.linalg.norm(null_map @ solved - incompatible))
    assert max(residuals + compatibility) < 2e-12
    assert incompatible_residual > 0.5
    record("N-independent", "NumPy SVD and independent Lorentz generators",
           "Compatible smooth algebraic data around a null crossing; rejection of an incompatible null target",
           max_residual=max(residuals + compatibility), tolerance=2e-12,
           incompatible_residual=incompatible_residual, seed=20260908)


def variational_crossing_checks() -> None:
    v = sp.Symbol("v", real=True)
    x = sp.Matrix([1, 1 + v, 0, 0])
    linear_map = sp.Matrix.hstack(*(b * x for b in lorentz_basis()), x)
    coeffs = sp.symbols("c0:12")
    euler = sp.Matrix([sum(coeffs[3 * i + j] * v ** j for j in range(3)) for i in range(4)])
    equations = [c for component in linear_map.T * euler for c in sp.Poly(component, v).all_coeffs()]
    system, _ = sp.linear_eq_to_matrix(equations, coeffs)
    assert system.rank() == len(coeffs)
    assert linear_map.subs(v, 0).rank() == 3
    # Two distinct constant representatives of one flat tetrad. Changing only
    # a fixed-X stabilizer cannot identify them. Both right inverses are exact.
    for scale in [1, 2]:
        x = sp.Matrix([scale, 0, 0, 0])
        chi = (x.T * ETA * x)[0]
        for target in sp.eye(4).columnspace():
            w = (x.T * ETA * target)[0] / chi
            u = target - w * x
            k = (u * (ETA * x).T - x * (ETA * u).T) / chi
            symbolic_zero(k * x + w * x - target)
    record("N4", "SymPy exact polynomial linear algebra and right inverses",
           "Polynomial Euler sections cannot be supported only at the rank-drop point; two distinct X representatives give the same flat tetrad",
           polynomial_unknowns=len(coeffs), polynomial_system_rank=system.rank(),
           limitation="Finite polynomial model is not a proof for arbitrary smooth Euler forms; the analytic argument uses continuity on a dense complement.")


def exact_spectral_checks() -> None:
    t, s, s0, lam = sp.symbols("t s s0 lam", positive=True, real=True)
    a, b = sp.symbols("a b")
    damped = sp.exp(-sp.I * lam * (t - sp.I * s))
    assert sp.simplify(damped - sp.exp(-sp.I * lam * t) * sp.exp(-s * lam)) == 0
    assert sp.simplify(sp.I * sp.diff(damped, t) - lam * damped) == 0
    assert sp.simplify(sp.diff(damped, t, 2) + lam ** 2 * damped) == 0
    window = a * sp.exp(-s * lam) + b * sp.exp(s * lam)
    da = (sp.exp(s0 * lam) * (window - sp.diff(window, s) / lam) / 2).subs(s, s0)
    db = (sp.exp(-s0 * lam) * (window + sp.diff(window, s) / lam) / 2).subs(s, s0)
    assert sp.simplify(da - a) == 0 and sp.simplify(db - b) == 0
    assert sp.diff(a + s * b, s, 2) == 0
    record("S1-exact", "SymPy exact differentiation",
           "Continuation signs, first/second-order equations, bounded-window coefficient formulas and kernel affine solution")

    L = sp.Symbol("L", positive=True)
    factor = 1 - sp.exp(-L * lam)
    # SymPy does not decide the positivity of this difference directly.
    # Its positive derivative and zero endpoint give the needed scalar fact.
    assert sp.diff(factor, L).is_positive is True
    assert sp.simplify(factor.subs(L, 0)) == 0
    assert sp.simplify(factor.subs(lam, 0)) == 0
    ell = sp.Symbol("ell", real=True)
    assert sp.expand((ell - sp.I) * (ell + sp.I)) == ell ** 2 + 1
    assert (ell ** 2 + 1).is_positive is True
    assert sp.simplify(1 + 2 * sp.exp(-(sp.log(2) + sp.I * sp.pi))) == 0
    record("S2-S3-exact", "SymPy exact scalar identities",
           "Periodic damping factor, real diagonal deficiency-factor nonvanishing and nonreal heat-trace zero")


def independent_spectral_checks() -> None:
    # Continuous spectral measure, not a finite-dimensional eigenvalue list.
    # H=L2((0,infinity),dlam), A f(lam)=lam f(lam), u(lam)=exp(-lam).
    errors = []
    for s in [0.01, 0.3, 1.0, 4.0]:
        value, bound = quad(lambda lam: math.exp(-2 * (1 + s) * lam),
                            0, np.inf, epsabs=1e-12, epsrel=1e-12)
        exact = 1 / (2 * (1 + s))
        errors.append(abs(value - exact))
        assert abs(value - exact) < 2e-11 and bound < 2e-11
    # A growing branch can exist at every finite depth, yet fail boundedness.
    growing_norms = []
    for s in [0.1, 1.0, 3.0]:
        value, bound = quad(lambda lam: math.exp(2 * s * lam - 2 * lam ** 2),
                            0, np.inf, epsabs=1e-11, epsrel=1e-11)
        exact = math.sqrt(math.pi) / (2 * math.sqrt(2)) * math.exp(s * s / 2) * (1 + erf(s / math.sqrt(2)))
        errors.append(abs(value - exact))
        assert abs(value - exact) < 2e-9 and bound < 2e-9
        growing_norms.append(value)
    assert growing_norms[-1] > 100
    record("S1-continuous", "SciPy adaptive quadrature versus analytic integrals",
           "Unbounded continuous multiplication spectrum reaching zero; finite continuation is not uniform boundedness",
           max_absolute_error=max(errors), tolerance=2e-9,
           growing_squared_norms=growing_norms)

    rng = np.random.default_rng(20260908)
    raw = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    q, _ = np.linalg.qr(raw)
    eigenvalues = np.array([0, 1 / 3, 2, 5])
    matrix = (q * eigenvalues) @ q.conj().T
    u = rng.normal(size=4) + 1j * rng.normal(size=4)
    errors = []
    for z in [0.3 - 0.01j, -1.2 - 0.5j, 2.0 - 3.0j]:
        direct = expm(-1j * z * matrix) @ u
        spectral = q @ (np.exp(-1j * z * eigenvalues) * (q.conj().T @ u))
        errors.append(float(np.linalg.norm(direct - spectral)))
        assert np.linalg.norm(direct) <= np.linalg.norm(u) + 1e-12
    assert max(errors) < 2e-12
    record("S1-matrix", "SciPy matrix exponential versus NumPy diagonal spectral calculus",
           "Non-diagonal positive semidefinite complex Hermitian generator; damping and contraction",
           max_residual=max(errors), tolerance=2e-12, seed=20260908)

    tails = []
    for n in [30, 300, 3000]:
        k = np.arange(1, n + 1, dtype=float)
        tail = float(math.pi ** 2 / 6 - np.sum(1 / k ** 2))
        assert 1 / (n + 1) - 1e-14 <= tail <= 1 / n + 1e-14
        assert np.sum(1 / k) >= math.log(n)
        tails.append(tail)
    record("S3-truncation", "NumPy sums versus exact zeta(2) and integral-test bounds",
           "Convergent trace truncations at exponent two and harmonic growth at the trace-class threshold",
           truncations=[30, 300, 3000], tails=tails)


def determinant_checks() -> None:
    m = sp.Symbol("m", positive=True)
    a, r = sp.symbols("a r", positive=True)
    block_lower_bound = (sp.exp(m + 1) - sp.exp(m) - 2) / (a + m + 1) ** r
    assert sp.limit(block_lower_bound, m, sp.oo) == sp.oo
    record("S4", "SymPy symbolic asymptotic limit",
           "Exponential integer-block lower bound diverges for arbitrary fixed positive shift and exponent; no finite Schatten order")

    z = sp.Symbol("z")
    sine_form = sp.sin(sp.pi * sp.sqrt(z)) / (sp.pi * sp.sqrt(z))
    trace_series = -sum(z ** k * sp.zeta(2 * k) / k for k in range(1, 5))
    assert sp.simplify(sp.series(sp.log(sine_form), z, 0, 5).removeO() - trace_series) == 0
    assert sp.limit(sine_form, z, 0) == 1
    for n in range(1, 5):
        assert sp.simplify(sine_form.subs(z, n ** 2)) == 0
    assert sp.simplify(sine_form.subs(z, -1) - sp.sinh(sp.pi) / sp.pi) == 0
    record("S5-exact", "SymPy series and exact trigonometric values",
           "Heat-determinant logarithmic trace series versus sine formula through fourth order; positive square zeros and nonzero negative unit argument")

    errors = []
    for z in [0.35 + 0.2j, -0.5 + 0j, 2.4 + 0.1j]:
        exact = cmath.sin(math.pi * cmath.sqrt(z)) / (math.pi * cmath.sqrt(z))
        previous = float("inf")
        for n in [100, 1000, 10000]:
            k = np.arange(1, n + 1, dtype=float)
            truncated = np.exp(np.sum(np.log1p(-z / k ** 2)))
            error = float(abs(truncated - exact))
            log_tail_bound = abs(z) / (n * (1 - abs(z) / (n + 1) ** 2))
            bound = abs(truncated) * math.expm1(log_tail_bound)
            assert error <= bound + 2e-12
            assert error < previous
            previous = error
            errors.append(error)
    record("S5-independent", "NumPy product versus independent complex sine evaluation",
           "Determinant convergence at three nonzero complex/real points with a logarithmic tail bound",
           truncations=[100, 1000, 10000], max_error=max(errors),
           roundoff_allowance=2e-12)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    exact_null_checks()
    numerical_null_checks()
    variational_crossing_checks()
    exact_spectral_checks()
    independent_spectral_checks()
    determinant_checks()
    paths = [
        "research_tracks/action_selection/split_jet_null_continuation.en.md",
        "research_tracks/action_selection/split_jet_null_continuation.cs.md",
        "research_tracks/action_selection/split_jet_palatii_variational_lift.en.md",
        "research_tracks/action_selection/split_jet_palatii_variational_lift.cs.md",
        "research_tracks/complex_time_branch_selection/bounded_selector_domain_completion.en.md",
        "research_tracks/complex_time_branch_selection/bounded_selector_domain_completion.cs.md",
        "research_tracks/complex_time_branch_selection/psi_branch_selection.en.md",
        "research_tracks/complex_time_branch_selection/psi_branch_selection.cs.md",
        "tools/verify_null_and_spectral_gap_steps.py",
        "tools/verify_psi_branch_selection.py",
    ]
    report = {
        "schema": "ubt.research-gap-verification/v1",
        "date": "2026-09-08",
        "base_commit": "6ee61b98bb7578d67c2babe16134128d1f0f910c",
        "result": "PASS",
        "versions": {"python": platform.python_version(), "sympy": sp.__version__,
                     "numpy": np.__version__, "scipy": scipy.__version__},
        "lean_status": "LEAN-PENDING",
        "lean_reason": "Neither Lean nor Lake found in the inspected runtime; no compiled formal proof supplied.",
        "runtime_tools": {"lean": shutil.which("lean"), "lake": shutil.which("lake")},
        "checks": CHECKS,
        "proof_scope": {
            "N1-N3": "Analytic local smooth divisibility and null-rank theorem; exact algebra and independent finite checks only.",
            "N4": "Analytic extension of the chosen Palatini action's equations across compatible smooth regular null hypersurfaces; surjective solution map, not a bijection modulo only fixed-X stabilizers.",
            "S1": "Analytic proof for weak norm-holomorphic solutions of a nonnegative self-adjoint operator equation with a bounded vertical ray and strong boundary value.",
            "S2": "Direct periodic damping under S1 forces kernel support.",
            "S3": "Analytic self-adjoint closure of the diagonal prime operator; trace class only for Re(omega)>1.",
            "S4-S5": "Prime resolvent belongs to no finite Schatten class; the trace-class heat determinant has integer-power zeros and fails the required xi identity.",
        },
        "not_verified": [
            "Formal infinite-dimensional spectral or smooth-manifold proofs",
            "A microscopic UBT action or generator and its domain or physical boundary condition",
            "Einstein dynamics, Newton coefficient, generic global/null continuation or quantum measure",
            "Riemann hypothesis, a Hilbert-Polya operator or the required determinant identity",
            "Human semantic equivalence of the bilingual prose",
        ],
        "canonical_claims_changed": False,
        "source_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
    }
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        print(f"PASS: {len(CHECKS)} check groups; record: {args.output}")
        print("LEAN-PENDING. Not a proof of RH, Einstein dynamics or the infinite-dimensional theorem by computation.")
    else:
        print(payload)


if __name__ == "__main__":
    main()
