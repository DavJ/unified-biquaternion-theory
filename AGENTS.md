# AGENTS.md — Unified Biquaternion Theory Development Protocol

This document defines operational rules for AI agents and contributors working
inside the Unified Biquaternion Theory (UBT) repository.

The repository is treated as a **scientific research environment**, not a
generic software project.

Agents must preserve both:

• theoretical consistency  
• repository structural stability  

---

# 1. Repository Structure

The repository follows a strict separation of concerns.

canonical/
Current best internally consistent formulation of UBT.

research_tracks/
Active research directions that are not yet canonical.

speculative_extensions/
Conceptual or exploratory ideas not yet mathematically closed.

ARCHIVE/
Historical or superseded material.

Agents must respect this separation.

No additional top-level theory roots may be created.

---

# 2. Root Directory Discipline

Agents MUST NOT:

• create new directories in repository root  
• duplicate theory trees  
• reorganize repository structure without instruction  

Allowed root directories:

canonical/
research_tracks/
speculative_extensions/
ARCHIVE/
docs/
tests/
tools/
scripts/
reports/

If new material is created, it must go into an existing category.

---

# 3. Canonical Theory Rules

canonical/ contains the **current reference formulation of UBT**.

Canonical means:

• internally consistent  
• mathematically defined  
• used for audits and publications  

Canonical does NOT mean final or infallible.

---

Material allowed in canonical:

• definitions of theory objects  
• core algebraic structures  
• main derivations  
• appendices supporting canonical derivations  
• bridges between theory sectors  

---

Material forbidden in canonical:

• conceptual designs  
• philosophical interpretations  
• experimental probes  
• incomplete derivations  
• speculative ontologies  

Such work belongs in:

research_tracks/
speculative_extensions/

---

# 4. Core Mathematical Structure of UBT

UBT is built around the following structural components.

Agents must preserve compatibility with these elements.

## Algebra

Biquaternion algebra

ℂ ⊗ ℍ

This algebra forms the base mathematical structure of the theory.

Located in:

canonical/algebra/

---

## Fundamental Field

The fundamental field of the theory is:

Θ(q, τ)

where:

q = biquaternion coordinate  
τ = complex time parameter

Θ is treated as a generating structure for fields and geometry.

Located in:

canonical/fields/

---

## Emergent Geometry

Spacetime geometry is derived from the Θ field structure.

Located in:

canonical/geometry/

Agents must preserve compatibility with the GR limit.

---

## Interaction Sector

Gauge structures and interaction sectors are located in:

canonical/interactions/

Agents should maintain compatibility with:

SU(3) × SU(2) × U(1)

as the Standard Model limit.

---

# 5. Development Priorities

Agents should prioritize improvements in:

1. algebraic consistency of the biquaternion framework
2. derivations involving Θ(q, τ)
3. emergence of metric structure
4. interaction sector derivations
5. compatibility with GR and Standard Model limits

Work that strengthens derivations is preferred over new speculation.

---

# 6. Open Problems

Agents should be aware that some aspects of the theory remain open.

Examples include:

• derivation of the fine structure constant α  
• derivation of particle mass spectrum  
• deeper structure of Θ spectral modes

Work on these problems belongs in research_tracks unless fully derived.

---

# 7. What Agents Must Avoid

Agents must avoid:

• introducing new entities without equations  
• adding ontology without mathematical definition  
• duplicating theory structures  
• increasing repository structural entropy  

Agents should prefer **clarification over expansion**.

---

# 8. Change Strategy

When modifying theory content:

1. propose minimal change
2. modify existing file
3. verify consistency with canonical structure
4. avoid structural side effects

Agents should prefer editing existing documents rather than creating new ones.

---

# 9. Promotion Workflow

New theory elements must follow this progression:

research_tracks → canonical

Promotion requires:

• internal consistency  
• mathematical closure  
• compatibility with canonical structure

---

# 10. Archival Policy

Scientific content must never be deleted.

Historical material should be moved to:

ARCHIVE/

This preserves reproducibility of theory evolution.

---

# 11. Minimal Change Principle

Agents must prefer:

• extending existing documents
• refining definitions
• clarifying derivations

over:

• creating new files
• duplicating derivations
• fragmenting the theory

---

# 12. Repository Philosophy

The repository should evolve toward:

• one canonical theory tree
• clear research tracks
• minimal structural entropy
• maximal theoretical clarity

Agents must treat repository organization as part of the scientific method.

---

# 13. Final Rule

When uncertain:

**do less, not more.**

Minimal precise improvements are preferred over speculative expansion.

