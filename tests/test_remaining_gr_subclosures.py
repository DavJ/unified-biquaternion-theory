from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_exact_remaining_gr_subclosure_verifier_runs() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools/verify_remaining_gr_subclosures.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert "ALL CHECKS PASSED" in result.stdout
    for phrase in (
        "rank 24/24",
        "Lorentz slice",
        "partial_psi g = 0",
        "augmented connection",
    ):
        assert phrase in result.stdout


def test_new_subclosure_sources_are_present_and_scoped() -> None:
    required = {
        "canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex": (
            "GAP-10T-PALATINI: CLOSED CONDITIONALLY",
            "GAP-10T-DYN: NARROWED",
        ),
        "canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex": (
            "GAP-10L-SYM: CLOSED CONDITIONALLY",
            "GAP-10$\\psi$: NARROWED",
        ),
        "canonical/gr_closure/gap_10i_augmented_holonomy.tex": (
            "GAP-10I-PRESCRIBED: CLOSED",
            "GAP-10I-CURVED: NARROWED",
        ),
        "canonical/gr_closure/gap_10d_low_energy_uniqueness.tex": (
            "GAP-10D-PALATINI: CLOSED CONDITIONALLY",
            "GAP-10D: NARROWED",
        ),
    }
    for rel, phrases in required.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for phrase in phrases:
            assert phrase in text
        assert "narrowed" in text.lower() or "conditional" in text.lower()


def test_claim_ledger_uses_conditional_and_narrowed_statuses() -> None:
    claims = yaml.safe_load((ROOT / "CLAIMS.yaml").read_text(encoding="utf-8"))
    assumptions = "\n".join(claims["claims"]["gr_chain"]["assumptions"])
    for phrase in (
        "GAP-10T-PALATINI: CLOSED CONDITIONALLY",
        "GAP-10T-DYN: NARROWED",
        "GAP-10L-SYM: CLOSED CONDITIONALLY",
        "GAP-10L-DYN: NARROWED",
        "GAP-10I-PRESCRIBED: CLOSED",
        "GAP-10I-CURVED: NARROWED",
        "GAP-10D-PALATINI: CLOSED CONDITIONALLY",
        "GAP-10D: NARROWED",
        "GAP-10psi: NARROWED",
    ):
        assert phrase in assumptions


def test_active_status_surfaces_do_not_overclaim_full_closure() -> None:
    files = (
        "AGENTS.md",
        "CLAIMS_MATRIX.md",
        "STATUS_OF_UBT.md",
        "WHAT_IS_PROVED.md",
        "canonical/AXIOMS.md",
        "papers/UBT_GR_Submission.tex",
        "docs/czech/UBT_KOVARIANTNI_GEOMETRIE_PRO_STUDENTY_CZ.md",
    )
    combined = "\n".join((ROOT / f).read_text(encoding="utf-8") for f in files)
    for full_gap in (
        "GAP-10T-DYN",
        "GAP-10L-DYN",
        "GAP-10I-CURVED",
        "GAP-10D",
    ):
        assert full_gap in combined
    assert "NARROWED" in combined
    assert "GAP-B-MASTER" in combined and "OPEN" in combined
    assert "GAP-U2" in combined


def test_agent_instructions_guard_conditional_subclosures() -> None:
    for rel in ("AGENTS.md", ".github/copilot-instructions.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        lower = text.lower()
        assert "palatini" in lower
        assert "lovelock" in lower
        assert "conditional" in lower
        assert "prescribed" in lower and "holonomy" in lower
        assert "never promote" in lower or "do not merge" in lower


def test_publish_map_contains_v10_3_subclosure_papers() -> None:
    mapping = (ROOT / ".github/latex_publish_map.tsv").read_text(encoding="utf-8")
    for name in (
        "gap_10t_paladini_torsion_dynamics.pdf",
        "gap_10l_psi_symmetry_propagation.pdf",
        "gap_10i_augmented_holonomy.pdf",
        "gap_10d_low_energy_uniqueness.pdf",
    ):
        assert name in mapping
