# Channel Analysis Summary

## Overview

This analysis examines 19 scan datasets to determine:
1. Whether signals at n=137 vs n=139 are distinguishable
2. Whether primes p≡1 mod 4 vs p≡3 mod 4 show systematic differences

## Key Findings

### 137 vs 139 Local Peak Comparison

- Analyzed 19 datasets with n=137 data
- Analyzed 18 datasets with n=139 data
- Average signal at 137: 3.331025e-01
- Average signal at 139: 4.458813e-01
- Average ratio (137/139): 0.7471

**Local significance (window ±10):**
- Mean z-score at 137: -1.940
- Mean z-score at 139: 0.966

### Mod-4 Prime Class Test

- Tested 3 datasets
- Significant results (p < 0.05): 1/3 (33.3%)

**Verdict:**

- **MIXED RESULTS**: Some datasets (1/3) show mod-4 class differences, but not consistently across all protocols

## Pipeline Dependencies

Results are pipeline-dependent. Different analysis protocols (TT, EE, BB, FFT, etc.) 
may show different sensitivities to the 137/139 distinction.

See detailed reports:
- `local_137_139_comparison.md` - Full local peak analysis
- `mod4_class_energy.md` - Complete mod-4 class test results
