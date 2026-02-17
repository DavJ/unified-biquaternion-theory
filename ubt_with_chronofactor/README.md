# Legacy UBT with Chronofactor

This directory contains the **legacy formulation** of Unified Biquaternion Theory (UBT) that includes the external/global chronofactor parameter (τ = t + iψ) as a foundational element.

## Purpose

This subtree preserves the original chronofactor-based implementation of UBT for:
- **Historical reference**: Complete record of the prior formulation
- **Regression testing**: Comparison against new core formulation
- **Existing workflows**: Maintaining reproducibility of published results

## What's Here

All content that depends on or assumes the chronofactor formulation has been moved to this directory:

### Directories
- **`forensic_fingerprint/`** - CMB fingerprint validation pipelines
- **`FORENSICS/`** - Forensic analysis tools and protocols
- **`TOOLS/`** - Data provenance, simulations, and analysis tools
- **`EXPERIMENTS/`** - Channel selection and experimental protocols
- **`scripts/`** - Python scripts for calculations and verification
- **`papers/`** - Papers written with chronofactor assumptions
- **`tools/`** - Additional tooling and utilities
- **`complex_consciousness/`** - Consciousness modeling (chronofactor-dependent)
- **`alpha_core_repro/`**, **`alpha_two_loop/`** - Alpha calculations
- **`ubt_masses/`**, **`ubt_strict_fix/`**, **`ubt_strict_minimal/`** - Mass derivations

## Running Legacy Tools

### Path Updates

Since files have moved, you'll need to update relative paths when running legacy scripts:

```bash
# From repository root:
cd legacy/ubt_with_chronofactor

# Run forensic fingerprint validation:
python -m forensic_fingerprint.run_audit_suite

# Run alpha calculations:
python scripts/emergent_alpha_calculator.py
```

### Python Path Setup

If importing modules, add the legacy directory to your Python path:

```python
import sys
sys.path.insert(0, '/path/to/repo/legacy/ubt_with_chronofactor')

# Now you can import legacy modules
from forensic_fingerprint import constants
```

### Environment Variables

Some scripts may reference hardcoded paths. Set up environment variables if needed:

```bash
export UBT_LEGACY_ROOT=/path/to/repo/legacy/ubt_with_chronofactor
export PYTHONPATH=$UBT_LEGACY_ROOT:$PYTHONPATH
```

## Key Differences from Core

The **core UBT** (in `ubt_core/`) differs from this legacy formulation in one fundamental aspect:

### Legacy (This Directory)
- **External chronofactor**: Complex time τ = t + iψ is a global parameter
- **Formulation**: Chronofactor appears as an input to the biquaternionic field Θ(q, τ)
- **Phase dynamics**: Imaginary time ψ is treated as an additional degree of freedom

### Core (New Formulation)
- **No external chronofactor**: τ is not a separate parameter
- **8D phase-capable field**: All phase information encoded within Θ(q) itself
- **Intrinsic phase**: Phase dynamics emerge from the internal structure of Θ

## Compatibility Notes

### What Remained Identical
- Mathematical definitions of biquaternions (8D complex quaternions)
- Core field equations structure
- Physical predictions (where comparable)

### What Changed
- **Directory structure**: Content moved to `legacy/ubt_with_chronofactor/`
- **Import paths**: Python modules now under legacy subtree
- **Conceptual framing**: Removal of external chronofactor as primitive

## Branch Reference

This content is preserved exactly as it was on the **`legacy/with-chronofactor`** branch.

To see the frozen state before restructuring:
```bash
git checkout legacy/with-chronofactor
```

## Link to Core

For the new chronofactor-free formulation, see:
- **Core definitions**: `/ubt_core/README.md`
- **Derivations**: `/derivations/README.md`
- **New papers**: `/papers/README.md`

## Questions?

If you encounter issues running legacy tools from new paths, please:
1. Check that relative paths in scripts are updated
2. Verify PYTHONPATH includes legacy directory
3. Consult root README.md for routing guidance

---

**Status**: ✅ Fully functional, preserved for reference and regression testing  
**Maintenance**: Read-only; new development happens in core  
**Git History**: Preserved via `git mv` operations
