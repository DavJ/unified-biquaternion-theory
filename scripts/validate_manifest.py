#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Manifest validation helpers with repository-relative path resolution."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from repo_utils import find_repo_root


def compute_sha256(file_path: str | Path) -> str:
    """Return the SHA-256 digest of *file_path*."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _default_base_dir(manifest_path: Path) -> Path:
    """Resolve repo-relative manifest paths independently of the process CWD."""
    try:
        return find_repo_root(manifest_path.parent)
    except FileNotFoundError:
        return manifest_path.parent.resolve()


def _load_manifest(manifest_path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def validate_manifest(manifest_path: str | Path, base_dir: str | Path | None = None) -> bool:
    """Validate all non-empty manifest entries.

    Relative paths are interpreted from an explicit ``base_dir`` when supplied;
    otherwise the repository root is discovered from the manifest location.  An
    empty or malformed file list fails closed rather than passing vacuously.
    """
    manifest_path = Path(manifest_path).resolve()
    if not manifest_path.is_file():
        return False

    manifest = _load_manifest(manifest_path)
    if manifest is None:
        return False

    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        return False

    base = Path(base_dir).resolve() if base_dir is not None else _default_base_dir(manifest_path)

    for file_info in files:
        if not isinstance(file_info, dict):
            return False

        stored_path = file_info.get("path")
        if not isinstance(stored_path, str) or not stored_path.strip():
            return False

        raw_path = Path(stored_path)
        resolved = raw_path if raw_path.is_absolute() else base / raw_path
        if not resolved.is_file():
            return False

        expected_size = file_info.get("size_bytes", file_info.get("size"))
        if expected_size is not None:
            if not isinstance(expected_size, int) or resolved.stat().st_size != expected_size:
                return False

        expected_hash = file_info.get("sha256")
        if not isinstance(expected_hash, str) or not expected_hash:
            return False
        if compute_sha256(resolved) != expected_hash:
            return False

    return True


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate a manifest JSON.")
    parser.add_argument("manifest_path")
    parser.add_argument("--base-dir", default=None)
    args = parser.parse_args()
    ok = validate_manifest(args.manifest_path, base_dir=args.base_dir)
    return 0 if ok else 1


def _main() -> int:
    return int(main())


if __name__ == "__main__":
    raise SystemExit(_main())
