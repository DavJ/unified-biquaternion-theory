# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
theta_sector_frame.py — theta-sector frame analysis
=====================================================

A ThetaSectorFrame records a matrix Phi together with its algebraic
diagnostics: rank, condition number, Gram matrix, and pseudoinverse
residual.

The frame is the intermediate half-grid space in the UBT progressive-growth
architecture (Milestone M2H).  Different theta segments at positions k + 1/2
supply different frames; the span and conditioning vary between segments.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import torch


@dataclass(frozen=True)
class ThetaSectorFrame:
    """
    Immutable descriptor of a half-grid theta-sector frame.

    Attributes
    ----------
    name : str
        Human-readable identifier (e.g. ``"phi_segment_A"``).
    matrix : torch.Tensor
        Frame matrix Phi of shape [sector_width, num_vectors].
    segment_id : str
        Canonical identifier for the theta-segment source (may equal *name*
        or carry additional provenance).
    rank : int
        Numerical rank of *matrix*.
    condition_number : float
        Ratio sigma_max / sigma_min (among nonzero singular values).
        ``inf`` when the frame is rank-deficient.
    gram_matrix : torch.Tensor
        Gram matrix Phi.T @ Phi (or Phi.conj().T @ Phi for complex),
        shape [num_vectors, num_vectors].
    singular_values : torch.Tensor
        All singular values in descending order.
    pseudoinverse_residual : float
        max_abs(pinv(Phi) @ Phi - I)  over the column space.
    """
    name: str
    matrix: torch.Tensor
    segment_id: str
    rank: int
    condition_number: float
    gram_matrix: torch.Tensor
    singular_values: torch.Tensor
    pseudoinverse_residual: float


def analyze_sector_frame(
    matrix: torch.Tensor,
    name: str = "unnamed_frame",
    segment_id: str = "",
    *,
    rank_tolerance: Optional[float] = None,
) -> ThetaSectorFrame:
    """
    Compute diagnostics for a theta-sector frame matrix.

    Parameters
    ----------
    matrix : Tensor, shape [sector_width, num_vectors]
        The frame matrix Phi.
    name : str
        Human-readable label.
    segment_id : str
        Provenance / canonical segment identifier.
    rank_tolerance : float or None
        Threshold for singular-value zero.  Defaults to
        ``eps * sigma_max * max_dim``.

    Returns
    -------
    ThetaSectorFrame

    Raises
    ------
    ValueError
        If *matrix* is not 2-D or contains non-finite entries.
    """
    if matrix.ndim != 2:
        raise ValueError(
            f"frame matrix must be 2-D, got shape {matrix.shape}"
        )
    if not torch.isfinite(matrix).all():
        raise ValueError("frame matrix contains non-finite entries")
    if matrix.numel() == 0:
        raise ValueError("frame matrix is empty")

    compute_dtype = torch.complex128 if matrix.is_complex() else torch.float64
    M = matrix.to(dtype=compute_dtype)

    # Singular values
    sv = torch.linalg.svdvals(M)
    sv_real = sv.real.abs() if sv.is_complex() else sv.abs()

    # Numerical rank
    if rank_tolerance is None:
        eps = torch.finfo(torch.float64).eps
        tol = sv_real[0].item() * max(sv_real.numel(), 1) * eps
    else:
        tol = rank_tolerance
    rank = int((sv_real > tol).sum().item())

    # Condition number
    if rank == 0:
        cond = float("inf")
    elif sv_real[rank - 1].item() < 1e-300:
        cond = float("inf")
    else:
        cond = (sv_real[0] / sv_real[rank - 1]).item()

    # Gram matrix: Phi^H @ Phi
    gram = M.conj().T @ M  # [num_vectors, num_vectors]

    # Pseudoinverse residual: max_abs(pinv(Phi) @ Phi - I)
    Phi_pinv = torch.linalg.pinv(M)   # [num_vectors, sector_width]
    n_cols = M.shape[1]
    residual_mat = Phi_pinv @ M       # [num_vectors, num_vectors]
    eye = torch.eye(n_cols, dtype=compute_dtype, device=matrix.device)
    pinv_residual = (residual_mat - eye).abs().max().item()

    return ThetaSectorFrame(
        name=name,
        matrix=matrix,
        segment_id=segment_id if segment_id else name,
        rank=rank,
        condition_number=cond,
        gram_matrix=gram.to(matrix.dtype),
        singular_values=sv_real.to(dtype=torch.float64),
        pseudoinverse_residual=pinv_residual,
    )
