from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "verify_gem_compact_modes.py"
TRACK = ROOT / "research_tracks" / "gem_compact_modes"


def test_track_files_exist() -> None:
    for name in (
        "README.md",
        "STATUS.md",
        "FALSIFICATION.md",
        "LEGACY_MAP.md",
        "gem_compact_modes.tex",
    ):
        assert (TRACK / name).is_file(), name


def test_verifier_passes_and_reports_open_scope() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["status"] == "PASS"
    assert payload["balanced"]["current_psi"] == 0.0
    assert payload["balanced"]["compact_gradient"] > 0.0
    assert all(
        value == "0"
        for row in payload["lorentz_delta_g"]
        for value in row
    )
    assert payload["godel_kinematics"]["g_ty"] != 0.0
    assert payload["godel_kinematics"]["dtheta0_xy"] != 0.0
    assert "canonical action coupling" in payload["not_tested"]


def test_legacy_sources_are_preserved() -> None:
    for relative in (
        "speculative_extensions/causality/ctc_conditions.tex",
        "speculative_extensions/causality/complex_time_causal_structure.tex",
        "speculative_extensions/causality/rotation_complex_time.tex",
        "speculative_extensions/causality/chronology_protection_ubt.tex",
        "speculative_extensions/causality/ctc_methodology.tex",
        "speculative_extensions/appendices/appendix_J_rotating_spacetime_ctc.tex",
    ):
        assert (ROOT / relative).is_file(), relative


def test_status_does_not_overclaim_godel_or_ctc() -> None:
    status = (TRACK / "STATUS.md").read_text(encoding="utf-8")
    assert "GEM-CM-G1 | **OPEN**" in status
    assert "GEM-CM-G2 | **OPEN**" in status
    assert "GEM-CM-CTC | **OPEN / SEPARATE**" in status
