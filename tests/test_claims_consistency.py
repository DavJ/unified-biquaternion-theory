#!/usr/bin/env python3
"""
Consistency guard between CLAIMS.yaml and status-facing docs.
"""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_FILE = REPO_ROOT / "CLAIMS.yaml"
TARGET_FILES = [
    REPO_ROOT / "STATUS_OF_UBT.md",
    REPO_ROOT / "README.md",
    REPO_ROOT / "WHAT_IS_PROVED.md",
    REPO_ROOT / "docs" / "CURRENT_STATUS.md",
    REPO_ROOT / "docs" / "THEORY_STATUS.md",
    REPO_ROOT / "docs" / "FINAL_STATUS_REPORT.md",
]


def _parse_claims_yaml(path: Path) -> dict[str, dict[str, object]]:
    claims: dict[str, dict[str, object]] = {}
    current_claim: str | None = None
    in_forbidden = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        if line == "claims:":
            continue

        if line.startswith("  ") and line.endswith(":") and not line.startswith("    "):
            current_claim = line.strip()[:-1]
            claims[current_claim] = {"forbidden_wording": []}
            in_forbidden = False
            continue

        if current_claim is None:
            continue

        stripped = line.strip()
        if stripped.startswith("forbidden_wording:"):
            in_forbidden = True
            continue

        if stripped.startswith(("status:", "evidence:")):
            in_forbidden = False
            continue

        if in_forbidden and stripped.startswith("- "):
            phrase = stripped[2:].strip().strip('"').strip("'")
            claims[current_claim]["forbidden_wording"].append(phrase)

    return claims


def test_forbidden_wording_not_present_in_status_docs() -> None:
    claims = _parse_claims_yaml(CLAIMS_FILE)
    violations: list[str] = []

    for claim_name, claim_data in claims.items():
        for phrase in claim_data.get("forbidden_wording", []):
            needle = phrase.casefold()
            for file_path in TARGET_FILES:
                for lineno, text in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
                    line_cf = text.casefold()
                    if needle not in line_cf:
                        continue
                    if phrase == "[L1] PROVEN":
                        if "alpha" not in line_cf and "α" not in line_cf:
                            continue
                    violations.append(
                        f"{file_path.relative_to(REPO_ROOT)}:{lineno}: {claim_name} forbidden wording '{phrase}' -> {text.strip()}"
                    )

    assert not violations, "Forbidden claim wording found:\n" + "\n".join(violations)
