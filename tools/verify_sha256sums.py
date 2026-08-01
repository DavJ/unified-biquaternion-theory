#!/usr/bin/env python3
"""Verify a GNU-style SHA-256 manifest without platform-specific utilities."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "SHA256SUMS.txt"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _entries(manifest: Path) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for lineno, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            raise ValueError(f"Malformed line {lineno} in {manifest}: {raw!r}")
        expected, relative = parts
        if len(expected) != 64 or any(ch not in "0123456789abcdefABCDEF" for ch in expected):
            raise ValueError(f"Invalid SHA-256 digest on line {lineno}: {expected!r}")
        entries.append((expected.lower(), relative.lstrip("*")))
    return entries


def verify(manifest: Path, *, quiet: bool = False) -> int:
    base = ROOT
    failures: list[str] = []
    entries = _entries(manifest)
    seen: set[str] = set()
    for expected, relative in entries:
        if relative in seen:
            failures.append(f"duplicate: {relative}")
            continue
        seen.add(relative)
        path = base / relative
        if not path.is_file():
            failures.append(f"missing: {relative}")
            if not quiet:
                print(f"{relative}: FAILED (missing)")
            continue
        actual = _sha256(path)
        if actual != expected:
            failures.append(f"mismatch: {relative}")
            if not quiet:
                print(f"{relative}: FAILED")
            continue
        if not quiet:
            print(f"{relative}: OK")

    if failures:
        print(
            f"SHA-256 verification failed for {len(failures)} of {len(entries)} entries:",
            file=sys.stderr,
        )
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1
    if quiet:
        print(f"SHA-256 verification passed: {len(entries)} entries")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Manifest to verify; paths remain repository-relative",
    )
    parser.add_argument("--quiet", action="store_true", help="Print only the summary")
    args = parser.parse_args()
    manifest = args.file.resolve()
    if not manifest.is_file():
        parser.error(f"manifest not found: {manifest}")
    raise SystemExit(verify(manifest, quiet=args.quiet))


if __name__ == "__main__":
    main()
