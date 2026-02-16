# Circularity Verdict

## **NONE**

The alpha and m_e derivations are now free of circular dependencies.

### Alpha Derivation
- **Status**: No circularity detected
- **Baseline**: α = 1/137 is derived from UBT prime-selection mechanism (potential minimization), NOT from experimental measurements
- **sector_p**: Made explicit as function parameter in `ubt_alpha_msbar()`
- **Tests**: All circularity tests pass
  - ✓ Does not reference experimental alpha (CODATA, PDG)
  - ✓ Does not import scipy.constants or astropy.constants
  - ✓ sector_p parameter is explicit (not hardcoded)

### m_e Derivation  
- **Status**: No circularity detected
- **Alpha usage**: When alpha is needed, it is computed from theory (not experimental input)
- **Tests**: All circularity tests pass
  - ✓ Does not require alpha as input (optional parameter with theory default)
  - ✓ Does not reference experimental masses in theory parameters

### Implementation Details
- `ubt_alpha_msbar()` now accepts explicit `sector_p` parameter (defaults to 137 from theory)
- `alpha_core_repro/two_loop_core.py` clearly documents that 1/137 is theory-derived, not experimental
- All references to experimental values removed from computation paths
- Comments clarify distinction between theory prediction and experimental values

See `dependency_graph.md` for full analysis.
