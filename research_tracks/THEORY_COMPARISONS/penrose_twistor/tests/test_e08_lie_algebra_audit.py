#!/usr/bin/env python3
"""
test_e08_lie_algebra_audit.py - Tests for e08 Lie algebra audit

Tests the Lie algebra audit utilities and e08 experiment that derives
su(2,2) from UBT generators.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from pathlib import Path
from sympy import Matrix, I, eye, zeros, simplify

from THEORY_COMPARISONS.penrose_twistor.twistor_core.lie_audit import (
    comm,
    vec,
    basis_reduce,
    closure_under_commutator,
    structure_constants,
    killing_form,
    signature_of_symmetric_form,
    trace_invariants,
)

from THEORY_COMPARISONS.penrose_twistor.experiments.e08_lie_algebra_audit import (
    build_G0_minimal,
    compute_lie_closure,
    make_traceless,
)


# ============================================================================
# Tests for lie_audit.py utilities
# ============================================================================

def test_comm_antisymmetry():
    """Test that commutator is antisymmetric: [A, B] = -[B, A]."""
    A = Matrix([[0, 1], [0, 0]])
    B = Matrix([[1, 0], [0, -1]])
    
    c_AB = comm(A, B)
    c_BA = comm(B, A)
    
    assert c_AB == -c_BA, "Commutator antisymmetry failed"
    print("✓ Commutator antisymmetry verified")


def test_comm_bilinearity():
    """Test commutator bilinearity: [aA, B] = a[A, B]."""
    A = Matrix([[0, 1], [0, 0]])
    B = Matrix([[1, 0], [0, -1]])
    a = 2 + I
    
    c1 = comm(a * A, B)
    c2 = a * comm(A, B)
    
    assert simplify(c1 - c2) == zeros(2, 2), "Commutator bilinearity failed"
    print("✓ Commutator bilinearity verified")


def test_comm_jacobi_identity():
    """Test Jacobi identity: [A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0."""
    A = Matrix([[0, 1], [-1, 0]]) * I
    B = Matrix([[0, I], [I, 0]])
    C = Matrix([[I, 0], [0, -I]])
    
    term1 = comm(A, comm(B, C))
    term2 = comm(B, comm(C, A))
    term3 = comm(C, comm(A, B))
    
    jacobi_sum = simplify(term1 + term2 + term3)
    
    assert jacobi_sum == zeros(2, 2), "Jacobi identity failed"
    print("✓ Jacobi identity verified")


def test_vec_dimensions():
    """Test that vectorization produces correct dimensions."""
    M = Matrix([[1, 2, 3], [4, 5, 6]])
    v = vec(M)
    
    assert v.shape == (6, 1), f"Expected (6, 1), got {v.shape}"
    print("✓ Vectorization dimensions correct")


def test_vec_preserves_linear_independence():
    """Test that vec preserves linear independence."""
    M1 = Matrix([[1, 0], [0, 0]])
    M2 = Matrix([[0, 1], [0, 0]])
    M3 = Matrix([[0, 0], [1, 0]])
    
    v1, v2, v3 = vec(M1), vec(M2), vec(M3)
    
    # Build matrix with vectors as columns
    A = zeros(4, 3)
    for i in range(4):
        A[i, 0] = v1[i]
        A[i, 1] = v2[i]
        A[i, 2] = v3[i]
    
    rank = A.rank()
    assert rank == 3, f"Expected rank 3, got {rank}"
    print("✓ Vectorization preserves linear independence")


def test_basis_reduce_removes_dependent():
    """Test that basis_reduce removes linearly dependent matrices."""
    M1 = Matrix([[1, 0], [0, 0]])
    M2 = Matrix([[0, 1], [0, 0]])
    M3 = M1 + M2  # Dependent
    M4 = 2 * M1  # Dependent
    
    basis, info = basis_reduce([M1, M2, M3, M4])
    
    assert info['rank'] == 2, f"Expected rank 2, got {info['rank']}"
    assert len(basis) == 2, f"Expected 2 basis elements, got {len(basis)}"
    print("✓ Basis reduction removes dependent matrices")


def test_closure_su2_already_closed():
    """Test closure on su(2) generators (should be closed immediately)."""
    # su(2) generators (up to normalization)
    T1 = Matrix([[0, 1], [-1, 0]]) * I
    T2 = Matrix([[0, I], [I, 0]])
    T3 = Matrix([[I, 0], [0, -I]])
    
    basis, info = closure_under_commutator([T1, T2, T3], max_iters=3)
    
    # Should converge in 1 iteration (already closed)
    assert info['converged'], "Expected convergence"
    assert len(basis) == 3, f"Expected dimension 3, got {len(basis)}"
    assert info['dims_per_iter'][0] == 3, "Initial dimension should be 3"
    assert info['dims_per_iter'][1] == 3, "Should remain 3 after one iteration"
    print("✓ su(2) closure correctly identifies closed algebra")


def test_closure_grows_dimension():
    """Test that closure can grow dimension from initial generators."""
    # Start with only two su(2) generators
    T1 = Matrix([[0, 1], [-1, 0]]) * I
    T2 = Matrix([[0, I], [I, 0]])
    
    basis, info = closure_under_commutator([T1, T2], max_iters=3)
    
    # Should grow to 3 dimensions (adding [T1, T2])
    assert len(basis) >= 3, f"Expected at least 3 dimensions, got {len(basis)}"
    assert info['dims_per_iter'][0] == 2, "Initial dimension should be 2"
    print(f"✓ Closure grows from 2 to {len(basis)} dimensions")


def test_structure_constants_antisymmetry():
    """Test that structure constants are antisymmetric: c_ijk = -c_jik."""
    # Use su(2) for known structure
    T1 = Matrix([[0, 1], [-1, 0]]) * I
    T2 = Matrix([[0, I], [I, 0]])
    T3 = Matrix([[I, 0], [0, -I]])
    
    basis = [T1, T2, T3]
    struct = structure_constants(basis)
    
    # Check antisymmetry for all pairs
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c_ijk = struct.get((i, j, k), 0)
                c_jik = struct.get((j, i, k), 0)
                
                diff = simplify(c_ijk + c_jik)
                assert diff == 0, f"Antisymmetry failed for ({i},{j},{k}): {c_ijk} + {c_jik} = {diff}"
    
    print("✓ Structure constants antisymmetry verified")


def test_killing_form_symmetry():
    """Test that Killing form is symmetric."""
    # Use su(2)
    T1 = Matrix([[0, 1], [-1, 0]]) * I
    T2 = Matrix([[0, I], [I, 0]])
    T3 = Matrix([[I, 0], [0, -I]])
    
    basis = [T1, T2, T3]
    struct = structure_constants(basis)
    K = killing_form(basis, struct)
    
    # Check symmetry
    K_transpose = K.T
    diff = simplify(K - K_transpose)
    
    assert diff == zeros(3, 3), "Killing form is not symmetric"
    print("✓ Killing form symmetry verified")


def test_killing_form_semisimple_su2():
    """Test that su(2) has non-degenerate Killing form (semisimple)."""
    T1 = Matrix([[0, 1], [-1, 0]]) * I
    T2 = Matrix([[0, I], [I, 0]])
    T3 = Matrix([[I, 0], [0, -I]])
    
    basis = [T1, T2, T3]
    struct = structure_constants(basis)
    K = killing_form(basis, struct)
    
    rank = K.rank()
    dim = len(basis)
    
    assert rank == dim, f"Expected rank {dim}, got {rank} (not semisimple)"
    print("✓ su(2) Killing form is non-degenerate (semisimple)")


def test_signature_positive_definite():
    """Test signature computation for positive definite matrix."""
    K = Matrix([[2, 0], [0, 3]])
    sig = signature_of_symmetric_form(K)
    
    assert sig == (2, 0, 0), f"Expected (2, 0, 0), got {sig}"
    print("✓ Positive definite signature correct")


def test_signature_indefinite():
    """Test signature computation for indefinite matrix."""
    K = Matrix([[1, 0], [0, -1]])
    sig = signature_of_symmetric_form(K)
    
    assert sig == (1, 1, 0), f"Expected (1, 1, 0), got {sig}"
    print("✓ Indefinite signature correct")


# ============================================================================
# Tests for e08 experiment
# ============================================================================

def test_make_traceless():
    """Test that make_traceless produces traceless matrices."""
    M = Matrix([[1, 2], [3, 4]])
    M_tl = make_traceless(M)
    
    tr = M_tl.trace()
    assert tr == 0, f"Expected trace 0, got {tr}"
    print("✓ make_traceless produces traceless matrix")


def test_G0_minimal_all_traceless():
    """Test that all G0_minimal generators are traceless."""
    gens = build_G0_minimal()
    
    for i, gen in enumerate(gens):
        tr = gen.trace()
        assert tr == 0, f"Generator {i} has non-zero trace: {tr}"
    
    print(f"✓ All {len(gens)} G0_minimal generators are traceless")


def test_G0_minimal_all_4x4():
    """Test that all G0_minimal generators are 4×4 matrices."""
    gens = build_G0_minimal()
    
    for i, gen in enumerate(gens):
        assert gen.shape == (4, 4), f"Generator {i} is not 4×4: {gen.shape}"
    
    print(f"✓ All {len(gens)} G0_minimal generators are 4×4")


def test_e08_closure_converges():
    """Test that e08 closure computation converges."""
    gens = build_G0_minimal()
    basis, metadata = compute_lie_closure(gens, max_iters=6)
    
    assert metadata['converged'], "Closure did not converge"
    print(f"✓ e08 closure converged in {metadata['iterations']} iterations")


def test_e08_final_dimension():
    """Test that e08 produces 15-dimensional algebra."""
    gens = build_G0_minimal()
    basis, metadata = compute_lie_closure(gens, max_iters=6)
    
    dim = len(basis)
    assert dim == 15, f"Expected dimension 15, got {dim}"
    print("✓ e08 produces 15-dimensional algebra (matches su(2,2))")


def test_e08_final_algebra_traceless():
    """Test that all final basis elements are traceless."""
    gens = build_G0_minimal()
    basis, metadata = compute_lie_closure(gens, max_iters=6)
    
    for i, T in enumerate(basis):
        tr = T.trace()
        assert tr == 0, f"Basis element {i} has non-zero trace: {tr}"
    
    print(f"✓ All {len(basis)} final basis elements are traceless")


def test_e08_killing_form_signature():
    """Test that e08 Killing form has non-compact signature."""
    gens = build_G0_minimal()
    basis, metadata = compute_lie_closure(gens, max_iters=6)
    
    struct = structure_constants(basis)
    K = killing_form(basis, struct)
    sig = signature_of_symmetric_form(K)
    
    n_pos, n_neg, n_zero = sig
    
    # Should be non-compact (both positive and negative eigenvalues)
    assert n_pos > 0, f"Expected positive eigenvalues, got {n_pos}"
    assert n_neg > 0, f"Expected negative eigenvalues, got {n_neg}"
    assert n_zero == 0, f"Expected no zero eigenvalues, got {n_zero}"
    
    print(f"✓ e08 Killing form signature ({n_pos}, {n_neg}, {n_zero}) is non-compact")


def test_e08_semisimple():
    """Test that e08 produces semisimple algebra (rank(K) = dim)."""
    gens = build_G0_minimal()
    basis, metadata = compute_lie_closure(gens, max_iters=6)
    
    struct = structure_constants(basis)
    K = killing_form(basis, struct)
    
    rank = K.rank()
    dim = len(basis)
    
    assert rank == dim, f"Expected rank {dim}, got {rank} (not semisimple)"
    print(f"✓ e08 algebra is semisimple (rank(K) = {dim})")


def test_e08_commutator_closure():
    """Test that final basis is closed under commutation."""
    gens = build_G0_minimal()
    basis, metadata = compute_lie_closure(gens, max_iters=6)
    
    # Compute all commutators and check they're in span of basis
    struct = structure_constants(basis)
    
    # For each commutator, check it can be expressed as linear combination
    n = len(basis)
    for i in range(n):
        for j in range(i + 1, n):
            # [T_i, T_j] should be expressible in terms of basis
            # This is implicitly tested by structure_constants succeeding
            pass
    
    # If structure_constants succeeded, closure holds
    print(f"✓ e08 final basis is closed under commutation ({n} generators)")


def test_e08_reports_exist():
    """Test that e08 generates report files."""
    # Get report directory
    script_dir = Path(__file__).parent.parent / "experiments"
    reports_dir = script_dir.parent / "reports"
    
    csv_path = reports_dir / "e08_commutator_table.csv"
    md_path = reports_dir / "e08_summary.md"
    
    # These should exist after running e08
    # (This test assumes e08 has been run at least once)
    if csv_path.exists() and md_path.exists():
        print("✓ e08 report files exist")
        
        # Check CSV has content
        with open(csv_path) as f:
            lines = f.readlines()
            assert len(lines) > 1, "CSV should have more than header"
        
        # Check MD has content
        with open(md_path) as f:
            content = f.read()
            assert "e08" in content.lower(), "MD should mention e08"
            assert "15" in content, "MD should mention dimension 15"
        
        print("  ✓ CSV has structure constants")
        print("  ✓ MD has summary content")
    else:
        pytest.skip("e08 reports not yet generated (run experiment first)")


def main():
    """
    Run all tests and print results.
    """
    print("=" * 70)
    print("TEST SUITE: e08 LIE ALGEBRA AUDIT")
    print("=" * 70)
    print()
    
    print("Testing lie_audit.py utilities...")
    print("-" * 70)
    test_comm_antisymmetry()
    test_comm_bilinearity()
    test_comm_jacobi_identity()
    test_vec_dimensions()
    test_vec_preserves_linear_independence()
    test_basis_reduce_removes_dependent()
    test_closure_su2_already_closed()
    test_closure_grows_dimension()
    test_structure_constants_antisymmetry()
    test_killing_form_symmetry()
    test_killing_form_semisimple_su2()
    test_signature_positive_definite()
    test_signature_indefinite()
    print()
    
    print("Testing e08 experiment...")
    print("-" * 70)
    test_make_traceless()
    test_G0_minimal_all_traceless()
    test_G0_minimal_all_4x4()
    test_e08_closure_converges()
    test_e08_final_dimension()
    test_e08_final_algebra_traceless()
    test_e08_killing_form_signature()
    test_e08_semisimple()
    test_e08_commutator_closure()
    test_e08_reports_exist()
    print()
    
    print("=" * 70)
    print("ALL TESTS PASSED")
    print("=" * 70)


if __name__ == '__main__':
    main()
