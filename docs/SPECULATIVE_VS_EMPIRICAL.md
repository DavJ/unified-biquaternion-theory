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

# Speculative vs. Empirical Content in UBT: Clear Separation Guide

**Document Purpose:** Help readers distinguish between validated derivations and speculative hypotheses  
**Importance:** Critical for scientific integrity and proper evaluation  
**Last Updated:** January 13, 2026

**See Also:** 
- [UBT_LAYERED_STRUCTURE.md](UBT_LAYERED_STRUCTURE.md) - 3-layer organization (Core/Observables/Research Front)
- **[STATUS_OF_CODING_ASSUMPTIONS.md](docs/STATUS_OF_CODING_ASSUMPTIONS.md)** - Core vs modeling layers separation
- **[RS_OPTIMAL_LENS.md](information_probes/RS_OPTIMAL_LENS.md)** - RS(255,201) optimality and probe-dependent predictions

---

## Why This Matters

**Problem:** UBT contains both:
- Rigorous mathematical derivations with experimental validation
- Testable research hypotheses under investigation
- Speculative hypotheses requiring extensive future work

**Risk:** If not clearly separated, readers may:
- Dismiss valid work due to speculative claims
- Accept speculative claims as established science
- Confuse active research (Layer C) with wild speculation
- Misunderstand the theory's actual status

**Solution:** This document provides clear categorization and labeling system, integrated with UBT's 3-layer structure.

---

## Classification System

### 🟢 EMPIRICAL (Green): Validated by Experiment or Rigorous Proof

**Criteria:**
- Mathematical proof complete and verified
- Experimental measurement matches prediction
- Peer-reviewed or reproducible

**Examples:**
- GR recovery in real limit (proven)
- Standard Model gauge group derivation (rigorous)
- Predictions matching experiment (α, m_e with caveats)

**UBT Layer**: **Layer A (Core Ontology)**

### 🟡 SEMI-EMPIRICAL (Yellow): Partially Validated, Gaps Remain

**Criteria:**
- Framework rigorous but details incomplete
- Prediction matches but derivation has gaps
- Mostly derived with fitted components

**Examples:**
- Fine-structure constant (α⁻¹ = 137.036 matches, but ~12% renormalization gap)
- Electron mass (topology proven, coefficients fitted)
- Baryonic density (Ω_b ≈ 4.9% from information structure)

**UBT Layer**: **Layer B (Direct Observables)**

### 🔵 THEORETICAL (Blue): Framework Established, Predictions Pending

**Criteria:**
- Mathematical framework complete
- Testable predictions identified but not yet calculated/validated
- Falsification criteria clear

**Examples:**
- **Hubble tension as information overhead** (framework established, observational test pending)
- Dark matter from p-adic extensions (framework exists, no specific mass/cross-section yet)
- Modified gravity corrections (formalism exists, magnitude not calculated)

**UBT Layer**: **Layer C (Research Front)**

**Important Distinction**: Layer C content is **scientific research hypotheses**, NOT speculation.
These are testable, falsifiable proposals under active investigation. Success would promote
them to Layer B; falsification is equally valuable scientifically.

### 🟠 SPECULATIVE (Orange): Hypothesis Without Quantitative Predictions

**Criteria:**
- Qualitative idea or framework
- No numerical predictions
- Testability unclear or distant future

**Examples:**
- Consciousness/psychon hypothesis (no quantitative parameters)
- Closed timelike curves (framework only, no specific solutions analyzed)
- **Digital simulation analogies** (Reed-Solomon codes, 16-channel multiplex, etc.)

**UBT Status**: **Outside core layers** - in `speculative_extensions/`

**Critical Note**: 🟠 Speculative content is **qualitatively different** from 🔵 Layer C research.
Layer C has quantitative frameworks and testable predictions; speculative content does not.

### 🔴 PHILOSOPHICAL (Red): Interpretational, Not Scientific Claim

**Criteria:**
- Interpretation of formalism
- Not testable by experiment
- Philosophical preference

**Examples:**
- Multiverse interpretation of complex time
- Meaning of imaginary time component
- Ontological status of biquaternions

