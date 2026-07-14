# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Layer2 configuration objects."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Layer2Config:
    rs_n: int
    rs_k: int
    ofdm_channels: int
    winding_number: int
    prime_gate_pattern: int
    quantization_grid: int


ConfigurationSpace = Layer2Config
