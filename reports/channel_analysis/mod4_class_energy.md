# Mod-4 Class Energy Test Results

## Summary

**Result**: Analysis skipped for all datasets due to insufficient prime data.

## Reason

The mod-4 class energy test requires:
1. Multiple prime numbers in the scan range
2. At least 2 primes in each class (p≡1 mod 4 and p≡3 mod 4)

## Findings

Most datasets in the `scans/` directory fall into one of these categories:

### Category 1: Targeted 137/139 Scans
Files like `*k137_139*.csv` contain **only 2 data points**:
- k=137 (prime, 137 ≡ 1 mod 4)
- k=139 (prime, 139 ≡ 3 mod 4)

With only one prime in each class, statistical testing is impossible.

**Example**: `tt_fft2d_torus_welch_k137_139.csv`
```
Rows: 2
Values: k=137, k=139
Primes: 2 (one per class)
```

### Category 2: Fine-grained Scans
Files like `bb_scan_100_200.csv` contain 600+ rows, but most are **non-integer** values (e.g., 138.402, 138.404).

After filtering to integers:
- Only 3 integer values found
- Only 2 are prime (137, 139)
- Still insufficient for class testing

**Example**: `bb_scan_100_200.csv`
```
Total rows: 604
Integer n: 3
Prime n: 2 (137, 139)
```

### Category 3: Broader Range Scans
Some files cover wider ranges (e.g., `scan_137_128_146.csv`), but the analysis script found:
- Most non-prime values
- Fewer than 10 primes total
- Not enough for reliable permutation testing

## Implications

The current scan data is **optimized for 137/139 comparison**, not for prime class structure analysis.

To properly test the mod-4 hypothesis, we would need:

1. **Broader integer scans**: n ∈ [100, 200] with integer steps
2. **More primes**: At least 20-30 primes to detect class differences
3. **Unbiased protocol**: Not specifically targeting 137/139

## Recommendation

Design new scans specifically for mod-4 testing:
- Scan all integers n ∈ [101, 199]
- Filter to primes post-analysis
- Compare class energies with adequate sample size
- Use multiple protocols (TT, EE, BB) for consistency

## Data Needed

For statistical power at α=0.05 with 80% power:
- Minimum: ~20 primes (10 per class)
- Recommended: ~50 primes (25 per class)
- Range [101-199] contains 20 primes suitable for this test

Primes in [101-199]:
```
101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
```

Classes:
- p≡1 mod 4: 101, 109, 113, 137, 149, 157, 173, 181, 193, 197 (10 primes)
- p≡3 mod 4: 103, 107, 127, 131, 139, 151, 163, 167, 179, 191, 199 (11 primes)

This would provide adequate statistical power.

## Technical Note

The analysis script `analyze_137_139_channels.py` implements the correct methodology:
1. Filter to primes
2. Partition by mod 4
3. Compute class energies
4. Run 10,000 permutations

The issue is purely **data availability**, not methodology.

## Files Analyzed

All 15 datasets were checked:
- 14 files: Only k=137 and k=139 (insufficient)
- 1 file: Broader range but only 2 integer primes found (insufficient)

See `input_inventory.md` for complete list.

---

**Note**: This limitation should be addressed in future experimental design. The current focus on 137/139 comparison is appropriate for Part A (local peak analysis) but prevents testing of broader prime structure hypotheses.
