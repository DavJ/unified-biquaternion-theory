# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
test_repo_sanity.py
===================
Pytest regression guards that wrap tools/verify_repo_sanity.py.

These tests fail if:
  - "psychon", "Consciousness coupling", or "consciousness substrate" reappear
    in any core/canonical geometry .tex file, OR
  - \\mathcal{G}_{\\mu\\nu} is re-introduced as the LHS of the biquaternionic
    field equation (symbol collision between metric and Einstein tensor).
"""

import sys
from pathlib import Path

import pytest

# Ensure the repo root is on the path so we can import the tools package.
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.verify_repo_sanity import check_forbidden_terms, check_symbol_collision


class TestConsciousnessTermsAbsent:
    """Guard: no consciousness/psychon terminology in core geometry files."""

    def test_no_psychon_in_core_geometry(self):
        """
        'psychon', 'Consciousness coupling', 'consciousness substrate' must not
        appear in canonical/THEORY geometry .tex files.
        """
        violations = check_forbidden_terms(verbose=False)
        assert not violations, (
            "Forbidden consciousness/psychon terms found in core geometry files:\n"
            + "\n".join(f"  {v}" for v in violations)
            + "\n\nThese terms belong only under speculative_extensions/. "
            "See tasks C1/C2 in the audit plan."
        )


class TestSymbolCollisionAbsent:
    """Guard: 𝒢_μν must not be used as the Einstein-tensor field-equation LHS."""

    def test_no_metric_symbol_as_einstein_tensor_lhs(self):
        """
        \\mathcal{G}_{\\mu\\nu} must denote only the biquaternionic *metric*.
        It must not appear as the LHS of the biquaternionic field equation;
        that role belongs to \\mathcal{E}_{\\mu\\nu}.
        """
        violations = check_symbol_collision(verbose=False)
        assert not violations, (
            "Symbol collision detected in core geometry files — "
            r"\\mathcal{G}_{\mu\nu} used as Einstein-tensor LHS:"
            + "\n"
            + "\n".join(f"  {v}" for v in violations)
            + "\n\nFix: use \\mathcal{E}_{\\mu\\nu} for the biquaternionic Einstein tensor. "
            "See task S1 in the audit plan."
        )
