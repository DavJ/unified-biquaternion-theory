# Repository Structure Guide

**Last Updated:** 2026-03-12  
**Purpose:** Help any reader navigate the repository in under 2 minutes.

---

## Quick Navigation

| Want to… | Go to… |
|---|---|
| Read the canonical UBT formulation | [`core/UBT_canonical_main.tex`](../core/UBT_canonical_main.tex) |
| Understand the 5 top-level sections | This document, §Sections below |
| Check derivation status of a claim | [`DERIVATION_INDEX.md`](../DERIVATION_INDEX.md) |
| Find the current theory status | [`CURRENT_STATUS.md`](../CURRENT_STATUS.md) |
| Understand what is proved vs. open | [`docs/THEORY_STATUS.md`](THEORY_STATUS.md) |

---

## Top-Level Directory Map

```
unified-biquaternion-theory/
├── core/                       ← Canonical physics/math (start here)
├── research_tracks/            ← Active non-mainline research
├── speculative_extensions/     ← Speculative/unproved extensions
├── experiments/                ← Numerical scans, code, computations
├── archive/                    ← Superseded/deprecated content
├── docs/                       ← Process, governance, meta documents
├── README.md                   ← Entry point
├── DERIVATION_INDEX.md         ← Derivation status index
└── CURRENT_STATUS.md           ← Theory status snapshot
```

---

## Sections

### `core/` — Canonical Physics and Math

**What it is:** The single authoritative formulation of Unified Biquaternion Theory. Contains only current-best, internally consistent, low-speculation physics and mathematics.

**When to read it:** When you want to understand what UBT actually claims, what has been proved, and what the canonical definitions are.

**Entry point:** `core/UBT_canonical_main.tex`  
**Definitions:** `core/CANONICAL_DEFINITIONS.md`  
**Scope policy:** `core/SCOPE.md`

**Subdirectories:**
| Directory | Contents |
|---|---|
| `algebra/` | Biquaternion algebra foundations |
| `appendices/` | Canonical appendices (symbol dictionary) |
| `bridges/` | Navigation bridge files (cross-references to proofs) |
| `fields/` | Canonical field definitions (Θ, T_B, algebra) |
| `geometry/` | Metric, connection, curvature, GR limit |
| `gr_limit/` | Full GR recovery derivation |
| `interactions/` | QED, QCD, SM gauge structure |

**Does NOT contain:** Consciousness, fingerprint tests, universe-as-atom, roadmap/checklist documents.

---

### `research_tracks/` — Active Non-Mainline Research

**What it is:** Active research directions that are not yet in the canonical mainline. These are investigative, may be inconclusive, and may eventually graduate to `core/` or be retired to `archive/`.

**When to read it:** When you want to follow active open problems or side investigations.

**Tracks:**
| Track | Topic |
|---|---|
| `associative_su3/` | SU(3) emergence from biquaternion involutions |
| `fingerprints/` | Spectral parity tests and coding fingerprints |
| `octonionic_completion/` | Octonionic extension hypothesis |
| `three_generations/` | Three-generation mechanism via ψ-winding |

---

### `speculative_extensions/` — Speculative and Unproved Extensions

**What it is:** Extrapolations beyond the proved UBT core. Includes consciousness models, cosmological speculation, and causality extensions. **These are speculative** — not proved results, not canonical UBT.

**When to read it:** When you are interested in the speculative implications of the framework, clearly understood as unverified.

**Subdirectories:**
| Directory | Topic |
|---|---|
| `P3_consciousness_model/` | Toy model for consciousness decision dynamics |
| `appendices/` | Speculative appendices (psychons, CTC, multiverse, Hubble tension) |
| `causality/` | Closed timelike curves, chronology protection |
| `consciousness/` | Psychon field and consciousness claims |
| `cosmology_or_metaphysics/` | Universe-as-atom and related speculation |
| `invisibility/` | Imaginary sector invisibility |
| `solution_consciousness_model_P3/` | P3 consciousness model derivation |

---

### `experiments/` — Numerical Computations and Code

**What it is:** Numerical experiments, parameter scans, code for deriving or testing specific UBT predictions. Outputs may feed back into `research_tracks/` or `core/` when results stabilise.

**When to read it:** When you want to reproduce a numerical result or run a computation.

**Contents:**
| Directory | Topic |
|---|---|
| `constants_derivation/` | Fine structure constant numerical derivation |
| `layer2_stability/` | Layer-2 rigidity and stability sweeps |

---

### `archive/` — Superseded and Deprecated Content

**What it is:** Files that are no longer part of the active theory but are preserved for reproducibility, history, and reference. Includes abandoned research tracks, historical status snapshots, old derivation attempts.

**When to read it:** When you need to understand why a certain approach was abandoned, or to reproduce historical results.

**See also:** `archive/README.md` for the archive policy, and `archive/archive_manifest.tsv` for a complete index of archived files with reasons.

**Contents:**
| Directory | Contents |
|---|---|
| `abandoned_tracks/` | Research directions that reached dead ends |
| `deprecated/` | Deprecated status documents and old research tracks |
| `historical_versions/` | Repository snapshots and old status files |

---

### `docs/` — Process, Governance, and Meta Documents

**What it is:** Documents about the project process, governance, publication plans, verification reports, and project history. Not primary physics content.

**When to read it:** When you need to understand the development process, review governance decisions, or find publication guidance.

**Key files:**
| File | Purpose |
|---|---|
| `THEORY_STATUS.md` | Full theory status map (Mermaid diagram) |
| `THEORY_STATUS_SUMMARY.md` | Summary table of proof status |
| `REPOSITORY_STRUCTURE.md` | This file — navigation guide |
| `CONSOLIDATION_ROADMAP.md` | Consolidation process roadmap |
| `IMPLEMENTATION_CHECKLIST.md` | Implementation checklist |
| `REVIEWER_FAQ.md` | FAQ for external reviewers |
| `REPLICATION_PROTOCOL.md` | Replication instructions |
| `DERIVATION_INDEX.md` | (copy) derivation status index |

---

## Other Top-Level Directories

These exist but are secondary:

| Directory | Purpose |
|---|---|
| `ARCHIVE/` | Upper-case ARCHIVE — older archive format; see `archive/` (lowercase) for current |
| `AUDITS/` | Audit reports on claims and overlaps |
| `DATA/` | Scientific datasets (Planck PR3, WMAP, modular forms) |
| `FINGERPRINTS/` | Fingerprint candidates and confirmed results |
| `HUBBLE_LATENCY/` | Hubble tension latency model |
| `THEORY/` | Topic indexes and architecture documents |
| `THEORY_COMPARISONS/` | Comparisons with other theories (Penrose, SU(3) qubit, etc.) |
| `consolidation_project/` | Historical consolidation work (partial consolidations) |
| `unified_biquaternion_theory/` | Original UBT documents — read-only historical archive |

---

## Five-Minute Reading Path for an External Reviewer

1. **Start**: `README.md` — overview and proof status table (2 min)
2. **Claims**: `DERIVATION_INDEX.md` — what is proved vs. open (3 min)
3. **Physics**: `core/UBT_canonical_main.tex` — canonical formulation (read as needed)
4. **Status**: `docs/THEORY_STATUS.md` — full status map with Mermaid diagram
5. **Speculative**: `speculative_extensions/README.md` — what is NOT claimed to be proved

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
