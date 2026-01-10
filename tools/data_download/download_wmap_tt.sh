#!/usr/bin/env bash
# Download WMAP 9-Year TT Power Spectrum
#
# This script downloads WMAP 9-year TT power spectrum from NASA Lambda Archive
# for independent replication of CMB comb fingerprint test.
#
# Usage:
#   bash tools/data_download/download_wmap_tt.sh
#
# Output:
#   Files downloaded to data/wmap/raw/
#
# License: MIT
# Author: UBT Research Team

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Paths
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR="${REPO_ROOT}/data/wmap/raw"

echo "========================================"
echo "WMAP 9-Year TT Spectrum Downloader"
echo "========================================"
echo ""

# Create output directory if it doesn't exist
mkdir -p "${OUTPUT_DIR}"

echo "Output directory: ${OUTPUT_DIR}"
echo ""

# Official WMAP data URLs from NASA Lambda
BASE_URL="https://lambda.gsfc.nasa.gov/data/map/dr5/ancillary"

# WMAP TT spectrum file
WMAP_TT_URL="${BASE_URL}/wmap_tt_spectrum_9yr_v5.txt"
WMAP_TT_FILE="wmap_tt_spectrum_9yr_v5.txt"

echo "Downloading WMAP 9-year TT power spectrum for independent replication..."
echo ""

# Function to download file if it doesn't exist
download_file() {
    local url="$1"
    local filename="$2"
    local filepath="${OUTPUT_DIR}/${filename}"
    
    if [ -f "${filepath}" ]; then
        echo -e "${YELLOW}[SKIP]${NC} ${filename} already exists"
        return 0
    fi
    
    echo -e "${GREEN}[DOWNLOAD]${NC} ${filename}"
    echo "  URL: ${url}"
    
    # Try wget first, fall back to curl
    if command -v wget &> /dev/null; then
        wget -q --show-progress -O "${filepath}" "${url}" || {
            echo -e "${RED}[ERROR]${NC} Download failed for ${filename}"
            echo ""
            echo "This may be due to:"
            echo "  - URL has changed (check NASA Lambda)"
            echo "  - Network connectivity issues"
            echo "  - Server is temporarily unavailable"
            echo ""
            echo "Please visit https://lambda.gsfc.nasa.gov/product/map/current/"
            echo "and download manually to: ${OUTPUT_DIR}"
            return 1
        }
    elif command -v curl &> /dev/null; then
        curl -L --progress-bar -o "${filepath}" "${url}" || {
            echo -e "${RED}[ERROR]${NC} Download failed for ${filename}"
            return 1
        }
    else
        echo -e "${RED}[ERROR]${NC} Neither wget nor curl found. Please install one of them."
        return 1
    fi
    
    echo -e "${GREEN}[SUCCESS]${NC} Downloaded ${filename}"
    echo ""
}

# Download WMAP TT spectrum
if ! download_file "${WMAP_TT_URL}" "${WMAP_TT_FILE}"; then
    echo ""
    echo -e "${RED}ERROR:${NC} Automatic download failed."
    echo ""
    echo "MANUAL DOWNLOAD REQUIRED:"
    echo "  1. Visit: https://lambda.gsfc.nasa.gov/product/map/current/"
    echo "  2. Navigate to: Data Products → Power Spectra → TT Spectrum"
    echo "  3. Download: ${WMAP_TT_FILE}"
    echo "  4. Save to: ${OUTPUT_DIR}"
    echo ""
    exit 1
fi

# Check if download was successful
if [ ! -f "${OUTPUT_DIR}/${WMAP_TT_FILE}" ]; then
    echo -e "${YELLOW}WARNING:${NC} Expected file not found after download."
    echo ""
    echo "Please download manually from:"
    echo "  https://lambda.gsfc.nasa.gov/product/map/current/"
    echo ""
    exit 1
fi

# Summary
echo ""
echo "========================================"
echo "Download Complete"
echo "========================================"
echo ""
echo "Downloaded files are in: ${OUTPUT_DIR}"
echo ""

# List downloaded files
echo "Files:"
ls -lh "${OUTPUT_DIR}" | grep -v "^total" | grep -v "^d" || true
echo ""

# Next steps
echo "========================================"
echo "Next Steps"
echo "========================================"
echo ""
echo "1. Compute SHA-256 hashes for provenance:"
echo ""
echo "   cd data/wmap/raw"
echo "   python ../../../tools/data_provenance/hash_dataset.py wmap_tt_*.txt > ../manifests/wmap_tt_manifest.json"
echo ""
echo "2. Validate data integrity:"
echo ""
echo "   python tools/data_provenance/validate_manifest.py data/wmap/manifests/wmap_tt_manifest.json"
echo ""
echo "3. Run CMB comb test for independent replication:"
echo ""
echo "   See forensic_fingerprint/RUNBOOK_REAL_DATA.md for complete instructions"
echo ""
echo "========================================"
echo ""
echo "Note: WMAP provides INDEPENDENT replication of Planck results."
echo "      Both datasets should show consistent signals if real."
echo ""
