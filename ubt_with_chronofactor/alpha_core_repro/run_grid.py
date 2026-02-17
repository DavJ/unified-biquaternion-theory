# alpha_core_repro/run_grid.py
from alpha_core_repro.alpha_two_loop import run_grid, TwoLoopConfig
from p_universes.sector_ff import sector_form_factor

if __name__ == "__main__":
    cfg = TwoLoopConfig(strict=False, form_factor=sector_form_factor)
    path = run_grid([127,131,137,139,149], cfg)
    print(f"Wrote {path}")
