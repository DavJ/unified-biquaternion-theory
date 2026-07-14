# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Planck spectrum loader without ARCHIVE dependency."""

from __future__ import annotations

from pathlib import Path

import numpy as np


def _load_planck_minimum_format(filepath: str | Path):
    return _load_planck_text(filepath, _skip_size_validation=True)


def _load_planck_text(
    filepath: str | Path,
    spectrum_type: str = "TT",
    _skip_size_validation: bool = False,
    convert_to_cl: bool = True,
):
    path = Path(filepath)
    text = path.read_text(encoding="utf-8", errors="replace")
    if "-log(like)" in text.lower():
        raise ValueError("Input appears to be a likelihood table, not a CMB spectrum.")

    rows = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = stripped.split()
        try:
            nums = [float(x) for x in parts[:4]]
        except ValueError:
            continue
        if len(nums) < 2:
            continue
        ell = nums[0]
        dl = nums[1]
        sigma = abs(nums[2]) if len(nums) > 2 else 0.0
        if len(nums) > 3:
            sigma = 0.5 * (abs(nums[2]) + abs(nums[3]))
        rows.append((ell, dl, sigma))

    if not _skip_size_validation and len(rows) < 50:
        raise ValueError(f"Expected at least 50 data rows for a spectrum, got {len(rows)}.")

    arr = np.asarray(rows, dtype=float)
    if arr.size == 0:
        raise ValueError("No numeric spectrum rows found.")

    ell = arr[:, 0]
    dl = arr[:, 1]
    sigma = arr[:, 2]
    if convert_to_cl:
        with np.errstate(divide="ignore", invalid="ignore"):
            cl = np.where(ell > 0, dl / (ell * (ell + 1) / (2.0 * np.pi)), dl)
        units = "Cl"
    else:
        cl = dl
        units = "Dl"
    return ell, cl, sigma, units


__all__ = ["_load_planck_text", "_load_planck_minimum_format"]
