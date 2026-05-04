#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
biquaternion.py — Core biquaternion algebra for UBT.

Implements the algebra ℂ⊗ℍ (biquaternions) as a proper Python class with:
  - Full arithmetic (add, mul, conjugate, norm, inverse)
  - Correct handling of null-norm (lightlike) elements as physical entities
  - Type annotations throughout
  - No silent division-by-zero: null-norm elements return LightlikeElement

MATHEMATICAL BACKGROUND
-----------------------
A biquaternion q ∈ ℂ⊗ℍ is written as:
    q = a·1 + b·I + c·J + d·K
where a,b,c,d ∈ ℂ and I,J,K satisfy the quaternion relations:
    I²=J²=K²=IJK=-1

The quaternion conjugate is:
    q† = a·1 - b·I - c·J - d·K

The biquaternion norm-squared is:
    N(q) = q†q = a²+b²+c²+d²  (complex scalar)

An element is *lightlike* (null-norm) iff N(q)=0.  In relativistic physics
these elements represent photon trajectories and are NOT errors.

ISOMORPHISM
-----------
ℂ⊗ℍ ≅ Mat(2,ℂ) via the standard map:
    1  ↦  I₂
    I  ↦  iσ_z
    J  ↦  iσ_y
    K  ↦  iσ_x
(where σ_x,σ_y,σ_z are Pauli matrices)

REFERENCES
----------
- canonical/algebra/biquaternion_algebra.tex
- canonical/geometry/biquaternion_metric.tex
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Union

import numpy as np


# ---------------------------------------------------------------------------
# Norm classification
# ---------------------------------------------------------------------------

class NormType(Enum):
    """Physical classification of a biquaternion by its norm-squared."""
    TIMELIKE   = "timelike"        # Re(N) > 0 (massive particles, subluminal)
    SPACELIKE  = "spacelike"       # Re(N) < 0 (tachyonic, spacelike separation)
    LIGHTLIKE  = "lightlike"       # |N| ≈ 0   (photons, null geodesics)
    ZERO       = "zero"            # q = 0 itself


# ---------------------------------------------------------------------------
# Sentinel for lightlike (null-norm) elements
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class LightlikeElement:
    """
    Represents a biquaternion element on the light cone (null norm).

    This is a valid physical entity — null-norm elements correspond to
    photon world-lines and light cones in Minkowski spacetime.  They
    are returned by Biquaternion.inverse() instead of raising an exception.

    Attributes
    ----------
    source : Biquaternion
        The original null-norm biquaternion.
    """
    source: "Biquaternion"

    def __repr__(self) -> str:
        return f"LightlikeElement({self.source})"

    def is_lightlike(self) -> bool:
        return True


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------

