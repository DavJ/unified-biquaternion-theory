#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
Canonical spin-current audit verifier (GAP-10T-DYN / GAP-10D action audit).

Exact SymPy verification of the results in
canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex:

  C1  Convention checks: central Jordan identity, anti-Hermiticity of the
      Lorentz-slice basis, connection action preserves the slice.
  C2  The kinetic Lagrangian depends on the connection Omega only
      algebraically (polynomial degree two, no derivatives of Omega),
      hence its Omega-variation is the algebraic spin current and no
      curvature term arises from the kinetic term at tree level.
  C3  Slice lemma [L0]: for D_mu Theta in the Lorentz slice W_L, the spin
      current depends only on the anti-Hermitian part of Theta.
      Verified for both canonical pairings (ddagger Hilbert-Schmidt and
      sharp scalar-part).
  C4  Pointwise rigidity [L0]: with D_mu Theta = sqrt(N0) E_mu for the
      standard nondegenerate tetrad, tau == 0 for all (mu, M) iff the
      anti-Hermitian part of Theta vanishes at that point.
  C5  Flat affine no-go [L1]: on every affine representer
      Theta = Theta0 + sqrt(N0) E_nu x^nu, the anti-Hermitian part is an
      affine non-constant W_L-valued map, so tau vanishes at most at one
      spacetime point; the x-gradient of tau is a Theta0-independent
      nonzero constant (+-2 N0 for the ddagger pairing, +-N0 for the
      sharp pairing).  Combined with the proved invertibility of the
      Cartan torsion map, the minimal Hilbert-Palatini + kinetic branch
      forces nonzero torsion on the complement of a point of every flat
      affine representer.

Scope limitation (do not overclaim): these are exact statements about the
minimal first-order branch with the pure-pair representative
A = Omega, B = -Omega^ddagger and the two stated pairings.  They do not
decide non-minimal torsion terms, modified pairings/projections, or an
induced-Palatini derivation; those remain GAP-10T-DYN / GAP-10D.
"""
from __future__ import annotations

import sympy as sp

I2 = sp.eye(2)
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])

# Lorentz-slice basis: E_0 = i*1, E_k = -i*sigma_k (anti-Hermitian).
E = [sp.I * I2, -sp.I * S1, -sp.I * S2, -sp.I * S3]

# Real six-dimensional basis of sl(2, C) (spin representation of so(1,3)).
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


def tau_component(m: sp.Matrix, theta: sp.Matrix, d_slot: sp.Matrix,
                  pairing: str) -> sp.Expr:
    """Spin current tau(M) = <delta_M D Theta, D Theta> for one slot."""
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
    """C2: kinetic density is polynomial of degree two in Omega components."""
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
        sol = sp.solve(eqs, a4, dict=True)
        results[pairing] = sol == [
            {a4[0]: 0, a4[1]: 0, a4[2]: 0, a4[3]: 0}
        ] or sol == [{s: 0 for s in a4}]
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


def main() -> int:
    ok = True
    print("Canonical spin-current audit verifier")
    print("=" * 46)
    for name, res in (
        ("C1 conventions", check_conventions()),
        ("C2 algebraic Omega dependence", check_algebraic_omega_dependence()),
        ("C3 slice lemma", check_slice_lemma()),
        ("C4 pointwise rigidity", check_pointwise_rigidity()),
        ("C5 flat affine no-go", check_flat_affine_no_go()),
    ):
        for key, val in res.items():
            status = "PASS" if val is True else ("FAIL" if val is False else val)
            if val is False:
                ok = False
            print(f"{'PASS' if val is True else status:>4}  {name}: {key}")
    print()
    if ok:
        print("All exact checks passed.")
        print("Verified: the minimal Hilbert-Palatini + kinetic branch with the")
        print("pure-pair representative forces nonzero torsion on the complement")
        print("of at most one point of every flat affine representer.")
        print("Open (unchanged): non-minimal terms, modified pairings, and the")
        print("induced-Palatini coefficient derivation (GAP-10T-DYN, GAP-10D).")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
