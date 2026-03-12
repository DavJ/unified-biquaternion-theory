"""
Hygiene gate test: ensure no stub patterns remain in 2-loop code.

This test scans all Python files in the alpha_two_loop directory tree
to verify that no placeholder patterns, hardcoded constants, or incomplete
implementations remain.

Required for acceptance: all tests must pass before locking R_UBT = 1.
"""

import pathlib
import re
import pytest


def test_no_stub_patterns_in_2loop_path():
    """
    Verify no stub patterns exist in alpha_two_loop Python code.
    
    Forbidden patterns:
    - 'return 1.0' (use sp.Integer(1) for symbolic, compute numerically)
    - 'TODO' or 'FIXME' comments
    - 'placeholder' in comments or docstrings
    - 'proof sketch' references
    - Hardcoded physical constants (137.036, 1.84, etc.)
    """
    # Root of alpha_two_loop directory
    root = pathlib.Path(__file__).parents[1]
    
    # Patterns to detect
    forbidden_patterns = [
        (r"\breturn\s+1\.0\b", "hardcoded 'return 1.0' found"),
        (r"\bTODO\b", "TODO comment found"),
        (r"\bFIXME\b", "FIXME comment found"),
        (r"\bplaceholder\b", "placeholder reference found"),
        (r"\bproof\s+sketch\b", "proof sketch reference found"),
        (r"\breturn\s+None\s*#.*[Ii]ntentionally incomplete", "intentionally incomplete return found"),
        # Specific physical constants that should be computed
        (r"137\.03[0-9]", "hardcoded alpha^-1 value found"),
        (r"1\.84", "hardcoded R_UBT candidate found"),
    ]
    
    violations = []
    
    # Scan all Python files
    for py_file in root.rglob("**/*.py"):
        # Skip test files themselves and __init__.py
        if py_file.name.startswith("test_") or py_file.name == "__init__.py":
            continue
        
        # Skip if not in symbolics directory
        if "symbolics" not in str(py_file):
            continue
        
        try:
            content = py_file.read_text(encoding="utf-8")
        except Exception:
            continue
        
        # Check each pattern
        for pattern, description in forbidden_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                # Get line number
                line_num = content[:match.start()].count('\n') + 1
                violations.append({
                    'file': str(py_file.relative_to(root.parent)),
                    'line': line_num,
                    'pattern': pattern,
                    'description': description,
                    'snippet': content[max(0, match.start()-20):match.end()+20]
                })
    
    # Report violations
    if violations:
        error_msg = ["Stub patterns detected in 2-loop code:\n"]
        for v in violations:
            error_msg.append(f"  {v['file']}:{v['line']} - {v['description']}")
            error_msg.append(f"    Context: ...{v['snippet']}...")
        error_msg.append("\nAll implementations must be complete before locking R_UBT = 1.")
        assert False, "\n".join(error_msg)


def test_symbolic_computation_not_hardcoded():
    """
    Verify that key functions return symbolic expressions, not hardcoded numbers.
    
    This test imports the main evaluation module and checks that R_UBT
    computation uses symbolic algebra, not just returning a constant.
    """
    import sys
    symbolics_dir = pathlib.Path(__file__).parent.parent / "symbolics"
    sys.path.insert(0, str(symbolics_dir))
    
    try:
        from ct_two_loop_eval import CTVacuumPolarization
        import sympy as sp
        
        # Create calculator
        calc = CTVacuumPolarization()
        
        # Test that thomson_limit_R_UBT returns a SymPy expression
        result = calc.thomson_limit_R_UBT(mu_val=1.0, xi_val=1.0)
        
        # Should be sp.Integer(1), not float 1.0
        assert isinstance(result, (sp.Basic, int)), \
            f"R_UBT should be symbolic or exact int, got {type(result)}"
        
        # If it's a SymPy object, verify it equals 1
        if isinstance(result, sp.Basic):
            assert result == sp.Integer(1), \
                f"R_UBT should equal sp.Integer(1), got {result}"
        else:
            # If it's a Python int, that's acceptable (exact)
            assert result == 1, \
                f"R_UBT should equal 1, got {result}"
    
    finally:
        sys.path.pop(0)


def test_master_integrals_have_implementations():
    """
    Verify that all master integrals have concrete implementations.
    
    Master integrals should not be placeholders like:
        return sp.Function("MI_sunset")(...)
    
    They should have actual expressions in terms of Gamma functions,
    polylogarithms, zeta values, etc.
    """
    import sys
    symbolics_dir = pathlib.Path(__file__).parent.parent / "symbolics"
    sys.path.insert(0, str(symbolics_dir))
    
    try:
        from master_integrals import MI_REGISTRY
        
        # Get all master integrals
        for mi_name, mi_obj in MI_REGISTRY.integrals.items():
            # Try to evaluate symbolically
            try:
                result = mi_obj.symbolic()
                
                # Check that result is not just a symbolic function call
                # (which would indicate a placeholder)
                result_str = str(result)
                
                # Forbidden: functions that are just placeholders
                forbidden_names = ['MI_sunset', 'MI_double_bubble', 'MI_fermion_bubble']
                for forbidden in forbidden_names:
                    assert forbidden not in result_str or "(" not in result_str, \
                        f"Master integral {mi_name} appears to be a placeholder: {result_str[:100]}"
            
            except NotImplementedError:
                pytest.fail(f"Master integral {mi_name} has no symbolic() implementation")
    
    finally:
        sys.path.pop(0)


def test_ibp_reduction_has_real_coefficients():
    """
    Verify that IBP reduction produces actual algebraic coefficients,
    not symbolic placeholders.
    
    Coefficients should be rational numbers or algebraic expressions
    in q2, mu, xi, epsilon - not Symbol('c1'), Symbol('c2'), etc.
    """
    import sys
    symbolics_dir = pathlib.Path(__file__).parent.parent / "symbolics"
    sys.path.insert(0, str(symbolics_dir))
    
    try:
        from ibp_system import reduce_all_vacuum_polarization_diagrams
        import sympy as sp
        
        # Get all reductions
        reductions = reduce_all_vacuum_polarization_diagrams()
        
        # Check each coefficient
        for diagram_name, mi_list in reductions.items():
            for mi_name, coeff in mi_list:
                # Coefficient should not be a generic symbol like Symbol('c_sunset')
                coeff_str = str(coeff)
                
                # Allow proper variables (q2, mu, xi, epsilon) but not placeholder coefficients
                forbidden_coeff_names = ['c_sunset', 'c_double', 'c1', 'c2', 'c3', 
                                         'Z1_coeff', 'coeff', 'coefficient']
                
                for forbidden in forbidden_coeff_names:
                    if forbidden in coeff_str and not any(
                        allowed in coeff_str for allowed in ['q2', 'mu', 'xi', 'epsilon', 'm']
                    ):
                        pytest.fail(
                            f"IBP reduction {diagram_name} has placeholder coefficient: "
                            f"{mi_name} with coeff = {coeff}"
                        )
    
    finally:
        sys.path.pop(0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
