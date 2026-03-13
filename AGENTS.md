# AGENTS.md — Unified Biquaternion Theory Repository Protocol

This document defines rules for AI agents and contributors working in the
Unified Biquaternion Theory (UBT) repository.

The goal is to maintain:
- theoretical clarity
- structural stability of the repository
- minimal entropy in the theory tree
- reproducible scientific development

The repository is treated as a scientific theory laboratory, not a general
software project.

---

# 1. Core Philosophy

The repository is organized around a strict separation of:

- canonical/ → current best formulation of the theory
- research_tracks/ → active research directions
- speculative_extensions/ → conceptual extensions
- ARCHIVE/ → historical material

Agents must respect this separation.

No other top-level theory roots are allowed.

---

# 2. Canonical Theory Rules

The directory canonical/ contains the current reference formulation of UBT.

This means:
- the most internally consistent version of the theory
- the formulation we currently consider correct
- the formulation used for audits and publications

Canonical does not mean final or infallible.

However, canonical must remain low-speculation and mathematically defined.

---

## Material allowed in canonical

Content must satisfy at least one of the following:
- formal definitions of theory objects
- derivations used in the mainline theory
- mathematical structures required by the theory
- appendices supporting canonical derivations
- bridges between canonical sectors

---

## Material forbidden in canonical

The following must not appear in canonical:
- conceptual designs
- speculative ontologies
- philosophical interpretations
- experimental probes
- exploratory mathematical constructions
- unfinished derivations

Such work must go to:
research_tracks/
speculative_extensions/

---

# 3. Repository Discipline

Agents must treat repository structure as part of the scientific method.

## Root directory rules

Agents MUST NOT:
- create new directories in the repository root
- create parallel theory roots
- reorganize the repository structure without instruction

Allowed top-level directories:
canonical/
research_tracks/
speculative_extensions/
ARCHIVE/
docs/
tests/
tools/
scripts/
reports/

---

## Canonical directory rules

Agents MUST NOT:
- create new files in canonical unnecessarily
- duplicate existing derivations
- introduce competing formulations

Agents SHOULD:
- extend existing documents
- refine definitions
- improve derivations in place

Prefer editing existing files instead of creating new ones.

---

# 4. Scientific Development Rules

The following sectors define the theoretical core of UBT:

canonical/algebra/
canonical/fields/
canonical/geometry/
canonical/interactions/

Agents should prioritize work in these sectors.

---

# 5. Development Priorities

Agents should prioritize:
1. algebraic consistency of the biquaternion framework
2. field derivations from Θ(q, τ)
3. emergence of spacetime geometry
4. interaction structures (gauge sector)
5. compatibility with GR and Standard Model limits

Work that strengthens derivations is preferred.

---

# 6. What Agents Must Avoid

Agents must avoid:
- introducing speculative particles or entities
- adding ontology without equations
- modifying axioms without justification
- duplicating theory branches
- increasing repository complexity

Agents must always prefer clarification over expansion.

---

# 7. Change Strategy

When modifying theory content:
1. propose minimal change
2. implement change
3. verify internal consistency
4. avoid structural side effects

Large reorganizations must be avoided unless explicitly requested.

---

# 8. Promotion Workflow

New ideas must follow this path:
research_tracks → canonical (after validation)

Material must not enter canonical directly unless it is a refinement of an
existing canonical derivation.

---

# 9. Archival Policy

Scientific material must never be deleted.

Instead it should be moved to:
ARCHIVE/

for historical preservation.

---

# 10. Repository Design Principle

The repository should evolve toward:
- one canonical theory tree
- clear separation of research directions
- minimal structural entropy
- maximal theoretical clarity

Agents must treat repository structure as part of the theory itself.

---

# 11. Minimal Change Principle

Agents must prefer:
- editing existing files
- extending sections
- improving clarity

over:
- creating new files
- duplicating derivations
- fragmenting theory documents

---

# 12. Final Rule

When uncertain:
do less, not more.

Minimal, precise improvements are preferred over large speculative changes.
