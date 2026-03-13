#!/usr/bin/env python3
"""
e08_lie_algebra_audit.py - Derive or refute su(2,2) emergence from UBT generators

This experiment attempts to derive the conformal Lie algebra su(2,2) from
UBT-side generators without importing known su(2,2) constructions.

Methodology:
1. Build 4×4 generator candidates from UBT's 2×2 biquaternion basis
2. Compute closure under commutator using generic Lie algebra tools
3. Analyze structure constants and Killing form
4. Compare invariants (dimension, signature) against su(2,2) expectations

Expected su(2,2) properties:
- Dimension: 15 (real form of sl(4,C))
- Killing form signature: (8, 7, 0) or similar non-compact signature
- Semisimple: det(K) ≠ 0

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
import csv
from pathlib import Path
from sympy import Matrix, I, zeros, eye, simplify, Rational

from THEORY_COMPARISONS.penrose_twistor.twistor_core.ubt_generators import (
    get_biquaternion_basis_2x2,
    get_sigma_matrices,
)

from THEORY_COMPARISONS.penrose_twistor.twistor_core.lie_audit import (
    comm,
    closure_under_commutator,
    structure_constants,
    killing_form,
    signature_of_symmetric_form,
    trace_invariants,
)


def print_header(title):
    """Print a formatted section header."""
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)
    print()


def build_4x4_from_2x2_block_diagonal(M_2x2):
    """
    Embed a 2×2 matrix into 4×4 as a block diagonal matrix.
    
    [[M, 0],
     [0, M]]
    
    Parameters
    ----------
    M_2x2 : sympy.Matrix (2×2)
        Input 2×2 matrix
    
    Returns
    -------
    sympy.Matrix (4×4)
        Block diagonal embedding
    """
    M = zeros(4, 4)
    for i in range(2):
        for j in range(2):
            M[i, j] = M_2x2[i, j]
            M[i+2, j+2] = M_2x2[i, j]
    return M


def build_4x4_from_2x2_off_diagonal(M_2x2):
    """
    Embed a 2×2 matrix into 4×4 in off-diagonal blocks.
    
    [[0, M],
     [M†, 0]]
    
    Parameters
    ----------
    M_2x2 : sympy.Matrix (2×2)
        Input 2×2 matrix
    
    Returns
    -------
    sympy.Matrix (4×4)
        Off-diagonal embedding
    """
    M = zeros(4, 4)
    for i in range(2):
        for j in range(2):
            M[i, j+2] = M_2x2[i, j]
            M[i+2, j] = M_2x2[i, j].conjugate()
    return M


def build_4x4_from_2x2_upper_left(M_2x2):
    """
    Embed a 2×2 matrix into upper-left block of 4×4.
    
    [[M, 0],
     [0, 0]]
    
    Parameters
    ----------
    M_2x2 : sympy.Matrix (2×2)
        Input 2×2 matrix
    
    Returns
    -------
    sympy.Matrix (4×4)
        Upper-left embedding
    """
    M = zeros(4, 4)
    for i in range(2):
        for j in range(2):
            M[i, j] = M_2x2[i, j]
    return M


def build_4x4_from_2x2_lower_right(M_2x2):
    """
    Embed a 2×2 matrix into lower-right block of 4×4.
    
    [[0, 0],
     [0, M]]
    
    Parameters
    ----------
    M_2x2 : sympy.Matrix (2×2)
        Input 2×2 matrix
    
    Returns
    -------
    sympy.Matrix (4×4)
        Lower-right embedding
    """
    M = zeros(4, 4)
    for i in range(2):
        for j in range(2):
            M[i+2, j+2] = M_2x2[i, j]
    return M


def make_traceless(M):
    """
    Make a matrix traceless by subtracting (tr(M)/n) * I.
    
    Parameters
    ----------
    M : sympy.Matrix
        Input matrix
    
    Returns
    -------
    sympy.Matrix
        Traceless matrix
    """
    n = M.rows
    tr_M = M.trace()
    return simplify(M - (tr_M / n) * eye(n))


def build_G0_minimal():
    """
    Build G0_minimal: Initial 4×4 generator set from UBT 2×2 basis.
    
    Strategy:
    - Start from 2×2 biquaternion basis {I, σ₁, σ₂, σ₃}
    - Embed into 4×4 using various block structures
    - Make traceless (required for su(n,m))
    - Include both diagonal and off-diagonal embeddings
    
    Returns
    -------
    list of sympy.Matrix (4×4)
        Initial generators for Lie algebra
    """
    print_header("BUILDING G0_MINIMAL GENERATOR SET")
    
    # Get 2×2 basis from UBT
    unit, sigma_1, sigma_2, sigma_3 = get_biquaternion_basis_2x2()
    
    print("UBT 2×2 biquaternion basis:")
    print(f"  I, σ₁, σ₂, σ₃")
    print()
    
    generators = []
    
    # Strategy 1: Block diagonal embeddings (traceless)
    print("Strategy 1: Block diagonal embeddings (made traceless)")
    
    # σ₃ block diagonal gives a traceless matrix already if σ₃ is traceless
    for name, sigma in [("σ₁", sigma_1), ("σ₂", sigma_2), ("σ₃", sigma_3)]:
        M_diag = build_4x4_from_2x2_block_diagonal(sigma)
        M_traceless = make_traceless(M_diag)
        generators.append(M_traceless)
        print(f"  Added: diag({name}) [traceless]")
    
    print()
    
    # Strategy 2: Off-diagonal embeddings
    print("Strategy 2: Off-diagonal embeddings")
    
    for name, sigma in [("σ₁", sigma_1), ("σ₂", sigma_2), ("σ₃", sigma_3)]:
        M_off = build_4x4_from_2x2_off_diagonal(sigma)
        M_traceless = make_traceless(M_off)
        generators.append(M_traceless)
        print(f"  Added: off_diag({name}) [traceless]")
    
    print()
    
    # Strategy 3: Upper-left and lower-right blocks (for SU(2,2) structure)
    print("Strategy 3: Upper-left and lower-right blocks")
    
    # Upper-left σ₃ (traceless by construction if σ₃ is traceless)
    M_ul = build_4x4_from_2x2_upper_left(sigma_3)
    M_ul_traceless = make_traceless(M_ul)
    generators.append(M_ul_traceless)
    print(f"  Added: upper_left(σ₃) [traceless]")
    
    # Lower-right σ₃ (creates difference with upper-left)
    M_lr = build_4x4_from_2x2_lower_right(sigma_3)
    M_lr_traceless = make_traceless(M_lr)
    generators.append(M_lr_traceless)
    print(f"  Added: lower_right(σ₃) [traceless]")
    
    print()
    
    # Strategy 4: Complexified combinations
    print("Strategy 4: Complexified generators")
    
    # i*σ₁ block diagonal
    M_i_sigma1 = build_4x4_from_2x2_block_diagonal(I * sigma_1)
    M_i_sigma1_traceless = make_traceless(M_i_sigma1)
    generators.append(M_i_sigma1_traceless)
    print(f"  Added: diag(i·σ₁) [traceless]")
    
    # i*σ₂ off-diagonal
    M_i_sigma2 = build_4x4_from_2x2_off_diagonal(I * sigma_2)
    M_i_sigma2_traceless = make_traceless(M_i_sigma2)
    generators.append(M_i_sigma2_traceless)
    print(f"  Added: off_diag(i·σ₂) [traceless]")
    
    print()
    print(f"Total initial generators: {len(generators)}")
    print()
    
    # Verify all are traceless
    for i, gen in enumerate(generators):
        tr = gen.trace()
        if tr != 0:
            print(f"WARNING: Generator {i} has non-zero trace: {tr}")
    
    print("✓ All generators verified traceless")
    print()
    
    return generators


def compute_lie_closure(generators, max_iters=6):
    """
    Compute Lie algebra closure from initial generators.
    
    Parameters
    ----------
    generators : list of sympy.Matrix
        Initial generators
    max_iters : int
        Maximum closure iterations
    
    Returns
    -------
    basis : list of sympy.Matrix
        Closed Lie algebra basis
    metadata : dict
        Closure metadata (iterations, dimensions, convergence)
    """
    print_header("COMPUTING LIE ALGEBRA CLOSURE")
    
    print(f"Initial generators: {len(generators)}")
    print(f"Maximum iterations: {max_iters}")
    print()
    
    print("Running closure computation...")
    basis, metadata = closure_under_commutator(generators, max_iters=max_iters)
    
    print()
    print("Results:")
    print(f"  Final dimension: {len(basis)}")
    print(f"  Iterations: {metadata['iterations']}")
    print(f"  Converged: {metadata['converged']}")
    print(f"  Dimension growth: {metadata['dims_per_iter']}")
    print()
    
    if metadata['converged']:
        print("✓ Closure achieved (dimension stabilized)")
    else:
        print("⚠ Did not converge within max iterations")
        print("  (May need more iterations or initial generators)")
    
    print()
    
    return basis, metadata


def compute_structure_and_killing(basis):
    """
    Compute structure constants and Killing form.
    
    Parameters
    ----------
    basis : list of sympy.Matrix
        Closed Lie algebra basis
    
    Returns
    -------
    struct : dict
        Structure constants
    K : sympy.Matrix
        Killing form
    signature : tuple
        (n_pos, n_neg, n_zero)
    """
    print_header("COMPUTING STRUCTURE CONSTANTS & KILLING FORM")
    
    n = len(basis)
    print(f"Computing structure constants for {n}-dimensional algebra...")
    
    struct = structure_constants(basis)
    
    n_nonzero = len(struct)
    print(f"  Non-zero structure constants: {n_nonzero}")
    print()
    
    print("Computing Killing form...")
    K = killing_form(basis, struct)
    
    print(f"  Killing form: {n}×{n} matrix")
    print()
    
    print("Computing Killing form signature...")
    signature = signature_of_symmetric_form(K)
    n_pos, n_neg, n_zero = signature
    
    print(f"  Signature: ({n_pos}, {n_neg}, {n_zero})")
    print(f"    Positive eigenvalues: {n_pos}")
    print(f"    Negative eigenvalues: {n_neg}")
    print(f"    Zero eigenvalues: {n_zero}")
    print()
    
    # Check semisimplicity
    rank_K = K.rank()
    is_semisimple = (rank_K == n)
    
    print(f"  Rank(K) = {rank_K}")
    print(f"  Dimension = {n}")
    
    if is_semisimple:
        print("  ✓ Algebra appears SEMISIMPLE (non-degenerate Killing form)")
    else:
        print(f"  ✗ Algebra is NOT semisimple (rank deficiency: {n - rank_K})")
    
    print()
    
    return struct, K, signature


def save_commutator_table(basis, struct, filepath):
    """
    Save commutator table to CSV.
    
    CSV format: i, j, k, c_ijk
    where [T_i, T_j] = sum_k c_ijk T_k
    
    Parameters
    ----------
    basis : list of sympy.Matrix
        Lie algebra basis
    struct : dict
        Structure constants
    filepath : str or Path
        Output CSV path
    """
    print(f"Saving commutator table to {filepath}...")
    
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['i', 'j', 'k', 'c_ijk'])
        
        for (i, j, k), c_ijk in sorted(struct.items()):
            # Convert to string for CSV
            c_str = str(c_ijk)
            writer.writerow([i, j, k, c_str])
    
    print(f"  Wrote {len(struct)} structure constants")
    print()


def save_summary_report(basis, metadata, struct, K, signature, filepath):
    """
    Save summary report to Markdown.
    
    Parameters
    ----------
    basis : list of sympy.Matrix
        Lie algebra basis
    metadata : dict
        Closure metadata
    struct : dict
        Structure constants
    K : sympy.Matrix
        Killing form
    signature : tuple
        (n_pos, n_neg, n_zero)
    filepath : str or Path
        Output markdown path
    """
    print(f"Saving summary report to {filepath}...")
    
    n = len(basis)
    n_pos, n_neg, n_zero = signature
    rank_K = K.rank()
    is_semisimple = (rank_K == n)
    
    with open(filepath, 'w') as f:
        f.write("# e08: Lie Algebra Audit Summary\n\n")
        
        f.write("## Experiment: Derive su(2,2) from UBT Generators\n\n")
        
        f.write("### Objective\n\n")
        f.write("Construct a candidate Lie algebra from UBT-side generators ")
        f.write("(2×2 biquaternion basis embedded into 4×4 matrices) and test ")
        f.write("whether the resulting algebra is isomorphic to su(2,2).\n\n")
        
        f.write("### Generator Construction\n\n")
        f.write("**Source**: UBT 2×2 biquaternion basis {I, σ₁, σ₂, σ₃}\n\n")
        f.write("**Embedding strategies**:\n")
        f.write("1. Block diagonal: `diag(σ, σ)`\n")
        f.write("2. Off-diagonal: `[[0, σ], [σ†, 0]]`\n")
        f.write("3. Upper-left / lower-right blocks\n")
        f.write("4. Complexified combinations: `i·σ` variants\n\n")
        f.write("All generators made traceless (required for su(n,m)).\n\n")
        
        f.write(f"**Initial generators**: {metadata['dims_per_iter'][0]}\n\n")
        
        f.write("### Closure Computation\n\n")
        f.write(f"**Algorithm**: Iterative commutator closure with basis reduction\n\n")
        f.write(f"**Iterations**: {metadata['iterations']}\n\n")
        f.write(f"**Dimension growth**: {metadata['dims_per_iter']}\n\n")
        f.write(f"**Converged**: {'Yes' if metadata['converged'] else 'No'}\n\n")
        
        f.write("### Final Algebra Properties\n\n")
        f.write(f"**Dimension**: {n}\n\n")
        f.write(f"**Structure constants**: {len(struct)} non-zero\n\n")
        f.write(f"**Killing form signature**: ({n_pos}, {n_neg}, {n_zero})\n")
        f.write(f"  - Positive eigenvalues: {n_pos}\n")
        f.write(f"  - Negative eigenvalues: {n_neg}\n")
        f.write(f"  - Zero eigenvalues: {n_zero}\n\n")
        
        f.write(f"**Rank(K)**: {rank_K}\n\n")
        f.write(f"**Semisimple**: {'Yes' if is_semisimple else 'No'}\n\n")
        
        f.write("### Comparison with su(2,2)\n\n")
        f.write("**Expected su(2,2) properties**:\n")
        f.write("- Dimension: 15\n")
        f.write("- Real form of sl(4,ℂ)\n")
        f.write("- Non-compact signature (mixed positive/negative eigenvalues)\n")
        f.write("- Semisimple: det(K) ≠ 0\n\n")
        
        f.write("**Observed vs Expected**:\n")
        f.write(f"- Dimension: {n} vs 15\n")
        
        if n == 15:
            f.write("  ✓ **MATCHES su(2,2) dimension**\n")
        else:
            f.write(f"  ✗ **Does NOT match** (deficit: {15 - n})\n")
        
        f.write("\n")
        
        if n_pos > 0 and n_neg > 0 and n_zero == 0:
            f.write(f"- Signature: ({n_pos}, {n_neg}, 0) - non-compact ✓\n")
        elif n_zero > 0:
            f.write(f"- Signature: ({n_pos}, {n_neg}, {n_zero}) - degenerate ✗\n")
        else:
            f.write(f"- Signature: ({n_pos}, {n_neg}, 0) - compact or degenerate\n")
        
        f.write("\n")
        
        if is_semisimple:
            f.write("- Semisimple: Yes ✓\n\n")
        else:
            f.write("- Semisimple: No ✗\n\n")
        
        f.write("### Conclusion\n\n")
        
        if n == 15 and is_semisimple and n_zero == 0:
            f.write("**STRONG INDICATION**: The derived algebra has dimension 15, ")
            f.write("is semisimple, and has a non-compact signature consistent with su(2,2).\n\n")
            f.write("**Further verification needed**:\n")
            f.write("- Check Lie algebra isomorphism via Cartan classification\n")
            f.write("- Verify conformal group action on spacetime\n")
            f.write("- Compare with known su(2,2) representation theory\n")
        elif n < 15:
            f.write(f"**INCOMPLETE ALGEBRA**: Dimension {n} < 15 suggests ")
            f.write("the initial generator set is insufficient to span su(2,2).\n\n")
            f.write("**Possible extensions**:\n")
            f.write("- Add more 4×4 embeddings of UBT generators\n")
            f.write("- Include higher-order combinations (e.g., [σᵢ, σⱼ] embeddings)\n")
            f.write("- Consider alternative block structures\n")
        else:
            f.write(f"**UNEXPECTED**: Dimension {n} > 15 suggests algebra is ")
            f.write("larger than su(2,2), or contains non-trivial center.\n\n")
        
        f.write("\n")
        f.write("### Files Generated\n\n")
        f.write("- `e08_commutator_table.csv`: Structure constants\n")
        f.write("- `e08_summary.md`: This report\n\n")
        
        f.write("---\n\n")
        f.write("**Experiment**: e08_lie_algebra_audit.py\n\n")
        f.write("**Date**: 2026-02-16\n\n")
    
    print("  Report saved successfully")
    print()


def main():
    """
    Run e08 Lie algebra audit experiment.
    """
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "e08: LIE ALGEBRA AUDIT (UBT → su(2,2)?)" + " " * 15 + "║")
    print("╚" + "═" * 68 + "╝")
    
    # Step 1: Build initial generators
    generators = build_G0_minimal()
    
    # Step 2: Compute closure
    basis, metadata = compute_lie_closure(generators, max_iters=6)
    
    # Step 3: Compute structure constants and Killing form
    struct, K, signature = compute_structure_and_killing(basis)
    
    # Step 4: Save reports
    print_header("SAVING REPORTS")
    
    # Determine output directory
    script_dir = Path(__file__).parent
    reports_dir = script_dir.parent / "reports"
    reports_dir.mkdir(exist_ok=True)
    
    csv_path = reports_dir / "e08_commutator_table.csv"
    md_path = reports_dir / "e08_summary.md"
    
    save_commutator_table(basis, struct, csv_path)
    save_summary_report(basis, metadata, struct, K, signature, md_path)
    
    # Step 5: Final summary
    print_header("EXPERIMENT COMPLETE")
    
    n = len(basis)
    n_pos, n_neg, n_zero = signature
    
    print(f"Final algebra dimension: {n}")
    print(f"Killing form signature: ({n_pos}, {n_neg}, {n_zero})")
    print()
    
    if n == 15:
        print("✓ Dimension matches su(2,2)")
    else:
        print(f"✗ Dimension {n} ≠ 15 (su(2,2) dimension)")
        if n < 15:
            print("  → Generator set may need enrichment")
    
    print()
    print("Reports saved to:")
    print(f"  - {csv_path}")
    print(f"  - {md_path}")
    print()
    
    print("=" * 70)
    print("e08 COMPLETE")
    print("=" * 70)
    print()
    
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
