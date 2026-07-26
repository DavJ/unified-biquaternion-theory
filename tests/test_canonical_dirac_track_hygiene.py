from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_legacy_current_tetrad_exists_only_in_history() -> None:
    stale_active = [
        ROOT / "research_tracks/dual_sector_clifford5/dual_sector_cl5_rank_status.md",
        ROOT / "tools/verify_dual_sector_cl5_rank.py",
        ROOT / "tests/test_dual_sector_cl5_rank.py",
    ]
    assert all(not path.exists() for path in stale_active)

    history = ROOT / "research_tracks/history/legacy_spinor_current_tetrad_2026-07-26"
    assert (history / "dual_sector_cl5_rank_status.md").exists()
    assert (history / "verify_dual_sector_cl5_rank.py").exists()
    assert (history / "historical_test_dual_sector_cl5_rank.py").exists()


def test_active_dirac_track_states_holomorphy_boundary() -> None:
    status = (
        ROOT
        / "research_tracks/canonical_relation_generalized_dirac/PROOF_STATUS.md"
    ).read_text(encoding="utf-8")
    assert "exact principal symbol and causal cone" in status.lower()
    assert "conditional psi-normal" in status.lower()
    assert "strict" in status.lower() and "holomorphy" in status.lower()
    assert "holomorphic on-shell rank" in status.lower()
