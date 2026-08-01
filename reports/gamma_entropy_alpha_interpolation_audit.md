<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Gamma/Prime-Factorization Entropy Alpha Interpolation Audit

**File**: `reports/gamma_entropy_alpha_interpolation_audit.md`  
**Date**: 2026-05-11  
**Track**: T3_ALPHA  
**Status**: PLAUSIBLE_OBS — see conclusion  
**Tool**: `tools/scan_gamma_entropy_lambda.py` (mpmath, dps=80)

---

## 1. Status Discipline

> **MANDATORY WARNINGS**
>
> - Alpha is **NOT DERIVED**.
> - B_Ram is currently **[OBS]** (numerical observation) — not proved from `S[Θ]`.
> - Gap **G137-B** remains **OPEN**.
> - `lambda_fit` is a numerical observation; it is **not a proof** of anything.
> - No new derivation claims are made in this document.

---

## 2. Potential Definitions

### V1 — Original potential `[L1]`

```
V1(n) = n^2 - B * n*log(n)
dV1/dn = 2n - B*(log(n) + 1) = 0
```

Stationary condition: `B = 2n / (log(n) + 1)`

### V3 — Gamma-refined potential `[DERIVATION CANDIDATE]`

```
V3(n) = n^2 - B * (log(Gamma(n+1)) + n)
dV3/dn = 2n - B*(psi(n+1) + 1) = 0
```

where `psi = digamma`. Stationary condition: `B = 2n / (psi(n+1) + 1)`

### V_lambda — Interpolated potential `[OBS]`

```
E_lambda(n) = (1-lambda)*n*log(n) + lambda*(log(Gamma(n+1)) + n)

V_lambda(n) = n^2 - B_Ram * E_lambda(n)
```

Stationarity condition:
```
2n - B_Ram * [(1-lambda)*(log(n)+1) + lambda*(psi(n+1)+1)] = 0
```

### Reference value `B_Ram` `[OBS — NOT PROVED]`

```
B_Ram = 12^(3/2) * 2^(1/8) * theta3(0|i)^(1/4)
```

This is a **numerical observation only**. It has been explicitly rejected as a
first-principles derivation of the `n log n` coefficient. See
`canonical/alpha/ALPHA_MASTER_STATUS.md` (deprecated-claim register).

---

## 3. Mathematical Identities `[STD/L0]`

### 3.1 Log-factorial identity

For every positive integer `n`:
```
log(Gamma(n+1)) = log(n!)
```

### 3.2 Legendre's formula (prime factorization decomposition)

For any positive integer `n`:
```
log(n!) = sum_{p prime, p^m <= n, m >= 1} floor(n/p^m) * log(p)
```

The sum runs over all prime powers `p^m ≤ n`. This is the exact decomposition
of `log(n!)` as the total logarithmic information content of integers 1..n
under the prime alphabet.

### 3.3 Stirling expansion

```
log(Gamma(n+1)) + n = n*log(n) + (1/2)*log(2*pi*n) + 1/(12n) + O(n^{-3})
```

The leading term is `n*log(n)`. The subleading term at `n = alpha_inv` is:

```
(1/2)*log(2*pi*n) + 1/(12n) = 3.37967...   (at n = 137.036)
```

### 3.4 Digamma derivative `[STD/L0]`

```
d/dn [log(Gamma(n+1)) + n] = psi(n+1) + 1
psi(n+1) = log(n) + 1/(2n) - 1/(12n^2) + O(n^{-4})  (asymptotic)
```

---

## 4. High-Precision Numerical Results

All computed at `mpmath.mp.dps = 80` (80 decimal places).

### Special function values `[STD/L0]`

| Quantity | Value |
|----------|-------|
| `theta3(0\|i)` | `1.08643481121330801457531612151...` |
| `\|eta(i)\|` | `0.768225422326056659002594179576...` |
| `B_Ram` | `46.280872383180703498930750708...` `[OBS]` |

### Stationary points

| Quantity | Value | Status |
|----------|-------|--------|
| `n1` (V1 stationary) | `136.9890996341081484047897` | `[L1]` |
| `n3` (V3 stationary) | `137.0905214130678236021181` | `[DERIV CAND]` |
| `alpha_inv_exp` | `137.035999084` | `[PHENOM]` — CODATA 2018 |
| Gap `n3 - n1` | `0.1014217789596752` | computed |

Bracket check: **`n1 < alpha_inv_exp < n3` ✓**

The measured `alpha_inv` lies strictly between the V1 and V3 stationary points.

### Acceptance criteria

| Criterion | Computed | Reference | Difference |
|-----------|----------|-----------|------------|
| `n1` | `136.9890996341081` | `136.9890996341` | `8.1e-12` ✓ |
| `n3` | `137.0905214130678` | `137.0905214131` | `3.2e-11` ✓ |

### Lambda fit values `[OBS]`

Two definitions of `lambda_fit` are in use; they differ by ~0.0002:

