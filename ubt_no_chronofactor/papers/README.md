# UBT Core Papers

This directory contains research papers and documents for the **chronofactor-free UBT Core formulation**.

## Purpose

Papers in this directory present the UBT Core framework:
- **No external chronofactor**: τ = t + iψ is not used
- **8D phase-capable field**: Θ(q) as the sole primitive
- **Clean-room derivations**: Built from first principles

## Current Papers

### Main Paper (In Development)

**File**: `ubt_core_no_chronofactor_outline.md` (stub)

**Title**: "Unified Biquaternion Theory: A Chronofactor-Free Formulation"

**Abstract**: We present a reformulation of Unified Biquaternion Theory (UBT) where all physics emerges from an 8-dimensional phase-capable field Θ(q) at each spacetime point, without invoking an external chronofactor parameter. The theory recovers General Relativity from the entropy channel and quantum mechanics from the phase channel, with nonlocal correlations arising from topological holonomy rather than extra dimensions.

**Status**: 🚧 Outline phase

---

## Paper Development Roadmap

### Phase 1: Foundations (Current)
- [ ] Complete derivations D01-D06
- [ ] Establish core definitions and notation
- [ ] Python implementation of Θ field and observables

### Phase 2: Main Results
- [ ] GR recovery proof (from D04)
- [ ] Quantum coupling derivation (from D05)
- [ ] Holonomy framework (from D06)

### Phase 3: Validation
- [ ] Comparison with legacy chronofactor formulation
- [ ] Numerical tests of key predictions
- [ ] Consistency checks

### Phase 4: Publication
- [ ] Full draft manuscript
- [ ] Figures and visualizations
- [ ] Peer review preparation

## Paper Structure (Planned)

### 1. Introduction
- Motivation: Why remove chronofactor?
- Overview of UBT Core approach
- Comparison to Standard Model + GR

### 2. Fundamental Field
- Biquaternion definition (from D01)
- 8D structure and degrees of freedom
- No chronofactor axiom

### 3. Observables
- Entropy channel S_Θ (from D03)
- Phase channel Σ_Θ (from D03)
- Polar decomposition (from D02)

### 4. General Relativity Emergence
- Metric from entropy (from D04)
- Einstein equations recovery
- Schwarzschild and FLRW solutions

### 5. Quantum Mechanics Emergence
- Dirac coupling (from D05)
- Gauge structure from phase
- Spin and fermion dynamics

### 6. Nonlocality and Topology
- Phase holonomy (from D06)
- EPR correlations
- Bell inequality violation

### 7. Comparison to Legacy
- Mapping to chronofactor formulation
- Physical equivalence in observable sector
- Conceptual advantages

### 8. Conclusions
- Summary of key results
- Open questions
- Future directions

## Supporting Documents

### Technical Reports
- Detailed calculations (supplements to main paper)
- Numerical validation results
- Algorithm implementations

### Comparison Studies
- UBT Core vs Legacy UBT (chronofactor)
- UBT Core vs String Theory
- UBT Core vs Loop Quantum Gravity

### Educational Materials
- Tutorial: "Introduction to Biquaternion Field Theory"
- Explainer: "Why 8D? A Visual Guide"
- FAQ: "Common Questions about UBT Core"

## Legacy Papers

Papers written with chronofactor assumptions are located in:
```
/legacy/ubt_with_chronofactor/papers/
```

These are preserved for:
- Historical reference
- Regression testing
- Comparison studies

## Writing Guidelines

When contributing papers to this directory:

1. **No chronofactor**: Never introduce τ = t + iψ as a primitive
2. **From first principles**: Build from Θ(q) definition
3. **Clear notation**: Define all symbols before use
4. **Cite derivations**: Reference D01-D06 as needed
5. **Comparison section**: Include mapping to legacy formulation where relevant

## File Naming Convention

- Main papers: `ubt_core_[topic].tex` or `.md`
- Technical reports: `tech_report_[topic].tex` or `.md`
- Comparison studies: `comparison_[topic].tex` or `.md`
- Educational: `tutorial_[topic].md`

## LaTeX Setup

For LaTeX papers, include:

```latex
\documentclass{article}
\usepackage{amsmath, amssymb}

% UBT Core notation
\newcommand{\Theta}{\boldsymbol{\Theta}}
\newcommand{\Stheta}{S_{\Theta}}
\newcommand{\Sigmatheta}{\Sigma_{\Theta}}
```

## Status

- ✅ **Directory created**: Ready for paper development
- 🚧 **Main paper outline**: In planning phase
- 🚧 **Derivations**: Being completed in `/derivations/`
- ⏳ **Full draft**: Pending completion of derivations

## Next Steps

1. Complete derivations D01-D06
2. Create outline document for main paper
3. Begin writing individual sections
4. Develop figures and visualizations

## References

- **Core definitions**: `/ubt_core/README.md`
- **Derivations**: `/derivations/README.md`
- **Legacy formulation**: `/legacy/ubt_with_chronofactor/`

---

**Maintainer**: UBT Core Team  
**Last Updated**: 2026-02-17
