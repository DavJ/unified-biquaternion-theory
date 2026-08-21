#!/usr/bin/env python3
"""Apply the signed UBT provenance policy to the generated LaTeX audit summary."""

from __future__ import annotations

from pathlib import Path

import apply_provenance_headers as provenance

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUMMARY = ROOT / "reports/latex_build/summary.md"


def mark_summary(path: Path = DEFAULT_SUMMARY) -> None:
    path = path.resolve()
    if not path.is_file():
        raise FileNotFoundError(f"LaTeX audit summary not found: {path}")
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError as exc:
        raise RuntimeError(f"Summary must be inside repository: {path}") from exc

    config = provenance.load_map()
    tier = provenance.classify_path(rel, config)
    if tier not in provenance.TIERS:
        raise RuntimeError(f"{rel} is not a markable provenance tier: {tier}")

    text = path.read_text(encoding="utf-8")
    desired = provenance.apply_marker(text, rel, tier, path.suffix.lower())
    path.write_text(desired, encoding="utf-8")
    print(f"Applied {tier} provenance marker to {rel}")


if __name__ == "__main__":
    mark_summary()
