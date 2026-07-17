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
TARGET_DIRS = [
    REPO_ROOT / "canonical" / "gauge",
    REPO_ROOT / "canonical" / "qm_emergence",
]
TARGET_SUFFIXES = {".md", ".tex"}


def _iter_target_files() -> list[Path]:
    files = list(TARGET_FILES)
    for directory in TARGET_DIRS:
        files.extend(
            path
            for path in directory.rglob("*")
            if path.is_file() and path.suffix.casefold() in TARGET_SUFFIXES
        )
    return sorted(set(files))


def _parse_claims_yaml(path: Path) -> dict[str, dict[str, object]]:
    claims: dict[str, dict[str, object]] = {}
    current_claim: str | None = None
    in_forbidden = False
    in_context = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        if line == "claims:":
            continue

        if line.startswith("  ") and line.endswith(":") and not line.startswith("    "):
            current_claim = line.strip()[:-1]
            claims[current_claim] = {"forbidden_wording": [], "context_tokens": []}
            in_forbidden = False
            in_context = False
            continue

        if current_claim is None:
            continue

        stripped = line.strip()
        if stripped.startswith("forbidden_wording:"):
            in_forbidden = True
            in_context = False
            continue

        if stripped.startswith("context_tokens:"):
            in_context = True
            in_forbidden = False
            continue

        if stripped.startswith(("status:", "evidence:")):
            in_forbidden = False
            in_context = False
            continue

        if in_forbidden and stripped.startswith("- "):
            phrase = stripped[2:].strip().strip('"').strip("'")
            claims[current_claim]["forbidden_wording"].append(phrase)
            continue

        if in_context and stripped.startswith("- "):
            token = stripped[2:].strip().strip('"').strip("'")
            claims[current_claim]["context_tokens"].append(token.casefold())

    return claims


def test_forbidden_wording_not_present_in_status_docs() -> None:
    claims = _parse_claims_yaml(CLAIMS_FILE)
    violations: list[str] = []

    for claim_name, claim_data in claims.items():
        context_tokens = claim_data.get("context_tokens", [])
        for phrase in claim_data.get("forbidden_wording", []):
            needle = phrase.casefold()
            for file_path in _iter_target_files():
                for lineno, text in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
                    line_cf = text.casefold()
                    if needle not in line_cf:
                        continue
                    if context_tokens and not any(token in line_cf for token in context_tokens):
                        continue
                    violations.append(
                        f"{file_path.relative_to(REPO_ROOT)}:{lineno}: {claim_name} forbidden wording '{phrase}' -> {text.strip()}"
                    )

    assert not violations, "Forbidden claim wording found:\n" + "\n".join(violations)


def test_gauge_and_qm_honest_status_headers_present() -> None:
    gauge = (REPO_ROOT / "canonical" / "gauge" / "GAUGE_MASTER_STATUS.md").read_text(encoding="utf-8")
    su3 = (REPO_ROOT / "canonical" / "su3_derivation" / "su3_from_involutions.tex").read_text(encoding="utf-8")
    born = (REPO_ROOT / "canonical" / "qm_emergence" / "step7_born_rule.tex").read_text(encoding="utf-8")

    assert "DEPRECATED AS A STATUS SOURCE" in gauge
    assert "GAP-SU3-DYN" in su3
    assert "(e^{i\\theta}\\mathbf{I})^2=-e^{2i\\theta}" in su3
    assert "RETRACTED (2026-07-17)" in born
    assert "L e^{-2Dk^2T}" in born
