# UBT Glossary

## Core Concepts

### Biquaternion

A quaternion with complex coefficients. If **q** = q₀ + q₁**i** + q₂**j** + q₃**k** is a quaternion (where **i**, **j**, **k** are quaternion units), then a biquaternion has each component qₙ ∈ ℂ (complex numbers).

**Example**: Θ = (a + ib) + (c + id)**i** + (e + if)**j** + (g + ih)**k**

**UBT usage**: The fundamental field Θ(q,τ) is biquaternion-valued.

### Complex Time (τ)

Time extended to the complex plane:
```
τ = t + iψ
```

Where:
- **t**: Real time (observable, measured by clocks)
- **ψ**: Imaginary time component (phase/synchronization degrees of freedom)
- **i**: Imaginary unit (not quaternion **i**)

**Key property**: Ordinary matter couples only to real time t, making ψ invisible to classical observations.

### Θ Field

The fundamental biquaternionic field Θ(q,τ) that unifies spacetime geometry and gauge fields.

**Arguments**:
- **q**: Quaternion spatial coordinates
- **τ**: Complex time

**Equation**: ∇†∇Θ(q,τ) = κ𝒯(q,τ)

**Physical interpretation**: Real part governs spacetime metric (gravity), complex/quaternion structure governs gauge fields (EM, weak, strong forces).

### Reed-Solomon Code RS(255,201)

Error-correcting code used in UBT's discrete computational architecture.

**Parameters**:
- **n = 255**: Total symbols (frame length minus 1)
- **k = 201**: Data symbols
- **F = 256**: Frame length (n + 1)

**Property**: Can correct up to (255-201)/2 = 27 symbol errors per frame.

**UBT interpretation**: Provides robustness against quantum fluctuations in discrete-time evolution.

## Predictions and Tests

### Fine Structure Constant (α)

Dimensionless constant characterizing electromagnetic interaction strength.

**Experimental value**: α⁻¹ = 137.035999084 ± 0.000000021 (CODATA 2018)

**UBT prediction**: α⁻¹ = 137.036 (from biquaternionic geometry)

**Error**: 0.00003% (exact to 4 decimal places)

**Status**: CONFIRMED

### Fingerprint

A testable prediction derived from UBT theory.

**Classification**:
- **Confirmed**: Agrees with observation, independently validated
- **Candidate**: Statistical signal without replication
- **Null**: Tested and found absent

**Principle**: Null results are first-class scientific outcomes.

### Court-Grade Test

A forensic-level empirical test with:
- ✅ Pre-registered protocol (parameters fixed before running)
- ✅ SHA-256 data manifests (cryptographic integrity)
- ✅ Reproducible pipeline (exact command documented)
- ✅ Fail-fast validation (HTML detection, units checks)
- ✅ Honest reporting (null results preserved)

**Purpose**: Make p-hacking impossible, make auditing easy.

### CMB Comb

Hypothesized periodic structure in Cosmic Microwave Background power spectrum with period Δℓ.

**UBT Variant C prediction**: Comb at Δℓ ∈ {8, 16, 32, 64, 128, 255}

**Planck PR3 result**: NULL (p = 0.919)

**Status**: Prediction falsified for temperature power spectrum channel

## Hubble Latency

### Hubble Tension

Discrepancy between early-universe (H₀ ≈ 67 km/s/Mpc) and late-universe (H₀ ≈ 73 km/s/Mpc) measurements of the Hubble parameter.

**Magnitude**: ~8-9% difference

**Standard explanations**: Early dark energy, modified gravity, systematic errors

**UBT explanation**: Synchronization latency (see below)

### Synchronization Latency (δ)

Fractional overhead required for global frame synchronization in discrete-time evolution.

**Definition**: δ = O / F

Where:
- **O**: Synchronization overhead (ticks)
- **F**: Frame length (256 ticks in UBT)

**UBT value**: δ ≈ 0.078 (O ≈ 20 ticks)

**Effect**: H₀_local ≈ H₀_global / (1 - δ)

