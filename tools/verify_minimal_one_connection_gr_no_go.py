#!/usr/bin/env python3
"""Exact algebraic checks supporting the minimal one-connection GR no-go.

The geometric concurrent-vector and local representer theorems are proved in
LaTeX companion notes. This verifier checks the algebraic hinge between them:
for a metric-compatible connection, contortion and torsion carry the same 24
components and the linear map K -> T is invertible. Thus retaining nonzero
contortion in the *same physical connection* cannot still be called a
Levi-Civita/torsion-free branch.
"""
from __future__ import annotations

import sympy as sp


def pairs(n: int):
    return [(a, b) for a in range(n) for b in range(a + 1, n)]


def contortion_to_torsion_matrix() -> sp.Matrix:
    """Map K_{ab c}=-K_{ba c} to T^a_{cd}=K^a_{d c}-K^a_{c d}.

    Raising/lowering with a nondegenerate diagonal Lorentz metric changes only
    signs and cannot change rank, so the rank computation is performed with
    Kronecker identification of the first index.
    """
    n = 4
    ab = pairs(n)
    cd = pairs(n)
    domain = [(a, b, c) for a, b in ab for c in range(n)]
    codomain = [(a, c, d) for a in range(n) for c, d in cd]
    index = {x: i for i, x in enumerate(domain)}

    def k_coeff(a: int, b: int, c: int):
        if a == b:
            return None, 0
        if a < b:
            return index[(a, b, c)], 1
        return index[(b, a, c)], -1

    m = sp.zeros(len(codomain), len(domain))
    for row, (a, c, d) in enumerate(codomain):
        # T^a_{cd} = K^a_{d c} - K^a_{c d}
        col, sign = k_coeff(a, d, c)
        if col is not None:
            m[row, col] += sign
        col, sign = k_coeff(a, c, d)
        if col is not None:
            m[row, col] -= sign
    return m


def main() -> int:
    m = contortion_to_torsion_matrix()
    checks = {
        "domain_dimension": m.cols == 24,
        "torsion_dimension": m.rows == 24,
        "K_to_T_rank": m.rank() == 24,
        "K_zero_iff_T_zero": len(m.nullspace()) == 0,
    }
    for name, ok in checks.items():
        print(f"[{ 'PASS' if ok else 'FAIL' }] {name}")
    if all(checks.values()):
        print("[PASS] same physical metric-compatible connection: nonzero K implies nonzero torsion")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
