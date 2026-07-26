#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
Canonical spin-current and pairing audit verifier
(GAP-10T-DYN / GAP-10D action audit).

Exact SymPy verification of the results in
canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex:

  C1  Convention checks: central Jordan identity, anti-Hermiticity of the
      Lorentz-slice basis, connection action preserves the slice.
  C2  The fixed-background kinetic Lagrangian depends on the independent
      connection Omega only algebraically (polynomial degree two, no
      derivatives of Omega).  Hence its Omega-variation is an algebraic
      Palatini matter current and no curvature term arises from that kinetic
      term at tree level.
  C3  Slice lemma [L0]: for D_mu Theta in the Lorentz slice W_L, the fixed-
      tetrad spin current depends only on the anti-Hermitian part of Theta.
      Verified for the ddagger Hilbert--Schmidt corpus pairing and the sharp
      scalar-part pairing.
  C4  Pointwise rigidity [L0]: with D_mu Theta = sqrt(N0) E_mu for the
      standard nondegenerate tetrad, tau == 0 for all (mu, M) iff the
      anti-Hermitian part of Theta vanishes at that point.
  C5  Flat affine no-go [L1]: on every affine representer
      Theta = Theta0 + sqrt(N0) E_nu x^nu, the anti-Hermitian part is an
      affine non-constant W_L-valued map, so tau vanishes at at most one
      spacetime point; the x-gradient of tau is a Theta0-independent nonzero
      constant (+-2 N0 for the ddagger pairing, +-N0 for the sharp pairing).
  C6  Lorentz-invariant pairing rigidity [L1]: every real symmetric bilinear
      form on W_L invariant under the full sl(2,C) Lorentz action is a scalar
      multiple of eta = diag(-1,1,1,1).  The sharp pairing realizes eta.  The
      ddagger Hilbert--Schmidt pairing realizes a Euclidean matrix and fails
      boost invariance.  Therefore no nonzero nondegenerate Lorentz-invariant
      pairing choice can remove C5.

