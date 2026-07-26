from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "docs" / "priority_evidence" / "OCTONION_MULTIVERSE_EVIDENCE.json"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_selected_legacy_assets_match_evidence_hashes():
    data = json.loads(EVIDENCE.read_text())
    for item in data["selected_primary_equation_assets"]:
        path = ROOT / item["path"]
        assert path.is_file(), path
        assert _sha(path) == item["sha256"]


def test_priority_claims_are_mechanism_specific():
    priority = (ROOT / "docs" / "PRIORITY.md").read_text()
    assert "18 March 2016" in priority
    assert "biquaternion electroscalar" in priority.lower()
    assert "not backdated" in priority.lower()
    assert "Einstein-equation derivation" in priority
    assert "clear and transparent **priority claim** for the origin of the theory" not in priority


def test_legacy_archive_is_not_silently_imported_as_canonical():
    readme = (ROOT / "ARCHIVE" / "legacy_research" / "README.md").read_text()
    assert "not part of the current canonical derivation" in readme
    data = json.loads(EVIDENCE.read_text())
    forbidden = "The 2026 projection-free tetrad/metric theorem was published in 2016."
    assert forbidden in data["claim_policy"]["forbidden_without_new_evidence"]
