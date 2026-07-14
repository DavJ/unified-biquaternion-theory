#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Repository utility helpers."""

from __future__ import annotations

from pathlib import Path


def find_repo_root(start_path: str | Path | None = None) -> Path:
    current = Path(start_path).resolve() if start_path else Path.cwd().resolve()
    markers = (".git", "pyproject.toml", "pytest.ini")
    while True:
        if any((current / marker).exists() for marker in markers):
            return current
        if current == current.parent:
            raise FileNotFoundError("Could not find repository root from start path")
        current = current.parent


__all__ = ["find_repo_root"]
