# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Layer2 metrics."""

from __future__ import annotations

import math


def compute_rarity_bits(hit_rate: float) -> float:
    if not (0.0 <= hit_rate <= 1.0):
        raise ValueError("hit_rate must be in [0, 1]")
    if hit_rate == 0.0:
        return float("inf")
    if hit_rate == 1.0:
        return 0.0
    return -math.log2(hit_rate)
