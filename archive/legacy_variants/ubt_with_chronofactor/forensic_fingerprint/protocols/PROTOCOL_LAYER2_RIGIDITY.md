# Protocol: Layer2 Rigidity Fingerprint Analysis

**Protocol Version**: 1.0  
**Date**: 2026-02-13  
**Status**: Pre-registered  
**License**: MIT  

---

## 1. Purpose

This protocol defines the pre-registered methodology for Layer 2 parameter space rigidity analysis using the forensic fingerprint framework.

**Objective**: Quantify how constrained Layer 2 architectural choices are by observed physical constants, and assess whether the current UBT configuration is statistically exceptional within the permitted parameter space.

**Critical Requirement**: This analysis is scientifically interpretable **ONLY** when using `--mapping ubt`. The `--mapping placeholder` mode is for framework demonstration only and produces NO physically meaningful results.

---

## 2. Mapping Mode Requirement

### 2.1 Valid Modes

- **`--mapping ubt`** (REQUIRED for scientific interpretation)
  - Uses real UBT derivations via adapters to existing calculation modules
  - Wires to: `TOOLS/simulations/emergent_alpha_calculator.py` (alpha)
  - Wires to: `TOOLS/simulations/validate_electron_mass.py` (electron mass)
  - Results are scientifically interpretable

- **`--mapping placeholder`** (Framework demonstration only)
  - Uses arbitrary toy formulas with NO physical basis
  - MUST emit WARNING in all outputs
  - Results are NOT scientifically valid
  - Use only for testing framework functionality

### 2.2 Validity Statement

**All rigidity claims, hit-rate interpretations, and "top X%" statements are ONLY valid when `--mapping ubt` is used.**

Any analysis using `--mapping placeholder` MUST carry explicit warnings and disclaimers that results have no physical interpretation.

---

## 3. Parameter Space Definition

### 3.1 Layer 2 Parameters

Layer 2 parameters represent the "digital architecture" choices in UBT's information-theoretic interpretation of spacetime.

| Parameter | Range (baseline) | Range (wide) | Justification |
|-----------|------------------|--------------|---------------|
| `rs_n` | [200, 300] | [100, 500] | Reed-Solomon code length. Physical: Discretization scale. Max GF(2^8) is 255, but theory permits variation around this. |
| `rs_k` | ratio ∈ [0.6, 0.9] | ratio ∈ [0.5, 0.95] | Information payload fraction. Physical: Determines baryon density fraction via M_payload mapping. |
| `ofdm_channels` | [8, 32] | [4, 64] | Frequency multiplexing channels. Physical: Related to field multiplicity. Current UBT uses 16. |
| `winding_number` | [101, 199] | [50, 250] | Topological winding number. Physical: UBT predicts n=137 from stability constraint. Testing: Does this emerge robustly? |
| `prime_gate_pattern` | {0..9} | {0..19} | Prime gating pattern index. Physical: Unknown constraint level. Testing: Discreteness requirement. |
| `quantization_grid` | {128,255,256,512} | {64,128,255,256,512,1024} | Quantization grid size. Physical: Related to digital precision. |

**Constraint**: `rs_k ≤ rs_n` (information theory requirement)

**Sampling Strategy**: 
- Winding number: Prefer prime numbers in baseline/wide spaces (physical motivation from discreteness)
- Other parameters: Uniform sampling within ranges
- Prime gate pattern: Uniform discrete sampling

### 3.2 Range Scaling (Robustness Testing)

To test robustness, ranges are scaled symmetrically around their centers:

- **Baseline**: `range_scale = 1.0`
- **Contracted**: `range_scale = 0.8` (ranges 80% of baseline)
- **Expanded**: `range_scale = 1.2` (ranges 120% of baseline)

Formula: `new_range = center ± (half_width × range_scale)`

This tests whether hit-rate is sensitive to exact range boundaries (which would indicate boundary artifacts) or robust to range variations (which supports genuine rigidity).

---

## 4. Sampling Method

### 4.1 Random Sampling

- **Method**: Pseudo-random sampling using numpy.random.default_rng
- **Reproducibility**: Fixed seed for each protocol run
- **Distribution**: Uniform within defined ranges

### 4.2 Sample Size Targets

| Mode | Sample Size | Purpose |
|------|-------------|---------|
| debug | 10-100 | Quick testing, framework validation |
| baseline | 5,000-10,000 | Standard analysis |
| wide | 10,000-50,000 | Comprehensive coverage |

**Justification**: Sample sizes chosen to ensure:
1. Hit-rate estimates have statistical stability
2. Rare configurations (p ~ 0.1%) are likely to be sampled
3. Computational feasibility within reasonable time (~minutes to hours)

---

## 5. Targets and Tolerances

