# Electron Mass Dependency Inventory

## Current State Analysis (Pre-Refactor)

### PDG/CODATA Usage in ubt_masses

#### File: `ubt_masses/core.py`

**Function: `ubt_mass_operator_electron_msbar()`**
- **Line 176**: `m_pole_pdg = 0.51099895  # MeV - PDG 2024 experimental value`
- **Status**: USES PDG experimental value directly
- **Context**: Converts PDG pole mass to MSbar using QED correction
- **Issue**: This creates circular reasoning in the derivation chain

**Function: `ubt_alpha_msbar()`**
- **Line 81**: `sector_p = 137` (default value)
- **Status**: Defaults to 137 without explicit theory-based selection
- **Context**: Should require explicit sector_p or call to selector function
- **Issue**: Implicit default masks the theory requirement

### Functions Returning m_e

1. **`ubt_mass_operator_electron_msbar(alpha_mu)`**
   - Returns: MSbar electron mass in MeV
   - Dependencies: 
     - PDG pole mass (0.51099895 MeV) ❌ EXPERIMENTAL
     - alpha_mu (optional, defaults to theory-derived)
     - QED 1-loop correction formula
   
2. **`compute_lepton_msbar_mass(lepton, mu)`**
   - Returns: MSbar lepton mass at scale μ
   - Dependencies:
     - Calls `ubt_mass_operator_electron_msbar()`
     - Calls `ubt_alpha_msbar(mu)` for α(μ)
   
3. **`solve_msbar_fixed_point(initial, lepton)`**
   - Returns: Self-consistent MSbar mass
   - Dependencies:
     - Iterates `ubt_mass_operator_electron_msbar()`
     - Calls `ubt_alpha_msbar()` at each iteration

### Functions Consuming Alpha

1. **`ubt_alpha_msbar(mu, sector_p)`**
   - Returns: α(μ) in MSbar scheme
   - Dependencies:
     - `compute_two_loop_delta()` from alpha_core_repro
     - `alpha_corrected()` from alpha_core_repro
     - sector_p (defaults to 137) ⚠️ SHOULD BE EXPLICIT
   
2. **`ubt_mass_operator_electron_msbar(alpha_mu)`**
   - Uses: α for QED 1-loop correction
   - Dependencies:
     - alpha_mu parameter (optional)
     - Falls back to theory-derived alpha if None

### Default sector_p Usage

**Current defaults:**
- `ubt_alpha_msbar()`: `sector_p = 137` (line 81)
- **Issue**: Should not default; must be explicit or selected by theory rule

### Circular Dependencies Identified

1. **m_e derivation path:**
   ```
   ubt_mass_operator_electron_msbar()
     → uses m_pole_pdg = 0.51099895  ❌ PDG experimental value
     → converts to MSbar using α
   ```

2. **α derivation path:**
   ```
   ubt_alpha_msbar(mu, sector_p=None)
     → defaults to sector_p = 137  ⚠️ Should be explicit
     → uses UBT two-loop calculation (theory-derived) ✓
   ```

3. **Desired non-circular path:**
   ```
   UBT theory primitives (complex time, topology, spectral action)
     → sector_p selection (from theory, not experiment)
     → α(μ) from UBT two-loop
     → m_e from UBT mass operator (no PDG input)
     → Can verify against experimental m_e without circularity
   ```

## Required Changes Summary

### High Priority (Blocks non-circular derivation)
1. ❌ Remove `m_pole_pdg = 0.51099895` from `ubt_mass_operator_electron_msbar()`
2. ⚠️ Remove default `sector_p = 137` from `ubt_alpha_msbar()`
3. ✅ Implement `ubt_select_sector_p()` with explicit theory-based selection rule
4. ✅ Implement theory-derived mass formula in `ubt_mass_operator_electron_msbar()`

### Medium Priority (Completeness)
5. Implement `alpha_from_me()` function to test reverse derivation
6. Add derived_mode/legacy_mode switching for backward compatibility
7. Document all assumptions in audit reports

### Testing Requirements
- Enforce no PDG/CODATA in derived path
- Verify sector_p is explicit or selected by theory
- Test that α does not implicitly default to experimental value
- Validate that m_e → α path is implementable without circularity

## Next Steps
1. Implement `ubt_select_sector_p()` function
2. Replace PDG mass with UBT theory-derived formula
3. Remove implicit sector_p=137 default
4. Add comprehensive tests
5. Update audit reports
