# Layer-0 Invariant Extraction Analysis

**Task**: `invariant_extraction_from_ubt`  
**Date**: February 16, 2026  
**Status**: ✅ Complete

## Overview

This analysis addresses the formal question: **Are Layer-2 discretization procedures in UBT numerical approximations of Layer-0 invariants, or do they introduce additional physical structure?**

## Documents

### 1. Main Technical Document
**File**: `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` (701 lines, ~31 KB)

**Contents**:
- Rigorous mathematical extraction of 5 Layer-0 invariants
- Noether symmetry analysis of the biquaternionic field Θ(q,τ)
- Formal mapping equations from Layer-2 to Layer-0
- Binary classification with complete proofs
- List of 6 additional postulates in Layer-2

**Compilation**: Will be automatically compiled by GitHub Actions workflow (see `.github/workflows/latex_build.yml`)

**Output**: `FORMAL_INVARIANT_EXTRACTION_LAYER0.pdf` (will be generated in CI)

### 2. Executive Summary
**File**: `INVARIANT_EXTRACTION_SUMMARY.md` (252 lines, ~9 KB)

**Contents**:
- Non-technical overview of findings
- Key results in tabular format
- Scientific implications
- Honest communication guidelines

**Format**: Markdown (human-readable without compilation)

## Key Findings

### Layer-0 Invariants (Rigorously Derived)

1. **Spectral Action**: I_spec[Θ] = Tr[f(D²/Λ²)]
   - Source: Heat kernel expansion of Dirac operator
   
2. **Topological Winding**: I_wind[Θ] = n_wind ∈ ℤ
   - Source: Homotopy class π₃(G/H)
   
3. **Phase Winding**: I_phase[Θ] = K_ψ ∈ ℤ
   - Source: Complex time periodicity
   
4. **Curvature Integral**: I_curv[Θ] = ∫dμ R
   - Source: Gauss-Bonnet theorem
   
5. **Action Functional**: I_action[Θ] = S[Θ]
   - Source: Variational principle

### Layer-2 Analysis

**Prime-Gating**: 
- Origin: Heuristic selection
- NOT symmetry-derived
- NOT topology-derived

**Winding Number n=137**:
- Origin: Empirical calibration to match α⁻¹ ≈ 137.036
- NOT unique stability minimum
- Higher primes (199, 197, 193) score better in stability analysis

**RS(255,201) Code**:
- Origin: Engineering optimization for GF(2⁸)
- NOT derived from field quantization

### Binary Verdict

```
┌─────────────────────────────────────────────────┐
│ Layer-2 Status: ADDED STRUCTURE                │
│                                                 │
│ Layer-2 introduces 6 additional postulates     │
│ beyond Layer-0, not merely numerical approx.   │
└─────────────────────────────────────────────────┘
```

## Additional Postulates in Layer-2

| ID | Description | Status |
|----|-------------|--------|
| L2.1 | Prime restriction on winding numbers | Heuristic |
| L2.2 | Specific choice n=137 | Empirical fit |
| L2.3 | RS(255,201) parameters | Engineering |
| L2.4 | 16 OFDM channels | Design choice |
| L2.5 | Fixed discretization grid | Computational |
| L2.6 | Prime-gating pattern | Parametric scan |

## Scientific Implications

### What This Means

1. **Layer-0 structure is mathematically sound**: Invariants well-defined from fundamental principles

2. **Layer-2 contains modeling choices**: Not uniquely determined by Layer-0

3. **Predictions are semi-empirical**: Require calibration parameters (e.g., n=137)

4. **Still scientifically valid**: But epistemic status clarified (not "parameter-free")

### Honest Communication

**Avoid**:
- ❌ "α⁻¹ = 137 derived from pure geometry with no free parameters"
- ❌ "Prime-gating emerges from fundamental symmetries"

**Use**:
- ✅ "Layer-0 provides spectral and topological invariants"
- ✅ "Layer-2 uses n=137 calibrated to match observations"
- ✅ "Prime-gating is a heuristic selection under investigation"

## Integration with Existing Docs

**Related Documents**:
- `docs/architecture/LAYERS.md` - Layer 1 vs Layer 2 separation
- `consolidation_project/appendix_AA_theta_action.tex` - Action principle
- `THETA_FIELD_DEFINITION.md` - Field structure
- `IMPLEMENTATION_SUMMARY_LAYER2_UBT_MAPPING.md` - Layer-2 implementation
- `forensic_fingerprint/protocols/PROTOCOL_LAYER2_RIGIDITY.md` - Rigidity protocol

## Citation

If referencing this analysis, cite:

```bibtex
@techreport{ubt_invariant_extraction_2026,
  title = {Formal Extraction of Layer-0 Invariant in Unified Biquaternion Theory},
  author = {UBT Theory Development},
  year = {2026},
  month = {February},
  institution = {Unified Biquaternion Theory Repository},
  type = {Technical Analysis},
  url = {https://github.com/DavJ/unified-biquaternion-theory}
}
```

## Future Work

To elevate Layer-2 to Layer-0 (eliminate additional postulates):

1. Prove topological constraint requiring primes
2. Derive n=137 as unique stability minimum
3. Derive RS parameters from field Hilbert space dimensions
4. Derive 16 channels from biquaternionic structure
5. Prove discretization convergence

**Current Status**: None of these derivations completed.

## License

- **Code/Scripts**: MIT License
- **Theoretical Content**: CC BY-NC-ND 4.0
- See `LICENSE.md` for details

## Contact

For questions about this analysis:
- Open issue in repository
- Tag with `theoretical-analysis` label
- Reference `invariant_extraction_from_ubt` task

---

**Last Updated**: February 16, 2026  
**Document Version**: 1.0  
**Repository**: https://github.com/DavJ/unified-biquaternion-theory
