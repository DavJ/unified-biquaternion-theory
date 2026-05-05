> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

# L0 / L1 / L2 — Code Analysis

**Task**: `ubt_L0_L1_L2_full_audit`  
**Date**: 2026-05-05  
**Mode**: deep_repo_analysis  
**Epistemic mode**: strict

---

## Summary

No Python functions or classes named `L0`, `L1`, or `L2` exist in the
repository. The L0/L1/L2 labels appear only as **documentation and status
vocabulary**, not as callable code objects.

The closest code-level analogs are Python functions that implement specific
Layer-2 operations (Hamming coding, Gray transport, winding number scan).
These are described below.

---

## Python Files with L0/L1/L2 References

### 1. `research_tracks/alpha/layer2_coding_alpha_scan.py`

**Type**: [code]  
**Purpose**: Tests whether Layer-2 coding constraints (Hamming, Gray, 1⊕3⊕3̄⊕1
decomposition) fix the fine-structure constant α.

#### Functions

**`generate_hamming_844_codewords() → list[int]`**
- Generates all 16 codewords of the extended Hamming (8,4,4) code.
- Input: none  
- Output: `list[int]` — 16 integers representing 8-bit codewords
- Codeword space: {0,1}^8, subspace of dimension 4, minimum distance 4

**`hamming_weight(x: int, nbits: int = 8) → int`**
- Counts 1-bits in nbits-bit integer.
- Input: integer x, bit width  
- Output: int ∈ {0, ..., 8}

**`hamming_distance(a: int, b: int, nbits: int = 8) → int`**
- Hamming distance d_H(a, b) = popcount(a XOR b)
- Input: two integers  
- Output: int ∈ {0, ..., 8}

**`minimum_code_distance(codewords: list[int]) → int`**
- Computes min_dist of a code from a list of codewords.
- Input: list of integers  
- Output: int (minimum Hamming distance between distinct codewords)

**`test_hamming_844_structure() → dict`**
- Tests whether Hamming (8,4,4) structure constrains charge spectrum or α.
- Input: none  
- Output: dict with keys: `test`, `n_codewords`, `d_min`, `codeword_weights`,
  `alpha_if_e_equals_1_over_dmin`, `matches_observed_alpha`, `classification`,
  `reason`
- **Classification result**: `"failed"` — Hamming code fixes allowed charge
  values (quantization spectrum) but NOT the magnitude of elementary charge;
  α = e²/(4π) requires e in physical units.

**`standard_gray_code(n: int) → list[int]`**
- Generates standard reflected binary Gray code for n-bit symbols.
- Input: number of bits n  
- Output: list of 2^n integers in Gray order
- Implementation: `[i ^ (i >> 1) for i in range(1 << n)]`

**`is_gray_adjacent(a: int, b: int, gray_order: list[int]) → bool`**
- Returns True if a and b are adjacent in the given Gray ordering.
- Input: two integers, Gray order list  
- Output: bool

**`test_gray_transport_layer() → dict`**
- Tests whether Gray transport constraints fix U(1) phase quantization → α.
- Input: none  
- Output: dict with `classification: "failed"` — Gray transport fixes phase
  step size 2π/N but N is a free parameter; does not determine coupling magnitude.

**`test_su2_decomposition_1330() → dict`**
- Tests whether 1⊕3⊕3̄⊕1 decomposition of B = C⊗H under SU(2) constrains α.
- Input: none  
- Output: dict with `classification: "failed"` — fixes representation structure
  but not U(1)_Y normalization; no j=1/2 doublet present.

**`test_combined_coding_constraint() → dict`**
- Combined test: all three coding constraints together.
- Input: none  
- Output: dict with `classification: "failed"` — coding constrains structure
  (charge spectrum, phase steps, representation type) but not the magnitude
  of elementary charge in physical units.

**`test_positive_contributions() → dict`**
- Identifies what the coding layer CAN contribute to the α derivation.
- Partial positive findings: charge quantization spectrum, Dirac quantization
  consistency, prime-attractor support.

---

### 2. `experiments/forensic_fingerprint/tools/gray_path_symbol_test.py`

**Type**: [code]  
**Purpose**: Implements the L2T (Gray transport) CMB path-fingerprint test.
Computes gray_adjacency_score A_gray on CMB phase symbols and tests against
shuffle/phase-randomized null models.

#### Functions

**`binary_to_gray(n: int) → int`**
- Converts non-negative integer to standard reflected binary Gray code.
- Input: int n ≥ 0  
- Output: int (Gray code of n)
- Implementation: `n ^ (n >> 1)`

**`gray_to_binary(g: int) → int`**
- Inverts the standard reflected binary Gray code.
- Input: Gray code integer g  
- Output: int (original n)

**`build_gray_order_table(N: int) → np.ndarray`**
- Builds table: `gray_rank[s]` = position of symbol s in Gray ordering.
- Input: N (power of 2, symbol alphabet size)  
- Output: `np.ndarray` of shape (N,), dtype int32
- Represents G^{-1}(s) from gray_path_fingerprint.tex §5

