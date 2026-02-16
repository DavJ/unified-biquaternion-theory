#!/usr/bin/env python3
"""
Theta-Fit Tau Tool for UBT

Fits cluster width in spectral scan CSV data to estimate effective dispersion
parameter tau_hat. Implements Gaussian envelope and theta3 envelope models.

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def load_csv(csv_path: Path) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load scan CSV and extract k and psd_obs columns.

    Supports columns: 'raw', 'n' (for k) and 'psd_obs' (for PSD).

    Args:
        csv_path: Path to CSV file

    Returns:
        k: Array of integer indices
        psd_obs: Array of observed PSD values

    Raises:
        ValueError: If CSV format is invalid
    """
    try:
        # Read header
        with open(csv_path, "r") as f:
            header = f.readline().strip().split(",")

        # Find column indices
        try:
            n_idx = header.index("n")
        except ValueError:
            try:
                n_idx = header.index("raw")
            except ValueError:
                raise ValueError(
                    f"CSV must contain 'n' or 'raw' column. Found: {header}"
                )

        try:
            psd_idx = header.index("psd_obs")
        except ValueError:
            raise ValueError(f"CSV must contain 'psd_obs' column. Found: {header}")

        # Read data as float array
        data = np.genfromtxt(csv_path, delimiter=",", skip_header=1)

        if data.ndim == 1:
            # Single row
            data = data.reshape(1, -1)

        # Extract columns
        k = data[:, n_idx].astype(int)
        psd_obs = data[:, psd_idx]

        return k, psd_obs

    except Exception as e:
        raise ValueError(f"Failed to load CSV {csv_path}: {e}") from e


def gauss_envelope(
    k: np.ndarray,
    baseline: float,
    A: float,
    k0: float,
    sigma: float,
) -> np.ndarray:
    """
    Gaussian envelope model.

    psd(k) = baseline + A * exp(-(k-k0)^2 / (2*sigma^2))

    Args:
        k: Index array
        baseline: Background level
        A: Peak amplitude
        k0: Peak center
        sigma: Width parameter

    Returns:
        Fitted PSD values
    """
    return baseline + A * np.exp(-((k - k0) ** 2) / (2 * sigma**2))


def gauss_envelope_with_spikes(
    k: np.ndarray,
    baseline: float,
    A: float,
    k0: float,
    sigma: float,
    spike_ks: List[int],
    spike_amplitudes: List[float],
) -> np.ndarray:
    """
    Gaussian envelope with discrete spikes at specified k values.

    Args:
        k: Index array
        baseline: Background level
        A: Peak amplitude
        k0: Peak center
        sigma: Width parameter
        spike_ks: List of k values where spikes occur
        spike_amplitudes: List of spike amplitudes

    Returns:
        Fitted PSD values
    """
    psd = gauss_envelope(k, baseline, A, k0, sigma)

    for spike_k, spike_amp in zip(spike_ks, spike_amplitudes):
        psd += spike_amp * (k == spike_k).astype(float)

    return psd


def theta3_envelope(
    k: np.ndarray,
    baseline: float,
    A: float,
    k0: float,
    a: float,
    M: int = 6,
    K: float = 1.0,
) -> np.ndarray:
    """
    Theta3-inspired envelope model using truncated Fourier series.

    w(k) = sum_{m=-M..M} exp(-a*m^2) * cos(2π*m*(k-k0)/K)
    psd(k) = baseline + A * w(k)

    Args:
        k: Index array
        baseline: Background level
        A: Peak amplitude
        k0: Peak center
        a: Dispersion parameter (related to tau)
        M: Truncation order (default 6)
        K: Period parameter (default 1.0)

    Returns:
        Fitted PSD values
    """
    w = np.zeros_like(k, dtype=float)

    for m in range(-M, M + 1):
        w += np.exp(-a * m**2) * np.cos(2 * np.pi * m * (k - k0) / K)

    return baseline + A * w


