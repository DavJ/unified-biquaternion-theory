#!/usr/bin/env python3
"""
Dependency Scanner - Build Symbol Dependency Graph
==================================================

Constructs a directed graph of symbol dependencies to detect circular
dependencies in the alpha derivation.

Requires: graphviz (for DOT export)

Author: UBT Team
Version: 1.0
"""

import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


def load_equations(filepath: Path) -> List[Dict]:
    """Load equations from JSON."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data.get('equations', [])
    except Exception as e:
        print(f"Warning: Could not load {filepath}: {e}")
        return []


def extract_symbols(equation_content: str) -> Set[str]:
    """
    Extract mathematical symbols from equation content.
    
    Looks for: R_psi, N_eff, alpha, B, m_e, tau, etc.
    """
    symbols = set()
    
    # Common UBT symbols
    patterns = [
        r'R_\\psi',
        r'R_psi',
        r'N_\\mathrm\{eff\}',
        r'N_eff',
        r'\\mathcal\{R\}_\{UBT\}',
        r'R_UBT',
        r'\\alpha',
        r'\balpha\b',
        r'\bB\b',
        r'm_e',
        r'm_\\mu',
        r'\\tau',
        r'\\psi',
        r'\\Lambda',
        r'\\mu',
        r'Z_1',
        r'Z_2',
        r'Z_3',
    ]
    
    for pattern in patterns:
        if re.search(pattern, equation_content):
            # Normalize symbol name
            symbol = pattern.replace('\\b', '').replace('\\\\', '').replace('\\', '')
            symbol = symbol.replace('mathrm{eff}', 'eff')
            symbol = symbol.replace('mathcal{R}_{UBT}', 'R_UBT')
            symbols.add(symbol)
    
    return symbols


def build_dependency_graph(equations: List[Dict]) -> Tuple[Dict[str, Set[str]], Dict[str, List[str]]]:
    """
    Build dependency graph from equations.
    
    Returns:
        (dependencies, sources) where:
        - dependencies[symbol] = set of symbols it depends on
        - sources[symbol] = list of file:line where it's defined
    """
    dependencies = defaultdict(set)
    sources = defaultdict(list)
    
    for eq in equations:
        content = eq.get('content', '')
        path = Path(eq['path']).name
        lineno = eq['lineno']
        
        # Look for definition patterns: "X = ...", "X := ...", "Let X be"
        def_patterns = [
            (r'([A-Z_][A-Za-z0-9_\\{}\-]*)\s*[:=]', 'lhs'),  # X = ...
            (r'Let\s+([A-Z_\\][A-Za-z0-9_\\{}\-]*)', 'def'),  # Let X ...
            (r'Define\s+([A-Z_\\][A-Za-z0-9_\\{}\-]*)', 'def'),  # Define X ...
        ]
        
        defined_symbol = None
        for pattern, type_hint in def_patterns:
            match = re.search(pattern, content)
            if match:
                sym = match.group(1)
                # Normalize
                sym = sym.replace('\\', '').replace('{', '').replace('}', '')
                defined_symbol = sym
                sources[sym].append(f"{path}:{lineno}")
                break
        
        # Extract all symbols in the equation
        symbols_in_eq = extract_symbols(content)
        
        # If we found a definition, create dependencies
        if defined_symbol:
            # Remove self-reference
            deps = symbols_in_eq - {defined_symbol}
            dependencies[defined_symbol].update(deps)
        else:
            # No explicit definition, but record symbols present
            for sym in symbols_in_eq:
                if sym not in dependencies:
                    dependencies[sym] = set()
    
    return dict(dependencies), dict(sources)


def detect_cycles(dependencies: Dict[str, Set[str]]) -> List[List[str]]:
    """
    Detect cycles in dependency graph using DFS.
    
    Returns list of cycles (each cycle is a list of symbols).
    """
    cycles = []
    visited = set()
    rec_stack = set()
    
    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)
        path = path + [node]
        
        for neighbor in dependencies.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, path)
            elif neighbor in rec_stack:
                # Found cycle
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                cycles.append(cycle)
        
        rec_stack.remove(node)
    
    for node in dependencies:
        if node not in visited:
            dfs(node, [])
    
    return cycles


def export_dot(dependencies: Dict[str, Set[str]], sources: Dict[str, List[str]], 
               output_file: Path) -> None:
    """Export dependency graph to DOT format."""
    
    lines = []
    lines.append('digraph alpha_dependencies {')
    lines.append('  rankdir=LR;')
    lines.append('  node [shape=box, style=rounded];')
    lines.append('')
    
    # Add nodes
    for symbol in dependencies:
        source_info = sources.get(symbol, [])
        label = symbol
        if source_info:
            label += f'\\n({source_info[0]})'
        
        lines.append(f'  "{symbol}" [label="{label}"];')
    
    lines.append('')
    
    # Add edges
    for symbol, deps in dependencies.items():
        for dep in deps:
            lines.append(f'  "{symbol}" -> "{dep}";')
    
    lines.append('}')
    
    # Write DOT file
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"DOT file written to: {output_file}")


def render_svg(dot_file: Path, svg_file: Path) -> bool:
    """Render DOT file to SVG using graphviz."""
    try:
        result = subprocess.run(
            ['dot', '-Tsvg', str(dot_file), '-o', str(svg_file)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"SVG rendered to: {svg_file}")
            return True
        else:
            print(f"Warning: dot command failed: {result.stderr}")
            return False
    
    except FileNotFoundError:
        print("Warning: 'dot' command not found. Install graphviz to generate SVG.")
        print("  Ubuntu/Debian: sudo apt-get install graphviz")
        print("  macOS: brew install graphviz")
        return False
    except Exception as e:
        print(f"Warning: Could not render SVG: {e}")
        return False


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Build dependency graph for alpha derivation'
    )
    
    parser.add_argument('--equations', type=str,
                       default='reports/alpha_equations.json',
                       help='Equations JSON file')
    parser.add_argument('--dot', type=str,
                       default='reports/alpha_deps.dot',
                       help='Output DOT file')
    parser.add_argument('--svg', type=str,
                       default='reports/alpha_deps.svg',
                       help='Output SVG file')
    
    args = parser.parse_args()
    
    equations_file = Path(args.equations)
    dot_file = Path(args.dot)
    svg_file = Path(args.svg)
    
    print("=" * 70)
    print("Dependency Scanner")
    print("=" * 70)
    print()
    
    # Load equations
    print("Loading equations...")
    equations = load_equations(equations_file)
    print(f"  Loaded {len(equations)} equations")
    print()
    
    # Build graph
    print("Building dependency graph...")
    dependencies, sources = build_dependency_graph(equations)
    print(f"  Found {len(dependencies)} symbols")
    print(f"  Found {sum(len(deps) for deps in dependencies.values())} dependencies")
    print()
    
    # Detect cycles
    print("Checking for cycles...")
    cycles = detect_cycles(dependencies)
    
    if cycles:
        print(f"  WARNING: Found {len(cycles)} cycles!")
        for i, cycle in enumerate(cycles, 1):
            print(f"    Cycle {i}: {' → '.join(cycle)}")
    else:
        print("  ✓ No cycles detected")
    print()
    
    # Export DOT
    print("Exporting graph...")
    dot_file.parent.mkdir(parents=True, exist_ok=True)
    export_dot(dependencies, sources, dot_file)
    print()
    
    # Render SVG
    print("Rendering SVG...")
    render_svg(dot_file, svg_file)
    print()
    
    # Summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print()
    print(f"Symbols in graph: {len(dependencies)}")
    print(f"Cycles detected: {len(cycles)}")
    print()
    
    if cycles:
        print("⚠ WARNING: Circular dependencies detected!")
        print("  This may indicate that some parameters are not independently defined.")
    else:
        print("✓ No circular dependencies - derivation chain is well-founded")
    
    print()


if __name__ == '__main__':
    main()
