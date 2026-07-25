"""
fock.py – Natural fermionic SU(3) action on a three-qubit Fock space.

The three qubits are interpreted as occupations of three fermionic modes.  The
Jordan–Wigner bilinears

    T_a = sum_ij c_i† (lambda_a/2)_ij c_j

provide an 8-dimensional representation of su(3) with decomposition

    Lambda^0 C^3 ⊕ Lambda^1 C^3 ⊕ Lambda^2 C^3 ⊕ Lambda^3 C^3
      = 1 ⊕ 3 ⊕ 3bar ⊕ 1.

This is distinct from the one-hot lift L_a = P lambda_a P†, which acts trivially
outside the weight-1 sector.
"""

from __future__ import annotations

import numpy as np

from .gell_mann import gell_mann_matrices, structure_constants


I2 = np.eye(2, dtype=complex)
I8 = np.eye(8, dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
ANNIHILATION = np.array([[0, 1], [0, 0]], dtype=complex)


def _tensor3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(np.kron(a, b), c)


def jordan_wigner_annihilators() -> list[np.ndarray]:
    """Return annihilation operators c_1,c_2,c_3 in big-endian qubit order."""
    return [
        _tensor3(ANNIHILATION, I2, I2),
        _tensor3(Z, ANNIHILATION, I2),
        _tensor3(Z, Z, ANNIHILATION),
    ]


def number_operator() -> np.ndarray:
    """Return N = sum_i c_i† c_i."""
    operators = jordan_wigner_annihilators()
    return sum(c.conj().T @ c for c in operators)


def fermionic_su3_generators() -> list[np.ndarray]:
    """Return T_a = c_i† (lambda_a/2)_ij c_j as eight 8x8 matrices."""
    c = jordan_wigner_annihilators()
    cd = [operator.conj().T for operator in c]
    generators = []
    for lam in gell_mann_matrices():
        generator = np.zeros((8, 8), dtype=complex)
        for i in range(3):
            for j in range(3):
                generator += (lam[i, j] / 2.0) * (cd[i] @ c[j])
        generators.append(generator)
    return generators


def occupation_sector_indices(number: int) -> list[int]:
    """Computational-basis indices with the requested occupation number."""
    if number not in (0, 1, 2, 3):
        raise ValueError("occupation number must be 0, 1, 2, or 3")
    return [index for index in range(8) if index.bit_count() == number]


def occupation_sector_projector(number: int) -> np.ndarray:
    """Orthogonal projector onto the fixed-occupation sector N=number."""
    projector = np.zeros((8, 8), dtype=complex)
    for index in occupation_sector_indices(number):
        projector[index, index] = 1.0
    return projector


def restrict(matrix: np.ndarray, indices: list[int]) -> np.ndarray:
    """Restrict a matrix to an ordered list of computational-basis indices."""
    return matrix[np.ix_(indices, indices)]


def verification_residuals() -> dict[str, float]:
    """Return numerical residuals for CAR, su(3), and the irrep decomposition."""
    c = jordan_wigner_annihilators()
    cd = [operator.conj().T for operator in c]
    generators = fermionic_su3_generators()
    fundamental = [lam / 2.0 for lam in gell_mann_matrices()]
    f = structure_constants()

    zero = np.zeros((8, 8), dtype=complex)
    car_ann = max(
        np.linalg.norm(c[i] @ c[j] + c[j] @ c[i])
        for i in range(3) for j in range(3)
    )
    car_mix = max(
        np.linalg.norm(c[i] @ cd[j] + cd[j] @ c[i] - (I8 if i == j else zero))
        for i in range(3) for j in range(3)
    )

    su3 = 0.0
    for a in range(8):
        for b in range(8):
            lhs = generators[a] @ generators[b] - generators[b] @ generators[a]
            rhs = 1j * sum(f[a, b, d] * generators[d] for d in range(8))
            su3 = max(su3, np.linalg.norm(lhs - rhs))

    w_indices = [4, 2, 1]  # |100>, |010>, |001> in r,g,b order
    anti_w_indices = [3, 5, 6]  # |011>, |101>, |110>
    orientation = np.diag([1, -1, 1]).astype(complex)

    w = max(
        np.linalg.norm(restrict(generators[a], w_indices) - fundamental[a])
        for a in range(8)
    )
    anti_w = max(
        np.linalg.norm(
            orientation.conj().T
            @ restrict(generators[a], anti_w_indices)
            @ orientation
            + fundamental[a].conj()
        )
        for a in range(8)
    )
    singlets = max(
        abs(generators[a][index, index])
        for a in range(8) for index in (0, 7)
    )
    sector_invariance = max(
        np.linalg.norm(
            generators[a] @ occupation_sector_projector(n)
            - occupation_sector_projector(n) @ generators[a]
        )
        for a in range(8) for n in range(4)
    )
    number_conservation = max(
        np.linalg.norm(generators[a] @ number_operator() - number_operator() @ generators[a])
        for a in range(8)
    )

    return {
        "car_annihilation": float(car_ann),
        "car_mixed": float(car_mix),
        "su3_algebra": float(su3),
        "w_fundamental": float(w),
        "anti_w_antifundamental": float(anti_w),
        "vacuum_and_filled_singlets": float(singlets),
        "occupation_sector_invariance": float(sector_invariance),
        "number_conservation": float(number_conservation),
    }
