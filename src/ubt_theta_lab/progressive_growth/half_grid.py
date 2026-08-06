# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
half_grid.py — half-grid theta-sector factorization
=====================================================

Core algebraic construction for Milestone M2H.

For an original matrix V of shape [output_dim, input_dim] and a theta-sector
frame Phi of shape [sector_width, r] (where r = numerical rank of V),
define::

    V = P @ diag(s) @ Qh            (compact SVD)
    sqrt_Sigma = diag(sqrt(s[:r]))

    A = Phi @ sqrt_Sigma @ Qh        shape [sector_width, input_dim]
    B = P @ sqrt_Sigma @ pinv(Phi)   shape [output_dim, sector_width]

Invariant: B @ A == V  within documented numerical tolerance.

This is NOT the trivial identity V U^T W U = V (which holds for any
orthogonal U and W=I); the frame Phi is the genuine half-grid sector
frame and encodes UBT theta-segment geometry.

The paired ReLU construction exploits::

    relu(z) - relu(-z) == z

to build::

    A_pm = cat([A, -A], dim=0)         shape [2*sector_width, input_dim]
    B_pm = cat([B, -B], dim=1)         shape [output_dim, 2*sector_width]

so that B_pm @ relu(A_pm @ x) == V @ x for all real x.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence, Tuple

import torch
import torch.nn as nn


# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class HalfGridFactorizationMetadata:
    """Immutable record of all diagnostics for one half-grid factorization."""
    input_dim: int
    output_dim: int
    matrix_rank: int
    sector_width: int
    frame_rank: int
    frame_condition_number: float
    frame_inverse_residual: float       # max_abs(pinv(Phi) @ Phi - I_r)
    reconstruction_max_abs_error: float
    reconstruction_relative_error: float
    dtype: str
    device: str


# ---------------------------------------------------------------------------
# Schedule
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class HalfGridSectorSchedule:
    """
    Lightweight schedule: segment_ids[k] names the theta sector frame
    inserted between original layer k and k+1 (at position k + 1/2).

    Example::

        schedule = HalfGridSectorSchedule(("phi_A", "phi_B", "phi_A"))
        # original layer 0 -> theta segment at 1/2  (phi_A)
        # original layer 1 -> theta segment at 3/2  (phi_B)
        # original layer 2 -> theta segment at 5/2  (phi_A)
    """
    segment_ids: Tuple[str, ...]


# ---------------------------------------------------------------------------
# Core factorization
# ---------------------------------------------------------------------------

def _numerical_rank(
    singular_values: torch.Tensor,
    rank_tolerance: Optional[float],
) -> int:
    """Return numerical rank given singular values (descending)."""
    sv = singular_values.real if singular_values.is_complex() else singular_values
    sv = sv.abs()
    if sv.numel() == 0:
        return 0
    if rank_tolerance is None:
        # Default: machine epsilon scaled by the largest singular value and
        # max matrix dimension.
        eps = torch.finfo(sv.to(torch.float64).dtype).eps
        tol = sv[0].item() * max(sv.numel(), 1) * eps
    else:
        tol = rank_tolerance
    return int((sv > tol).sum().item())


