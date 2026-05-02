# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/model.py — Compatibility shim.

Earlier code imported from sportka.model; this module re-exports from
sportka.models so both import paths work.
"""
from sportka.models import (  # noqa: F401
    BasePredictor,
    RandomPredictor,
    GlobalFreqPredictor,
    RollingFreqPredictor,
    ExpDecayFreqPredictor,
    LogisticPredictor,
    MLPPredictor,
    UBTMLPPredictor,
    ALL_PREDICTORS,
)
