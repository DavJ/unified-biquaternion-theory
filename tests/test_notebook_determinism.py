"""Regression test: repeated stabilization of the same notebook must be idempotent.

This guards against non-deterministic cell ID generation (e.g. random UUIDs
injected by jupytext on each conversion), which previously produced spurious
[skip ci] commits that changed only cell IDs without changing scientific content.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Add tools/ to path so we can import the stabilizer directly.
sys.path.insert(0, str(ROOT / "tools"))
from stabilize_notebook_ids import stabilize  # noqa: E402


SAMPLE_NOTEBOOKS = [
    ROOT / "docs/notebooks/verify/verify_8pi_connection.ipynb",
    ROOT / "docs/notebooks/verify/verify_su3_superposition.ipynb",
    ROOT / "docs/notebooks/experiments/derive_fine_structure.ipynb",
    ROOT / "docs/notebooks/research_tracks/e01_incidence_sanity.ipynb",
]


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_stabilize_is_idempotent() -> None:
    """Running stabilize_notebook_ids twice must produce the same notebook.

    Uses check=True so tracked notebooks are never modified, even on failure.
    """
    for nb_path in SAMPLE_NOTEBOOKS:
        if not nb_path.is_file():
            continue
        # check=True: read-only — reports whether a write would be needed
        # without touching the file.
        would_change = stabilize(nb_path, check=True)
        assert not would_change, (
            f"{nb_path.name}: stabilize would change IDs — "
            "build is non-deterministic; check tools/stabilize_notebook_ids.py"
        )


def test_cell_ids_are_deterministic_across_runs() -> None:
    """Simulating two conversions of the same source must yield identical IDs."""
    for nb_path in SAMPLE_NOTEBOOKS:
        if not nb_path.is_file():
            continue

        original = _load(nb_path)
        # Simulate a fresh jupytext run that forgot IDs by stripping them.
        nb_stripped = copy.deepcopy(original)
        for cell in nb_stripped.get("cells", []):
            cell.pop("id", None)

        # Write stripped notebook to a temp file and stabilize it.
        import tempfile, os

        with tempfile.NamedTemporaryFile(
            suffix=".ipynb", delete=False, dir=ROOT / "docs/notebooks"
        ) as tmp:
            tmp_path = Path(tmp.name)
        try:
            tmp_path.write_text(json.dumps(nb_stripped, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            stabilize(tmp_path)
            result1 = _load(tmp_path)

            # Strip again and re-stabilize — must give same IDs.
            for cell in nb_stripped.get("cells", []):
                cell.pop("id", None)
            tmp_path.write_text(json.dumps(nb_stripped, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            stabilize(tmp_path)
            result2 = _load(tmp_path)

            ids1 = [c.get("id") for c in result1.get("cells", [])]
            ids2 = [c.get("id") for c in result2.get("cells", [])]
            assert ids1 == ids2, (
                f"{nb_path.name}: cell IDs differ between runs — stabilizer is not deterministic"
            )
        finally:
            os.unlink(tmp_path)
