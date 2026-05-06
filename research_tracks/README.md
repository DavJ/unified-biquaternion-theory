<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# research_tracks/ — UBT Research Tracks Index

This directory contains **active and exploratory research tracks** that are not yet
part of the canonical UBT formulation.  Material here is work in progress: some
tracks are close to promotion, others are purely exploratory.

**Promotion path**: research_tracks → canonical (requires internal consistency,
mathematical closure, and compatibility with canonical structure).

---

## Confidence Labels

| Label | Meaning |
|-------|---------|
| **Strong** | Rigorous derivation; zero free parameters |
| **Strong Partial** | Structural derivation substantially complete; ≤1 open sub-gap |
| **Candidate** | Proposed mechanism with supporting evidence; ≥1 gap unresolved |
| **Experimental** | Hypothesis supported by numerical/observational tests; no algebraic proof |
| **Applied Experimental** | Applied/computational result with empirical support; theory not fully closed |
| **Open** | No complete derivation known; active problem |
| **Deprecated** | Approach proved to fail or superseded; preserved for reference |

---

## Track Index

### Physics and Geometry

| Track | Directory | Confidence | Notes |
|-------|-----------|-----------|-------|
| GR off-shell rank proof | `research/` | **Strong Partial** | ker J = U(2) on ℝ¹˒³ proved; compact M⁴ open |
| Schwarzschild from Θ | `research/` | **Strong Partial** | Full metric proved [L1]; Zerilli even-parity open |
| Graviton in Schwarzschild background | `research/` | **Strong Partial** | Odd-parity (Regge-Wheeler) proved; even-parity (Zerilli) open |
| Mirror sector (twin prime vacuum) | `mirror_sector/` | **Candidate** | V_eff(139) branch motivated; mirror α⁻¹=139 is numerical observation |
| Moduli space / de Sitter structure | `research/` | **Candidate** | dS physical M⁴ follows from GR+Λ; AdS/CFT analogy is structural only |
| Higgs/Yukawa sector | `research/` | **Candidate** | Radiative Hosotani partially proved [L1]; λ gap factor ~11 open |
| r-factor (R≈1.114 two-loop correction) | `research/` | **Open** | 27+ approaches; best candidate ΔB=3π/2 (Motivated Conjecture) |
| Three fermion generations | `research/` | **Open** | Algebraic origin Candidate; mass ratios not reproduced |

### Symmetry and Algebra

| Track | Directory | Confidence | Notes |
|-------|-----------|-----------|-------|
| SU(3) qubit / one-hot mapping | `THEORY_COMPARISONS/su3_qubit_mapping/` | **Candidate** | Valid Lie algebra homomorphism; separate from mainline involution derivation |
| Penrose twistor bridge | `THEORY_COMPARISONS/penrose_twistor/` | **Candidate** | Flat Minkowski sector proved; curved sector and ψ-twistor mapping open |
| Hecke bridge (modular forms ↔ ℂ⊗ℍ) | `hecke_bridge/` | **Candidate** | Weight/level correspondences are motivated conjectures; derivation open |
| RH trace formula (ψ-Hamiltonian → ζ) | `rh_trace_formula/` | **Open** | Candidate H_ψ defined; 6 open gaps (G1–G6) before any ζ-connection; NO RH claim |
| Prime Fock operator (Fock-space H_prime, partition fn = ζ) | `prime_fock_operator/` | **Open** | Tr(e^{−sH_prime})=ζ(s) established; UBT embedding and analytic continuation open; NO RH claim |
| Quantization grid | `quantization_grid/` | **Experimental** | Discretization hypothesis under numerical investigation |

### Coding and Information (Layer 2)

| Track | Directory | Confidence | Notes |
|-------|-----------|-----------|-------|
| L2S: Hamming (8,4,4) state fingerprint | (see `experiments/research_tracks/fingerprints/`) | **Experimental** (Strong Experimental) | P₀ syndrome-zero fraction; positive CMB detection pending peer review |
| L2T: Gray transport layer | `gray_transport_layer/` | **Experimental** | Gray adjacency score hypothesis; CMB path-fingerprint test proposed; no algebraic proof |
| Channel stability lab (137/139) | `ubt-channel-lab/` | **Experimental** | Statistical scan of channel selection; falsifiability framework in place |
| Information probes (RS codes) | `information_probes/` | **Applied Experimental** | Reed-Solomon RS(255,201) as MDS-optimal probe; observable predictions probe-dependent |
| Coding fingerprint (applied / cryptographic) | `fingerprints/` | **Applied Experimental** | SHA-256 data integrity + Hamming parity check applied to CMB data; not a UBT first-principles prediction |

### Observational / Applied

| Track | Directory | Confidence | Notes |
|-------|-----------|-----------|-------|
| CERN findings and UBT | `cern_findings_and_ubt/` | **Experimental** | Consistency check of LHC anomalies with UBT predictions |
| CMB 2D FFT analysis | `research_front/cmb_2d_fft/` | **Experimental** | 2D power spectrum of CMB maps; probe of Layer 2 hypothesis |
| Hubble latency model | `HUBBLE_LATENCY/` | **Experimental** | Complex-time latency mechanism for Hubble tension; no algebraic derivation |
| Research phase lock | `research_phase_lock/` | **Experimental** | Phase-locking mechanism in ψ-time; exploratory |
| Insensitivity analysis | `insensitivity/` | **Experimental** | Robustness/insensitivity tests for key UBT predictions |
| CERN / p-universes | `p_universes/` | **Experimental** | p-adic universe branching; speculative extension of mirror sector |

### Comparisons and Legacy

| Track | Directory | Confidence | Notes |
|-------|-----------|-----------|-------|
| Theory comparisons (multi-criteria) | `THEORY_COMPARISONS/` | Reference | Systematic comparison of UBT with alternative frameworks |
| Legacy theory variants | `legacy_theory_variants/` | **Deprecated** | Older UBT formulations preserved for reference; not canonical |
| Extensions | `extensions/` | **Candidate** | Exploratory extensions to canonical structure |
| Automorphic / analysis | `automorphic/`, `analysis/` | **Candidate** | Automorphic form connections; rank analysis |

---

## Notes on the crypto / coding branch

The **applied coding branch** (RS codes, Hamming fingerprints, Gray transport) uses
classical error-correcting codes as **observational probes** of UBT Layer 2
predictions.  These are not first-principles UBT derivations; they are applied
experimental tools.  Confidence: **Applied Experimental**.

The canonical L2S fingerprint (Hamming (8,4,4)) is the strongest experimental
result in this branch; it is tracked as **Experimental (Strong)** in
`DERIVATION_INDEX.md`.

---

## Promotion Criteria

A research track may be promoted to `canonical/` when:

1. Internal consistency established (no circular arguments).
2. Mathematical closure achieved (no free parameters unexplained).
3. Compatible with existing canonical structure (GR limit, SM gauge structure).
4. Independent reproducibility verified (at least one script or external check).

---

**Last Updated**: 2026-05-04