**Interpretation**: Clock skew between local and global measurements, NOT new physics.

### Standard Siren

Gravitational wave event with electromagnetic counterpart, enabling independent H₀ measurement.

**Example**: GW170817 (neutron star merger)

**UBT prediction**: Standard sirens should show same δ ≈ 7.8% bias as distance ladder

**Status**: Awaiting sufficient statistics for validation

## Data Provenance

### SHA-256 Manifest

JSON file containing cryptographic hashes of all data files used in analysis.

**Purpose**: Ensures bit-exact reproducibility and detects corruption.

**Example structure**:
```json
{
  "generated": "2026-01-12T03:00:00",
  "hash_algorithm": "SHA-256",
  "files": [
    {
      "filename": "data.txt",
      "path": "DATA/planck_pr3/raw/data.txt",
      "size": 151876,
      "sha256": "a1b2c3d4..."
    }
  ]
}
```

**Validation**: Before running analysis, recompute hashes and compare. Abort if ANY file mismatches.

### Pre-Registration

Documenting test parameters **before** running the test.

**Required elements**:
- Observable channel
- Dataset(s)
- Analysis method
- Pass/fail criteria
- Random seed

**Purpose**: Prevents p-hacking (changing parameters to get desired result).

**Implementation**: Commit protocol to git before looking at results.

## Theoretical Framework

### ∇ (Biquaternionic Derivative)

Covariant derivative operator acting on biquaternionic fields.

**Properties**:
- Generalizes partial derivative to curved spacetime
- Respects quaternion multiplication rules
- Includes connection coefficients (like Christoffel symbols)

**Adjoint**: ∇† (complex conjugate transpose of ∇)

**Field equation**: ∇†∇Θ = κ𝒯

### 𝒯 (Energy-Momentum-Stress Tensor)

Biquaternionic generalization of stress-energy tensor from GR.

**Contains**:
- Energy density
- Momentum density
- Stress (pressure, shear)
- Complex/quaternion components (gauge field sources)

**Coupling**: κ = 8πG/c⁴ (Einstein's gravitational constant)

### Real Limit

The restriction of UBT to real time (ψ → 0) and real field components.

**Property**: In real limit, UBT **exactly reproduces** General Relativity.

**Implication**: All GR confirmations automatically validate UBT's real sector.

**Language**: "UBT generalizes GR", NOT "alternative to GR"

## Speculative Extensions (NOT Core UBT)

### Psychons

Hypothesized quantum excitations of consciousness field.

**Status**: SPECULATIVE (in `SPECULATIVE/`, not core UBT)

**Core UBT position**: Makes NO claims about consciousness.

### Closed Timelike Curves (CTCs)

Worldlines that loop back in time, allowing time travel.

**Status**: Exist mathematically (like in GR), not claimed to be physically realized

**Core UBT position**: Makes NO claims about observable time travel.

### Multiverse

Interpretation of parallel branches as separate universes.

**Status**: SPECULATIVE (in `SPECULATIVE/`, not core UBT)

**Core UBT position**: Parallel branches are coherent paths in single universe, NOT separate worlds.

## Repository Navigation

### THEORY/

Contains axioms, mathematical formalism, and architectural structure.

**Principle**: Clearly separate what is assumed vs derived.

### FINGERPRINTS/

Contains testable predictions organized by empirical status.

**Principle**: Null results are first-class outcomes.

### FORENSICS/

Contains court-grade testing protocols and pipelines.

**Principle**: Make p-hacking impossible, make auditing easy.

### HUBBLE_LATENCY/

Contains Hubble tension synchronization model.

**Principle**: Conservative language, clear disclaimers (NOT dark energy, NOT modified gravity).

### SPECULATIVE/

Contains consciousness, CTCs, multiverse, and other non-core content.

**Principle**: Clear separation prevents contamination of core scientific claims.

---

**For additional definitions**, see theory papers in repository root or contact maintainers.

**Last updated**: 2026-01-12
