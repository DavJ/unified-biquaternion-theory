# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Regression tests for the linearized D-composite audit (GAP-10T-DYN).

Mirrors tools/verify_dcomposite_linearized.py.  The symbol assembly is
shared through a module-scoped fixture; symbolically heavy checks are
marked slow.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

repo_root = Path(__file__).resolve().parents[1]
if str(repo_root / "tools") not in sys.path:
    sys.path.insert(0, str(repo_root / "tools"))

import verify_dcomposite_linearized as dcomp  # noqa: E402


@pytest.fixture(scope="module")
def symbol_matrix():
    return dcomp.assemble_symbol()


def test_wl_subsector_lemma_and_counterexample():
    res = dcomp.check_sector_lemma()
    assert res["hermitian_part_forced_zero_under_all_connections"]
    assert res["necessity_counterexample_D_in_WL_with_Theta_not_in_WL"]


def test_gradient_annihilation_regression(symbol_matrix):
    # regression for the 2026-07-26 delta-e transposition bug: the
    # linearized Levi-Civita connection must annihilate exact gradients
    assert dcomp.check_gradient_annihilation(symbol_matrix)["gradients_in_kernel"]


@pytest.mark.slow
def test_gradient_annihilation_symbolic(symbol_matrix):
    assert dcomp.check_gradient_annihilation_symbolic(symbol_matrix)["gradients_in_kernel_symbolic"]


def test_generic_ranks_and_determinant(symbol_matrix):
    res = dcomp.check_generic_ranks(symbol_matrix)
    assert res["rank_A_is_9"]
    assert res["rank_A2_is_6"]
    assert res["det_I_minus_A_is_(1-q)^6"]


def test_off_resonance_flatness(symbol_matrix):
    res = dcomp.check_off_resonance_flatness(symbol_matrix)
    assert res["driven_solution_is_exact_gradient"]
    assert res["zero_anholonomy_off_resonance"]


def test_resonant_sector(symbol_matrix):
    res = dcomp.check_resonant_sector(symbol_matrix)
    assert res["resonant_eigenspace_dim_6"]
    assert res["all_resonant_modes_anholonomic"]
    assert res["resonant_curl_rank_6"]


@pytest.mark.slow
def test_operator_identity_symbolic(symbol_matrix):
    assert dcomp.check_operator_identity(symbol_matrix)["A3_equals_qA2_symbolic"]


def test_resonant_multipoint(symbol_matrix):
    res = dcomp.check_resonant_multipoint(symbol_matrix)
    assert res["dim6_at_all_points"]
    assert res["curl_rank6_at_all_points"]


def test_resonant_riemann_image(symbol_matrix):
    res = dcomp.check_resonant_riemann_image(symbol_matrix)
    assert res["riemann_map_rank6_at_all_generic_test_points"]


@pytest.mark.slow
def test_trace_theorem_symbolic(symbol_matrix):
    assert dcomp.check_trace_theorem(symbol_matrix)["traces_6qk_symbolic"]


def test_real_fourier_no_go():
    res = dcomp.check_real_fourier_no_go()
    assert res["fourier_determinant_modulus_is_1_plus_r2"]
    assert res["no_real_fourier_singularity"]
