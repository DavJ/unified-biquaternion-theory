# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path

# Add ubt_with_chronofactor directory to sys.path so that
# `alpha_core_repro` package can be imported correctly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
