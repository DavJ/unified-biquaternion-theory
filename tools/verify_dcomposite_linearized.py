#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
Linearized self-consistent D-composite audit verifier (GAP-10T-DYN).

Exact checks for canonical/gr_closure/gap_10t_dcomposite_linearized.tex:

  L0  W_L subsector lemma: imposing Theta in W_L defines a consistent
      Lorentz-real subsector (Hermitian part forced to zero when W_L
      preservation is demanded for EVERY independently chosen connection).
      Necessity for self-consistent solutions is NOT proved: the constant
      Hermitian shift Theta_aff + H at a constant tetrad (Omega[E] = 0)
      is an explicit counterexample, verified in check L0b.
  D1  Corrected linearized Levi-Civita spin connection annihilates every
      exact-gradient tetrad perturbation (regression test for the
      delta-e index transposition bug caught on 2026-07-26).
  D2  Operator identity A^3 = (lambda . s) A^2, proved symbolically in all
      eight variables; hence spec A = {0, q} with q = lambda . s.
  D3  Generic ranks: rank A = 9, rank A^2 = 6; char poly t^10 (t - q)^6;
      det(I - A) = (1 - q)^6; unique solvability iff q != 1.
  D4  Off resonance the unique delta-Theta-driven solution is the exact
      gradient F = d(theta); zero anholonomy (pullback-flat at linear
      order).
  D5  Resonant sector at q = 1: the eigenspace is exactly six-dimensional
      (= dim so(1,3)); every resonant mode is anholonomic and their curls
      are linearly independent (rank 6).

