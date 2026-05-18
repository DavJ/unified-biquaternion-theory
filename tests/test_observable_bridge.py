# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Tests for disciplined observable bridge scaffold behavior."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ubt.observables.physics_observable_bridge import (  # noqa: E402
    ObservableResult,
    PhysicsObservableBridge,
)


def test_unimplemented_observables_return_open_gap_status() -> None:
    bridge = PhysicsObservableBridge()
    result = bridge.predict_fine_structure_constant()

    assert result.status == "OPEN_GAP"
    assert result.value is None
    assert result.required_derivation


def test_comparison_without_prediction_is_not_treated_as_prediction() -> None:
    bridge = PhysicsObservableBridge()
    cmp_result = bridge.compare_to_reference_data("alpha")

    assert cmp_result["status"] == "OPEN_GAP"
    assert cmp_result["prediction"] is None
    assert cmp_result["reference_value"] is not None


def test_comparison_separates_prediction_from_reference_value() -> None:
    bridge = PhysicsObservableBridge()
    prediction = ObservableResult(
        value=0.0072,
        status="NUMERICAL_EVIDENCE",
        required_derivation=[],
        references=["tests"],
        comparison_target="alpha",
    )

    cmp_result = bridge.compare_to_reference_data("alpha", prediction=prediction)
    assert cmp_result["status"] == "COMPARED"
    assert cmp_result["prediction"] == prediction.value
    assert cmp_result["prediction"] != cmp_result["reference_value"]


def test_predictor_does_not_return_codata_as_ubt_prediction() -> None:
    bridge = PhysicsObservableBridge()
    alpha_result = bridge.predict_fine_structure_constant()

    assert alpha_result.value is None
    assert alpha_result.status == "OPEN_GAP"
