#!/usr/bin/env python3
"""Assign deterministic cell IDs to a Jupyter notebook.

IDs are derived from the notebook's repository-relative path, the cell index,
and a stable hash of the cell source.  Existing IDs that already match the
deterministic scheme are preserved unchanged.  Random or stale IDs are
replaced so that repeated builds of the same source produce a byte-identical
notebook, eliminating meaningless churn commits.

Usage:
    python tools/stabilize_notebook_ids.py path/to/notebook.ipynb [...]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _deterministic_id(rel_path: str, cell_index: int, source: str) -> str:
    """Return an 8-character hex ID that is stable for a given (path, index, source)."""
    payload = f"{rel_path}:{cell_index}:{source}".encode()
    return hashlib.sha1(payload).hexdigest()[:8]


def stabilize(nb_path: Path) -> bool:
    """Rewrite *nb_path* with deterministic cell IDs.

    Returns True if the file was modified, False if it was already stable.
    """
    rel_path = str(nb_path.relative_to(ROOT))
    text = nb_path.read_text(encoding="utf-8")
    nb = json.loads(text)

    changed = False
    for idx, cell in enumerate(nb.get("cells", [])):
        source = "".join(cell.get("source", []))
        expected = _deterministic_id(rel_path, idx, source)
        if cell.get("id") != expected:
            cell["id"] = expected
            changed = True

    if changed:
        nb_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebooks", nargs="+", type=Path, help="Notebook file(s) to stabilize")
    args = parser.parse_args()

    any_changed = False
    for path in args.notebooks:
        path = path.resolve()
        if not path.is_file():
            print(f"WARNING: {path} does not exist, skipping", file=sys.stderr)
            continue
        if stabilize(path):
            print(f"Stabilized IDs: {path}")
            any_changed = True
        else:
            print(f"Already stable: {path}")

    if not any_changed:
        print("All notebooks already have deterministic IDs.")


if __name__ == "__main__":
    main()