Scope (do not overclaim): frozen-coefficient analysis of the linearization
at the affine point, in the W_L subsector, using the real-exponential
(Laplace-type) symbol d_mu -> s_mu with REAL s.  For real Fourier modes
d_mu -> i k_mu the invariant is q = i lambda.k, so q = 1 has no real-k
solution: the six-dimensional sector consists of exponential/evanescent
symbol modes, and its relation to real-frequency propagation is open.
What is proved is modewise invertibility of the frozen full symbol for
q != 1, not local or global uniqueness for the variable-coefficient PDE.
The assembly across the moving surface (x0 + theta0) . s = 1, the
quadratic action on the sector, gauge counting, ghost analysis, on-shell
torsion, and the chain-rule spin current remain open inside GAP-10T-DYN.
"""
from __future__ import annotations

import random

import sympy as sp

I2 = sp.eye(2)
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
E = [sp.I * I2, -sp.I * S1, -sp.I * S2, -sp.I * S3]
SL2 = [S1 / 2, S2 / 2, S3 / 2, sp.I * S1 / 2, sp.I * S2 / 2, sp.I * S3 / 2]
ETA = sp.diag(-1, 1, 1, 1)

S_SYM = sp.symbols("s0:4", real=True)
L_SYM = sp.symbols("l0:4", real=True)
F_SYM = sp.symbols("F0:16", real=True)
Q_SYM = sum(L_SYM[a] * S_SYM[a] for a in range(4))


def dag(x):
    return x.conjugate().T


def coords(x):
    return [
        sp.simplify(-sp.I * sp.trace(x) / 2),
        sp.simplify(sp.I * sp.trace(S1 * x) / 2),
        sp.simplify(sp.I * sp.trace(S2 * x) / 2),
        sp.simplify(sp.I * sp.trace(S3 * x) / 2),
    ]


def check_sector_lemma():
    """L0: W_L closure under EVERY connection forces H = 0 (subsector
    consistency).  L0b: necessity fails - explicit counterexample."""
    h = sp.symbols("h0:4", real=True)
    herm = sp.Matrix([[h[0], h[1] + sp.I * h[2]], [h[1] - sp.I * h[2], h[3]]])
    eqs = []
    for w in SL2:
        r = w * herm + herm * dag(w)
        sym = sp.expand(r + dag(r))
        eqs += [sym[i, j] for i in range(2) for j in range(2)]
    sol = sp.solve(eqs, h, dict=True)
    # L0b: constant Hermitian shift at constant tetrad keeps D Theta in W_L
    x = sp.symbols("x0:4", real=True)
    n0 = sp.symbols("N0", positive=True)
    theta = herm + sp.sqrt(n0) * sum((E[a] * x[a] for a in range(4)), sp.zeros(2, 2))
    d_in_wl = all(
        sp.simplify(sp.diff(theta, x[mu]).conjugate().T + sp.diff(theta, x[mu]))
        == sp.zeros(2, 2)
        for mu in range(4)
    )
    return {
        "hermitian_part_forced_zero_under_all_connections": sol == [{v: 0 for v in h}],
        "necessity_counterexample_D_in_WL_with_Theta_not_in_WL": d_in_wl,
    }


def _rep_generators():
    gens = []
    for m in SL2:
        cols = [coords(sp.expand(m * E[b] + E[b] * dag(m))) for b in range(4)]
        gens.append(sp.Matrix(4, 4, lambda a, b: cols[b][a]))
    return gens


def _rep_inv_factory():
    gens = _rep_generators()
    basis = sp.Matrix(
        [[gens[j][a, b] for j in range(6)] for a in range(4) for b in range(4)]
    )

    def rep_inv(k):
        vec = sp.Matrix([k[a, b] for a in range(4) for b in range(4)])
        sol = basis.solve_least_squares(vec)
        resid = sp.simplify(basis * sol - vec)
        assert all(r == 0 for r in resid), "matrix not in the so(1,3) image"
        m = sp.zeros(2, 2)
        for j in range(6):
            m = m + sol[j] * SL2[j]
        return m

    return rep_inv


def linearized_spin_connection(f, s):
    """Corrected linearized Levi-Civita omega^1_mu^{ab} at identity tetrad.

    f[mu][a] are tetrad perturbation components; d_nu -> s_nu plane-wave
    symbol.  delta e_{sigma mu} = eta_{mu c} f^c_sigma (index order matters:
    the 2026-07-26 transposition bug used eta_{sigma c} f^c_mu and thereby
    leaked the symmetric part into the connection).
    """
    om = [[[sp.S(0)] * 4 for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for a in range(4):
            for b in range(4):
                t1 = sum(
                    ETA[a, nu] * (s[mu] * f[nu][b] - s[nu] * f[mu][b])
                    for nu in range(4)
                ) / 2
                t2 = sum(
                    ETA[b, nu] * (s[mu] * f[nu][a] - s[nu] * f[mu][a])
                    for nu in range(4)
                ) / 2
                t3 = sum(
                    ETA[r, a]
                    * ETA[p, b]
                    * (
                        s[r] * sum(ETA[mu, c] * f[p][c] for c in range(4))
                        - s[p] * sum(ETA[mu, c] * f[r][c] for c in range(4))
                    )
                    for r in range(4)
                    for p in range(4)
                ) / 2
                om[mu][a][b] = sp.expand(t1 - t2 - t3)
    return om


def assemble_symbol():
    """Frozen symbol A(s, lambda) of the linearized D-composite system."""
    rep_inv = _rep_inv_factory()
    f = [[F_SYM[4 * mu + a] for a in range(4)] for mu in range(4)]
    om = linearized_spin_connection(f, S_SYM)
    lam_m = sp.zeros(2, 2)
    for a in range(4):
        lam_m = lam_m + L_SYM[a] * E[a]
    a_mat = sp.zeros(16, 16)
    for mu in range(4):
        k = sp.Matrix(
            4, 4, lambda a, b: sum(ETA[b, c] * om[mu][a][c] for c in range(4))
        )
        m = rep_inv(k)
        g = coords(sp.expand(m * lam_m + lam_m * dag(m)))
        for a in range(4):
            expr = sp.expand(g[a])
            for j in range(16):
                a_mat[4 * mu + a, j] = sp.expand(sp.diff(expr, F_SYM[j]))
    return a_mat


def _draw(seed):
    random.seed(seed)
    return {
        v: sp.Rational(random.randint(-4, 4), random.randint(1, 3))
        for v in list(S_SYM) + list(L_SYM)
    }


def check_gradient_annihilation(a_mat, seed=3):
    sub = _draw(seed)
    an = a_mat.subs(sub)
    sv = [sub[S_SYM[m]] for m in range(4)]
    ok = True
    for a0 in range(4):
        v = sp.zeros(16, 1)
        for mu in range(4):
            v[4 * mu + a0] = sv[mu]
        if not (an * v).is_zero_matrix:
            ok = False
    return {"gradients_in_kernel": ok}


def check_operator_identity(a_mat):
    a2 = sp.expand(a_mat * a_mat)
    r = sp.expand(a_mat * a2 - Q_SYM * a2)
    bad = sum(
        1
        for i in range(16)
        for j in range(16)
        if sp.simplify(r[i, j]) != 0
    )
    return {"A3_equals_qA2_symbolic": bad == 0}


def check_generic_ranks(a_mat, seed=61):
    sub = _draw(seed)
    an = a_mat.subs(sub)
    a2 = an * an
    qn = Q_SYM.subs(sub)
    d = (sp.eye(16) - an).det()
    return {
        "rank_A_is_9": an.rank() == 9,
        "rank_A2_is_6": a2.rank() == 6,
        "det_I_minus_A_is_(1-q)^6": sp.simplify(d - (1 - qn) ** 6) == 0,
    }


def check_off_resonance_flatness(a_mat, seed=21):
    sub = _draw(seed)
    qn = Q_SYM.subs(sub)
    assert qn != 1
    an = a_mat.subs(sub)
    sv = [sub[S_SYM[m]] for m in range(4)]
    th = sp.symbols("th0:4", real=True)
    rhs = sp.zeros(16, 1)
    for mu in range(4):
        for a in range(4):
            rhs[4 * mu + a] = sv[mu] * th[a]
    sol = (sp.eye(16) - an).LUsolve(rhs)
    exact = all(
        sp.simplify(sol[4 * mu + a] * sv[nu] - sol[4 * nu + a] * sv[mu]) == 0
        for a in range(4)
        for mu in range(4)
        for nu in range(mu + 1, 4)
    )
    driven_is_gradient = all(
        sp.simplify(sol[4 * mu + a] - sv[mu] * th[a]) == 0
        for a in range(4)
        for mu in range(4)
    )
    return {
        "driven_solution_is_exact_gradient": driven_is_gradient,
        "zero_anholonomy_off_resonance": exact,
    }


def check_resonant_sector(a_mat):
    sub = {
        L_SYM[0]: sp.Rational(1, 2),
        L_SYM[1]: sp.Rational(1, 3),
        L_SYM[2]: sp.Rational(-1, 4),
        L_SYM[3]: sp.Rational(1, 5),
        S_SYM[0]: 1,
        S_SYM[1]: 1,
        S_SYM[2]: 1,
        S_SYM[3]: sp.Rational(25, 12),
    }
    assert Q_SYM.subs(sub) == 1
    an = a_mat.subs(sub)
    sv = [sub[S_SYM[m]] for m in range(4)]
    eig = (an - sp.eye(16)).nullspace()
    rows = []
    all_anholonomic = True
    for v in eig:
        row = []
        nz = 0
        for a in range(4):
            for mu in range(4):
                for nu in range(mu + 1, 4):
                    h = sp.simplify(v[4 * mu + a] * sv[nu] - v[4 * nu + a] * sv[mu])
                    row.append(h)
                    if h != 0:
                        nz += 1
        if nz == 0:
            all_anholonomic = False
        rows.append(row)
    return {
        "resonant_eigenspace_dim_6": len(eig) == 6,
        "all_resonant_modes_anholonomic": all_anholonomic,
        "resonant_curl_rank_6": sp.Matrix(rows).rank() == 6,
    }


def check_trace_theorem(a_mat):
    """D2b: tr A^k = 6 q^k for k = 1,2,3 symbolically.  With the minimal
    polynomial dividing t^2 (t - q) this pins char poly = t^10 (t - q)^6,
    hence det(I - A) = (1 - q)^6 as a theorem, not a sampled fact."""
    a2 = sp.expand(a_mat * a_mat)
    a3 = sp.expand(a_mat * a2)
    t1 = sp.simplify(sp.trace(a_mat) - 6 * Q_SYM)
    t2 = sp.simplify(sp.trace(a2) - 6 * Q_SYM ** 2)
    t3 = sp.simplify(sp.trace(a3) - 6 * Q_SYM ** 3)
    return {"traces_6qk_symbolic": (t1 == 0) and (t2 == 0) and (t3 == 0)}


def _resonant_points():
    return [
        {
            L_SYM[0]: sp.Rational(1, 2), L_SYM[1]: sp.Rational(1, 3),
            L_SYM[2]: sp.Rational(-1, 4), L_SYM[3]: sp.Rational(1, 5),
            S_SYM[0]: 1, S_SYM[1]: 1, S_SYM[2]: 1, S_SYM[3]: sp.Rational(25, 12),
        },
        {
            L_SYM[0]: 1, L_SYM[1]: 0, L_SYM[2]: 0, L_SYM[3]: 0,
            S_SYM[0]: 1, S_SYM[1]: sp.Rational(1, 2), S_SYM[2]: 0, S_SYM[3]: 0,
        },
        {
            L_SYM[0]: sp.Rational(-1, 3), L_SYM[1]: sp.Rational(2, 3),
            L_SYM[2]: sp.Rational(1, 2), L_SYM[3]: 1,
            S_SYM[0]: 0, S_SYM[1]: 1, S_SYM[2]: sp.Rational(2, 3), S_SYM[3]: 0,
        },
    ]


def check_resonant_multipoint(a_mat):
    """D5b: dim 6 and full curl rank at several exact resonant points."""
    ok_dim, ok_rank = True, True
    for sub in _resonant_points():
        assert Q_SYM.subs(sub) == 1
        an = a_mat.subs(sub)
        sv = [sub[S_SYM[m]] for m in range(4)]
        eig = (an - sp.eye(16)).nullspace()
        if len(eig) != 6:
            ok_dim = False
            continue
        rows = []
        for v in eig:
            rows.append([
                sp.simplify(v[4 * mu + a] * sv[nu] - v[4 * nu + a] * sv[mu])
                for a in range(4) for mu in range(4) for nu in range(mu + 1, 4)
            ])
        if sp.Matrix(rows).rank() != 6:
            ok_rank = False
    return {"dim6_at_all_points": ok_dim, "curl_rank6_at_all_points": ok_rank}


def check_resonant_riemann_image(a_mat):
    """D5c: resonant modes have nonzero linearized curvature image
    R^1_{mu nu}{}^{ab} = s_mu om^1_nu{}^{ab} - s_nu om^1_mu{}^{ab}."""
    sub = _resonant_points()[0]
    an = a_mat.subs(sub)
    sv = [sub[S_SYM[m]] for m in range(4)]
    eig = (an - sp.eye(16)).nullspace()
    nonzero_modes = 0
    for v in eig:
        f = [[v[4 * mu + a] for a in range(4)] for mu in range(4)]
        om = linearized_spin_connection(f, sv)
        nz = any(
            sp.simplify(sv[mu] * om[nu][a][b] - sv[nu] * om[mu][a][b]) != 0
            for mu in range(4) for nu in range(mu + 1, 4)
            for a in range(4) for b in range(4)
        )
        if nz:
            nonzero_modes += 1
    return {"all_resonant_modes_have_nonzero_linear_riemann": nonzero_modes == 6}


def main() -> int:
    ok = True
    print("Linearized D-composite audit verifier")
    print("=" * 46)
    a_mat = assemble_symbol()
    for name, res in (
        ("L0 sector lemma", check_sector_lemma()),
        ("D1 gradient annihilation", check_gradient_annihilation(a_mat)),
        ("D2 operator identity", check_operator_identity(a_mat)),
        ("D2b trace theorem", check_trace_theorem(a_mat)),
        ("D3 generic ranks", check_generic_ranks(a_mat)),
        ("D4 off-resonance flatness", check_off_resonance_flatness(a_mat)),
        ("D5 resonant sector", check_resonant_sector(a_mat)),
        ("D5b resonant multipoint", check_resonant_multipoint(a_mat)),
        ("D5c resonant Riemann image", check_resonant_riemann_image(a_mat)),
    ):
        for key, val in res.items():
            if val is not True:
                ok = False
            print(f"{'PASS' if val is True else 'FAIL':>4}  {name}: {key}")
    print()
    if ok:
        print("All exact checks passed.")
        print("In the frozen W_L subsector with the real-exponential symbol,")
        print("driven modes off q = 1 are exactly holonomic (pullback-flat).")
        print("All linearized anholonomy lives in the six-dimensional")
        print("exponential symbol sector at q = 1, whose modes carry nonzero")
        print("linearized Riemann image.  Relation to real-frequency")
        print("propagation, gauge/ghost content, quadratic action, on-shell")
        print("torsion, and variable-coefficient assembly remain open.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