def factor_matrix_through_frame(
    weight: torch.Tensor,
    frame: torch.Tensor,
    *,
    rank_tolerance: Optional[float] = None,
    max_condition_number: Optional[float] = None,
) -> Tuple[torch.Tensor, torch.Tensor, HalfGridFactorizationMetadata]:
    """
    Factorize *weight* through *frame* so that ``B @ A == weight``.

    Parameters
    ----------
    weight : Tensor, shape [output_dim, input_dim]
        The matrix to be factorized.  May be rectangular or rank-deficient.
        Complex tensors are supported (purely linear factorization).
    frame : Tensor, shape [sector_width, r_or_more]
        The half-grid theta-sector frame.  Must have full column rank >= r
        where r is the numerical rank of *weight*.
    rank_tolerance : float or None
        Threshold for declaring a singular value numerically zero.
        Defaults to eps * sigma_max * max_dim.
    max_condition_number : float or None
        If given, raise ValueError when the frame condition number exceeds
        this value.

    Returns
    -------
    A : Tensor, shape [sector_width, input_dim]
    B : Tensor, shape [output_dim, sector_width]
    meta : HalfGridFactorizationMetadata

    Raises
    ------
    ValueError
        On incompatible dimensions, non-finite entries, empty inputs,
        insufficient frame rank, or exceeded condition number.
    """
    # --- basic validation ---
    if weight.ndim != 2:
        raise ValueError(f"weight must be 2-D, got shape {weight.shape}")
    if frame.ndim != 2:
        raise ValueError(f"frame must be 2-D, got shape {frame.shape}")
    if not torch.isfinite(weight).all():
        raise ValueError("weight contains non-finite entries")
    if not torch.isfinite(frame).all():
        raise ValueError("frame contains non-finite entries")
    if weight.numel() == 0:
        raise ValueError("weight is empty")
    if frame.numel() == 0:
        raise ValueError("frame is empty")

    out_dim, in_dim = weight.shape
    sector_width, frame_cols = frame.shape

    if frame_cols == 0:
        raise ValueError("frame has zero columns")
    if sector_width == 0:
        raise ValueError("frame has zero rows (sector_width = 0)")

    # Work in FP64 for SVD accuracy; restore original dtype at the end.
    orig_dtype = weight.dtype
    orig_device = weight.device
    compute_dtype = torch.complex128 if weight.is_complex() else torch.float64
    W = weight.to(dtype=compute_dtype)
    Phi = frame.to(dtype=compute_dtype)

    # --- compact SVD of weight ---
    P, s, Qh = torch.linalg.svd(W, full_matrices=False)
    # P:  [out_dim, k],  s: [k],  Qh: [k, in_dim],  k = min(out_dim, in_dim)

    r = _numerical_rank(s, rank_tolerance)

    # Trim to rank r
    P_r = P[:, :r]      # [out_dim, r]
    s_r = s[:r]         # [r]
    Qh_r = Qh[:r, :]   # [r, in_dim]

    # --- frame rank check ---
    # frame must have at least r columns or sector_width >= r
    if frame_cols < r:
        raise ValueError(
            f"frame has {frame_cols} columns but weight has numerical rank {r}; "
            "frame column count must be >= rank(weight)."
        )

    # Check frame column rank
    _, s_phi, _ = torch.linalg.svd(Phi, full_matrices=False)
    phi_rank = _numerical_rank(s_phi, rank_tolerance)

    if phi_rank < r:
        raise ValueError(
            f"Frame column rank ({phi_rank}) is below the numerical rank of "
            f"weight ({r}).  Cannot perform exact half-grid factorization."
        )

    # Condition number of frame (using full frame, not just top-r columns)
    s_phi_real = s_phi.real.abs() if s_phi.is_complex() else s_phi.abs()
    if s_phi_real[-1].item() < 1e-300:
        cond = float("inf")
    else:
        cond = (s_phi_real[0] / s_phi_real[phi_rank - 1]).item()

    if max_condition_number is not None and cond > max_condition_number:
        raise ValueError(
            f"Frame condition number ({cond:.6g}) exceeds requested maximum "
            f"({max_condition_number:.6g})."
        )

    # --- frame pseudo-inverse residual ---
    Phi_pinv = torch.linalg.pinv(Phi)  # [frame_cols, sector_width]
    residual_mat = Phi_pinv @ Phi      # [frame_cols, frame_cols]
    eye_r = torch.eye(frame_cols, dtype=compute_dtype, device=orig_device)
    frame_inv_residual = (residual_mat - eye_r).abs().max().item()

    # --- build A and B ---
    sqrt_s = s_r.sqrt()
    sqrt_Sigma_Qh = sqrt_s.unsqueeze(-1) * Qh_r   # [r, in_dim]

    A = Phi[:, :r] @ sqrt_Sigma_Qh                        # [sector_width, in_dim]
    B = (P_r * sqrt_s.unsqueeze(0)) @ Phi_pinv[:r, :]     # [out_dim, sector_width]

    # --- reconstruction error ---
    recon = B @ A
    err = (recon - W).abs()
    max_abs_err = err.max().item()
    W_norm = W.abs().max().item()
    rel_err = max_abs_err / W_norm if W_norm > 0 else max_abs_err

    meta = HalfGridFactorizationMetadata(
        input_dim=in_dim,
        output_dim=out_dim,
        matrix_rank=r,
        sector_width=sector_width,
        frame_rank=phi_rank,
        frame_condition_number=cond,
        frame_inverse_residual=frame_inv_residual,
        reconstruction_max_abs_error=max_abs_err,
        reconstruction_relative_error=rel_err,
        dtype=str(orig_dtype),
        device=str(orig_device),
    )

    A_out = A.to(dtype=orig_dtype)
    B_out = B.to(dtype=orig_dtype)

    return A_out, B_out, meta


