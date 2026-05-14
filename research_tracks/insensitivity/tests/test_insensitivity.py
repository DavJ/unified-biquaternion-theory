# insensitivity/tests/test_insensitivity.py
from __future__ import annotations
import csv, math, os
from insensitivity.sweep import run_sweep

def test_ubt_insensitivity_flatness():
    path = run_sweep()
    with open(path, "r", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    # Expect near-constancy of rydberg_rel under co-scaling (within ~1e-3)
    vals = [float(r["rydberg_rel"]) for r in rows]
    assert max(vals) - min(vals) < 1e-3
