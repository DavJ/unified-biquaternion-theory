"""
UBT / CMB 2D FFT proof-of-concept (Original Planck Version)

NOTE: This is the original version that requires Planck FITS maps and healpy/astropy.
For a standalone version that works without external data, use cmb_2d_fft_poc.py instead.

- Load Planck CMB map (HEALPix FITS, e.g. SMICA/NILC/SEVEM/Commander)
- Extract a clean small patch via gnomonic projection
- Apodize (taper) to suppress edge ringing
- Compute 2D FFT power
- Detect oriented "comb"/grid-like anisotropy and estimate tilt angle

Dependencies: healpy, astropy, scipy, matplotlib, numpy
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

# --- deps ---
# Try to import healpy and astropy with helpful error message
try:
    import healpy as hp
    from astropy.io import fits
except ImportError as e:
    print("=" * 80)
    print("ERROR: Required dependencies not found for Planck map analysis.")
    print("=" * 80)
    print("\nThis script requires:")
    print("  - healpy (for HEALPix map handling)")
    print("  - astropy (for FITS file reading)")
    print("\nTo install:")
    print("  pip install healpy astropy")
    print("\nAlternatively, use the standalone proof-of-concept:")
    print("  python research_front/cmb_2d_fft/cmb_2d_fft_poc.py")
    print("\nThe PoC version works with synthetic data and requires only:")
    print("  - numpy")
    print("  - scipy")
    print("  - matplotlib")
    print("=" * 80)
    sys.exit(1)

from scipy.ndimage import gaussian_filter
from scipy.signal import windows

# =========================
# CONFIG
# =========================

# Path to a Planck component-separated CMB map in HEALPix FITS.
# Examples (you choose what you have): COM_CMB_IQU-smica_2048_R3.00_full.fits, etc.
MAP_FITS = "data/planck_pr3/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits"  # <-- adjust

# Optional mask path (recommended). If you have a Planck common mask, use it.
MASK_FITS = None  # e.g. "data/planck_pr3/raw/COM_Mask_CMB-common-MaskInt_2048_R3.00.fits"

# Choose a patch center (lon, lat) in degrees.
# Pick something clean: high galactic latitude (|b| > 30 deg). Example: (lon=0, lat=60)
# You can test several and compare stability.
LON_DEG, LAT_DEG = 0.0, 60.0

# Patch geometry
PATCH_DEG = 20.0        # patch width/height in degrees (e.g. 10-30)
PIX_ARCMIN = 5.0        # flat-sky pixel size (arcmin). 5 arcmin is OK for PoC.

# Target tilt angle (degrees)
TARGET_TILT_DEG = np.degrees(np.arctan(1/256))  # ~0.224°
# but we will estimate from data; target only for reporting.
print("Target tilt (deg):", TARGET_TILT_DEG)

# FFT analysis parameters
SMOOTH_SIGMA_PIX = 1.5   # smooth FFT power a bit to make ridge detection easier
RADIAL_BINS = 60         # for angular power vs angle
ANGLE_RES_DEG = 0.05     # resolution for scanning oriented energy

# =========================
# HELPERS
# =========================

def read_planck_cmb_map(path_fits):
    """
    Reads a HEALPix map.
    If IQU, we take I (field=0).
    Works for typical Planck products.
    """
    # healpy can read directly
    # field=0 for temperature
    m = hp.read_map(path_fits, field=0, verbose=False)
    return m

def read_mask(path_fits, nside_target):
    mask = hp.read_map(path_fits, field=0, verbose=False)
    # Ensure same nside
    if hp.get_nside(mask) != nside_target:
        mask = hp.ud_grade(mask, nside_out=nside_target, order_in='RING', order_out='RING')
    # binarize softly
    return (mask > 0.5).astype(np.float32)

def gnomonic_patch(m, lon_deg, lat_deg, patch_deg, pix_arcmin, mask=None):
    """
    Create a flat-sky (gnomonic) projection patch from HEALPix map.
    Returns patch (2D), and optional patch mask (2D).
    """
    # number of pixels
    pix_deg = pix_arcmin / 60.0
    npix = int(np.round(patch_deg / pix_deg))
    npix = max(npix, 64)  # floor
    reso_arcmin = pix_arcmin

    # rot: (lon, lat, psi). Using lon/lat in degrees.
    # 'coord' can be used if map is in Galactic vs Equatorial. Assume map is in Galactic.
    patch = hp.visufunc.gnomview(
        m, rot=(lon_deg, lat_deg, 0.0),
        xsize=npix, ysize=npix, reso=reso_arcmin,
        return_projected_map=True, no_plot=True
    )

    patch_mask = None
    if mask is not None:
        patch_mask = hp.visufunc.gnomview(
            mask, rot=(lon_deg, lat_deg, 0.0),
            xsize=npix, ysize=npix, reso=reso_arcmin,
            return_projected_map=True, no_plot=True
        )
        # ensure {0,1}
        patch_mask = (patch_mask > 0.5).astype(np.float32)

    return patch.astype(np.float32), patch_mask

def apodize_2d(patch, mask=None, alpha=0.2):
    """
    Apply a 2D taper window (Tukey) to reduce edge ringing.
    If mask provided: apply mask then window.
    """
    ny, nx = patch.shape
    wx = windows.tukey(nx, alpha=alpha)
    wy = windows.tukey(ny, alpha=alpha)
    w2 = np.outer(wy, wx).astype(np.float32)

    x = patch.copy()
    if mask is not None:
        x = x * mask
    x = x * w2
    return x, w2

def fft_power(patch):
    """
    Compute centered FFT power spectrum.
    """
    f = np.fft.fft2(patch)
    f = np.fft.fftshift(f)
    p = np.abs(f) ** 2
    return p

def angle_map(ny, nx):
    """
    Return angle (radians) of each FFT pixel w.r.t. center.
    """
    y = np.arange(ny) - ny//2
    x = np.arange(nx) - nx//2
    X, Y = np.meshgrid(x, y)
    ang = np.arctan2(Y, X)  # [-pi,pi]
    r = np.sqrt(X*X + Y*Y)
    return ang, r

def oriented_energy(P, ang, r, rmin=10, rmax=None, theta_deg=0.0, dtheta_deg=0.25):
    """
    Measure energy in an angular wedge around theta and theta+pi (both directions),
    within radial band [rmin, rmax].
    """
    if rmax is None:
        rmax = r.max()
    theta = np.deg2rad(theta_deg)
    dtheta = np.deg2rad(dtheta_deg)

    # wrap angle distance
    def angdist(a, b):
        d = np.angle(np.exp(1j*(a-b)))
        return np.abs(d)

    sel_r = (r >= rmin) & (r <= rmax)

    sel1 = sel_r & (angdist(ang, theta) <= dtheta)
    sel2 = sel_r & (angdist(ang, theta + np.pi) <= dtheta)
    return float(P[sel1].sum() + P[sel2].sum())

def scan_tilt(P, ang, r, rmin=10, rmax=None, scan_deg=(-5, 5), step_deg=0.05, wedge_deg=0.25):
    """
    Scan for the angle maximizing oriented energy.
    Returns best angle in degrees and energy curve.
    """
    angles = np.arange(scan_deg[0], scan_deg[1] + 1e-9, step_deg)
    energies = np.array([oriented_energy(P, ang, r, rmin=rmin, rmax=rmax, theta_deg=a, dtheta_deg=wedge_deg)
                         for a in angles], dtype=np.float64)
    best_idx = int(np.argmax(energies))
    return angles[best_idx], angles, energies

# =========================
# MAIN
# =========================

m = read_planck_cmb_map(MAP_FITS)
nside = hp.get_nside(m)

mask = None
if MASK_FITS:
    mask = read_mask(MASK_FITS, nside)

patch, patch_mask = gnomonic_patch(m, LON_DEG, LAT_DEG, PATCH_DEG, PIX_ARCMIN, mask=mask)

# Remove mean (and optionally a plane) to suppress huge low-k power
patch0 = patch.copy()
if patch_mask is not None:
    valid = patch_mask > 0.5
    mu = patch0[valid].mean()
    patch0[valid] -= mu
    patch0[~valid] = 0.0
else:
    patch0 -= patch0.mean()

# Apodize
patch_w, win = apodize_2d(patch0, mask=patch_mask, alpha=0.2)

# FFT power
P = fft_power(patch_w)
P = np.log1p(P)  # stabilize dynamic range

# Smooth FFT power slightly (optional)
P_s = gaussian_filter(P, sigma=SMOOTH_SIGMA_PIX)

ang, r = angle_map(*P_s.shape)

# Scan small angles around 0 deg to find tiny tilt. In general, a grid manifests as peaks.
# Here we measure oriented energy; you can also look for comb-like peaks along a line.
best, angles, energies = scan_tilt(
    P_s, ang, r,
    rmin=20, rmax=r.max()*0.9,
    scan_deg=(-2, 2),
    step_deg=ANGLE_RES_DEG,
    wedge_deg=0.25
)

print("Best tilt angle (deg):", best)
print("Target tilt angle (deg):", TARGET_TILT_DEG)

# =========================
# PLOTS
# =========================

fig = plt.figure(figsize=(14, 4))

ax1 = fig.add_subplot(1, 3, 1)
ax1.set_title("CMB patch (gnomonic)")
im1 = ax1.imshow(patch0, origin="lower")
plt.colorbar(im1, ax=ax1, fraction=0.046)

ax2 = fig.add_subplot(1, 3, 2)
ax2.set_title("FFT power (log, smoothed)")
im2 = ax2.imshow(P_s, origin="lower")
plt.colorbar(im2, ax=ax2, fraction=0.046)

ax3 = fig.add_subplot(1, 3, 3)
ax3.set_title("Oriented energy vs angle")
ax3.plot(angles, energies)
ax3.axvline(TARGET_TILT_DEG, linestyle="--", label=f"target {TARGET_TILT_DEG:.3f}°")
ax3.axvline(best, linestyle="-", label=f"best {best:.3f}°")
ax3.set_xlabel("angle (deg)")
ax3.set_ylabel("energy (a.u.)")
ax3.legend()

plt.tight_layout()
plt.show()

