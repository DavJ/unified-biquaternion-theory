# Alpha Stability Audit - Implementation Summary

## Overview

This document summarizes the comprehensive alpha stability audit implementation that establishes scientific defensibility for UBT's alpha prediction claims.

## What Was Implemented

### 1. Alpha Stability Scan Infrastructure ✅

**Created:**
- `analysis/alpha_stability_scan.py` - Main stability scan tool
- `analysis/stability_metrics.py` - Two independent stability metrics
- `tests/test_alpha_stability_scan.py` - Non-circular test suite
- `docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md` - Analysis documentation

**Key Finding:**
```
n=137 ranks 53/99 in stability metrics
→ NOT a local maximum
→ Better candidates: n=199 (rank 1), 197, 193, 191, 181
→ Conclusion: Layer 2 channel selection, NOT Layer 1 derivation
```

**Usage:**
```bash
python3 -m analysis.alpha_stability_scan --range 101 199 --seed 0
```

### 2. Layer 1 vs Layer 2 Architecture ✅

**Created:**
- `docs/architecture/LAYERS.md` - Comprehensive layer separation contract

**Defines:**
- **Layer 1**: Geometry/topology/dynamics (derived from axioms)
- **Layer 2**: Coding/modulation/protocol (channel selections, engineering choices)

**Key Rule:**
> Layer-2 choices cannot be claimed as derived constants without explicit falsifiable selection principle

**Application to Alpha:**
- Layer 1: Geometric framework α⁻¹ ≈ n + corrections ✅ Derived
- Layer 2: Choice of n=137 specifically ⚠️ Hypothesis/selection

### 3. README Scientific Defensibility ✅

**Updated README.md with:**
- "Derivation Status" column in all quantitative tables
- "What IS and ISN'T Derived Yet" section
- Clear Layer 1 vs Layer 2 separation
- Stability scan results incorporated
- Removed claims of "exact prediction" or "only theory"
- Marked n=137 as "Hypothesis (channel selection, not stability max)"

**Before:**
```markdown
| Fine-structure constant | α⁻¹ = 137.000 | Status: ✅ DERIVED |
```

**After:**
```markdown
| Fine-structure constant (n=137 baseline) | α⁻¹ = 137.000 |
| Derivation Status: **Hypothesis** (channel selection, not stability max) |
```

### 4. OVERVIEW.md Layer Separation ✅

**Updated OVERVIEW.md with:**
- Layer separation notice at top
- Stability scan results in alpha section
- Framework (Layer 1) vs selection (Layer 2) distinction
- Updated status section with honest assessment

## Scientific Integrity Achieved

### Honest Claims

✅ **What we CAN claim:**
- Geometric framework α⁻¹ ≈ n + corrections is derived
- Electron mass baseline from Hopfion topology is derived
- SM gauge group from biquaternionic structure is derived
- n=137 can be used as geometric reference point

✅ **What we CANNOT claim:**
- ❌ n=137 is uniquely derived from first principles
- ❌ n=137 is a stability maximum
- ❌ "Exact prediction" without acknowledging selection
- ❌ "Only theory predicting α" without noting selection

### Falsifiability

The stability scan makes UBT **falsifiable**:
- If n=137 were uniquely stable, scan would show it as maximum
- Scan shows n=137 is NOT maximum → falsifies uniqueness claim
- This is proper science: testable, falsifiable, honest

### Non-Circular Testing

Tests verify:
- ✅ Determinism (same seed → same results)
- ✅ Schema compliance (correct output format)
- ✅ Positive metrics and consistent ranking
- ❌ **DO NOT** test "137 must win" (circular)

## Files Created/Modified

### New Files (9):
1. `analysis/__init__.py`
2. `analysis/alpha_stability_scan.py`
3. `analysis/stability_metrics.py`
4. `tests/test_alpha_stability_scan.py`
5. `docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md`
6. `docs/architecture/LAYERS.md`
7. `scans/alpha_stability_101_199.csv`
8. `scans/alpha_stability_summary.json`
9. `scans/test_scan.csv`