### 5.1 Target Observables

Primary targets (required for all runs):

1. **Fine structure constant inverse** (`alpha_inv`)
   - Observed value: 137.035999084 (CODATA 2018)
   - Uncertainty (1σ): 2.1e-8 (relative)

2. **Electron mass** (`electron_mass`)
   - Observed value: 0.51099895000 MeV (CODATA 2018)
   - Uncertainty (1σ): 2.9e-10 (relative)

### 5.2 Default Tolerances

**Critical Decision**: Tolerances define what constitutes a "hit" (match within tolerance).

Default tolerances (PROVISIONAL - subject to revision):

| Observable | Tolerance | Justification |
|------------|-----------|---------------|
| `alpha_inv` | 0.5 | Practical for parameter space exploration. Theory should predict within ~0.4% of 137.036. |
| `electron_mass` | 0.001 MeV (1 keV) | Practical tolerance. Theory should predict within ~0.2% of 0.511 MeV. |

**Alternative (5σ tolerances)**:
- `alpha_inv`: 5σ ≈ 1.4e-5 (extremely tight - likely too restrictive for parameter space sweep)
- `electron_mass`: 5σ ≈ 1.5e-9 MeV (extremely tight - likely too restrictive)

**Protocol Rule**: 
- Default tolerances are used unless explicitly overridden via `--tolerances` flag
- Any override MUST be documented in output metadata
- Tolerance choice affects hit-rate interpretation and MUST be justified

### 5.3 Hit Criterion

**Definition**: A configuration is a "hit" if and only if **ALL** normalized errors are ≤ 1:

```
normalized_error(obs) = |predicted - observed| / tolerance(obs)
is_hit = all(normalized_error(obs) ≤ 1 for obs in targets)
```

This is a strict criterion: even one observable outside tolerance → not a hit.

---

## 6. Output Requirements

Every protocol run MUST produce:

### 6.1 Required Files

1. **`configurations.csv`**
   - All sampled configurations with scores
   - Columns: all Layer 2 params, predictions, errors, combined_score, is_hit

2. **`summary.json`**
   - Machine-readable summary statistics
   - Fields: space_type, n_samples, seed, mapping_mode, hit_rate, rarity_bits, etc.

3. **`report.md`** (or `results.txt`)
   - Human-readable summary
   - MUST include WARNING if mapping=placeholder
   - Best configuration, statistics, rigidity assessment

4. **`VERDICT.md`**
   - Final assessment document
   - Hit-rate, rarity_bits, robustness analysis
   - Explicit conclusion (see Section 7)

5. **Figures** (in `figures/` subdirectory):
   - `score_hist.png` - Distribution of combined scores
   - `alpha_error_hist.png` - Distribution of alpha errors
   - `scatter_winding_vs_alpha_error.png` - Parameter correlation
   - Additional diagnostic plots as needed

### 6.2 Metadata Requirements

All outputs MUST document:
- Protocol version
- Mapping mode
- Space type
- Range scale
- Sample size
- Random seed
- Tolerances used
- Timestamp

---

## 7. Robustness Criteria

### 7.1 Range Perturbation Tests

For robust analysis, run with three range_scale values:

| Scale | Interpretation |
|-------|----------------|
| 0.8 | Contracted ranges (−20% width) |
| 1.0 | Baseline (protocol default) |
| 1.2 | Expanded ranges (+20% width) |

### 7.2 Robustness Metrics

Compute for each scale:
- Hit-rate
- Rarity bits
- Best configuration score

### 7.3 Robustness Assessment

**Criterion**: Hit-rate is considered ROBUST if it remains within [1/3×, 3×] of baseline across all perturbations.

```
robust = (hit_rate(0.8) / hit_rate(1.0)) ∈ [1/3, 3]
         AND (hit_rate(1.2) / hit_rate(1.0)) ∈ [1/3, 3]
```

**Interpretation**:
- **Robust**: Hit-rate stable across range variations → rigidity is genuine, not boundary artifact
- **Not robust**: Hit-rate varies strongly → need to refine ranges or investigate boundary effects

This criterion prevents false rigidity claims from accidental range choices.

---

## 8. Statistical Interpretation

### 8.1 Hit-Rate

**Definition**: `hit_rate = n_hits / n_total`

**Interpretation**:
- hit_rate < 0.01 (1%) → High rigidity (rare matches)
- hit_rate 0.01-0.05 (1-5%) → Moderate rigidity
- hit_rate ≥ 0.05 (≥5%) → Low rigidity (common matches)

### 8.2 Rarity Bits

**Definition**: `rarity_bits = -log₂(hit_rate)`

