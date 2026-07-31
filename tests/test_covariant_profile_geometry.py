from pathlib import Path

import sympy as sp

from tools.verify_covariant_profile_geometry import (
    ambient_frame_check,
    centrality_check,
    lorentz_slice_check,
)


def test_general_sharp_symmetric_product_is_central() -> None:
    _, vector, _ = centrality_check()
    assert vector == sp.zeros(3, 1)


def test_lorentz_slice_is_real_lorentzian() -> None:
    expression = lorentz_slice_check()
    assert sp.I not in expression.free_symbols


def test_ambient_profile_frame_is_pairing_compatible() -> None:
    assert ambient_frame_check() == sp.zeros(14, 14)


def test_covariant_note_keeps_metric_channels_separate() -> None:
    root = Path(__file__).resolve().parents[1]
    note = (
        root
        / "research_tracks/T1_GR/free_fiber_completion/"
        "gap_10s_covariant_profile_geometry.tex"
    ).read_text(encoding="utf-8")
    lower = note.lower()

    assert "central complex metric" in lower
    assert "no noncentral" in lower
    assert "antisymmetric bivector" in lower
    assert "flat ambient/profile transport" in lower
    assert "induced levi--civita" in lower
    assert "no new propagating field" in lower
    assert "action origin and mode selection" in lower
