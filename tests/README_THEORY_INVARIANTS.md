# UBT Theory Invariant Tests

## Purpose

These tests enforce **theory-level invariants** to ensure the Unified Biquaternion Theory (UBT) never silently reverts to treating classical General Relativity as the fundamental theory.

**CRITICAL**: These are NOT optional documentation checks. They are core theory constraints that protect the integrity of the biquaternionic formalism.

## What These Tests Enforce

### 1. Metric Projection Requirement
- The classical metric `g_{μν}` must ALWAYS be defined as the real projection of the biquaternionic metric: `g_{μν} := Re(𝓖_{μν})`
- `𝓖_{μν}` is fundamental, `g_{μν}` is derived
- Tests verify this projection definition exists somewhere in the codebase

### 2. Lock-in Files Must Exist
Required files that define the fundamental theory structure:
- `UBT_Main.tex` - Core theory definition
- `THEORY_STATUS_DISCLAIMER.tex` - Biquaternionic geometry lock-in statement

These files must contain explicit statements about the biquaternionic nature of the theory.

### 3. No Forbidden GR Language
The tests detect and reject language that treats classical GR as fundamental:

**Forbidden patterns (without proper context):**
- "Let g_{μν} be the spacetime metric"
- "standard Einstein equations" (use "recovers Einstein equations" instead)
- References to Christoffel symbols or Levi-Civita connection without clarifying they are projections

**Allowed contexts:**
- "in the real limit"
- "after projection"
- "Re(𝓖_{μν})"
- "recovers/reproduces Einstein equations"
- "reduces to classical GR"
- "are derived from"

### 4. Biquaternionic Primacy
The tests verify that biquaternionic objects remain primary:
- `𝓖_{μν}` (biquaternionic metric) - fundamental
- `Ω_μ` (biquaternionic connection) - fundamental
- `𝓡_{μν}` (biquaternionic curvature) - fundamental
- `𝓣_{μν}` (biquaternionic stress-energy) - fundamental

While their real projections `g`, `Γ`, `R`, `T` are properly contextualized as derived quantities.

## Running the Tests

### Locally
```bash
# Run all UBT theory invariant tests
pytest tests/test_ubt_tex_invariants.py -v

# Run specific test
pytest tests/test_ubt_tex_invariants.py::TestUBTTheoryInvariants::test_no_forbidden_gr_language -v
```

### In CI
The tests run automatically on every push and pull request via the GitHub Actions workflow:
`.github/workflows/ubt-ci.yml`

## Test Files

- `tests/rules.py` - Defines forbidden patterns, required projections, and allowed contexts
- `tests/test_ubt_tex_invariants.py` - Test suite with 8 tests

## When Tests Fail

If these tests fail, it indicates:

1. **Missing projection definition**: Add explicit definition of `g_{μν} := Re(𝓖_{μν})`
2. **Forbidden language detected**: Review the violation and add proper projection context
3. **Missing lock-in file**: Do not remove `UBT_Main.tex` or `THEORY_STATUS_DISCLAIMER.tex`
4. **Missing biquaternionic objects**: Define fundamental biquaternionic quantities

## Design Philosophy

These tests implement a "theory firewall" that prevents accidental regression to classical GR as the fundamental framework. They ensure that:

- Future contributors (including AI assistants) must respect the biquaternionic formalism
- Documentation and derivations maintain theoretical consistency
- The relationship between UBT and GR (generalization, not replacement) is preserved
- Classical GR appears only as `Re(...)` / Hermitian projection

## Future Extensions

When adding new content to UBT:

1. Define new structures at the biquaternionic level first
2. Explicitly state how classical GR objects are obtained via `Re(·)`
3. Avoid introducing classical GR objects as axioms without projection
4. Run tests to verify compliance: `pytest tests/test_ubt_tex_invariants.py`

## False Positives

The tests use context-aware pattern matching and may occasionally flag valid content. If you believe a test violation is incorrect:

1. Check that proper projection context appears within ~200 characters of the match
2. Add appropriate context phrases from the allowed list
3. If the pattern genuinely needs updating, modify `tests/rules.py` carefully

## License

These tests are part of the UBT repository and follow the same licensing as the repository itself. See `LICENSE.md` for details.

---

**Remember**: `𝓖_{μν}` is fundamental, `g_{μν}` is derived!
