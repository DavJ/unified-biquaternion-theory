# 137 vs 139 Channel Analysis and Alpha Audit

This directory contains the results of a comprehensive analysis addressing two key questions about the Unified Biquaternion Theory (UBT):

1. **Is there statistical evidence for distinct 137 vs 139 channels?**
2. **Does the theory derive α and m_e without circular reasoning?**

## Quick Links

- **[Combined Report](combined_137_139_and_alpha_audit.md)** - Full analysis with both parts
- **[Channel Analysis Summary](channel_analysis/summary.md)** - Part A findings
- **[Alpha Circularity Verdict](alpha_audit/circularity_verdict.md)** - Part B verdict

## Executive Summary

### Part A: Channel Analysis

**Objective**: Determine if scan-derived spectral signatures support distinct "137-channel" vs "139-channel" and whether primes with p≡1 mod 4 vs p≡3 mod 4 show systematic differences.

**Key Findings**:
- Analyzed 15 datasets across different protocols (TT, EE, BB, FFT methods)
- Average 137/139 signal ratio: 1.05 (137 slightly higher)
- **No consistent statistical significance** across all protocols
- **No mod-4 prime class structure** detected (0/15 datasets showed significance)
- Results are **highly protocol-dependent**

**Verdict**: No strong evidence for a universally distinct "137-channel" in the analyzed scan data.

### Part B: Alpha Circularity Audit

**Objective**: Verify whether UBT derives m_e from first principles and computes α from m_e without circular reasoning.

**Key Findings**:
- Both α and m_e derivations show **mutual dependencies**
- α derivation uses m_e in some calculations
- m_e derivation uses α in some calculations
- Both depend on selection of n=137, which itself comes from α≈1/137
- Parameters A, B in V_eff(n) may be fitted rather than derived

**Verdict**: **SEVERE CIRCULARITY** detected. Neither α nor m_e can be claimed as purely "first principles" derivation without addressing these circular dependencies.

## Structure

```
reports/
├── combined_137_139_and_alpha_audit.md    # Main combined report
├── channel_analysis/
│   ├── summary.md                          # Part A summary
│   ├── input_inventory.md                  # Data sources catalog
│   ├── local_137_139_comparison.md         # Detailed peak analysis
│   ├── local_137_139_comparison.csv        # Comparison data table
│   └── mod4_class_energy.md                # Mod-4 class test results
└── alpha_audit/
    ├── summary.md                           # Part B summary
    ├── circularity_verdict.md               # One-line verdict
    ├── dependency_graph.md                  # Full dependency analysis
    ├── me_derivation_sources.md             # Electron mass sources
    ├── alpha_paths.md                       # Alpha computation paths
    └── alpha_from_me_relation.md            # α-m_e relationship analysis
```

## Methodology

### Part A: Statistical Analysis

1. **Data Loading**: Normalized 15 CSV files from `scans/` directory
   - Standardized columns: n (scanned integer), signal (primary metric)
   - Used psd_obs, obs_psd, or -log10(p_mc) as signal

2. **Local Peak Comparison**:
   - Computed window statistics (±10, ±25) around n=137 and n=139
   - Calculated z-scores, ranks, slopes, peak widths
   - Generated side-by-side comparison tables

3. **Mod-4 Class Test**:
   - Filtered to prime numbers only
   - Partitioned by p≡1 mod 4 (C1) vs p≡3 mod 4 (C3)
   - Computed class energies: E(C) = Σ signal[p]
   - Ran 10,000-permutation test for significance

4. **Stability Analysis**:
   - Compared results across different protocols (TT, EE, BB)
   - Tested FFT vs pair-correlation methods
   - Checked window size effects (w128, w256, w512)

### Part B: Code Analysis

1. **m_e Derivation Search**:
   - Grep-based search for "m_e", "electron mass", "0.51 MeV"
   - Identified key files: hopfion derivations, fermion calculators
   - Extracted formulas and input requirements

2. **α Computation Search**:
   - Searched for "alpha", "fine structure", "1/137"
   - Identified minimization procedures: V_eff(n) = A×n² - B×n×ln(n)
   - Documented parameter dependencies

3. **Dependency Graph**:
   - Mapped: constants → parameters → n=137 → α → m_e
   - Flagged circular edges: α→m_e, m_e→α, n=137↔α
   - Analyzed code for implicit dependencies

4. **Circularity Verdict**:
   - Checked if α uses m_e (YES)
   - Checked if m_e uses α (YES)
   - Checked if n=137 is input or output (MIXED)
   - Assessed severity: SEVERE (bidirectional circularity)

## Detailed Findings

### 137 vs 139 Comparison

Example results from different protocols:

| Dataset | Signal(137) | Signal(139) | Ratio |
|---------|-------------|-------------|-------|
| bb_fft2d_torus_welch | 1.24×10⁻¹¹ | 1.04×10⁻¹¹ | 1.19 |
| tt_fft2d_torus_welch_W384 | 3.09×10⁻⁸ | 3.20×10⁻⁸ | 0.97 |
| tt_obs_w128 | 3.50×10⁻⁸ | 3.16×10⁻⁸ | 1.11 |

**Observation**: Some protocols favor 137, others favor 139. No universal pattern.

### Circular Dependency Chain

```
n=137 selection
  ↓
α ≈ 1/137 (from minimization with parameters A, B)
  ↓
m_e derivation (may use α for EM corrections)
  ↓
Calibration of A, B? (may use experimental α, m_e)
  ↑_______________|
   circular loop
```

## Recommendations

### For Part A (Channel Analysis)

1. **Broader scans**: Include more prime values (not just 137, 139)
2. **Independent protocols**: Design tests that don't assume 137 is special
3. **Systematic parameter sweeps**: Test across all n∈[100,200]
4. **Blind analysis**: Analyze without knowing which n corresponds to α≈1/137

### For Part B (Circularity)

1. **Break the loop**:
   - Derive A, B from pure geometry (no fitting to α or m_e)
   - Show n=137 emerges independently
   - Compute α and m_e without cross-dependencies

2. **Document order**:
   - Clarify historical: was n=137 predicted before measuring α?
   - Clarify logical: can we compute A, B without knowing α?

3. **Separate fitted from derived**:
   - Label all calibrated parameters explicitly
   - Distinguish predictions from post-dictions
   - Quantify degrees of freedom in parameter choices

4. **Independent validation**:
   - Test UBT predictions that don't involve α or m_e
   - Look for other emergent numbers (not 137)
   - Cross-validate against unrelated experiments

## Running the Analysis

The analysis can be reproduced using:

```bash
# Channel analysis
python3 scripts/analyze_137_139_channels.py

# Alpha circularity audit
python3 scripts/alpha_circularity_audit.py
```

Requirements: `numpy`, `pandas`, `scipy`, `tabulate`

## Citations

If you use these results, please cite:

- Analysis scripts: `scripts/analyze_137_139_channels.py`, `scripts/alpha_circularity_audit.py`
- Data sources: `scans/*.csv` (15 datasets)
- UBT code: `TOOLS/simulations/emergent_alpha_calculator.py` and related files

## Authors

Analysis performed by: GitHub Copilot Workspace (automated analysis)  
Date: 2026-02-16  
Task: ubt_137_vs_139_channels_and_alpha_audit  
Repository: DavJ/unified-biquaternion-theory

## License

Copyright (c) 2025 Ing. David Jaroš  
Licensed under the MIT License
