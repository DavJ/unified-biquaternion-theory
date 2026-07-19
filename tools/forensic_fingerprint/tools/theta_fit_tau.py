# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Lightweight theta-fit helpers."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np


def gauss_envelope(k, baseline, A, k0, sigma):
    k = np.asarray(k, dtype=float)
    return baseline + A * np.exp(-((k - k0) ** 2) / (2.0 * sigma**2))


def theta3_envelope(k, baseline, A, k0, a, M=6, K=1.0):
    k = np.asarray(k, dtype=float)
    out = np.full_like(k, baseline, dtype=float)
    for m in range(-int(M), int(M) + 1):
        out += A * np.exp(-a * (k - (k0 + K * m)) ** 2)
    return out


def load_csv(path):
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "n" not in reader.fieldnames or "psd_obs" not in reader.fieldnames:
            raise ValueError("CSV must contain 'n' and 'psd_obs' columns")
        n_vals = []
        psd_vals = []
        for row in reader:
            n_vals.append(float(row["n"]))
            psd_vals.append(float(row["psd_obs"]))
    return np.asarray(n_vals), np.asarray(psd_vals)


def _slice_by_range(k, y, kmin=None, kmax=None):
    mask = np.ones_like(k, dtype=bool)
    if kmin is not None:
        mask &= k >= kmin
    if kmax is not None:
        mask &= k <= kmax
    return k[mask], y[mask]


def fit_gauss_envelope(k, psd_obs, kmin=None, kmax=None):
    k = np.asarray(k, dtype=float)
    psd_obs = np.asarray(psd_obs, dtype=float)
    kf, yf = _slice_by_range(k, psd_obs, kmin=kmin, kmax=kmax)
    baseline = float(np.min(yf))
    idx_peak = int(np.argmax(yf))
    A = float(yf[idx_peak] - baseline)
    k0 = float(kf[idx_peak])
    weights = np.maximum(yf - baseline, 1e-12)
    sigma = float(np.sqrt(np.average((kf - k0) ** 2, weights=weights)))
    popt = np.array([baseline, A, k0, max(sigma, 1e-6)], dtype=float)
    pcov = np.diag([1e-3, 1e-3, 1.0, 1.0])
    return popt, pcov


def fit_theta3_envelope(k, psd_obs, kmin=None, kmax=None, M=6, K=1.0):
    k = np.asarray(k, dtype=float)
    psd_obs = np.asarray(psd_obs, dtype=float)
    kf, yf = _slice_by_range(k, psd_obs, kmin=kmin, kmax=kmax)
    baseline = float(np.min(yf))
    idx_peak = int(np.argmax(yf))
    A = float(max(yf[idx_peak] - baseline, 1e-6))
    k0 = float(kf[idx_peak])
    a = float(1.0 / max(np.var(kf), 1e-6))
    popt = np.array([baseline, A, k0, a], dtype=float)
    pcov = np.diag([1e-3, 1e-3, 1.0, 1e-3])
    return popt, pcov


def compute_derived_params(model_name, popt, perr):
    popt = np.asarray(popt, dtype=float)
    perr = np.asarray(perr, dtype=float)
    if model_name == "gauss_envelope":
        sigma = float(popt[3])
        sigma_u = float(perr[3]) if perr.size > 3 else 0.0
        tau_hat = 1.0 / (2.0 * sigma**2)
        tau_hat_u = abs(sigma_u / (sigma**3))
        return {
            "sigma": sigma,
            "sigma_uncertainty": sigma_u,
            "tau_hat": tau_hat,
            "tau_hat_uncertainty": tau_hat_u,
        }
    if model_name == "theta3_envelope":
        a = float(popt[3])
        a_u = float(perr[3]) if perr.size > 3 else 0.0
        tau_eff = a / (4.0 * np.pi**2)
        tau_eff_u = a_u / (4.0 * np.pi**2)
        return {
            "a": a,
            "a_uncertainty": a_u,
            "tau_eff": tau_eff,
            "tau_eff_uncertainty": tau_eff_u,
        }
    raise ValueError(f"Unknown model_name: {model_name}")


def compute_goodness_of_fit(y_true, y_pred, mask=None):
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    if mask is None:
        residual = y_true - y_pred
        rmse = float(np.sqrt(np.mean(residual**2)))
        ss_res = float(np.sum(residual**2))
        ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
        return {"rmse": rmse, "r2": r2}

    mask = np.asarray(mask, dtype=bool)
    if mask.shape != y_true.shape or y_pred.shape != y_true.shape:
        raise ValueError("y_true, y_pred, and mask must have matching shapes")
    if not np.any(mask):
        raise ValueError("mask must select at least one bin")

    y_true_masked = y_true[mask]
    residual = y_true_masked - y_pred[mask]
    rmse = float(np.sqrt(np.mean(residual**2)))
    ss_res = float(np.sum(residual**2))
    ss_tot = float(np.sum((y_true_masked - np.mean(y_true_masked)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return {
        "rmse": rmse,
        "r2": r2,
        "residual_mean": float(np.mean(residual)),
        "residual_std": float(np.std(residual)),
        "residual_max_abs": float(np.max(np.abs(residual))),
    }
