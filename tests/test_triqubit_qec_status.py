from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.verify_triqubit_qec_status import (  # noqa: E402
    X,
    embedding,
    on_qubit,
    scalar_residual,
    verification,
)


def test_single_x_and_y_errors_are_detectable_as_leakage() -> None:
    result = verification()
    assert result.x_detection_max < 1e-12
    assert result.y_detection_max < 1e-12


def test_single_z_errors_are_not_detected_by_occupation_projector() -> None:
    result = verification()
    assert result.z_nonscalar_min > 1e-12


def test_knill_laflamme_fails_for_unknown_single_x_error() -> None:
    result = verification()
    assert result.kl_violation_max > 1e-12


def test_explicit_x1_x2_witness_is_a_color_swap_not_a_scalar() -> None:
    p = embedding()
    compressed = p.conj().T @ on_qubit(X, 0) @ on_qubit(X, 1) @ p
    expected = np.array(
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        dtype=complex,
    )
    assert np.allclose(compressed, expected)
    assert scalar_residual(compressed) > 1e-12


def test_code_dimension_is_three_not_a_qubit_stabilizer_power() -> None:
    result = verification()
    assert result.code_dimension == 3
    assert result.code_dimension & (result.code_dimension - 1) != 0
