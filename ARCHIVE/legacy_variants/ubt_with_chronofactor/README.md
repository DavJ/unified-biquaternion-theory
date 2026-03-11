# UBT with Chronofactor

This directory contains the **chronofactor-based formulation** of Unified Biquaternion Theory (UBT) that includes the external/global chronofactor parameter (τ = t + iψ) as a foundational element.

## Purpose

This is a **first-class formulation** of UBT maintained for:
- **Systematic comparison**: A/B testing against the chronofactor-free formulation
- **Complete implementation**: Full set of papers, tools, experiments, and validation
- **Open research question**: Exploring the physical meaning of complex time

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

## Running Tools

### Path Updates

From the repository root:

```bash
# Run forensic fingerprint validation:
cd ubt_with_chronofactor
python -m forensic_fingerprint.run_audit_suite

# Run alpha calculations:
python scripts/emergent_alpha_calculator.py
```

### Python Path Setup

If importing modules from outside this directory, add ubt_with_chronofactor to your Python path:

```python
import sys
from pathlib import Path
repo_root = Path(__file__).resolve().parents[2]  # Adjust as needed
sys.path.insert(0, str(repo_root / 'ubt_with_chronofactor'))

# Now you can import modules
from forensic_fingerprint import constants
from ubt_masses import core
```

### Environment Variables

If needed, set up environment variables:

```bash
export UBT_CHRONOFACTOR_ROOT=/path/to/repo/ubt_with_chronofactor
export PYTHONPATH=$UBT_CHRONOFACTOR_ROOT:$PYTHONPATH
```

## Key Differences from Chronofactor-Free Formulation

The **chronofactor-free UBT** (in `ubt_no_chronofactor/`) differs from this formulation in one fundamental aspect:

### With Chronofactor (This Directory)
- **External chronofactor**: Complex time τ = t + iψ is a global parameter
- **Formulation**: Chronofactor appears as an input to the biquaternionic field Θ(q, τ)
- **Phase dynamics**: Imaginary time ψ is treated as an additional degree of freedom
- **Status**: Mature implementation with extensive validation

### Without Chronofactor
- **No external chronofactor**: τ is not a separate parameter
- **8D phase-capable field**: All phase information encoded within Θ(q) itself
- **Intrinsic phase**: Phase dynamics emerge from the internal structure of Θ
- **Status**: Core scaffolding complete, derivations in progress

## Compatibility Notes

### What Remained Identical
- Mathematical definitions of biquaternions (8D complex quaternions)
- Core field equations structure
- Physical predictions (where comparable)

### What Changed in Repository Structure
- **Directory location**: Content organized under `ubt_with_chronofactor/`
- **Import paths**: Python modules accessible via ubt_with_chronofactor prefix
- **Parallel formulations**: Both chronofactor and chronofactor-free maintained as first-class

Root-level shims are provided for backward compatibility:
- `validate_manifest.py`, `hash_dataset.py`, `repo_utils.py` → redirect to this directory
- `forensic_fingerprint/` → redirects to `ubt_with_chronofactor/forensic_fingerprint/`

## Link to Chronofactor-Free Formulation

For the chronofactor-free formulation, see:
- **Core definitions**: `/ubt_no_chronofactor/core/README.md`
- **Comparison**: `/ubt_compare/README.md`

## Questions?

If you encounter import issues:
1. Check that you're using the correct import path
2. Verify PYTHONPATH includes ubt_with_chronofactor if needed
3. Use root-level shims for backward compatibility
4. Open an issue with details if problems persist
3. Consult root README.md for routing guidance

---

**Status**: ✅ Fully functional, preserved for reference and regression testing  
**Maintenance**: Read-only; new development happens in core  
**Git History**: Preserved via `git mv` operations