**Interpretation**: Information-theoretic measure of surprise.
- 0 hits → ∞ bits (impossible to hit)
- hit_rate = 0.5 → 1 bit
- hit_rate = 0.01 → ~6.64 bits
- hit_rate = 0.001 → ~9.97 bits

Higher rarity_bits = more exceptional to find matching configuration.

### 8.3 Current Configuration Ranking

**Metric**: Percentile rank of current UBT configuration (RS(255,200), OFDM=16, n=137, etc.) within sampled population.

**Interpretation**:
- Top 1% → Current config is exceptional
- Top 10% → Current config is good
- Top 50% → Current config is moderate
- Bottom 50% → Current config needs review

**Note**: This ranking is ONLY meaningful for `--mapping ubt`.

### 8.4 No P-Values Without Null Model

**CRITICAL**: This protocol does NOT compute p-values or significance tests unless:
1. A null hypothesis is formally defined
2. A null distribution is properly constructed
3. Multiple testing corrections are applied (if needed)

Current analysis uses descriptive statistics (hit-rate, rarity_bits, percentile) which do NOT require null hypotheses.

---

## 9. VERDICT.md Format

The `VERDICT.md` file MUST contain:

```markdown
# Layer2 Fingerprint Rigidity Verdict

**Protocol Version**: 1.0
**Mapping Mode**: [placeholder|ubt]
**Space Type**: [debug|baseline|wide]
**Sample Size**: [N]
**Random Seed**: [seed]
**Timestamp**: [ISO 8601]

---

## Hit-Rate Analysis

- **Hits**: [n_hits] / [n_total]
- **Hit-Rate**: [hit_rate] ([percentage]%)
- **Rarity**: [rarity_bits] bits

---

## Robustness Analysis

| Range Scale | Hit-Rate | Rarity (bits) | Ratio to Baseline |
|-------------|----------|---------------|-------------------|
| 0.8         | [...]    | [...]         | [...]             |
| 1.0         | [...]    | [...]         | 1.00              |
| 1.2         | [...]    | [...]         | [...]             |

---

## Conclusion

[If mapping=ubt:]

**Rigidity Assessment**: [High|Moderate|Low] - [justification based on hit-rate]

**Robustness**: [Robust|Not Robust] - [justification based on ratio criterion]

**Current Configuration**: [Ranking statement]

**Verdict**: [Overall assessment of whether Layer 2 appears constrained]

[If mapping=placeholder:]

⚠️ **WARNING**: This analysis uses PLACEHOLDER physics mapping.
Results have NO scientific interpretation.
Framework demonstration only.
```

---

## 10. Protocol Compliance

### 10.1 Checklist for Valid Run

- [ ] Mapping mode documented (ubt or placeholder)
- [ ] WARNING emitted if mapping=placeholder
- [ ] Parameter ranges documented
- [ ] Sample size meets minimum targets
- [ ] Random seed recorded
- [ ] Tolerances documented
- [ ] All required outputs generated
- [ ] Figures saved
- [ ] VERDICT.md created
- [ ] Robustness runs completed (if `--robustness` flag used)

### 10.2 Protocol Violations

The following constitute protocol violations and invalidate results:

1. Using `--mapping placeholder` without prominent warnings
2. Making rigidity claims without `--mapping ubt`
3. Omitting required output files
4. Failing to document tolerances or range scales
5. Cherry-picking results from multiple runs without disclosure

---

## 11. Future Protocol Versions

Changes requiring new protocol version (e.g., v1.1):

- Modified parameter ranges
- New target observables
- Changed tolerance definitions
- Different sampling strategies
- Alternative robustness criteria

All protocol changes MUST be documented and version-controlled.

---

## Appendix A: Theoretical Justification

### Layer 2 vs Layer 1

**Layer 1** (fundamental physics): Biquaternionic field Θ, metric g_μν, gauge fields
**Layer 2** (information architecture): RS codes, OFDM, quantization - implementation details

**Key Question**: Are Layer 2 choices arbitrary (like choosing computer architecture) or constrained by physics?

**This protocol tests**: If Layer 2 were free to vary, would random choices reproduce observed constants? Or is current configuration special?

**Interpretation**:
- High rigidity + current config in top percentile → Layer 2 may be physically constrained
- Low rigidity → Layer 2 choices are arbitrary (as expected for "architecture")

### Connection to Nobel-Grade Science

This analysis aims to provide:
1. **Quantitative rigor**: Not "it works" but "how rare is it to work"
2. **Falsifiability**: Clear null outcome (high hit-rate = not constrained)
3. **Reproducibility**: Pre-registered protocol, fixed seeds, version control
4. **Robustness**: Tests against range perturbations

These are prerequisites for credible scientific claims about parameter space constraints.

---

**Protocol End**

---

**Revision History**:
- v1.0 (2026-02-13): Initial protocol definition
