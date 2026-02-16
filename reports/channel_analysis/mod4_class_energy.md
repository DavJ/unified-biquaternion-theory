## Mod-4 Class Energy Test

**Source**: bb_scan_int_100_200.csv
**Signal metric**: psd_obs

### Prime Statistics

- Total primes analyzed: 21
- Class C1 (p≡1 mod 4): 10 primes
- Class C3 (p≡3 mod 4): 11 primes

### Energy Analysis

**Raw Energy:**
- E(C1) = 1.548392e+01
- E(C3) = 1.466743e+01
- ΔE = E(C1) - E(C3) = 8.164962e-01

**Z-score Energy (robust):**
- E_z(C1) = 2.187421e+01
- E_z(C3) = 1.471030e+01
- ΔE_z = 7.163901e+00

### Permutation Test Result

- Number of permutations: 10000
- Observed |ΔE|: 8.164962e-01
- p-value (two-tailed): 8.377000e-01

**Interpretation:**

- **Verdict**: NOT SIGNIFICANT
- No significant difference detected between mod-4 classes (p = 8.377000e-01)


---

## Mod-4 Class Energy Test

**Source**: ee_scan_int_100_200.csv
**Signal metric**: psd_obs

### Prime Statistics

- Total primes analyzed: 21
- Class C1 (p≡1 mod 4): 10 primes
- Class C3 (p≡3 mod 4): 11 primes

### Energy Analysis

**Raw Energy:**
- E(C1) = 1.026663e+01
- E(C3) = 1.332807e+01
- ΔE = E(C1) - E(C3) = -3.061443e+00

**Z-score Energy (robust):**
- E_z(C1) = 1.161903e+01
- E_z(C3) = 2.287431e+01
- ΔE_z = -1.125527e+01

### Permutation Test Result

- Number of permutations: 10000
- Observed |ΔE|: 3.061443e+00
- p-value (two-tailed): 0.000000e+00

**Interpretation:**

- **Verdict**: SIGNIFICANT
- The difference between mod-4 classes is statistically significant (p < 0.01)


---

## Mod-4 Class Energy Test

**Source**: tt_scan_int_100_200.csv
**Signal metric**: psd_obs

### Prime Statistics

- Total primes analyzed: 21
- Class C1 (p≡1 mod 4): 10 primes
- Class C3 (p≡3 mod 4): 11 primes

### Energy Analysis

**Raw Energy:**
- E(C1) = 2.330986e+01
- E(C3) = 2.471256e+01
- ΔE = E(C1) - E(C3) = -1.402704e+00

**Z-score Energy (robust):**
- E_z(C1) = 1.983132e+01
- E_z(C3) = 1.955340e+01
- ΔE_z = 2.779170e-01

### Permutation Test Result

- Number of permutations: 10000
- Observed |ΔE|: 1.402704e+00
- p-value (two-tailed): 9.755000e-01

**Interpretation:**

- **Verdict**: NOT SIGNIFICANT
- No significant difference detected between mod-4 classes (p = 9.755000e-01)
