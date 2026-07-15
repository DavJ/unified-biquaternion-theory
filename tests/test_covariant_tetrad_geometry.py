"""Exact algebra and status tests for the canonical covariant-tetrad route."""
from pathlib import Path

from tools.verify_covariant_tetrad_rank import (
    arbitrary_metric_variation_check,
    central_jordan_check,
    rank_check,
)

ROOT = Path(__file__).resolve().parent.parent


def test_central_jordan_identity() -> None:
    central_jordan_check()


def test_tetrad_metric_rank() -> None:
    rank, nullity = rank_check()
    assert rank == 10
    assert nullity == 6


def test_arbitrary_symmetric_variation_is_reachable() -> None:
    arbitrary_metric_variation_check()


def test_student_chapter_is_wired_into_textbook() -> None:
    main = (ROOT / "docs/textbook/main.tex").read_text(encoding="utf-8")
    chapter = ROOT / "docs/textbook/chapters/04_covariant_tetrad_geometry.tex"
    assert "04_covariant_tetrad_geometry" in main
    assert chapter.exists()


def test_connection_is_not_naively_identified_with_christoffel() -> None:
    text = (ROOT / "canonical/geometry/biquaternion_connection.tex").read_text(encoding="utf-8")
    assert "related but not identical" in text
    assert "tetrad postulate" in text
    assert "generally incorrect" in text
