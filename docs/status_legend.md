# Status Legend for UBT Repository Claims

**Path**: `docs/status_legend.md`  
**Date**: 2026-03-11  
**Authority**: This document defines the canonical vocabulary for status labels
used across all UBT repository files.

---

## 1. Allowed Status Labels

All claims in UBT documents **must** use exactly one of the following labels.
Do not use synonyms, degree-qualifiers ("almost proved"), or informal phrasing
("basically done").

### ✅ `proved`

**Definition**: The claim follows by rigorous mathematical argument from stated
assumptions, with all key steps spelled out and no unverified logical gaps.

**Criteria**:
- All assumptions are explicit and justified.
- Every step follows from a prior result or a standard reference.
- The proof has been reviewed and no gap is known.
- Computational checks (if any) are exact (symbolic), not numerical.

**May NOT be used when**:
- The argument relies on unproved intermediate steps.
- The conclusion holds only under a genericity assumption that is not proved.
- Coefficients or parameters are fitted (empirically chosen), not derived.
- The result holds only for a special case or ansatz without an extension theorem.

**Examples**:
- The linearized GR recovery from UBT (first-order perturbations): ✅ proved
- det(X) = Minkowski interval for X = x^μ σ_μ: ✅ proved
- Lorentzian signature from Clifford algebra structure: ✅ proved
  (conditional on admissible-class assumption; assumption stated explicitly)

---

### 🔬 `computationally_verified`

**Definition**: The claim has been checked by symbolic computation (exact arithmetic)
or by numerical computation (floating point), with a proof sketch present but not
fully fleshed out.

**Criteria**:
- Code exists and tests pass.
- The numerical/symbolic check covers representative cases.
- A proof sketch or informal argument explains why the result should hold.
- No known counterexample.

**May NOT be used when**:
- Code produces results but no theoretical justification exists.
- The computation is only approximate with large error.
- Only a single case has been tested.

**Examples**:
- Conformal Möbius action on X preserves light-cone structure (tested numerically
  for random SU(2,2) matrices): 🔬 computationally_verified
- Commutator closure of UBT generators converges to dim-15 algebra: 🔬 computationally_verified

---

### 📊 `semi_empirical`

**Definition**: The claim matches observational or experimental data, but the
derivation from first principles is incomplete.  Fitted parameters are involved,
or one or more links in the derivation chain use empirical input.

**Criteria**:
- Numerical agreement with experiment is demonstrated.
- At least one free parameter is fitted (not derived) or at least one step
  uses empirical data as input.
- The claim is physically meaningful and the fit is non-trivial.

**May NOT be used when**:
- All parameters are derived from first principles with no fitting.
  (Use `proved` or `computationally_verified` in that case.)

**Examples**:
- Fine-structure constant with higher-order corrections (fitted structural
  corrections): 📊 semi_empirical
- Fermion mass ratios (fitted mixing angles): 📊 semi_empirical

---

### 🔶 `indicated`

**Definition**: The evidence is consistent with the claim but a rigorous proof
or confirmed isomorphism is lacking.  Dimension counting, signature matching,
or pattern recognition are the primary evidence.

**Criteria**:
- Multiple independent evidences point in the same direction.
- No counterexample is known.
- An upgrade criterion (what would be needed to prove it) is stated.

**May NOT be used when**:
- A single coincidence is the only evidence.
- The claim has no upgrade criterion stated.

**Examples**:
- UBT generator algebra ≅ su(2,2) (dimension 15, signature (8,7,0) match,
  but no explicit isomorphism): 🔶 indicated

---

### ❓ `open`

**Definition**: The question is not resolved.  Neither a proof nor a disproof
is known.  Active investigation may or may not be ongoing.

**Criteria**:
- The question is precisely stated.
- No confirmed answer exists.

**Examples**:
- Mapping of UBT phase ψ to twistor geometry: ❓ open
- Off-shell injectivity of Θ ↦ g[Θ]: ❓ open
- Full non-perturbative GR embedding (Θ-only, all orders): ❓ open

---

### ❌ `dead_end`

**Definition**: A specific approach or claim has been shown not to work.
The negative result is kept visible to prevent rediscovery of failed paths.

**Criteria**:
- An explicit obstruction or counterexample is documented.
- The file or section clearly explains *why* the approach fails.

**Examples**:
- Direct identification Re(∇†∇Θ) = G_μν: ❌ dead_end
  (rank mismatch: ∇†∇Θ is rank-0, G_μν is rank-2)
- ψ as projective phase Z ~ λZ: ❌ dead_end
  (projectivization removes the information ψ would carry)

---

## 2. Mandatory Rules for Status Assignment

These rules derive from the hard rules in `research_priorities.yaml`:

### R1: Fitted or motivated coefficients → NOT `proved`

If any coefficient, parameter, or structural constant in a derivation is:
- chosen to fit data,
- motivated by a pattern or aesthetic,
- borrowed from another theory without derivation,

then the overall claim **cannot** be labelled `proved`.  Use `semi_empirical`
or `indicated` instead.

### R2: Dimension/signature match → NOT `proved` for isomorphism

If the only evidence for an algebraic isomorphism is:
- matching dimension,
- matching signature of Killing form,
- matching semisimplicity,

then the status is **at most** `indicated`.  A full Cartan classification or an
explicit isomorphism is required for `proved`.

### R3: Injectivity or genericity assumptions → state explicitly

If a result holds "for generic Θ" or "assuming injectivity of the map Θ → g[Θ]",
these assumptions must be stated explicitly in the theorem/proposition.  The result
may still be called `proved` if the assumption is clearly labelled as a condition.

### R4: On-shell vs off-shell

Results proved for on-shell configurations (satisfying Euler–Lagrange equations)
must not be stated as if they hold off-shell.  On-shell and off-shell scope must
be clearly distinguished.

### R5: Hilbert variation with independent metric ≠ Θ-only derivation

Varying S_total[g, Θ] with respect to g^μν (with g independent) gives
Einstein equations with matter.  This is **not** the same as a Θ-only derivation
in which g = g[Θ] is substituted first.  The two are equivalent only on-shell
and only assuming injectivity (see `GR_closure/step2_theta_only_closure.tex`).

---

## 3. Files with Known Status Inconsistencies (as of 2026-03-11)

The following files have been identified as requiring status review.  See
`AUDITS/followup_gap_backlog_2026_03.md` for detailed gap descriptions.

| File | Known issue |
|------|-------------|
| `CURRENT_STATUS.md` | "FULLY DERIVED" for α with corrections; should be semi_empirical |
| `CURRENT_STATUS.md` | "FULLY DERIVED" for e-mass with corrections; fitted parameters present |
| `THEORY_COMPARISONS/penrose_twistor/reports/e08_summary.md` | "STRONG INDICATION" — correct, but could be confused with proved |
| `THEORY_COMPARISONS/penrose_twistor/su22_notes.md` | §5.1 — correct overall, but phrasing "emerges naturally" could be misread |
| `reports/gr_recovery_final_status.md` | Overall status table is accurate; internal text should be checked for overclaims |

---

## 4. Scan Patterns for Overclaims

When reviewing documents, flag and review any occurrence of:

- `"fully derived"` — check whether any fitted parameters are present
- `"proved exactly"` — check that a proof exists and is complete
- `"exact recovery"` — check that no genericity assumption is hidden
- `"equivalent to"` — check that an explicit isomorphism is stated
- `"we have shown"` — check that the argument actually appears, not just claimed

See also: `AUDITS/followup_gap_backlog_2026_03.md` for current known cases.
