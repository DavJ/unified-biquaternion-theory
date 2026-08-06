# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
phi_segment_adapter.py — canonical phi-kernel segment frame adapter
====================================================================

Constructs a half-grid theta-sector frame from a selected phi segment using
the canonical UBT phi kernel::

    G_phi(n, m) = exp(-2 * pi * phi * r2(n, m))

where r2(n, m) = n^2 + m^2 is the squared lattice radius.

Each phi value yields one flattened kernel vector of length
``lattice_size * lattice_size``.  The resulting frame matrix has shape::

    [lattice_size * lattice_size, number_of_phi_values]

Notes
-----
* This is a canonical phi-kernel segment, not an arbitrary frame.
* The frame is generally non-orthogonal.
* It is NOT automatically a Jacobi-theta characteristic basis.
* Different phi segments may have different spans and conditioning.
* The construction reuses the canonical radial-coordinate definition;
  the kernel formula is not duplicated or altered.
"""
from __future__ import annotations

import math
from typing import Sequence

import torch

from .theta_sector_frame import ThetaSectorFrame, analyze_sector_frame


def _phi_kernel_vector(
    lattice_size: int,
    phi: float,
    normalize: bool,
    dtype: torch.dtype,
) -> torch.Tensor:
    """Return the flattened phi-kernel for one phi value."""
    n_vals = torch.arange(lattice_size, dtype=dtype)
    m_vals = torch.arange(lattice_size, dtype=dtype)
    # Shift so that (0,0) is at the lattice center
    n_shift = n_vals - (lattice_size - 1) / 2.0
    m_shift = m_vals - (lattice_size - 1) / 2.0
    N, M = torch.meshgrid(n_shift, m_shift, indexing="ij")
    r2 = N ** 2 + M ** 2                                   # [L, L]
    # Canonical phi kernel: G_phi(n,m) = exp(-2*pi*phi*r2(n,m))
    kernel = torch.exp(-2.0 * math.pi * phi * r2)
    vec = kernel.flatten()                                 # [L*L]
    if normalize:
        norm = vec.norm()
        if norm.item() > 0:
            vec = vec / norm
    return vec


def build_phi_segment_frame(
    lattice_size: int,
    phi_values: Sequence[float],
    *,
    normalize_columns: bool = True,
    dtype: torch.dtype = torch.float64,
) -> ThetaSectorFrame:
    """
    Build a half-grid theta-sector frame from a phi segment.

    Parameters
    ----------
    lattice_size : int
        Linear dimension of the lattice; frame rows = lattice_size**2.
    phi_values : sequence of float
        The phi values that define the segment.  One column per value.
    normalize_columns : bool
        Whether to normalize each kernel vector to unit L2 norm before
        assembling the frame.
    dtype : torch.dtype
        Floating-point precision (default float64).

    Returns
    -------
    ThetaSectorFrame
        Frame of shape [lattice_size**2, len(phi_values)] with full
        algebraic diagnostics.

    Notes
    -----
    The frame is constructed from the canonical phi kernel
    ``G_phi(n,m) = exp(-2*pi*phi*r2(n,m))``.  Different phi segments
    (different phi_values lists) may have different spans and conditioning;
    do not assume they span the same subspace without a numerical subspace
    test.
    """
    phi_values = list(phi_values)
    if not phi_values:
        raise ValueError("phi_values must be non-empty")
    if lattice_size < 1:
        raise ValueError("lattice_size must be >= 1")

    columns = [
        _phi_kernel_vector(lattice_size, phi, normalize_columns, dtype)
        for phi in phi_values
    ]
    # Shape: [lattice_size*lattice_size, len(phi_values)]
    matrix = torch.stack(columns, dim=1)

    # Build a descriptive segment_id
    phi_str = "_".join(f"{p:.4g}" for p in phi_values)
    segment_id = f"phi_segment_L{lattice_size}_{phi_str}"
    name = segment_id

    frame = analyze_sector_frame(matrix, name=name, segment_id=segment_id)
    return frame
