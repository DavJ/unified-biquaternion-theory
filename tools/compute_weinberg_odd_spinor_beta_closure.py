#!/usr/bin/env python3
"""Compute the UBT odd-spinor threshold beta coefficients and Weinberg closure.

The threshold spectrum is the minimal N=1-like odd-spinor Layer2 spectrum:
three SM chiral generations plus a conjugate electroweak doublet pair H_u,H_d.
For gauge multiplets, b_i = -3 C_2(G_i) + sum_chiral T_i(R).
For U(1)_Y the GUT-normalised index is T_1=(3/5) Y^2 times multiplicity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math

MZ = 91.1876
MUBT = 2.0e16
ALPHA_EM_INV_MZ = 127.934499434164  # UBT/QED-compatible Z-pole input used in the closure note
TARGET_SIN2 = 0.23122


@dataclass(frozen=True)
class ChiralField:
    name: str
    su3_dim: int
    su2_dim: int
    hypercharge: Fraction
    generations: int = 1

    def t1(self) -> Fraction:
        multiplicity = self.su3_dim * self.su2_dim * self.generations
        return Fraction(3, 5) * self.hypercharge * self.hypercharge * multiplicity

    def t2(self) -> Fraction:
        if self.su2_dim == 1:
            return Fraction(0)
        if self.su2_dim == 2:
            return Fraction(1, 2) * self.su3_dim * self.generations
        raise ValueError(f"Unsupported SU(2) dimension for {self.name}")

    def t3(self) -> Fraction:
        if self.su3_dim == 1:
            return Fraction(0)
        if self.su3_dim == 3:
            return Fraction(1, 2) * self.su2_dim * self.generations
        raise ValueError(f"Unsupported SU(3) dimension for {self.name}")


FIELDS = [
    ChiralField("Q", 3, 2, Fraction(1, 6), 3),
    ChiralField("u^c", 3, 1, Fraction(-2, 3), 3),
    ChiralField("d^c", 3, 1, Fraction(1, 3), 3),
    ChiralField("L", 1, 2, Fraction(-1, 2), 3),
    ChiralField("e^c", 1, 1, Fraction(1, 1), 3),
    ChiralField("H_u", 1, 2, Fraction(1, 2), 1),
    ChiralField("H_d", 1, 2, Fraction(-1, 2), 1),
]


def beta_coefficients():
    sum_t1 = sum((f.t1() for f in FIELDS), Fraction(0))
    sum_t2 = sum((f.t2() for f in FIELDS), Fraction(0))
    sum_t3 = sum((f.t3() for f in FIELDS), Fraction(0))
    b1 = sum_t1
    b2 = sum_t2 - 3 * 2  # C2(SU2)=2
    b3 = sum_t3 - 3 * 3  # C2(SU3)=3
    return sum_t1, sum_t2, sum_t3, b1, b2, b3


def rg_closure(alpha_em_inv_mz: float = ALPHA_EM_INV_MZ, m_ubt: float = MUBT, mz: float = MZ):
    _, _, _, b1, b2, _ = beta_coefficients()
    b1f = float(b1)
    b2f = float(b2)
    L = math.log(m_ubt / mz) / (2.0 * math.pi)
    # alpha_em^-1 = alpha_Y^-1 + alpha_2^-1
    # alpha_Y^-1 = (5/3) alpha_1^-1, alpha_i^-1 = A + b_i L
    # => alpha_em^-1 = (8/3) A + ((5/3)b1+b2)L
    alpha_gut_inv = Fraction(3, 8) * (alpha_em_inv_mz - ((5.0 / 3.0) * b1f + b2f) * L)
    alpha_gut_inv = float(alpha_gut_inv)
    alpha1_inv = alpha_gut_inv + b1f * L
    alpha2_inv = alpha_gut_inv + b2f * L
    alpha_y_inv = (5.0 / 3.0) * alpha1_inv
    sin2 = alpha2_inv / alpha_em_inv_mz  # alpha_EM/alpha_2 = alpha_2^{-1}/alpha_EM^{-1}
    return {
        "L": L,
        "alpha_gut_inv": alpha_gut_inv,
        "alpha1_inv": alpha1_inv,
        "alpha2_inv": alpha2_inv,
        "alphaY_inv": alpha_y_inv,
        "alphaEM_inv": alpha_em_inv_mz,
        "sin2": sin2,
    }


def main() -> None:
    print("Odd-spinor Layer2 threshold spectrum")
    print("=====================================")
    for f in FIELDS:
        print(f"{f.name:4s} gen={f.generations} dim=({f.su3_dim},{f.su2_dim}) Y={f.hypercharge} "
              f"T1={f.t1()} T2={f.t2()} T3={f.t3()}")
    sum_t1, sum_t2, sum_t3, b1, b2, b3 = beta_coefficients()
    print()
    print(f"sum T1(chiral) = {sum_t1} = {float(sum_t1):.12f}")
    print(f"sum T2(chiral) = {sum_t2} = {float(sum_t2):.12f}")
    print(f"sum T3(chiral) = {sum_t3} = {float(sum_t3):.12f}")
    print(f"b1 = {b1} = {float(b1):.12f}")
    print(f"b2 = {b2} = {float(b2):.12f}")
    print(f"b3 = {b3} = {float(b3):.12f}")
    print()
    r = rg_closure()
    print("Z-pole closure from alpha_EM(M_Z) and M_UBT")
    print("-------------------------------------------")
    print(f"M_UBT                    = {MUBT:.6e} GeV")
    print(f"M_Z                      = {MZ:.6f} GeV")
    print(f"L                        = {r['L']:.12f}")
    print(f"alpha_EM^-1(M_Z)         = {r['alphaEM_inv']:.12f}")
    print(f"alpha_UBT^-1             = {r['alpha_gut_inv']:.12f}")
    print(f"alpha1^-1(M_Z)           = {r['alpha1_inv']:.12f}")
    print(f"alpha2^-1(M_Z)           = {r['alpha2_inv']:.12f}")
    print(f"alphaY^-1(M_Z)           = {r['alphaY_inv']:.12f}")
    print(f"sin^2(theta_W)(M_Z)      = {r['sin2']:.12f}")
    print(f"diff from 0.23122        = {r['sin2'] - TARGET_SIN2:+.12f}")


if __name__ == "__main__":
    main()