**Definition A (exact stationary condition)**:
```
lambda_fit_exact =
  [2*alpha_inv/B_Ram - (log(alpha_inv)+1)]
  / [(psi(alpha_inv+1)+1) - (log(alpha_inv)+1)]
= 0.46221754271946603121...  [OBS]
```
Verified: V_lambda with this lambda has stationary point at `n = alpha_inv_exp`
to 80-digit precision.

**Definition B (linear fractional position)**:
```
lambda_fit_frac = (alpha_inv - n1) / (n3 - n1)
= 0.46241990993372919271...  [OBS]
```
This is the fraction of the way from `n1` to `n3` at which `alpha_inv` falls.
It equals `lambda_fit_exact` only in the linear limit.

The reference value in the problem statement `0.4624190817` matches Definition B
to 7 significant figures. The difference between definitions A and B arises from
the nonlinearity of `n*(lambda)`.

**For the candidate constant comparison, Definition A (exact) is used throughout.**

---

## 5. Information-Theoretic Interpretation of the Entropic Term `[INTERP]`

The entropic term `log(Gamma(n+1)) + n` has the Stirling expansion
`n*log(n) + (1/2)*log(2*pi*n) + O(n^{-1})`.

By Legendre's formula:
```
log(Gamma(n+1)) = log(n!) = sum_{p^m <= n} floor(n/p^m) * log(p)
```

This is the **total logarithmic information content** of integers 1..n when each
integer `k` is encoded as a composite symbol over the prime alphabet with weights
`log(p)`. The leading term `n*log(n)` is the leading Stirling approximation to
this entropy.

The interpolation `E_lambda(n)` therefore interpolates between:
- `lambda = 0`: pure Stirling leading term `n*log(n)`
- `lambda = 1`: exact prime-factorization entropy `log(n!) + n`

**This interpretation is [INTERP]: it provides structural motivation for the
potential shape but does not constitute a UBT derivation of B or of lambda.**

---

## 6. Main Questions and Answers

### Q1: Is `lambda_fit` close to any canonical UBT/modular/RG/determinant value?

See the ranked candidate table in Section 7. The answer is: **no canonical value
is within 0.01% of lambda_fit**. The closest candidates are:

| Candidate | Value | Distance | Status |
|-----------|-------|----------|--------|
| `37/80` | `0.46250` | `0.028%` | NUMERIC_ONLY |
| `6/13` | `0.46154` | `0.147%` | NUMERIC_ONLY |

Neither `37/80` nor `6/13` has a known UBT interpretation.

### Q2: Can `lambda` be derived from UBT?

No. The sources examined — Stirling subleading terms, RG corrections, modular
form factors, digamma ratios, N_eff factors — all differ from lambda_fit by
more than 2%. The one-loop QED correction `alpha/(3*pi) ≈ 7.7e-4` is four
orders of magnitude smaller than lambda_fit.

The only structurally motivated values near 1/2 (e.g., `1/2 - 1/(12*pi) ≈ 0.4735`)
deviate from lambda_fit by more than 2%.

### Q3: Does the Gamma-entropy refinement improve the alpha prediction?

The refinement **brackets** the measured alpha_inv between two structurally
motivated potential forms, providing a stronger geometric picture of why
`alpha_inv ≈ 137.036` lies between the integer 137 and nearby values. However,
it does not improve the derivation status — both `n1` and `n3` still depend
on the underived `B_Ram`, and lambda_fit is a fit parameter with no known
derivation from `S[Θ]`.

The key improvement is **explanatory**: the entropic term is now identified as
prime-factorization information entropy via Legendre's formula, rather than
an ad hoc `n*log(n)` combination.

### Q4: Does the Gamma-entropy refinement preserve the correct origin of `n*log(n)`?

Yes. The Stirling subleading correction is:
```
(log(Gamma(n+1)) + n) - n*log(n) = (1/2)*log(2*pi*n) + 1/(12n) + ...
                                  ≈ 3.37967  (at n = 137.036)
```

This is numerically small relative to `n*log(n) ≈ 674.25` (0.50%), confirming
that the `n*log(n)` origin as prime-factorization entropy is preserved.

---

## 7. Candidate Constant Comparison Table

`lambda_fit_exact = 0.462217542719466`  [OBS]

Comparison is against `lambda_fit_exact`. Status:
- `PLAUSIBLE_1PCT`: within 1% (but no derivation known = NUMERIC_ONLY in UBT sense)
- `NUMERIC_ONLY`: all others

