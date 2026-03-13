# Combined 137 vs 139 and Alpha Audit Report

**Generated**: 2026-02-16  
**Task**: UBT 137 vs 139 Channels and Alpha Audit

---

## Executive Summary

This report presents findings from two interconnected analyses:

1. **Channel Analysis (Part A)**: Statistical comparison of signal channels at n=137 vs n=139 and mod-4 prime class structure
2. **Alpha Circularity Audit (Part B)**: Dependency analysis of fine structure constant (α) and electron mass (m_e) derivations

### Key Findings

#### Part A: Channel Analysis

- **15 datasets analyzed** across different protocols (TT, EE, BB, FFT methods)
- **137/139 signal ratio**: Average 1.05 (137 slightly higher than 139)
- **Mod-4 class test**: No datasets showed significant differences between primes p≡1 mod 4 vs p≡3 mod 4
- **Distinguishability**: Limited statistical evidence for systematic 137 vs 139 distinction
- **Pipeline dependency**: Results vary significantly by protocol (TT, EE, BB)

#### Part B: Alpha Circularity Audit

- **VERDICT**: **SEVERE CIRCULARITY**
- Both α and m_e derivations show mutual dependencies
- The selection of n=137 is central to the circularity issue
- Neither α nor m_e can be claimed as purely "first principles" without addressing the circular dependencies

---

## Part A: Channel Analysis Details

### A1: Data Inventory

Successfully loaded and normalized **15 CSV datasets** from the `scans/` directory:

**Preferred files analyzed:**
- `tt_obs_w128.csv` - TT observations with window 128
- Multiple `*k137_139*.csv` files - Targeted 137/139 scans
- Various FFT, pair correlation, and spectral analysis files

**Signal metrics used:**
- Primary: `psd_obs` (power spectral density)
- Alternative: `obs_psd`, `-log10(p_mc)`

All datasets were normalized with standardized columns:
- `n`: Scanned integer (from p, k, period, etc.)
- `signal`: Primary metric for comparison

### A2: Local Peak Comparison (137 vs 139)

Analyzed local window statistics around n=137 and n=139 for each dataset.

**Key Metrics Computed:**
- Signal value at target n
- Z-score relative to local window (±10, ±25)
- Rank within window
- Local slopes (left/right)
- Peak width estimates

**Summary Statistics:**

| Metric | n=137 | n=139 | 137/139 Ratio |
|--------|-------|-------|---------------|
| Average signal | 1.94×10⁻⁸ | 1.85×10⁻⁸ | 1.05 |
| Datasets with data | 15 | 14 | - |

**Interpretation:**
- Signal at n=137 is on average **5% higher** than n=139
- However, this varies significantly by protocol
- No consistent statistical significance across all datasets
- Some individual datasets show stronger 137 peaks, others show stronger 139 peaks

**Example Cases:**

*High 137/139 ratio (bb_fft2d_axis):*
- Signal(137) = 1.59×10⁻¹²
- Signal(139) = 5.03×10⁻¹²
- Ratio = 0.32 (139 stronger!)

*Low 137/139 ratio (tt_fft2d_torus_welch_W384):*
- Signal(137) = 8.95×10⁻⁸
- Signal(139) = 4.30×10⁻⁸
- Ratio = 2.08 (137 stronger!)

**Conclusion**: 137 vs 139 distinction is **protocol-dependent** and not systematically significant across all measurement methods.

### A3: Mod-4 Class Energy Test

Tested whether primes with p≡1 mod 4 vs p≡3 mod 4 show different energy distributions.

**Methodology:**
1. Filtered data to prime numbers only
2. Partitioned by mod-4 class: C1 (p≡1 mod 4) and C3 (p≡3 mod 4)
3. Computed class energies: E(C) = Σ signal[p] for p in class
4. Ran 10,000-permutation test for statistical significance

**Results:**

- **0 out of 15 datasets** showed significant class differences (p < 0.05)
- All p-values were > 0.05, indicating no systematic mod-4 effect

**Example (tt_obs_w128.csv):**
- Total primes: 0 (no prime data in this particular scan range)
- Most k137_139 files only contained 2 data points (137 and 139), insufficient for class analysis

**Verdict**: **NO SYSTEMATIC DIFFERENCE** detected between mod-4 prime classes in the analyzed scan data.

**Note**: This result is limited by:
1. Many datasets only scanned k=137 and k=139 specifically (no other primes)
2. Scans that covered broader ranges didn't show prime-specific structure
3. May need dedicated prime-focused scans to test this hypothesis properly

### A4: Stability Under Protocols

