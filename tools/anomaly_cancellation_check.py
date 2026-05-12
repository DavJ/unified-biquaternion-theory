#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Check simple anomaly-cancellation sums for one SM-like UBT generation.

Conventions:
- Left-handed Weyl basis with conjugated right-handed singlets:
  Q_L, u_R^c, d_R^c, L_L, e_R^c
- Hypercharge values use PDG normalization:
  (1/6, -2/3, 1/3, -1/2, 1)
- Multiplicities include color and weak components.
"""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    fields = [
        ("Q_L", Fraction(1, 6), 6),      # 3 colors * 2 weak components
        ("u_R^c", Fraction(-2, 3), 3),   # 3 colors
        ("d_R^c", Fraction(1, 3), 3),    # 3 colors
        ("L_L", Fraction(-1, 2), 2),     # 2 weak components
        ("e_R^c", Fraction(1, 1), 1),
    ]

    sum_q = sum(mult * q for _, q, mult in fields)
    sum_q3 = sum(mult * q**3 for _, q, mult in fields)

    print("=== U(1) anomaly checks (one generation) ===")
    for name, q, mult in fields:
        print(f"{name:6} : q={q:>5}, multiplicity={mult}")
    print()
    print(f"Σ q   = {sum_q}   ({float(sum_q):.6f})")
    print(f"Σ q^3 = {sum_q3}   ({float(sum_q3):.6f})")
    print(f"Pass linear  anomaly check (Σq=0):   {sum_q == 0}")
    print(f"Pass cubic   anomaly check (Σq^3=0): {sum_q3 == 0}")
    print()

    # [SU(2)_L]^2 U(1)_Y mixed condition: sum T(2)*Y over SU(2) doublets
    # Q_L contributes with 3 colors, L_L with 1 color.
    mixed = 3 * Fraction(1, 2) * Fraction(1, 6) + 1 * Fraction(1, 2) * Fraction(-1, 2)
    print("=== Mixed [SU(2)_L]^2 U(1)_Y check ===")
    print(f"Σ T(r)*Y = {mixed}   ({float(mixed):.6f})")
    print(f"Pass mixed anomaly check: {mixed == 0}")


if __name__ == "__main__":
    main()
