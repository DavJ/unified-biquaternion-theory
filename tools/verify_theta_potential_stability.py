#!/usr/bin/env python3
"""Exact witnesses and case checks for the classified UBT Theta potential."""

from fractions import Fraction


def H(a, b, c, d):
    # Restrict witnesses to Gaussian-rational values used below.
    # Represent complex numbers as (re, im) Fraction pairs.
    def abs2(z):
        return z[0] * z[0] + z[1] * z[1]

    def mul(z, w):
        return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

    def conj(z):
        return (z[0], -z[1])

    adbar = mul(a, conj(d))
    return 2 * adbar[0] - abs2(b) - abs2(c)


def D(a, b, c, d):
    def mul(z, w):
        return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

    def sub(z, w):
        return (z[0] - w[0], z[1] - w[1])

    def abs2(z):
        return z[0] * z[0] + z[1] * z[1]

    return abs2(sub(mul(a, d), mul(b, c)))


def r(x):
    return (Fraction(x), Fraction(0))


def i(x):
    return (Fraction(0), Fraction(x))


def witnesses(t=Fraction(3)):
    zero = r(0)
    # nilpotent: [[0,t],[0,0]] => H=-t^2, D=0
    nilpotent = (zero, r(t), zero, zero)
    # phase diagonal: diag(t, i t) => H=0, D=t^4
    phase_diag = (r(t), zero, zero, i(t))
    # identity ray: t I => H=2t^2, D=t^4
    identity = (r(t), zero, zero, r(t))
    # rank-one flat ray: diag(t,0) => H=D=0
    flat = (r(t), zero, zero, zero)
    return nilpotent, phase_diag, identity, flat


def verify():
    t = Fraction(3)
    nilpotent, phase_diag, identity, flat = witnesses(t)
    assert H(*nilpotent) == -t * t and D(*nilpotent) == 0
    assert H(*phase_diag) == 0 and D(*phase_diag) == t**4
    assert H(*identity) == 2 * t * t and D(*identity) == t**4
    assert H(*flat) == 0 and D(*flat) == 0

    # Necessity witnesses for excluded parameter regions.
    # lambda1 < 0: quartic along nilpotent ray tends to -infinity.
    assert H(*nilpotent) ** 2 > 0
    # lambda2 < 0: quartic along phase diagonal tends to -infinity.
    assert D(*phase_diag) > 0
    # lambda1=lambda2=0, sign of m2 is excluded by opposite H rays.
    assert H(*nilpotent) < 0 < H(*identity)

    print("Theta potential stability witnesses: PASS")
    print("flat direction H=D=0: PASS")


if __name__ == "__main__":
    verify()
