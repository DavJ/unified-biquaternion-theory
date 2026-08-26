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


def gauss_sum_mod_5(k: int) -> complex:
    return sum(
        character_mod_5(k, residue)
        * complex(math.cos(2 * math.pi * residue / 5),
                  math.sin(2 * math.pi * residue / 5))
        for residue in range(1, 5)
    )


def root_number_mod_5(k: int) -> complex:
    parity = k % 2
    return gauss_sum_mod_5(k) / (complex(0, 1) ** parity * math.sqrt(5))


def primitive_functional_equation_matrix():
    epsilon_1 = root_number_mod_5(1)
    epsilon_2 = root_number_mod_5(2)
    epsilon_3 = root_number_mod_5(3)
    return (
        (0j, 0j, epsilon_1),
        (0j, epsilon_2, 0j),
        (epsilon_3, 0j, 0j),
    )


def conjugate_transpose_3(matrix):
    return tuple(tuple(matrix[j][i].conjugate() for j in range(3)) for i in range(3))


def matrices_close_3(left, right, tolerance: float = 1e-12) -> bool:
    return all(
        abs(left[i][j] - right[i][j]) <= tolerance
        for i in range(3)
        for j in range(3)
    )


def check_primitive_functional_equations_mod_5() -> None:
    root_numbers = {k: root_number_mod_5(k) for k in (1, 2, 3)}
    for k, epsilon in root_numbers.items():
        if not math.isclose(abs(gauss_sum_mod_5(k)), math.sqrt(5), abs_tol=1e-12):
            raise AssertionError(("Gauss-sum magnitude", k, gauss_sum_mod_5(k)))
        if not math.isclose(abs(epsilon), 1.0, abs_tol=1e-12):
            raise AssertionError(("root-number magnitude", k, epsilon))
    if abs(root_numbers[2] - 1) > 1e-12:
        raise AssertionError(("quadratic root number", root_numbers[2]))
    if abs(root_numbers[3] - root_numbers[1].conjugate()) > 1e-12:
        raise AssertionError(("conjugate root numbers", root_numbers))

    functional_equation = primitive_functional_equation_matrix()
    identity = ((1 + 0j, 0j, 0j), (0j, 1 + 0j, 0j), (0j, 0j, 1 + 0j))
    if not matrices_close_3(mat_mul(functional_equation, functional_equation), identity):
        raise AssertionError("primitive functional-equation matrix is not involutive")
    if not matrices_close_3(
        mat_mul(conjugate_transpose_3(functional_equation), functional_equation),
        identity,
    ):
        raise AssertionError("primitive functional-equation matrix is not unitary")

    # The phase/conjugation metric has independent odd-pair and quadratic
    # weights.  The functional equation preserves arbitrary unequal values.
    metric = ((3 + 0j, 0j, 0j), (0j, 7 + 0j, 0j), (0j, 0j, 3 + 0j))
    transformed = mat_mul(
        mat_mul(conjugate_transpose_3(functional_equation), metric),
        functional_equation,
    )
    if not matrices_close_3(transformed, metric):
        raise AssertionError("primitive metric is not functional-equation invariant")

    # The principal mod-5 character is imprimitive.  Its completion is
    # f(s) Lambda_zeta(s), and f(s)/f(1-s) is not a constant root number.
    def principal_multiplier(s: float) -> float:
        return 5 ** (s / 2) - 5 ** (-s / 2)

    ratios = tuple(
        principal_multiplier(s) / principal_multiplier(1 - s)
        for s in (1.25, 1.75)
    )
    if math.isclose(ratios[0], ratios[1], rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError(("principal completion unexpectedly has constant epsilon", ratios))


def mat_mul_n(left, right):
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def conjugate_transpose_n(matrix):
    return tuple(
        tuple(matrix[j][i].conjugate() for j in range(len(matrix)))
        for i in range(len(matrix[0]))
    )


def matrices_close_n(left, right, tolerance: float = 1e-11) -> bool:
    return all(
        abs(left[i][j] - right[i][j]) <= tolerance
        for i in range(len(left))
        for j in range(len(left[0]))
    )


def additive_fourier_mod_5():
    root = complex(math.cos(2 * math.pi / 5), math.sin(2 * math.pi / 5))
    return tuple(
        tuple(root ** (r * s) / math.sqrt(5) for s in range(5))
        for r in range(5)
    )


def additive_translation_mod_5():
    root = complex(math.cos(2 * math.pi / 5), math.sin(2 * math.pi / 5))
    return tuple(
        tuple(root ** (r * r) if r == s else 0j for s in range(5))
        for r in range(5)
    )


def additive_reflection_mod_5():
    return tuple(
        tuple(1 + 0j if s == (-r) % 5 else 0j for s in range(5))
        for r in range(5)
    )


def commutant_dimension(generators, dimension: int) -> int:
    constraints = []
    for generator in generators:
        for i in range(dimension):
            for j in range(dimension):
                constraints.append([
                    (generator[b][j] if i == a else 0j)
                    - (generator[i][a] if b == j else 0j)
                    for a in range(dimension)
                    for b in range(dimension)
                ])
    return dimension * dimension - matrix_rank(constraints, tolerance=1e-9)


def check_additive_residue_representation_mod_5() -> None:
    fourier = additive_fourier_mod_5()
    translation = additive_translation_mod_5()
    reflection = additive_reflection_mod_5()
    identity = tuple(
        tuple(1 + 0j if i == j else 0j for j in range(5))
        for i in range(5)
    )
    if not matrices_close_n(
        mat_mul_n(conjugate_transpose_n(fourier), fourier), identity
    ):
        raise AssertionError("additive Fourier matrix is not unitary")
    if not matrices_close_n(mat_mul_n(fourier, fourier), reflection):
        raise AssertionError("additive Fourier square is not residue reflection")
    if not matrices_close_n(
        mat_mul_n(translation, reflection),
        mat_mul_n(reflection, translation),
    ):
        raise AssertionError("translation does not preserve residue parity")
    if commutant_dimension((fourier, translation), 5) != 2:
        raise AssertionError("full additive commutant does not have dimension two")

    # Orthonormal basis of the even sector: e0, (e1+e4)/sqrt(2),
    # (e2+e3)/sqrt(2).  Scalar theta constants at z=0 live here.
    root_two = math.sqrt(2)
    even_basis = (
        (1 + 0j, 0j, 0j),
        (0j, 1 / root_two, 0j),
        (0j, 0j, 1 / root_two),
        (0j, 0j, 1 / root_two),
        (0j, 1 / root_two, 0j),
    )
    even_fourier = mat_mul_n(
        mat_mul_n(conjugate_transpose_n(even_basis), fourier), even_basis
    )
    even_translation = mat_mul_n(
        mat_mul_n(conjugate_transpose_n(even_basis), translation), even_basis
    )
    if commutant_dimension((even_fourier, even_translation), 3) != 1:
        raise AssertionError("even additive commutant is not scalar")

    def residue_theta(residue: int, t: float, cutoff: int = 100) -> float:
        return math.fsum(
            math.exp(-math.pi * t * (5 * n + residue) ** 2 / 5)
            for n in range(-cutoff, cutoff + 1)
        )

    for t in (0.4, 1.0, 2.5):
        for residue in (1, 2):
            if not math.isclose(
                residue_theta(residue, t),
                residue_theta((-residue) % 5, t),
                rel_tol=1e-12,
                abs_tol=1e-12,
            ):
                raise AssertionError(("residue-theta parity", residue, t))


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
    check_primitive_functional_equations_mod_5()
    check_additive_residue_representation_mod_5()
    print("PASS: S-matrix involution/eigenchannels, boundary multiplier zeros, "
          "open-strip nonvanishing, three Mellin-series checks, and rank-four "
          "mod-5 character channels with exhaustive symmetry-admissible "
          "metric, functional-equation, and additive-residue classifications")


if __name__ == "__main__":
    main()
