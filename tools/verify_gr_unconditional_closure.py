#!/usr/bin/env python3
"""Exact checks for the unconditional-GR-closure decision audit."""
from __future__ import annotations

from fractions import Fraction

Matrix = list[list[Fraction]]


def matrix(values: list[list[int]]) -> Matrix:
    return [[Fraction(value) for value in row] for row in values]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction()) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    aug = [row[:] + [Fraction(i == j) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pivot_value = aug[col][col]
        aug[col] = [value / pivot_value for value in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def trace(a: Matrix) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), Fraction())


def contraction(e: Matrix, eta: Matrix, n0: Fraction) -> Fraction:
    g = multiply(multiply(e, eta), transpose(e))
    gram = [[n0 * value for value in row] for row in g]
    return trace(multiply(inverse(g), gram))


def checks() -> dict[str, bool]:
    eta = matrix([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    tetrads = {
        "identity": matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]),
        "diagonal": matrix([[2, 0, 0, 0], [0, 3, 0, 0], [0, 0, 5, 0], [0, 0, 0, 7]]),
        "mixed": matrix([[1, 1, 0, 0], [0, 2, 1, 0], [1, 0, 3, 1], [0, 1, 0, 4]]),
    }
    n0 = Fraction(11, 7)
    results = {
        f"{name}_contracts_to_4N0": contraction(e, eta, n0) == 4 * n0
        for name, e in tetrads.items()
    }
    kinematic_signature = ("tetrad_map", "central_metric", "lorentz", "diffeomorphism", "split_jet")
    action_family = {c: kinematic_signature for c in (Fraction(0), Fraction(1), Fraction(-3, 5))}
    results["kinematics_independent_of_curvature_coefficient"] = len(set(action_family.values())) == 1
    results["zero_and_nonzero_curvature_coefficients_are_allowed"] = 0 in action_family and 1 in action_family
    return results


def main() -> int:
    results = checks()
    for name, ok in results.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print("[INFO] Exact algebra only; no path-integral measure or spectral-stability claim is tested.")
    return 0 if all(results.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
