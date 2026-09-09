#!/usr/bin/env python3
"""Exact and independent checks for the bounded spectral-domain results.

The analytic infinite-dimensional proofs and their hypotheses are in the
paired research note.  These finite checks do not prove RH, Einstein dynamics,
or a microscopic UBT action.
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
CHECKS: list[dict] = []


def record(identifier: str, channel: str, scope: str, **details) -> None:
    CHECKS.append(dict(id=identifier, result="PASS", channel=channel,
                       scope=scope, **details))


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
    exact_spectral_checks()
    independent_spectral_checks()
    determinant_checks()
    paths = [
        "research_tracks/complex_time_branch_selection/bounded_selector_domain_completion.en.md",
        "research_tracks/complex_time_branch_selection/bounded_selector_domain_completion.cs.md",
        "research_tracks/complex_time_branch_selection/psi_branch_selection.en.md",
        "research_tracks/complex_time_branch_selection/psi_branch_selection.cs.md",
        "tools/verify_bounded_spectral_gap_steps.py",
        "tools/verify_psi_branch_selection.py",
    ]
    report = {
        "schema": "ubt.research-gap-verification/v1",
        "date": "2026-09-09",
        "base_commit": "6ee61b98bb7578d67c2babe16134128d1f0f910c",
        "result": "PASS",
        "versions": {"python": platform.python_version(), "sympy": sp.__version__,
                     "numpy": np.__version__, "scipy": scipy.__version__},
        "lean_status": "LEAN-PENDING",
        "lean_reason": "Neither Lean nor Lake found in the inspected runtime; no compiled formal proof supplied.",
        "runtime_tools": {"lean": shutil.which("lean"), "lake": shutil.which("lake")},
        "checks": CHECKS,
        "proof_scope": {
            "S1": "Analytic proof for weak norm-holomorphic solutions of a nonnegative self-adjoint operator equation with a bounded vertical ray and strong boundary value.",
            "S2": "Direct periodic damping under S1 forces kernel support.",
            "S3": "Analytic self-adjoint closure of the diagonal prime operator; trace class only for Re(omega)>1.",
            "S4-S5": "Prime resolvent belongs to no finite Schatten class; the trace-class heat determinant has integer-power zeros and fails the required xi identity.",
        },
        "not_verified": [
            "Formal infinite-dimensional spectral proofs",
            "A microscopic UBT action or generator and its physical boundary condition",
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
        print("LEAN-PENDING. Not a proof of RH or the infinite-dimensional theorem by computation.")
    else:
        print(payload)


if __name__ == "__main__":
    main()