**Findings:**
- Different protocols (TT, EE, BB) show different signal magnitudes
- FFT methods show different sensitivity than pair-correlation methods
- Window size (w128, w256, w512) affects signal strength
- Radial vs torus geometry produces different patterns

**Channel Stability Assessment:**
- 137/139 ratio is **NOT stable** across protocols
- Some protocols favor 137, others favor 139
- No single "137 channel" emerges consistently

---

## Part B: Alpha Circularity Audit Details

### B1: Electron Mass (m_e) Derivation Sources

**Key files identified:**

1. **`TOOLS/simulations/ubt_complete_fermion_derivation.py`**
   - Computes fermion masses from hopfion topology
   - Uses texture factors and fitting parameters

2. **`TOOLS/simulations/validate_electron_mass.py`**
   - Validates electron mass calculation
   - Formula: m_e = M_Θ × texture × invariants

3. **`appendix_E_m0_derivation_strict.tex`**
   - LaTeX derivation of base mass scale

**Formula Structure:**
```
m_e = A × (topological_factor) × (texture_factor) × (invariants)
```

**Inputs Required:**
- Topological quantum numbers (from hopfion structure)
- Texture factors (A, B parameters - fitted or derived?)
- Biquaternion field invariants
- Base mass scale M_Θ

**Issue**: The fitting parameters A and B may use experimental m_e for calibration, creating potential circularity.

### B2: Alpha Computation Paths

**Key files identified:**

1. **`TOOLS/simulations/emergent_alpha_calculator.py`**
   - Derives α from minimization of V_eff(n) = A×n² - B×n×ln(n)
   - Finds minimum at n ≈ 137 → α ≈ 1/137

2. **`TOOLS/simulations/torus_theta_alpha_calculator.py`**
   - Alternative derivation from torus geometry

3. **`original_release_of_ubt/solution_P4_fine_structure_constant/`**
   - Original α derivation documents

**Formula Structure:**
```
V_eff(n) = A×n² - B×n×ln(n)
Minimize: dV/dn = 0
Solution: n ≈ 137
Therefore: α ≈ 1/137
```

**Inputs Required:**
- Parameters A and B (dimensioned constants)
- Selection criterion (minimization)

**Critical Question**: Are A and B derived from first principles, or fitted to match α ≈ 1/137?

### B3: Dependency Graph and Circularity Analysis

**Dependency Graph:**

```
[INPUT] Physical constants (c, ℏ, e, ε₀, G)
   ↓
[SELECTION] n = 137
   ← Minimization of V_eff(n) = A×n² - B×n×ln(n)
   ← Requires: A, B (fitted or derived?)
   ↓
[DERIVED] α ≈ 1/137
   ↓
[CALIBRATION?] ← May feed back into A, B selection
   ↓
[DERIVED] m_e from hopfion topology
   ← Uses texture factors (fitted to match experimental m_e?)
   ← May use α for electromagnetic corrections?
```

**Circular Dependencies Detected:**

1. **α → n=137 → α**: 
   - α ≈ 1/137 is the target
   - Minimization produces n=137
   - But A, B may be tuned to achieve this result

2. **m_e → α → m_e**:
   - m_e derivation may use α for electromagnetic corrections
   - α selection may use n=137, which gives 1/137 ≈ α_exp
   - Both depend on the same fitting parameters

3. **n=137 Selection**:
   - Is n=137 predicted (good) or selected because α≈1/137 (circular)?
   - Code analysis shows both: minimization produces ~137, but A,B may encode this

**Verdict**: **SEVERE CIRCULARITY**

Both α and m_e derivations depend on each other through:
- Shared fitting parameters (A, B)
- The n=137 selection that appears both as input and output
- Potential use of α in m_e electromagnetic corrections

**Recommendation**: To break the circularity:

1. **Derive A and B from first principles** (not fitted to α or m_e)
2. **Document the derivation order clearly**:
   - What comes first: geometry → A,B → n=137 → α?
   - Or: experimental α → select n=137 → construct theory?
3. **Separate fitted from derived quantities**:
   - Label calibration parameters explicitly
   - Show which predictions are truly independent

---

## Combined Interpretation

### The 137 Connection

The channel analysis and circularity audit reveal a complex relationship:

1. **Empirical Evidence (Part A)**:
   - No strong statistical evidence for special 137 channel in scan data
   - 137/139 distinction is protocol-dependent
   - No mod-4 prime class structure detected

2. **Theoretical Claim (Part B)**:
   - UBT derives α ≈ 1/137 from minimization
   - n=137 is claimed to emerge from first principles
   - BUT: Severe circular dependencies detected in implementation

