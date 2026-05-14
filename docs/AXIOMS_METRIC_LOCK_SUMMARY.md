# Axioms and Metric Lock Implementation Summary

**Date**: February 10, 2026  
**Branch**: `chore/axioms-metric-lock`  
**Status**: ✅ Complete

---

## Overview

This implementation adds **canonical axiom documentation** and **automated enforcement** to protect UBT's fundamental definitions from accidental redefinition during development, refactoring, or AI-assisted coding.

**Key Principle**: Documentation + automated guards, **NO physics/code changes**.

---

## Files Added

### 1. core/AXIOMS.md (9,341 bytes)

**Purpose**: Lock down the four canonical axioms of UBT

**Content**:

#### AXIOM A: Fundamental Field Object
```
Θ(q, τ) is the fundamental biquaternionic field
Θ: M × C → B ≡ C ⊗ H
```
- **Lock Rule**: Θ is the unique fundamental object. No alternative fundamental fields.

#### AXIOM B: Complex Time (Final Formulation)
```
τ = t + iψ ∈ C
```
- **Lock Rule**: Time is complex-valued, NOT quaternionic in final formulation
- **Historical Note**: Earlier drafts explored quaternionic time as heuristic; final uses complex time only

#### AXIOM C: Unique Emergent Metric (LOCKED)
```
g_μν(x) := Re[(D_μ Θ(x,τ))† D_ν Θ(x,τ)]
```
- **CRITICAL LOCK RULES**:
  1. NO background metric
  2. NO alternative metrics (effective_metric, metric_v2, etc.)
  3. NO metric redefinition
  4. Emergent only - not a fundamental field

#### AXIOM D: General Relativity as Classical Limit
```
G_μν = R_μν - ½g_μν R = κ T^(Θ)_μν
```
- **Lock Rule**: GR is a derived limit/projection of UBT, not an independent framework

**AI/Copilot Guardrails**:
- ✓ Permitted: Verify, compute, derive, formalize
- ✗ Forbidden: Redefine τ/ψ/Θ, introduce alternative metrics, treat GR as independent

**Cross-References**: Links to all formal verification appendices and field definitions

---

### 2. tests/test_metric_lock.py (9,098 bytes)

**Purpose**: Automated enforcement of canonical axioms

**Test Suite**:

#### Test 1: Axioms File Exists
```python
def test_axioms_file_exists():
    # Asserts core/AXIOMS.md exists
```

#### Test 2: Axioms Content Complete
```python
def test_axioms_content_complete():
    # Verifies AXIOMS.md contains:
    # - τ = t + iψ
    # - g_μν metric formula
    # - Re[·] operator
    # - D_μΘ covariant derivative
    # - Lock rules
```

#### Test 3: No Forbidden Metric Patterns
```python
def test_no_forbidden_metric_patterns():
    # Scans *.py, *.md, *.tex for forbidden patterns:
    # - effective_metric (as variable)
    # - background_metric
    # - metric_v2
    # - g0_mu_nu (as background metric)
    # - metric_hat
    # - \newcommand\geffective
    # etc.
```

**Smart Exclusions**:
- Skips AXIOMS.md itself (documents forbidden patterns)
- Skips test_metric_lock.py itself (defines patterns to search)
- Allows `\label{eq:effective_metric}` (equation labels, not definitions)
- Skips comments and excluded directories

**Dual-Mode Operation**:
- **Standalone**: `python3 tests/test_metric_lock.py`
- **Pytest**: `pytest tests/test_metric_lock.py -v`

---

## Verification Results

### Standalone Execution

```bash
$ python3 tests/test_metric_lock.py

======================================================================
UBT Metric Lock Test - Standalone Mode
======================================================================

Test 1: Checking core/AXIOMS.md exists...
  ✓ PASS: AXIOMS.md found

Test 2: Checking AXIOMS.md content...
  ✓ PASS: All required canonical elements present

Test 3: Scanning repository for forbidden metric patterns...
  ✓ PASS: No forbidden patterns detected

======================================================================
✓ ALL TESTS PASSED - Metric lock is secure
======================================================================
```

**Success Rate**: 3/3 tests passed (100%)

---

## CI/CD Integration

### Automatic Integration

The test is **automatically picked up** by existing CI workflows:

**File**: `.github/workflows/verify.yml`
```yaml
- name: Run pytest
  run: |
    python -m pip install pytest
    pytest -q
```

**File**: `.github/workflows/ubt-ci.yml`
```yaml
- name: Install pytest
  run: |
    pip install pytest
    pytest tests/test_ubt_tex_invariants.py -v
```

**Note**: The new test will run alongside existing tests whenever CI executes pytest.

**No new CI setup required** - leverages existing infrastructure.

---

## Usage Instructions

### For Developers