Scope limitation (do not overclaim): the current formula holds for the
independent Palatini/effective variation in which e, g, the volume form and
Theta are fixed while Omega varies.  If e is first imposed as the composite
jet D Theta / sqrt(N0), the induced variations of g, sqrt(-g), index raising
and any composite connection must also be included.  This verifier does not
compute that full Theta-only composite variation and does not derive the
Hilbert--Palatini term or its coefficient.
"""
from __future__ import annotations

import sympy as sp

I2 = sp.eye(2)
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
SIGMA = [S1, S2, S3]

# Lorentz-slice basis: E_0 = i*1, E_k = -i*sigma_k (anti-Hermitian).
E = [sp.I * I2, -sp.I * S1, -sp.I * S2, -sp.I * S3]

# Real six-dimensional basis of sl(2, C) (boosts followed by rotations).
SL2 = [S1 / 2, S2 / 2, S3 / 2, sp.I * S1 / 2, sp.I * S2 / 2, sp.I * S3 / 2]

N0 = sp.symbols("N0", positive=True)


def dag(x: sp.Matrix) -> sp.Matrix:
    """ddagger involution: Hermitian conjugation."""
    return x.conjugate().T


def sharp(x: sp.Matrix) -> sp.Matrix:
    """sharp involution: 2x2 adjugate, X^sharp = tr(X) 1 - X."""
    return sp.trace(x) * I2 - x


def msum(terms) -> sp.Matrix:
    total = sp.zeros(2, 2)
    for term in terms:
        total = total + term
    return total


def generic_theta(prefix: str = "t"):
    t = sp.symbols(f"{prefix}0:8", real=True)
    theta = sp.Matrix(
        [
            [t[0] + sp.I * t[1], t[2] + sp.I * t[3]],
            [t[4] + sp.I * t[5], t[6] + sp.I * t[7]],
        ]
    )
    return theta, t


def slice_coordinates(x: sp.Matrix) -> sp.Matrix:
    """Return real coordinates in E_0=i1, E_k=-i sigma_k for x in W_L."""
    return sp.Matrix(
        [
            sp.simplify(-sp.I * sp.trace(x) / 2),
            *[sp.simplify(sp.I * sp.trace(s * x) / 2) for s in SIGMA],
        ]
    )


def lorentz_slice_generator(m: sp.Matrix) -> sp.Matrix:
    """4x4 infinitesimal Lorentz matrix induced by X -> M X + X M^dag."""
    columns = []
    for basis_vector in E:
        moved = sp.simplify(m * basis_vector + basis_vector * dag(m))
        columns.append(slice_coordinates(moved))
    return sp.Matrix.hstack(*columns)


def pairing_matrix(pairing: str) -> sp.Matrix:
    """Matrix of a corpus pairing restricted to the Lorentz slice."""
    g = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            if pairing == "ddagger":
                raw = sp.trace(dag(E[a]) * E[b])
            elif pairing == "sharp":
                raw = sp.Rational(1, 2) * sp.trace(sharp(E[a]) * E[b])
            else:  # pragma: no cover
                raise ValueError(f"unknown pairing {pairing!r}")
            g[a, b] = sp.simplify(sp.re(raw))
    return g


def tau_component(m: sp.Matrix, theta: sp.Matrix, d_slot: sp.Matrix,
                  pairing: str) -> sp.Expr:
    """Fixed-background current tau(M)=<delta_M DTheta,DTheta> for one slot."""
    delta_d = m * theta + theta * dag(m)
    if pairing == "ddagger":
        raw = sp.trace(dag(delta_d) * d_slot)
    elif pairing == "sharp":
        raw = sp.Rational(1, 2) * sp.trace(sharp(delta_d) * d_slot)
    else:  # pragma: no cover - guarded by callers
        raise ValueError(f"unknown pairing {pairing!r}")
    return sp.simplify(sp.re(sp.expand(raw)))


def check_conventions() -> dict[str, bool]:
    x = sp.symbols("x0:4", real=True)
    y = sp.symbols("y0:4", real=True)
    big_x = msum(x[a] * E[a] for a in range(4))
    big_y = msum(y[a] * E[a] for a in range(4))
    eta = -x[0] * y[0] + sum(x[k] * y[k] for k in (1, 2, 3))
    jordan = sp.simplify(
        sp.Rational(1, 2) * (sharp(big_x) * big_y + sharp(big_y) * big_x)
        - eta * I2
    ) == sp.zeros(2, 2)
    antiherm = all(
        sp.simplify(dag(ea) + ea) == sp.zeros(2, 2) for ea in E
    )
    slice_preserved = all(
        sp.simplify(dag(m * big_x + big_x * dag(m)) + (m * big_x + big_x * dag(m)))
        == sp.zeros(2, 2)
        for m in SL2
    )
    return {
        "central_jordan": jordan,
        "slice_antihermitian": antiherm,
        "connection_preserves_slice": slice_preserved,
    }


def check_algebraic_omega_dependence() -> dict[str, bool]:
    """C2: fixed-background kinetic density is degree two in Omega."""
    theta, _ = generic_theta()
    w = sp.symbols("w0:6", real=True)
    omega = msum(w[j] * SL2[j] for j in range(6))
    d_theta = omega * theta + theta * dag(omega)  # connection part of D Theta
    density = sp.re(sp.expand(sp.trace(dag(d_theta) * d_theta)))
    poly = sp.Poly(sp.expand(density), *w)
    return {
        "polynomial_in_omega": True,
        "degree_two": poly.total_degree() == 2,
    }


def check_slice_lemma() -> dict[str, bool]:
    theta, _ = generic_theta()
    d = sp.symbols("d0:4", real=True)
    d_slot = msum(d[a] * E[a] for a in range(4))
    anti = (theta - dag(theta)) / 2
    results = {}
    for pairing in ("ddagger", "sharp"):
        results[pairing] = all(
            sp.simplify(
                tau_component(m, theta, d_slot, pairing)
                - tau_component(m, anti, d_slot, pairing)
            )
            == 0
            for m in SL2
        )
    return results


def check_pointwise_rigidity() -> dict[str, bool]:
    """C4: joint kernel over all four tetrad slots is anti-Herm part == 0."""
    a4 = sp.symbols("a0:4", real=True)
    anti = msum(a4[i] * E[i] for i in range(4))
    results = {}
    for pairing in ("ddagger", "sharp"):
        eqs = [
            tau_component(m, anti, sp.sqrt(N0) * E[mu], pairing)
            for mu in range(4)
            for m in SL2
        ]
        coefficient_matrix, _ = sp.linear_eq_to_matrix(eqs, a4)
        results[pairing] = coefficient_matrix.rank() == 4
    return results


def check_flat_affine_no_go() -> dict[str, object]:
    theta0, t = generic_theta()
    xc = sp.symbols("X0:4", real=True)
    theta = theta0 + sp.sqrt(N0) * msum(E[a] * xc[a] for a in range(4))
    out: dict[str, object] = {}
    for pairing, expected in (("ddagger", {2 * N0, -2 * N0}),
                              ("sharp", {N0, -N0})):
        grads = set()
        theta0_independent = True
        for mu in range(4):
            d_slot = sp.sqrt(N0) * E[mu]
            for m in SL2:
                val = tau_component(m, theta, d_slot, pairing)
                for nu in range(4):
                    g = sp.simplify(sp.diff(val, xc[nu]))
                    if any(sym in g.free_symbols for sym in t):
                        theta0_independent = False
                    if g != 0:
                        grads.add(g)
        out[f"{pairing}_gradient_theta0_independent"] = theta0_independent
        out[f"{pairing}_nonzero_gradients"] = grads == expected
    return out


def check_lorentz_invariant_pairings() -> dict[str, bool]:
    """C6: classify real symmetric invariant bilinear forms on W_L."""
    generators = [lorentz_slice_generator(m) for m in SL2]
    eta = sp.diag(-1, 1, 1, 1)

    # Generic symmetric matrix, ordered by upper-triangular entries.
    gv = sp.symbols("g00 g01 g02 g03 g11 g12 g13 g22 g23 g33", real=True)
    g00, g01, g02, g03, g11, g12, g13, g22, g23, g33 = gv
    generic_g = sp.Matrix(
        [
            [g00, g01, g02, g03],
            [g01, g11, g12, g13],
            [g02, g12, g22, g23],
            [g03, g13, g23, g33],
        ]
    )
    equations = []
    for j in generators:
        equations.extend(list(j.T * generic_g + generic_g * j))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, gv)
    nullspace = coefficient_matrix.nullspace()
    expected = sp.Matrix([-1, 0, 0, 0, 1, 0, 0, 1, 0, 1])
    unique_eta = (
        len(nullspace) == 1
        and sp.Matrix.hstack(nullspace[0], expected).rank() == 1
    )

    g_dd = pairing_matrix("ddagger")
    g_sh = pairing_matrix("sharp")
    dd_invariant_all = all(
        sp.simplify(j.T * g_dd + g_dd * j) == sp.zeros(4, 4)
        for j in generators
    )
    dd_rotation_invariant = all(
        sp.simplify(j.T * g_dd + g_dd * j) == sp.zeros(4, 4)
        for j in generators[3:]
    )
    dd_all_boosts_fail = all(
        sp.simplify(j.T * g_dd + g_dd * j) != sp.zeros(4, 4)
        for j in generators[:3]
    )
    sharp_invariant = all(
        sp.simplify(j.T * g_sh + g_sh * j) == sp.zeros(4, 4)
        for j in generators
    )

    return {
        "unique_symmetric_form_is_eta": unique_eta,
        "sharp_matrix_is_eta": g_sh == eta,
        "sharp_full_lorentz_invariant": sharp_invariant,
        "ddagger_matrix_is_euclidean": g_dd == 2 * sp.eye(4),
        "ddagger_rotation_invariant": dd_rotation_invariant,
        "ddagger_all_boosts_fail": dd_all_boosts_fail,
        "ddagger_not_full_lorentz_invariant": not dd_invariant_all,
    }


def check_composite_flat_admissibility(fast: bool = False) -> dict[str, bool]:
    """C7: auxiliary exact-gradient restriction admits the flat affine map.

    In the gradient-composite torsion-free scheme (tetrad defined from the
    slice coordinates of d Theta, V == 0, Lorentz-real variations) the first
    variation of every action term vanishes identically at the affine
    background, for all Lambda, kappa, N0:

      * S_kin + Lambda term are volume functionals of the induced metric;
        their first variation is a total divergence against the constant
        background jet (verified by exact box integration of a polynomial
        boundary-vanishing variation);
      * the Einstein term first variation is eps e e d(delta omega) with
        constant e, hence exact (verified by exact box integration of the
        linearised Levi-Civita spin connection unless fast=True).

    This verifies the affine-stationarity corollary only.  Since an exact
    coframe e^a=dY^a/sqrt(N0) induces a locally flat pullback metric, the
    restriction is a flatness no-go rather than a surviving curved-GR
    branch.  The canonical self-consistent D-composite scheme remains open.
    """
    x = sp.symbols("x0:4", real=True)
    eta_m = sp.diag(-1, 1, 1, 1)
    bump = sp.prod([(1 - x[m] ** 2) ** 2 for m in range(4)])
    # deterministic polynomial slice-valued variation (linear + quadratic)
    coeffs = [
        1 + x[0] - 2 * x[1] + x[2] * x[3],
        -1 + 2 * x[2] + x[0] * x[1],
        x[3] - x[0] + x[1] ** 2,
        2 - x[1] + x[0] * x[2],
    ]
    d_theta = sp.expand(bump * msum(coeffs[a] * E[a] for a in range(4)))

    def pair_sharp(a_m, b_m):
        return sp.re(sp.expand(sp.Rational(1, 2) * sp.trace(sharp(a_m) * b_m)))

    d_vol = sp.S(0)
    for m in range(4):
        for n in range(4):
            dh = pair_sharp(sp.sqrt(N0) * E[m], sp.diff(d_theta, x[n])) + pair_sharp(
                sp.diff(d_theta, x[m]), sp.sqrt(N0) * E[n]
            )
            d_vol += sp.Rational(1, 2) * eta_m[m, n] * dh / N0
    box = [(x[m], -1, 1) for m in range(4)]
    vol_ok = sp.simplify(sp.integrate(sp.expand(d_vol), *box)) == 0

    out = {"volume_terms_first_variation_vanishes": vol_ok}
    if fast:
        return out

    # linearised Levi-Civita spin connection of the varied tetrad
    de = [[sp.S(0)] * 4 for _ in range(4)]
    for mu in range(4):
        c = slice_coordinates(sp.diff(d_theta, x[mu]))
        for a in range(4):
            de[mu][a] = c[a]

    def dif(mu, expr):
        return sp.diff(expr, x[mu])

    om1 = [[[sp.S(0)] * 4 for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for a in range(4):
            for b in range(4):
                t1 = sum(
                    eta_m[a, nu] * (dif(mu, de[nu][b]) - dif(nu, de[mu][b]))
                    for nu in range(4)
                ) / 2
                t2 = sum(
                    eta_m[b, nu] * (dif(mu, de[nu][a]) - dif(nu, de[mu][a]))
                    for nu in range(4)
                ) / 2
                t3 = sum(
                    eta_m[r, a]
                    * eta_m[s, b]
                    * (
                        dif(r, sum(eta_m[s, c] * de[c][mu] for c in range(4)))
                        - dif(s, sum(eta_m[r, c] * de[c][mu] for c in range(4)))
                    )
                    for r in range(4)
                    for s in range(4)
                ) / 2
                om1[mu][a][b] = sp.expand(t1 - t2 - t3)

    def lc4(i, j, k, l):
        p = [i, j, k, l]
        if len(set(p)) < 4:
            return 0
        sign = 1
        for ii in range(4):
            for jj in range(3 - ii):
                if p[jj] > p[jj + 1]:
                    p[jj], p[jj + 1] = p[jj + 1], p[jj]
                    sign = -sign
        return sign

    d_eh = sp.S(0)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for e_idx in range(4):
                    eabcd = lc4(a, b, c, e_idx)
                    if eabcd == 0:
                        continue
                    mu, nu = a, b  # background tetrad is the identity
                    for r in range(4):
                        for s in range(4):
                            emnrs = lc4(mu, nu, r, s)
                            if emnrs == 0:
                                continue
                            omcd = sum(
                                eta_m[c, p] * eta_m[e_idx, q] * om1[s][p][q]
                                for p in range(4)
                                for q in range(4)
                            )
                            d_eh += eabcd * emnrs * dif(r, omcd)
    eh_ok = sp.simplify(sp.integrate(sp.expand(d_eh), *box)) == 0
    out["einstein_term_first_variation_vanishes"] = eh_ok
    return out


def main() -> int:
    ok = True
    print("Canonical spin-current and pairing audit verifier")
    print("=" * 52)
    for name, res in (
        ("C1 conventions", check_conventions()),
        ("C2 algebraic Omega dependence", check_algebraic_omega_dependence()),
        ("C3 slice lemma", check_slice_lemma()),
        ("C4 pointwise rigidity", check_pointwise_rigidity()),
        ("C5 flat affine no-go", check_flat_affine_no_go()),
        ("C6 Lorentz-invariant pairings", check_lorentz_invariant_pairings()),
        ("C7 auxiliary gradient-affine stationarity", check_composite_flat_admissibility()),
    ):
        for key, val in res.items():
            status = "PASS" if val is True else ("FAIL" if val is False else val)
            if val is False:
                ok = False
            print(f"{'PASS' if val is True else status:>4}  {name}: {key}")
    print()
    if ok:
        print("All exact checks passed.")
        print("Verified: the fixed-background minimal Hilbert-Palatini + kinetic")
        print("branch forces nonzero torsion away from at most one point of every")
        print("flat affine representer.  The unique nondegenerate symmetric")
        print("Lorentz-invariant slice pairing is the sharp/Minkowski pairing up")
        print("to scale, so pairing selection alone cannot remove the obstruction.")
        print("Open: the full composite Theta-only variation, non-minimal torsion")
        print("terms or relative/translational completion, and induced Palatini.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
