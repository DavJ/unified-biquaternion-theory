# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Layer2 predictors."""

from __future__ import annotations

from .config_space import Layer2Config

BASE_OFFSET = 100.0
RS_N_COEFF = 0.05
RS_K_COEFF = 0.02
OFDM_COEFF = 0.1
WINDING_COEFF = 0.01
PRIME_GATE_COEFF = 0.5
GRID_COEFF = 0.001
ELECTRON_BASE = 0.4
ELECTRON_ALPHA_COEFF = 0.0007


def _base_predictions(cfg: Layer2Config) -> dict[str, float]:
    alpha_inv = (
        BASE_OFFSET
        + RS_N_COEFF * cfg.rs_n
        + RS_K_COEFF * cfg.rs_k
        + OFDM_COEFF * cfg.ofdm_channels
        + WINDING_COEFF * cfg.winding_number
        + PRIME_GATE_COEFF * cfg.prime_gate_pattern
        + GRID_COEFF * cfg.quantization_grid
    )
    electron_mass = ELECTRON_BASE + ELECTRON_ALPHA_COEFF * alpha_inv
    return {"alpha_inv": float(alpha_inv), "electron_mass": float(electron_mass)}


def predict_constants(
    cfg: Layer2Config,
    mapping: str = "placeholder",
    targets: list[str] | None = None,
) -> dict[str, float]:
    mode = mapping.lower()
    if mode not in {"placeholder", "ubt"}:
        raise ValueError(f"Unknown mapping: {mapping}")
    if mode == "ubt":
        raise RuntimeError(
            "The Layer2-to-observables UBT adapter is not implemented in the active tree; "
            "use mapping='placeholder' only for framework tests."
        )

    preds = _base_predictions(cfg)
    if targets is None:
        return preds
    return {k: v for k, v in preds.items() if k in set(targets)}


def get_experimental_values() -> dict[str, float]:
    """Reference values used only to score the prototype sweep."""
    return {"alpha_inv": 137.035999177, "electron_mass": 0.51099895069}


def get_default_tolerances() -> dict[str, float]:
    """Prototype hit tolerances; they are not UBT prediction uncertainties."""
    return {"alpha_inv": 0.1, "electron_mass": 0.01}
