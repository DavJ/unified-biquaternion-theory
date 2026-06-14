#!/usr/bin/env python3
"""Reproduce the GUT-normalised Weinberg-angle boundary calculation."""
from fractions import Fraction

reps = [
    ("Q_L", 6, Fraction(1, 6)),
    ("u_R", 3, Fraction(2, 3)),
    ("d_R", 3, Fraction(-1, 3)),
    ("L_L", 2, Fraction(-1, 2)),
    ("e_R", 1, Fraction(-1, 1)),
    ("nu_R", 1, Fraction(0, 1)),
]
S_Y = sum(mult * Y * Y for _, mult, Y in reps)
S_T3 = 3 * Fraction(1, 2) + Fraction(1, 2)
kY = S_Y / S_T3
ratio = Fraction(1, 1) / kY  # g_Y^2/g_2^2 at g1=g2, g1^2=kY gY^2
sin2 = ratio / (1 + ratio)
print(f"sum_Y2 = {S_Y} = {float(S_Y):.12f}")
print(f"sum_T3_2 = {S_T3} = {float(S_T3):.12f}")
print(f"k_Y = {kY} = {float(kY):.12f}")
print(f"gY2_over_g2 = {ratio} = {float(ratio):.12f}")
print(f"sin2_thetaW_GUT = {sin2} = {float(sin2):.12f}")
assert S_Y == Fraction(10, 3)
assert S_T3 == Fraction(2, 1)
assert kY == Fraction(5, 3)
assert ratio == Fraction(3, 5)
assert sin2 == Fraction(3, 8)