---

## Content Categorization by Document

### Main Repository Documents

#### README.md
**Mixed Content:**
- 🟢 GR recovery statement
- 🟡 α and m_e predictions
- 🟢 SM gauge group derivation
- 🟠 Consciousness claims (properly labeled)
- 🔵 Dark sector framework

**Labeling:** ✅ Good - uses warning symbols and status notes

#### OVERVIEW.md
**Balanced:**
- Clear separation of validated vs. speculative
- Honest assessment of limitations
- Explicit FAQs addressing speculation

**Labeling:** ✅ Excellent - explicit categorization

#### UBT_READING_GUIDE.md
**Purpose-Built:**
- Explicitly separates by category
- Guides readers to appropriate content
- Warns about speculative sections

**Labeling:** ✅ Excellent

### Technical Papers

#### unified_biquaternion_theory/ubt_main_article.tex
**Status:** Needs Updating
- 🟢 GR sections well-grounded
- 🟡 α derivation presented but gaps exist
- 🔴 Philosophical sections not clearly labeled

**Action Needed:**
- [ ] Add disclaimer at beginning
- [ ] Label speculative sections explicitly
- [ ] Separate appendices by category

#### consolidation_project/ubt_2_main.tex
**Status:** Better than original
- Has THEORY_STATUS_DISCLAIMER.tex
- Some labeling present

**Action Needed:**
- [ ] Ensure all appendices categorized
- [ ] Color-code or symbol-code sections
- [ ] Add summary table of content categories

#### Appendices
**Variable Quality:**
- Some have disclaimers (e.g., Appendix V on α)
- Others don't distinguish rigor level

**Action Needed:**
- [ ] Audit all appendices
- [ ] Add status banner to each
- [ ] Create appendix categorization table

### Speculative Content

**⚠️ UPDATE (November 2025): All speculative content moved to `speculative_extensions/` folder**

See [speculative_extensions/README.md](speculative_extensions/README.md) for complete organization and disclaimers.

#### speculative_extensions/complex_consciousness/ctc_2.0_main.tex
**Status:** Appropriately Labeled and Isolated
- Has disclaimer in document
- Separated into dedicated folder
- Not mixed with core physics
- Clear documentation of speculative nature

**Completed Actions:**
- ✅ Moved to separate `speculative_extensions/` folder
- ✅ Created comprehensive README with disclaimers
- ✅ Updated all documentation references
- ✅ References CONSCIOUSNESS_CLAIMS_ETHICS.md

#### CTC / Time Travel Content
**Status:** Separated and Labeled
- `speculative_extensions/appendices/appendix_J_rotating_spacetime_ctc.tex`
- Clearly marked as speculative in file header
- Treated as mathematical exercise, not physical reality claim

**Completed Actions:**
- ✅ Moved to `speculative_extensions/` folder
- ✅ Clarified mathematical vs. physical interpretation
- [ ] Stability analysis (if stable, less speculative)
- [ ] Causality resolution (essential for any claim)

---

## Recommended Labeling System

### In LaTeX Documents

**Add Status Banner:**
```latex
\begin{tcolorbox}[colback=green!5!white,colframe=green!75!black,title=EMPIRICAL CONTENT]
This section contains validated derivations with experimental confirmation or rigorous proof.
\end{tcolorbox}
```

**Or:**
```latex
\begin{tcolorbox}[colback=orange!5!white,colframe=orange!75!black,title=SPECULATIVE HYPOTHESIS]
\textbf{Warning:} This section contains speculative ideas without quantitative predictions. 
Treat as philosophical exploration, not established science.
\end{tcolorbox}
```

**Categories:**
- 🟢 Green box: EMPIRICAL CONTENT
- 🟡 Yellow box: SEMI-EMPIRICAL (Gaps Acknowledged)
- 🔵 Blue box: THEORETICAL FRAMEWORK
- 🟠 Orange box: SPECULATIVE HYPOTHESIS
- 🔴 Red box: PHILOSOPHICAL INTERPRETATION

