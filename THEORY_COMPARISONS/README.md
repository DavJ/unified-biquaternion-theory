# THEORY_COMPARISONS

## Overview

This directory contains **isolated sandbox environments** for comparing the Unified Biquaternion Theory (UBT) with other theoretical frameworks in modern physics.

**Purpose**: To explore structural similarities, mathematical mappings, and conceptual bridges between UBT and established or alternative theories.

**Scope**: These comparisons are **experimental research layers** and do NOT modify core UBT modules.

---

## Design Philosophy

### Structural Closeness

When we say two theories show "structural closeness," we mean:

1. **Mathematical Isomorphisms**: Existence of structure-preserving maps between their formalism (e.g., biquaternions ↔ twistors)

2. **Shared Symmetries**: Common underlying symmetry groups or invariance principles (e.g., conformal invariance, gauge symmetries)

3. **Equivalent Limits**: Agreement in specific physical regimes or limiting cases (e.g., flat spacetime, weak field limits)

4. **Predictive Overlap**: Ability to reproduce similar or identical observable predictions for measurable quantities

5. **Conceptual Bridges**: Logical connections between fundamental objects (e.g., complex time in UBT vs spinor geometry in twistor theory)

**Important**: Structural closeness does NOT imply theoretical equivalence. It identifies where theories share mathematical machinery or interpretive frameworks.

---

## Current Comparisons

### 1. Penrose Twistor Theory

**Directory**: `penrose_twistor/`

**Focus**: Mapping between:
- UBT's biquaternion formalism and complex time τ = t + iψ
- Penrose's twistor geometry and null structures in complexified Minkowski space

**Key Questions**:
- Can UBT's 2×2 matrix representations embed into twistor space?
- Do incidence relations preserve physical information?
- Is there a natural SU(2,2) symmetry connection?

See `penrose_twistor/README.md` for details.

---

## Future Comparisons (Planned)

Potential future sandboxes:

- **Loop Quantum Gravity**: Spin networks vs biquaternion lattices
- **String Theory**: Worldsheet formalism vs complex-time dynamics
- **Geometric Algebra**: Clifford algebra vs biquaternion algebra
- **Non-commutative Geometry**: Spectral triples vs UBT metric structure

---

## Usage Guidelines

### For Researchers

1. Each comparison lives in its own subdirectory
2. Comparisons must be **self-contained** with their own documentation
3. Use only lightweight dependencies (preferably sympy for symbolic work)
4. Include tests to validate mathematical claims
5. Provide runnable experiments demonstrating key results

### For Contributors

- Do NOT modify core UBT files from comparison code
- Keep comparisons **independent** of each other
- Document assumptions and limitations clearly
- Use standard scientific attribution in references
- Follow existing code style and testing patterns

---

## Structure Template

Each comparison subdirectory should contain:

```
theory_name/
├── README.md           # Theory-specific overview
├── references.md       # Academic citations and resources
├── common/             # Shared utilities
├── [theory]_core/      # Core implementation
├── experiments/        # Runnable demonstrations
└── tests/              # Automated validation
```

---

## Testing and Validation

All comparison code must:
- Pass `pytest` without errors
- Include at least one non-trivial numeric validation
- Document expected vs actual results
- Provide clear failure messages

Run tests with:
```bash
pytest THEORY_COMPARISONS/[theory_name]/tests/
```

---

## License and Attribution

All comparison code follows the repository's main license (see `LICENSE.md`).

Original theory attribution:
- **UBT**: Ing. David Jaroš
- **External theories**: See individual `references.md` files

---

## Contact and Contributions

For questions about theory comparisons:
- Open an issue on the repository
- Tag with `theory-comparison` label
- Reference the specific comparison subdirectory

Contributions welcome! Please follow the guidelines above and ensure all tests pass.
