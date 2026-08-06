# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
ubt_theta_lab.progressive_growth
=================================
Half-grid theta-sector factorization for the UBT progressive-growth
architecture (Milestone M2H).

Ordinary neuron duplication is the baseline; the intended architecture
decomposes every original matrix operator through an intermediate half-grid
space whose frame is defined by a selected theta segment.
"""
from .half_grid import (
    HalfGridFactorizationMetadata,
    factor_matrix_through_frame,
    factor_relu_layer_through_frame,
    HalfGridSectorSchedule,
)
from .theta_sector_frame import (
    ThetaSectorFrame,
    analyze_sector_frame,
)
from .phi_segment_adapter import build_phi_segment_frame

__all__ = [
    "HalfGridFactorizationMetadata",
    "factor_matrix_through_frame",
    "factor_relu_layer_through_frame",
    "HalfGridSectorSchedule",
    "ThetaSectorFrame",
    "analyze_sector_frame",
    "build_phi_segment_frame",
]
