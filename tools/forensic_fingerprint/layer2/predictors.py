# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Layer2 predictors."""

from __future__ import annotations

from .config_space import Layer2Config


def _base_predictions(cfg: Layer2Config) -> dict[str, float]:
    alpha_inv = (
        100.0
        + 0.05 * cfg.rs_n
        + 0.02 * cfg.rs_k
        + 0.1 * cfg.ofdm_channels
        + 0.01 * cfg.winding_number
        + 0.5 * cfg.prime_gate_pattern
        + 0.001 * cfg.quantization_grid
    )
    electron_mass = 0.4 + 0.0007 * alpha_inv
    return {"alpha_inv": float(alpha_inv), "electron_mass": float(electron_mass)}


def predict_constants(
    cfg: Layer2Config,
    mapping: str = "placeholder",
    targets: list[str] | None = None,
) -> dict[str, float]:
    mode = mapping.lower()
    if mode not in {"placeholder", "ubt"}:
        raise ValueError(f"Unknown mapping: {mapping}")

    preds = _base_predictions(cfg)
    if targets is None:
        return preds
    return {k: v for k, v in preds.items() if k in set(targets)}
