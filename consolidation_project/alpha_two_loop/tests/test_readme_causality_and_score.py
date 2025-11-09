import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
README = ROOT / "README.md"

def test_score_is_6_2():
    txt = README.read_text(encoding="utf-8", errors="ignore")
    assert "6.2/10" in txt, "README must show 6.2/10"

def test_has_causality_line():
    txt = README.read_text(encoding="utf-8", errors="ignore")
    has_causality = (
        "CT scheme preserves macroscopic causality" in txt 
        or "macroscopic causality is preserved" in txt
    )
    assert has_causality, "Add causality clarification to README"
