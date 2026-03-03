# Research Operating System (ROS)

> Lightweight workflow for the Unified Biquaternion Theory repository.  
> All contributors must read this document before opening issues or pull requests.

---

## 1. Roles

### 1.1 Librarian
- **Responsibility**: Canonical source-of-truth keeper.
- **Actions**: Locates definitions, equations, and proofs within the repository; produces `path:line` citations; runs `grep`/ripgrep queries.
- **Constraints**: **NEVER commits code or theory changes.** Opens `canonical_gap` issues when definitions are missing.

### 1.2 Scientist
- **Responsibility**: Proposes theoretical structures, conjectures, and derivations.
- **Actions**: Opens `research_theory` issues; writes mathematical proposals in issues/comments; may attach diff previews.
- **Constraints**: Every claim **must cite repo evidence** (path:line from Librarian or self-found). Cannot merge without Auditor approval.

### 1.3 Engineer
- **Responsibility**: Implements code, tools, scripts, and refactors.
- **Actions**: Opens `engineering_task` issues; submits PRs referencing a Scientist proposal or a documented need.
- **Constraints**: **Cannot modify protected core paths** (see §5) without the `allow-core-change` label on the PR.

### 1.4 Experimentalist
- **Responsibility**: Designs and runs reproducible experiments.
- **Actions**: Opens `research_experiment` issues; adds executable scripts with run instructions; attaches output artifacts/logs.
- **Constraints**: Every experiment PR **must include execution instructions** and at least one output artifact or log file committed alongside the script.

### 1.5 Auditor (Opponent)
- **Responsibility**: Quality gate and skeptic.
- **Actions**: Verifies path:line citations, checks reproducibility, rejects unsupported claims, approves or blocks merges.
- **Constraints**: **Blocks merge** if Repo Grounding is missing or citations are unverifiable. Mandatory reviewer for all protected-path changes.

---

## 2. Repo Grounding Protocol

Every PR and every `research_theory` / `canonical_gap` issue **must** contain a **Repo Grounding** block:

```
## Repo Grounding
- <relative/path/to/file.tex>:<line_number> — <one-line quote or description>
- <relative/path/to/file.tex>:<line_number> — <one-line quote or description>
```

Rules:
1. At least **2 path:line citations** are required.
2. Citations must point to lines that actually exist in the repository at the time of the PR.
3. The Auditor verifies citations before approving.
4. If a concept has no canonical home yet, open a `canonical_gap` issue first.

---

## 3. Claim vs. Hypothesis Labeling

| Label | Meaning | Required evidence |
|---|---|---|
| `[CLAIM]` | Assertion believed to be established within UBT | Repo Grounding (≥2 citations) + derivation pointer |
| `[HYPOTHESIS]` | Conjecture not yet derived from first principles | Clearly marked speculative; no existing citation required |
| `[SPECULATION]` | Exploratory idea with minimal mathematical support | Must be placed in `speculative_extensions/` |

Use these prefixes in issue titles and PR sections where applicable.

---

## 4. How to Assign Work

1. **Identify the role** whose scope covers the task (§1).
2. **Open the corresponding issue template** (§6) and fill all required fields.
3. **Assign** the issue to the relevant contributor (or self-assign).
4. **Label** the issue:
   - `role:librarian`, `role:scientist`, `role:engineer`, `role:experimentalist`, `role:auditor`
   - `priority:high/medium/low`
   - `allow-core-change` (only if protected-path modification is justified)
5. The **Auditor** must be added as a reviewer on any PR touching protected paths.
6. For cross-role work, open **multiple linked issues** (one per role) and reference them in the PR.

---

## 5. Protected Paths

The following paths contain foundational theory and must **not** be modified without the `allow-core-change` label and mandatory Auditor review:

| Path | Reason |
|---|---|
| `original_release_of_ubt/` | Read-only archival scientific record — must not be modified |
| `canonical/` | Canonical definitions and derivations |
| `core/` | Core axioms and assumptions |
| `unified_biquaternion_theory/` | Original UBT formulation |

Changes to `docs/theory/`, `tools/`, and `experiments/` require the respective role owners as reviewers (see CODEOWNERS).

---

## 6. Issue Templates

| Template file | Use when |
|---|---|
| `research_theory.yml` | Proposing or discussing theoretical structure |
| `research_experiment.yml` | Designing or reporting a computational experiment |
| `engineering_task.yml` | Implementing code, tools, or refactors |
| `canonical_gap.yml` | A definition or proof is missing from canonical paths |

---

## 7. Merge Rules

1. All PRs require at least **1 approving review**.
2. PRs touching **protected paths** require the `allow-core-change` label **and** Auditor approval.
3. **Repo Grounding section** (≥2 path:line citations) must be present — enforced by CI (`repo_integrity_gate`).
4. Experiment PRs must pass the CI script-run check.
5. The Auditor may **block** a merge at any time by requesting changes; the block is only lifted by the Auditor themselves.
6. `[SPECULATION]` content must live under `speculative_extensions/` — PRs placing speculation elsewhere will be rejected.
