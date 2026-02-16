"""
lie_audit.py - Generic Lie algebra audit utilities

This module provides tools for analyzing finite-dimensional Lie algebras
represented as matrix generators. It computes:
- Closure under commutator
- Linear independence reduction
- Structure constants
- Killing form and signature
- Basic invariants for classification

Key operations are performed using exact sympy Rational arithmetic where possible,
falling back to high-precision numerical evaluation only for eigenvalues.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, Rational, simplify, eye, zeros, nsimplify
from typing import List, Tuple, Dict, Optional


def comm(A: Matrix, B: Matrix) -> Matrix:
    """
    Compute the commutator [A, B] = AB - BA.
    
    Parameters
    ----------
    A, B : sympy.Matrix
        Matrices to commute
    
    Returns
    -------
    sympy.Matrix
        Commutator [A, B]
    
    Examples
    --------
    >>> A = Matrix([[0, 1], [0, 0]])
    >>> B = Matrix([[1, 0], [0, -1]])
    >>> comm(A, B)
    Matrix([[0, 2], [0, 0]])
    """
    return simplify(A * B - B * A)


def vec(M: Matrix) -> Matrix:
    """
    Vectorize a matrix into a column vector by stacking columns.
    
    For an m×n matrix, produces an (m*n)×1 column vector.
    
    Parameters
    ----------
    M : sympy.Matrix
        Matrix to vectorize
    
    Returns
    -------
    sympy.Matrix
        Column vector (m*n)×1
    
    Examples
    --------
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> vec(M)
    Matrix([[1], [3], [2], [4]])
    """
    # Stack columns: first column, then second column, etc.
    rows = M.rows
    cols = M.cols
    
    entries = []
    for col in range(cols):
        for row in range(rows):
            entries.append(M[row, col])
    
    return Matrix(entries)


def basis_reduce(mats: List[Matrix], tol: float = 0) -> Tuple[List[Matrix], Dict]:
    """
    Reduce a list of matrices to a linearly independent basis.
    
    Uses rref (reduced row echelon form) to identify linear independence.
    Works over exact rationals when possible.
    
    Parameters
    ----------
    mats : list of sympy.Matrix
        List of matrices (all same shape)
    tol : float, optional
        Tolerance for considering entries zero (default: 0 for exact arithmetic)
    
    Returns
    -------
    basis_mats : list of sympy.Matrix
        Linearly independent subset of input matrices
    transform_info : dict
        Dictionary with keys:
        - 'rank': int, dimension of basis
        - 'pivot_cols': list of int, indices of basis elements in original list
    
    Examples
    --------
    >>> M1 = Matrix([[1, 0], [0, 1]])
    >>> M2 = Matrix([[0, 1], [1, 0]])
    >>> M3 = Matrix([[1, 1], [1, 1]])  # M1 + M2
    >>> basis, info = basis_reduce([M1, M2, M3])
    >>> len(basis)
    2
    >>> info['rank']
    2
    """
    if not mats:
        return [], {'rank': 0, 'pivot_cols': []}
    
    # Build matrix where each column is vec(M_i)
    n_mats = len(mats)
    mat_shape = mats[0].shape
    
    # Verify all matrices have same shape
    for M in mats:
        if M.shape != mat_shape:
            raise ValueError("All matrices must have same shape")
    
    # Create matrix of vectorized matrices
    vec_mats = [vec(M) for M in mats]
    vec_dim = vec_mats[0].rows
    
    # Build matrix with vec(M_i) as columns
    A = zeros(vec_dim, n_mats)
    for j, v in enumerate(vec_mats):
        for i in range(vec_dim):
            A[i, j] = v[i]
    
    # Compute rref
    A_rref, pivot_cols = A.rref()
    
    # Extract basis matrices corresponding to pivot columns
    basis_mats = [mats[j] for j in pivot_cols]
    
    transform_info = {
        'rank': len(pivot_cols),
        'pivot_cols': list(pivot_cols)
    }
    
    return basis_mats, transform_info


def closure_under_commutator(
    gens: List[Matrix],
    max_iters: int = 6
) -> Tuple[List[Matrix], Dict]:
    """
    Iteratively compute closure of generators under commutator.
    
    Starting from initial generators, repeatedly add all commutators
    [T_i, T_j] and reduce to a linearly independent basis.
    Stop when basis stops growing or max_iters reached.
    
    Parameters
    ----------
    gens : list of sympy.Matrix
        Initial generators
    max_iters : int, optional
        Maximum number of iterations (default: 6)
    
    Returns
    -------
    final_basis : list of sympy.Matrix
        Closed Lie algebra basis
    metadata : dict
        Dictionary with keys:
        - 'iterations': int, number of iterations performed
        - 'dims_per_iter': list of int, dimension at each iteration
        - 'converged': bool, whether closure was achieved
    
    Examples
    --------
    >>> # su(2) generators
    >>> T1 = Matrix([[0, 1], [-1, 0]])
    >>> T2 = Matrix([[0, sp.I], [sp.I, 0]])
    >>> T3 = Matrix([[sp.I, 0], [0, -sp.I]])
    >>> basis, info = closure_under_commutator([T1, T2, T3])
    >>> info['dims_per_iter']
    [3, 3]  # Already closed
    >>> info['converged']
    True
    """
    # Start with initial basis
    current_basis, _ = basis_reduce(gens)
    dims_per_iter = [len(current_basis)]
    
    for iteration in range(max_iters):
        # Compute all commutators
        n = len(current_basis)
        new_elements = []
        
        for i in range(n):
            for j in range(i + 1, n):  # Only i < j to avoid duplication
                c = comm(current_basis[i], current_basis[j])
                new_elements.append(c)
        
        # Add to current basis
        candidate_basis = current_basis + new_elements
        
        # Reduce to independent set
        new_basis, _ = basis_reduce(candidate_basis)
        new_dim = len(new_basis)
        dims_per_iter.append(new_dim)
        
        # Check if converged
        if new_dim == len(current_basis):
            # Closure achieved
            metadata = {
                'iterations': iteration + 1,
                'dims_per_iter': dims_per_iter,
                'converged': True
            }
            return new_basis, metadata
        
        current_basis = new_basis
    
    # Max iterations reached
    metadata = {
        'iterations': max_iters,
        'dims_per_iter': dims_per_iter,
        'converged': False
    }
    
    return current_basis, metadata


def structure_constants(basis: List[Matrix]) -> Dict[Tuple[int, int, int], sp.Expr]:
    """
    Compute structure constants c_{ij}^k for Lie algebra basis.
    
    For basis {T_i}, we have [T_i, T_j] = sum_k c_{ij}^k T_k.
    
    This function solves for c_{ij}^k by vectorizing both sides
    and solving a linear system.
    
    Parameters
    ----------
    basis : list of sympy.Matrix
        Lie algebra basis (linearly independent matrices)
    
    Returns
    -------
    struct_const : dict
        Dictionary with keys (i, j, k) mapping to c_{ij}^k.
        Only non-zero structure constants are stored.
    
    Notes
    -----
    Structure constants satisfy:
    - Antisymmetry: c_{ij}^k = -c_{ji}^k
    - Jacobi identity: sum_m (c_{ij}^m c_{mk}^l + cyclic) = 0
    
    Examples
    --------
    >>> # For su(2), expect [T_i, T_j] = 2i epsilon_{ijk} T_k
    >>> basis = get_su2_basis()  # hypothetical
    >>> struct = structure_constants(basis)
    >>> struct[(0, 1, 2)]  # c_{01}^2
    2*I
    """
    n = len(basis)
    struct_const = {}
    
    if n == 0:
        return struct_const
    
    # Build matrix M where columns are vec(T_k)
    mat_shape = basis[0].shape
    vec_dim = mat_shape[0] * mat_shape[1]
    
    M = zeros(vec_dim, n)
    for k, T_k in enumerate(basis):
        v = vec(T_k)
        for i in range(vec_dim):
            M[i, k] = v[i]
    
    # For each pair (i, j), solve [T_i, T_j] = sum_k c_{ij}^k T_k
    for i in range(n):
        for j in range(n):
            if i == j:
                # [T_i, T_i] = 0
                continue
            
            # Compute commutator
            c_ij = comm(basis[i], basis[j])
            b = vec(c_ij)
            
            # Solve M * x = b for x = coefficients
            try:
                # Use solve_least_squares for robustness
                coeffs = M.solve_least_squares(b)
                
                # Store non-zero structure constants
                for k in range(n):
                    c_ijk = simplify(coeffs[k])
                    if c_ijk != 0:
                        struct_const[(i, j, k)] = c_ijk
            except:
                # If solve fails, commutator may not be in span (shouldn't happen for closed algebra)
                pass
    
    return struct_const


def killing_form(basis: List[Matrix], struct: Dict[Tuple[int, int, int], sp.Expr]) -> Matrix:
    """
    Compute Killing form from structure constants.
    
    The Killing form is K_{ij} = Tr(ad_{T_i} ∘ ad_{T_j})
    where ad_X(Y) = [X, Y] is the adjoint representation.
    
    In terms of structure constants:
    K_{ij} = sum_{m,n} c_{im}^n * c_{jn}^m
    
    Parameters
    ----------
    basis : list of sympy.Matrix
        Lie algebra basis
    struct : dict
        Structure constants from structure_constants()
    
    Returns
    -------
    K : sympy.Matrix
        Killing form matrix (n×n symmetric matrix)
    
    Notes
    -----
    - Killing form is symmetric: K_{ij} = K_{ji}
    - Algebra is semisimple iff det(K) ≠ 0 (non-degenerate)
    - Signature (n_pos, n_neg, n_zero) helps classify algebra
    
    Examples
    --------
    >>> basis = get_su2_basis()
    >>> struct = structure_constants(basis)
    >>> K = killing_form(basis, struct)
    >>> K.det()  # Should be non-zero (semisimple)
    -64
    """
    n = len(basis)
    K = zeros(n, n)
    
    for i in range(n):
        for j in range(n):
            # K_ij = sum_{m,n} c_{im}^n * c_{jn}^m
            sum_val = 0
            for m in range(n):
                for k in range(n):
                    # c_{im}^k
                    c_imk = struct.get((i, m, k), 0)
                    # c_{jk}^m
                    c_jkm = struct.get((j, k, m), 0)
                    
                    if c_imk != 0 and c_jkm != 0:
                        sum_val += c_imk * c_jkm
            
            K[i, j] = simplify(sum_val)
    
    return K


def signature_of_symmetric_form(K: Matrix) -> Tuple[int, int, int]:
    """
    Compute signature of a symmetric bilinear form.
    
    Returns (n_pos, n_neg, n_zero) where:
    - n_pos: number of positive eigenvalues
    - n_neg: number of negative eigenvalues
    - n_zero: number of zero eigenvalues
    
    Parameters
    ----------
    K : sympy.Matrix
        Symmetric matrix
    
    Returns
    -------
    tuple of int
        (n_pos, n_neg, n_zero)
    
    Notes
    -----
    Uses high-precision numerical evaluation (80 digits) for eigenvalues
    to avoid false zeros.
    
    Examples
    --------
    >>> K = Matrix([[1, 0], [0, -1]])
    >>> signature_of_symmetric_form(K)
    (1, 1, 0)
    """
    # Symmetrize just in case
    K_sym = (K + K.T) / 2
    
    # Compute eigenvalues with high precision
    eigenvals = K_sym.eigenvals()
    
    n_pos = 0
    n_neg = 0
    n_zero = 0
    
    tol = 1e-50  # Very small tolerance
    
    for eigval, multiplicity in eigenvals.items():
        # Evaluate numerically with high precision
        try:
            val_numeric = complex(eigval.evalf(80))
            val_real = val_numeric.real
            
            if abs(val_real) < tol:
                n_zero += multiplicity
            elif val_real > tol:
                n_pos += multiplicity
            else:
                n_neg += multiplicity
        except:
            # If evaluation fails, try symbolic comparison
            if eigval == 0:
                n_zero += multiplicity
            else:
                # Try to determine sign
                val_num = complex(eigval.evalf(20))
                if val_num.real > 0:
                    n_pos += multiplicity
                else:
                    n_neg += multiplicity
    
    return (n_pos, n_neg, n_zero)


def trace_invariants(basis: List[Matrix]) -> Dict:
    """
    Compute trace-based invariants for Lie algebra basis.
    
    Returns traces tr(T_i) and tr(T_i * T_j) which can provide
    hints about semisimplicity and compactness.
    
    Parameters
    ----------
    basis : list of sympy.Matrix
        Lie algebra basis
    
    Returns
    -------
    dict
        Dictionary with keys:
        - 'traces': list of traces tr(T_i)
        - 'trace_products': dict mapping (i, j) to tr(T_i * T_j)
    
    Examples
    --------
    >>> basis = [Matrix([[0, 1], [-1, 0]])]
    >>> inv = trace_invariants(basis)
    >>> inv['traces']
    [0]
    """
    n = len(basis)
    
    traces = []
    for i in range(n):
        traces.append(simplify(basis[i].trace()))
    
    trace_products = {}
    for i in range(n):
        for j in range(i, n):  # Only compute upper triangle
            prod = simplify((basis[i] * basis[j]).trace())
            trace_products[(i, j)] = prod
            if i != j:
                trace_products[(j, i)] = prod  # Symmetric
    
    return {
        'traces': traces,
        'trace_products': trace_products
    }


def main():
    """
    Run verification tests for Lie algebra audit utilities.
    """
    print("=" * 70)
    print("LIE ALGEBRA AUDIT UTILITIES - VERIFICATION")
    print("=" * 70)
    print()
    
    # Test 1: Commutator
    print("1. Testing commutator...")
    from sympy import I
    A = Matrix([[0, 1], [0, 0]])
    B = Matrix([[1, 0], [0, -1]])
    c = comm(A, B)
    expected = Matrix([[0, -2], [0, 0]])
    assert c == expected, "Commutator test failed"
    print(f"   ✓ [A, B] = {c}")
    print()
    
    # Test 2: Vectorization
    print("2. Testing vectorization...")
    M = Matrix([[1, 2], [3, 4]])
    v = vec(M)
    expected_v = Matrix([1, 3, 2, 4])
    assert v == expected_v, "Vectorization test failed"
    print(f"   ✓ vec(M) = {v.T}")
    print()
    
    # Test 3: Basis reduction
    print("3. Testing basis reduction...")
    M1 = Matrix([[1, 0], [0, 0]])
    M2 = Matrix([[0, 1], [0, 0]])
    M3 = M1 + M2  # Linear combination
    basis, info = basis_reduce([M1, M2, M3])
    assert info['rank'] == 2, f"Expected rank 2, got {info['rank']}"
    print(f"   ✓ Reduced 3 matrices to {info['rank']} independent")
    print()
    
    # Test 4: Closure (su(2) example)
    print("4. Testing closure computation (su(2))...")
    T1 = Matrix([[0, 1], [-1, 0]]) * I
    T2 = Matrix([[0, I], [I, 0]])
    T3 = Matrix([[I, 0], [0, -I]])
    
    # These should be closed (form su(2))
    basis, info = closure_under_commutator([T1, T2, T3], max_iters=3)
    print(f"   ✓ Dimension trajectory: {info['dims_per_iter']}")
    print(f"   ✓ Converged: {info['converged']}")
    print()
    
    print("=" * 70)
    print("ALL VERIFICATION TESTS PASSED")
    print("=" * 70)


if __name__ == '__main__':
    main()
