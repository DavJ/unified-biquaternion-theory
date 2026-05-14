# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
test_gr_status_consistency.py
==============================
Pytest regression guards for GR-sector claims across the repository.

These tests fail if:
  1. README.md or core status files simultaneously claim both
     "full exact Theta-only Einstein derivation completed" and
     "only sector recovery" (contradictory claims).
  2. Key GR deliverable files are missing from the repository.
  3. Any file in the scan set contains explicitly forbidden overclaim language
     about the GR derivation.

These tests encode the invariant established in March 2026:
  - The combined variation equation is the fundamental statement.
  - Termwise separation is NOT automatic.
  - GR is recovered as a sector/limit/projection, not for all Theta.
  - There is no contradiction between "UBT contains GR" and
    "not yet exact full Theta-only theorem".
"""

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _read_file(path: pathlib.Path) -> str:
    """Read a file, returning empty string on error."""
    try:
        return path.read_text(errors="ignore")
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# W2: Required deliverable files must exist
# ---------------------------------------------------------------------------

class TestRequiredFilesExist:
    """Guard: GR-sector deliverable files must be present."""

    REQUIRED = [
        "docs/reports/gr_recovery_levels.md",
        "ARCHIVE/archive_legacy/consolidation_project/GR_closure/theta_vs_metric_variation_note.tex",
        "ARCHIVE/archive_legacy/consolidation_project/GR_closure/gr_sector_conditions.tex",
        "docs/ubt_gr_relationship.md",
    ]

    @pytest.mark.parametrize("rel_path", REQUIRED)
    def test_file_exists(self, rel_path):
        path = ROOT / rel_path
        assert path.exists(), (
            f"Required GR-sector deliverable file is missing: {rel_path}\n"
            "This file encodes the UBT-vs-GR relationship and must not be deleted."
        )


# ---------------------------------------------------------------------------
# W5: No conflicting GR claims across README / status files
# ---------------------------------------------------------------------------

# Phrases that assert "full exact Theta-only derivation completed"
_OVERCLAIM_PATTERNS = [
    # Do not claim the pure-Theta-only derivation is complete/proved
    # when only sector recovery has been established.
    r"full\s+exact\s+[Tt]heta[\-\s]+only\s+[Ee]instein\s+derivation\s+completed",
    r"[Tt]heta[\-\s]+only\s+closure\s+(?:fully\s+)?proved",
    r"pure[\-\s]+[Tt]heta\s+action\s+(?:fully\s+)?(?:proves?|derives?)\s+[Ee]instein",
    # Do not say termwise separation is automatic
    r"each\s+term\s+must\s+vanish\s+separately",
    r"terms?\s+vanish\s+independently",
    r"(?:arbitrary|independent)\s+variation\s+of\s+(?:the\s+)?two\s+(?:summed\s+)?terms",
    # Do not claim UBT contradicts GR (match only the POSITIVE contradiction claim,
    # not the "no contradiction" / "there is no contradiction" statement)
    r"\bUBT\s+(?:is\s+in\s+)?contradicts?\s+(?:with\s+)?GR\b",
    r"\bthere\s+is\s+a\s+contradiction\b[^,\.]*\bUBT\b",
    r"\bUBT\s+(?:is\s+)?incompatible\s+with\s+GR\b",
]

# Files to scan for conflicting claims
_SCAN_FILES = [
    "README.md",
    "CURRENT_STATUS.md",
    "DERIVATION_INDEX.md",
    "docs/THEORY_STATUS.md",
    "docs/reports/gr_recovery_final_status.md",
    "docs/reports/gr_recovery_levels.md",
    "ARCHIVE/archive_legacy/consolidation_project/GR_closure/step2_theta_only_closure.tex",
]


class TestNoConflictingGRClaims:
    """Guard: forbidden GR-claim language must not appear in key files."""

    @pytest.mark.parametrize("rel_path", _SCAN_FILES)
    def test_no_overclaim_language(self, rel_path):
        path = ROOT / rel_path
        if not path.exists():
            pytest.skip(f"File not found: {rel_path}")
        text = _read_file(path)
        violations = []
        for pat in _OVERCLAIM_PATTERNS:
            if re.search(pat, text, re.IGNORECASE):
                violations.append(pat)
        assert not violations, (
            f"Forbidden GR-claim language found in {rel_path}:\n"
            + "\n".join(f"  Pattern: {p}" for p in violations)
            + "\n\nUse permitted language instead:\n"
            "  ✅ 'GR-compatible sector recovered'\n"
            "  ✅ 'Einstein equations hold on the admissible sector'\n"
            "  ✅ 'variational embedding / standard Einstein-sector recovery'\n"
            "  ❌ 'full exact Theta-only Einstein derivation completed'\n"
            "  ❌ 'each term must vanish separately'\n"
            "  ❌ 'UBT contradicts GR'\n"
        )


# ---------------------------------------------------------------------------
# W5: gr_recovery_levels.md must contain the three level labels
# ---------------------------------------------------------------------------

class TestGRRecoveryLevelsContent:
    """Guard: gr_recovery_levels.md must define the three canonical levels."""

    LEVEL_LABELS = [
        "exact_projected_recovery",
        "constrained_sector_recovery",
        "low_energy_limit_recovery",
    ]

    def test_level_labels_present(self):
        path = ROOT / "docs/reports/gr_recovery_levels.md"
        if not path.exists():
            pytest.fail("docs/reports/gr_recovery_levels.md does not exist")
        text = _read_file(path)
        missing = [lbl for lbl in self.LEVEL_LABELS if lbl not in text]
        assert not missing, (
            "docs/reports/gr_recovery_levels.md is missing required level labels:\n"
            + "\n".join(f"  {lbl}" for lbl in missing)
        )

    def test_consistency_sentence_present(self):
        """The mandatory consistency sentence must appear in gr_recovery_levels.md."""
        path = ROOT / "docs/reports/gr_recovery_levels.md"
        if not path.exists():
            pytest.fail("docs/reports/gr_recovery_levels.md does not exist")
        text = _read_file(path)
        # Check for the key phrase about no contradiction
        assert re.search(
            r"no\s+contradiction",
            text,
            re.IGNORECASE,
        ), (
            "docs/reports/gr_recovery_levels.md must contain a statement that "
            "'There is no contradiction between UBT and GR'."
        )


# ---------------------------------------------------------------------------
# W1: theta_vs_metric_variation_note.tex must contain the key equation label
# ---------------------------------------------------------------------------

class TestThetaVariationNoteContent:
    """Guard: the theta variation note must define E_Theta, E_g, J, and combined eq."""

    REQUIRED_STRINGS = [
        r"mathcal{E}_\Theta",  # E_Theta operator
        r"mathcal{E}_g",       # E_g operator
        r"J^{",                # J map (adjoint)
        # The combined equation label or the combined equation itself
    ]

    def test_key_operators_defined(self):
        path = ROOT / "ARCHIVE/archive_legacy/consolidation_project/GR_closure/theta_vs_metric_variation_note.tex"
        if not path.exists():
            pytest.fail("theta_vs_metric_variation_note.tex does not exist")
        text = _read_file(path)
        missing = [s for s in self.REQUIRED_STRINGS if s not in text]
        assert not missing, (
            "theta_vs_metric_variation_note.tex is missing required content:\n"
            + "\n".join(f"  {s}" for s in missing)
        )

    def test_warning_box_present(self):
        """The note must contain an explicit warning against termwise separation."""
        path = ROOT / "ARCHIVE/archive_legacy/consolidation_project/GR_closure/theta_vs_metric_variation_note.tex"
        if not path.exists():
            pytest.fail("theta_vs_metric_variation_note.tex does not exist")
        text = _read_file(path)
        assert "Warning" in text or "tcolorbox" in text, (
            "theta_vs_metric_variation_note.tex must contain a Warning box "
            "explicitly stating that termwise separation is not automatic."
        )


# ---------------------------------------------------------------------------
# W3: gr_sector_conditions.tex must contain condition table
# ---------------------------------------------------------------------------

class TestGRSectorConditionsContent:
    """Guard: gr_sector_conditions.tex must list explicit conditions C1–C6."""

    def test_conditions_listed(self):
        path = ROOT / "ARCHIVE/archive_legacy/consolidation_project/GR_closure/gr_sector_conditions.tex"
        if not path.exists():
            pytest.fail("gr_sector_conditions.tex does not exist")
        text = _read_file(path)
        # At minimum, conditions C1 and C6 should appear
        for condition in ["C1", "C6"]:
            assert condition in text, (
                f"gr_sector_conditions.tex must list condition {condition}"
            )

    def test_mandatory_statement_present(self):
        """Must explicitly state GR recovery is exact only on the sector."""
        path = ROOT / "ARCHIVE/archive_legacy/consolidation_project/GR_closure/gr_sector_conditions.tex"
        if not path.exists():
            pytest.fail("gr_sector_conditions.tex does not exist")
        text = _read_file(path)
        # Check for either the exact phrasing or a close variant
        assert re.search(
            r"(?:GR\s+reproduction|GR\s+recovery)\s+is\s+exact\s+only",
            text,
            re.IGNORECASE,
        ) or re.search(
            r"only\s+on\s+the\s+sector",
            text,
            re.IGNORECASE,
        ), (
            "gr_sector_conditions.tex must contain the mandatory statement: "
            "'GR reproduction is exact only on the sector satisfying the listed conditions'"
        )
