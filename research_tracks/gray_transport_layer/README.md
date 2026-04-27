> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

# Gray Transport Layer — Research Track

**Author**: Ing. David Jaroš  
**Date**: 2026-04-27  
**Status**: Research Track — Hypothesis under investigation

---

## Summary

This research track formalizes the **Gray-code transport hypothesis** as a
mechanism complementary to the canonical Hamming (8,4,4) Layer 2 fingerprint.

The two coding schemes address distinct physical questions:

| Layer | Code | Role | Observable |
|-------|------|------|------------|
| **L2S** (state) | Hamming (8,4,4) | State/storage protection | P₀ = syndrome-zero fraction |
| **L2T** (transport) | Gray adjacency | Path/transition cost | gray_adjacency_score |

**Core claim:**
> Hamming coding protects state identity. Gray coding minimizes transition cost
> and supports path-consistency tests. The two schemes are complementary:
> Hamming for storage, Gray for transport.

**What is NOT claimed:**
- Gray code does not replace Hamming.
- Gray code does not prove QCD.
- Gray code does not prove dark matter.
- Not all SU(3) generators are one SWAP.

---

## Files in this Directory

| File | Description |
|------|-------------|
| `README.md` | This overview |
| `gray_vs_hamming_layer2.md` | Detailed comparison: L2S vs L2T; definitions; complementarity argument |
| `gray_path_fingerprint.tex` | LaTeX derivation: formal definitions, one-hot analysis, CMB path-fingerprint test |

## Related Files

| File | Role |
|------|------|
| `experiments/research_tracks/fingerprints/UBT_coding_fingerprint.tex` | Canonical Hamming (8,4,4) fingerprint document — updated to include Gray transport section |
| `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/triqubit_minimality_note.md` | One-hot triqubit; Gray adjacency note appended |
| `experiments/forensic_fingerprint/tools/gray_path_symbol_test.py` | Python test for CMB gray_adjacency_score |

---

## Theoretical Context

### Layer 2 Split

UBT Layer 2 (Coding and Stability) is subdivided:

- **L2S — State Layer**: discrete stabilizer selection rules protecting the
  identity of admissible field configurations. The Hamming (8,4,4) code is the
  canonical L2S fingerprint: it detects single-symbol errors and corrects
  single-bit errors in 8-symbol phase blocks. Observable: P₀ (syndrome-zero
  probability vs. shuffled null).

- **L2T — Transport Layer**: transition-cost rules governing sequential
  phase-symbol evolution. Gray code ordering minimizes the Hamming distance
  between successive symbols, making single-step transitions the least costly.
  Observable: gray_adjacency_score (fraction of consecutive aℓm symbol pairs
  that are Gray-adjacent vs. phase-randomized null).

### SU(3) Connection

In the one-hot triqubit representation {|r⟩=|100⟩, |g⟩=|010⟩, |b⟩=|001⟩}:

- **Off-diagonal (color-changing) generators** (λ₁,λ₂,λ₄,λ₅,λ₆,λ₇): each
  changes color identity, i.e., permutes one-hot states. These transitions
  connect states at Hamming distance 2 from each other.

- **Diagonal (phase) generators** (λ₃,λ₈): preserve the one-hot state identity
  while changing the phase. These transitions remain within the same one-hot
  state and are natural candidates for Gray-adjacent phase steps.

Gray transport applies specifically to the diagonal/phase sector. It is a
path-ordering constraint, not a replacement for the one-hot Hamming stabilizer.

---

## Promotion Criteria

To be promoted from research track to canonical:

1. CMB path-fingerprint test returns p-value < 0.01 against null (phase-randomized).
2. Theoretical argument derived from S[Θ] for why sequential ψ-phase transitions
   prefer minimal Hamming distance.
3. No conflict with Hamming L2S fingerprint.
4. Independent reproduction.
