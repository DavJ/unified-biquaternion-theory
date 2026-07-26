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

def test_lorentz_invariant_pairing_rigidity():
    res = audit.check_lorentz_invariant_pairings()
    assert res["unique_symmetric_form_is_eta"]
    assert res["sharp_matrix_is_eta"]
    assert res["sharp_full_lorentz_invariant"]
    assert res["ddagger_matrix_is_euclidean"]
    assert res["ddagger_rotation_invariant"]
    assert res["ddagger_all_boosts_fail"]
    assert res["ddagger_not_full_lorentz_invariant"]



def test_authoritative_ledgers_include_pairing_no_go():
    root = repo_root
    authoritative = [
        root / "CLAIMS.yaml",
        root / "CLAIMS_MATRIX.md",
        root / "STATUS.md",
        root / "STATUS_OF_UBT.md",
        root / "WHAT_IS_PROVED.md",
        root / "canonical/gr_closure/README.md",
        root / "papers/UBT_GR_Submission.tex",
    ]
    for path in authoritative:
        text = path.read_text(encoding="utf-8")
        assert "GAP-10T-PAIRING-NOGO" in text, f"missing pairing no-go in {path}"


def test_authoritative_ledgers_do_not_reopen_exact_spin_current():
    stale = (
        "derive the minimal branch, exact UBT spin current",
        "derive the exact spin current",
        "canonical action and exact spin current",
    )
    authoritative = [
        repo_root / "CLAIMS.yaml",
        repo_root / "STATUS_OF_UBT.md",
        repo_root / "canonical/CANONICAL_DEFINITIONS.md",
        repo_root / "canonical/THEORY/canonical/canonical_action.tex",
        repo_root / "papers/UBT_GR_Submission.tex",
    ]
    for path in authoritative:
        text = path.read_text(encoding="utf-8")
        for phrase in stale:
            assert phrase not in text, f"stale phrase {phrase!r} in {path}"


def test_composite_flat_admissibility_volume_terms():
    res = audit.check_composite_flat_admissibility(fast=True)
    assert res["volume_terms_first_variation_vanishes"], (
        "auxiliary exact-gradient volume terms must be stationary at the affine "
        "background for all Lambda, kappa, N0"
    )


import pytest  # noqa: E402


@pytest.mark.slow
def test_composite_flat_admissibility_einstein_term():
    res = audit.check_composite_flat_admissibility(fast=False)
    assert res["einstein_term_first_variation_vanishes"], (
        "linearised Einstein-term variation must integrate to zero at the "
        "constant exact-gradient background"
    )
