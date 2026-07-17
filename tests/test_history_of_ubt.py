from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / "docs" / "HISTORY_OF_UBT.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"


def _history() -> str:
    return HISTORY.read_text(encoding="utf-8")


def test_history_records_pre_ai_author_work() -> None:
    text = _history()
    assert "2013–2015 — Handwritten metric and electromagnetic foundations" in text
    assert "calculated several candidate metric tensors" in text
    assert "without AI assistance" in text
    assert "unified biquaternionic" in text


def test_history_preserves_hypotheses_without_overclaiming() -> None:
    text = _history()
    assert "historical research" in text and "hypotheses" in text
    assert "not current canonical theorems" in text
    assert "Ordinary Lorentz transformations preserve the null cone" in text
    assert "transformation-optics/metamaterial cloaking" in text


def test_history_records_human_authorship_and_ai_timeline() -> None:
    text = _history()
    assert "AICON 2025 in Seattle" in text
    assert "NDC London in 2026" in text
    assert "From **16 July 2026**" in text
    assert "This was not an autonomous AI pivot" in text
    assert "human-directed and is not yet fully automated" in text


def test_history_is_linked_and_changelog_records_review() -> None:
    assert "docs/HISTORY_OF_UBT.md" in README.read_text(encoding="utf-8")
    changelog = CHANGELOG.read_text(encoding="utf-8")
    assert "reviewed History of UBT" in changelog
    assert "historical hypotheses" in changelog
