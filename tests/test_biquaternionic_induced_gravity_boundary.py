"""Regression gates for the direct biquaternionic induced-gravity audit."""
from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "verify_biquaternionic_induced_gravity_boundary.py"


def _load():
    spec = importlib.util.spec_from_file_location("biquat_induced", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_biquaternionic_boundary_checks() -> None:
    module = _load()
    module.pairing_signatures()
    module.determinant_hessian()
    module.heat_factor_and_coefficients()
    assert {item["id"] for item in module.CHECKS} == {"B1", "B2", "B3", "B4"}


def test_covariant_variations_against_coordinate_determinant() -> None:
    module = _load()
    module.covariant_volume_variations()


def test_composite_connection_terms_are_retained() -> None:
    module = _load()
    module.value_dependent_connection()
    module.composite_chain_rule()
