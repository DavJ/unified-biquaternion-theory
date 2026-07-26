from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_gr_canonical_is_current_submission_file():
    text = (ROOT / "papers" / "PUBLICATION_CANONICALS.md").read_text()
    assert "GR track canonical manuscript: `papers/UBT_GR_Submission.tex`" in text
    assert "UBT_GR_Flagship.tex" in text and "superseded" in text.lower()
    assert "UBT_GR_RC2_final.tex" in text


def test_gr_track_is_not_marked_submit_ready_while_dynamics_open():
    index = (ROOT / "papers" / "PUBLICATION_INDEX.md").read_text()
    assert "not submission-ready" in index.lower()
    checklist = (ROOT / "papers" / "ARXIV_SUBMISSION_CHECKLIST.md").read_text()
    assert "SUPERSEDED CHECKLIST" in checklist
    assert "GAP-10T-JET-DYN" in checklist
    assert "GAP-10D" in checklist


def test_current_abstract_states_dynamic_boundary():
    abstract = (ROOT / "papers" / "UBT_GR_Abstract.md").read_text()
    assert "split-jet right inverse" in abstract
    assert "Hilbert--Palatini" in abstract
    assert "remaining problems are dynamical" in abstract
