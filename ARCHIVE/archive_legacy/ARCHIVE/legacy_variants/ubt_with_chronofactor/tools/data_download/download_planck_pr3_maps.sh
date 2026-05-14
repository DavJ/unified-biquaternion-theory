#!/usr/bin/env bash
# Download Planck PR3 CMB Maps for Phase-Comb Test
#
# This script downloads Planck PR3 (Release 3) CMB maps and masks
# for phase-comb fingerprint analysis (requires map-level data, not just C_ℓ).
#
# Required files:
#   - COM_CMB_IQU-smica_2048_R3.00_full.fits  (SMICA CMB map)
#   - COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits  (Common intensity mask)
#
# Usage:
#   bash tools/data_download/download_planck_pr3_maps.sh
#
# Output:
#   Files downloaded to data/planck_pr3/maps/raw/
#   Masks downloaded to data/planck_pr3/maps/masks/
#
# License: MIT
# Author: UBT Research Team

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Paths
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR_MAPS="${REPO_ROOT}/data/planck_pr3/maps/raw"
OUTPUT_DIR_MASKS="${REPO_ROOT}/data/planck_pr3/maps/masks"

echo "========================================"
echo "Planck PR3 CMB Maps Downloader"
echo "========================================"
echo ""
echo -e "${BLUE}Purpose:${NC} Download HEALPix CMB maps for phase-comb test"
echo ""

# Create output directories
mkdir -p "${OUTPUT_DIR_MAPS}"
mkdir -p "${OUTPUT_DIR_MASKS}"

echo "Output directories:"
echo "  Maps:  ${OUTPUT_DIR_MAPS}"
echo "  Masks: ${OUTPUT_DIR_MASKS}"
echo ""

# Official Planck PR3 data URLs from IRSA
# Directory structure: all-sky-maps/maps/component-maps/cmb/
BASE_URL_MAPS="https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb"
BASE_URL_MASKS="https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb"

# Required files
# Note: SMICA is the recommended CMB map for analysis
CMB_MAP_FILE="COM_CMB_IQU-smica_2048_R3.00_full.fits"
MASK_FILE="COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits"

# Function to check if file is not HTML (detects 404 pages)
check_not_html() {
    local filepath="$1"
    
    # Read first 200 bytes
    local header=$(head -c 200 "${filepath}" 2>/dev/null)
    
    # Check for HTML markers
    if echo "${header}" | grep -qi "<!DOCTYPE"; then
        return 1  # Is HTML
    fi
    
    if echo "${header}" | grep -qi "<html"; then
        return 1  # Is HTML
    fi
    
    return 0  # Not HTML
}

# Function to download file if it doesn't exist
download_file() {
    local url="$1"
    local filename="$2"
    local output_dir="$3"
    local filepath="${output_dir}/${filename}"
    
    if [ -f "${filepath}" ]; then
        echo -e "${YELLOW}[SKIP]${NC} ${filename} already exists"
        return 0
    fi
    
    echo -e "${GREEN}[DOWNLOAD]${NC} ${filename}"
    echo "  URL: ${url}"
    echo "  Size: This is a large file (~300-800 MB), please be patient..."
    
    # Try wget first, fall back to curl (with longer timeout for large files)
    if command -v wget &> /dev/null; then
        wget -q --show-progress --timeout=60 --tries=3 -O "${filepath}" "${url}" 2>&1 || {
            echo -e "${RED}[ERROR]${NC} Download failed for ${filename}"
            echo ""
            echo "This may be due to:"
            echo "  - URL has changed (check Planck Legacy Archive)"
            echo "  - Network connectivity issues"
            echo "  - Server is temporarily unavailable"
            echo "  - File is very large and timed out"
            echo ""
            echo "For large files, you may need to download manually from:"
            echo "  https://irsa.ipac.caltech.edu/Missions/planck.html"
            echo ""
            return 1
        }
    elif command -v curl &> /dev/null; then
        curl -L --max-time 300 --retry 2 --progress-bar -o "${filepath}" "${url}" || {
            echo -e "${RED}[ERROR]${NC} Download failed for ${filename}"
            echo ""
            echo "For large files, you may need to download manually."
            echo ""
            return 1
        }
    else
        echo -e "${RED}[ERROR]${NC} Neither wget nor curl found. Please install one of them."
        return 1
    fi
    
    # Verify the downloaded file is not HTML (404 page)
    if ! check_not_html "${filepath}"; then
        echo -e "${RED}[ERROR]${NC} Downloaded HTML (likely 404 error page) instead of data file"
        echo ""
        echo "File: ${filename}"
        echo "URL:  ${url}"
        echo ""
        echo "This likely means:"
        echo "  - The URL path is incorrect"
        echo "  - The file doesn't exist at this location"
        echo ""
        echo "MANUAL DOWNLOAD REQUIRED:"
        echo "  1. Visit: https://irsa.ipac.caltech.edu/Missions/planck.html"
        echo "  2. Navigate to: Release 3 → All-Sky Maps → Component Maps → CMB"
        echo "  3. Download: ${filename}"
        echo "  4. Save to: ${output_dir}/"
        echo ""
        # Remove the invalid HTML file
        rm -f "${filepath}"
        return 1
    fi
    
    # Verify file is a FITS file (should start with "SIMPLE  =")
    local first_line=$(head -c 80 "${filepath}" 2>/dev/null || true)
    if ! echo "${first_line}" | grep -q "SIMPLE"; then
        echo -e "${YELLOW}[WARNING]${NC} Downloaded file may not be a valid FITS file"
        echo "  First 80 bytes: ${first_line}"
        echo "  If download failed, try manual download (see below)"
    fi
    
    echo -e "${GREEN}[SUCCESS]${NC} Downloaded ${filename}"
    
    # Show file size
    local size=$(du -h "${filepath}" | cut -f1)
    echo "  Size: ${size}"
    echo ""
    return 0
}

