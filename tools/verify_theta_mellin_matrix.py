#!/usr/bin/env python3
"""Checks for the joint Mellin analysis of theta2, theta3, and theta4.

This verifies classical identities only; it neither derives a UBT kernel nor tests RH.
"""

from __future__ import annotations

import math


S_MATRIX = ((0, 0, 1), (0, 1, 0), (1, 0, 0))
UNITS_MOD_5 = (1, 2, 4, 3)


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(3)) for row in matrix)


def mat_mul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def check_s_matrix() -> None:
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    if mat_mul(S_MATRIX, S_MATRIX) != identity:
        raise AssertionError("S is not an involution")
    eigenpairs = (((0, 1, 0), 1), ((1, 0, 1), 1), ((1, 0, -1), -1))
    for vector, eigenvalue in eigenpairs:
        expected = tuple(eigenvalue * entry for entry in vector)
        if mat_vec(S_MATRIX, vector) != expected:
            raise AssertionError(("S eigenchannel", vector, eigenvalue))


def mellin_multipliers(s: complex) -> tuple[complex, complex, complex]:
    return (2**s - 1, 1 + 0j, 1 - 2 ** (1 - s))


def check_boundary_zero_lines(samples: range = range(-5, 6)) -> None:
    log2 = math.log(2.0)
    for k in samples:
        left = 2j * math.pi * k / log2
        right = 1 + 2j * math.pi * k / log2
        if abs(2**left - 1) > 2e-13:
            raise AssertionError(("theta2 multiplier zero", k))
        if abs(1 - 2 ** (1 - right)) > 2e-13:
            raise AssertionError(("theta4 multiplier zero", k))


def check_open_strip_nonvanishing() -> None:
    for real in (0.1, 0.25, 0.5, 0.75, 0.9):
        for imag in (-30.0, -7.0, 0.0, 11.0, 29.0):
            m2, _, m4 = mellin_multipliers(complex(real, imag))
            if abs(m2) < 1e-10 or abs(m4) < 1e-10:
                raise AssertionError(("unexpected interior multiplier zero", real, imag))


def zeta_real(s: float, cutoff: int = 400_000) -> float:
    total = math.fsum(n ** (-s) for n in range(1, cutoff + 1))
    tail = cutoff ** (1 - s) / (s - 1) + 0.5 * cutoff ** (-s)
    return total + tail


def transformed_series(s: float, cutoff: int = 400_000) -> tuple[float, float, float]:
    zeta = zeta_real(s, cutoff)
    factor = math.pi ** (-s / 2) * math.gamma(s / 2)
    return (
        factor * (2**s - 1) * zeta,
        factor * zeta,
        factor * (1 - 2 ** (1 - s)) * zeta,
    )


def independent_series(s: float, cutoff: int = 400_000) -> tuple[float, float, float]:
    factor = math.pi ** (-s / 2) * math.gamma(s / 2)
    half_integer = math.fsum((n + 0.5) ** (-s) for n in range(cutoff))
    half_integer += (cutoff + 0.5) ** (1 - s) / (s - 1)
    ordinary = zeta_real(s, cutoff)
    alternating = math.fsum(((-1) ** (n - 1)) * n ** (-s) for n in range(1, cutoff + 1))
    return factor * half_integer, factor * ordinary, factor * alternating


def check_mellin_series(tolerance: float = 2e-6) -> None:
    for s in (2.0, 2.5, 3.0):
        expected = transformed_series(s)
        observed = independent_series(s)
        for channel, (lhs, rhs) in enumerate(zip(observed, expected), start=2):
            if not math.isclose(lhs, rhs, rel_tol=tolerance, abs_tol=tolerance):
                raise AssertionError(("Mellin channel", channel, s, lhs, rhs))


def character_mod_5(k: int, n: int) -> complex:
    residue = n % 5
    if residue == 0:
        return 0j
    exponent = UNITS_MOD_5.index(residue)
    return complex(0, 1) ** (k * exponent)


def character_matrix_mod_5() -> tuple[tuple[complex, ...], ...]:
    return tuple(
        tuple(character_mod_5(k, residue) for residue in UNITS_MOD_5)
        for k in range(4)
    )


def conjugate_transpose(matrix):
    return tuple(tuple(matrix[j][i].conjugate() for j in range(4)) for i in range(4))


def mat_mul_4(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4))
        for i in range(4)
    )


def matrix_rank(matrix, tolerance: float = 1e-12) -> int:
    work = [list(row) for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if abs(work[row][column]) > tolerance),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [entry / pivot_value for entry in work[rank]]
        for row in range(len(work)):
            if row != rank:
                factor = work[row][column]
                work[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[rank])
                ]
        rank += 1
    return rank


def check_character_channels_mod_5() -> None:
    matrix = character_matrix_mod_5()
    gram = mat_mul_4(matrix, conjugate_transpose(matrix))
    expected = tuple(
        tuple((4 + 0j) if i == j else 0j for j in range(4))
        for i in range(4)
    )
    if gram != expected:
        raise AssertionError(("character orthogonality", gram))
    if matrix_rank(matrix) != 4:
        raise AssertionError("mod-5 character matrix does not have rank four")
    for k in range(4):
        if character_mod_5(k, -1) != complex((-1) ** k, 0):
            raise AssertionError(("character parity", k, character_mod_5(k, -1)))
    for n in range(1, 100):
        principal = character_mod_5(0, n)
        expected_principal = 0j if n % 5 == 0 else 1 + 0j
        if principal != expected_principal:
            raise AssertionError(("principal character", n))


