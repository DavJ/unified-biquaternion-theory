# Alpha Stability Selection Rule: Analysis and Results

## Executive Summary

**Question**: Is α⁻¹ ≈ 137 a derived consequence of stability principles (Layer 1), or an arbitrary channel selection (Layer 2)?

**Answer** (based on stability scan): **Layer 2 channel selection**

The comprehensive stability scan over candidate winding numbers n ∈ [101, 199] reveals that **n=137 is NOT a stability maximum**. It ranks 53/99 in combined stability score, with numerous candidates (especially larger primes) scoring significantly higher.

## Scan Results

### Full Scan Parameters
- Range: n ∈ [101, 199] (99 candidates)
- Metrics: Spectral gap + Robustness under perturbations
- Random seed: 0 (for reproducibility)
- Filter: All integers (primes and composites)

### Top 15 Candidates by Combined Stability

| Rank | n | Prime | Twin Prime | Spectral Gap | Robustness | Combined |
|------|---|-------|------------|--------------|------------|----------|
| 1 | 199 | ✓ | ✓ | -45.94 | 465921 | 232938 |
| 2 | 197 | ✓ | ✓ | -45.48 | 460423 | 230189 |
| 3 | 193 | ✓ | ✓ | -44.55 | 449319 | 224637 |
| 4 | 191 | ✓ | ✓ | -44.09 | 443714 | 221835 |
| 5 | 181 | ✓ | ✓ | -41.78 | 415194 | 207576 |
| ... | ... | ... | ... | ... | ... | ... |
| 53 | **137** | **✓** | **✓** | **-31.61** | **282461** | **141215** |

### Local Maximum Analysis for n=137

- **Target value**: 141214.82
- **Rank**: 53/99 (middle of pack)
- **Window**: ±5
- **Neighbors with higher stability**: 1 (n=139 scores 144300.84)
- **Neighbors with lower stability**: 9

**Conclusion**: n=137 is **NOT** a local maximum. Better candidates exist even in immediate neighborhood (n=139).

## Interpretation

### What This Means

1. **n=137 is not uniquely selected by stability principles**
   - Larger primes (191, 193, 197, 199) consistently score higher
   - Even immediate neighbor n=139 is more stable
   
2. **Current status: Layer 2 channel selection**
   - The choice of n=137 appears to be a coding/modulation parameter
   - Similar to choosing channel 137 in an OFDM system
   - Valid for engineering/protocol purposes
   - **Cannot be claimed as a fundamental derived constant**

3. **Implications for UBT claims**
   - Baseline prediction α⁻¹ = 137.000 should be labeled "Hypothesis" or "Channel selection"
   - NOT "Derived from first principles" without additional selection rule
   - The match to experiment (α⁻¹ ≈ 137.036) remains valid as a geometric anchor
   - But the selection of n=137 specifically is not explained by stability alone

### Alternative Interpretations

If future work identifies a selection principle that picks n=137, candidates include:

1. **Number-theoretic constraint** (e.g., modular arithmetic conditions)
2. **Topological obstruction** (e.g., only n=137 admits consistent winding)
3. **Anthropic constraint** (e.g., only n≈137 allows stable matter)
4. **Experimental calibration** (n=137 chosen to match observed α)

Currently, none of these are demonstrated. The scan suggests **option 4** is most accurate.

## Reproducibility

### Command to Reproduce

```bash
python -m analysis.alpha_stability_scan --range 101 199 --seed 0 --out scans/alpha_stability_101_199.csv
```

### Files Generated

- `scans/alpha_stability_101_199.csv` - Full scan results (n, metrics, ranks)
- `scans/alpha_stability_summary.json` - JSON summary with top candidates and local max analysis

### Test Suite

Run non-circular tests:
```bash
python -m pytest tests/test_alpha_stability_scan.py -v
```

**Important**: Tests do NOT hardcode "n=137 must win". They test:
- Determinism (same seed → same results)
- Schema compliance (correct output format)
- Invariants (positive metrics, consistent ranking)

This ensures the scan is falsifiable and not circular.

## Recommendations for Documentation

### README.md Updates Required

1. **Add "Derivation Status" column** to quantitative predictions table
   - α⁻¹ = 137.000 baseline: "Hypothesis (channel selection)" 
   - α⁻¹ ≈ 137.036 with corrections: "Partly derived (~90%)"

2. **Separate Layer 1 vs Layer 2**
   - Layer 1 (geometry/topology): Biquaternionic structure, GR recovery, SM gauge group
   - Layer 2 (coding/modulation): Channel n=137 selection, OFDM parameters, prime gating
   
3. **Remove claims of "derived from first principles"** for α baseline
   - Replace with: "Geometric anchor at n=137 (channel selection)"
   - Or: "Hypothesis: stability selects n=137 (falsified by scan)"

4. **Add transparency statement**
   - "Stability scan shows n=137 is not a stability maximum"
   - "Current interpretation: Layer 2 channel selection"
   - "Baseline remains valid as geometric reference point"

## Conclusion

The alpha stability scan provides critical scientific honesty:

✅ **What it supports**: n=137 can be used as a geometric reference point
✅ **What it supports**: Multiple approaches converge near α⁻¹ ≈ 137
❌ **What it falsifies**: n=137 is uniquely selected by stability principles
❌ **What it falsifies**: "Derived from first principles" claim for this specific value

**Scientific integrity requires** acknowledging this in all documentation.

---

**Last Updated**: 2026-02-12  
**Scan Version**: v0.1.0  
**Reproducibility**: Full scan artifacts in `scans/` directory  
**Tests**: `tests/test_alpha_stability_scan.py` (non-circular)