### Modified Files (2):
1. `README.md` - Major updates for scientific defensibility
2. `OVERVIEW.md` - Layer separation and honest assessment

## Verification Commands

### Run Stability Scan
```bash
python3 -m analysis.alpha_stability_scan --range 101 199 --seed 0 --out scans/alpha_stability_101_199.csv
```

### Run Tests
```bash
python3 -m pytest tests/test_alpha_stability_scan.py -v
```

### Check Top Candidates
```bash
head -20 scans/alpha_stability_101_199.csv
```

## Results Summary

### Top 10 Most Stable Candidates (n ∈ [101, 199])

| Rank | n | Prime | Twin Prime | Combined Stability |
|------|---|-------|------------|-------------------|
| 1 | 199 | ✓ | ✓ | 232938 |
| 2 | 197 | ✓ | ✓ | 230189 |
| 3 | 193 | ✓ | ✓ | 224637 |
| 4 | 191 | ✓ | ✓ | 221835 |
| 5 | 181 | ✓ | ✓ | 207576 |
| ... | ... | ... | ... | ... |
| **53** | **137** | **✓** | **✓** | **141215** |

### Interpretation

**n=137 is NOT uniquely selected by stability:**
- Ranks in middle of pack (53/99)
- Larger twin primes consistently score higher
- Even immediate neighbor n=139 is more stable

**Therefore:**
- n=137 is Layer 2 channel selection
- Matches experimental α⁻¹ ≈ 137.036 by calibration
- Geometric framework remains valid
- But specific value n=137 is not derived from stability

## Impact on Documentation

### README.md Table Updates

**Quantitative Predictions:**
- Added "Derivation Status" column
- Marked α baseline as "Hypothesis (channel selection)"
- Marked electron baseline as "Derived (Hopfion topology)"
- Marked corrections as "Partly derived"

**New Section:**
- "What IS and ISN'T Derived Yet"
- Clear Layer 1 / Layer 2 separation
- Honest about hypotheses and selections

### Transparency Documents

All documentation now references:
- `FITTED_PARAMETERS.md` - Authoritative parameter status
- `docs/architecture/LAYERS.md` - Layer separation rules
- `docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md` - Stability analysis

## Comparison: Before vs After

### Before (Overstated)
> "UBT derives α⁻¹ = 137 from pure geometry with no free parameters. This is the only theory achieving exact α prediction from first principles."

### After (Honest)
> "UBT's geometric framework predicts α⁻¹ ≈ n + corrections. The choice of n=137 is a channel selection that matches experimental α⁻¹ ≈ 137.036. Stability analysis shows n=137 is not uniquely selected by stability principles (ranks 53/99; better candidates exist). The geometric framework is derived (Layer 1); the specific value n=137 is a hypothesis/calibration (Layer 2)."

## Recommendations for Future Work

### If n=137 Selection is to be Derived:

Must demonstrate ONE of:
1. **Number-theoretic constraint** that picks n=137 uniquely
2. **Topological obstruction** that forbids other values
3. **Modified stability metric** where n=137 IS maximum
4. **Anthropic/selection principle** with testable consequences

### If n=137 Remains Selection:

Acknowledge honestly:
- "n=137 selected to match experimental α"
- "Geometric framework validated by match"
- "Layer 2 calibration parameter, not Layer 1 constant"

## Conclusion

This implementation achieves **scientific defensibility** through:

1. ✅ **Falsifiable testing** - Stability scan can fail (and did)
2. ✅ **Honest reporting** - n=137 is NOT uniquely stable
3. ✅ **Layer separation** - Clear framework vs selection
4. ✅ **Transparency** - All parameters documented
5. ✅ **Non-circular** - Tests don't assume conclusions

**Result:** UBT documentation is now audit-ready and scientifically honest.

---

**Implementation Date**: February 12, 2026  
**Repository**: DavJ/unified-biquaternion-theory  
**Branch**: copilot/update-honestly-achievements  
**Status**: Complete ✅