def check_principal_l_factor(s: float = 2.5, cutoff: int = 400_000) -> None:
    lhs = math.fsum(n ** (-s) for n in range(1, cutoff + 1) if n % 5)
    rhs = (1 - 5 ** (-s)) * zeta_real(s, cutoff)
    if not math.isclose(lhs, rhs, rel_tol=2e-6, abs_tol=2e-6):
        raise AssertionError(("principal L factor", lhs, rhs))


def phase_matrix_mod_5():
    return tuple(
        tuple((complex(0, 1) ** i) if i == j else 0j for j in range(4))
        for i in range(4)
    )


def conjugation_permutation():
    return (
        (1 + 0j, 0j, 0j, 0j),
        (0j, 0j, 0j, 1 + 0j),
        (0j, 0j, 1 + 0j, 0j),
        (0j, 1 + 0j, 0j, 0j),
    )


def cyclic_shift():
    return (
        (0j, 0j, 0j, 1 + 0j),
        (1 + 0j, 0j, 0j, 0j),
        (0j, 1 + 0j, 0j, 0j),
        (0j, 0j, 1 + 0j, 0j),
    )


def diagonal_metric(g0: float, g1: float, g2: float):
    values = (g0, g1, g2, g1)
    return tuple(
        tuple(complex(values[i], 0) if i == j else 0j for j in range(4))
        for i in range(4)
    )


def conjugate_matrix(matrix):
    return tuple(tuple(entry.conjugate() for entry in row) for row in matrix)


def matrices_close(left, right, tolerance: float = 1e-12) -> bool:
    return all(
        abs(left[i][j] - right[i][j]) <= tolerance
        for i in range(4)
        for j in range(4)
    )


def matrix_unit(row: int, column: int):
    return [
        [1.0 if (i, j) == (row, column) else 0.0 for j in range(4)]
        for i in range(4)
    ]


def check_metric_classification() -> None:
    phase = phase_matrix_mod_5()
    conjugation = conjugation_permutation()
    shift = cyclic_shift()

    # The four phase eigenvalues are distinct.  Checking all sixteen matrix
    # units proves that D^dagger G D = G retains exactly the diagonal modes.
    surviving_modes = set()
    for row in range(4):
        for column in range(4):
            unit = matrix_unit(row, column)
            transformed = mat_mul_4(
                mat_mul_4(conjugate_transpose(phase), unit),
                phase,
            )
            if matrices_close(transformed, unit):
                surviving_modes.add((row, column))
    if surviving_modes != {(0, 0), (1, 1), (2, 2), (3, 3)}:
        raise AssertionError(
            f"unexpected phase-invariant matrix modes: {surviving_modes}"
        )

    # On diagonal Hermitian matrices the antiunitary permutation fixes 0 and
    # 2 and exchanges 1 with 3, leaving precisely three real parameters.
    diagonal_orbits = []
    unseen = {0, 1, 2, 3}
    permutation = {0: 0, 1: 3, 2: 2, 3: 1}
    while unseen:
        index = min(unseen)
        orbit = frozenset({index, permutation[index]})
        diagonal_orbits.append(orbit)
        unseen -= orbit
    if set(diagonal_orbits) != {
        frozenset({0}),
        frozenset({2}),
        frozenset({1, 3}),
    }:
        raise AssertionError(f"unexpected conjugation orbits: {diagonal_orbits}")

    metric = diagonal_metric(2.0, 3.0, 5.0)
    phase_invariant = mat_mul_4(
        mat_mul_4(conjugate_transpose(phase), metric),
        phase,
    )
    if not matrices_close(phase_invariant, metric):
        raise AssertionError("phase invariance failed")
    conjugation_compatible = mat_mul_4(
        mat_mul_4(conjugate_transpose(conjugation), metric),
        conjugation,
    )
    if not matrices_close(conjugation_compatible, conjugate_matrix(metric)):
        raise AssertionError("conjugation compatibility failed")
    if matrices_close(
        mat_mul_4(mat_mul_4(conjugate_transpose(shift), metric), shift),
        metric,
    ):
        raise AssertionError("unequal weights unexpectedly have cyclic symmetry")
    scalar_metric = diagonal_metric(7.0, 7.0, 7.0)
    if not matrices_close(
        mat_mul_4(mat_mul_4(conjugate_transpose(shift), scalar_metric), shift),
        scalar_metric,
    ):
        raise AssertionError("scalar metric lacks cyclic symmetry")


def main() -> None:
    check_s_matrix()
    check_boundary_zero_lines()
    check_open_strip_nonvanishing()
    check_mellin_series()
    check_character_channels_mod_5()
    check_principal_l_factor()
    check_metric_classification()
    print("PASS: S-matrix involution/eigenchannels, boundary multiplier zeros, "
          "open-strip nonvanishing, three Mellin-series checks, and rank-four "
          "mod-5 character channels with symmetry-admissible metrics")


if __name__ == "__main__":
    main()
