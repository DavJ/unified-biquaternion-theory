# UBT Comparison Harness

## Purpose

This directory provides tools and protocols for **systematic A/B comparison** between the two first-class formulations of Unified Biquaternion Theory (UBT):

1. **UBT with Chronofactor** (`ubt_with_chronofactor/`) - Uses complex time τ = t + iψ as external evolution parameter
2. **UBT without Chronofactor** (`ubt_no_chronofactor/`) - All phase information intrinsic to 8D field Θ(q)

## The Open Question

**What is the physical meaning of the chronofactor?**

The chronofactor formulation uses τ = t + iψ as a foundational parameter, which raises conceptual questions:
- Is ψ an observer-dependent phase or a universal field?
- How does ψ evolve dynamically?
- Is it a mathematical convenience or a physical degree of freedom?

The chronofactor-free formulation addresses these questions by making all phase information **intrinsic** to the 8D biquaternionic field structure.

## Comparison Protocol

### Goal

To determine which formulation:
1. Provides cleaner conceptual foundations
2. Makes more testable predictions
3. Better matches observational data
4. Offers simpler derivations

### Methodology

1. **Identify Shared Invariants** - Physical observables that both formulations must predict (see `invariants.md`)
2. **Map Objects Between Formulations** - Establish correspondence between mathematical structures (see `mapping_table.md`)
3. **Run Parallel Derivations** - Derive the same observables in both formulations
4. **Compare Results** - Check for consistency and identify where predictions differ

### What Must Match

Both formulations should predict:
- General Relativity in appropriate limits
- Standard Model gauge structure (SU(3) × SU(2) × U(1))
- Fine structure constant α ≈ 1/137
- Electron mass m_e ≈ 0.51 MeV
- CMB power spectrum features

### What May Differ

- Mathematical complexity of derivations
- Conceptual clarity
- Additional predictions (e.g., dark sector physics)
- Computational tractability

## Experimental Protocol

### Running A/B Comparison

```bash
# Extract observable from chronofactor formulation
cd ../ubt_with_chronofactor
python scripts/extract_observable.py --observable alpha

# Extract same observable from chronofactor-free formulation  
cd ../ubt_no_chronofactor
python scripts/extract_observable.py --observable alpha

# Compare results
cd ../ubt_compare
python scripts/compare_observables.py --observable alpha
```

### Invariant Validation

```bash
# Validate that both formulations respect shared invariants
cd ubt_compare/scripts
python validate_invariants.py --formulation1 with_chronofactor --formulation2 no_chronofactor
```

## Status

- **Chronofactor formulation**: ✅ Complete with papers, experiments, forensic fingerprint
- **Chronofactor-free formulation**: 🚧 Core derivations in progress
- **Comparison harness**: 🚧 Initial scaffolding complete

## Research Position

The **meaning of the chronofactor is an open research question**. This comparison harness does not prejudge the answer. Both formulations are maintained as first-class alternatives to enable:

1. Systematic comparison
2. Independent verification
3. Identification of conceptual advantages
4. Empirical testing

The research community can evaluate both approaches and determine which provides a better foundation for unified physics.

## Files in This Directory

- `README.md` (this file) - Overview and experimental protocol
- `invariants.md` - List of shared physical invariants
- `mapping_table.md` - Object correspondence between formulations
- `scripts/` - Python tools for automated comparison (future)

## License

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0

This comparison framework is part of the UBT research project and is released under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