**Before making changes that might affect axioms:**
```bash
# Quick check
python3 tests/test_metric_lock.py

# Run all tests
pytest tests/
```

**If test fails:**
1. Review the violation report showing file:line of forbidden pattern
2. Verify if it's a legitimate violation or false positive
3. If legitimate: Remove the alternative metric/redefinition
4. If false positive: Update test to exclude (e.g., it's just a comment)

### For AI Assistants (Copilot, etc.)

**Before suggesting changes:**
1. Check if change involves τ, ψ, Θ, or g_μν
2. If yes, verify against `core/AXIOMS.md`
3. Do NOT suggest alternative metric definitions
4. Do NOT redefine fundamental fields
5. If unsure, run: `python3 tests/test_metric_lock.py`

---

## What Was NOT Changed

Per strict requirements, **NO** physics or code changes:

- ❌ NO changes to existing Θ field definitions
- ❌ NO changes to covariant derivatives
- ❌ NO changes to metric formulas
- ❌ NO changes to equations or mathematics
- ❌ NO changes to computational code

Only **NEW** files added:
- ✅ Documentation: `core/AXIOMS.md`
- ✅ Test: `tests/test_metric_lock.py`

---

## Cross-References

This implementation complements and protects:

### Formal Verification Framework
- `consolidation_project/appendix_FORMAL_qm_gr_unification.tex`
- `consolidation_project/appendix_FORMAL_emergent_metric.tex`
- `consolidation_project/appendix_FORMAL_black_hole_radiation.tex`
- `consolidation_project/appendix_FORMAL_constants_normalization.tex`

### Core Documentation
- `consolidation_project/FORMAL_VERIFICATION_FRAMEWORK.md`
- `THETA_FIELD_DEFINITION.md`
- `UBT_CORE_VERIFICATION_REPORT.md`

### Main Documents
- `consolidation_project/ubt_core_main.tex`
- `consolidation_project/appendix_R_GR_equivalence.tex`

---

## Rationale

### Why Lock the Axioms?

**Problem**: During development, refactoring, or AI-assisted coding, it's easy to accidentally:
- Introduce alternative metric definitions
- Redefine fundamental fields
- Treat GR as independent from UBT
- Change τ or ψ semantics

**Solution**: Explicit documentation + automated enforcement prevents accidental violations.

### Why These Specific Patterns?

The forbidden patterns represent common mistakes:

1. **effective_metric**: Often introduced when deriving GR limit (use "emergent metric" instead)
2. **background_metric**: Violates the principle that metric is emergent, not fundamental
3. **metric_v2**: Suggests multiple metric definitions exist
4. **g0_mu_nu**: Often used for "background" or "flat" metric
5. **metric_hat**: Suggests alternative metric formulation

### Why Not Just Grep?

The test is more sophisticated than simple grep:
- Context-aware (ignores comments, labels, documentation of forbidden patterns)
- Structured (provides clear violation reports with file:line)
- Maintainable (easy to add/remove patterns)
- Integrated (runs automatically in CI)

---

## Future Enhancements (If Needed)

### Potential Extensions

1. **Additional patterns**: Monitor for other potential violations
2. **Whitelist mechanism**: Allow specific exceptions with comments
3. **Severity levels**: Distinguish errors vs warnings
4. **Auto-fix suggestions**: Suggest correct alternatives when violations found

### Not Needed Currently

The current implementation is intentionally minimal and focused:
- Protects the most critical axioms
- Easy to understand and maintain
- Low false-positive rate
- Runs fast

---

## Commands Reference

### Run Tests Locally

```bash
# Standalone mode (no pytest needed)
python3 tests/test_metric_lock.py

# With pytest (if installed)
pytest tests/test_metric_lock.py -v

# Run specific test
pytest tests/test_metric_lock.py::test_axioms_file_exists -v

# Run with output
pytest tests/test_metric_lock.py -v -s
```

### Check Files

```bash
# View axioms
cat core/AXIOMS.md

# View test
cat tests/test_metric_lock.py

# Check git status
git status
git diff core/AXIOMS.md
```

---

## Conclusion

✅ **Implementation Complete**

The canonical axioms are now:
1. **Documented**: Clear, comprehensive, cross-referenced in `core/AXIOMS.md`
2. **Locked**: Protected against accidental modification
3. **Enforced**: Automated testing prevents violations
4. **Integrated**: Runs automatically in CI/CD

**Zero physics changes** - only protective documentation and guards added.

The UBT fundamental definitions are now safeguarded against accidental redefinition while still allowing legitimate derivations, computations, and extensions.

---

**Author**: UBT Team  
**Based on requirements from**: David Jaroš  
**Repository**: unified-biquaternion-theory  
**Branch**: chore/axioms-metric-lock  
**Date**: February 10, 2026
