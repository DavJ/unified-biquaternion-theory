import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]
README = ROOT / "README.md"
def test_readme_has_updated_rating_and_no_bq_confusion():
    txt = README.read_text(encoding="utf-8", errors="ignore")
    assert "6.2/10" in txt, "README score must be updated to 6.2/10"
    bad_phrases = [
        "not really biquaternionic",
        "isn't truly biquaternionic",
        "not biquaternionic in practice",
    ]
    for p in bad_phrases:
        assert p not in txt, f"Remove misleading phrase in README: {p!r}"