### In Markdown Documents

**Use Callout Boxes:**

> **🟢 EMPIRICAL:** This content is validated by experiment or rigorous proof.

> **🟡 SEMI-EMPIRICAL:** Framework solid, but some gaps or fitted parameters remain.

> **🔵 THEORETICAL:** Mathematical framework established, predictions pending calculation.

> **🟠 SPECULATIVE:** Qualitative hypothesis without quantitative predictions. Highly uncertain.

> **🔴 PHILOSOPHICAL:** Interpretation only, not a scientific claim.

### In Presentations

**Color-Code Slides:**
- Green border: validated content
- Yellow border: mostly validated
- Blue border: theoretical framework
- Orange border: speculation
- Red border: interpretation

**Always include legend** explaining color system

---

## Document-by-Document Categorization

### Core Physics (Mostly Empirical/Semi-Empirical)

| Document | Primary Category | UBT Layer | Notes |
|----------|------------------|-----------|-------|
| **Appendix R (GR equivalence)** | 🟢 EMPIRICAL | Layer A | Rigorous proof, experimentally validated |
| **Appendix E (SM gauge group)** | 🟢 EMPIRICAL | Layer A | Rigorous derivation, matches known SM |
| **Appendix A (Θ-field action)** | 🟢 EMPIRICAL | Layer A | Mathematical foundation solid |
| **emergent_alpha_from_ubt.tex** | 🟡 SEMI-EMPIRICAL | Layer B | Matches experiment, derivation gaps remain |
| **Hopfion fermion mass** | 🟡 SEMI-EMPIRICAL | Layer B | Topology solid, coefficients fitted |
| **Baryonic density (Ω_b)** | 🟡 SEMI-EMPIRICAL | Layer B | Information-theoretic derivation, validated |
| **Appendix Y (Yukawa)** | 🔵 THEORETICAL | Layer C | Framework complete, values not calculated |

### Extensions (Theoretical/Speculative)

| Document | Primary Category | UBT Layer | Notes |
|----------|------------------|-----------|-------|
| **Hubble tension overhead** | 🔵 THEORETICAL | Layer C | Framework exists, testable, observational validation pending |
| **p-adic dark matter** | 🔵 THEORETICAL | Layer C | Framework exists, no predictions yet |
| **Modified gravity** | 🔵 THEORETICAL | Layer C | Formalism established, magnitude TBD |
| **CMB signatures** | 🔵 THEORETICAL | Layer C | Protocol ready, analysis not complete |
| **Psychons/consciousness** | 🟠 SPECULATIVE | Outside core | No quantitative parameters |
| **CTCs** | 🟠 SPECULATIVE | Outside core | Mathematical solutions, physical status unclear |
| **Digital simulation (IT appendix)** | 🔴 PHILOSOPHICAL | Outside core | Reed-Solomon analogy, not physical claim |
| **Time travel** | 🟠 SPECULATIVE | Outside core | Conceptual only |
| **Multiverse interpretation** | 🔴 PHILOSOPHICAL | Outside core | Interpretation of formalism |

### Assessment Documents (Meta)

| Document | Purpose |
|----------|---------|
| **UBT_SCIENTIFIC_RATING_2025.md** | Honest assessment of status |
| **TESTABILITY_AND_FALSIFICATION.md** | Falsification criteria |
| **FITTED_PARAMETERS.md** | Parameter transparency |
| **CONSCIOUSNESS_CLAIMS_ETHICS.md** | Ethics for speculative claims |
| **UBT_READING_GUIDE.md** | Navigation by rigor level |

---

## Guidelines for Creating New Content

### Before Adding Content, Ask:

1. **What is the rigor level?**
   - Proven mathematically?
   - Experimentally validated?
   - Framework only?
   - Pure speculation?

2. **What is the testability?**
   - Already tested?
   - Testable with current technology?
   - Testable in principle but not practice?
   - Unfalsifiable?

3. **What are the assumptions?**
   - First principles?
   - Building on validated work?
   - Requires new assumptions?
   - Circular reasoning?

