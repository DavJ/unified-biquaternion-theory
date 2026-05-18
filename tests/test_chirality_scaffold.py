# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Tests for chirality/parity algebra scaffold."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tools.dirac_from_biquaternion import biq_gamma_matrices  # noqa: E402
from ubt.algebra.chirality import (  # noqa: E402
    CPTPlaceholder,
    chirality_projectors,
    gamma5,
    parity_conjugation_of_gamma,
    pauli_matrices,
)


def test_pauli_matrices_square_to_identity() -> None:
    pauli = pauli_matrices()
    ident = pauli["0"]
    for axis in ("x", "y", "z"):
        assert np.allclose(pauli[axis] @ pauli[axis], ident)


def test_i_sigma_squares_to_negative_identity() -> None:
    pauli = pauli_matrices()
    ident = pauli["0"]
    for axis in ("x", "y", "z"):
        i_sigma = 1j * pauli[axis]
        assert np.allclose(i_sigma @ i_sigma, -ident)


def test_clifford_anticommutation_is_explicit() -> None:
    gamma = biq_gamma_matrices("dirac")
    eta = np.diag([1.0, -1.0, -1.0, -1.0])
    ident = np.eye(4, dtype=complex)

    for mu in range(4):
        for nu in range(4):
            lhs = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
            rhs = 2.0 * eta[mu, nu] * ident
            assert np.allclose(lhs, rhs)


def test_pseudoscalar_behavior_gamma5() -> None:
    g5 = gamma5("dirac")
    gamma = biq_gamma_matrices("dirac")
    ident = np.eye(4, dtype=complex)

    assert np.allclose(g5 @ g5, ident)
    for mu in range(4):
        assert np.allclose(g5 @ gamma[mu] + gamma[mu] @ g5, np.zeros((4, 4), dtype=complex))


def test_parity_transformation_behavior() -> None:
    gamma = biq_gamma_matrices("dirac")
    assert np.allclose(parity_conjugation_of_gamma(0), gamma[0])
    for i in (1, 2, 3):
        assert np.allclose(parity_conjugation_of_gamma(i), -gamma[i])


def test_chirality_projectors_properties() -> None:
    p_left, p_right = chirality_projectors("dirac")
    ident = np.eye(4, dtype=complex)

    assert np.allclose(p_left @ p_left, p_left)
    assert np.allclose(p_right @ p_right, p_right)
    assert np.allclose(p_left @ p_right, np.zeros((4, 4), dtype=complex))
    assert np.allclose(p_left + p_right, ident)


def test_cpt_placeholder_is_open_gap() -> None:
    cpt = CPTPlaceholder()
    assert cpt.status == "OPEN_GAP"
    with pytest.raises(NotImplementedError):
        cpt.transform(np.zeros(4, dtype=complex))
