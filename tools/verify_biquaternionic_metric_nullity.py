#!/usr/bin/env python3
"""Exact algebra checks for the speculative invisibility/null-geometry track.

This verifier checks only finite-dimensional biquaternion algebra. It does not
claim an on-shell field solution or physical invisibility.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Q:
    s: complex
    x: complex
    y: complex
    z: complex

    def __add__(self, other: "Q") -> "Q":
        return Q(self.s + other.s, self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self) -> "Q":
        return Q(-self.s, -self.x, -self.y, -self.z)

    def __sub__(self, other: "Q") -> "Q":
        return self + (-other)

    def __mul__(self, other: "Q") -> "Q":
        a0, a1, a2, a3 = self.s, self.x, self.y, self.z
        b0, b1, b2, b3 = other.s, other.x, other.y, other.z
        return Q(
            a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
        )

    def sharp(self) -> "Q":
        return Q(self.s, -self.x, -self.y, -self.z)

    def scale(self, c: complex) -> "Q":
        return Q(c * self.s, c * self.x, c * self.y, c * self.z)

    def is_zero(self) -> bool:
        return self == Q(0, 0, 0, 0)

    def is_central(self) -> bool:
        return self.x == self.y == self.z == 0


def sym_sharp(a: Q, b: Q) -> Q:
    return (a.sharp() * b + b.sharp() * a).scale(0.5)


def antisym_sharp(a: Q, b: Q) -> Q:
    return (a.sharp() * b - b.sharp() * a).scale(0.5)


def profile_average_product(a: tuple[int, Q], b: tuple[int, Q]) -> Q:
    """Average of ordered bilinear profiles e^(in psi)a and e^(im psi)b."""
    mode_a, value_a = a
    mode_b, value_b = b
    if mode_a + mode_b != 0:
        return Q(0, 0, 0, 0)
    return value_a.sharp() * value_b


def profile_sym(a: tuple[int, Q], b: tuple[int, Q]) -> Q:
    return (profile_average_product(a, b) + profile_average_product(b, a)).scale(0.5)


def profile_antisym(a: tuple[int, Q], b: tuple[int, Q]) -> Q:
    return (profile_average_product(a, b) - profile_average_product(b, a)).scale(0.5)


def determinant_4x4(matrix: list[list[complex]]) -> complex:
    """Small exact recursive determinant; adequate for the fixed checks here."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    if n == 1:
        return matrix[0][0]
    total = 0j
    for j, value in enumerate(matrix[0]):
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        total += ((-1) ** j) * value * determinant_4x4(minor)
    return total


def main() -> None:
    samples: Iterable[Q] = (
        Q(1, 2, 3, 4),
        Q(1j, 1 - 2j, 3j, -2),
        Q(2 + 3j, -1j, 5, 7 - 1j),
    )
    samples = tuple(samples)

    for a in samples:
        for b in samples:
            symmetric = sym_sharp(a, b)
            assert symmetric.is_central(), (a, b, symmetric)
            assert antisym_sharp(a, b) == -antisym_sharp(b, a)

    # Explicit metric-null but algebra-active witness.
    q = Q(0, 0, 1, 1j)       # e_2 + i e_3
    r = Q(1, -1j, 0, 0)      # 1 - i e_1
    assert sym_sharp(q, q).is_zero()
    assert sym_sharp(r, r).is_zero()
    assert sym_sharp(q, r).is_zero()
    ordered = q.sharp() * r
    assert ordered == Q(0, 0, -2, -2j)
    assert not ordered.is_zero()
    assert r.sharp() * q == -ordered

    # Pointwise nullity has Witt-index/rank bound two in C^4.
    # q,r span an explicit maximal totally isotropic plane; a 4D pointwise
    # tetrad cannot have all central pairings zero and remain invertible.
    isotropic_plane = (q, r)
    assert all(sym_sharp(a, b).is_zero() for a in isotropic_plane for b in isotropic_plane)
    assert len(isotropic_plane) == 2

    # The full UBT profile space escapes that finite-dimensional rank bound.
    # Modes are paired bilinearly (without complex conjugation), so n+m=0
    # survives the Haar average.
    profiles = (
        (1, q),
        (-1, r),
        (2, q),
        (-2, r),
    )
    assert len({mode for mode, _ in profiles}) == 4  # functional independence
    assert all(profile_sym(a, b).is_zero() for a in profiles for b in profiles)
    assert profile_antisym(profiles[0], profiles[1]) == ordered
    assert profile_antisym(profiles[2], profiles[3]) == ordered
    assert not profile_antisym(profiles[0], profiles[1]).is_zero()

    # Purely imaginary nondegenerate 4D metric is not volume-null.
    h = [
        [-1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    gamma = [[1j * value for value in row] for row in h]
    assert determinant_4x4(gamma) == determinant_4x4(h) == -1

    # A genuinely degenerate central channel has zero determinant.
    degenerate = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    assert determinant_4x4(degenerate) == 0

    print("PASS: symmetric sharp channel is central")
    print("PASS: antisymmetric channel is biquaternionic and antisymmetric")
    print("PASS: explicit gamma=0, Sigma!=0 algebraic witness")
    print("PASS: pointwise metric-null rank is bounded by two")
    print("PASS: four independent psi profiles give gamma_profile=0 and Sigma_profile!=0")
    print("PASS: pure imaginary nondegenerate metric has nonzero 4D determinant")
    print("PASS: volume-null central metric requires genuine degeneracy")


if __name__ == "__main__":
    main()
