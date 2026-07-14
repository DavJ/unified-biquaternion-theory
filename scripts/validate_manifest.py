#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Manifest validation helpers."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def compute_sha256(file_path: str | Path) -> str:
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def validate_manifest(manifest_path: str | Path, base_dir: str | Path | None = None) -> bool:
    manifest_path = Path(manifest_path)
    base = Path(base_dir).resolve() if base_dir else manifest_path.parent.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for file_info in manifest.get("files", []):
        raw_path = Path(file_info["path"])
        resolved = raw_path if raw_path.is_absolute() else (base / raw_path)
        if not resolved.exists():
            return False
        expected = file_info.get("sha256")
        if expected and compute_sha256(resolved) != expected:
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
