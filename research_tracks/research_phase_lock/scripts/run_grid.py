#!/usr/bin/env python3
"""
run_grid.py

Wrapper script to execute the main grid runner.
This is a convenience wrapper for the main run_grid module.

Usage:
    python scripts/run_grid.py --config configs/grid.yaml
    python scripts/run_grid.py --config configs/grid.yaml --dry-run
    python scripts/run_grid.py --config configs/grid.yaml --resume

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

# Import and run the main grid runner
from research_phase_lock.run_grid import main

if __name__ == "__main__":
    main()
