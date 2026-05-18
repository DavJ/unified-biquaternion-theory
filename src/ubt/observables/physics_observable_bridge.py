# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Bridge scaffold from UBT quantities to measurable observables."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ObservableResult:
    """Structured observable status preserving claim-level discipline."""

    value: float | None
    status: str
    required_derivation: list[str]
    references: list[str]
    comparison_target: str | None = None


class AnomalousMagneticMoment:
    """
    UBT prediction for the anomalous magnetic moment of the electron.

    STATUS: OPEN_GAP
    The standard QED result a_e = (α/2π) + ... is reproduced by QED.
    UBT does not yet derive α from first principles (Gap G137-B).
    Therefore no independent UBT prediction for a_e exists at this stage.
    """

    QED_VALUE = 0.001159652181643  # CODATA 2018

    def ubt_prediction(self) -> dict[str, Any]:
        return {
            "value": None,
            "status": "OPEN_GAP",
            "reason": (
                "Requires α from first principles (Gap G137-B). "
                "Until Gap G137-B is closed, UBT prediction = QED prediction "
                "with α as input, not a new result."
            ),
            "qed_reference": self.QED_VALUE,
        }


class PhysicsObservableBridge:
    """Open-gap bridge from UBT structures to particle/coupling observables."""

    def __init__(self, reference_file: str | Path | None = None) -> None:
        root = Path(__file__).resolve().parents[3]
        default_ref = root / "data" / "reference_constants" / "codata_reference.json"
        self.reference_file = Path(reference_file) if reference_file else default_ref
        self._reference_data = self._load_reference_data(self.reference_file)

    @staticmethod
    def _load_reference_data(path: Path) -> dict[str, Any]:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError("Reference constants file must contain a JSON object")
        return data

    @staticmethod
    def _open_gap_result(required_derivation: list[str], references: list[str], target: str) -> ObservableResult:
        return ObservableResult(
            value=None,
            status="OPEN_GAP",
            required_derivation=required_derivation,
            references=references,
            comparison_target=target,
        )

    def predict_anomalous_magnetic_moment(self, particle: str = "electron") -> ObservableResult:
        return self._open_gap_result(
            required_derivation=[
                "Derive loop-corrected g-2 observable from UBT action.",
                "Establish renormalization prescription tied to UBT variables.",
            ],
            references=["canonical/interactions/", "research_tracks/"],
            target=f"{particle}_g_minus_2",
        )

    def predict_fine_structure_constant(self) -> ObservableResult:
        return self._open_gap_result(
            required_derivation=[
                "Close alpha derivation blockers in canonical alpha route.",
                "Show uncertainty-controlled extraction from UBT without fitted constants.",
            ],
            references=["canonical/alpha/ALPHA_MASTER_STATUS.md", "DERIVATION_INDEX.md"],
            target="alpha",
        )

    def predict_mass_ratio(self, particle_a: str, particle_b: str) -> ObservableResult:
        return self._open_gap_result(
            required_derivation=[
                f"Derive {particle_a}/{particle_b} mass relation from UBT spectrum.",
                "Establish generation structure and mass mechanism closure.",
            ],
            references=["research_tracks/", "canonical/interactions/"],
            target=f"{particle_a}_to_{particle_b}",
        )

    def compare_to_reference_data(
        self,
        observable_name: str,
        prediction: ObservableResult | None = None,
    ) -> dict[str, Any]:
        reference_value = self._reference_data.get(observable_name)
        payload: dict[str, Any] = {
            "observable_name": observable_name,
            "reference_value": reference_value,
            "reference_source": self._reference_data.get("source"),
            "reference_version": self._reference_data.get("version_date"),
        }

        if prediction is None or prediction.value is None:
            payload.update(
                {
                    "status": "OPEN_GAP",
                    "prediction": None,
                    "note": "No UBT-derived prediction available.",
                }
            )
            return payload

        payload.update(
            {
                "status": "COMPARED",
                "prediction": prediction.value,
                "delta": prediction.value - reference_value if reference_value is not None else None,
                "prediction_status": prediction.status,
            }
        )
        return payload

    def serialize_result(self, result: ObservableResult) -> dict[str, Any]:
        """Convert an ObservableResult to a JSON-serializable dictionary."""
        return asdict(result)
