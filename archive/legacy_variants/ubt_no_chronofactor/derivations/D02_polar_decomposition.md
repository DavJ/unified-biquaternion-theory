# D02: Polar Decomposition of Theta Field

## Overview

This derivation explores the decomposition of Θ(q) into amplitude and phase sectors.

**Key Result**: Θ admits a polar decomposition that separates "volume" (amplitude) from "orientation" (phase).

## Prerequisites

- D01: Theta Field and 8D Structure
- Complex analysis (exponential map, logarithm)
- Quaternion exponentials

## Motivation

The biquaternion Θ contains both magnitude and phase information. We seek a decomposition:

```
Θ(q) = |Θ(q)| · exp(iΦ(q))
```

where:
- |Θ(q)|: Amplitude/magnitude factor
- Φ(q): Phase structure

This separation will enable us to identify:
- **Amplitude channel** → Entropy → Metric (GR)
- **Phase channel** → Holonomy → Quantum structure

## Decomposition Schemes

### Scheme 1: Exponential Map

```
Θ = ||Θ|| · exp(Φ)
```

where Φ is a "phase quaternion."

**Challenge**: Defining quaternion exponential for complex-valued arguments.

### Scheme 2: Component-wise Polar Form

```
Θᵢ = rᵢ exp(iφᵢ)    (i = 0,1,2,3)
```

**Advantage**: Uses standard complex exponential for each component.

**Challenge**: How to aggregate 4 separate phases into single Φ(q)?

### Scheme 3: Determinant-based

```
|Θ| = (det(Θ†Θ))^(1/4)
Phase structure from arg det Θ
```

**Advantage**: Coordinate-free, uses invariant (determinant).

**Challenge**: Losing information about individual component phases.

## Proposed Decomposition

For UBT Core, we adopt a **mixed approach**:

1. **Global magnitude**: 
   ```
   |Θ| = ||Θ|| = sqrt(Θ†Θ)
   ```

2. **Normalized field**:
   ```
   Θ̂ = Θ / ||Θ||    (unit biquaternion)
   ```

3. **Phase extraction from Θ̂**:
   - Individual component phases: φᵢ = arg(Θᵢ)
   - Global phase: Φ_global = arg det Θ

## Relationship to Observables

The observables S_Θ and Σ_Θ are defined from this decomposition:

```
S_Θ = 2 k_B ln |det Θ| ≈ function of |Θ|
Σ_Θ = k_B arg det Θ = function of Φ_global
```

## Open Questions

1. **Uniqueness**: Is the decomposition Θ = |Θ| exp(iΦ) unique? What gauge freedom remains?

2. **Geometric meaning**: Does Φ represent a point on some phase manifold (e.g., SU(2), U(1)⁴)?

3. **Coupling**: How do amplitude and phase channels interact dynamically?

4. **Quaternion vs complex**: Should we use quaternionic exponentials or complex exponentials for each component?

## Next Steps

- **D03**: Use this decomposition to define S_Θ and Σ_Θ rigorously
- **D04**: Show how |Θ| sector gives metric
- **D05**: Show how Φ sector gives spinor coupling

## References

- D01: Theta Field and 8D Structure
- `/ubt_core/README.md` - Observable definitions
- `/ubt_core/entropy_phase.py` - Implementation

---

**Status**: Stub created  
**Last Updated**: 2026-02-17  
**Author**: UBT Core Team
