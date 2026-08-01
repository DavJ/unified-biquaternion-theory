"""Regression guard for the release-level SHA256SUMS.txt integrity anchor."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SUMS_FILE = ROOT / "SHA256SUMS.txt"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _entries() -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for lineno, raw in enumerate(SUMS_FILE.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        assert len(parts) == 2, f"Malformed SHA256SUMS line {lineno}: {raw!r}"
        expected, relative = parts
        relative = relative.lstrip("*")
        assert SHA256_RE.fullmatch(expected), f"Invalid SHA-256 at line {lineno}"
        path = Path(relative)
        assert not path.is_absolute(), f"Absolute path forbidden at line {lineno}: {relative}"
        assert ".." not in path.parts, f"Parent traversal forbidden at line {lineno}: {relative}"
        entries.append((expected, path.as_posix()))
    return entries


def test_sha256sums_manifest_matches_repository_files():
    entries = _entries()
    assert entries, "SHA256SUMS.txt must not be empty"

    paths = [relative for _, relative in entries]
    assert len(paths) == len(set(paths)), "SHA256SUMS.txt contains duplicate paths"

    mismatches: list[str] = []
    for expected, relative in entries:
        path = ROOT / relative
        if not path.is_file():
            mismatches.append(f"missing: {relative}")
            continue
        actual = _sha256(path)
        if actual != expected:
            mismatches.append(f"mismatch: {relative} expected={expected} actual={actual}")

    assert not mismatches, "SHA256SUMS.txt integrity failures:\n" + "\n".join(mismatches)