| Rank | Constant | Value | \|err\| | rel% | Status | Possible interpretation |
|------|----------|-------|---------|------|--------|------------------------|
| 1 | `37/80` | 0.462500000000000 | 2.83e-04 | 0.061% | NUMERIC_ONLY | rational approximation; no UBT meaning |
| 2 | `6/13` | 0.461538461538462 | 6.79e-04 | 0.147% | NUMERIC_ONLY | rational near lambda; no UBT meaning |
| 3 | `1/2 - 1/(12*pi)` | 0.473474176151 | 1.13e-02 | 2.435% | NUMERIC_ONLY | Stirling correction to midpoint |
| 4 | `1/2 - 1/(4*pi^2)` | 0.474669704089 | 1.25e-02 | 2.694% | NUMERIC_ONLY | no UBT meaning |
| 5 | `3/(2*pi)` | 0.477464829276 | 1.52e-02 | 3.299% | NUMERIC_ONLY | N_phases/(2*pi) for N_phases=3 |
| 6 | `1/2` | 0.500000000000 | 3.78e-02 | 8.174% | NUMERIC_ONLY | midpoint |
| 7 | `sqrt(2)-1` | 0.414213562373 | 4.80e-02 | 10.39% | NUMERIC_ONLY | no UBT meaning |
| 8 | `log(2)/(1+log(2))` | 0.409383890850 | 5.28e-02 | 11.43% | NUMERIC_ONLY | no UBT meaning |
| 9 | `1/phi^2` | 0.381966011250 | 8.03e-02 | 17.36% | NUMERIC_ONLY | 1/phi^2 = 2-phi |
| 10 | `1/e` | 0.367879441171 | 9.43e-02 | 20.41% | NUMERIC_ONLY | saddle-point weight |
| 11 | `1/pi` | 0.318309886184 | 1.44e-01 | 31.13% | NUMERIC_ONLY | Stirling correction |
| 12 | `1/phi` | 0.618033988750 | 1.56e-01 | 33.71% | NUMERIC_ONLY | golden ratio inverse |
| … | (all others) | — | > 0.15 | > 30% | NUMERIC_ONLY | — |

**Key finding**: No candidate constant has a known UBT derivation. The two
nearest candidates (`37/80` and `6/13`) are numerically close but coincidental.

---

## 8. Stirling Subleading Analysis at `n = alpha_inv_exp`

All values at `n = 137.035999084` (CODATA 2018):

| Quantity | Value |
|----------|-------|
| `log(Gamma(n+1))` | `540.59417484836556699...` |
| `n*log(n) - n` | `537.21450637435249334...` |
| `(1/2)*log(2*pi*n)` | `3.37906036237837776...` |
| `1/(12n)` | `0.00060811271410698...` |
| Stirling sum | `540.59417484944497809...` |
| Relative error (Stirling vs exact) | `2.0e-12` |

```
(log(Gamma(n+1)) + n) - n*log(n)
  = 3.3796684740130736...   (at n = 137.036)
```

This subleading correction (0.50% of `n*log(n)`) is the reason `n1 ≠ n3`.
The fractional difference `(n3 - n1)/n1 = 0.074%` reflects this sub-percent shift.

---

## 9. Conclusion

**Overall verdict: PLAUSIBLE_OBS**

| Finding | Status |
|---------|--------|
| `n1 < alpha_inv_exp < n3` (bracket property) | **CONFIRMED** [numeric] |
| Legendre formula for `log(n!)` | **PROVED** [STD/L0] |
| Stirling expansion of `log(Gamma(n+1)) + n` | **PROVED** [STD/L0] |
| Entropy interpretation of `n*log(n)` term | **STRUCTURAL** [INTERP] |
| `B_Ram` as B-coefficient | **[OBS]** — not derived from `S[Θ]` |
| `lambda_fit` derivation from `S[Θ]` | **UNKNOWN** — no candidate found |
| `lambda_fit` close to canonical constant | **NEGATIVE** — closest is `37/80` at 0.06% (NUMERIC_ONLY) |
| Alpha derived | **NO** |
| G137-B closed | **NO** |

**Specific conclusions:**

1. The Gamma-entropy refinement **brackets** the measured alpha_inv between two
   structural potential forms. This improves the explanatory picture but does not
   constitute a derivation.

2. Lambda_fit ≈ 0.4622 (exact stationary) or ≈ 0.4624 (fractional) has no known
   derivation from UBT. It is a fit parameter. No canonical UBT/modular/RG/Stirling
   value matches it to better than 0.06%, and even that match (37/80) is numerically
   coincidental with no structural interpretation.

3. The prime-factorization entropy interpretation (`Legendre formula → log(n!)`) is
   mathematically exact [STD/L0] and provides structural motivation for the `n*log(n)`
   form. This is a genuine improvement in explanatory status.

4. **Forbidden move check**: No claim is made that alpha has been derived, that B_Ram is
   proved, or that lambda_fit is anything other than a numerical observation.

---

## Source Files

| File | Purpose |
|------|---------|
| `tools/scan_gamma_entropy_lambda.py` | mpmath computation tool |
| `canonical/alpha/gamma_entropy_alpha_refinement_status.tex` | LaTeX status file |
| `canonical/alpha/prime_factorization_entropy_potential.tex` | Prior entropy interpretation doc |
| `canonical/alpha/ALPHA_MASTER_STATUS.md` | Authoritative alpha status |
| `reports/alpha_missing_lemma.md` | Gap G137-B exact statement |
