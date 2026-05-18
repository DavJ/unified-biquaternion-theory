# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Chirality algebra scaffold for future weak-sector derivation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np

from tools.dirac_from_biquaternion import biq_gamma_matrices


CHIRALITY_SCAFFOLD_LABEL = "chirality algebra scaffold for future weak-sector derivation."


def pauli_matrices() -> dict[str, np.ndarray]:
    """Return the standard Pauli matrices and identity."""
    return {
        "x": np.array([[0, 1], [1, 0]], dtype=complex),
        "y": np.array([[0, -1j], [1j, 0]], dtype=complex),
        "z": np.array([[1, 0], [0, -1]], dtype=complex),
        "0": np.eye(2, dtype=complex),
    }


def gamma5(representation: str = "dirac") -> np.ndarray:
    """Compute γ5 = iγ0γ1γ2γ3 for the selected representation."""
    gamma = biq_gamma_matrices(representation)
    return 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]


def chirality_projectors(representation: str = "dirac") -> tuple[np.ndarray, np.ndarray]:
    """Return chiral projectors P_L=(1-γ5)/2 and P_R=(1+γ5)/2."""
    g5 = gamma5(representation)
    identity = np.eye(g5.shape[0], dtype=complex)
    p_left = 0.5 * (identity - g5)
    p_right = 0.5 * (identity + g5)
    return p_left, p_right


def parity_operator(representation: str = "dirac") -> np.ndarray:
    """Return a standard spinor parity operator P=γ0 in the selected basis."""
    gamma = biq_gamma_matrices(representation)
    return gamma[0]


def apply_parity(spinor: np.ndarray, representation: str = "dirac") -> np.ndarray:
    """Apply parity transformation to a spinor with the scaffold operator P."""
    p_op = parity_operator(representation)
    vec = np.asarray(spinor, dtype=complex)
    if vec.shape != (4,):
        raise ValueError("spinor must be shape (4,)")
    return p_op @ vec


def parity_conjugation_of_gamma(
    gamma_index: int,
    representation: str = "dirac",
) -> np.ndarray:
    """Return P^{-1}γ^μP for testing standard parity behavior."""
    if gamma_index not in (0, 1, 2, 3):
        raise ValueError("gamma_index must be 0..3")
    gamma = biq_gamma_matrices(representation)
    p_op = parity_operator(representation)
    p_inv = np.linalg.inv(p_op)
    return p_inv @ gamma[gamma_index] @ p_op


class CPTTransform(Protocol):
    """Placeholder interface for a future CPT derivation from UBT."""

    def transform(self, spinor: np.ndarray) -> np.ndarray:
        """Apply CPT transformation once derivation is available."""


@dataclass(frozen=True)
class CPTPlaceholder:
    """Explicit placeholder; CPT theorem proof from UBT remains open."""

    status: str = "OPEN_GAP"
    required_derivation: str = "Derive CPT theorem from UBT action and symmetry structure."

    def transform(self, spinor: np.ndarray) -> np.ndarray:
        raise NotImplementedError(
            "CPT transform is OPEN_GAP in UBT scaffold; derivation not implemented."
        )