# Main download logic
echo "Downloading Planck PR3 CMB map and mask..."
echo ""
echo "Required files:"
echo "  1. ${CMB_MAP_FILE} (CMB temperature map)"
echo "  2. ${MASK_FILE} (Common mask)"
echo ""

success_count=0

# Download CMB map
echo "========================================" 
echo "1/2: CMB Map (SMICA)"
echo "========================================" 
url="${BASE_URL_MAPS}/${CMB_MAP_FILE}"
if download_file "${url}" "${CMB_MAP_FILE}" "${OUTPUT_DIR_MAPS}"; then
    success_count=$((success_count + 1))
fi

# Download mask
echo "========================================" 
echo "2/2: Common Mask (Intensity)"
echo "========================================" 
url="${BASE_URL_MASKS}/${MASK_FILE}"
if download_file "${url}" "${MASK_FILE}" "${OUTPUT_DIR_MASKS}"; then
    success_count=$((success_count + 1))
fi

# Check final status
echo ""
echo "========================================"
echo "Download Summary"
echo "========================================"
echo ""

if [ -f "${OUTPUT_DIR_MAPS}/${CMB_MAP_FILE}" ]; then
    echo -e "${GREEN}✓${NC} CMB Map: ${CMB_MAP_FILE}"
else
    echo -e "${RED}✗${NC} CMB Map: ${CMB_MAP_FILE}"
fi

if [ -f "${OUTPUT_DIR_MASKS}/${MASK_FILE}" ]; then
    echo -e "${GREEN}✓${NC} Mask: ${MASK_FILE}"
else
    echo -e "${RED}✗${NC} Mask: ${MASK_FILE}"
fi

echo ""

if [ ${success_count} -eq 2 ]; then
    echo -e "${GREEN}SUCCESS:${NC} All required files downloaded!"
else
    echo -e "${RED}INCOMPLETE:${NC} Some files missing!"
    echo ""
    echo "========================================" 
    echo "MANUAL DOWNLOAD INSTRUCTIONS"
    echo "========================================" 
    echo ""
    echo "If automatic download failed, download manually:"
    echo ""
    echo "1. Visit Planck Legacy Archive:"
    echo "   https://irsa.ipac.caltech.edu/Missions/planck.html"
    echo ""
    echo "2. Navigate to: Release 3 → All-Sky Maps → Component Maps → CMB"
    echo ""
    echo "3. Download these files:"
    echo "   - ${CMB_MAP_FILE}"
    echo "   - ${MASK_FILE}"
    echo ""
    echo "4. Save them to:"
    echo "   - CMB map: ${OUTPUT_DIR_MAPS}/"
    echo "   - Mask:    ${OUTPUT_DIR_MASKS}/"
    echo ""
    echo "Alternative direct download links (may not work if URL structure changed):"
    echo "  ${BASE_URL_MAPS}/${CMB_MAP_FILE}"
    echo "  ${BASE_URL_MASKS}/${MASK_FILE}"
    echo ""
    echo "========================================" 
    exit 1
fi

# List downloaded files with sizes
echo ""
echo "========================================"
echo "Downloaded Files"
echo "========================================"
echo ""
echo "CMB Maps:"
ls -lh "${OUTPUT_DIR_MAPS}" | grep -v "^total" | grep -v "^d" | grep -v ".gitkeep" || true
echo ""
echo "Masks:"
ls -lh "${OUTPUT_DIR_MASKS}" | grep -v "^total" | grep -v "^d" | grep -v ".gitkeep" || true
echo ""

# Next steps
echo "========================================"
echo "Next Steps"
echo "========================================"
echo ""
echo "1. Generate SHA-256 manifest for provenance:"
echo ""
echo "   mkdir -p data/planck_pr3/maps/manifests"
echo "   python tools/data_provenance/hash_dataset.py \\"
echo "     data/planck_pr3/maps/raw/${CMB_MAP_FILE} \\"
echo "     data/planck_pr3/maps/masks/${MASK_FILE} \\"
echo "     > data/planck_pr3/maps/manifests/planck_maps_manifest.json"
echo ""
echo "2. Validate manifest:"
echo ""
echo "   python tools/data_provenance/validate_manifest.py \\"
echo "     data/planck_pr3/maps/manifests/planck_maps_manifest.json"
echo ""
echo "3. Run phase-comb test:"
echo ""
echo "   python forensic_fingerprint/run_real_data_cmb_phase_comb.py \\"
echo "     --planck_map data/planck_pr3/maps/raw/${CMB_MAP_FILE} \\"
echo "     --planck_mask data/planck_pr3/maps/masks/${MASK_FILE} \\"
echo "     --planck_manifest data/planck_pr3/maps/manifests/planck_maps_manifest.json \\"
echo "     --mc_samples 10000"
echo ""
echo "4. See forensic_fingerprint/RUNBOOK_PHASE_COMB.md for complete instructions"
echo ""
echo "========================================"
