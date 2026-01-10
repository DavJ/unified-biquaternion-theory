#!/usr/bin/env bash
# Download Planck PR3 Cosmoparams Data
#
# This script downloads Planck PR3 (Release 3) cosmological parameters
# including TT power spectrum for CMB comb fingerprint analysis.
#
# Usage:
#   bash tools/data_download/download_planck_pr3_cosmoparams.sh
#
# Output:
#   Files downloaded to data/planck_pr3/raw/
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
OUTPUT_DIR="${REPO_ROOT}/data/planck_pr3/raw"

echo "========================================"
echo "Planck PR3 Cosmoparams Downloader"
echo "========================================"
echo ""

# Create output directory if it doesn't exist
mkdir -p "${OUTPUT_DIR}"

echo "Output directory: ${OUTPUT_DIR}"
echo ""

# Official Planck PR3 data URLs from IRSA
# Note: These are example URLs - actual URLs may need updating
BASE_URL="https://irsa.ipac.caltech.edu/data/Planck/release_3"

# Files to download
# Primary: COM_CosmoParams package (contains TT spectrum and model)
COSMOPARAMS_URL="${BASE_URL}/ancillary-data/cosmoparams/COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip"
COSMOPARAMS_FILE="COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip"

# Alternative: Direct power spectrum download
POWERSPECT_URL="${BASE_URL}/all-sky-maps/spectra/COM_PowerSpect_CMB-TT-full_R3.01.txt"
POWERSPECT_FILE="COM_PowerSpect_CMB-TT-full_R3.01.txt"

echo "Available downloads:"
echo "  1. Cosmoparams package (includes TT spectrum, model, parameters)"
echo "  2. Direct TT power spectrum only"
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
            echo "  - URL has changed (check Planck Legacy Archive)"
            echo "  - Network connectivity issues"
            echo "  - Server is temporarily unavailable"
            echo ""
            echo "Please visit https://irsa.ipac.caltech.edu/Missions/planck.html"
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

# Main downloads
echo "Downloading Planck PR3 data..."
echo ""

# Option 1: Try downloading cosmoparams package
echo "Attempting to download cosmoparams package..."
if ! download_file "${COSMOPARAMS_URL}" "${COSMOPARAMS_FILE}"; then
    echo ""
    echo -e "${YELLOW}WARNING:${NC} Cosmoparams download failed. This is expected if URL has changed."
    echo "Trying direct power spectrum download..."
    echo ""
    
    # Option 2: Fall back to direct spectrum download
    if ! download_file "${POWERSPECT_URL}" "${POWERSPECT_FILE}"; then
        echo ""
        echo -e "${RED}ERROR:${NC} Automatic download failed."
        echo ""
        echo "MANUAL DOWNLOAD REQUIRED:"
        echo "  1. Visit: https://irsa.ipac.caltech.edu/Missions/planck.html"
        echo "  2. Navigate to: Release 3 → Ancillary Data → Cosmoparams"
        echo "  3. Download: ${COSMOPARAMS_FILE}"
        echo "  4. Save to: ${OUTPUT_DIR}"
        echo ""
        exit 1
    fi
fi

# Check if download directory is empty
if [ -z "$(ls -A "${OUTPUT_DIR}")" ]; then
    echo -e "${YELLOW}WARNING:${NC} No files downloaded successfully."
    echo ""
    echo "Please download files manually from:"
    echo "  https://irsa.ipac.caltech.edu/Missions/planck.html"
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
echo "   cd data/planck_pr3/raw"
echo "   python ../../../tools/data_provenance/hash_dataset.py *.txt *.fits > ../manifests/planck_pr3_tt_manifest.json"
echo ""
echo "2. Validate data integrity:"
echo ""
echo "   python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/planck_pr3_tt_manifest.json"
echo ""
echo "3. Run CMB comb test:"
echo ""
echo "   See forensic_fingerprint/RUNBOOK_REAL_DATA.md for complete instructions"
echo ""
echo "========================================"
