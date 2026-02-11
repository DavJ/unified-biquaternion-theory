#!/usr/bin/env python3
"""
cmb_fft2d_scan.py

Global 2D FFT of a CMB sky map after projecting HEALPix to an equirectangular (lon/lat) grid.

Goal: test for spatial-frequency "spikes" at k≈137,139 (or any k) in 2D Fourier domain,
using targets expressed in *cycles per full map extent* (NOT inverse periods).

Why this tool exists
- Your earlier 1D "phase-stream FFT" depends on a particular serialization of (ℓ,m) and on window leakage.
- This tool works directly on a 2D raster of the sky (lon/lat), so k is an honest spatial frequency on the raster.
- It supports radial averaging (|k|) and optional simple null Monte Carlo.

Notes / Caveats
- Equirectangular projection distorts areas near the poles; if you want to minimize this, you can:
  (a) analyze only an equatorial band via --lat-cut, or
  (b) later switch to an equal-area projection (Mollweide) and resample to a uniform grid.
- For EE/BB, we compute E/B on a degraded nside_out (recommended) before projecting.
- "k" here is FFT bin index in cycles per full width/height (integer-ish). For a grid (Ny,Nx),
  Nyquist requires Nx >= 2*k_max and Ny >= 2*k_max to resolve k_max without aliasing.

Example
MPLBACKEND=Agg python -m forensic_fingerprint.tools.cmb_fft2d_scan \
  --q-map data/...Q...fits --u-map data/...U...fits \
  --channels BB --nside-out 256 --nlat 512 --nlon 1024 \
  --window2d hann --targets 137,139 --radial \
  --mc 2000 --null phi-roll --seed 0 \
  --report-csv scans/bb_fft2d.csv --plot-png scans/bb_fft2d.png
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import healpy as hp


# -------------------------
# Small helpers
# -------------------------

def _parse_list_csv(s: str) -> List[str]:
    return [x.strip() for x in (s or "").split(",") if x.strip()]

def _parse_ints_csv(s: str) -> List[int]:
    return [int(tok) for tok in _parse_list_csv(s)]

def _ensure_dir_for(path: Optional[str]) -> None:
    if not path:
        return
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)


def _write_radial_dump_csv(
    path: str,
    channel: str,
    meta: Dict[str, Any],
    obs_spec: np.ndarray,
    mc_mean: Optional[np.ndarray] = None,
    mc_std: Optional[np.ndarray] = None,
    z: Optional[np.ndarray] = None,
    p_tail: Optional[np.ndarray] = None,
) -> None:
    """Write full radial spectrum (and optional MC summary stats) to CSV."""
    _ensure_dir_for(path)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "channel","nside_out","nlat","nlon","lat_cut_deg","field","window2d","radial","null","mc","seed",
            "k","obs_psd","mc_mean","mc_std","z","p_tail"
        ])
        kmax_eff = len(obs_spec) - 1
        for k in range(kmax_eff + 1):
            w.writerow([
                channel,
                meta["nside_out"], meta["nlat"], meta["nlon"], meta["lat_cut_deg"],
                meta["field"], meta["window2d"], meta["radial"], meta["null"], meta["mc"], meta["seed"],
                k,
                float(obs_spec[k]) if k < len(obs_spec) else float("nan"),
                float(mc_mean[k]) if mc_mean is not None and k < len(mc_mean) else float("nan"),
                float(mc_std[k]) if mc_std is not None and k < len(mc_std) else float("nan"),
                float(z[k]) if z is not None and k < len(z) else float("nan"),
                float(p_tail[k]) if p_tail is not None and k < len(p_tail) else float("nan"),
            ])


def _map2alm_spin_compat(qu_maps, spin: int, lmax: int):
    # Healpy signature differences across versions; try a few combos.
    attempts = [
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax),
    ]
    for fn in attempts:
        try:
            return fn()
        except TypeError:
            continue
    return hp.map2alm_spin(qu_maps, spin, lmax)

def _nside_of_map(m: np.ndarray) -> int:
    return hp.get_nside(m)

def _ud_grade(m: np.ndarray, nside_out: int) -> np.ndarray:
    nside_in = _nside_of_map(m)
    if nside_out == nside_in:
        return m
    return hp.ud_grade(m, nside_out, order_in="RING", order_out="RING", power=0)

def _window_1d(name: str, n: int) -> np.ndarray:
    name = (name or "none").lower()
    if name in ("none", "rect", "boxcar"):
        return np.ones(n, dtype=float)
    if name in ("hann", "hanning"):
        return np.hanning(n).astype(float)
    if name == "hamming":
        return np.hamming(n).astype(float)
    if name == "blackman":
        return np.blackman(n).astype(float)
    raise ValueError(f"Unknown window: {name}")

def _window_2d(name: str, ny: int, nx: int, normalize_rms: bool = True) -> np.ndarray:
    wy = _window_1d(name, ny)
    wx = _window_1d(name, nx)
    w = wy[:, None] * wx[None, :]
    if normalize_rms:
        rms = math.sqrt(float(np.mean(w**2)))
        if rms > 0:
            w = w / rms
    return w

def _project_to_equirect(m: np.ndarray, nlat: int, nlon: int, lat_cut_deg: float = 0.0, projection: str = "lonlat") -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Sample a HEALPix map onto an (nlat, nlon) grid.

    projection:
      - "lonlat": uniform in theta (equirectangular in lat)
      - "cyl-ea": cylindrical equal-area (uniform in mu=cos(theta)=sin(lat))
      - "torus": same sampling as lonlat/cyl-ea, but caller may post-process to enforce 2D periodicity in both axes.
    """
    projection = (projection or "lonlat").lower()

    # Grid centers: avoid exact poles to reduce interpolation quirks
    if projection == "cyl-ea":
        # uniform in mu=cos(theta) gives equal-area rings in latitude
        mu = 1.0 - (np.arange(nlat) + 0.5) * (2.0 / nlat)  # ~[+1 .. -1]
        mu = np.clip(mu, -1.0, 1.0)
        theta = np.arccos(mu)  # 0..pi
    else:
        theta = (np.arange(nlat) + 0.5) * (np.pi / nlat)  # 0..pi

    phi = (np.arange(nlon) + 0.5) * (2.0 * np.pi / nlon)  # 0..2pi

    # Optional latitude cut: keep only |lat| <= lat_cut
    if lat_cut_deg and lat_cut_deg > 0:
        lat = 0.5 * np.pi - theta  # radians
        keep = np.abs(lat) <= np.deg2rad(lat_cut_deg)
        theta_use = theta[keep]
    else:
        keep = None
        theta_use = theta

    # Sample using healpy interpolation
    th2, ph2 = np.meshgrid(theta_use, phi, indexing="ij")
    img = hp.get_interp_val(m, th2, ph2).astype(np.float64)

    if keep is None:
        return img, theta, phi
    return img, theta_use, phi