4. **What is the uncertainty?**
   - Error bars quantified?
   - Alternative explanations?
   - Sensitivity to assumptions?
   - Null hypothesis?

### Decision Tree

```
New Content → Is it proven/validated? 
   ├─ Yes → 🟢 EMPIRICAL (provide proof/reference)
   └─ No → Does rigorous framework exist?
      ├─ Yes → Predictions quantitative?
      │   ├─ Yes (calculated) → 🔵 THEORETICAL
      │   ├─ Yes (gaps remain) → 🟡 SEMI-EMPIRICAL  
      │   └─ No → 🟠 SPECULATIVE
      └─ No → Is it testable in principle?
         ├─ Yes → 🟠 SPECULATIVE (develop framework)
         └─ No → 🔴 PHILOSOPHICAL (label clearly)
```

### Required Elements for Each Category

**🟢 EMPIRICAL:**
- Reference to proof or experimental paper
- Reproducible code if computational
- Independent verification status

**🟡 SEMI-EMPIRICAL:**
- Explicit statement of what's validated
- Clear description of gaps
- Roadmap to full derivation

**🔵 THEORETICAL:**
- Complete mathematical framework
- Outline of prediction calculation
- Timeline for completing calculation

**🟠 SPECULATIVE:**
- "SPECULATIVE HYPOTHESIS" label
- Explanation of what's missing for testability
- Honest probability estimate if possible

**🔴 PHILOSOPHICAL:**
- "INTERPRETATION ONLY" label
- Alternative interpretations mentioned
- Not claimed as physics prediction

---

## Examples of Good vs. Bad Practice

### Example 1: Fine-Structure Constant

**❌ BAD (Overstatement):**
> "UBT derives α⁻¹ = 137 from first principles with no free parameters."

**Problems:**
- "First principles" ignores perturbative gap
- "No free parameters" is not fully true (R~12% correction)

**✅ GOOD (Honest):**
> "🟡 SEMI-EMPIRICAL: UBT predicts α⁻¹ = 137 from complex time topology. The prediction matches experiment to 0.026%. However, ~12% of the B constant derives from perturbative QED corrections not yet calculated from UBT first principles. See FITTED_PARAMETERS.md for details."

### Example 2: Electron Mass

**❌ BAD:**
> "UBT calculates electron mass as 0.510 MeV, proving the hopfion mechanism."

**Problems:**
- "Proves" is too strong (formula coefficients fitted)
- Doesn't mention muon/tau predictions needed

**✅ GOOD:**
> "🟡 SEMI-EMPIRICAL: UBT predicts m_e = 0.510 MeV from hopfion topology (0.22% error). The topological structure is rigorously derived, but formula coefficients (A, p, B) are currently fitted to lepton masses. Deriving these from first principles is in progress (ROADMAP.md §2.2). This represents a promising but not yet complete derivation."

### Example 3: Consciousness

**❌ BAD:**
> "UBT explains consciousness through psychons."

**Problems:**
- "Explains" is false (no quantitative model)
- Implies scientific achievement

**✅ GOOD:**
> "🟠 SPECULATIVE HYPOTHESIS: UBT proposes that consciousness might arise from quantum excitations ('psychons') in complex-time phase space. This is a highly speculative philosophical hypothesis with NO quantitative predictions, testable parameters, or neuroscientific grounding. It is properly isolated in appendices and should not be confused with UBT's empirical physics predictions. See CONSCIOUSNESS_CLAIMS_ETHICS.md."

### Example 4: Dark Matter

**❌ BAD:**
> "UBT predicts dark matter properties."

**Problems:**
- "Predicts" implies calculated values
- Actually only framework exists

**✅ GOOD:**
> "🔵 THEORETICAL FRAMEWORK: UBT provides a p-adic extension framework for dark sector physics. Specific predictions (dark matter mass, cross-section) are not yet calculated. These calculations are planned for 2027 (ROADMAP.md §4.2). Current status: mathematical framework established, physical predictions pending."

---

## How to Use This Guide

