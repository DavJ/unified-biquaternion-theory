from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_palatini_filename_is_corrected() -> None:
    new = ROOT / "canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex"
    old = ROOT / "canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex"
    assert new.is_file()
    assert not old.exists()


def test_active_status_surfaces_use_correct_name() -> None:
    active = (
        ROOT / "CLAIMS.yaml",
        ROOT / "CLAIMS_MATRIX.md",
        ROOT / "DERIVATION_INDEX.md",
        ROOT / "WHAT_IS_PROVED.md",
        ROOT / ".github/latex_publish_map.tsv",
        ROOT / "canonical/gr_closure/README.md",
        ROOT / "papers/UBT_GR_Submission.tex",
    )
    for path in active:
        text = path.read_text(encoding="utf-8")
        normalized = text.replace("\\_", "_")
        assert "gap_10t_palatini_torsion_dynamics" in normalized
        assert "gap_10t_paladini_torsion_dynamics" not in normalized


def test_standard_provenance_references_are_present() -> None:
    holonomy = (ROOT / "canonical/gr_closure/gap_10i_augmented_holonomy.tex").read_text(
        encoding="utf-8"
    )
    symmetry = (ROOT / "canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex").read_text(
        encoding="utf-8"
    )
    assert "Kobayashi--Nomizu" in holonomy
    assert "kobayashi_nomizu_1963" in holonomy
    assert "Olver" in symmetry
    assert "olver1993" in symmetry