def _torusify_lat(img: np.ndarray) -> np.ndarray:
    """Make latitude axis periodic by mirroring (sphere -> cylinder -> torus trick)."""
    return np.vstack([img, img[::-1, :]])



def _fft2_psd(img: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    2D FFT-based power spectral density (PSD).
    Uses rfft2 for x (longitude) to save space.
    Returns: psd, ky, kx
      psd: (ny, nx_r) where nx_r = nx//2+1
      ky: cycles per full height (can be negative)
      kx: cycles per full width (non-negative)
    """
    ny, nx = img.shape
    F = np.fft.rfft2(img)
    psd = (np.abs(F) ** 2) / float(nx * ny)
    ky = np.fft.fftfreq(ny) * ny
    kx = np.fft.rfftfreq(nx) * nx
    return psd, ky, kx

def _radial_average(psd: np.ndarray, ky: np.ndarray, kx: np.ndarray, kmax: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Radially average psd over integer |k| shells:
      k = sqrt(kx^2 + ky^2)
    Returns:
      k_bins (int), psd_mean
    """
    ny, nxr = psd.shape
    KX, KY = np.meshgrid(kx, ky, indexing="xy")
    KR = np.sqrt(KX**2 + KY**2)

    if kmax is None:
        kmax = int(np.floor(np.max(KR)))

    # Bin by nearest integer
    idx = np.rint(KR).astype(int)
    idx = np.clip(idx, 0, kmax)

    sums = np.bincount(idx.ravel(), weights=psd.ravel(), minlength=kmax+1)
    cnts = np.bincount(idx.ravel(), minlength=kmax+1)
    with np.errstate(invalid="ignore", divide="ignore"):
        mean = sums / np.maximum(cnts, 1)
    k_bins = np.arange(kmax+1)
    return k_bins, mean

def _null_phi_roll(img: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """
    Null by randomly rolling each latitude row by a random longitude shift.
    Preserves per-row amplitude distribution while scrambling coherent structures in phi.
    """
    ny, nx = img.shape
    out = np.empty_like(img)
    shifts = rng.integers(0, nx, size=ny)
    for i in range(ny):
        out[i] = np.roll(img[i], int(shifts[i]))
    return out

def _null_pixel_shuffle(img: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    flat = img.ravel().copy()
    rng.shuffle(flat)
    return flat.reshape(img.shape)


@dataclass(frozen=True)
class Target:
    k: int  # target radial k (cycles per full map)


def _parse_pair_int(s: str) -> Optional[Tuple[int,int]]:
    s = (s or "").strip()
    if not s:
        return None
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 2:
        raise ValueError(f"Expected 'A,B' got: {s!r}")
    return int(parts[0]), int(parts[1])

def _welch_targets(img: np.ndarray,
                   targets: Sequence[Target],
                   window2d: str,
                   radial: bool,
                   wx: int, wy: int,
                   sx: int, sy: int) -> Dict[int, float]:
    """Welch-style averaged spectrum using sliding windows with trojčlenka scaling."""
    nlat, nlon = img.shape
    kmax = int(math.floor(math.sqrt((nlon//2)**2 + (nlat//2)**2)))
    acc = np.zeros(kmax + 1, dtype=float) if radial else np.zeros(nlon//2 + 1, dtype=float)
    cnt = np.zeros_like(acc)

    w2 = _window_2d(window2d, wy, wx, normalize_rms=True)

    ky = np.fft.fftfreq(wy)
    kx = np.fft.fftfreq(wx)
    ky_idx = np.where(ky >= 0)[0]
    kx_idx = np.where(kx >= 0)[0]

    for y0 in range(0, nlat - wy + 1, sy):
        for x0 in range(0, nlon - wx + 1, sx):
            patch = img[y0:y0+wy, x0:x0+wx]
            patch = patch - float(np.mean(patch))
            pw = patch * w2
            P, _, _ = _fft2_psd(pw)

            for iy in ky_idx:
                jy = int(round(abs(ky[iy]) * wy))
                kyg = int(round(jy * (nlat / wy)))
                if kyg > nlat//2:
                    continue
                for ix in kx_idx:
                    jx = int(round(abs(kx[ix]) * wx))
                    kxg = int(round(jx * (nlon / wx)))
                    if kxg > nlon//2:
                        continue
                    val = float(P[iy, ix])
                    if radial:
                        # Robust radial binning:
                        # The previous implementation used a hard integer bin via round(|k|).
                        # For some (grid, window) combinations this can leave certain integer
                        # radii completely empty (cnt==0), producing NaNs for those targets.
                        # Distribute power linearly between the two nearest integer bins.
                        kgf = math.sqrt(kxg * kxg + kyg * kyg)
                        kg0 = int(math.floor(kgf))
                        kg1 = kg0 + 1
                        w1 = kgf - kg0
                        w0 = 1.0 - w1

                        if 0 <= kg0 <= kmax:
                            acc[kg0] += w0 * val
                            cnt[kg0] += w0
                        if 0 <= kg1 <= kmax:
                            acc[kg1] += w1 * val
                            cnt[kg1] += w1
                    else:
                        if kyg == 0:
                            acc[kxg] += val
                            cnt[kxg] += 1

    # Avoid RuntimeWarning: np.where evaluates both branches eagerly.
    # Use np.divide with a mask so division is only performed where cnt>0.
    spec = np.full_like(acc, np.nan, dtype=float)
    np.divide(acc, cnt, out=spec, where=cnt > 0)
    out: Dict[int, float] = {}
    for t in targets:
        out[t.k] = float(spec[t.k]) if 0 <= t.k < len(spec) else float("nan")
    return out

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tt-map", help="HEALPix FITS containing IQU or temperature in field 0")
    ap.add_argument("--q-map", help="HEALPix FITS Q map (single field)")
    ap.add_argument("--u-map", help="HEALPix FITS U map (single field)")

    ap.add_argument("--channels", default="TT", help="Comma-separated: TT,EE,BB,Q,U")
    ap.add_argument("--lmax-alm", type=int, default=512, help="lmax used for E/B reconstruction")
    ap.add_argument("--nside-out", type=int, default=256, help="Degrade maps to this NSIDE before projection/FFT")
    ap.add_argument("--nlat", type=int, default=512, help="Equirectangular grid height (latitude samples)")
    ap.add_argument("--nlon", type=int, default=1024, help="Equirectangular grid width (longitude samples)")
    ap.add_argument("--projection", choices=["latlon", "torus"], default="latlon",
                    help="Projection for full-sky map to 2D grid. 'torus' uses equal-area v=sin(lat) mapping.")
    ap.add_argument("--window-size", default="", help="Optional sliding window size Wx,Wy (enables Welch averaged spectrum with trojclenka scaling).")
    ap.add_argument("--stride", default="", help="Stride Sx,Sy for sliding window (default: Wx//2,Wy//2).")

    ap.add_argument("--lat-cut", type=float, default=0.0, help="If >0, keep only |lat|<=lat_cut (deg) to reduce polar distortion")

    ap.add_argument("--field", choices=["value", "phase"], default="value",
                    help="Analyze scalar values or phases (phase = exp(i*angle)).")
    ap.add_argument("--window2d", default="hann", help="2D window: none|hann|hamming|blackman")

    ap.add_argument("--targets", default="137,139", help="Comma-separated target k (cycles per full map), e.g. 137,139")
    ap.add_argument("--radial", action="store_true", help="Use radial average |k| for targets (recommended)")

    ap.add_argument("--mc", type=int, default=0, help="Monte Carlo null samples")
    ap.add_argument("--null", choices=["phi-roll", "pixel-shuffle"], default="phi-roll")
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--report-csv", help="Write per-target results to CSV")
    ap.add_argument("--plot-png", help="Write diagnostic plot PNG (requires matplotlib)")
    ap.add_argument("--dump-radial-csv", default="", help="Write full radial spectrum to CSV (adds MC mean/std/Z/p_tail when --mc>0)")
    ap.add_argument("--kmax", type=int, default=None, help="Optional max k for --dump-radial-csv (speeds up MC)")

    args = ap.parse_args()

    ch_list = [c.upper() for c in _parse_list_csv(args.channels)]
    targets = [Target(k=int(k)) for k in _parse_ints_csv(args.targets)]
    if not targets:
        raise SystemExit("No --targets provided.")

    # Load / build channel maps on nside_out
    maps: Dict[str, np.ndarray] = {}

    if "TT" in ch_list:
        if not args.tt_map:
            raise SystemExit("--tt-map is required for TT")
        mT = hp.read_map(args.tt_map, field=0)  # no verbose kw to avoid deprecation warnings
        maps["TT"] = _ud_grade(mT, args.nside_out)

    need_qu = any(ch in ch_list for ch in ("Q", "U", "EE", "BB"))
    if need_qu:
        if not (args.q_map and args.u_map):
            raise SystemExit("--q-map and --u-map are required for Q/U/EE/BB")
        q = hp.read_map(args.q_map, field=0)
        u = hp.read_map(args.u_map, field=0)
        q = _ud_grade(q, args.nside_out)
        u = _ud_grade(u, args.nside_out)
        if "Q" in ch_list:
            maps["Q"] = q
        if "U" in ch_list:
            maps["U"] = u
        if ("EE" in ch_list) or ("BB" in ch_list):
            lmax = int(args.lmax_alm)
            almE, almB = _map2alm_spin_compat([q, u], 2, lmax)
            if "EE" in ch_list:
                maps["EE"] = hp.alm2map(almE, nside=args.nside_out, lmax=lmax, verbose=False)
            if "BB" in ch_list:
                maps["BB"] = hp.alm2map(almB, nside=args.nside_out, lmax=lmax, verbose=False)

    print(f"[cmb_fft2d_scan] channels={','.join(ch_list)} nside_out={args.nside_out} grid={args.nlat}x{args.nlon} field={args.field} window2d={args.window2d} targets={[t.k for t in targets]} radial={args.radial} mc={args.mc} null={args.null}")

    rng = np.random.default_rng(args.seed)

    # Prepare plotting
    have_mpl = False
    if args.plot_png:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt  # noqa
            have_mpl = True
        except Exception as e:
            print(f"[warn] matplotlib not available; skipping plot ({e})")
            have_mpl = False

    rows: List[Dict[str, object]] = []

    for ch in ch_list:
        if ch not in maps:
            print(f"[warn] channel {ch} not available (missing inputs); skipping")
            continue

        m = maps[ch]
        img, theta, phi = _project_to_equirect(m, args.nlat, args.nlon, lat_cut_deg=args.lat_cut, projection=args.projection)
        if (args.projection or 'lonlat').lower() == 'torus':
            # Enforce 2D periodicity in both axes by mirroring latitude.
            img = _torusify_lat(img)


        # Convert to "phase field" if requested.
        if args.field == "phase":
            # phase of real scalar: treat as complex on unit circle via sign as angle proxy
            # (For actual complex fields, you'd pass complex. Here we use angle of (x + i*0).)
            ang = np.angle(img.astype(np.complex128))
            img = np.exp(1j * ang)
            # For FFT, use complex; later psd uses |F|^2 anyway.
        else:
            img = img.astype(np.float64)

        # Remove mean to suppress DC spike.
        img = img - np.mean(img)
        nlat_eff, nlon_eff = img.shape
        # Window / spectrum
        wxwy = _parse_pair_int(args.window_size)
        wx = wy = sx = sy = None  # type: ignore
        obs_welch: Optional[Dict[int, float]] = None
        if wxwy:
            wx, wy = wxwy
            sxsy = _parse_pair_int(args.stride)
            if sxsy:
                sx, sy = sxsy
            else:
                sx, sy = max(1, wx // 2), max(1, wy // 2)
            obs_welch = _welch_targets(img, targets, args.window2d, args.radial, wx=wx, wy=wy, sx=sx, sy=sy)
            # also compute global PSD for visualization
            w2 = _window_2d(args.window2d, nlat_eff, nlon_eff, normalize_rms=True)
            imgw = img * w2
            psd, ky, kx = _fft2_psd(imgw)

        # --- ANNULUS 2D DIAGNOSTIC ---
        # Writes a 2D diagnostic map of power in an annulus |k| in [k1,k2].
        # This is in Fourier-space, not "center of the universe".
        if args.annulus_png and args.band_k:
            try:
                k1_s, k2_s = [x.strip() for x in args.band_k.split(",")]
                k1 = float(k1_s); k2 = float(k2_s)
                if not (k2 > k1 >= 0):
                    raise ValueError("band-k must satisfy 0 <= k1 < k2")
            except Exception as e:
                raise SystemExit(f"--band-k parse error (expected k1,k2): {e}")

            try:
                import matplotlib.pyplot as plt
            except Exception as e:
                raise SystemExit(f"matplotlib required for --annulus-png: {e}")

            # Build k-grid and annulus mask
            KX, KY = np.meshgrid(kx, ky)
            KR = np.sqrt(KX*KX + KY*KY)

            # Mask outside annulus; add epsilon for log
            eps = 1e-300
            band = (KR >= k1) & (KR <= k2)
            band_psd = np.where(band, psd, np.nan)

            # Use fftshift for nicer visualization (DC at center)
            band_psd_s = np.fft.fftshift(band_psd)
            band_log = np.log10(band_psd_s + eps)

            out_png = args.annulus_png
            if len(ch_list) > 1 and out_png:
                base, ext = os.path.splitext(out_png)
                out_png = f"{base}_{ch}{ext}"

            plt.figure(figsize=(7, 4.5))
            plt.imshow(band_log, origin="lower", aspect="auto")
            plt.title(f"Annulus power map ({ch}): |k| in [{k1:g}, {k2:g}]")
            plt.xlabel("kx (fftshifted index)")
            plt.ylabel("ky (fftshifted index)")
            plt.colorbar(label="log10(PSD)")
            _ensure_dir_for(out_png)
            plt.tight_layout()
            plt.savefig(out_png, dpi=150)
            plt.close()
            print(f"[info] wrote annulus PNG: {out_png}")

        else:
            w2 = _window_2d(args.window2d, nlat_eff, nlon_eff, normalize_rms=True)
            imgw = img * w2
            psd, ky, kx = _fft2_psd(imgw)


        # Build a spectrum for plotting (always global), but only use it for target-values
        # when Welch windowing is NOT enabled.
        if args.radial:
            k_bins, psd_r = _radial_average(psd, ky, kx)
            obs_global = {t.k: float(psd_r[t.k]) if t.k < len(psd_r) else float("nan") for t in targets}

        # FIRST FILTER: prepare full observed radial spectrum for dumping
        obs_spec = None
        if args.dump_radial_csv and args.radial:
            if args.kmax is not None and args.kmax >= 0 and args.kmax < len(psd_r) - 1:
                obs_spec = psd_r[: args.kmax + 1]
            else:
                obs_spec = psd_r

        # FIRST FILTER: MC summary arrays (mean/std/Z/p_tail) for full spectrum
        mc_mean = mc_std = z = p_tail = None
        mean = m2 = ge = None
        n_mc = 0
        if args.dump_radial_csv and args.radial and obs_spec is not None and args.mc and args.mc > 0:
            mean = np.zeros_like(obs_spec, dtype=float)
            m2 = np.zeros_like(obs_spec, dtype=float)
            ge = np.zeros_like(obs_spec, dtype=float)
        else:
            # Use axis-aligned (ky=0, kx=k) bins (positive kx only)
            ky0 = int(np.where(ky == 0)[0][0]) if np.any(ky == 0) else 0
            obs_global = {}
            for t in targets:
                k = t.k
                if 0 <= k < len(kx):
                    obs_global[k] = float(psd[ky0, k])
                else:
                    obs_global[k] = float("nan")

        obs = obs_welch if obs_welch is not None else obs_global

        print(f"\n[{ch}] obs targets:")
        for t in targets:
            print(f"  k={t.k}: PSD={obs[t.k]:.6g}")

        # Monte Carlo p-values
        p_mc: Dict[int, float] = {t.k: float("nan") for t in targets}
        if args.mc > 0:
            mc_vals = {t.k: [] for t in targets}
            for i in range(1, args.mc + 1):
                if i % 100 == 0 or (args.mc <= 2000 and i % 50 == 0):
                    print(f"[mc] {i}/{args.mc}")

                if args.null == "phi-roll":
                    img_null = _null_phi_roll(img, rng)
                else:
                    img_null = _null_pixel_shuffle(img, rng)

                img_null = img_null - np.mean(img_null)
                if obs_welch is not None:
                    # Welch mode: evaluate targets via the same sliding-window estimator.
                    vals_n = _welch_targets(img_null, targets, args.window2d, args.radial, wx=wx, wy=wy, sx=sx, sy=sy)
                    for t in targets:
                        mc_vals[t.k].append(float(vals_n[t.k]))

                    # FIRST FILTER accumulation (welch branch via global FFT)
                    # Even in Welch-target mode, accumulate MC full-spectrum via *global* FFT
                    # so we can compute mc_mean/mc_std/z/p_tail in the dump CSV.
                    if args.dump_radial_csv and args.radial and obs_spec is not None and mean is not None:
                        imgw_null = img_null * w2
                        psd_n, ky_n, kx_n = _fft2_psd(imgw_null)
                        _, psd_rn = _radial_average(psd_n, ky_n, kx_n, kmax=len(k_bins)-1)
                        psd_rn2 = psd_rn[: len(obs_spec)]
                        n_mc += 1
                        delta = psd_rn2 - mean
                        mean += delta / n_mc
                        delta2 = psd_rn2 - mean
                        m2 += delta * delta2
                        ge += (psd_rn2 >= obs_spec).astype(float)
                else:
                    imgw_null = img_null * w2
                    psd_n, ky_n, kx_n = _fft2_psd(imgw_null)

                    if args.radial:
                        _, psd_rn = _radial_average(psd_n, ky_n, kx_n, kmax=len(k_bins)-1)

                        # FIRST FILTER accumulation (global radial spectrum)
                        if args.dump_radial_csv and args.radial and obs_spec is not None and mean is not None:
                            psd_rn2 = psd_rn[: len(obs_spec)]
                            n_mc += 1
                            delta = psd_rn2 - mean
                            mean += delta / n_mc
                            delta2 = psd_rn2 - mean
                            m2 += delta * delta2
                            ge += (psd_rn2 >= obs_spec).astype(float)
                        for t in targets:
                            if t.k < len(psd_rn):
                                mc_vals[t.k].append(float(psd_rn[t.k]))
                    else:
                        ky0 = int(np.where(ky_n == 0)[0][0]) if np.any(ky_n == 0) else 0
                        for t in targets:
                            k = t.k
                            if 0 <= k < len(kx_n):
                                mc_vals[t.k].append(float(psd_n[ky0, k]))

            for t in targets:
                vals = np.asarray(mc_vals[t.k], dtype=float)
                if len(vals) > 0 and np.isfinite(obs[t.k]):
                    p_mc[t.k] = float(np.mean(vals >= obs[t.k]))


            # FIRST FILTER finalize
            if args.dump_radial_csv and args.radial and obs_spec is not None and mean is not None and n_mc > 1:
                mc_mean = mean
                mc_std = np.sqrt(m2 / (n_mc - 1))
                z = np.full_like(obs_spec, np.nan, dtype=float)
                np.divide(obs_spec - mc_mean, mc_std, out=z, where=mc_std > 0)
                p_tail = ge / float(n_mc)
            print("\n=== MC p-values (one-sided: PSD >= observed) ===")
            for t in targets:
                print(f"{ch} k={t.k} p_mc={p_mc[t.k]:.6g}")

        for t in targets:
            rows.append({
                "channel": ch,
                "nside_out": args.nside_out,
                "nlat": args.nlat,
                "nlon": args.nlon,
                "lat_cut_deg": args.lat_cut,
                "field": args.field,
                "window2d": args.window2d,
                "radial": bool(args.radial),
                "null": args.null if args.mc > 0 else "",
                "mc": int(args.mc),
                "seed": int(args.seed),
                "k_target": int(t.k),
                "obs_psd": obs[t.k],
                "p_mc": p_mc[t.k],
            })

        # Plot: show log-psd and radial curve
        if have_mpl:
            import matplotlib.pyplot as plt
            fig = plt.figure(figsize=(10, 4))
            ax1 = fig.add_subplot(1, 2, 1)
            im = ax1.imshow(np.log10(psd + 1e-30), origin="lower", aspect="auto")
            ax1.set_title(f"{ch} log10 PSD (2D FFT)")
            ax1.set_xlabel("kx (rfft bins)")
            ax1.set_ylabel("ky (fft bins)")
            fig.colorbar(im, ax=ax1, fraction=0.046, pad=0.04)

            ax2 = fig.add_subplot(1, 2, 2)
            if args.radial:
                ax2.plot(k_bins, psd_r)
                for t in targets:
                    if t.k < len(psd_r):
                        ax2.axvline(t.k, linestyle="--", linewidth=1)
                ax2.set_xlabel("|k| (cycles / map)")
                ax2.set_ylabel("radial PSD")
                ax2.set_title(f"{ch} radial PSD")
            else:
                # slice ky=0
                ky0 = int(np.where(ky == 0)[0][0]) if np.any(ky == 0) else 0
                ax2.plot(np.arange(len(kx)), psd[ky0])
                for t in targets:
                    ax2.axvline(t.k, linestyle="--", linewidth=1)
                ax2.set_xlabel("kx (cycles / map)")
                ax2.set_ylabel("PSD(ky=0)")
                ax2.set_title(f"{ch} ky=0 PSD")

            _ensure_dir_for(args.plot_png)
            # If multiple channels requested, suffix each channel.
            out_png = args.plot_png
            if len(ch_list) > 1 and out_png:
                base, ext = os.path.splitext(out_png)
                out_png = f"{base}_{ch}{ext}"
            fig.tight_layout()
            fig.savefig(out_png, dpi=160)
            plt.close(fig)
            print(f"[info] wrote PNG: {out_png}")

        # FIRST FILTER: dump full radial spectrum CSV
        if args.dump_radial_csv and args.radial and obs_spec is not None:
            meta = dict(
                nside_out=args.nside_out,
                nlat=args.nlat,
                nlon=args.nlon,
                lat_cut_deg=args.lat_cut,
                field=args.field,
                window2d=args.window2d,
                radial=True,
                null=args.null if args.mc and args.mc > 0 else "",
                mc=int(args.mc),
                seed=int(args.seed),
            )
            out_csv = args.dump_radial_csv
            if len(ch_list) > 1 and out_csv:
                base, ext = os.path.splitext(out_csv)
                out_csv = f"{base}_{ch}{ext}"
            _write_radial_dump_csv(out_csv, ch, meta, obs_spec, mc_mean, mc_std, z, p_tail)
            print(f"[info] wrote radial dump CSV: {out_csv}")

    if args.report_csv:
        _ensure_dir_for(args.report_csv)
        # Consistent columns
        fieldnames = [
            "channel","nside_out","nlat","nlon","lat_cut_deg","field","window2d","radial",
            "null","mc","seed","k_target","obs_psd","p_mc"
        ]
        with open(args.report_csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for r in rows:
                w.writerow(r)
        print(f"[info] wrote CSV: {args.report_csv}")


if __name__ == "__main__":
    main()