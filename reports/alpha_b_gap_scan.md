<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Alpha B-gap reproducibility scan

Equation set:
- Stationary condition: `2n = B(log n + 1)`
- Potential: `V_eff(n) = n^2 - B n log n`

## Continuous stationary n*(B)

| case | B | n*(B) |
|---|---:|---:|
| B = 8π | 25.132741 | 65.028843 |
| B = 39 | 39.000000 | 111.407252 |
| B = 46 | 46.000000 | 135.989243 |
| B = B_required(137) | 46.283933 | 137.000000 |
| B = 46.298 | 46.298000 | 137.050103 |

## Required B for selected primes

| prime n | B_required(n) = 2n/(log n + 1) |
|---:|---:|
| 127 | 43.461990 |
| 131 | 44.594247 |
| 137 | 46.283933 |
| 139 | 46.844927 |
| 149 | 49.634021 |
| 151 | 50.188791 |
| 157 | 51.847301 |

## Discrete prime minimizers (range 2..300)

| B | prime minimizer | V_eff(prime minimizer) |
|---:|---:|---:|
| 25.132741 | 67 | -2591.255254 |
| 39.000000 | 113 | -8064.598117 |
| 46.000000 | 137 | -12236.719795 |
| 46.283933 | 137 | -12428.101191 |
| 46.298000 | 137 | -12437.582936 |

## Prime minimizer windows (B sweep 45.0..47.0, step 0.05)

| B_start | B_end | prime minimizer over window |
|---:|---:|---:|
| 45.00 | 45.40 | 131 |
| 45.45 | 46.55 | 137 |
| 46.60 | 47.00 | 139 |