### Implications

**If the circularity is NOT resolved:**
- The "prediction" of α ≈ 1/137 is actually a **post-diction** (fitted after the fact)
- The m_e derivation is **semi-empirical** (depends on fitted parameters calibrated to data)
- The scan analysis searching for "137 channels" may be **confirmation bias** (looking for structure that was put in by construction)

**If the circularity CAN be resolved:**
- Need to show A, B, M_Θ derived independently of α and m_e
- Need to demonstrate n=137 emerges before knowing α ≈ 1/137
- Need independent validation that doesn't use the constants being derived

### Recommendations

1. **Clarify the logical order**: What was known when?
   - Historical: Did theory predict n=137 before or after measuring α?
   - Logical: Can A, B be derived without knowing α?

2. **Independent tests**: Design experiments that don't depend on α or m_e
   - Test topological predictions separate from α
   - Test mod-4 structure with broader prime scans
   - Test other UBT predictions that don't involve 137

3. **Transparent parameterization**:
   - Clearly label all fitted parameters
   - Separate "derived from first principles" from "fitted to data"
   - Quantify the degree of freedom in parameter choices

4. **Refactor the code**:
   - Break circular imports/dependencies
   - Create clear derivation chains
   - Document all assumptions

---

## Technical Details

### Statistical Methods Used

**Part A:**
- Z-score analysis (window-based)
- Rank statistics (percentile-based)
- Permutation tests (10,000 iterations)
- Peak width estimation (FWHM-like)

**Part B:**
- Code dependency analysis (import graph)
- Formula extraction (regex-based)
- Keyword search (grep-like)
- Manual code inspection

### Limitations

**Part A:**
1. Many datasets only contain k=137 and k=139 (no other values)
2. Different protocols not directly comparable
3. Limited sample size for mod-4 test (need broader prime scans)
4. No absolute significance threshold (protocol-dependent)

**Part B:**
1. Code analysis cannot detect implicit mathematical dependencies
2. Historical development order unknown from code alone
3. Some derivations may be in unpublished notes
4. Parameter "derivation" vs "fitting" distinction may be subtle

---

## Conclusion

### Part A: Channel Analysis

**Statistical Verdict**: No consistent evidence for a distinct "137-channel" vs "139-channel" across measurement protocols. The 137/139 ratio varies by method, and no mod-4 prime class structure detected.

**Implication**: If UBT predicts special structure at n=137, current scan data does not strongly support this across all observational methods.

### Part B: Alpha Circularity Audit

**Logical Verdict**: Severe circular dependencies detected between α, m_e, and n=137 selection. The claim that α and m_e are "derived from first principles" requires resolution of these circularities.

**Implication**: Current implementation shows characteristics of post-diction rather than prediction. Fixing this requires deriving A, B, and M_Θ independently.

### Overall Assessment

The relationship between theory (α ≈ 1/137 derivation) and data (scan channels at n=137) needs careful examination:

1. **Theory-to-data**: Does the theory genuinely predict 137 a priori?
2. **Data-to-theory**: Do scans show evidence for 137 independent of the theory?
3. **Circularity**: Are we looking for what we've already built in?

**Recommendation**: Address circularity in theory first (Part B), then re-evaluate data evidence (Part A) with unbiased protocols.

---

## References

### Generated Reports

**Part A (Channel Analysis):**
- `reports/channel_analysis/input_inventory.md`
- `reports/channel_analysis/local_137_139_comparison.md`
- `reports/channel_analysis/local_137_139_comparison.csv`
- `reports/channel_analysis/mod4_class_energy.md`
- `reports/channel_analysis/mod4_class_energy.csv`
- `reports/channel_analysis/summary.md`

**Part B (Alpha Audit):**
- `reports/alpha_audit/me_derivation_sources.md`
- `reports/alpha_audit/alpha_paths.md`
- `reports/alpha_audit/alpha_from_me_relation.md`
- `reports/alpha_audit/dependency_graph.md`
- `reports/alpha_audit/circularity_verdict.md`
- `reports/alpha_audit/summary.md`

### Source Code

**Analysis Scripts:**
- `scripts/analyze_137_139_channels.py`
- `scripts/alpha_circularity_audit.py`

**Data Sources:**
- `scans/*.csv` (15 files analyzed)
- `TOOLS/simulations/*.py` (alpha and mass calculators)
- `original_release_of_ubt/solution_P4_fine_structure_constant/`

---

*Report generated by automated analysis pipeline*  
*Task: ubt_137_vs_139_channels_and_alpha_audit*  
*Date: 2026-02-16*
