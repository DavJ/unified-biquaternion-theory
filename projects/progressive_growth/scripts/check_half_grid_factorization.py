#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
check_half_grid_factorization.py
=================================
Diagnostic script for the half-grid theta-sector factorization
(Milestone M2H).

Prints, for each tested frame:
  - original matrix shape and rank
  - theta segment identifier
  - frame shape and rank
  - condition number
  - pseudoinverse residual
  - linear reconstruction error
  - ReLU reconstruction error (real matrices only)
  - verdict: EXACT_TRANSFER or SECTOR_INSUFFICIENT_FOR_EXACT_TRANSFER

Usage::

    python projects/progressive_growth/scripts/check_half_grid_factorization.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# Allow running from repo root
sys.path.insert(0, str(Path(__file__).parents[3] / "src"))

import torch
import torch.nn as nn

from ubt_theta_lab.progressive_growth import (
    analyze_sector_frame,
    build_phi_segment_frame,
    factor_matrix_through_frame,
    factor_relu_layer_through_frame,
)


def _sep():
    print("-" * 70)


def run_case(
    label: str,
    W: torch.Tensor,
    frame: torch.Tensor,
    segment_id: str,
) -> None:
    _sep()
    print(f"Case: {label}")
    print(f"  Original matrix shape : {list(W.shape)}")
    out_dim, in_dim = W.shape

    # Frame diagnostics
    tsf = analyze_sector_frame(frame, name=segment_id, segment_id=segment_id)
    print(f"  Segment id            : {segment_id}")
    print(f"  Frame shape           : {list(frame.shape)}")
    print(f"  Frame rank            : {tsf.rank}")
    print(f"  Condition number      : {tsf.condition_number:.6g}")
    print(f"  Pinv residual         : {tsf.pseudoinverse_residual:.3e}")
    sv = tsf.singular_values
    print(f"  Singular values       : [{', '.join(f'{v:.4g}' for v in sv.tolist())}]")

    # Compact SVD rank of weight
    _, s_w, _ = torch.linalg.svd(W.to(dtype=torch.float64), full_matrices=False)
    s_w_real = s_w.abs()
    eps = torch.finfo(torch.float64).eps
    tol = s_w_real[0].item() * max(s_w_real.numel(), 1) * eps
    r_w = int((s_w_real > tol).sum().item())
    print(f"  Matrix numerical rank : {r_w}")

    # Attempt linear factorization
    try:
        A, B, meta = factor_matrix_through_frame(W, frame)
        err_lin = meta.reconstruction_max_abs_error
        print(f"  Linear recon max err  : {err_lin:.3e}")

        # Attempt ReLU factorization (real matrices only)
        if not W.is_complex() and not frame.is_complex():
            layer = nn.Linear(in_dim, out_dim, bias=False, dtype=W.dtype)
            with torch.no_grad():
                layer.weight.copy_(W)
            mod, _ = factor_relu_layer_through_frame(layer, frame)
            gen = torch.Generator().manual_seed(0)
            x = torch.randn(64, in_dim, generator=gen, dtype=W.dtype)
            with torch.no_grad():
                expected = layer(x)
                got = mod(x)
            err_relu = (got - expected).abs().max().item()
            print(f"  ReLU recon max err    : {err_relu:.3e}")
        else:
            print(f"  ReLU recon max err    : (complex weight — ReLU path not applicable)")

        verdict = "EXACT_TRANSFER"
    except ValueError as exc:
        print(f"  Factorization error   : {exc}")
        verdict = "SECTOR_INSUFFICIENT_FOR_EXACT_TRANSFER"

    print(f"  Verdict               : {verdict}")


