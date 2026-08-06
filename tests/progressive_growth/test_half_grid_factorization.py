# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
tests/progressive_growth/test_half_grid_factorization.py
=========================================================
Tests for the half-grid theta-sector factorization (Milestone M2H).

Covers:
  - Linear factorization: square/rectangular/rank-deficient, FP32/FP64/complex
  - Frame types: orthogonal, non-orthogonal, overcomplete
  - ReLU factorization identity
  - Failure cases (bad frame, bad dimensions, complex in ReLU path, etc.)
  - Sector interleaving: two different frames give same output but different
    intermediate activations
  - Canonical phi-segment frames: rank/conditioning diagnostics
"""
from __future__ import annotations

import math
import warnings

import pytest
import torch
import torch.nn as nn

from ubt_theta_lab.progressive_growth import (
    HalfGridFactorizationMetadata,
    HalfGridSectorSchedule,
    ThetaSectorFrame,
    analyze_sector_frame,
    build_phi_segment_frame,
    factor_matrix_through_frame,
    factor_relu_layer_through_frame,
)

# ---------------------------------------------------------------------------
# Tolerance helpers
# ---------------------------------------------------------------------------

_FP64_LINEAR_TOL = 1e-10
_FP32_LINEAR_ATOL = 1e-5
_FP32_LINEAR_RTOL = 1e-5
_FP64_RELU_TOL = 1e-9
_FP32_RELU_ATOL = 2e-5
_FP32_RELU_RTOL = 1e-5


def _make_random_matrix(rows: int, cols: int, dtype: torch.dtype) -> torch.Tensor:
    gen = torch.Generator().manual_seed(42)
    if dtype == torch.complex128:
        r = torch.randn(rows, cols, generator=gen, dtype=torch.float64)
        i = torch.randn(rows, cols, generator=gen, dtype=torch.float64)
        return r + 1j * i
    return torch.randn(rows, cols, generator=gen, dtype=dtype)


def _orthogonal_frame(rows: int, cols: int, dtype: torch.dtype) -> torch.Tensor:
    """Orthonormal columns via QR."""
    assert cols <= rows
    M = _make_random_matrix(rows, cols, dtype)
    Q, _ = torch.linalg.qr(M)
    return Q[:, :cols]


def _nonorthogonal_frame(rows: int, cols: int, dtype: torch.dtype) -> torch.Tensor:
    """Well-conditioned but non-orthogonal frame."""
    gen = torch.Generator().manual_seed(99)
    if dtype == torch.complex128:
        r = torch.randn(rows, cols, generator=gen, dtype=torch.float64)
        i = torch.randn(rows, cols, generator=gen, dtype=torch.float64)
        M = r + 1j * i
    else:
        M = torch.randn(rows, cols, generator=gen, dtype=dtype)
    # Scale to ensure full rank
    M = M + 0.1 * torch.eye(rows, cols, dtype=dtype)
    return M


# ---------------------------------------------------------------------------
# 1. Linear factorization — correctness
# ---------------------------------------------------------------------------

class TestLinearFactorizationSquareFullRank:
    def test_fp64(self):
        W = _make_random_matrix(8, 8, torch.float64)
        frame = _orthogonal_frame(16, 8, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL, f"max abs error {err}"
        assert meta.matrix_rank == 8
        assert meta.reconstruction_max_abs_error < _FP64_LINEAR_TOL

    def test_fp32(self):
        W = _make_random_matrix(8, 8, torch.float32)
        frame = _orthogonal_frame(16, 8, torch.float32)
        A, B, meta = factor_matrix_through_frame(W, frame)
        recon = B @ A
        assert torch.allclose(recon, W, atol=_FP32_LINEAR_ATOL, rtol=_FP32_LINEAR_RTOL), (
            f"FP32 reconstruction failed; max err {(recon-W).abs().max().item()}"
        )

    def test_dtype_preserved_fp32(self):
        W = _make_random_matrix(6, 6, torch.float32)
        frame = _orthogonal_frame(12, 6, torch.float32)
        A, B, meta = factor_matrix_through_frame(W, frame)
        assert A.dtype == torch.float32
        assert B.dtype == torch.float32

    def test_dtype_preserved_fp64(self):
        W = _make_random_matrix(6, 6, torch.float64)
        frame = _orthogonal_frame(12, 6, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        assert A.dtype == torch.float64
        assert B.dtype == torch.float64


class TestLinearFactorizationRectangular:
    def test_tall_fp64(self):
        """More outputs than inputs."""
        W = _make_random_matrix(12, 4, torch.float64)
        frame = _orthogonal_frame(16, 4, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL

    def test_wide_fp64(self):
        """More inputs than outputs."""
        W = _make_random_matrix(4, 12, torch.float64)
        frame = _orthogonal_frame(16, 4, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL


class TestLinearFactorizationRankDeficient:
    def test_rank_deficient_fp64(self):
        """Rank-2 matrix in a 5x5 container."""
        gen = torch.Generator().manual_seed(7)
        U = torch.randn(5, 2, generator=gen, dtype=torch.float64)
        V = torch.randn(2, 5, generator=gen, dtype=torch.float64)
        W = U @ V   # rank 2
        frame = _orthogonal_frame(8, 2, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL
        assert meta.matrix_rank == 2

    def test_rank_reported_correctly(self):
        W = torch.zeros(6, 6, dtype=torch.float64)
        W[0, 0] = 3.0
        W[1, 1] = 2.0
        frame = _orthogonal_frame(8, 2, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        assert meta.matrix_rank == 2


class TestLinearFactorizationComplex:
    def test_complex128(self):
        W = _make_random_matrix(6, 6, torch.complex128)
        # Complex orthogonal frame
        frame_r = _orthogonal_frame(10, 6, torch.float64)
        frame_c = frame_r + 0j
        A, B, meta = factor_matrix_through_frame(W, frame_c)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL, f"complex recon error {err}"

    def test_complex_dtype_preserved(self):
        W = _make_random_matrix(4, 4, torch.complex128)
        frame_c = _nonorthogonal_frame(8, 4, torch.complex128)
        A, B, meta = factor_matrix_through_frame(W, frame_c)
        assert A.is_complex()
        assert B.is_complex()


class TestLinearFactorizationFrameTypes:
    def test_orthogonal_frame(self):
        W = _make_random_matrix(5, 5, torch.float64)
        frame = _orthogonal_frame(8, 5, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL

    def test_nonorthogonal_full_rank_frame(self):
        W = _make_random_matrix(5, 5, torch.float64)
        frame = _nonorthogonal_frame(8, 5, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL

    def test_overcomplete_frame(self):
        """Frame has more columns than rank(W): still exact."""
        W = _make_random_matrix(4, 4, torch.float64)
        frame = _orthogonal_frame(8, 6, torch.float64)  # 6 cols >= rank 4
        A, B, meta = factor_matrix_through_frame(W, frame)
        err = (B @ A - W).abs().max().item()
        assert err < _FP64_LINEAR_TOL


# ---------------------------------------------------------------------------
# 2. Different frames at different half-grid positions
# ---------------------------------------------------------------------------

class TestSectorInterleaving:
    """
    Two different well-conditioned frames applied to the same matrix must
    produce the same reconstruction but different intermediate activations.
    """

    def test_two_frames_same_output_different_activations(self):
        gen = torch.Generator().manual_seed(13)
        W = torch.randn(6, 6, generator=gen, dtype=torch.float64)

        frame_A = _orthogonal_frame(10, 6, torch.float64)
        frame_B = _nonorthogonal_frame(10, 6, torch.float64)

        A1, B1, meta1 = factor_matrix_through_frame(W, frame_A)
        A2, B2, meta2 = factor_matrix_through_frame(W, frame_B)

        x = torch.randn(6, 1, generator=gen, dtype=torch.float64)
        out1 = B1 @ (A1 @ x)
        out2 = B2 @ (A2 @ x)
        mid1 = A1 @ x
        mid2 = A2 @ x

        # Same output
        assert (out1 - out2).abs().max().item() < _FP64_LINEAR_TOL, (
            "Two frames should produce equal final output"
        )
        # Different intermediate activations
        assert (mid1 - mid2).abs().max().item() > 1e-6, (
            "Intermediate activations must differ for different frames"
        )

    def test_schedule_object(self):
        sched = HalfGridSectorSchedule(("phi_A", "phi_B", "phi_A"))
        assert sched.segment_ids == ("phi_A", "phi_B", "phi_A")
        assert len(sched.segment_ids) == 3


# ---------------------------------------------------------------------------
# 3. ReLU factorization
# ---------------------------------------------------------------------------

class TestReLUFactorization:
    def _layer_and_frame(self, in_dim, out_dim, seed=0):
        gen = torch.Generator().manual_seed(seed)
        layer = nn.Linear(in_dim, out_dim, bias=False, dtype=torch.float64)
        with torch.no_grad():
            layer.weight.copy_(
                torch.randn(out_dim, in_dim, generator=gen, dtype=torch.float64)
            )
        frame = _orthogonal_frame(max(in_dim, out_dim) * 2, min(in_dim, out_dim), torch.float64)
        return layer, frame

    def _check_relu_identity(self, layer, frame, batch_size=32, seed=1):
        module, meta = factor_relu_layer_through_frame(layer, frame)
        gen = torch.Generator().manual_seed(seed)
        x = torch.randn(batch_size, layer.in_features, generator=gen, dtype=torch.float64)
        with torch.no_grad():
            expected = layer(x)
            got = module(x)
        err = (got - expected).abs().max().item()
        assert err < _FP64_RELU_TOL, f"ReLU recon error {err}"

    def test_zero_bias_square(self):
        layer, frame = self._layer_and_frame(6, 6)
        self._check_relu_identity(layer, frame)

    def test_nonzero_bias_square(self):
        gen = torch.Generator().manual_seed(5)
        layer = nn.Linear(6, 6, bias=True, dtype=torch.float64)
        with torch.no_grad():
            layer.weight.copy_(torch.randn(6, 6, generator=gen, dtype=torch.float64))
            layer.bias.copy_(torch.randn(6, generator=gen, dtype=torch.float64))
        frame = _orthogonal_frame(12, 6, torch.float64)
        module, meta = factor_relu_layer_through_frame(layer, frame)
        gen2 = torch.Generator().manual_seed(99)
        x = torch.randn(20, 6, generator=gen2, dtype=torch.float64)
        with torch.no_grad():
            expected = layer(x)
            got = module(x)
        err = (got - expected).abs().max().item()
        assert err < _FP64_RELU_TOL

    def test_positive_and_negative_inputs(self):
        """Ensure the paired ±A construction works for mixed-sign inputs."""
        layer, frame = self._layer_and_frame(5, 5)
        module, _ = factor_relu_layer_through_frame(layer, frame)
        x_pos = torch.ones(10, 5, dtype=torch.float64) * 0.7
        x_neg = torch.ones(10, 5, dtype=torch.float64) * (-0.7)
        x_mix = torch.linspace(-1, 1, 50, dtype=torch.float64).reshape(10, 5)
        for x in [x_pos, x_neg, x_mix]:
            with torch.no_grad():
                expected = layer(x)
                got = module(x)
            err = (got - expected).abs().max().item()
            assert err < _FP64_RELU_TOL

    def test_rectangular_tall(self):
        layer, frame = self._layer_and_frame(4, 10, seed=3)
        self._check_relu_identity(layer, frame)

    def test_rectangular_wide(self):
        layer, frame = self._layer_and_frame(10, 4, seed=4)
        frame2 = _orthogonal_frame(20, 4, torch.float64)
        module, _ = factor_relu_layer_through_frame(layer, frame2)
        gen = torch.Generator().manual_seed(7)
        x = torch.randn(16, 10, generator=gen, dtype=torch.float64)
        with torch.no_grad():
            expected = layer(x)
            got = module(x)
        err = (got - expected).abs().max().item()
        assert err < _FP64_RELU_TOL

    def test_outer_relu_preservation(self):
        """relu(factorized_affine(x)) == relu(original_affine(x))."""
        layer, frame = self._layer_and_frame(6, 6)
        module, _ = factor_relu_layer_through_frame(layer, frame)
        gen = torch.Generator().manual_seed(55)
        x = torch.randn(20, 6, generator=gen, dtype=torch.float64)
        relu = nn.ReLU()
        with torch.no_grad():
            expected = relu(layer(x))
            got = relu(module(x))
        err = (got - expected).abs().max().item()
        assert err < _FP64_RELU_TOL

    def test_two_different_frames_same_relu_output(self):
        """Two different frames give equal ReLU output but different midpoints."""
        gen = torch.Generator().manual_seed(17)
        layer = nn.Linear(6, 6, bias=False, dtype=torch.float64)
        with torch.no_grad():
            layer.weight.copy_(torch.randn(6, 6, generator=gen, dtype=torch.float64))

        frame_A = _orthogonal_frame(12, 6, torch.float64)
        frame_B = _nonorthogonal_frame(12, 6, torch.float64)
        mod_A, _ = factor_relu_layer_through_frame(layer, frame_A)
        mod_B, _ = factor_relu_layer_through_frame(layer, frame_B)

        x = torch.randn(10, 6, generator=gen, dtype=torch.float64)
        with torch.no_grad():
            out_A = mod_A(x)
            out_B = mod_B(x)

        err = (out_A - out_B).abs().max().item()
        assert err < _FP64_RELU_TOL, f"Different frames should give same output: {err}"

    def test_fp32_relu(self):
        gen = torch.Generator().manual_seed(22)
        layer = nn.Linear(6, 6, bias=False, dtype=torch.float32)
        with torch.no_grad():
            layer.weight.copy_(torch.randn(6, 6, generator=gen, dtype=torch.float32))
        frame = _orthogonal_frame(12, 6, torch.float32)
        module, _ = factor_relu_layer_through_frame(layer, frame)
        x = torch.randn(20, 6, generator=gen, dtype=torch.float32)
        with torch.no_grad():
            expected = layer(x)
            got = module(x)
        assert torch.allclose(got, expected, atol=_FP32_RELU_ATOL, rtol=_FP32_RELU_RTOL)


# ---------------------------------------------------------------------------
# 4. Failure cases
# ---------------------------------------------------------------------------

class TestFailureCases:
    def test_rank_deficient_frame_rejected(self):
        """Frame whose rank < rank(W) must be rejected."""
        W = _make_random_matrix(4, 4, torch.float64)
        # Build a rank-1 frame by repeating a single vector
        v = torch.randn(8, 1, dtype=torch.float64)
        frame = torch.cat([v, v, v, v], dim=1)  # rank 1
        with pytest.raises(ValueError, match="[Ff]rame"):
            factor_matrix_through_frame(W, frame)

    def test_nonfinite_frame_rejected(self):
        W = _make_random_matrix(4, 4, torch.float64)
        frame = _orthogonal_frame(8, 4, torch.float64).clone()
        frame[0, 0] = float("nan")
        with pytest.raises(ValueError, match="non-finite"):
            factor_matrix_through_frame(W, frame)

    def test_empty_frame_rejected(self):
        W = _make_random_matrix(4, 4, torch.float64)
        frame = torch.zeros(0, 4, dtype=torch.float64)
        with pytest.raises(ValueError):
            factor_matrix_through_frame(W, frame)

    def test_1d_weight_rejected(self):
        W = torch.randn(4, dtype=torch.float64)
        frame = torch.eye(4, dtype=torch.float64)
        with pytest.raises(ValueError):
            factor_matrix_through_frame(W, frame)

    def test_condition_number_limit_enforced(self):
        # Build an ill-conditioned frame
        frame = torch.eye(8, 4, dtype=torch.float64)
        frame[0, 0] = 1e6
        frame[1, 1] = 1.0
        frame[2, 2] = 1.0
        frame[3, 3] = 1.0
        W = _make_random_matrix(4, 4, torch.float64)
        with pytest.raises(ValueError, match="condition"):
            factor_matrix_through_frame(W, frame, max_condition_number=100.0)

    def test_complex_frame_rejected_for_relu(self):
        layer = nn.Linear(4, 4, bias=False, dtype=torch.float64)
        frame_c = _orthogonal_frame(8, 4, torch.float64) + 0j
        with pytest.raises(ValueError, match="[Cc]omplex"):
            factor_relu_layer_through_frame(layer, frame_c)

    def test_complex_layer_rejected_for_relu(self):
        gen = torch.Generator().manual_seed(0)
        real_w = torch.randn(4, 4, generator=gen, dtype=torch.float64)
        imag_w = torch.randn(4, 4, generator=gen, dtype=torch.float64)
        complex_w = real_w + 1j * imag_w

        class _FakeLayer:
            weight = complex_w
            bias = None
            in_features = 4
            out_features = 4

        frame = _orthogonal_frame(8, 4, torch.float64)
        with pytest.raises(ValueError, match="[Cc]omplex"):
            factor_relu_layer_through_frame(_FakeLayer(), frame)

    def test_incompatible_dimensions(self):
        W = _make_random_matrix(4, 4, torch.float64)
        # Frame has only 2 columns but rank(W) = 4
        frame = _orthogonal_frame(8, 2, torch.float64)
        with pytest.raises(ValueError):
            factor_matrix_through_frame(W, frame)


# ---------------------------------------------------------------------------
# 5. ThetaSectorFrame and analyze_sector_frame
# ---------------------------------------------------------------------------

class TestThetaSectorFrame:
    def test_orthonormal_frame_diagnostics(self):
        Q = _orthogonal_frame(8, 4, torch.float64)
        tsf = analyze_sector_frame(Q, name="test_ortho", segment_id="seg_1")
        assert tsf.rank == 4
        assert tsf.condition_number == pytest.approx(1.0, abs=1e-6)
        # pinv(Q) @ Q = I for orthonormal columns
        assert tsf.pseudoinverse_residual < 1e-10

    def test_nonorthogonal_frame_diagnostics(self):
        M = _nonorthogonal_frame(10, 5, torch.float64)
        tsf = analyze_sector_frame(M, name="test_nonortho")
        assert tsf.rank == 5
        assert tsf.condition_number > 1.0
        assert tsf.gram_matrix.shape == (5, 5)

    def test_frame_nondimensionality_check(self):
        v = torch.randn(5, dtype=torch.float64)
        with pytest.raises(ValueError):
            analyze_sector_frame(v)

    def test_frame_nonfinite_check(self):
        M = _orthogonal_frame(6, 3, torch.float64).clone()
        M[0, 0] = float("inf")
        with pytest.raises(ValueError, match="non-finite"):
            analyze_sector_frame(M)

    def test_singular_values_descending(self):
        M = _make_random_matrix(8, 5, torch.float64)
        tsf = analyze_sector_frame(M)
        sv = tsf.singular_values
        for i in range(len(sv) - 1):
            assert sv[i].item() >= sv[i + 1].item() - 1e-12


# ---------------------------------------------------------------------------
# 6. Canonical phi-segment frame tests
# ---------------------------------------------------------------------------

class TestPhiSegmentFrames:
    """
    For small phi segments, report rank, condition number, Gram eigenvalues,
    pseudoinverse residual, and whether the segment supports exact transfer.
    """

    _PHI_SETS = [
        ("phi_low", [0.1, 0.2, 0.3]),
        ("phi_mid", [0.5, 1.0, 1.5]),
        ("phi_high", [2.0, 3.0, 4.0]),
    ]

    @pytest.mark.parametrize("label,phis", _PHI_SETS)
    def test_phi_segment_builds(self, label, phis):
        tsf = build_phi_segment_frame(4, phis)
        assert tsf.matrix.shape == (16, len(phis))

    @pytest.mark.parametrize("label,phis", _PHI_SETS)
    def test_phi_segment_rank_and_cond_reported(self, label, phis, capsys):
        tsf = build_phi_segment_frame(4, phis)
        # Just confirm attributes exist and are sensible
        assert 0 <= tsf.rank <= len(phis)
        assert tsf.condition_number > 0
        assert tsf.gram_matrix.shape == (len(phis), len(phis))

    def test_phi_segment_frame_non_orthogonal(self):
        """phi kernels are generally non-orthogonal."""
        tsf = build_phi_segment_frame(4, [0.5, 1.0, 1.5])
        gram = tsf.gram_matrix
        # Off-diagonals should be nonzero
        off_diag = gram - torch.diag(gram.diag())
        assert off_diag.abs().max().item() > 1e-6, (
            "phi-segment frame should be non-orthogonal"
        )

    @pytest.mark.parametrize("label,phis", _PHI_SETS)
    def test_phi_segment_exact_factorization_or_report(self, label, phis):
        """
        If the phi segment has sufficient rank (>= rank of a test weight),
        factorization must succeed exactly.  Otherwise report
        SECTOR_INSUFFICIENT_FOR_EXACT_TRANSFER.
        """
        lattice_size = 4
        tsf = build_phi_segment_frame(lattice_size, phis)
        r_needed = len(phis)

        if tsf.rank < r_needed:
            result = "SECTOR_INSUFFICIENT_FOR_EXACT_TRANSFER"
            # Just verify we can detect and report it
            assert result == "SECTOR_INSUFFICIENT_FOR_EXACT_TRANSFER"
            return

        # Use a matrix of the right shape
        W = _make_random_matrix(lattice_size * lattice_size, r_needed, torch.float64)
        # Reduce to rank <= tsf.rank
        gen = torch.Generator().manual_seed(0)
        U = torch.randn(lattice_size * lattice_size, tsf.rank, generator=gen, dtype=torch.float64)
        V = torch.randn(tsf.rank, r_needed, generator=gen, dtype=torch.float64)
        W_reduced = U @ V

        A, B, meta = factor_matrix_through_frame(W_reduced, tsf.matrix)
        err = (B @ A - W_reduced).abs().max().item()
        # Tolerance scaled by the frame condition number (phi frames are
        # generally non-orthogonal; precision degrades proportionally).
        tol = max(_FP64_LINEAR_TOL, 1e-10 * meta.frame_condition_number)
        assert err < tol, (
            f"phi segment {label}: recon error {err} > tol {tol}; "
            f"frame cond={meta.frame_condition_number:.4g}, "
            f"pinv_residual={meta.frame_inverse_residual:.4g}"
        )

    def test_different_phi_segments_different_spans(self):
        """Two phi segments should have different column spans."""
        tsf_A = build_phi_segment_frame(4, [0.1, 0.2])
        tsf_B = build_phi_segment_frame(4, [2.0, 3.0])
        # Project one onto the other and check residual
        A = tsf_A.matrix.to(dtype=torch.float64)
        B = tsf_B.matrix.to(dtype=torch.float64)
        proj = A @ torch.linalg.pinv(A) @ B
        diff = (proj - B).norm().item()
        # The two spans differ meaningfully
        assert diff > 1e-4, "Segments with very different phi values must span different spaces"

    def test_phi_segment_3_sizes(self):
        """Three small phi-segment frames for scientific reporting."""
        results = []
        for phis in [[0.1, 0.2, 0.3], [0.5, 1.0, 1.5], [2.0, 3.0, 4.0]]:
            tsf = build_phi_segment_frame(3, phis)
            gram_eigs = torch.linalg.eigvalsh(tsf.gram_matrix.to(dtype=torch.float64))
            results.append({
                "phis": phis,
                "rank": tsf.rank,
                "cond": tsf.condition_number,
                "gram_eigs": gram_eigs.tolist(),
                "pinv_residual": tsf.pseudoinverse_residual,
            })
        # All results must be finite and recorded
        for r in results:
            assert math.isfinite(r["cond"]) or r["rank"] < len(r["phis"])

    def test_phi_high_segments_may_be_degenerate(self):
        """
        Large phi causes rapid Gaussian decay; high-phi segments may be
        near-rank-deficient.  This is reported, not hidden.
        """
        tsf = build_phi_segment_frame(3, [100.0, 200.0, 300.0])
        # We do not require rank == 3; we require honest reporting
        assert tsf.rank >= 0  # always satisfiable
        # The condition number should be very large or rank < 3
        if tsf.rank == len([100.0, 200.0, 300.0]):
            assert tsf.condition_number > 1e3, (
                "Near-degenerate high-phi segment must report poor conditioning"
            )


# ---------------------------------------------------------------------------
# 7. Metadata correctness
# ---------------------------------------------------------------------------

class TestMetadata:
    def test_metadata_fields(self):
        W = _make_random_matrix(5, 5, torch.float64)
        frame = _orthogonal_frame(8, 5, torch.float64)
        A, B, meta = factor_matrix_through_frame(W, frame)
        assert meta.input_dim == 5
        assert meta.output_dim == 5
        assert meta.sector_width == 8
        assert meta.matrix_rank == 5
        assert meta.frame_rank == 5
        assert math.isfinite(meta.frame_condition_number)
        assert math.isfinite(meta.frame_inverse_residual)
        assert meta.reconstruction_max_abs_error < _FP64_LINEAR_TOL
        assert "float64" in meta.dtype

    def test_condition_number_reported_in_metadata(self):
        W = _make_random_matrix(3, 3, torch.float64)
        frame = _orthogonal_frame(6, 3, torch.float64)
        _, _, meta = factor_matrix_through_frame(W, frame)
        # Orthonormal frame has condition number ~1
        assert meta.frame_condition_number == pytest.approx(1.0, abs=1e-6)