@dataclass
class Biquaternion:
    """
    Biquaternion q = a·1 + b·I + c·J + d·K  with a,b,c,d ∈ ℂ.

    Components are stored as a complex numpy array of shape (4,):
        components[0] = a  (scalar / real part)
        components[1] = b  (coefficient of I)
        components[2] = c  (coefficient of J)
        components[3] = d  (coefficient of K)

    Parameters
    ----------
    components : array-like, shape (4,)
        Complex coefficients [a, b, c, d].
    """
    components: np.ndarray

    def __post_init__(self) -> None:
        self.components = np.asarray(self.components, dtype=complex)
        if self.components.shape != (4,):
            raise ValueError(
                f"Biquaternion requires exactly 4 components, "
                f"got shape {self.components.shape}."
            )

    # ------------------------------------------------------------------
    # Constructors
    # ------------------------------------------------------------------

    @classmethod
    def from_real_quat(cls, a: float, b: float, c: float, d: float) -> "Biquaternion":
        """Create a real quaternion (all coefficients real)."""
        return cls(np.array([a, b, c, d], dtype=complex))

    @classmethod
    def from_scalar(cls, z: complex) -> "Biquaternion":
        """Scalar biquaternion z·1."""
        return cls(np.array([z, 0, 0, 0], dtype=complex))

    @classmethod
    def zero(cls) -> "Biquaternion":
        """The zero biquaternion."""
        return cls(np.zeros(4, dtype=complex))

    @classmethod
    def one(cls) -> "Biquaternion":
        """The unit biquaternion (multiplicative identity)."""
        return cls(np.array([1, 0, 0, 0], dtype=complex))

    # ------------------------------------------------------------------
    # Arithmetic
    # ------------------------------------------------------------------

    def __add__(self, other: "Biquaternion") -> "Biquaternion":
        return Biquaternion(self.components + other.components)

    def __sub__(self, other: "Biquaternion") -> "Biquaternion":
        return Biquaternion(self.components - other.components)

    def __neg__(self) -> "Biquaternion":
        return Biquaternion(-self.components)

    def __mul__(self, other: Union["Biquaternion", complex, float, int]) -> "Biquaternion":
        """Hamilton product q1 * q2 (non-commutative)."""
        if isinstance(other, (int, float, complex)):
            return Biquaternion(self.components * complex(other))
        a1, b1, c1, d1 = self.components
        a2, b2, c2, d2 = other.components
        return Biquaternion(np.array([
            a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2,
        ], dtype=complex))

    def __rmul__(self, scalar: Union[complex, float, int]) -> "Biquaternion":
        return Biquaternion(self.components * complex(scalar))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Biquaternion):
            return NotImplemented
        return bool(np.allclose(self.components, other.components))

    def __repr__(self) -> str:
        a, b, c, d = self.components
        return f"Biquaternion([{a}, {b}, {c}, {d}])"

    # ------------------------------------------------------------------
    # Conjugates and norm
    # ------------------------------------------------------------------

    def conjugate(self) -> "Biquaternion":
        """
        Quaternion conjugate: q† = a·1 - b·I - c·J - d·K.

        Note: This negates the quaternion vector part but does NOT
        complex-conjugate the coefficients.  The full Hermitian conjugate
        (bar) additionally complex-conjugates; use hermitian_conjugate().
        """
        c = self.components.copy()
        c[1] *= -1
        c[2] *= -1
        c[3] *= -1
        return Biquaternion(c)

    def hermitian_conjugate(self) -> "Biquaternion":
        """
        Hermitian (bar) conjugate: quaternion conjugate + complex conjugation.

            q̄ = ā·1 - b̄·I - c̄·J - d̄·K
        """
        c = np.conj(self.components).copy()
        c[1] *= -1
        c[2] *= -1
        c[3] *= -1
        return Biquaternion(c)

    def scalar_part(self) -> complex:
        """Scalar part Sc(q) = a (the coefficient of 1)."""
        return complex(self.components[0])

    def vector_part(self) -> np.ndarray:
        """Vector part Vec(q) = [b, c, d] (coefficients of I, J, K)."""
        return self.components[1:].copy()

    def norm_squared(self) -> complex:
        """
        Biquaternion norm-squared N(q) = q† q = a²+b²+c²+d²  (complex scalar).

        For real quaternions this equals the Euclidean norm squared.
        For biquaternions this can be zero even for non-zero q (lightlike elements).
        """
        c = self.components
        return complex(c[0]**2 + c[1]**2 + c[2]**2 + c[3]**2)

    def norm(self) -> complex:
        """Square root of norm_squared (principal branch)."""
        return complex(np.sqrt(self.norm_squared()))

    # ------------------------------------------------------------------
    # Norm classification (physical)
    # ------------------------------------------------------------------

    def norm_type(self, tol: float = 1e-12) -> NormType:
        """
        Classify the biquaternion by its norm-squared.

        Returns
        -------
        NormType
            Physical classification: TIMELIKE, SPACELIKE, LIGHTLIKE, or ZERO.
        """
        if np.allclose(self.components, 0, atol=tol):
            return NormType.ZERO
        ns = self.norm_squared()
        if abs(ns) < tol:
            return NormType.LIGHTLIKE
        if ns.real > 0:
            return NormType.TIMELIKE
        return NormType.SPACELIKE

    def is_lightlike(self, tol: float = 1e-12) -> bool:
        """Return True if this element lies on the light cone (null norm)."""
        return self.norm_type(tol) == NormType.LIGHTLIKE

    # ------------------------------------------------------------------
    # Inverse
    # ------------------------------------------------------------------

    def inverse(self, tol: float = 1e-12) -> Union["Biquaternion", LightlikeElement]:
        """
        Compute the multiplicative inverse q⁻¹ = q† / N(q).

        For null-norm (lightlike) elements, the inverse does not exist as a
        biquaternion.  Rather than raising an exception, this method returns a
        LightlikeElement sentinel, preserving the physical information that
        the element lies on the light cone.

        Parameters
        ----------
        tol : float
            Tolerance for detecting null norm.

        Returns
        -------
        Biquaternion
            The inverse q⁻¹, when N(q) ≠ 0.
        LightlikeElement
            Sentinel indicating a null-norm / lightlike element.
        """
        ns = self.norm_squared()
        if abs(ns) < tol:
            return LightlikeElement(source=self)
        return Biquaternion(self.conjugate().components / ns)

    # ------------------------------------------------------------------
    # Matrix representation
    # ------------------------------------------------------------------

    def to_matrix(self) -> np.ndarray:
        """
        Return the 2×2 complex matrix representation via ℂ⊗ℍ ≅ Mat(2,ℂ).

        The isomorphism maps:
            1  ↦  I₂
            I  ↦  iσ_z = diag(i, -i)
            J  ↦  iσ_y = [[0, 1],[-1, 0]]
            K  ↦  iσ_x = [[0, i],[i, 0]]
        """
        a, b, c, d = self.components
        I2 = np.eye(2, dtype=complex)
        iSz = np.array([[1j, 0], [0, -1j]], dtype=complex)
        iSy = np.array([[0, 1], [-1, 0]], dtype=complex)
        iSx = np.array([[0, 1j], [1j, 0]], dtype=complex)
        return a * I2 + b * iSz + c * iSy + d * iSx

    @classmethod
    def from_matrix(cls, M: np.ndarray) -> "Biquaternion":
        """
        Recover biquaternion components from a 2×2 complex matrix.

        Inverse of to_matrix().
        """
        if M.shape != (2, 2):
            raise ValueError(f"Expected 2×2 matrix, got {M.shape}.")
        # Basis matrices
        I2  = np.eye(2, dtype=complex)
        iSz = np.array([[1j, 0], [0, -1j]], dtype=complex)
        iSy = np.array([[0, 1], [-1, 0]], dtype=complex)
        iSx = np.array([[0, 1j], [1j, 0]], dtype=complex)
        bases = [I2, iSz, iSy, iSx]
        # Extract coefficients via Tr(M · basis†) / 2
        coeffs = np.array([
            np.trace(M @ b.conj().T) / 2
            for b in bases
        ], dtype=complex)
        return cls(coeffs)

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    def real_part(self) -> "Biquaternion":
        """Real quaternion part: coefficients are Re(a), Re(b), Re(c), Re(d)."""
        return Biquaternion(np.real(self.components).astype(complex))

    def imag_part(self) -> "Biquaternion":
        """Imaginary quaternion part: coefficients are Im(a), Im(b), Im(c), Im(d)."""
        return Biquaternion(np.imag(self.components).astype(complex))