def fit_gauss_envelope(
    k: np.ndarray,
    psd_obs: np.ndarray,
    kmin: int,
    kmax: int,
    include_spikes: bool = False,
    spike_ks: Optional[List[int]] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Fit Gaussian envelope model to data in [kmin, kmax] range.

    Args:
        k: Index array
        psd_obs: Observed PSD values
        kmin: Minimum k for fit window
        kmax: Maximum k for fit window
        include_spikes: Whether to include spike terms
        spike_ks: List of k values for spikes

    Returns:
        popt: Optimal parameters
        pcov: Covariance matrix

    Raises:
        RuntimeError: If fit fails
    """
    # Filter to fit window
    mask = (k >= kmin) & (k <= kmax)
    k_fit = k[mask]
    psd_fit = psd_obs[mask]

    if len(k_fit) < 4:
        raise ValueError(
            f"Insufficient data points in range [{kmin}, {kmax}]: {len(k_fit)}"
        )

    # Initial guess
    k0_guess = (kmin + kmax) / 2
    baseline_guess = np.percentile(psd_fit, 10)
    A_guess = np.max(psd_fit) - baseline_guess
    sigma_guess = (kmax - kmin) / 4

    if include_spikes and spike_ks:
        # Include spike amplitudes in fit
        n_spikes = len(spike_ks)
        p0 = [baseline_guess, A_guess, k0_guess, sigma_guess] + [0.5] * n_spikes

        def model(k_val, baseline, A, k0, sigma, *spike_amps):
            return gauss_envelope_with_spikes(
                k_val, baseline, A, k0, sigma, spike_ks, list(spike_amps)
            )

    else:
        p0 = [baseline_guess, A_guess, k0_guess, sigma_guess]
        model = gauss_envelope

    try:
        popt, pcov = curve_fit(
            model,
            k_fit,
            psd_fit,
            p0=p0,
            bounds=(
                [0, 0, kmin, 0.1] + ([0] * (len(p0) - 4)),
                [np.inf, np.inf, kmax, (kmax - kmin)] + ([np.inf] * (len(p0) - 4)),
            ),
            maxfev=10000,
        )
        return popt, pcov

    except Exception as e:
        raise RuntimeError(f"Gaussian fit failed: {e}") from e


def fit_theta3_envelope(
    k: np.ndarray,
    psd_obs: np.ndarray,
    kmin: int,
    kmax: int,
    M: int = 6,
    K: float = 1.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Fit theta3 envelope model to data in [kmin, kmax] range.

    Args:
        k: Index array
        psd_obs: Observed PSD values
        kmin: Minimum k for fit window
        kmax: Maximum k for fit window
        M: Truncation order
        K: Period parameter

    Returns:
        popt: Optimal parameters [baseline, A, k0, a]
        pcov: Covariance matrix

    Raises:
        RuntimeError: If fit fails
    """
    # Filter to fit window
    mask = (k >= kmin) & (k <= kmax)
    k_fit = k[mask]
    psd_fit = psd_obs[mask]

    if len(k_fit) < 4:
        raise ValueError(
            f"Insufficient data points in range [{kmin}, {kmax}]: {len(k_fit)}"
        )

    # Initial guess
    k0_guess = (kmin + kmax) / 2
    baseline_guess = np.percentile(psd_fit, 10)
    A_guess = (np.max(psd_fit) - baseline_guess) / (2 * M + 1)  # Normalize by sum
    a_guess = 0.1

    p0 = [baseline_guess, A_guess, k0_guess, a_guess]

    def model(k_val, baseline, A, k0, a):
        return theta3_envelope(k_val, baseline, A, k0, a, M=M, K=K)

    try:
        popt, pcov = curve_fit(
            model,
            k_fit,
            psd_fit,
            p0=p0,
            bounds=(
                [0, 0, kmin, 0.001],
                [np.inf, np.inf, kmax, 10.0],
            ),
            maxfev=10000,
        )
        return popt, pcov

    except Exception as e:
        raise RuntimeError(f"Theta3 fit failed: {e}") from e


def bootstrap_uncertainty(
    k: np.ndarray,
    psd_obs: np.ndarray,
    kmin: int,
    kmax: int,
    model_name: str,
    n_bootstrap: int = 200,
    seed: int = 0,
    **fit_kwargs,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Estimate parameter uncertainties via bootstrap resampling.

    Args:
        k: Index array
        psd_obs: Observed PSD values
        kmin: Minimum k for fit window
        kmax: Maximum k for fit window
        model_name: 'gauss_envelope' or 'theta3_envelope'
        n_bootstrap: Number of bootstrap resamples
        seed: Random seed for reproducibility
        fit_kwargs: Additional arguments for fit function

    Returns:
        param_means: Mean parameter values
        param_stds: Standard deviations of parameters
    """
    rng = np.random.default_rng(seed)

    # Filter to fit window
    mask = (k >= kmin) & (k <= kmax)
    k_fit = k[mask]
    psd_fit = psd_obs[mask]
    n_points = len(k_fit)

    if n_points < 4:
        raise ValueError(f"Insufficient data for bootstrap: {n_points} points")

    # Storage for bootstrap parameters
    boot_params = []

    for _ in range(n_bootstrap):
        # Resample with replacement
        indices = rng.choice(n_points, size=n_points, replace=True)
        k_boot = k_fit[indices]
        psd_boot = psd_fit[indices]

        try:
            if model_name == "gauss_envelope":
                popt, _ = fit_gauss_envelope(k_boot, psd_boot, kmin, kmax, **fit_kwargs)
            elif model_name == "theta3_envelope":
                popt, _ = fit_theta3_envelope(
                    k_boot, psd_boot, kmin, kmax, **fit_kwargs
                )
            else:
                raise ValueError(f"Unknown model: {model_name}")

            boot_params.append(popt)

        except Exception:
            # Skip failed fits
            continue

    if len(boot_params) < n_bootstrap / 2:
        print(
            f"Warning: Only {len(boot_params)}/{n_bootstrap} bootstrap fits succeeded",
            file=sys.stderr,
        )

    boot_params = np.array(boot_params)

    if len(boot_params) == 0:
        raise RuntimeError("All bootstrap fits failed")

    param_means = np.mean(boot_params, axis=0)
    param_stds = np.std(boot_params, axis=0)

    return param_means, param_stds


def compute_derived_params(
    model_name: str, popt: np.ndarray, perr: np.ndarray
) -> Dict[str, Any]:
    """
    Compute derived parameters (tau_hat, sigma, a) from fit parameters.

    Args:
        model_name: 'gauss_envelope' or 'theta3_envelope'
        popt: Optimal parameters
        perr: Parameter uncertainties

    Returns:
        Dictionary with derived parameters and their uncertainties
    """
    derived = {}

    if model_name == "gauss_envelope":
        # popt = [baseline, A, k0, sigma, ...]
        sigma = popt[3]
        sigma_err = perr[3]

        # tau_hat = 1 / (2 * sigma^2) - dimensionless dispersion proxy
        tau_hat = 1.0 / (2 * sigma**2)

        # Uncertainty propagation: d(tau_hat)/d(sigma) = -1/(sigma^3)
        tau_hat_err = abs(sigma_err / (sigma**3))

        derived["sigma"] = float(sigma)
        derived["sigma_uncertainty"] = float(sigma_err)
        derived["tau_hat"] = float(tau_hat)
        derived["tau_hat_uncertainty"] = float(tau_hat_err)

    elif model_name == "theta3_envelope":
        # popt = [baseline, A, k0, a]
        a = popt[3]
        a_err = perr[3]

        # tau_eff = a / (4π^2) - dimensionless effective tau
        tau_eff = a / (4 * np.pi**2)
        tau_eff_err = a_err / (4 * np.pi**2)

        derived["a"] = float(a)
        derived["a_uncertainty"] = float(a_err)
        derived["tau_eff"] = float(tau_eff)
        derived["tau_eff_uncertainty"] = float(tau_eff_err)

    return derived


def compute_goodness_of_fit(
    psd_obs: np.ndarray,
    psd_fit: np.ndarray,
    mask: np.ndarray,
) -> Dict[str, float]:
    """
    Compute goodness-of-fit statistics.

    Args:
        psd_obs: Observed PSD values
        psd_fit: Fitted PSD values
        mask: Boolean mask for fit window

    Returns:
        Dictionary with RMSE, R^2, and residual statistics
    """
    residuals = psd_obs[mask] - psd_fit[mask]

    rmse = float(np.sqrt(np.mean(residuals**2)))

    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((psd_obs[mask] - np.mean(psd_obs[mask])) ** 2)
    r2 = float(1 - ss_res / ss_tot if ss_tot > 0 else 0)

    return {
        "rmse": rmse,
        "r2": r2,
        "residual_mean": float(np.mean(residuals)),
        "residual_std": float(np.std(residuals)),
        "residual_max_abs": float(np.max(np.abs(residuals))),
    }


def save_outputs(
    csv_path: Path,
    kmin: int,
    kmax: int,
    model_name: str,
    popt: np.ndarray,
    perr: np.ndarray,
    derived: Dict[str, Any],
    goodness: Dict[str, float],
    k: np.ndarray,
    psd_obs: np.ndarray,
    psd_fit: np.ndarray,
    out_json: Path,
    out_csv: Path,
    spike_ks: Optional[List[int]] = None,
) -> None:
    """
    Save JSON and CSV outputs.

    Args:
        csv_path: Input CSV path
        kmin: Minimum k
        kmax: Maximum k
        model_name: Model name
        popt: Optimal parameters
        perr: Parameter uncertainties
        derived: Derived parameters
        goodness: Goodness-of-fit statistics
        k: Full k array
        psd_obs: Full observed PSD
        psd_fit: Full fitted PSD
        out_json: Output JSON path
        out_csv: Output CSV path
        spike_ks: Spike k values (optional)
    """
    # Build parameter dictionary
    if model_name == "gauss_envelope":
        param_names = ["baseline", "A", "k0", "sigma"]
        if spike_ks:
            param_names += [f"spike_{sk}" for sk in spike_ks]
    elif model_name == "theta3_envelope":
        param_names = ["baseline", "A", "k0", "a"]
    else:
        param_names = [f"param_{i}" for i in range(len(popt))]

    best_fit_params = {name: float(val) for name, val in zip(param_names, popt)}
    param_uncertainties = {name: float(err) for name, err in zip(param_names, perr)}

    # Build JSON output
    json_output = {
        "csv": str(csv_path),
        "kmin": int(kmin),
        "kmax": int(kmax),
        "model": model_name,
        "best_fit_params": best_fit_params,
        "param_uncertainties": param_uncertainties,
        "derived": derived,
        "goodness": goodness,
    }

    if spike_ks:
        json_output["spike_ks"] = spike_ks

    # Save JSON
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with open(out_json, "w") as f:
        json.dump(json_output, f, indent=2)

    print(f"Saved JSON output to {out_json}")

    # Build CSV output
    residuals = psd_obs - psd_fit

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with open(out_csv, "w") as f:
        f.write("k,psd_obs,psd_fit,residual\n")
        for k_val, obs, fit, res in zip(k, psd_obs, psd_fit, residuals):
            f.write(f"{k_val},{obs},{fit},{res}\n")

    print(f"Saved CSV output to {out_csv}")


def plot_fit(
    k: np.ndarray,
    psd_obs: np.ndarray,
    psd_fit: np.ndarray,
    kmin: int,
    kmax: int,
    model_name: str,
    derived: Dict[str, Any],
    out_png: Path,
) -> None:
    """
    Generate and save fit plot.

    Args:
        k: Index array
        psd_obs: Observed PSD values
        psd_fit: Fitted PSD values
        kmin: Minimum k for fit window
        kmax: Maximum k for fit window
        model_name: Model name
        derived: Derived parameters
        out_png: Output PNG path
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Top panel: data and fit
    ax1.plot(k, psd_obs, "o", label="Observed", markersize=4, alpha=0.6)
    ax1.plot(k, psd_fit, "-", label="Fit", linewidth=2)
    ax1.axvline(kmin, color="gray", linestyle="--", alpha=0.5)
    ax1.axvline(kmax, color="gray", linestyle="--", alpha=0.5)
    ax1.set_ylabel("PSD")
    ax1.legend()
    ax1.grid(alpha=0.3)

    # Add derived parameter text
    if model_name == "gauss_envelope":
        text = f"σ = {derived['sigma']:.2f} ± {derived['sigma_uncertainty']:.2f}\n"
        text += f"τ̂ = {derived['tau_hat']:.4f} ± {derived['tau_hat_uncertainty']:.4f}"
    elif model_name == "theta3_envelope":
        text = f"a = {derived['a']:.3f} ± {derived['a_uncertainty']:.3f}\n"
        text += (
            f"τ_eff = {derived['tau_eff']:.4f} ± {derived['tau_eff_uncertainty']:.4f}"
        )
    else:
        text = ""

    ax1.text(
        0.02,
        0.98,
        text,
        transform=ax1.transAxes,
        verticalalignment="top",
        fontfamily="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
    )

    # Bottom panel: residuals
    residuals = psd_obs - psd_fit
    ax2.plot(k, residuals, "o", markersize=4, alpha=0.6)
    ax2.axhline(0, color="black", linestyle="-", linewidth=0.5)
    ax2.axvline(kmin, color="gray", linestyle="--", alpha=0.5)
    ax2.axvline(kmax, color="gray", linestyle="--", alpha=0.5)
    ax2.set_xlabel("k")
    ax2.set_ylabel("Residual")
    ax2.grid(alpha=0.3)

    plt.tight_layout()

    out_png.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_png, dpi=150)
    plt.close()

    print(f"Saved plot to {out_png}")


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="Fit cluster width in scan CSV to estimate tau_hat parameter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Gaussian fit with default range
  python -m forensic_fingerprint.tools.theta_fit_tau \\
      --csv scans/tt_scan_int_100_200.csv \\
      --out_json results/tau_gauss.json
  
  # Theta3 fit with custom range
  python -m forensic_fingerprint.tools.theta_fit_tau \\
      --csv scans/tt_scan_int_100_200.csv \\
      --kmin 134 --kmax 143 \\
      --model theta3_envelope \\
      --out_json results/tau_theta3.json

  # With spike terms at primes 137 and 139
  python -m forensic_fingerprint.tools.theta_fit_tau \\
      --csv scans/tt_scan_int_100_200.csv \\
      --include_spikes \\
      --spike_ks 137,139 \\
      --plot_png results/tau_spikes.png
""",
    )

    parser.add_argument(
        "--csv",
        type=Path,
        required=True,
        help="Path to input CSV file (must contain 'n' or 'raw' and 'psd_obs' columns)",
    )
    parser.add_argument(
        "--kmin",
        type=int,
        default=130,
        help="Minimum k value for fit window (default: 130)",
    )
    parser.add_argument(
        "--kmax",
        type=int,
        default=150,
        help="Maximum k value for fit window (default: 150)",
    )
    parser.add_argument(
        "--model",
        type=str,
        choices=["gauss_envelope", "theta3_envelope"],
        default="gauss_envelope",
        help="Model to fit (default: gauss_envelope)",
    )
    parser.add_argument(
        "--include_spikes",
        action="store_true",
        help="Include discrete spike terms at specified k values",
    )
    parser.add_argument(
        "--spike_ks",
        type=str,
        default="137,139",
        help="Comma-separated list of k values for spikes (default: 137,139)",
    )
    parser.add_argument(
        "--out_json",
        type=Path,
        default=Path("scans/tau_fit_result.json"),
        help="Output JSON path (default: scans/tau_fit_result.json)",
    )
    parser.add_argument(
        "--out_csv",
        type=Path,
        default=Path("scans/tau_fit_result.csv"),
        help="Output CSV path (default: scans/tau_fit_result.csv)",
    )
    parser.add_argument(
        "--plot_png",
        type=Path,
        default=None,
        help="Output PNG plot path (optional)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed for bootstrap (default: 0)",
    )
    parser.add_argument(
        "--n_bootstrap",
        type=int,
        default=200,
        help="Number of bootstrap resamples (default: 200)",
    )

    args = parser.parse_args()

    # Validate inputs
    if not args.csv.exists():
        print(f"Error: CSV file not found: {args.csv}", file=sys.stderr)
        sys.exit(1)

    if args.kmin >= args.kmax:
        print(
            f"Error: kmin ({args.kmin}) must be less than kmax ({args.kmax})",
            file=sys.stderr,
        )
        sys.exit(1)

    # Parse spike_ks
    spike_ks = None
    if args.include_spikes:
        try:
            spike_ks = [int(x.strip()) for x in args.spike_ks.split(",")]
        except ValueError:
            print(f"Error: Invalid spike_ks format: {args.spike_ks}", file=sys.stderr)
            sys.exit(1)

    # Load data
    print(f"Loading CSV: {args.csv}")
    try:
        k, psd_obs = load_csv(args.csv)
        print(f"Loaded {len(k)} data points, k range: [{k.min()}, {k.max()}]")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Perform fit
    print(f"Fitting {args.model} model in range [{args.kmin}, {args.kmax}]...")

    try:
        if args.model == "gauss_envelope":
            popt, pcov = fit_gauss_envelope(
                k,
                psd_obs,
                args.kmin,
                args.kmax,
                include_spikes=args.include_spikes,
                spike_ks=spike_ks,
            )
        elif args.model == "theta3_envelope":
            popt, pcov = fit_theta3_envelope(k, psd_obs, args.kmin, args.kmax)
        else:
            print(f"Error: Unknown model: {args.model}", file=sys.stderr)
            sys.exit(1)

        # Get parameter uncertainties from covariance
        perr = np.sqrt(np.diag(pcov))

        print("Fit successful!")
        print(f"Parameters: {popt}")
        print(f"Uncertainties: {perr}")

    except (ValueError, RuntimeError) as e:
        print(f"Error during fit: {e}", file=sys.stderr)
        sys.exit(1)

    # Bootstrap uncertainties
    print(f"Computing bootstrap uncertainties ({args.n_bootstrap} resamples)...")
    try:
        fit_kwargs = {}
        if args.model == "gauss_envelope" and args.include_spikes:
            fit_kwargs["include_spikes"] = True
            fit_kwargs["spike_ks"] = spike_ks

        boot_means, boot_stds = bootstrap_uncertainty(
            k,
            psd_obs,
            args.kmin,
            args.kmax,
            args.model,
            n_bootstrap=args.n_bootstrap,
            seed=args.seed,
            **fit_kwargs,
        )

        # Use bootstrap uncertainties if larger (more conservative)
        perr = np.maximum(perr, boot_stds)

        print("Bootstrap complete!")

    except (ValueError, RuntimeError) as e:
        print(f"Warning: Bootstrap failed: {e}", file=sys.stderr)
        print("Using covariance-based uncertainties only")

    # Compute derived parameters
    derived = compute_derived_params(args.model, popt, perr)

    print("\nDerived parameters:")
    for key, value in derived.items():
        print(f"  {key}: {value}")

    # Generate full fitted curve
    if args.model == "gauss_envelope":
        if args.include_spikes and spike_ks:
            psd_fit = gauss_envelope_with_spikes(
                k, popt[0], popt[1], popt[2], popt[3], spike_ks, list(popt[4:])
            )
        else:
            psd_fit = gauss_envelope(k, popt[0], popt[1], popt[2], popt[3])
    elif args.model == "theta3_envelope":
        psd_fit = theta3_envelope(k, popt[0], popt[1], popt[2], popt[3])

    # Compute goodness of fit
    mask = (k >= args.kmin) & (k <= args.kmax)
    goodness = compute_goodness_of_fit(psd_obs, psd_fit, mask)

    print("\nGoodness of fit:")
    print(f"  RMSE: {goodness['rmse']:.4f}")
    print(f"  R^2: {goodness['r2']:.4f}")

    # Save outputs
    save_outputs(
        args.csv,
        args.kmin,
        args.kmax,
        args.model,
        popt,
        perr,
        derived,
        goodness,
        k,
        psd_obs,
        psd_fit,
        args.out_json,
        args.out_csv,
        spike_ks=spike_ks,
    )

    # Generate plot if requested
    if args.plot_png:
        print("\nGenerating plot...")
        plot_fit(
            k,
            psd_obs,
            psd_fit,
            args.kmin,
            args.kmax,
            args.model,
            derived,
            args.plot_png,
        )

    print("\n✓ All outputs generated successfully")


if __name__ == "__main__":
    main()
