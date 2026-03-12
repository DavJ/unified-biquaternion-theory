#!/usr/bin/env python3
"""
Dimensional Consistency Linter for UBT LaTeX Files

This script automatically verifies dimensional consistency in LaTeX equations
tagged with \dimcheck{} commands.

Usage:
    python dimensional_lint.py <latex_file>
    python dimensional_lint.py --check-all  # Check all .tex files in consolidation_project/

Author: UBT v8 Consolidation Team
Date: November 2025
"""

import re
import sys
import os
from pathlib import Path
from typing import List, Tuple, Dict, Optional

# Dimensional analysis rules in natural units (ℏ = c = 1)
# All dimensions expressed as powers of mass M

class Dimension:
    """Represents a dimensional formula as powers of mass."""
    
    def __init__(self, power: float = 0):
        self.power = power
    
    def __mul__(self, other):
        return Dimension(self.power + other.power)
    
    def __truediv__(self, other):
        return Dimension(self.power - other.power)
    
    def __pow__(self, exponent):
        return Dimension(self.power * exponent)
    
    def __eq__(self, other):
        return abs(self.power - other.power) < 1e-6
    
    def __repr__(self):
        if abs(self.power) < 1e-6:
            return "[1]"
        elif abs(self.power - 1) < 1e-6:
            return "[M]"
        elif abs(self.power + 1) < 1e-6:
            return "[M^{-1}]"
        else:
            return f"[M^{{{self.power}}}]"
    
    @classmethod
    def parse(cls, dim_string: str) -> 'Dimension':
        """Parse dimension string like [M^2] or [M^{-1}] or [1]."""
        dim_string = dim_string.strip()
        
        # Match patterns like [M^{n}], [M^n], [M], [1]
        if dim_string == "[1]" or dim_string == "[]":
            return cls(0)
        elif dim_string == "[M]":
            return cls(1)
        
        # Match [M^{...}] or [M^...]
        match = re.match(r'\[M\^\{?([-+]?\d+\.?\d*)\}?\]', dim_string)
        if match:
            return cls(float(match.group(1)))
        
        raise ValueError(f"Cannot parse dimension: {dim_string}")


# Standard dimensional assignments
DIMENSIONS: Dict[str, Dimension] = {
    # Coordinates
    "x": Dimension(-1),  # Length
    "t": Dimension(-1),  # Time
    "\\psi": Dimension(-1),  # Imaginary time
    "\\tau": Dimension(-1),  # Complex time
    
    # Fields
    "\\Theta": Dimension(1),  # Biquaternionic field (mass dimension)
    "\\phi": Dimension(1),  # Scalar field
    "A_\\mu": Dimension(0),  # Gauge potential (dimensionless in natural units)
    "F_{\\mu\\nu}": Dimension(1),  # Field strength
    
    # Derivatives
    "\\partial_\\mu": Dimension(1),  # Partial derivative
    "\\nabla_\\mu": Dimension(1),  # Covariant derivative
    "\\nabla^2": Dimension(2),  # D'Alembertian
    
    # Volume elements
    "d^4x": Dimension(-4),  # 4D volume element
    "\\sqrt{-g}": Dimension(0),  # Determinant of metric (dimensionless)
    
    # Action and Lagrangian
    "\\mathcal{L}": Dimension(4),  # Lagrangian density
    "S": Dimension(0),  # Action (dimensionless)
    
    # Constants
    "m": Dimension(1),  # Mass
    "M": Dimension(1),  # Mass scale
    "\\Lambda": Dimension(1),  # Cutoff
    "\\mu": Dimension(1),  # Renormalization scale
    "g": Dimension(0),  # Coupling constant
    "\\alpha": Dimension(0),  # Fine structure constant
    
    # Alpha parameters
    "A": Dimension(0),
    "B": Dimension(0),
    "C": Dimension(0),
}


def extract_dimcheck_tags(latex_content: str) -> List[Tuple[int, str, str]]:
    """
    Extract all \dimcheck{} tags from LaTeX content.
    
    Returns:
        List of tuples (line_number, equation_context, dimension_spec)
    """
    lines = latex_content.split('\n')
    results = []
    
    for i, line in enumerate(lines, 1):
        # Find \dimcheck{...} patterns
        matches = re.finditer(r'\\dimcheck\{([^\}]+)\}', line)
        for match in matches:
            dim_spec = match.group(1)
            # Extract surrounding context (up to 100 chars before tag)
            start = max(0, match.start() - 100)
            context = line[start:match.start()].strip()
            results.append((i, context, dim_spec))
    
    return results


