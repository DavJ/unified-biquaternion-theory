# UBT Validation Tools

This directory contains symbolic verification scripts and validation tools for the Unified Biquaternion Theory (UBT).

## Contents

### alpha_symbolic_verification.py

Symbolic verification of the fine-structure constant derivation using SymPy.

**Purpose**: Document assumptions, demonstrate internal consistency, and clearly acknowledge limitations in the α derivation.

**Status**: Template for future rigorous verification. Current UBT formulation includes empirically fitted parameters.

**Usage**:
```bash
python alpha_symbolic_verification.py
```

**Requirements**:
- Python 3.7+
- SymPy (`pip install sympy`)
- NumPy (optional, for numerical checks)
- Matplotlib (optional, for visualization)

**Output**:
- Symbolic expressions for UBT vacuum polarization coefficient
- Numerical comparison with standard QED running
- Documentation of all assumptions and fitted parameters
- Clear statement of limitations

## Important Notes

### Alpha Derivation Status

As documented in `consolidation_project/appendix_P4_alpha_status.tex`, UBT has **NOT** achieved an ab initio derivation of the fine-structure constant α ≈ 1/137.036 from first principles.

Current approach:
- α is treated as an **empirical input** (consistent with Standard Model practice)
- Renormalization factors are **empirically fitted** to match experimental data
- Derivation includes adjustable parameters (N_eff, R_ψ, correction factors)

### Scientific Honesty

These validation tools are designed to:
1. Demonstrate internal mathematical consistency
2. Document all assumptions explicitly
3. Acknowledge limitations and fitted parameters
4. Provide templates for future rigorous verification

They do NOT claim to:
- Derive α from first principles
- Eliminate free parameters
- Provide unique predictions for fundamental constants

## Future Work

Planned extensions:
- [ ] Full one-loop effective action computation
- [ ] Monodromy condition verification on T² torus
- [ ] Chern-Simons invariant calculations
- [ ] Dimensional analysis verification
- [ ] Comparison with experimental α(μ) running from Particle Data Group
- [ ] Extension to strong (g_s) and weak (g_2) couplings

## References

- **Honest assessment**: `consolidation_project/appendix_P4_alpha_status.tex`
- **Symbol disambiguation**: `SYMBOL_B_USAGE_CLARIFICATION.md`
- **Emergent alpha work**: `emergent_alpha_from_ubt.tex`

## Contributing

Improvements to validation scripts are welcome. Please ensure:
- All assumptions are clearly documented
- Limitations are explicitly stated
- Code is well-commented
- Scientific honesty is maintained

## License

These validation tools are part of the UBT repository and are licensed under CC BY 4.0.
