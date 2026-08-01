<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->
<!-- Auto-generated sections are marked with BEGIN/END GENERATED markers.
     Run tools/generate_wiki.py to refresh them. -->
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
| Understand holographic structure and dS geometry | **[Holography](Holography)** — dS vs AdS structure, moduli space geometry, open tasks |
| QM / GR / stat-mech from one field equation | **[FPE Equivalence](FPE_Equivalence)** — Gap G3 Closed [L0] ⭐ — FPE ↔ EL Proved ALL sectors (U(1), SU(2), SU(3)) |
| QM emergence and Born rule | **[QM Emergence](QM_Emergence)** — Dirac, Schrödinger, Born rule from ℂ⊗ℍ |
| Why α⁻¹ = 137 is prime-stable | **[Prime Attractor](Prime_Attractor)** — V_eff minimum at n* = 137 |
| Why SU(2) is left-handed only | **[Chirality Derivation](Chirality_Derivation)** — ψ-parity selects SU(2)_L |
| QED at φ≠0 | **[QED Reproducibility](QED_Reproducibility)** — α, Schwinger term, Lamb shift |
| φ-Universe parameter and vacuum | **[φ-Universe](Phi_Universe)** — h_μν vacuum, moduli space |
| Common origin of 8π in GR and QFT | **[8π Origin](EightPi_Origin)** — dim_ℂ(ℂ⊗ℍ) = 4

---

## Derivation Status Summary

<!-- BEGIN GENERATED: status_summary -->
| Area | ✅ Proved | ⚡ Supported | ⚠️ Semi-emp. | 💭 Conjecture | ❌ Open/Dead-end |
|------|----------|------------|------------|-------------|----------------|
| Gauge Structure | 0 | 0 | 0 | 0 | 0 |
| Fine Structure Constant | 0 | 0 | 0 | 0 | 0 |
| Three Generations | 0 | 0 | 0 | 0 | 0 |
| Gravity / φ-Universe | 0 | 0 | 0 | 0 | 0 |
| Mirror Sector | 0 | 0 | 0 | 0 | 0 |
| Algebra | 0 | 0 | 0 | 0 | 0 |
| **Total** | **0** | **0** | **0** | **0** | **0** |
*Auto-generated from [`DERIVATION_INDEX.md`](https://github.com/UBT-Institute/unified-biquaternion-theory/blob/master/DERIVATION_INDEX.md). Dead Ends are counted in Open/Dead-end.*
<!-- END GENERATED: status_summary -->

---

## Canonical Theory Document

The full canonical theory is available as a compiled PDF, auto-built
from `canonical/UBT_canonical_main.tex` on every push to main:

🌐 **<a href="https://davj.github.io/unified-biquaternion-theory/canonical/UBT_canonical_main.html">View rendered (GitHub Pages)</a>**
· 📄 **<a href="https://davj.github.io/unified-biquaternion-theory/UBT_canonical_main.pdf">Download PDF</a>**
· 📝 **<a href="https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/UBT_canonical_main.tex">Raw .tex source</a>**

The PDF contains all canonical derivations with full LaTeX typesetting
and cross-references. For individual derivation files, follow links
in the wiki tables below.

---

## Interactive Notebooks

Key verification scripts are available as runnable Jupyter notebooks.
Launch them in the browser — no installation required:

<a href="https://mybinder.org/v2/gh/DavJ/unified-biquaternion-theory/master?filepath=docs/notebooks/"><img src="https://mybinder.org/badge_logo.svg"></a>

| Notebook | What it verifies |
|----------|-----------------|
| <a href="https://mybinder.org/v2/gh/DavJ/unified-biquaternion-theory/master?filepath=docs/notebooks/verify/verify_8pi_connection.ipynb">verify_8pi_connection</a> | Common algebraic origin of 8π in GR and QFT |
| <a href="https://mybinder.org/v2/gh/DavJ/unified-biquaternion-theory/master?filepath=docs/notebooks/verify/verify_su3_superposition.ipynb">verify_su3_superposition</a> | SU(3) from ℂ³ superposition over {I,J,K} |
| <a href="https://mybinder.org/v2/gh/DavJ/unified-biquaternion-theory/master?filepath=docs/notebooks/experiments/derive_fine_structure.ipynb">derive_fine_structure</a> | Fine structure constant derivation chain |
| <a href="https://mybinder.org/v2/gh/DavJ/unified-biquaternion-theory/master?filepath=docs/notebooks/research_tracks/e01_incidence_sanity.ipynb">e01_incidence_sanity</a> | UBT–Twistor incidence relation (flat Minkowski) |

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

<!-- BEGIN GENERATED: provenance_footer -->
---
> **AI provenance — Tier C (working):** AI assistance may have been used in
> drafting or maintenance. Exhaustive human review is not claimed. See the
> [repository provenance policy](https://github.com/UBT-Institute/unified-biquaternion-theory/blob/master/AI_PROVENANCE.md).
<!-- END GENERATED: provenance_footer -->