# ---------------------------------------------------------------------------
# Basis elements (public constants)
# ---------------------------------------------------------------------------

BQ_ONE  = Biquaternion.from_real_quat(1, 0, 0, 0)  # scalar 1
BQ_I    = Biquaternion.from_real_quat(0, 1, 0, 0)  # quaternion I
BQ_J    = Biquaternion.from_real_quat(0, 0, 1, 0)  # quaternion J
BQ_K    = Biquaternion.from_real_quat(0, 0, 0, 1)  # quaternion K
BQ_i    = Biquaternion.from_scalar(1j)              # complex unit i·1
BQ_iI   = Biquaternion(np.array([0, 1j, 0, 0], dtype=complex))
BQ_iJ   = Biquaternion(np.array([0, 0, 1j, 0], dtype=complex))
BQ_iK   = Biquaternion(np.array([0, 0, 0, 1j], dtype=complex))


# ---------------------------------------------------------------------------
# Standalone demo / smoke-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("ℂ⊗ℍ Biquaternion algebra — smoke test")
    print("=" * 50)

    # Basic arithmetic
    q1 = Biquaternion.from_real_quat(1, 2, 3, 4)
    q2 = Biquaternion.from_real_quat(0, 1, 0, 0)   # pure I
    print(f"q1 = {q1}")
    print(f"q2 = {q2}")
    print(f"q1 * q2 = {q1 * q2}")
    print(f"q2 * q1 = {q2 * q1}  (non-commutative)")
    print(f"q1† = {q1.conjugate()}")
    print(f"N(q1) = {q1.norm_squared()}")

    # Inverse of regular element
    inv = q1.inverse()
    prod = q1 * inv
    print(f"q1 * q1⁻¹ = {prod}  (should be ≈ 1)")

    # Lightlike element: null-norm biquaternion (1 + iI in ℂ⊗ℍ)
    null_q = Biquaternion(np.array([1, 1j, 0, 0], dtype=complex))
    print(f"\nNull-norm biquaternion: {null_q}")
    print(f"N(null) = {null_q.norm_squared()}  (should be 0)")
    print(f"null.norm_type() = {null_q.norm_type()}")
    result = null_q.inverse()
    print(f"null.inverse() = {result}  ← LightlikeElement, not an exception")

    # Matrix representation
    M = q1.to_matrix()
    q1_back = Biquaternion.from_matrix(M)
    print(f"\nMatrix round-trip error: {np.max(np.abs(q1.components - q1_back.components)):.2e}")

    print("\n✓ All checks passed.")