### For Authors (Adding Content)
1. Categorize new content using decision tree
2. Add appropriate color-coded label
3. Write honest description with caveats
4. Link to supporting evidence or acknowledge gaps
5. Update this document if new category needed

### For Readers (Evaluating Claims)
1. Look for category labels (color boxes)
2. Read 🟢 EMPIRICAL content as validated
3. Read 🟡🔵 with appropriate skepticism
4. Treat 🟠 as interesting ideas, not science
5. Recognize 🔴 as interpretation, not fact

### For Reviewers (Peer Review)
1. Verify categorization is accurate
2. Check if caveats are sufficient
3. Ensure no speculation presented as fact
4. Confirm experimental claims match reality
5. Recommend re-categorization if needed

### For Maintainers (Repository)
1. Audit documents quarterly
2. Update categorizations as work progresses
3. Upgrade 🔵→🟡→🟢 as derivations complete
4. Downgrade 🟡→🟠 if gaps discovered
5. Remove or clarify misleading content

---

## Integration with Existing Documents

### Update README.md
- [ ] Add legend explaining color system
- [ ] Label each major claim with appropriate color
- [ ] Link to this document for details

### Update All LaTeX Documents
- [ ] Add status banner to each section/appendix
- [ ] Create categorization table of contents
- [ ] Include legend in each document

### Update Presentation Materials
- [ ] Color-code slides
- [ ] Include legend on each slide set
- [ ] Never present speculative content without label

### Update CONTRIBUTING.md
- [ ] Require categorization for all new content
- [ ] Provide templates for each category
- [ ] Review process checks categorization

---

## Success Criteria

**This system succeeds if:**

1. **Clarity:** Readers immediately know rigor level of any content
2. **Honesty:** No overstatement or understatement of status
3. **Protection:** Speculative content doesn't damage empirical credibility
4. **Guidance:** Researchers know where to focus efforts
5. **Evolution:** Categories update as work progresses

**Failure modes to avoid:**

- ❌ Everything labeled "speculative" (dismisses valid work)
- ❌ Nothing labeled "speculative" (misleads readers)
- ❌ Labels inconsistent across documents
- ❌ Labels not updated as status changes
- ❌ System too complex to use

---

## Quarterly Review Checklist

**Every 3 months, review:**

- [ ] Are categorizations still accurate?
- [ ] Have any 🔵 progressed to 🟡 or 🟢?
- [ ] Have any 🟡 been completed to 🟢?
- [ ] Have any gaps been discovered (downgrade)?
- [ ] Are all new documents properly labeled?
- [ ] Is this document itself up to date?

**Document changes in CHANGELOG.md**

---

## Conclusion

### Purpose Achieved If:

Physicists can evaluate UBT fairly:
- Appreciate validated aspects (GR recovery, SM gauge group)
- Understand semi-empirical predictions (α, m_e) with appropriate caveats
- Recognize theoretical frameworks (dark matter) as incomplete
- Dismiss or bracket speculative claims (consciousness)

### Ultimate Goal:

**UBT judged on its empirical content**, not dragged down by speculation or propped up by overstatement.

**Honest categorization = scientific integrity = long-term credibility**

---

**Document Status:** Living guide, updated with theory development  
**Review Schedule:** Quarterly  
**Next Review:** Q1 2026  
**Responsibility:** All contributors (enforced by maintainers)  
**Compliance:** Required for all new content  
**Last Updated:** November 5, 2025

---

## Quick Reference Table

| Symbol | Category | Criteria | Examples | Trust Level |
|--------|----------|----------|----------|-------------|
| 🟢 | EMPIRICAL | Proven/validated | GR recovery, SM gauge group | High |
| 🟡 | SEMI-EMPIRICAL | Mostly validated, gaps remain | α, m_e predictions | Medium-High |
| 🔵 | THEORETICAL | Framework complete, values pending | Dark matter, Yukawa | Medium |
| 🟠 | SPECULATIVE | No predictions yet | Consciousness, CTCs | Low |
| 🔴 | PHILOSOPHICAL | Interpretation only | Multiverse, ontology | Not applicable |

**Use this table in presentations and summaries.**
