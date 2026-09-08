#!/usr/bin/env python3
"""Finite certificates for the conditional curvature-channel equivalence theorem.

SymPy exact bivector/Clifford algebra is cross-checked with independent
NumPy coordinate tensors and a different Dirac-matrix representation.
This does not prove microscopic action selection, RH, or a formal theorem.
"""
from __future__ import annotations

import argparse
import hashlib
from itertools import combinations, permutations
import json
import platform
import shutil
from pathlib import Path

import numpy as np
import sympy as sp

from verify_clifford_palatini_trace_selector import canonical_gammas

ROOT = Path(__file__).resolve().parents[1]
PAIRS = list(combinations(range(4), 2))
TRIPLES = list(combinations(range(4), 3))
ETA = [-1, 1, 1, 1]
CHECKS = []


def eps(indices):
    if len(set(indices)) < len(indices):
        return 0
    return (-1)**sum(a > b for i, a in enumerate(indices) for b in indices[i+1:])


def wedge(a, b):
    out = {}
    for ia, ca in a.items():
        for ib, cb in b.items():
            if set(ia) & set(ib):
                continue
            key = tuple(sorted(ia + ib))
            out[key] = out.get(key, 0) + eps(ia + ib) * ca * cb
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def add(a, b, scale=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + scale * v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def record(identifier, channel, scope, **details):
    CHECKS.append(dict(id=identifier, channel=channel, scope=scope,
                       result="PASS", **details))


def exact_hodge_and_cartan():
    # Internal star on LOWER bivector indices.
    star = sp.Matrix([[eps((a, b, c, d)) * ETA[c] * ETA[d]
                       for c, d in PAIRS] for a, b in PAIRS])
    assert star**2 == -sp.eye(6)
    u, v = sp.symbols("u v", real=True)
    p = u * star + v * sp.eye(6)
    assert sp.factor(p.det()) == (u*u + v*v)**3
    assert sp.simplify(p * (v * sp.eye(6) - u * star)) == (u*u + v*v) * sp.eye(6)
    assert (star + sp.I * sp.eye(6)).rank() == 3
    assert (star - sp.I * sp.eye(6)).rank() == 3
    record("H1", "SymPy exact bivector algebra",
           "Lorentz Hodge square, determinant and inverse; complex exceptional ranks",
           determinant="(u^2+v^2)^3", exceptional_ranks=[3, 3])

    e = [{(a,): sp.Integer(1)} for a in range(4)]
    torsion_variables = sp.symbols("t0:24", real=True)
    torsion = [dict(zip(PAIRS, torsion_variables[6*a:6*a+6])) for a in range(4)]
    columns = []
    for a, b in PAIRS:
        dsigma = add(wedge(torsion[a], e[b]), wedge(e[a], torsion[b]), -1)
        columns.extend(ETA[a] * ETA[b] * dsigma.get(key, 0) for key in TRIPLES)
    m = sp.Matrix(columns).jacobian(torsion_variables)
    determinant = m.det()
    assert determinant != 0 and m.rank() == 24
    c = sp.kronecker_product(p, sp.eye(4)) * m
    # Exact integer witnesses supplement the general determinant product proof.
    for uu, vv in [(1, 0), (0, 1), (2, 3), (-2, 3)]:
        assert c.subs({u: uu, v: vv}).det() == determinant * (uu*uu + vv*vv)**12
    record("H2", "SymPy exact exterior/linear algebra",
           "D(E wedge E) has invertible 24-component torsion map; full real connection determinant",
           base_determinant=str(determinant),
           full_determinant=f"{determinant}*(u^2+v^2)^12")

    gradients = sp.symbols("dv0:4", real=True)
    dv = {(a,): gradients[a] for a in range(4)}
    gradient_equations = []
    for a, b in PAIRS:
        form = wedge(dv, wedge(e[a], e[b]))
        gradient_equations.extend(form.get(key, 0) for key in TRIPLES)
    assert sp.Matrix(gradient_equations).jacobian(gradients).rank() == 4
    record("H3", "SymPy exact rank",
           "With constant nonzero u, torsion-free variable-v connection equation forces dv=0")


def exact_bianchi():
    # Arbitrary symmetric H supplies algebraic Riemann curvature eta Kulkarni H.
    h = sp.zeros(4)
    variables = iter(sp.symbols("h0:10", real=True))
    for a in range(4):
        for b in range(a, 4):
            h[a, b] = h[b, a] = next(variables)
    eta = sp.diag(*ETA)
    r = [[{} for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c, d in PAIRS:
                r[a][b][(c, d)] = (eta[a, c]*h[b, d] + eta[b, d]*h[a, c]
                                    - eta[a, d]*h[b, c] - eta[b, c]*h[a, d])
    for a in range(4):
        result = {}
        for b in range(4):
            result = add(result, wedge({(b,): 1}, r[a][b]))
        assert not result
    record("H4", "SymPy exact algebraic curvature",
           "Holst tetrad term vanishes for an arbitrary symmetric-tensor curvature family satisfying first Bianchi; Einstein curvature not assumed")


def exact_clifford():
    gammas, grading = canonical_gammas()
    unknowns = sp.symbols("z0:16")
    z = sp.Matrix(4, 4, unknowns)
    equations = []
    for a, b in PAIRS:
        generator = gammas[a] * gammas[b] / 2
        equations.extend(z * generator - generator * z)
    linear, _ = sp.linear_eq_to_matrix(equations, unknowns)
    assert len(linear.nullspace()) == 2
    assert linear * sp.eye(4).reshape(16, 1) == sp.zeros(linear.rows, 1)
    assert linear * grading.reshape(16, 1) == sp.zeros(linear.rows, 1)
    for fifth in (grading, sp.I * grading):
        extended_equations = list(equations)
        for gamma in gammas:
            generator = gamma * fifth / 2
            extended_equations.extend(z * generator - generator * z)
        extended, _ = sp.linear_eq_to_matrix(extended_equations, unknowns)
        assert len(extended.nullspace()) == 1
        assert extended * sp.eye(4).reshape(16, 1) == sp.zeros(extended.rows, 1)
    record("C1", "SymPy exact commutant",
           "Lorentz-scalar insertions span I and Gamma_star; adding the translation generators leaves only I",
           lorentz_dimension=2, extended_dimension=1)

    for sign in (1, -1):
        fifth = grading if sign == 1 else sp.I * grading
        lorentz = [gammas[a] * gammas[b] / 2 for a, b in PAIRS]
        translation = [gammas[a] * fifth / 2 for a in range(4)]
        for j, (a, b) in enumerate(PAIRS):
            for k, (c, d) in enumerate(PAIRS):
                expected = -(ETA[a]*ETA[b] if j == k else 0)
                assert sp.trace(lorentz[j] * lorentz[k]) == expected
                assert sp.trace(grading * lorentz[j] * lorentz[k]) == -sp.I * eps((a,b,c,d))
            for translation_generator in translation:
                assert sp.trace(lorentz[j] * translation_generator) == 0
                assert sp.trace(grading * lorentz[j] * translation_generator) == 0
        for a in range(4):
            for b in range(4):
                assert sp.trace(translation[a] * translation[b]) == (-sign*ETA[a] if a == b else 0)
                assert sp.trace(grading * translation[a] * translation[b]) == 0
    record("C2", "SymPy exact Clifford traces",
           "All Lorentz/translation trace blocks, graded and ungraded, for both fifth-channel signs; fixes Pontryagin and Nieh-Yan coefficients")

    cg = sp.Symbol("c_g", nonzero=True, real=True)
    ell = sp.Symbol("ell", positive=True)
    for sign in (1, -1):
        u = -2 * cg * sign / ell**2
        lam = -6 * cg / ell**4
        assert sp.simplify(lam / u) == 3 * sign / ell**2
        # Coefficients in c_g * i Tr(Gamma_star F wedge F).
        assert sp.simplify(-cg * sign / (2*ell**2) - u/4) == 0
        assert sp.simplify(cg / (4*ell**4) + lam/24) == 0
    record("C3", "SymPy exact coefficient matching",
           "General real graded coefficient gives u=-2*epsilon*c_g/ell^2 and Lambda=3*epsilon/ell^2; constant ungraded coefficient changes neither")


def numerical_curvature():
    rng = np.random.default_rng(649202609)
    # Independent standard Dirac representation, not the canonical block lift.
    sigmas = [np.array([[0,1],[1,0]], complex),
              np.array([[0,-1j],[1j,0]], complex), np.diag([1,-1]).astype(complex)]
    z = np.zeros((2,2), complex)
    gammas = [1j * np.diag([1,1,-1,-1]).astype(complex)]
    gammas.extend(1j * np.block([[z,s],[-s,z]]) for s in sigmas)
    grading = 1j * gammas[0] @ gammas[1] @ gammas[2] @ gammas[3]
    ell = 1.7
    permutations4 = list(permutations(range(4)))

    def wedge_scalar(a, b):
        return sum(eps(p) * a[p[0],p[1]] * b[p[2],p[3]]
                   for p in permutations4) / 4

    def wedge_trace(f, insertion):
        return sum(eps(p) * np.trace(insertion @ f[p[0],p[1]] @ f[p[2],p[3]])
                   for p in permutations4) / 4

    def spin_connection(frame):
        return sum((frame[a,b] * ETA[b] * gammas[a] @ gammas[b] / 4
                    for a in range(4) for b in range(4)), np.zeros((4,4), complex))

    max_residual = 0.0
    eta = np.diag(ETA)
    for sign in (1, -1):
        fifth = grading if sign == 1 else 1j * grading
        trans = [g @ fifth / 2 for g in gammas]
        for _ in range(8):
            coframe = np.eye(4) + rng.normal(0, .15, (4,4))  # internal, coordinate
            assert abs(np.linalg.det(coframe)) > .1
            de = rng.normal(0, .2, (4,4,4))  # derivative, internal, coordinate
            lower = rng.normal(0, .2, (4,4,4))
            lower -= lower.transpose(0,2,1)
            omega = np.einsum("ab,mbc->mac", eta, lower)
            dlower = rng.normal(0, .2, (4,4,4,4))
            dlower -= dlower.transpose(0,1,3,2)
            domega = np.einsum("ab,nmbc->nmac", eta, dlower)
            ext = [spin_connection(omega[mu]) + sum(
                (coframe[a,mu]*trans[a]/ell for a in range(4)), np.zeros((4,4),complex))
                for mu in range(4)]
            dext = [[spin_connection(domega[mu,nu]) + sum(
                (de[mu,a,nu]*trans[a]/ell for a in range(4)), np.zeros((4,4),complex))
                for nu in range(4)] for mu in range(4)]
            f = np.zeros((4,4,4,4), complex)
            r = np.zeros((4,4,4,4))
            torsion = np.zeros((4,4,4))
            for mu in range(4):
                for nu in range(4):
                    f[mu,nu] = dext[mu][nu]-dext[nu][mu]+ext[mu]@ext[nu]-ext[nu]@ext[mu]
                    r[mu,nu] = (domega[mu,nu]-domega[nu,mu]
                                 +omega[mu]@omega[nu]-omega[nu]@omega[mu]) @ eta
                    torsion[mu,nu] = (de[mu,:,nu]-de[nu,:,mu]
                        +omega[mu]@coframe[:,nu]-omega[nu]@coframe[:,mu])
            sigma = np.zeros_like(r)
            for a in range(4):
                for b in range(4):
                    sigma[:,:,a,b] = np.outer(coframe[a],coframe[b])-np.outer(coframe[b],coframe[a])
            rr = sum(ETA[a]*ETA[b]*wedge_scalar(r[:,:,a,b],r[:,:,a,b])
                     for a in range(4) for b in range(4))
            eer = sum(ETA[a]*ETA[b]*wedge_scalar(sigma[:,:,a,b],r[:,:,a,b])
                      for a in range(4) for b in range(4))
            tt = sum(ETA[a]*wedge_scalar(torsion[:,:,a],torsion[:,:,a]) for a in range(4))
            ungraded = wedge_trace(f, np.eye(4))
            expected = -.5*rr + sign/ell**2*(eer-tt)
            scaled = abs(ungraded-expected) / max(1, abs(expected))
            assert scaled < 2e-12
            max_residual = max(max_residual, float(scaled))
            shifted = r-sign/ell**2*sigma
            expected_graded = sum(eps((a,b,c,d))*wedge_scalar(
                shifted[:,:,a,b],shifted[:,:,c,d]) for a,b,c,d in permutations4)/4
            assert abs(1j*wedge_trace(f,grading)-expected_graded) < 2e-11
    record("C2-independent", "NumPy coordinate connection jets and distinct Dirac representation",
           "16 full dA+A wedge A calculations, both fifth signs, compare complete graded and ungraded curvature-square forms",
           seed=649202609, witnesses=16, max_scaled_residual=max_residual)


def numerical_cartan():
    rng = np.random.default_rng(649202610)
    maximum_error = 0.0

    def dual(source):
        # Reconstruct antisymmetric internal indices and contract all ordered pairs.
        full = np.zeros((4, 4, 4))
        for k, (a, b) in enumerate(PAIRS):
            full[a,b] = source[k]
            full[b,a] = -source[k]
        return np.array([sum((eps((a,b,c,d))*ETA[c]*ETA[d]*full[c,d]/2
                              for c in range(4) for d in range(4)), np.zeros(4))
                         for a,b in PAIRS])

    for _ in range(4):
        e = np.eye(4) + rng.normal(0, .12, (4,4))
        assert abs(np.linalg.det(e)) > .1

        def dsigma(components):
            t = np.zeros((4,4,4))
            for a in range(4):
                for k, (mu,nu) in enumerate(PAIRS):
                    t[a,mu,nu] = components[6*a+k]
                    t[a,nu,mu] = -components[6*a+k]
            return np.array([[ETA[a]*ETA[b]*(
                t[a,mu,nu]*e[b,rho]+t[a,nu,rho]*e[b,mu]+t[a,rho,mu]*e[b,nu]
                -e[a,mu]*t[b,nu,rho]-e[a,nu]*t[b,rho,mu]-e[a,rho]*t[b,mu,nu])
                for mu,nu,rho in TRIPLES] for a,b in PAIRS])

        basis_responses = [dsigma(np.eye(24)[i]) for i in range(24)]
        m = np.column_stack([s.ravel() for s in basis_responses])
        source = rng.normal(size=(6,4))
        solutions = []
        for u, v in [(2., 0.), (2., 3.)]:
            c = np.column_stack([(u*dual(s)+v*s).ravel() for s in basis_responses])
            direct = np.linalg.solve(c, source.ravel())
            inverse_source = (v*source-u*dual(source))/(u*u+v*v)
            factored = np.linalg.solve(m, inverse_source.ravel())
            error = float(np.max(np.abs(direct-factored)))
            assert error < 1e-11
            maximum_error = max(maximum_error, error)
            solutions.append(direct)
        assert np.linalg.norm(solutions[0]-solutions[1]) > 1e-4
    record("H1-H2-independent", "NumPy full coordinate torsion system",
           "Four nontrivial coframes; direct 24-component spin-response solve agrees with bivector inverse, and changing Holst coefficient changes sourced torsion",
           seed=649202610, witnesses=4, max_absolute_error=maximum_error)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    exact_hodge_and_cartan()
    exact_bianchi()
    exact_clifford()
    numerical_curvature()
    numerical_cartan()
    paths = [
        "tools/verify_curvature_channel_equivalence.py",
        "tools/verify_clifford_palatini_trace_selector.py",
        *[f"research_tracks/action_selection/{stem}.{lang}.md"
          for stem in ("curvature_channel_dynamical_equivalence",
                       "clifford_palatini_trace_selector",
                       "fifth_channel_macdowell_mansouri",
                       "single_theta_macdowell_mansouri_candidate")
          for lang in ("en", "cs")],
    ]
    report = {
        "schema": "ubt-verification/v1", "date": "2026-09-08",
        "base_commit": "728a68e10564e802be70ac57bfef946a6f31b3e1",
        "result": "PASS", "check_groups": len(CHECKS), "checks": CHECKS,
        "tools": {"python": platform.python_version(), "sympy": sp.__version__,
                  "numpy": np.__version__},
        "lean": {"status": "LEAN-PENDING", "lean_available": bool(shutil.which("lean")),
                 "lake_available": bool(shutil.which("lake")),
                 "reason": "No compiled Lean proof; Lean and Lake absent in inspected runtime."},
        "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                          for p in paths},
        "limitations": [
            "Finite checks do not formally prove smooth Euler-Lagrange, Chern-Weil transgression or null-continuation statements.",
            "Palatini-Holst vacuum equivalence assumes constant real coefficients, nonzero Palatini coefficient, nondegenerate Lorentz coframe and no matter sources or additional action sectors.",
            "Constant extended ungraded trace is locally variationally trivial; global topology, boundary data and quantum phases can still differ.",
            "Action origin, nonzero graded coefficient, coupling normalization, full UBT sectors and RH remain open.",
        ],
        "canonical_claim_status_changes": [],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    for check in CHECKS:
        print(f"PASS {check['id']}: {check['scope']}")
    print(f"{len(CHECKS)} groups passed; LEAN-PENDING.")


if __name__ == "__main__":
    main()
