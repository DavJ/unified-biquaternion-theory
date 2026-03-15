<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# Derivations

This section tracks the derivation status of all major UBT results.

**Single source of truth**: [`DERIVATION_INDEX.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/DERIVATION_INDEX.md)  
**Full theory map**: [`docs/THEORY_MAP_FROM_DERIVATION_INDEX.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/THEORY_MAP_FROM_DERIVATION_INDEX.md)

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | **Proved** — rigorous derivation, zero free parameters |
| ⚡ | **Supported** — strong numerical or structural evidence |
| ⚠️ | **Semi-empirical** — structural derivation with ≥1 free parameter |
| ❌ | **Open Hard Problem** — no known derivation path |
| 💭 | **Conjecture** — proposed but not derived |

---

## Pages in This Section

| Page | Key Claim | Status |
|------|-----------|--------|
| [GR Recovery](GR_Recovery) | Einstein equations from UBT | ✅ Steps 1–5 Proved |
| [Fine Structure Constant α](Alpha_Constant) | α⁻¹ = 137.036 | ⚠️ Semi-empirical |
| [SU(3) Structure](SU3_Structure) | Color gauge group from ℂ⊗ℍ | ✅ Proved [L0] |
| [Hecke / Modular Structure](Hecke_Modular_Structure) | Lepton masses via Hecke at p=137 | ⚡ Numerical support |
| [Mirror Sector](Mirror_Sector) | Twin prime 139 mirror sector | ⚡ Numerical observation |

---

## Overall Derivation Summary

<!-- BEGIN GENERATED: derivation_summary -->
| Area | ✅ Proved | ⚡ Supported | ⚠️ Semi-emp. | 💭 Conjecture | ❌ Open/Dead-end |
|------|----------|------------|------------|-------------|----------------|
| Gauge Structure | 20 | 1 | 1 | 0 | 3 |
| Fine Structure Constant | 10 | 0 | 3 | 1 | 4 |
| Three Generations | 5 | 2 | 5 | 5 | 8 |
| Gravity / φ-Universe | 18 | 0 | 0 | 1 | 1 |
| Mirror Sector | 2 | 3 | 0 | 3 | 0 |
| Algebra | 21 | 0 | 0 | 0 | 3 |
| **Total** | **76** | **6** | **9** | **10** | **19** |
*Auto-generated from [`DERIVATION_INDEX.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/DERIVATION_INDEX.md). Dead Ends are counted in Open/Dead-end.*
<!-- END GENERATED: derivation_summary -->

---

## How to Read DERIVATION_INDEX.md

Each section in DERIVATION_INDEX.md covers one major topic:
- A blockquote pointing to the ⭐ canonical source and topic index file
- A Markdown table with columns: Result | Status | File | Notes

Status labels in the table follow the Layer convention:
- `[L0]` = pure biquaternionic geometry (no quantum corrections)
- `[L1]` = one-loop quantum corrections
- `[L2]` = higher-loop or non-perturbative

The topic index files in [`canonical/THEORY/topic_indexes/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical/THEORY/topic_indexes)
provide a quick-reference entry point per topic with links to canonical sources.
