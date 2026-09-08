#!/usr/bin/env python3
"""Finite certificates for the Lorentz-slice audit, not a formal field-theory proof.

Two formulations: exact realified SymPy algebra and independent complex 2x2
NumPy/SciPy calculations. The Ricci tensor is computed from the full metric.
No result promotes a canonical UBT claim, proves a quantum theory, or proves RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import shutil
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
G = sp.Matrix([[0, 0, 0, 1], [0, -1, 0, 0],
               [0, 0, -1, 0], [1, 0, 0, 0]])
ETA = sp.diag(-1, 1, 1, 1)
OMEGA = sp.zeros(4).row_join(G).col_join((-G).row_join(sp.zeros(4)))
C = sp.Matrix([[sp.I, 0, 0, -sp.I], [0, -sp.I, -1, 0],
               [0, -sp.I, 1, 0], [sp.I, 0, 0, sp.I]])
J = C.applyfunc(sp.re).col_join(C.applyfunc(sp.im))
CHECKS: list[dict] = []


def zero(values):
    for value in values:
        assert sp.simplify(value) == 0, value


def record(identifier, channel, scope, **details):
    CHECKS.append(dict(id=identifier, result="PASS", channel=channel,
                       scope=scope, **details))


def pf(q):
    return q[0, 1] * q[2, 3] - q[0, 2] * q[1, 3] + q[0, 3] * q[1, 2]


def exact_slice():
    gram = C.conjugate().T * G * C
    assert gram == -2 * ETA
    assert J.rank() == 4 and OMEGA.det() == 1
    zero(J.T * OMEGA * J)
    e = sp.Matrix(4, 4, sp.symbols("e0:16", real=True))
    zero((J * e).T * OMEGA * (J * e))
    record("M1", "SymPy exact matrix algebra",
           "Lorentz Gram matrix, half-dimensional isotropy, arbitrary real tetrad",
           gram_diagonal=[2, -2, -2, -2], slice_rank=4)


def exact_variations():
    # Differentiate the unrestricted jet density before evaluating on the slice.
    p = sp.Matrix(8, 4, sp.symbols("p0:32", real=True))
    q = p.T * OMEGA * p
    density = pf(q)
    for e in (sp.eye(4), sp.diag(1, 2, 3, 4)):
        p0 = J * e
        sub = dict(zip(list(p), list(p0), strict=True))
        assert sp.expand(density.subs(sub)) == 0
        zero([sp.diff(density, component).subs(sub) for component in p])
    # Explicit dependence through F also multiplies Pf(Q)=0.
    record("M2", "SymPy exact differentiation",
           "Unrestricted density gradient in all 32 real jet variables at two nondegenerate slice jets; coefficient derivative vanishes too")

    complex_structure = sp.zeros(4).row_join(-sp.eye(4)).col_join(
        sp.eye(4).row_join(sp.zeros(4)))
    normal = complex_structure * J
    h = -2 * ETA
    target = sp.zeros(4)
    target[0, 1] = target[2, 3] = 1
    target[1, 0] = target[3, 2] = -1
    b = h.inv() * target / 2
    v = normal * b
    eps = sp.Symbol("eps", real=True)
    f0, f1, f2 = sp.symbols("f0 f1 f2", real=True)
    qeps = (J + eps * v).T * OMEGA * (J + eps * v)
    zero(qeps - eps * target)
    leps = sp.expand((f0 + eps * f1 + eps**2 * f2) * pf(qeps))
    assert leps == f0 * eps**2 + f1 * eps**3 + f2 * eps**4
    assert sp.diff(leps, eps).subs(eps, 0) == 0
    assert sp.diff(leps, eps, 2).subs(eps, 0) == 2 * f0
    delta_e = sp.Matrix(4, 4, sp.symbols("v0:16", real=True))
    tangent = J * delta_e
    zero(J.T * OMEGA * tangent + tangent.T * OMEGA * J)
    record("M3", "SymPy exact polynomial algebra",
           "Slice-tangent first variation of Q is zero; a normal jet has nonzero pointwise density second variation, not a propagating bulk Hessian certificate",
           normal_density="f0*eps^2+f1*eps^3+f2*eps^4",
           normal_second_derivative="2*f0")


def exact_curved_witness():
    t = sp.Symbol("t", positive=True)
    c0 = sp.Symbol("c0", positive=True)
    coords = (t, *sp.symbols("x y z", real=True))
    e = sp.diag(1, t**2, t**2, t**2)  # internal index, coordinate index
    x = sp.Matrix([c0 * t, 0, 0, 0])
    jet = [sp.zeros(4) for _ in range(4)]
    physical = [sp.zeros(4) for _ in range(4)]
    for i in range(1, 4):
        jet[i][0, i] = jet[i][i, 0] = t
        physical[i][0, i] = physical[i][i, 0] = 2 * t
    p = sp.zeros(4)
    for mu in range(4):
        zero(jet[mu].T * ETA + ETA * jet[mu])
        zero(physical[mu].T * ETA + ETA * physical[mu])
        p[:, mu] = x.diff(coords[mu]) + jet[mu] * x
    zero(p - c0 * e)
    zero((J * p).T * OMEGA * (J * p))
    # Independent two-sided matrix realization fixes the boost sign convention.
    sigma = [sp.Matrix([[0, 1], [1, 0]]),
             sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1)]
    basis = [sp.I * sp.eye(2)] + [-sp.I * s for s in sigma]
    theta = c0 * t * basis[0]
    for mu in range(4):
        a = sp.zeros(2) if mu == 0 else -t * sigma[mu - 1] / 2
        native_jet = theta.diff(coords[mu]) + a * theta + theta * a.conjugate().T
        target_jet = c0 * sum((e[k, mu] * basis[k] for k in range(4)), sp.zeros(2))
        zero(native_jet - target_jet)
    for mu in range(4):
        for nu in range(mu + 1, 4):
            torsion = (e[:, nu].diff(coords[mu]) - e[:, mu].diff(coords[nu])
                       + physical[mu] * e[:, nu] - physical[nu] * e[:, mu])
            zero(torsion)
    assert e.det() == t**6
    record("M4-jet", "SymPy exact differentiation",
           "Non-null single-field representer with Lorentz jet connection; distinct torsion-free physical connection and composite difference",
           tetrad_diagonal=["1", "t^2", "t^2", "t^2"],
           field_norm="-c0^2*t^2", determinant="t^6")

    # Full coordinate Christoffel/Ricci calculation, not an inserted FLRW formula.
    g = e.T * ETA * e
    gi = g.inv()
    gamma = [[[sp.simplify(sum(
        gi[r, a] * (sp.diff(g[a, nu], coords[mu])
                    + sp.diff(g[a, mu], coords[nu])
                    - sp.diff(g[mu, nu], coords[a])) / 2
        for a in range(4))) for nu in range(4)] for mu in range(4)]
        for r in range(4)]
    ricci = sp.zeros(4)
    for mu in range(4):
        for nu in range(4):
            value = 0
            for r in range(4):
                value += (sp.diff(gamma[r][mu][nu], coords[r])
                          - sp.diff(gamma[r][mu][r], coords[nu]))
                for a in range(4):
                    value += (gamma[r][r][a] * gamma[a][mu][nu]
                              - gamma[r][nu][a] * gamma[a][mu][r])
            ricci[mu, nu] = sp.simplify(value)
    assert ricci == sp.diag(-6 / t**2, 10 * t**2, 10 * t**2, 10 * t**2)
    assert sp.simplify(sp.trace(gi * ricci)) == 36 / t**2
    assert sp.simplify(ricci[0, 0] / g[0, 0] - ricci[1, 1] / g[1, 1]) == -4 / t**2
    record("M4-Ricci", "SymPy full coordinate curvature",
           "Explicit metric is not Ricci-proportional, even for a variable proportionality factor",
           ricci_diagonal=["-6/t^2", "10*t^2", "10*t^2", "10*t^2"],
           scalar_curvature="36/t^2", proportionality_mismatch="-4/t^2")


SIGMA = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]
BASIS = [1j * np.eye(2)] + [-1j * s for s in SIGMA]


def sharp(x):
    return np.array([[x[1, 1], -x[0, 1]], [-x[1, 0], x[0, 0]]])


def q_from_matrices(vectors):
    # Independent matrix-algebra polarization h(U,V)=Tr(U^dagger V^sharp).
    return np.array([[np.trace(u.conj().T @ sharp(v)).imag
                      for v in vectors] for u in vectors])


def numerical_checks():
    rng = np.random.default_rng(648202609)
    max_scaled_residual = 0.0
    for _ in range(24):
        e = np.eye(4) + rng.normal(0, 0.2, (4, 4))
        assert abs(np.linalg.det(e)) > 0.05
        vectors = [sum((e[a, mu] * BASIS[a] for a in range(4)),
                       np.zeros((2, 2), complex)) for mu in range(4)]
        spin = expm(sum(((rng.normal(0, .15) + 1j * rng.normal(0, .15)) * s
                         for s in SIGMA), np.zeros((2, 2), complex)))
        phase = np.exp(1j * rng.uniform(-np.pi, np.pi))
        transformed = [phase * spin @ v @ spin.conj().T for v in vectors]
        q = q_from_matrices(transformed)
        scale = max(1.0, max(np.linalg.norm(v)**2 for v in transformed))
        residual = float(np.max(np.abs(q))) / scale
        max_scaled_residual = max(max_scaled_residual, residual)
        assert residual < 2e-13
    record("M1-independent", "NumPy complex 2x2 algebra / SciPy exponential",
           "24 seeded nondegenerate coframes, Lorentz transformations and common phases; no realification matrix reused",
           seed=648202609, witnesses=24, max_scaled_residual=max_scaled_residual)

    h = np.diag([2.0, -2.0, -2.0, -2.0])
    target = np.zeros((4, 4))
    target[0, 1] = target[2, 3] = 1
    target[1, 0] = target[3, 2] = -1
    b = np.linalg.solve(h, target) / 2
    normal = [sum((1j * BASIS[a] * b[a, mu] for a in range(4)),
                  np.zeros((2, 2), complex)) for mu in range(4)]

    def density(eps):
        q = q_from_matrices([BASIS[mu] + eps * normal[mu] for mu in range(4)])
        return (2.0 + 3.0 * eps) * pf(q)

    residuals = []
    for eps in [1e-3, 5e-4, 2.5e-4]:
        first = (density(eps) - density(-eps)) / (2 * eps)
        second = (density(eps) + density(-eps) - 2 * density(0)) / eps**2
        assert abs(first - 3 * eps**2) < 1e-12
        assert abs(second - 4) < 1e-9
        residuals.append(float(first))
    record("M2-M3-independent", "NumPy complex density / central differences",
           "First derivative tends to zero quadratically while a normal pointwise second derivative tends to four; not a bulk fluctuation-mode calculation",
           first_derivative_estimates=residuals, expected_second_derivative=4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    exact_slice()
    exact_variations()
    exact_curved_witness()
    numerical_checks()
    paths = [
        "tools/verify_multisymplectic_lorentz_slice.py",
        *[f"research_tracks/action_selection/{stem}.{lang}.md"
          for stem in ("multisymplectic_lorentz_slice_audit",
                       "theta_covariant_multisymplectic_gauging",
                       "unconditional_gr_action_decision")
          for lang in ("en", "cs")],
    ]
    report = {
        "schema": "ubt-verification/v1",
        "date": "2026-09-08",
        "base_commit": "7059bda2094b691b0d2eb0a61130788a34c77fff",
        "result": "PASS", "check_groups": len(CHECKS), "checks": CHECKS,
        "tools": {"python": platform.python_version(), "sympy": sp.__version__,
                  "numpy": np.__version__, "scipy": scipy.__version__},
        "lean": {"status": "LEAN-PENDING", "lean_available": bool(shutil.which("lean")),
                 "lake_available": bool(shutil.which("lake")),
                 "reason": "No compiled Lean proof; Lean and Lake absent in the inspected runtime."},
        "source_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                          for p in paths},
        "scope": "Finite exact and numerical certificates accompanying an analytic local theorem for the specified F Q wedge Q family.",
        "limitations": [
            "No formal proof of the full smooth functional chain rule or infinite-dimensional variational statement.",
            "A pointwise density Hessian witness does not establish a nonzero integrated bulk Hessian or propagating modes.",
            "The curved witness uses the approved distinction between a composite jet connection and the physical Levi-Civita connection.",
            "No claim about other actions, quantum corrections, RH, or unconditional UBT gravity is closed.",
        ],
        "canonical_claim_status_changes": [],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    for check in CHECKS:
        print(f"PASS {check['id']}: {check['scope']}")
    print(f"{len(CHECKS)} check groups passed; LEAN-PENDING.")


if __name__ == "__main__":
    main()
