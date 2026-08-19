#!/usr/bin/env python3
"""Independent exact-arithmetic cross-check for the action-order note.

No SymPy/NumPy is used.  This checks the same core logic in a different
formulation using integer/Fraction arithmetic and characteristic polynomials.
"""

from fractions import Fraction


def quadratic_second_difference(a: Fraction, v: Fraction) -> Fraction:
    def kinetic(x: Fraction) -> Fraction:
        return Fraction(1, 2) * a * x * x

    return kinetic(v + 1) - 2 * kinetic(v) + kinetic(v - 1)


def second_order_characteristic(lam: int, m: int) -> int:
    return (lam - m) * (lam + m)


def first_order_plus_characteristic(lam: int, m: int) -> int:
    return lam + m


def determinant_diagonal(values):
    result = 1
    for value in values:
        result *= value
    return result


def main() -> None:
    # Exact discrete Hessian of a v^2/2 at arbitrary rational point.
    a = Fraction(7, 3)
    v = Fraction(11, 5)
    assert quadratic_second_difference(a, v) == a
    assert a != 0

    # Factorized second-order characteristic equation admits both roots ±m,
    # while the + first-order factor admits only -m.
    m = 5
    assert second_order_characteristic(+m, m) == 0
    assert second_order_characteristic(-m, m) == 0
    assert first_order_plus_characteristic(-m, m) == 0
    assert first_order_plus_characteristic(+m, m) != 0

    # Independent diagonal Kronecker determinant instance.
    # diag(2,3) ⊗ diag(5,7) = diag(10,14,15,21).
    det = determinant_diagonal([10, 14, 15, 21])
    expected = (2 * 3) ** 2 * (5 * 7) ** 2
    assert det == expected
    assert det != 0

    print("PASS: independent exact-arithmetic generalized-Dirac action-order checks")


if __name__ == "__main__":
    main()
