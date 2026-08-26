"""Regression tests for the joint theta Mellin matrix verifier."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "verify_theta_mellin_matrix.py"


def load_tool():
    spec = importlib.util.spec_from_file_location("verify_theta_mellin_matrix", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TOOL = load_tool()


def test_modular_s_matrix() -> None:
    TOOL.check_s_matrix()


def test_multiplier_zero_lines() -> None:
    TOOL.check_boundary_zero_lines()


def test_multipliers_nonzero_in_sampled_open_strip() -> None:
    TOOL.check_open_strip_nonvanishing()


def test_three_mellin_series() -> None:
    TOOL.check_mellin_series()


def test_rank_four_character_channels_mod_5() -> None:
    TOOL.check_character_channels_mod_5()


def test_principal_character_l_factor() -> None:
    TOOL.check_principal_l_factor()


def test_symmetry_admissible_metric_classification() -> None:
    TOOL.check_metric_classification()


def test_primitive_mod_5_functional_equations() -> None:
    TOOL.check_primitive_functional_equations_mod_5()


def test_additive_residue_representation_mod_5() -> None:
    TOOL.check_additive_residue_representation_mod_5()


def test_elliptic_derivative_odd_sector_mod_5() -> None:
    TOOL.check_elliptic_derivative_odd_sector_mod_5()
