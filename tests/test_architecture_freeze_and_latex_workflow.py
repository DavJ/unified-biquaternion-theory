from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_architecture_freeze_is_present_in_agent_instructions() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    copilot = (ROOT / ".github/copilot-instructions.md").read_text(encoding="utf-8")
    for text in (agents, copilot):
        lower = text.lower()
        assert "architecture" in lower and "repair" in lower
        assert "framework freeze" in lower
        assert "no agent" in lower or "never perform an autonomous" in lower


def test_historical_fiber_route_is_not_described_as_disproved() -> None:
    note = (ROOT / "canonical/gr_closure/HISTORICAL_FIBER_ROUTE_STATUS.md").read_text(
        encoding="utf-8"
    )
    assert "not" in note.lower() and "abandoned because of a" in note.lower()
    assert "weak" in note.lower() and "select" in note.lower()


def test_latex_workflow_uses_non_fail_fast_batch_report() -> None:
    workflow = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    tool = (ROOT / "tools/latex_audit.py").read_text(encoding="utf-8")
    assert "tools/latex_audit.py" in workflow
    assert "reports/latex_build" in workflow
    assert "Commit report and curated PDFs" in workflow
    assert 'remote_head="$(git rev-parse origin/master)"' in workflow
    assert '"$remote_head" != "$GITHUB_SHA"' in workflow
    assert "refusing to commit stale PDFs/report" in workflow
    assert "git pull --rebase" not in workflow
    assert "shutil.rmtree(report_dir" in tool
    assert "as_completed" in tool
    assert "--strict" in tool


def test_pdf_publish_map_contains_only_whitelisted_pdfs() -> None:
    """New policy: only two curated PDFs are tracked in git.
    All other milestone PDFs are produced as CI artifacts (not committed).
    """
    mapping = (ROOT / ".github/latex_publish_map.tsv").read_text(encoding="utf-8")
    # Only the two whitelisted PDFs appear in the publish map.
    assert "canonical/UBT_canonical_main.pdf" in mapping
    assert "papers/UBT_GR_Submission.pdf" in mapping
    # General git add of the whole pdfs directory is forbidden.
    assert "git add docs/pdfs" not in mapping

    # Milestone .tex sources still exist and are compiled by the LaTeX audit.
    gr = ROOT / "canonical" / "gr_closure"
    for stem in (
        "gap_10omega_connection_elimination",
        "gap_10i_integrability_selection",
        "gap_10t_palatini_torsion_dynamics",
        "gap_10l_psi_symmetry_propagation",
        "gap_10i_augmented_holonomy",
        "gap_10d_low_energy_uniqueness",
        "covariant_tetrad_rank_theorem",
    ):
        assert (gr / f"{stem}.tex").is_file(), f"Missing milestone source: {stem}.tex"

    # The two whitelisted destination paths are present.
    for tracked in (
        "docs/pdfs/UBT_canonical_main.pdf",
        "docs/pdfs/UBT_GR_Submission.pdf",
    ):
        assert tracked in mapping
