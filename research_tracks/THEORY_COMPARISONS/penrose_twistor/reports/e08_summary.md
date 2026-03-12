# e08: Lie Algebra Audit Summary

## Experiment: Derive su(2,2) from UBT Generators

### Objective

Construct a candidate Lie algebra from UBT-side generators (2×2 biquaternion basis embedded into 4×4 matrices) and test whether the resulting algebra is isomorphic to su(2,2).

### Generator Construction

**Source**: UBT 2×2 biquaternion basis {I, σ₁, σ₂, σ₃}

**Embedding strategies**:
1. Block diagonal: `diag(σ, σ)`
2. Off-diagonal: `[[0, σ], [σ†, 0]]`
3. Upper-left / lower-right blocks
4. Complexified combinations: `i·σ` variants

All generators made traceless (required for su(n,m)).

**Initial generators**: 8

### Closure Computation

**Algorithm**: Iterative commutator closure with basis reduction

**Iterations**: 3

**Dimension growth**: [8, 14, 15, 15]

**Converged**: Yes

### Final Algebra Properties

**Dimension**: 15

**Structure constants**: 156 non-zero

**Killing form signature**: (8, 7, 0)
  - Positive eigenvalues: 8
  - Negative eigenvalues: 7
  - Zero eigenvalues: 0

**Rank(K)**: 15

**Semisimple**: Yes

### Comparison with su(2,2)

**Expected su(2,2) properties**:
- Dimension: 15
- Real form of sl(4,ℂ)
- Non-compact signature (mixed positive/negative eigenvalues)
- Semisimple: det(K) ≠ 0

**Observed vs Expected**:
- Dimension: 15 vs 15
  ✓ **MATCHES su(2,2) dimension**

- Signature: (8, 7, 0) - non-compact ✓

- Semisimple: Yes ✓

### Conclusion

**STRONG INDICATION**: The derived algebra has dimension 15, is semisimple, and has a non-compact signature consistent with su(2,2).

**Further verification needed**:
- Check Lie algebra isomorphism via Cartan classification
- Verify conformal group action on spacetime
- Compare with known su(2,2) representation theory

### Files Generated

- `e08_commutator_table.csv`: Structure constants
- `e08_summary.md`: This report

---

**Experiment**: e08_lie_algebra_audit.py

**Date**: 2026-02-16