def main() -> None:
    print("=" * 70)
    print("Half-Grid Theta-Sector Factorization Diagnostic")
    print("Milestone M2H — Ing. David Jaroš, 2026")
    print("=" * 70)

    gen = torch.Generator().manual_seed(42)

    # --- Case 1: Identity / orthogonal baseline frame ---
    W_sq = torch.randn(6, 6, generator=gen, dtype=torch.float64)
    Q, _ = torch.linalg.qr(torch.randn(12, 6, generator=gen, dtype=torch.float64))
    run_case("Identity/orthogonal baseline frame", W_sq, Q, "ortho_baseline")

    # --- Case 2: Non-orthogonal synthetic frame ---
    W_rect = torch.randn(8, 4, generator=gen, dtype=torch.float64)
    M_nonortho = torch.randn(10, 4, generator=gen, dtype=torch.float64)
    M_nonortho = M_nonortho + 0.1 * torch.eye(10, 4, dtype=torch.float64)
    run_case("Non-orthogonal synthetic frame", W_rect, M_nonortho, "synthetic_nonortho")

    # --- Case 3: Canonical phi segment A (low phi) ---
    tsf_A = build_phi_segment_frame(4, [0.1, 0.2, 0.3], dtype=torch.float64)
    W_A = torch.randn(16, 3, generator=gen, dtype=torch.float64)
    run_case(
        "Canonical phi segment A (low phi: 0.1, 0.2, 0.3)",
        W_A,
        tsf_A.matrix,
        tsf_A.segment_id,
    )

    # --- Case 4: Canonical shifted phi segment B (mid phi) ---
    tsf_B = build_phi_segment_frame(4, [0.5, 1.0, 1.5], dtype=torch.float64)
    W_B = torch.randn(16, 3, generator=gen, dtype=torch.float64)
    run_case(
        "Canonical phi segment B (mid phi: 0.5, 1.0, 1.5)",
        W_B,
        tsf_B.matrix,
        tsf_B.segment_id,
    )

    # --- Case 5: High-phi near-degenerate segment (expected: may fail) ---
    tsf_hi = build_phi_segment_frame(3, [100.0, 200.0, 300.0], dtype=torch.float64)
    W_hi = torch.randn(9, 3, generator=gen, dtype=torch.float64)
    run_case(
        "High-phi near-degenerate segment (phi: 100, 200, 300)",
        W_hi,
        tsf_hi.matrix,
        tsf_hi.segment_id,
    )

    _sep()
    print()
    print("Sector interleaving check:")
    print("  Two different frames factorizing the same 6x6 matrix:")
    W_il = torch.randn(6, 6, generator=gen, dtype=torch.float64)
    Q2, _ = torch.linalg.qr(torch.randn(12, 6, generator=gen, dtype=torch.float64))
    M2 = torch.randn(12, 6, generator=gen, dtype=torch.float64)
    M2 = M2 + 0.1 * torch.eye(12, 6, dtype=torch.float64)

    A1, B1, m1 = factor_matrix_through_frame(W_il, Q2)
    A2, B2, m2 = factor_matrix_through_frame(W_il, M2)

    x_test = torch.randn(4, 6, generator=gen, dtype=torch.float64)
    out1 = B1 @ (A1 @ x_test.T)
    out2 = B2 @ (A2 @ x_test.T)
    mid1 = A1 @ x_test.T
    mid2 = A2 @ x_test.T

    print(f"  Max output difference     : {(out1-out2).abs().max().item():.3e}")
    print(f"  Max midpoint difference   : {(mid1-mid2).abs().max().item():.3e}")
    print(f"  Frames have equal output  : {(out1-out2).abs().max().item() < 1e-8}")
    print(f"  Frames have diff midpoints: {(mid1-mid2).abs().max().item() > 1e-6}")

    _sep()
    print()
    print("Mathematical limitations:")
    print("  1. Action-level sector selection is not derived (GAP-10T-DYN).")
    print("  2. Error accumulation across many composed layers is not analyzed.")
    print("  3. Torsion interpretation of frame non-orthogonality is open.")
    print("  4. Training dynamics after insertion are out of scope for M2H.")
    print("  5. Complex ReLU extension is not implemented.")
    print()
    print("This is not a proven Theta Grid speedup.")
    print("=" * 70)


if __name__ == "__main__":
    main()
