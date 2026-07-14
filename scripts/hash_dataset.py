#!/usr/bin/env python3
# hash_dataset.py
# SPDX-License-Identifier: MIT
"""Root-level hash_dataset implementation without ARCHIVE dependency."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent


def compute_sha256(file_path: str | Path) -> str:
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _resolve_stored_path(path: Path, relative_to: Path | None) -> str:
    if relative_to is not None:
        try:
            return str(path.relative_to(relative_to))
        except ValueError:
            return str(path)
    try:
        repo_root = Path.cwd()
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def hash_dataset(paths: list[str], relative_to: str | Path | None = None) -> dict:
    rel_base = Path(relative_to).resolve() if relative_to else None
    files = []
    for item in paths:
        p = Path(item).resolve()
        files.append(
            {
                "filename": p.name,
                "path": _resolve_stored_path(p, rel_base),
                "sha256": compute_sha256(p),
                "size": p.stat().st_size,
            }
        )
    return {"files": files}


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Hash dataset files.")
    parser.add_argument("paths", nargs="+", help="Files to hash")
    parser.add_argument("--relative-to", default=None, help="Base path for stored relative paths")
    args = parser.parse_args()
    manifest = hash_dataset(args.paths, relative_to=args.relative_to)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


def _main() -> int:
    """Entry point for CLI execution."""
    return int(main())


if __name__ == "__main__":
    raise SystemExit(_main())