# ---------------------------------------------------------------------------
# ReLU factorized module
# ---------------------------------------------------------------------------

class _HalfGridReLUModule(nn.Module):
    """
    Factorized layer: input -> A_pm -> ReLU -> B_pm -> +bias.

    Computes B_pm @ relu(A_pm @ x) + bias == V @ x + bias for real inputs.
    """

    def __init__(
        self,
        A: torch.Tensor,
        B: torch.Tensor,
        bias: Optional[torch.Tensor],
    ) -> None:
        super().__init__()
        # A_pm = cat([A, -A], dim=0),  B_pm = cat([B, -B], dim=1)
        A_pm = torch.cat([A, -A], dim=0)     # [2*sector_width, in_dim]
        B_pm = torch.cat([B, -B], dim=1)     # [out_dim, 2*sector_width]
        self.register_buffer("A_pm", A_pm)
        self.register_buffer("B_pm", B_pm)
        if bias is not None:
            self.register_buffer("bias", bias.clone())
        else:
            self.register_buffer("bias", None)
        self.relu = nn.ReLU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = x @ self.A_pm.t()               # [..., 2*sector_width]
        h = self.relu(h)
        out = h @ self.B_pm.t()             # [..., out_dim]
        if self.bias is not None:
            out = out + self.bias
        return out


def factor_relu_layer_through_frame(
    layer: nn.Linear,
    frame: torch.Tensor,
    *,
    rank_tolerance: Optional[float] = None,
    max_condition_number: Optional[float] = None,
) -> Tuple[nn.Module, HalfGridFactorizationMetadata]:
    """
    Factorize a ``torch.nn.Linear`` layer through a half-grid theta-sector
    frame using the paired ReLU identity.

    The returned module computes::

        B_pm @ relu(A_pm @ x) + bias == layer.weight @ x + layer.bias

    for all real inputs x, where::

        A_pm = cat([A, -A], dim=0)
        B_pm = cat([B, -B], dim=1)

    and A, B come from :func:`factor_matrix_through_frame`.

    Parameters
    ----------
    layer : nn.Linear
        The linear layer to factorize.  Must be real-valued.
    frame : torch.Tensor
        The half-grid sector frame (real).
    rank_tolerance, max_condition_number
        Passed to :func:`factor_matrix_through_frame`.

    Returns
    -------
    module : nn.Module
        Factorized equivalent layer (no further training assumed for
        exact preservation).
    meta : HalfGridFactorizationMetadata

    Raises
    ------
    ValueError
        If inputs are complex (ReLU factorization is real-valued only),
        or if other validity constraints fail.
    """
    weight = layer.weight  # [out_dim, in_dim]

    if weight.is_complex():
        raise ValueError(
            "ReLU half-grid factorization is defined for real-valued layers "
            "only.  Received a complex weight tensor."
        )
    if frame.is_complex():
        raise ValueError(
            "ReLU half-grid factorization requires a real frame.  "
            "Received a complex frame tensor."
        )

    A, B, meta = factor_matrix_through_frame(
        weight,
        frame,
        rank_tolerance=rank_tolerance,
        max_condition_number=max_condition_number,
    )

    bias = layer.bias.detach() if layer.bias is not None else None
    module = _HalfGridReLUModule(A.detach(), B.detach(), bias)
    return module, meta
