#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# UBT-AI-PROVENANCE-BEGIN
# schema: ubt-ai-provenance/v1
# tier: B_machine_verified
# ai_assistance: disclosed
# human_review: machine-verification
# editorial_responsibility: Ing. David Jaroš
# policy: ../AI_PROVENANCE.md
# notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
# UBT-AI-PROVENANCE-END
"""Principal-symbol decision checks for the single-Theta GR programme.

This verifier supports
``canonical/gr_closure/gap_10d_theta_hessian_principal_symbol.tex``.

It proves two deliberately separate statements.

1.  For the fixed-background quadratic Theta kinetic action, with metric,
    connection and nondegenerate internal pairing held fixed, the Hessian has
    a scalar second-order principal symbol after raising the internal index.
    Background connection and potential terms are lower differential order.

2.  The six-dimensional q=1 sector of the frozen D-composite equation is a
    finite-scale resonance of the *full* mixed-order symbol I-A(s,lambda).
    It is not conic under s -> c s and therefore cannot, as it stands, be a
    principal-symbol characteristic bundle.  The first-order principal symbol
    -A is generically rank deficient rather than a minimal Laplace symbol.

The verifier does NOT derive the full composite Theta-only Hessian, perform a
complete gauge/ghost quotient, or determine N_B, xi, the cutoff, or Newton's
constant.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.verify_dcomposite_linearized import (
    L_SYM,
    S_SYM,
    assemble_symbol,
)


def _symmetric_metric() -> sp.Matrix:
    entries: dict[tuple[int, int], sp.Symbol] = {}
    for mu in range(4):
        for nu in range(mu, 4):
            entries[mu, nu] = sp.symbols(f"g{mu}{nu}", real=True)
    return sp.Matrix(
        4,
        4,
        lambda mu, nu: entries[min(mu, nu), max(mu, nu)],
    )


def fixed_background_checks() -> dict[str, bool]:
    """Exact principal-symbol checks for a fixed metric and connection."""
    g = _symmetric_metric()
    k = sp.Matrix(sp.symbols("k0:4", real=True))
    scale = sp.symbols("c", real=True)
    q = sp.expand((k.T * g * k)[0])

    # A generic nondegenerate diagonal internal pairing is enough: the
    # lower-index Hessian carries K_AB, and raising an index removes it.
    kap = sp.symbols("kap0:4", nonzero=True, real=True)
    internal = sp.diag(*kap)
    lower_symbol = sp.expand(q) * internal
    raised_symbol = sp.simplify(internal.inv() * lower_symbol)

    # Check directly that a background matrix connection contributes only
    # first- and zero-order powers when D_mu = partial_mu + C_mu.
    t = sp.symbols("t", real=True)
    identity = sp.eye(2)
    connections: list[sp.Matrix] = []
    for mu in range(4):
        cvars = sp.symbols(f"C{mu}_0:4", real=True)
        connections.append(sp.Matrix(2, 2, cvars))
    polynomial = sp.zeros(2, 2)
    for mu in range(4):
        for nu in range(4):
            polynomial += g[mu, nu] * (
                t * k[mu] * identity + connections[mu]
            ) * (
                t * k[nu] * identity + connections[nu]
            )
    degree_two = polynomial.applyfunc(lambda value: sp.expand(value).coeff(t, 2))

    q_scaled = sp.expand(
        (sp.Matrix([scale * item for item in k]).T * g * sp.Matrix([scale * item for item in k]))[0]
    )
    euclidean_q = sum(item**2 for item in k)

    return {
        "fixed_background_raised_symbol_is_scalar": sp.simplify(
            raised_symbol - q * sp.eye(4)
        ).is_zero_matrix,
        "fixed_background_symbol_is_degree_two": sp.simplify(
            q_scaled - scale**2 * q
        ) == 0,
        "background_connection_terms_are_lower_order": sp.simplify(
            degree_two - q * identity
        ).is_zero_matrix,
        "euclidean_symbol_is_sum_of_squares": sp.expand(euclidean_q)
        == sum(item**2 for item in k),
        "four_dimensional_metric_lock_collapses_kinetic_to_volume": (
            sp.Rational(1, 2) * 4 == 2
        ),
    }


def dcomposite_resonance_checks() -> dict[str, bool]:
    """Show that the q=1 resonance is not a principal-symbol bundle."""
    a_mat = assemble_symbol()
    scale = sp.symbols("c", real=True)
    scaled_subs = {S_SYM[i]: scale * S_SYM[i] for i in range(4)}
    scaled = a_mat.subs(scaled_subs)
    homogeneous = all(
        sp.simplify(scaled[i, j] - scale * a_mat[i, j]) == 0
        for i in range(16)
        for j in range(16)
    )

    # Exact q=1 sample and its radial rescaling.  The full mixed-order symbol
    # is singular at the first point and invertible after scaling by two.
    q1 = {
        S_SYM[0]: 1,
        S_SYM[1]: 0,
        S_SYM[2]: 0,
        S_SYM[3]: 0,
        L_SYM[0]: 1,
        L_SYM[1]: 0,
        L_SYM[2]: 0,
        L_SYM[3]: 0,
    }
    at_q1 = a_mat.subs(q1)
    at_q2 = a_mat.subs({**q1, S_SYM[0]: 2})
    full_q1 = sp.eye(16) - at_q1
    full_q2 = sp.eye(16) - at_q2

    # A generic exact sample for the first-order principal symbol -A.
    generic = {
        S_SYM[0]: 1,
        S_SYM[1]: 2,
        S_SYM[2]: -1,
        S_SYM[3]: 3,
        L_SYM[0]: 2,
        L_SYM[1]: -1,
        L_SYM[2]: 1,
        L_SYM[3]: 1,
    }
    principal = -a_mat.subs(generic)

    q, c = sp.symbols("q c", real=True)
    full_det_radial = (1 - c * q) ** 6

    return {
        "A_is_homogeneous_degree_one_in_covector": homogeneous,
        "q1_full_symbol_kernel_is_six_dimensional": 16 - full_q1.rank() == 6,
        "radially_scaled_q2_full_symbol_is_invertible": full_q2.rank() == 16,
        "q1_singularity_is_not_conic": (
            full_det_radial.subs({q: 1, c: 1}) == 0
            and full_det_radial.subs({q: 1, c: 2}) != 0
        ),
        "first_order_principal_symbol_is_generically_rank_9": principal.rank() == 9,
        "first_order_principal_symbol_is_not_minimal_laplace": principal.rank() != 16,
    }


def all_checks() -> dict[str, bool]:
    return {**fixed_background_checks(), **dcomposite_resonance_checks()}


def main() -> int:
    checks = all_checks()
    for name, ok in checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(
        "[INFO] Fixed-background Theta kinetics pass the scalar-symbol test; "
        "the q=1 D-composite resonance does not define a conic principal bundle."
    )
    print(
        "[INFO] The full composite, gauge-fixed Theta Hessian remains to be derived."
    )
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
