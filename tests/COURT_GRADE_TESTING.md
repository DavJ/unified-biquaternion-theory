# Court-Grade Testing Infrastructure

This document describes the court-grade testing infrastructure implemented for the UBT repository. The test suite has been hardened to catch bugs early, prevent circular dependencies, and enforce strict correctness standards suitable for production code review.

## Overview

The court-grade test suite implements:

1. **Real assertions** replacing all placeholder tests
2. **Circular import detection** via AST-based dependency graph analysis
3. **Module boundary enforcement** to prevent hidden coupling
4. **NaN/inf guards** on all numeric operations
5. **Strict warning enforcement** (warnings treated as errors)

## Running Tests

### Standard Test Run

```bash
pytest
```

All warnings are treated as errors by default (configured in `pytest.ini`).

### Run Specific Test Categories

```bash
# Circularity checks
pytest tests/test_no_circularity.py -v

# QED limit tests (numeric correctness)
pytest tests/test_qed_limit.py -v

# Forensic fingerprint tests
pytest tests/test_forensic_fingerprint.py -v
```

### Expected Output

```
======================== 169 passed, 2 skipped in 9.82s ========================
```

All tests should pass with no warnings. Skipped tests are intentional (e.g., precision tests requiring heavy computation).

## New Testing Features

### 1. Circular Import Detection

**File:** `tests/_import_graph.py`

Analyzes all Python files in the repository to detect circular import dependencies.

**How it works:**
- Walks repository directory tree (excluding venv, build, .git, etc.)
- Parses each `.py` file using Python AST
- Builds directed graph of module dependencies
- Runs DFS cycle detection
- Reports any circular import chains found

**Example usage:**

```python
from _import_graph import ImportGraphAnalyzer, find_repo_root

analyzer = ImportGraphAnalyzer(find_repo_root())
analyzer.build_graph(include_external=False)
cycles = analyzer.detect_cycles()

if cycles:
    for cycle in cycles:
        print(" -> ".join(cycle))
```

**Test:** `tests/test_no_circularity.py::test_no_circular_imports`

If a circular import exists, output will show:
```
✗ Found 1 circular import(s):
  1. module_a -> module_b -> module_c -> module_a
```

### 2. Dependency Boundary Enforcement

**Test:** `tests/test_no_circularity.py::test_dependency_boundaries`

Enforces architectural boundaries between modules.

**Current rules:**
- `forensic_fingerprint/` **must not** import from:
  - `strict_ubt`
  - `alpha_core_repro`
  - `ubt_masses`
  - `scripts.ubt_*`
  - `scripts.fit_*`

**Rationale:** 
The forensic fingerprint pipeline is a standalone statistical analysis tool. Importing theory-specific modules would create hidden coupling and prevent reuse.

**Example violation output:**
```
✗ Found 2 boundary violation(s):
  - forensic_fingerprint.loaders.planck imports strict_ubt
    (violates 'forensic_fingerprint' boundary)
```

### 3. NaN/inf Guards

All numeric calculations now check for invalid values:

```python
# Before (risky):
R_UBT = Pi_CT / Pi_QED

# After (court-grade):
if abs(Pi_QED) < 1e-15:
    # Handle zero denominator explicitly
    continue

R_UBT = Pi_CT / Pi_QED

# Assert results are finite
assert not np.isnan(R_UBT), f"R_UBT is NaN at μ={mu}"
assert not np.isinf(R_UBT), f"R_UBT is inf at μ={mu}"
```

**Files updated:**
- `tests/test_qed_limit.py` - Three test functions hardened

### 4. Strict Warning Enforcement

**Configuration:** `pytest.ini`

```ini
filterwarnings =
    error  # Treat all warnings as errors
```

**Expected warnings must be explicitly handled:**

Example from `test_forensic_fingerprint.py`:

```python
# Synthetic data without uncertainties generates expected warning
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', message='No uncertainties in.*', category=UserWarning)
    data = planck.load_planck_data(obs_file, model_file=model_file)
```

**Why this matters:**
- Catches accidental warnings that hide bugs
- Forces developers to acknowledge and handle warnings explicitly
- Prevents warning suppression at global scope

## Removed Placeholder Tests

All `assert True` and `assert False` placeholders have been replaced with real checks:

### Before:
```python
def test_M_theta_independence():
    # ... documentation ...
    assert True, "M_Θ is correctly used as an independent input parameter"
```

### After:
```python
def test_M_theta_independence():
    # ... documentation ...
    from fit_flavour_minimal import texture_to_masses
    import inspect
    
    sig = inspect.signature(texture_to_masses)
    params = list(sig.parameters.keys())
    
    # Real assertion: M_theta must be a parameter
    theta_found = any('theta' in p.lower() for p in params)
    assert theta_found, "M_Θ not found as input parameter"
    
    # Real assertion: Experimental masses must NOT be parameters
    mass_params = [p for p in params if 'mass' in p.lower() and 'exp' in p.lower()]
    assert len(mass_params) == 0, f"Experimental masses found: {mass_params}"
```

## Import Graph API

### `ImportGraphAnalyzer`

**Methods:**

- `build_graph(include_external=False)` - Parse all Python files and build dependency graph
- `detect_cycles()` - Find circular import chains via DFS
- `check_forbidden_imports(module_pattern, forbidden_patterns)` - Check boundary violations

