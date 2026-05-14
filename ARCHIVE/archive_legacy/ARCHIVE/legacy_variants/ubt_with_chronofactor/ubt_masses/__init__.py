# ubt_masses/__init__.py
# SPDX-License-Identifier: MIT
"""
UBT Masses Package
==================

Fit-free fermion mass calculations from Unified Biquaternion Theory.

Key features:
- Uses exact two-loop α from alpha_core_repro (strict mode)
- MSbar scheme with μ = m̄_ℓ(μ) for leptons
- QED pole mass conversion (1-loop, TODO: 2-loop)
- Self-consistent fixed-point solver
"""

from .core import (
    ubt_alpha_msbar,
    compute_lepton_msbar_mass,
    solve_msbar_fixed_point,
)
from .qed import pole_from_msbar_lepton

__all__ = [
    "ubt_alpha_msbar",
    "compute_lepton_msbar_mass",
    "solve_msbar_fixed_point",
    "pole_from_msbar_lepton",
]
