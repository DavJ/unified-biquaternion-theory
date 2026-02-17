#!/usr/bin/env python3
# tests/scan_top_level_imports.py
# SPDX-License-Identifier: MIT
"""
Scan test files for top-level imports that may be broken after restructuring.

This script walks through all test files and identifies imports that:
1. Are attempting to import modules from the repository root
2. May have been moved to subdirectories during restructuring
3. Need shims or path updates to work correctly

Usage:
    python tests/scan_top_level_imports.py
    
Output:
    Lists imports that are currently broken or may need attention.
"""
import ast
import sys
from pathlib import Path
from typing import Set, List, Tuple, Dict


def extract_imports_from_file(filepath: Path) -> Tuple[Set[str], Set[Tuple[str, str]]]:
    """
    Extract imports from a Python file using AST parsing.
    
    Returns:
        (simple_imports, from_imports)
        - simple_imports: Set of module names from 'import X' statements
        - from_imports: Set of (module, name) tuples from 'from X import Y' statements
    """
    simple_imports = set()
    from_imports = set()
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content, filename=str(filepath))
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    simple_imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    for alias in node.names:
                        from_imports.add((node.module, alias.name))
    except SyntaxError as e:
        print(f"Warning: Could not parse {filepath}: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Warning: Error reading {filepath}: {e}", file=sys.stderr)
    
    return simple_imports, from_imports


def is_module_importable(module_name: str, repo_root: Path) -> bool:
    """
    Check if a module can be imported from the repository root.
    
    Tries to import the module to see if it's available.
    """
    # Save original sys.path
    original_path = sys.path.copy()
    
    try:
        # Ensure repo root is in path
        if str(repo_root) not in sys.path:
            sys.path.insert(0, str(repo_root))
        
        # Try to import
        __import__(module_name)
        return True
    except ImportError:
        return False
    except Exception:
        # Other errors (AttributeError, etc.) suggest module exists but has issues
        return True
    finally:
        # Restore sys.path
        sys.path = original_path


def is_stdlib_or_third_party(module_name: str) -> bool:
    """
    Check if a module is from stdlib or a common third-party package.
    """
    # Common stdlib modules
    stdlib_modules = {
        'sys', 'os', 'pathlib', 'json', 'argparse', 'tempfile', 'unittest',
        'pytest', 're', 'subprocess', 'collections', 'functools', 'itertools',
        'math', 'datetime', 'inspect', 'ast', 'typing', 'hashlib', 'csv',
        'io', 'textwrap', 'shutil', 'glob', 'time', 'warnings', 'contextlib',
    }
    
    # Common third-party packages
    third_party_modules = {
        'numpy', 'scipy', 'matplotlib', 'pandas', 'pytest', 'healpy',
        'astropy', 'sklearn', 'torch', 'tensorflow',
    }
    
    # Get the top-level module name (e.g., 'numpy.linalg' -> 'numpy')
    top_level = module_name.split('.')[0]
    
    return top_level in stdlib_modules or top_level in third_party_modules


def scan_tests_directory(tests_dir: Path, repo_root: Path) -> Dict[str, List[str]]:
    """
    Scan all test files and identify broken imports.
    
    Returns:
        Dictionary mapping import names to list of files using them
    """
    broken_imports = {}
    
    # Find all Python test files
    test_files = list(tests_dir.glob("test_*.py"))
    test_files.extend(tests_dir.glob("*_test.py"))
    
    for test_file in test_files:
        simple_imports, from_imports = extract_imports_from_file(test_file)
        
        # Check simple imports (import X)
        for module_name in simple_imports:
            if is_stdlib_or_third_party(module_name):
                continue
            
            if not is_module_importable(module_name, repo_root):
                if module_name not in broken_imports:
                    broken_imports[module_name] = []
                broken_imports[module_name].append(str(test_file.relative_to(repo_root)))
        
        # Check from imports (from X import Y)
        for module_name, _ in from_imports:
            if is_stdlib_or_third_party(module_name):
                continue
            
            if not is_module_importable(module_name, repo_root):
                if module_name not in broken_imports:
                    broken_imports[module_name] = []
                if str(test_file.relative_to(repo_root)) not in broken_imports[module_name]:
                    broken_imports[module_name].append(str(test_file.relative_to(repo_root)))
    
    return broken_imports


def main():
    """Main entry point."""
    # Find repository root
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    tests_dir = repo_root / "tests"
    
    if not tests_dir.exists():
        print(f"Error: Tests directory not found: {tests_dir}", file=sys.stderr)
        return 1
    
    print("=" * 80)
    print("Scanning test files for broken top-level imports...")
    print("=" * 80)
    print()
    
    broken_imports = scan_tests_directory(tests_dir, repo_root)
    
    if not broken_imports:
        print("✅ SUCCESS: All imports in test files are valid!")
        print()
        print("No broken imports detected.")
        return 0
    
    print(f"⚠️  Found {len(broken_imports)} potentially broken imports:")
    print()
    
    for module_name in sorted(broken_imports.keys()):
        files = broken_imports[module_name]
        print(f"Module: {module_name}")
        print(f"  Used in {len(files)} file(s):")
        for filepath in sorted(files):
            print(f"    - {filepath}")
        print()
        
        # Suggest action
        print(f"  Action: Create root shim '{module_name}.py' or update import paths")
        print()
    
    print("=" * 80)
    print("Recommendations:")
    print("=" * 80)
    print()
    print("For each broken module:")
    print("  1. Check if it exists in a subdirectory (e.g., ubt_with_chronofactor/)")
    print("  2. Create a root-level shim that imports from the correct location")
    print("  3. Or update test files to use the correct import path")
    print()
    print("Example shim template:")
    print("  # module_name.py (root shim)")
    print("  from ubt_with_chronofactor.path.to.module import *")
    print()
    
    return 1


if __name__ == "__main__":
    sys.exit(main())