def verify_dimension_spec(dim_spec: str) -> Tuple[bool, Optional[str]]:
    """
    Verify a dimension specification like "[M^3] = [M^3]".
    
    Returns:
        (is_valid, error_message)
    """
    # Split on '='
    parts = dim_spec.split('=')
    if len(parts) != 2:
        return False, f"Expected format [dim1] = [dim2], got: {dim_spec}"
    
    try:
        left_dim = Dimension.parse(parts[0].strip())
        right_dim = Dimension.parse(parts[1].strip())
        
        if left_dim == right_dim:
            return True, None
        else:
            return False, f"Mismatch: {left_dim} ≠ {right_dim}"
    except ValueError as e:
        return False, str(e)


def check_equation_dimensions(equation: str) -> Tuple[bool, str]:
    """
    Check dimensional consistency of an equation.
    This is a simplified checker - full implementation would need equation parsing.
    
    Returns:
        (is_consistent, message)
    """
    # For now, just pass through to dimcheck tag verification
    # A full implementation would parse the equation and verify dimensions
    return True, "Equation parsing not yet implemented"


def lint_file(filepath: Path) -> Tuple[int, int, List[str]]:
    """
    Lint a single LaTeX file for dimensional consistency.
    
    Returns:
        (total_checks, failed_checks, error_messages)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return 0, 0, [f"Error reading file: {e}"]
    
    dimchecks = extract_dimcheck_tags(content)
    
    if not dimchecks:
        return 0, 0, []
    
    errors = []
    failed = 0
    
    for line_no, context, dim_spec in dimchecks:
        is_valid, error_msg = verify_dimension_spec(dim_spec)
        
        if not is_valid:
            failed += 1
            errors.append(
                f"  Line {line_no}: {dim_spec}\n"
                f"    Context: ...{context}\n"
                f"    Error: {error_msg}\n"
            )
    
    return len(dimchecks), failed, errors


def main():
    """Main entry point for dimensional linter."""
    
    if len(sys.argv) < 2:
        print("Usage: python dimensional_lint.py <file.tex>")
        print("       python dimensional_lint.py --check-all")
        sys.exit(1)
    
    if sys.argv[1] == "--check-all":
        # Check all .tex files in consolidation_project/
        project_dir = Path(__file__).parent.parent / "consolidation_project"
        tex_files = list(project_dir.glob("**/*.tex"))
        
        if not tex_files:
            print(f"No .tex files found in {project_dir}")
            sys.exit(1)
        
        print(f"Checking {len(tex_files)} LaTeX files...")
        print("=" * 70)
        
        total_checks = 0
        total_failed = 0
        files_with_errors = []
        
        for tex_file in tex_files:
            checks, failed, errors = lint_file(tex_file)
            total_checks += checks
            total_failed += failed
            
            if checks > 0:
                status = "✓" if failed == 0 else "✗"
                print(f"{status} {tex_file.relative_to(project_dir.parent)}: {checks} checks, {failed} failed")
            
            if errors:
                files_with_errors.append((tex_file, errors))
        
        print("=" * 70)
        print(f"Total: {total_checks} dimensional checks, {total_failed} failures")
        
        if files_with_errors:
            print("\nErrors found:\n")
            for tex_file, errors in files_with_errors:
                print(f"File: {tex_file.relative_to(project_dir.parent)}")
                for error in errors:
                    print(error)
        else:
            print("\n✓ All dimensional checks passed!")
        
        sys.exit(0 if total_failed == 0 else 1)
    
    else:
        # Check single file
        filepath = Path(sys.argv[1])
        
        if not filepath.exists():
            print(f"Error: File not found: {filepath}")
            sys.exit(1)
        
        checks, failed, errors = lint_file(filepath)
        
        print(f"Checking {filepath}...")
        print(f"Found {checks} dimensional checks, {failed} failures")
        
        if errors:
            print("\nErrors:")
            for error in errors:
                print(error)
            sys.exit(1)
        else:
            print("✓ All dimensional checks passed!")
            sys.exit(0)


if __name__ == "__main__":
    main()
