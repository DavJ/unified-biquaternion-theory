#!/usr/bin/env python3
"""Exact regression checks for the pointwise Lorentz-metric congruence orbit."""

from fractions import Fraction as Q


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def det4(m):
    total = Q(0)
    for j in range(4):
        sub = [row[:j] + row[j + 1 :] for row in m[1:]]
        total += (-1) ** j * m[0][j] * det3(sub)
    return total


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def inverse4(a):
    n = 4
    aug = [list(map(Q, row)) + [Q(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for c in range(n):
        pivot = next(r for r in range(c, n) if aug[r][c] != 0)
        aug[c], aug[pivot] = aug[pivot], aug[c]
        p = aug[c][c]
        aug[c] = [x / p for x in aug[c]]
        for r in range(n):
            if r == c:
                continue
            f = aug[r][c]
            aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
    return [row[n:] for row in aug]


def metric(e):
    eta = [[Q(-1), Q(0), Q(0), Q(0)], [Q(0), Q(1), Q(0), Q(0)],
           [Q(0), Q(0), Q(1), Q(0)], [Q(0), Q(0), Q(0), Q(1)]]
    return matmul(matmul(e, eta), transpose(e))


def verify():
    e1 = [[Q(1), Q(0), Q(0), Q(0)],
          [Q(1, 3), Q(2), Q(0), Q(0)],
          [Q(0), Q(1, 5), Q(3), Q(0)],
          [Q(0), Q(0), Q(1, 7), Q(4)]]
    e2 = [[Q(2), Q(1, 2), Q(0), Q(0)],
          [Q(0), Q(3), Q(1, 3), Q(0)],
          [Q(1, 4), Q(0), Q(2), Q(1, 5)],
          [Q(0), Q(1, 6), Q(0), Q(5)]]
    assert det4(e1) != 0 and det4(e2) != 0
    g1, g2 = metric(e1), metric(e2)
    A = matmul(e2, inverse4(e1))
    assert matmul(matmul(A, g1), transpose(A)) == g2
    # det(A g A^T)=det(A)^2 det(g), the density transformation law.
    assert det4(g2) == det4(A) ** 2 * det4(g1)
    print("First-jet Lorentz metric congruence orbit: PASS")


if __name__ == "__main__":
    verify()
