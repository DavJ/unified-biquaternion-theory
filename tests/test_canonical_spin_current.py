# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""
Regression tests for the GAP-10T-DYN / GAP-10D canonical action audit.

Mirrors tools/verify_canonical_spin_current.py.  All checks are exact
(SymPy); see canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex.
"""
from __future__ import annotations

import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
if str(repo_root / "tools") not in sys.path:
    sys.path.insert(0, str(repo_root / "tools"))

import verify_canonical_spin_current as audit  # noqa: E402


def test_conventions_exact():
    res = audit.check_conventions()
    assert res["central_jordan"], "central Jordan identity failed"
    assert res["slice_antihermitian"], "slice basis not anti-Hermitian"
    assert res["connection_preserves_slice"], "pure pair leaves Lorentz slice"


def test_kinetic_term_algebraic_in_connection():
    res = audit.check_algebraic_omega_dependence()
    assert res["degree_two"], (
        "kinetic density must be algebraic (degree two) in Omega; "
        "otherwise the no-curvature-from-S_Theta statement fails"
    )


def test_slice_lemma_both_pairings():
    res = audit.check_slice_lemma()
    assert res["ddagger"] and res["sharp"], (
        "spin current must depend only on the anti-Hermitian part of Theta "
        "when D Theta lies in the Lorentz slice"
    )


def test_pointwise_rigidity_both_pairings():
    res = audit.check_pointwise_rigidity()
    assert res["ddagger"] and res["sharp"], (
        "joint kernel over the four tetrad slots must be exactly "
        "anti-Hermitian part == 0"
    )


def test_flat_affine_no_go_gradients():
    res = audit.check_flat_affine_no_go()
    assert res["ddagger_gradient_theta0_independent"]
    assert res["sharp_gradient_theta0_independent"]
    assert res["ddagger_nonzero_gradients"], "expected gradients {+-2 N0}"
    assert res["sharp_nonzero_gradients"], "expected gradients {+-N0}"
