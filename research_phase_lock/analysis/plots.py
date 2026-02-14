#!/usr/bin/env python3
"""
plots.py

Visualization utilities for grid experiment results.

Provides functions to:
- Create comparison plots across parameter variations
- Visualize parameter space exploration
- Generate diagnostic visualizations

Author: UBT Research Team
License: See repository LICENSE.md
"""

import os
from typing import Any, Dict, List, Optional

from research_phase_lock.utils.io import ensure_dir


def plot_parameter_sweep(
    results: List[Dict[str, Any]],
    param_name: str,
    metric: str = "phase_coherence",
    output_path: Optional[str] = None,
    title: Optional[str] = None
) -> None:
    """
    Plot metric vs. parameter value.
    
    Args:
        results: List of result dictionaries
        param_name: Parameter to plot on x-axis
        metric: Metric to plot on y-axis
        output_path: Output PNG path (None = show only)
        title: Plot title
    """
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("Warning: matplotlib not available, skipping plot")
        return
    
    # Extract data
    x_vals = []
    y_vals = []
    
    for r in results:
        if param_name not in r or metric not in r:
            continue
        
        try:
            x = float(r[param_name]) if isinstance(r[param_name], (int, float, str)) else str(r[param_name])
            y = float(r[metric])
            x_vals.append(x)
            y_vals.append(y)
        except (ValueError, TypeError):
            continue
    
    if not x_vals:
        print(f"Warning: No valid data for {param_name} vs {metric}")
        return
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Scatter plot
    ax.scatter(x_vals, y_vals, alpha=0.6, s=50)
    
    ax.set_xlabel(param_name, fontsize=12)
    ax.set_ylabel(metric, fontsize=12)
    
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold')
    else:
        ax.set_title(f"{metric} vs {param_name}", fontsize=14)
    
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if output_path:
        ensure_dir(output_path)
        plt.savefig(output_path, dpi=150)
        print(f"Saved plot: {output_path}")
    else:
        plt.show()
    
    plt.close()


def plot_grid_heatmap(
    results: List[Dict[str, Any]],
    param_x: str,
    param_y: str,
    metric: str = "phase_coherence",
    output_path: Optional[str] = None
) -> None:
    """
    Create heatmap of metric across two parameters.
    
    Args:
        results: List of result dictionaries
        param_x: Parameter for x-axis
        param_y: Parameter for y-axis
        metric: Metric for color
        output_path: Output PNG path
    """
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("Warning: matplotlib not available, skipping heatmap")
        return
    
    # Build grid
    grid_data = {}
    for r in results:
        if param_x not in r or param_y not in r or metric not in r:
            continue
        
        try:
            x = str(r[param_x])
            y = str(r[param_y])
            z = float(r[metric])
            
            if (x, y) not in grid_data:
                grid_data[(x, y)] = []
            grid_data[(x, y)].append(z)
        except (ValueError, TypeError):
            continue
    
    if not grid_data:
        print(f"Warning: No valid data for heatmap")
        return
    
    # Average duplicate entries
    for key in grid_data:
        grid_data[key] = np.mean(grid_data[key])
    
    # Convert to matrix
    x_labels = sorted(set(k[0] for k in grid_data.keys()))
    y_labels = sorted(set(k[1] for k in grid_data.keys()))
    
    matrix = np.full((len(y_labels), len(x_labels)), np.nan)
    
    for (x, y), z in grid_data.items():
        i = y_labels.index(y)
        j = x_labels.index(x)
        matrix[i, j] = z
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    
    im = ax.imshow(matrix, aspect='auto', cmap='viridis', interpolation='nearest')
    
    ax.set_xticks(range(len(x_labels)))
    ax.set_yticks(range(len(y_labels)))
    ax.set_xticklabels(x_labels, rotation=45, ha='right')
    ax.set_yticklabels(y_labels)
    
    ax.set_xlabel(param_x, fontsize=12)
    ax.set_ylabel(param_y, fontsize=12)
    ax.set_title(f"{metric} Heatmap", fontsize=14, fontweight='bold')
    
    plt.colorbar(im, ax=ax, label=metric)
    
    plt.tight_layout()
    
    if output_path:
        ensure_dir(output_path)
        plt.savefig(output_path, dpi=150)
        print(f"Saved heatmap: {output_path}")
    else:
        plt.show()
    
    plt.close()
