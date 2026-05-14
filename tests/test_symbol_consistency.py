# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
test_symbol_consistency.py
==========================
Pytest regression guards wrapping tools/verify_symbol_consistency.py.

These tests fail if:
  SC2/SC3 — \\mathcal{G}_{\\mu\\nu} is used as the left-hand side of the
             biquaternionic field equation in any scanned .tex or .md file.
             The correct symbol for the biquaternionic Einstein tensor is
             \\mathcal{E}_{\\mu\\nu}.

  SC4     — In canonical/papers/research_tracks .tex files, plain
             G_{\\mu\\nu} = \\kappa appears in a context suggesting the
             biquaternionic field equation (rather than the classical GR
             limit).
"""

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.verify_symbol_consistency import (
    check_metric_symbol_collision,
    check_einstein_tensor_symbol,
)


class TestMetricSymbolNotUsedAsEinsteinLHS:
    """Guard SC2/SC3: \\mathcal{G}_{\\mu\\nu} must not be the field-equation LHS."""

    def test_no_metric_symbol_as_field_equation_lhs(self):
        """
        \\mathcal{G}_{\\mu\\nu} is reserved for the biquaternionic *metric*.
        It must not appear immediately followed by '= \\kappa', '= 8\\pi G',
        or '= \\mathcal{T}' (field-equation left-hand side).
        The biquaternionic Einstein tensor must be written \\mathcal{E}_{\\mu\\nu}.
        """
        violations = check_metric_symbol_collision(verbose=False)
        assert not violations, (
            "Symbol collision SC2/SC3: \\mathcal{G}_{\\mu\\nu} used as "
            "biquaternionic field-equation LHS in:\n"
            + "\n".join(f"  {v}" for v in violations)
            + "\n\nFix: replace with \\mathcal{E}_{\\mu\\nu} for the "
            "biquaternionic Einstein tensor."
        )


class TestEinsteinTensorSymbolInCanonicalFiles:
    """Guard SC4: canonical/papers/research_tracks files use correct symbols."""

    def test_field_equation_uses_calE_not_plain_G(self):
        """
        In canonical, papers, and research_tracks .tex files, the
        biquaternionic field equation must use \\mathcal{E}_{\\mu\\nu},
        not plain G_{\\mu\\nu} = \\kappa.
        """
        violations = check_einstein_tensor_symbol(verbose=False)
        assert not violations, (
            "Symbol inconsistency SC4 in canonical files — "
            "plain G_{\\mu\\nu} = \\kappa found where "
            "\\mathcal{E}_{\\mu\\nu} is required:\n"
            + "\n".join(f"  {v}" for v in violations)
            + "\n\nFix: use \\mathcal{E}_{\\mu\\nu} = \\kappa\\mathcal{T}_{\\mu\\nu} "
            "for the biquaternionic field equation."
        )