**Example:**

```python
from _import_graph import ImportGraphAnalyzer, find_repo_root

analyzer = ImportGraphAnalyzer(find_repo_root())
analyzer.build_graph()

# Find cycles
cycles = analyzer.detect_cycles()
print(f"Found {len(cycles)} cycle(s)")

# Check boundaries
violations = analyzer.check_forbidden_imports(
    'forensic_fingerprint',
    ['strict_ubt', 'alpha_core_repro']
)
print(f"Found {len(violations)} violation(s)")
```

## Adding New Tests

### Guideline: No Placeholders

❌ **Never do this:**
```python
def test_something():
    # TODO: implement this later
    assert True
```

✅ **Instead:**
```python
@pytest.mark.skip(reason="Issue #123: Waiting for X to be implemented")
def test_something():
    # Will be implemented when X is ready
    pass
```

Or implement a real check immediately, even if partial.

### Guideline: Handle Expected Warnings

If a test legitimately produces warnings:

```python
def test_something():
    import warnings
    with warnings.catch_warnings():
        # Narrow scope: only ignore specific warning
        warnings.filterwarnings('ignore', message='Expected warning text', category=UserWarning)
        
        # Code that produces warning
        result = function_that_warns()
    
    # Continue with assertions
    assert result is not None
```

### Guideline: Check Numeric Results

Always validate that numeric results are finite:

```python
result = compute_something()

# Check for invalid values
assert not np.isnan(result), "Result is NaN"
assert not np.isinf(result), "Result is infinite"
assert result > 0, "Result must be positive"
```

## Maintenance

### Adding New Modules

When adding new Python packages to the repository:

1. **Test for circular imports:** The test runs automatically
2. **Check boundary rules:** Update `test_dependency_boundaries()` if new boundaries are needed
3. **Run full suite:** Ensure `pytest` passes

### Fixing Circular Import Issues

If `test_no_circular_imports` fails:

1. **Identify the cycle:** Test output shows the full import chain
2. **Break the cycle:** Options:
   - Move shared code to a common module
   - Use late imports (import inside functions)
   - Restructure module hierarchy
3. **Verify fix:** Re-run `pytest tests/test_no_circularity.py::test_no_circular_imports`

### Adding Boundary Rules

To add a new boundary rule:

Edit `tests/test_no_circularity.py`, function `test_dependency_boundaries()`:

```python
boundary_rules = {
    'forensic_fingerprint': [
        'strict_ubt',
        'alpha_core_repro',
        # Add new forbidden imports here
    ],
    # Add new boundaries here
    'new_module': ['forbidden_module'],
}
```

## Technical Details

### Import Graph Construction

The import graph analyzer uses Python's `ast` module to parse imports:

```python
tree = ast.parse(source_code)

for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        # Handle: import foo
        ...
    elif isinstance(node, ast.ImportFrom):
        # Handle: from foo import bar
        ...
```

**Supported:**
- Absolute imports: `import foo`, `from foo import bar`
- Relative imports: `from . import bar`, `from ..foo import baz`
- Internal module filtering (external packages excluded by default)

**Not supported (intentionally):**
- Dynamic imports: `__import__()`, `importlib.import_module()`
- These are rare and should be avoided for clarity

### Cycle Detection Algorithm

Uses depth-first search with recursion stack tracking:

```python
def dfs(node):
    visited.add(node)
    rec_stack.add(node)  # Mark as "in current path"
    
    for neighbor in graph[node]:
        if neighbor in rec_stack:
            # Found cycle: neighbor is already in path
            report_cycle()
        elif neighbor not in visited:
            dfs(neighbor)
    
    rec_stack.remove(node)  # No longer in path
```

Time complexity: O(V + E) where V = modules, E = imports

## FAQ

### Q: Why treat warnings as errors?

**A:** Warnings often indicate bugs:
- Division by zero (NaN results)
- Deprecated API usage
- Type mismatches
- Resource leaks

In production code, warnings should either be fixed or explicitly acknowledged.

### Q: What if I need to add a legitimate warning?

**A:** Handle it explicitly in the test:

```python
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', message='...', category=...)
    code_that_warns()
```

Or if it's a bug: fix the underlying issue instead of suppressing.

### Q: Can I disable strict warnings temporarily?

**A:** Yes, but not recommended:

```bash
# Disable for one run
pytest -W default

# Or modify pytest.ini temporarily (remember to revert)
```

Better approach: Fix the warnings or handle them explicitly.

### Q: How do I know if a cycle is acceptable?

**A:** Circular imports are rarely acceptable. They indicate:
- Poor module separation
- Missing abstraction layers
- Potential initialization issues

If you think you have a legitimate case, discuss with the team first.

## Summary

The court-grade test suite ensures:

✅ **No placeholder tests** - every test makes real assertions  
✅ **No circular imports** - clean module dependency graph  
✅ **No boundary violations** - architecture enforced by tests  
✅ **No silent NaN/inf** - numeric correctness validated  
✅ **No ignored warnings** - all warnings acknowledged explicitly  

This infrastructure provides confidence that code changes won't introduce subtle bugs or architectural violations.
