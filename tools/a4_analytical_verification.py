#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Symbolic consistency checks for the a4/theta3 bridge candidate.

This script verifies algebraic identities used in the Gap G137-B a4 note:
1) theta3(0|i) = pi^(1/4)/Gamma(3/4)
2) B_target = 12^(3/2) * 2^(1/8) * theta3(0|i)^(1/4)
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    pi = sp.pi
    theta3 = sp.functions.special.elliptic_functions.jtheta(3, 0, sp.exp(-pi))
    theta3_ramanujan = pi ** sp.Rational(1, 4) / sp.gamma(sp.Rational(3, 4))
    diff_theta = sp.simplify(theta3 - theta3_ramanujan)

    b_from_theta = 12 ** sp.Rational(3, 2) * 2 ** sp.Rational(1, 8) * theta3 ** sp.Rational(1, 4)
    b_from_ramanujan = (
        12 ** sp.Rational(3, 2)
        * 2 ** sp.Rational(1, 8)
        * (pi ** sp.Rational(1, 4) / sp.gamma(sp.Rational(3, 4))) ** sp.Rational(1, 4)
    )
    diff_b = sp.simplify(b_from_theta - b_from_ramanujan)

    print("theta3(0|i) symbolic:", theta3)
    print("theta3 Ramanujan form:", theta3_ramanujan)
    print("theta3 difference (symbolic):", diff_theta)
    print("theta3 difference (numeric):", sp.N(diff_theta, 50))
    print()
    print("B(theta3) symbolic:", b_from_theta)
    print("B(Ramanujan) symbolic:", b_from_ramanujan)
    print("B difference (symbolic):", diff_b)
    print("B difference (numeric):", sp.N(diff_b, 50))
    print("B value (numeric):", sp.N(b_from_theta, 30))


if __name__ == "__main__":
    main()
