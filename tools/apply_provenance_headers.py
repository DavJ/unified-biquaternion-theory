#!/usr/bin/env python3
"""Apply and verify UBT AI-provenance source markers.

The editorial tier map is PROVENANCE_TIERS.yaml.  This tool may implement the
map, but it must never assign a tier or sign the author's attestation.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MAP = ROOT / "PROVENANCE_TIERS.yaml"
SUPPORTED_SUFFIXES = {".md", ".tex"}
INTERNAL_SKIP_DIRS = {
    ".git",
    ".lake",
    ".pytest_cache",
    "__pycache__",
    "build",
    ".venv",
    "venv",
}
BEGIN = "UBT-AI-PROVENANCE-BEGIN"
END = "UBT-AI-PROVENANCE-END"
SCHEMA = "ubt-ai-provenance/v1"


@dataclass(frozen=True)
class TierInfo:
    key: str
    short: str
    human_review: str
    notice: str


TIERS = {
    "A_attested": TierInfo(
        "A_attested",
        "A",
        "substantive",
        "The author has read the substance and accepts editorial responsibility.",
    ),
    "B_machine_verified": TierInfo(
        "B_machine_verified",
        "B",
        "machine-verification",
        "Machine-verified against named sources or verifiers; individual attestation is not claimed.",
    ),
    "C_working": TierInfo(
        "C_working",
        "C",
        "risk-based",
        "Working material; exhaustive human review is not claimed.",
    ),
}


class ProvenanceError(RuntimeError):
    """Raised when the tier map or a source marker is invalid."""


def load_map(path: Path = DEFAULT_MAP) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ProvenanceError(f"Tier map not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise ProvenanceError(f"Invalid YAML in {path}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("tiers"), dict):
        raise ProvenanceError(f"Malformed tier map: {path}")
    if data.get("default_tier") not in TIERS:
        raise ProvenanceError("default_tier must be A_attested, B_machine_verified, or C_working")
    return data


def matches(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch(path, pattern) for pattern in patterns)


def classify_path(relpath: str, config: dict) -> str | None:
    """Return a tier key, D_historical, or None for excluded paths."""
    relpath = relpath.replace(os.sep, "/")
    if matches(relpath, config.get("exclude", [])):
        return None
    tiers = config["tiers"]
    for key in ("A_attested", "D_historical", "B_machine_verified", "C_working"):
        if matches(relpath, tiers.get(key, [])):
            return key
    return config["default_tier"]


def _policy_path(relpath: str) -> str:
    depth = max(0, len(Path(relpath).parts) - 1)
    return "../" * depth + "AI_PROVENANCE.md"


def marker_fields(relpath: str, tier_key: str) -> list[str]:
    info = TIERS[tier_key]
    return [
        BEGIN,
        f"schema: {SCHEMA}",
        f"tier: {info.key}",
        "ai_assistance: disclosed",
        f"human_review: {info.human_review}",
        "editorial_responsibility: Ing. David Jaroš",
        f"policy: {_policy_path(relpath)}",
        f"notice: {info.notice}",
        END,
    ]


def expected_marker(relpath: str, tier_key: str, suffix: str) -> str:
    fields = marker_fields(relpath, tier_key)
    if suffix == ".md":
        return "<!--\n" + "\n".join(fields) + "\n-->"
    if suffix == ".tex":
        return "\n".join(f"% {line}" for line in fields)
    raise ProvenanceError(f"Unsupported suffix for {relpath}: {suffix}")


def remove_existing_marker(text: str, suffix: str) -> str:
    lines = text.splitlines(keepends=True)
    begin_token = BEGIN
    end_token = END
    begin = next((i for i, line in enumerate(lines) if line.strip().lstrip("% ") == begin_token), None)
    if begin is None:
        return text
    end = next((i for i in range(begin, len(lines)) if lines[i].strip().lstrip("% ") == end_token), None)
    if end is None:
        raise ProvenanceError(f"Found {BEGIN} without {END}")
    start = begin
    if suffix == ".md" and begin > 0 and lines[begin - 1].strip() == "<!--":
        start = begin - 1
    if suffix == ".md" and end + 1 < len(lines) and lines[end + 1].strip() == "-->":
        end += 1
    del lines[start : end + 1]
    # Remove at most one blank line left by the old marker.
    if start < len(lines) and lines[start].strip() == "":
        del lines[start]
    return "".join(lines)


def _markdown_insertion_index(lines: list[str]) -> int:
    """Preserve leading front matter, status blockquotes, and comment headers."""
    i = 0
    n = len(lines)
    if n and lines[0].strip() == "---":
        i = 1
        while i < n and lines[i].strip() != "---":
            i += 1
        if i < n:
            i += 1
    while i < n:
        start = i
        while i < n and not lines[i].strip():
            i += 1
        if i < n and lines[i].lstrip().startswith("<!--"):
            while i < n:
                line = lines[i]
                i += 1
                if "-->" in line:
                    break
            continue
        if i < n and lines[i].lstrip().startswith(">"):
            while i < n and (lines[i].lstrip().startswith(">") or not lines[i].strip()):
                i += 1
            continue
        if i == start:
            break
        # Only blank lines were consumed; insert before them rather than drift.
        if i >= n or (i < n and not lines[i].lstrip().startswith(("<!--", ">"))):
            i = start
            break
    return i


def _tex_insertion_index(lines: list[str]) -> int:
    i = 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        if not stripped or stripped.startswith("%"):
            i += 1
            continue
        break
    return i


def apply_marker(text: str, relpath: str, tier_key: str, suffix: str) -> str:
    clean = remove_existing_marker(text, suffix)
    lines = clean.splitlines(keepends=True)
    index = _markdown_insertion_index(lines) if suffix == ".md" else _tex_insertion_index(lines)
    marker = expected_marker(relpath, tier_key, suffix) + "\n\n"
    lines.insert(index, marker)
    return "".join(lines)


def iter_sources(root: Path, config: dict) -> Iterable[tuple[Path, str, str]]:
    for path in sorted(root.rglob("*")):
        rel_parts = path.relative_to(root).parts
        if any(part in INTERNAL_SKIP_DIRS for part in rel_parts):
            continue
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        rel = path.relative_to(root).as_posix()
        tier = classify_path(rel, config)
        if tier is None or tier == "D_historical":
            yield path, rel, tier or "excluded"
        else:
            yield path, rel, tier


def inventory_counts(root: Path, config: dict) -> dict[str, int]:
    """Count the canonical source inventory independently of filesystem case.

    Git permits tracked paths that differ only by case, while the default
    macOS filesystem collapses them.  Count the union of Git-index paths and
    visible filesystem paths so the report is identical on macOS and Linux
    and still includes newly created, not-yet-tracked sources.
    """
    relative_paths: set[str] = set()
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            check=True,
            capture_output=True,
        )
        for raw in result.stdout.split(b"\0"):
            if raw:
                relative_paths.add(raw.decode("utf-8"))
    except (FileNotFoundError, subprocess.CalledProcessError, UnicodeDecodeError):
        pass

    relative_paths.update(rel for _path, rel, _tier in iter_sources(root, config))
    counts = {
        "A_attested": 0,
        "B_machine_verified": 0,
        "C_working": 0,
        "D_historical": 0,
        "excluded": 0,
    }
    for rel in sorted(relative_paths):
        path = Path(rel)
        if any(part in INTERNAL_SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        tier = classify_path(rel, config)
        counts[tier or "excluded"] += 1
    return counts


def check_one(path: Path, rel: str, tier: str) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    if tier in {"excluded", "D_historical"}:
        if BEGIN in text or END in text:
            return False, f"{rel}: excluded/historical file carries a provenance marker"
        return True, ""
    expected = apply_marker(text, rel, tier, path.suffix.lower())
    if expected != text:
        return False, f"{rel}: marker missing, stale, duplicated, or assigned to the wrong tier"
    return True, ""


def run(root: Path, map_path: Path, apply: bool, report: bool) -> int:
    config = load_map(map_path)
    counts = inventory_counts(root, config)
    changed = 0
    errors: list[str] = []
    for path, rel, tier in iter_sources(root, config):
        if tier in {"excluded", "D_historical"}:
            ok, message = check_one(path, rel, tier)
            if not ok:
                errors.append(message)
            continue
        text = path.read_text(encoding="utf-8")
        desired = apply_marker(text, rel, tier, path.suffix.lower())
        if desired != text:
            if apply:
                path.write_text(desired, encoding="utf-8")
                changed += 1
            else:
                errors.append(f"{rel}: marker missing, stale, duplicated, or assigned to the wrong tier")

    if report or apply:
        print(
            "Provenance source inventory: "
            + ", ".join(f"{key}={counts.get(key, 0)}" for key in
                        ("A_attested", "B_machine_verified", "C_working", "D_historical", "excluded"))
        )
    if apply:
        print(f"Updated {changed} source file(s).")
    if errors:
        for message in errors[:100]:
            print(f"ERROR: {message}", file=sys.stderr)
        if len(errors) > 100:
            print(f"ERROR: {len(errors) - 100} additional mismatch(es) omitted", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--apply", action="store_true", help="write the expected markers")
    mode.add_argument("--check", action="store_true", help="verify without modifying files")
    mode.add_argument("--report", action="store_true", help="print tier inventory only")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--map", dest="map_path", type=Path, default=DEFAULT_MAP)
    args = parser.parse_args(argv)
    try:
        return run(args.root.resolve(), args.map_path.resolve(), args.apply, args.report)
    except (OSError, UnicodeError, ProvenanceError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
