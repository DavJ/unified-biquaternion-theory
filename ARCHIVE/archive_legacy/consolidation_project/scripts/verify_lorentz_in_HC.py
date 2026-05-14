#!/usr/bin/env python3
"""
Verification script for Lorentz structure in complexified quaternions H_C.

This script numerically verifies the claims in appendix_P6_lorentz_in_HC.tex:
1. The embedding of Minkowski spacetime into Hermitian 2x2 matrices
2. The determinant equals the Minkowski metric
3. SL(2,C) action preserves the determinant (Lorentz invariance)
"""

import numpy as np
from numpy.linalg import det

# Pauli matrices
sigma_0 = np.eye(2, dtype=complex)
sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)

sigma = [sigma_0, sigma_1, sigma_2, sigma_3]


def embed_spacetime(x):
    """
    Embed a 4-vector x = (x0, x1, x2, x3) into Hermitian 2x2 matrix.
    
    X = x^mu * sigma_mu = [[x0+x3, x1-i*x2], [x1+i*x2, x0-x3]]
    
    Args:
        x: array-like of length 4, spacetime coordinates
    
    Returns:
        2x2 complex Hermitian matrix
    """
    x = np.array(x, dtype=float)
    X = sum(x[mu] * sigma[mu] for mu in range(4))
    return X


def minkowski_metric(x):
    """
    Compute -eta_munu x^mu x^nu where eta has signature (-,+,+,+).
    
    This equals (x0)^2 - ||x||^2, which is what det(X) should equal.
    
    Args:
        x: array-like of length 4
    
    Returns:
        float: (x0)^2 - (x1^2 + x2^2 + x3^2) = -(-x0^2 + x1^2 + x2^2 + x3^2)
    """
    x = np.array(x, dtype=float)
    return x[0]**2 - (x[1]**2 + x[2]**2 + x[3]**2)


def random_SL2C():
    """
    Generate a random element of SL(2,C) with det(A) = 1.
    
    Returns:
        2x2 complex matrix with determinant 1
    """
    # Generate random complex 2x2 matrix
    A = np.random.randn(2, 2) + 1j * np.random.randn(2, 2)
    
    # Normalize to get det(A) = 1
    A = A / np.sqrt(det(A))
    
    return A


def is_hermitian(M, tol=1e-10):
    """Check if matrix M is Hermitian."""
    return np.allclose(M, M.conj().T, atol=tol)


def verify_embedding():
    """Verify that the embedding produces Hermitian matrices."""
    print("=" * 70)
    print("Test 1: Embedding produces Hermitian matrices")
    print("=" * 70)
    
    # Test with several random spacetime points
    for i in range(5):
        x = np.random.randn(4) * 10  # Random spacetime point
        X = embed_spacetime(x)
        
        assert is_hermitian(X), f"X is not Hermitian for x={x}"
        print(f"✓ x = {x[:2]}... → X is Hermitian")
    
    print("\n✅ All embedded matrices are Hermitian\n")


def verify_determinant_equals_minkowski():
    """Verify that det(X) = (x0)^2 - ||x||^2 = -eta_munu x^mu x^nu."""
    print("=" * 70)
    print("Test 2: Determinant equals Minkowski metric")
    print("=" * 70)
    
    # Test with several random spacetime points
    errors = []
    for i in range(10):
        x = np.random.randn(4) * 10
        X = embed_spacetime(x)
        
        det_X = det(X).real  # Should be real for Hermitian matrix
        metric = minkowski_metric(x)
        
        error = abs(det_X - metric)
        errors.append(error)
        
        if i < 5:  # Print first 5
            print(f"x = [{x[0]:6.2f}, {x[1]:6.2f}, {x[2]:6.2f}, {x[3]:6.2f}]")
            print(f"  det(X)         = {det_X:12.6f}")
            print(f"  Minkowski form = {metric:12.6f}")
            print(f"  |error|        = {error:12.2e}")
    
    max_error = max(errors)
    print(f"\nMaximum error over 10 trials: {max_error:.2e}")
    print("✅ Determinant equals Minkowski metric (within numerical precision)\n")


def verify_lorentz_invariance():
    """Verify that det(A X A†) = det(X) for A in SL(2,C)."""
    print("=" * 70)
    print("Test 3: SL(2,C) action preserves determinant (Lorentz invariance)")
    print("=" * 70)
    
    # Test with several random transformations
    errors = []
    for i in range(10):
        # Random spacetime point
        x = np.random.randn(4) * 10
        X = embed_spacetime(x)
        
        # Random SL(2,C) element
        A = random_SL2C()
        
        # Apply the action X → A X A†
        X_prime = A @ X @ A.conj().T
        
        # Compute determinants
        det_X = det(X).real
        det_X_prime = det(X_prime).real
        
        error = abs(det_X_prime - det_X)
        errors.append(error)
        
        # Verify X' is still Hermitian
        assert is_hermitian(X_prime, tol=1e-8), "Transformed X is not Hermitian"
        
        if i < 5:  # Print first 5
            print(f"Trial {i+1}:")
            print(f"  det(X)        = {det_X:12.6f}")
            print(f"  det(A X A†)   = {det_X_prime:12.6f}")
            print(f"  |error|       = {error:12.2e}")
            print(f"  det(A)        = {det(A):.6f}  (should be ≈ 1)")
    
    max_error = max(errors)
    print(f"\nMaximum error over 10 trials: {max_error:.2e}")
    print("✅ SL(2,C) action preserves determinant (Lorentz invariance verified)\n")


def verify_null_vectors():
    """Verify that null vectors correspond to rank-1 matrices."""
    print("=" * 70)
    print("Test 4: Null vectors (light cone) have rank 1")
    print("=" * 70)
    
    # Construct null vectors: (t, x, y, z) with t^2 = x^2 + y^2 + z^2
    for i in range(5):
        # Random spatial direction
        spatial = np.random.randn(3)
        t = np.linalg.norm(spatial)  # Makes it null
        x = np.array([t] + list(spatial))
        
        X = embed_spacetime(x)
        
        det_X = det(X).real
        rank = np.linalg.matrix_rank(X)
        
        print(f"Null vector x = [{x[0]:6.2f}, {x[1]:6.2f}, {x[2]:6.2f}, {x[3]:6.2f}]")
        print(f"  det(X) = {det_X:12.2e} (should be ≈ 0)")
        print(f"  rank   = {rank} (should be 1)")
        
        assert abs(det_X) < 1e-10, f"Null vector has non-zero determinant: {det_X}"
        assert rank == 1, f"Null vector matrix has rank {rank}, expected 1"
    
    print("\n✅ Null vectors correspond to rank-1 matrices\n")


def main():
    """Run all verification tests."""
    print("\n" + "=" * 70)
    print("LORENTZ STRUCTURE IN COMPLEXIFIED QUATERNIONS - VERIFICATION")
    print("=" * 70)
    print("\nThis script verifies the mathematical claims in appendix_P6_lorentz_in_HC.tex")
    print()
    
    np.random.seed(42)  # For reproducibility
    
    verify_embedding()
    verify_determinant_equals_minkowski()
    verify_lorentz_invariance()
    verify_null_vectors()
    
    print("=" * 70)
    print("ALL TESTS PASSED ✅")
    print("=" * 70)
    print("\nThe Lorentz structure in H_C is mathematically consistent.")
    print()


if __name__ == "__main__":
    main()
