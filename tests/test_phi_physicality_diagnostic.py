"""Regression tests for the corrected phi physicality criterion."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "compute_dalpha_dphi.py"
SPEC = importlib.util.spec_from_file_location("compute_dalpha_dphi", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def test_nonzero_r_alone_does_not_give_local_phase_dependence() -> None:
    assert MOD.dalpha_dphi_at_zero(r=0.1, rho=0.0) == 0.0
    assert "no local phase dependence" in MOD.phi_status(r=0.1, rho=0.0)


def test_nonzero_rho_r_gives_nonzero_formula_value() -> None:
    derivative = MOD.dalpha_dphi_at_zero(r=0.1, rho=0.5)
    assert derivative != 0.0
    assert "local phase dependence for supplied data" in MOD.phi_status(r=0.1, rho=0.5)
