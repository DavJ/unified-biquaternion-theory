#!/usr/bin/env python3
"""
Import Graph Analysis for Circular Dependency Detection
========================================================

Utility module for analyzing Python import dependencies and detecting
circular imports in the repository.

Uses Python AST to parse import statements and build a directed graph
of module dependencies, then runs cycle detection to find circular imports.

Author: UBT Team
Version: v1.0
Status: Test infrastructure for court-grade test suite
"""

import ast
import os
from pathlib import Path
from typing import Dict, Set, List, Tuple, Optional


class ImportGraphAnalyzer:
    """Analyzes Python imports to detect circular dependencies."""
    
    def __init__(self, repo_root: Path):
        """
        Initialize the import graph analyzer.
        
        Args:
            repo_root: Root directory of the repository
        """
        self.repo_root = Path(repo_root)
        self.import_graph: Dict[str, Set[str]] = {}
        self.module_files: Dict[str, Path] = {}
        
    def _should_skip_dir(self, dir_path: Path) -> bool:
        """Check if directory should be skipped during analysis."""
        skip_dirs = {
            '.git', '__pycache__', '.pytest_cache', 'venv', '.venv',
            'build', 'dist', 'out', '.tox', 'htmlcov', 'node_modules',
            '.mypy_cache', '.eggs', '*.egg-info'
        }
        
        dir_name = dir_path.name
        return (
            dir_name.startswith('.') or
            dir_name in skip_dirs or
            dir_name.endswith('.egg-info')
        )
    
    def _get_module_name(self, file_path: Path) -> Optional[str]:
        """
        Convert file path to module name.
        
        Args:
            file_path: Path to Python file
            
        Returns:
            Module name (e.g., 'forensic_fingerprint.loaders.planck')
            or None if not a valid module
        """
        try:
            rel_path = file_path.relative_to(self.repo_root)
            parts = list(rel_path.parts)
            
            # Remove .py extension from last part
            if parts[-1].endswith('.py'):
                parts[-1] = parts[-1][:-3]
            
            # Skip if __init__.py (parent dir is the module)
            if parts[-1] == '__init__':
                parts = parts[:-1]
                if not parts:
                    return None
            
            return '.'.join(parts)
        except ValueError:
            return None
    
    def _parse_imports(self, file_path: Path) -> Set[str]:
        """
        Parse import statements from a Python file.
        
        Args:
            file_path: Path to Python file
            
        Returns:
            Set of imported module names
        """
        imports = set()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.add(alias.name.split('.')[0])
                
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.add(node.module.split('.')[0])
                    elif node.level > 0:
                        # Relative import - try to resolve
                        current_module = self._get_module_name(file_path)
                        if current_module:
                            parts = current_module.split('.')
                            if len(parts) >= node.level:
                                base = '.'.join(parts[:-node.level]) if node.level < len(parts) else parts[0]
                                imports.add(base.split('.')[0])
        
        except (SyntaxError, UnicodeDecodeError, FileNotFoundError):
            # Skip files that can't be parsed
            pass
        
        return imports
    
    def build_graph(self, include_external: bool = False) -> None:
        """
        Build the import dependency graph.
        
        Args:
            include_external: If True, include external packages.
                            If False, only internal modules are tracked.
        """
        # Find all Python files
        for root, dirs, files in os.walk(self.repo_root):
            root_path = Path(root)
            
            # Filter out directories to skip
            dirs[:] = [d for d in dirs if not self._should_skip_dir(root_path / d)]
            
            for file in files:
                if not file.endswith('.py'):
                    continue
                
                file_path = root_path / file
                module_name = self._get_module_name(file_path)
                
                if not module_name:
                    continue
                
                # Store module file mapping
                self.module_files[module_name] = file_path
                
                # Parse imports
                imports = self._parse_imports(file_path)
                
                if not include_external:
                    # Filter to only internal modules
                    internal_imports = {
                        imp for imp in imports
                        if self._is_internal_module(imp)
                    }
                    imports = internal_imports
                
                # Store in graph
                if module_name not in self.import_graph:
                    self.import_graph[module_name] = set()
                
                self.import_graph[module_name].update(imports)
    
    def _is_internal_module(self, module_name: str) -> bool:
        """Check if a module is internal to the repository."""
        # Check if it's one of our known packages
        internal_packages = {
            'forensic_fingerprint', 'alpha_core_repro', 'strict_ubt',
            'ubt_masses', 'scripts', 'tools', 'tests'
        }
        
        top_level = module_name.split('.')[0]
        return top_level in internal_packages
    
    def detect_cycles(self) -> List[List[str]]:
        """
        Detect circular dependencies using DFS.
        
        Returns:
            List of cycles, where each cycle is a list of module names
            forming a circular dependency chain.
        """
        cycles = []
        visited = set()
        rec_stack = set()
        path = []
        
        def dfs(node: str) -> None:
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            
            for neighbor in self.import_graph.get(node, set()):
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in rec_stack:
                    # Found a cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)
            
            path.pop()
            rec_stack.remove(node)
        
        # Run DFS from each unvisited node
        for node in self.import_graph:
            if node not in visited:
                dfs(node)
        
        return cycles
    
    def check_forbidden_imports(
        self,
        module_pattern: str,
        forbidden_patterns: List[str]
    ) -> List[Tuple[str, str]]:
        """
        Check if modules matching a pattern import forbidden modules.
        
        Args:
            module_pattern: Pattern to match modules (e.g., 'forensic_fingerprint')
            forbidden_patterns: List of patterns that should not be imported
            
        Returns:
            List of (module, forbidden_import) tuples representing violations
        """
        violations = []
        
        for module, imports in self.import_graph.items():
            # Check if module matches pattern
            if not module.startswith(module_pattern):
                continue
            
            # Check each import against forbidden patterns
            for imp in imports:
                for forbidden in forbidden_patterns:
                    if imp.startswith(forbidden):
                        violations.append((module, imp))
        
        return violations


def format_cycle(cycle: List[str]) -> str:
    """
    Format a cycle for display.
    
    Args:
        cycle: List of module names forming a cycle
        
    Returns:
        Formatted string showing the cycle path
    """
    if not cycle:
        return "No cycle"
    
    return " -> ".join(cycle)


def find_repo_root(start_path: Optional[Path] = None) -> Path:
    """
    Find the repository root by looking for .git directory.
    
    Args:
        start_path: Starting path for search (defaults to current directory)
        
    Returns:
        Path to repository root
        
    Raises:
        FileNotFoundError: If repository root cannot be found
    """
    if start_path is None:
        start_path = Path.cwd()
    
    current = Path(start_path).resolve()
    
    while current != current.parent:
        if (current / '.git').exists():
            return current
        current = current.parent
    
    raise FileNotFoundError("Could not find repository root (no .git directory)")
