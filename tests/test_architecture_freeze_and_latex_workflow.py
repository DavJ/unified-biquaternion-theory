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
    assert "shutil.rmtree(report_dir" in tool
    assert "as_completed" in tool
    assert "--strict" in tool


def test_pdf_publish_map_contains_tetrad_milestone_documents() -> None:
    mapping = (ROOT / ".github/latex_publish_map.tsv").read_text(encoding="utf-8")
    for required in (
        "canonical/UBT_canonical_main.pdf",
        "papers/UBT_GR_Submission.pdf",
        "gap_10omega_connection_elimination.pdf",
        "gap_10i_integrability_selection.pdf",
        "covariant_tetrad_student_paper.pdf",
    ):
        assert required in mapping
