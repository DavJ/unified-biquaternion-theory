"""Tests for the natural fermionic SU(3) action on three qubits."""

import numpy as np

from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.fock import (
    I8,
    fermionic_su3_generators,
    jordan_wigner_annihilators,
    number_operator,
    occupation_sector_projector,
    restrict,
    verification_residuals,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.gell_mann import (
    gell_mann_matrices,
    structure_constants,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.mapping import (
    lift_gell_mann,
)

TOL = 1e-12


def test_jordan_wigner_car():
    residuals = verification_residuals()
    assert residuals["car_annihilation"] < TOL
    assert residuals["car_mixed"] < TOL


def test_full_space_su3_algebra():
    assert verification_residuals()["su3_algebra"] < TOL


def test_weight_one_sector_is_fundamental_triplet():
    assert verification_residuals()["w_fundamental"] < TOL


def test_weight_two_sector_is_antifundamental_triplet():
    assert verification_residuals()["anti_w_antifundamental"] < TOL


def test_vacuum_and_filled_sectors_are_singlets():
    assert verification_residuals()["vacuum_and_filled_singlets"] < TOL


def test_fixed_occupation_sectors_are_invariant():
    residuals = verification_residuals()
    assert residuals["occupation_sector_invariance"] < TOL
    assert residuals["number_conservation"] < TOL


def test_one_hot_and_fock_actions_agree_on_w_only():
    fock = fermionic_su3_generators()
    one_hot = [matrix / 2.0 for matrix in lift_gell_mann()]
    w_indices = [4, 2, 1]
    anti_w_indices = [3, 5, 6]

    for a in range(8):
        assert np.allclose(restrict(fock[a], w_indices), restrict(one_hot[a], w_indices))

    assert any(
        not np.allclose(restrict(fock[a], anti_w_indices), restrict(one_hot[a], anti_w_indices))
        for a in range(8)
    )


def test_one_hot_projector_detects_each_single_x_flip():
    annihilators = jordan_wigner_annihilators()
    creators = [operator.conj().T for operator in annihilators]
    x_ops = [annihilators[i] + creators[i] for i in range(3)]
    p_w = occupation_sector_projector(1)
    for x_i in x_ops:
        assert np.linalg.norm(p_w @ x_i @ p_w) < TOL


def test_phase_z_is_not_detected_as_leakage():
    p_w = occupation_sector_projector(1)
    z1 = np.diag([-1 if (index & 4) else 1 for index in range(8)]).astype(complex)
    restricted = p_w @ z1 @ p_w
    assert np.linalg.norm((I8 - p_w) @ z1 @ p_w) < TOL
    assert not np.allclose(restricted, p_w)
