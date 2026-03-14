<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->
<!-- Auto-generated sections are marked with BEGIN/END GENERATED markers.
     Run tools/generate_wiki.py to refresh them. -->

# Unified Biquaternion Theory — Wiki Home

**Author**: Ing. David Jaroš  
**License**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)  
**Repository**: [DavJ/unified-biquaternion-theory](https://github.com/DavJ/unified-biquaternion-theory)

---

## What is UBT?

The **Unified Biquaternion Theory (UBT)** is a theoretical physics framework that
unifies General Relativity, Quantum Field Theory, and Standard Model symmetries
within a single biquaternionic field defined over **complex time** τ = t + iψ.

The fundamental object is the biquaternion field **Θ(q, τ)**, from which spacetime
geometry, gauge interactions, and particle content emerge without free parameters at
the structural level.

---

## Theory Architecture

```
ℂ⊗ℍ  (Biquaternion algebra)
  └─▶  Θ(q,τ)  (Fundamental field over complex time)
         ├─▶  g_μν   Spacetime metric  →  GR in real limit
         ├─▶  SU(3)×SU(2)_L×U(1)_Y  →  Standard Model gauge group
         ├─▶  ψ-modes  →  Three fermion generations (conjecture)
         └─▶  n* = 137  →  Fine structure constant (semi-empirical)
```

See the full architecture in [Overview](Overview).

---

## Quick Navigation

| Goal | Page |
|------|------|
| Understand the theory structure | [Overview](Overview) |
| Read canonical theory definitions | [Canonical Theory](Canonical_Theory) |
| Check derivation status of a claim | [Derivations](Derivations) |
| Find mathematical foundations | [Mathematical Foundations](Mathematical_Foundations) |
| See open research questions | [Research Tracks](Research_Tracks) |
| Read speculative extensions | [Speculative Extensions](Speculative_Extensions) |

---

## Derivation Status Summary

<!-- BEGIN GENERATED: status_summary -->
| Area | ✅ Proved | ⚡ Supported | ⚠️ Semi-emp. | 💭 Conjecture | ❌ Open/Dead-end |
|------|----------|------------|------------|-------------|----------------|
| Gauge Structure | 11 | 0 | 1 | 0 | 0 |
| Fine Structure Constant | 7 | 0 | 3 | 1 | 3 |
| Three Generations | 5 | 2 | 5 | 5 | 7 |
| Gravity / φ-Universe | 15 | 0 | 0 | 1 | 2 |
| Mirror Sector | 1 | 3 | 0 | 3 | 0 |
| Algebra | 3 | 0 | 0 | 1 | 2 |
| **Total** | **42** | **5** | **9** | **11** | **14** |
*Auto-generated from [`DERIVATION_INDEX.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/DERIVATION_INDEX.md). Dead Ends are counted in Open/Dead-end.*
<!-- END GENERATED: status_summary -->

---

## Repository Structure

| Directory | Contents |
|-----------|----------|
| [`canonical/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical) | Current canonical UBT formulation |
| [`research_tracks/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/research_tracks) | Active exploratory directions |
| [`speculative_extensions/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/speculative_extensions) | Conceptual extensions beyond canonical theory |
| [`ARCHIVE/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/ARCHIVE) | Historical and superseded material |
| [`tools/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/tools) | Computation and validation scripts |
| [`experiments/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/experiments) | Experimental computations |

**Single source of truth for derivation status**:
[`DERIVATION_INDEX.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/DERIVATION_INDEX.md)

---

*This wiki summarises the theory — it does not duplicate derivations. All claims
link to canonical source files in the repository.*
