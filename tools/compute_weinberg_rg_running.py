#!/usr/bin/env python3
"""One-loop Weinberg-angle running from the UBT 3/8 boundary.

This script compares two RG branches:

1. Minimal non-supersymmetric SM running with b1=41/10, b2=-19/6.
   This does not reproduce the observed Z-pole weak mixing angle from the
   3/8 boundary by itself.

2. Twisted odd-spinor / MSSM-like Layer2 threshold running with b1=33/5,
   b2=1.  This is the branch naturally suggested by the odd-winding fermionic
   sector used in the alpha proof.  For M_GUT=2e16 GeV and alpha_GUT^-1 near
   24.3 it gives sin^2(theta_W)(M_Z) close to the observed value.

No experimental value is used to compute the displayed forward predictions.
The final solver line only reports which alpha_GUT^-1 would reproduce the
reference target exactly on the twisted branch.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

MZ = 91.1876
MGUT = 2.0e16
TARGET_SIN2 = 0.23122


@dataclass(frozen=True)
class Branch:
    name: str
    b1: float
    b2: float
    alpha_gut_inv: float


def run_branch(branch: Branch, mgut: float = MGUT, mz: float = MZ):
    L = math.log(mgut / mz) / (2.0 * math.pi)
    alpha1_inv = branch.alpha_gut_inv + branch.b1 * L
    alpha2_inv = branch.alpha_gut_inv + branch.b2 * L
    alpha1 = 1.0 / alpha1_inv
    alpha2 = 1.0 / alpha2_inv
    alpha_y = (3.0 / 5.0) * alpha1
    sin2 = alpha_y / (alpha_y + alpha2)
    alpha_em = alpha_y * alpha2 / (alpha_y + alpha2)
    return {
        "L": L,
        "alpha1_inv_MZ": alpha1_inv,
        "alpha2_inv_MZ": alpha2_inv,
        "alphaY_inv_MZ": 1.0 / alpha_y,
        "alphaEM_inv_MZ": 1.0 / alpha_em,
        "sin2_MZ": sin2,
    }


def solve_alpha_gut_inv_for_target(branch_template: Branch, target: float = TARGET_SIN2):
    lo, hi = 1.0, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        branch = Branch(branch_template.name, branch_template.b1, branch_template.b2, mid)
        s = run_branch(branch)["sin2_MZ"]
        if s > target:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def print_branch(branch: Branch) -> None:
    r = run_branch(branch)
    print(branch.name)
    print("-" * len(branch.name))
    print(f"b1, b2                         = {branch.b1:.12g}, {branch.b2:.12g}")
    print(f"M_GUT                          = {MGUT:.6e} GeV")
    print(f"M_Z                            = {MZ:.6f} GeV")
    print(f"L = ln(M_GUT/M_Z)/(2*pi)       = {r['L']:.12f}")
    print(f"alpha_GUT^-1                   = {branch.alpha_gut_inv:.12f}")
    print(f"alpha1^-1(M_Z)                 = {r['alpha1_inv_MZ']:.12f}")
    print(f"alpha2^-1(M_Z)                 = {r['alpha2_inv_MZ']:.12f}")
    print(f"alphaY^-1(M_Z)                 = {r['alphaY_inv_MZ']:.12f}")
    print(f"alphaEM^-1(M_Z)                = {r['alphaEM_inv_MZ']:.12f}")
    print(f"sin^2(theta_W)(M_Z)            = {r['sin2_MZ']:.12f}")
    print(f"diff from reference 0.23122    = {r['sin2_MZ'] - TARGET_SIN2:+.12f}")
    print()


def main() -> None:
    branches = [
        Branch("Minimal SM one-loop branch", 41.0 / 10.0, -19.0 / 6.0, 40.0),
        Branch("Twisted odd-spinor / MSSM-like branch", 33.0 / 5.0, 1.0, 24.3),
    ]
    for b in branches:
        print_branch(b)

    twisted = branches[1]
    solved = solve_alpha_gut_inv_for_target(twisted)
    solved_branch = Branch(twisted.name + " solved alpha_GUT", twisted.b1, twisted.b2, solved)
    r = run_branch(solved_branch)
    print("Twisted branch exact-reference diagnostic")
    print("-----------------------------------------")
    print(f"alpha_GUT^-1 required for sin^2=0.23122 = {solved:.12f}")
    print(f"alphaEM^-1(M_Z) at that point          = {r['alphaEM_inv_MZ']:.12f}")


if __name__ == "__main__":
    main()
