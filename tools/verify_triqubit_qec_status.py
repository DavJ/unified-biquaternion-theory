#!/usr/bin/env python3
"""Exact numerical verifier for the triqubit leakage/QEC status theorem.

The verifier treats the one-hot color carrier as a 3-dimensional code subspace
of three qubits and checks:
  * P X_i P = P Y_i P = 0 (leakage detection),
  * P Z_i P is non-scalar (phase error not detected),
  * Knill--Laflamme fails for {I, X_1, X_2, X_3}.

A PASS means the stated positive and no-go results are both reproduced.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass

import numpy as np


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def on_qubit(op: np.ndarray, index: int) -> np.ndarray:
    """Return ``op`` acting on qubit ``index`` in |q1 q2 q3> ordering."""
    factors = [I2, I2, I2]
    factors[index] = op
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return result


def embedding() -> np.ndarray:
    """8x3 isometry mapping (r,g,b) to |100>, |010>, |001>."""
    p = np.zeros((8, 3), dtype=complex)
    p[4, 0] = 1
    p[2, 1] = 1
    p[1, 2] = 1
    return p


def scalar_residual(matrix: np.ndarray) -> float:
    """Distance from the nearest scalar multiple of the identity."""
    dim = matrix.shape[0]
    scalar = np.trace(matrix) / dim
    return float(np.linalg.norm(matrix - scalar * np.eye(dim), ord="fro"))


@dataclass(frozen=True)
class Verification:
    x_detection_max: float
    y_detection_max: float
    z_nonscalar_min: float
    kl_violation_max: float
    kl_witness: tuple[str, str]
    code_dimension: int


def verification() -> Verification:
    p = embedding()
    pd = p.conj().T
    xs = [on_qubit(X, i) for i in range(3)]
    ys = [on_qubit(Y, i) for i in range(3)]
    zs = [on_qubit(Z, i) for i in range(3)]

    x_detection_max = max(np.linalg.norm(pd @ op @ p) for op in xs)
    y_detection_max = max(np.linalg.norm(pd @ op @ p) for op in ys)
    z_nonscalar_min = min(scalar_residual(pd @ op @ p) for op in zs)

    errors = [("I", np.eye(8, dtype=complex))] + [
        (f"X{i + 1}", op) for i, op in enumerate(xs)
    ]
    violations: list[tuple[float, tuple[str, str]]] = []
    for (name_a, error_a), (name_b, error_b) in itertools.product(errors, repeat=2):
        compressed = pd @ error_a.conj().T @ error_b @ p
        violations.append((scalar_residual(compressed), (name_a, name_b)))
    kl_violation_max, kl_witness = max(violations, key=lambda item: item[0])

    return Verification(
        x_detection_max=float(x_detection_max),
        y_detection_max=float(y_detection_max),
        z_nonscalar_min=float(z_nonscalar_min),
        kl_violation_max=float(kl_violation_max),
        kl_witness=kl_witness,
        code_dimension=int(round(np.trace(p @ pd).real)),
    )


def main() -> int:
    tol = 1e-12
    result = verification()
    checks = [
        ("all P X_i P vanish", result.x_detection_max < tol, result.x_detection_max),
        ("all P Y_i P vanish", result.y_detection_max < tol, result.y_detection_max),
        ("all compressed Z_i are non-scalar", result.z_nonscalar_min > tol, result.z_nonscalar_min),
        ("Knill-Laflamme has a non-scalar cross term", result.kl_violation_max > tol, result.kl_violation_max),
        ("code-space dimension is three", result.code_dimension == 3, float(result.code_dimension)),
    ]

    print("Triqubit leakage/QEC status verifier")
    print("=" * 43)
    for label, passed, value in checks:
        print(f"{'PASS' if passed else 'FAIL':4s}  {label:48s} {value:.6g}")
    print(f"KL witness: {result.kl_witness[0]}^dagger {result.kl_witness[1]}")
    print("Verdict: leakage detector for X/Y; not a single-X correcting code; Z is logical.")
    return 0 if all(passed for _, passed, _ in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
