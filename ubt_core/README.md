# UBT Core: Chronofactor-Free Formulation

This directory contains the **core canonical implementation** of Unified Biquaternion Theory (UBT) without any external/global chronofactor parameter.

## Fundamental Axioms

### 1. The Θ Field: 8D Phase-Capable Structure

The fundamental field Θ(q) is defined at each spacetime point q as a **biquaternion** (complex quaternion):

```
Θ(q) ∈ ℍ ⊗ ℂ ≅ ℂ^4
```

**Explicit representation**:
```
Θ(q) = Θ₀(q) + iΘ₁(q) + jΘ₂(q) + kΘ₃(q)
```

where each component Θᵢ(q) ∈ ℂ is complex-valued, giving **8 real degrees of freedom**:

```
Θᵢ(q) = Aᵢ(q) + iφᵢ(q)    (i = 0,1,2,3)
```

- **Amplitude channel**: Aᵢ(q) ∈ ℝ (4 real amplitudes)
- **Phase channel**: φᵢ(q) ∈ ℝ (4 real phases)

### 2. No External Chronofactor

**Critical statement**: This formulation does **NOT** include an external/global chronofactor parameter τ.

- ❌ **Not used**: τ = t + iψ as a separate input
- ❌ **Not used**: Complex time as a universal parameter
- ✅ **Instead**: All phase information is **intrinsic** to the 8D structure of Θ(q)

The field Θ depends only on spacetime coordinates q = (t, x, y, z), with all phase dynamics encoded within the field itself.

## Polar Decomposition (Conceptual)

The field Θ(q) can be conceptually decomposed into amplitude and phase sectors:

```
Θ(q) = |Θ(q)| · exp(iΦ(q))
```

where:
- **|Θ(q)|**: Amplitude magnitude (related to entropy channel)
- **Φ(q)**: Phase structure (related to holonomy channel)

**Note**: This is a conceptual split. The specific mathematical decomposition will be developed in the derivations. We do not commit to a unique decomposition here.

## Core Observables

### Entropy Channel: S_Θ

The entropy associated with the Θ field is defined as:

**Primary definition**:
```
S_Θ(x) = 2 k_B ln |det Θ(x)|
```

**Equivalent form** (using Hermitian conjugate):
```
S_Θ(x) = k_B ln det(Θ†(x) Θ(x))
```

where:
- k_B is Boltzmann's constant
- det Θ is the quaternionic determinant
- |det Θ| is the absolute value of the determinant

**Physical interpretation**: S_Θ measures the "volume" occupied by the biquaternionic field configuration in its internal space. This entropy channel will be shown to relate to the emergent metric structure (General Relativity recovery) through the **real channel** projection.

### Phase Channel: Σ_Θ

The phase observable associated with the Θ field is defined as:

```
Σ_Θ(x) = k_B arg det Θ(x)
```

where arg det Θ is the argument (phase) of the quaternionic determinant.

**Physical interpretation**: Σ_Θ measures topological/holonomic properties of the field configuration. This phase channel is a candidate for:
- **Holonomy constraints**: Global phase winding and topological sectors
- **Nonlocal correlations**: Phase coherence across spatial regions
- **Quantum mechanical phase**: Connection to Dirac spinor dynamics

**Critical distinction**: Σ_Θ is **not** an external chronofactor. It is an intrinsic observable derived from the internal phase structure of Θ(q).

## Nonlocality and Phase Constraints

Nonlocal correlations in UBT are encoded through:

1. **Global phase constraints**: Holonomy conditions on Σ_Θ around closed loops
2. **Topological sectors**: Different winding numbers of the phase field Φ(q)
3. **8D Θ-phase space structure**: Internal phase relationships within the 8D field

**Not via**:
- ❌ Extra dimensions beyond 4D spacetime
- ❌ External chronofactor time-like parameter
- ❌ Additional hidden variables

## Physical Channels (Emergent Structure)

From the 8D Θ field, two primary physical channels emerge:

### Real Channel (Amplitude) → Metric Structure
- **Source**: Amplitude components Aᵢ(q) and entropy S_Θ
- **Emergent**: Spacetime metric g_μν (General Relativity)
- **Observable**: Gravitational field, curvature, Einstein equations

### Phase Channel → Quantum Structure  
- **Source**: Phase components φᵢ(q) and holonomy Σ_Θ
- **Emergent**: Dirac spinor coupling, gauge fields
- **Observable**: Quantum mechanical phase, fermion dynamics

**Key principle**: These channels are **coupled** through the unified structure of Θ, but can be analyzed separately in appropriate limits.

## Mapping to Legacy Formulation

The legacy formulation (see `legacy/ubt_with_chronofactor/`) used an external chronofactor τ = t + iψ:

```
Θ_legacy(q, τ) = Θ(q) · f(τ)
```

In the **core formulation**:
- The dependence on imaginary time ψ is **removed**
- All phase information is **internalized** within Θ(q)
- The factor f(τ) is either absorbed into Θ or treated as a legacy artifact

**Conceptual shift**: Instead of "complex time evolution," we have "phase-capable field dynamics."

## Implementation

This directory contains placeholder implementations:

- **`theta_field.py`**: Object model for Θ field, basic operations
- **`entropy_phase.py`**: Definitions and calculations for S_Θ and Σ_Θ

Full derivations and detailed implementations are in the **`derivations/`** directory.

## Next Steps

1. **Derivations**: See `/derivations/README.md` for systematic development
2. **Papers**: See `/papers/README.md` for research documents
3. **Legacy comparison**: See `/legacy/ubt_with_chronofactor/README.md` for prior formulation

## Status

- ✅ **Axioms defined**: Core field structure and observables
- ✅ **Chronofactor removed**: No external τ parameter
- 🚧 **Derivations in progress**: See derivations directory
- 🚧 **Papers in development**: See papers directory

---

**Key Takeaway**: UBT Core treats Θ(q) as an **8D phase-capable field** at each spacetime point, with all dynamics emerging from this structure—**no external chronofactor required**.