**`gray_adjacency_mask(s, sp, N, gray_rank) → np.ndarray`**
- Returns boolean array: True where pairs (s[i], sp[i]) are Gray-adjacent.
- Input: symbol arrays s, sp; alphabet size N; gray_rank table  
- Output: boolean array, same shape as s
- Implementation: `|gray_rank[s] - gray_rank[sp]| == 1 (mod N)`

**`phases_to_symbols(phases: np.ndarray, N: int) → np.ndarray`**
- Discretizes phase values ∈ [-π, π) into N symbols.
- Input: float array of phases; N (power of 2)  
- Output: int array in {0, ..., N-1}
- Formula: `s = floor(N / (2π) * (phase + π))`

**`alm_to_symbols(alm: np.ndarray, N: int) → np.ndarray`**
- Extracts phase symbols from complex a_lm coefficients.
- Input: complex array, N  
- Output: int array in {0, ..., N-1}

**`gray_adjacency_score(symbols, N, gray_rank) → float`**
- Computes A_gray = fraction of consecutive symbol pairs that are Gray-adjacent.
- Input: symbol array, N, gray_rank table  
- Output: float ∈ [0, 1]
- Formula: `A_gray = (1/(m-1)) Σᵢ 1[s_{i+1} is Gray-adjacent to sᵢ]`
- Expected null value: 2/N (for i.i.d. uniform symbols)

**`shuffle_null(symbols, rng) → np.ndarray`**
- Generates shuffle-null sequence (random permutation).
- Input: symbol array, numpy RNG  
- Output: shuffled symbol array

**`phase_randomized_null(n_symbols, N, rng) → np.ndarray`**
- Generates phase-randomized null (i.i.d. uniform symbols).
- Input: sequence length, N, numpy RNG  
- Output: random symbol array

**`run_test(symbols, N, n_null, null_type, seed, verbose) → dict`**
- Runs the full Gray path-fingerprint test.
- Input: symbol array, N, n_null realizations, null_type, seed, verbose  
- Output: dict with keys: `observed`, `null_scores`, `null_mean`, `null_std`,
  `p_value`, `expected_null`, `N`, `n_symbols`, `n_null`, `null_type`
- Interpretation: p < 0.01 → detection of L2T Gray transport preference

---

### 3. `experiments/layer2_stability/layer2_rigidity.py`

**Type**: [code]  
**Purpose**: Layer-2 rigidity analysis — parameter stability scan. Tests
whether the fine-structure constant prediction α⁻¹ = 137 is stable under
parameter variations in N_eff ∈ [8, 20] and R_UBT ∈ [0.9, 1.4].

**Key functions** (from file header):
- `sieve_primes(limit: int) → list` — Sieve of Eratosthenes
- Computes `V_eff(n) = n² - B·n·ln(n)` for winding modes
- Sweeps (N_eff, R_UBT) parameter space to compute hit_rate and rarity_bits

**Metrics**:
- `hit_rate`: fraction of (N_eff, R_UBT) samples where p_opt = 137
- `rarity_bits`: −log₂(hit_rate)
- `max_delta`: maximum shift of p_opt in stable region

**Layer label usage**: Layer 2 in the file title refers to System A
(coding/protocol layer), NOT the perturbative loop order [L2].

---

### 4. `research_tracks/legacy_theory_variants/ubt_core/verify_Vpsi.py`

**Type**: [code]  
**Purpose**: Verifies V_ψ potential; contains L1/L2 references in comments only.

---

## Functions Not Found

The following were searched for explicitly and **not found** in any Python file:

| Pattern | Result |
|---------|--------|
| `def L0(` | Not found |
| `def L1(` | Not found |
| `def L2(` | Not found |
| `class L0` | Not found |
| `class L1` | Not found |
| `class L2` | Not found |
| `def project(` | Not found (as layer-specific function) |
| `def transform(` | Not found (as layer-specific function) |
| `def encode(` | Not found |
| `def decode(` | Not found |

---

## LaTeX Files with L0/L1/L2 Definitions

### `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`

**Type**: [doc] (formal LaTeX document)

This is the most detailed mathematical definition of the Layer 0/1/2
architecture. Provides:
- Definition 2.1: Biquaternionic Field (Layer 0 field space)
- Definition 2.2: Hermitian Structure
- Definition 2.3: UBT Action (Layer 0 action functional)
- Symmetry analysis (Layer 0 Noether charges)
- Layer-0 invariants (five mathematical invariants)
- Layer-2 to Layer-0 mapping equations with error decomposition
- Binary classification: Layer-2 = ADDED STRUCTURE (not mere approximation)

### `docs/architecture/LAYERS.md`

**Type**: [doc]

Defines Layer 1 vs Layer 2 contract for architecture. Note: this file does
not define a "Layer 0" — it starts from Layer 1.

---

*Generated by ubt_L0_L1_L2_full_audit, Step 2.*
