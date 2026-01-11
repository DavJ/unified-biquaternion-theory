#!/usr/bin/env bash
# Download Planck PR3 Cosmoparams Data
#
# This script downloads Planck PR3 (Release 3) cosmological parameters
# including TT power spectrum for CMB comb fingerprint analysis.
#
# Required files:
#   - COM_PowerSpect_CMB-TT-full_R3.01.txt  (observation)
#   - COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt (model)
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
# Correct directory: ancillary-data/cosmoparams/
BASE_URL="https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams"

# Required files
REQUIRED_FILES=(
    "COM_PowerSpect_CMB-TT-full_R3.01.txt"                                      # Observation
    "COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt" # Model
)

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
    
    # Try wget first, fall back to curl (with timeouts to avoid hanging)
    if command -v wget &> /dev/null; then
        wget -q --timeout=10 --tries=2 -O "${filepath}" "${url}" 2>&1 || {
            echo -e "${RED}[ERROR]${NC} Download failed for ${filename}"
            echo ""
            echo "This may be due to:"
            echo "  - URL has changed (check Planck Legacy Archive)"
            echo "  - Network connectivity issues"
            echo "  - Server is temporarily unavailable"
            echo ""
            return 1
        }
    elif command -v curl &> /dev/null; then
        curl -L --max-time 10 --retry 1 --progress-bar -o "${filepath}" "${url}" || {
            echo -e "${RED}[ERROR]${NC} Download failed for ${filename}"
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
        echo "  - Use the correct PR3 cosmoparams directory:"
        echo "    https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/"
        echo ""
        # Remove the invalid HTML file
        rm -f "${filepath}"
        return 1
    fi
    
    echo -e "${GREEN}[SUCCESS]${NC} Downloaded ${filename}"
    echo ""
    return 0
}

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

# Function to try scraping index for file URLs
scrape_planck_urls() {
    echo "Attempting to discover file URLs from Planck archive..."
    
    # Try to download the cosmoparams directory index
    local index_url="${BASE_URL}/"
    local temp_index="/tmp/planck_cosmoparams_index.html"
    
    if command -v wget &> /dev/null; then
        wget -q -O "${temp_index}" "${index_url}" 2>/dev/null || return 1
    elif command -v curl &> /dev/null; then
        curl -sL -o "${temp_index}" "${index_url}" 2>/dev/null || return 1
    else
        return 1
    fi
    
    # Extract URLs for our required files
    local urls=()
    for filename in "${REQUIRED_FILES[@]}"; do
        # Look for href containing the filename
        local found_url=$(grep -o "href=\"[^\"]*${filename}\"" "${temp_index}" 2>/dev/null | sed 's/href="//;s/"$//' | head -1)
        
        if [ -n "${found_url}" ]; then
            # Make absolute URL if relative
            if [[ "${found_url}" != http* ]]; then
                found_url="${index_url}${found_url}"
            fi
            urls+=("${found_url}")
        fi
    done
    
    rm -f "${temp_index}"
    
    # Return URLs (newline separated)
    if [ ${#urls[@]} -gt 0 ]; then
        printf '%s\n' "${urls[@]}"
        return 0
    else
        return 1
    fi
}

# Main download logic
echo "Downloading required Planck PR3 files..."
echo ""
echo "Required files:"
for file in "${REQUIRED_FILES[@]}"; do
    echo "  - ${file}"
done
echo ""

# Try direct download with known URLs first
success_count=0

# Attempt 1: Try hardcoded URLs
echo "Attempt 1: Using hardcoded URLs..."
for filename in "${REQUIRED_FILES[@]}"; do
    url="${BASE_URL}/${filename}"
    if download_file "${url}" "${filename}"; then
        success_count=$((success_count + 1))
    fi
done

# Attempt 2: If not all files downloaded, try scraping index
if [ ${success_count} -lt ${#REQUIRED_FILES[@]} ]; then
    echo ""
    echo -e "${YELLOW}WARNING:${NC} Some files failed to download with hardcoded URLs."
    echo "Attempt 2: Trying to discover URLs from archive index..."
    echo ""
    
    if scraped_urls=$(scrape_planck_urls); then
        # Convert to array
        mapfile -t url_array <<< "${scraped_urls}"
        
        # Try downloading with scraped URLs
        idx=0
        for filename in "${REQUIRED_FILES[@]}"; do
            if [ -f "${OUTPUT_DIR}/${filename}" ]; then
                continue  # Already downloaded
            fi
            
            if [ ${idx} -lt ${#url_array[@]} ]; then
                url="${url_array[${idx}]}"
                if download_file "${url}" "${filename}"; then
                    success_count=$((success_count + 1))
                fi
            fi
            idx=$((idx + 1))
        done
    else
        echo -e "${YELLOW}WARNING:${NC} Could not scrape URLs from archive index."
    fi
fi

# Check final status
echo ""
echo "========================================"
echo "Download Summary"
echo "========================================"
echo ""

missing_files=()
for filename in "${REQUIRED_FILES[@]}"; do
    if [ -f "${OUTPUT_DIR}/${filename}" ]; then
        echo -e "${GREEN}✓${NC} ${filename}"
    else
        echo -e "${RED}✗${NC} ${filename}"
        missing_files+=("${filename}")
    fi
done

echo ""

if [ ${#missing_files[@]} -eq 0 ]; then
    echo -e "${GREEN}SUCCESS:${NC} All required files downloaded!"
else
    echo -e "${RED}ERROR:${NC} ${#missing_files[@]} file(s) missing!"
    echo ""
    echo "MANUAL DOWNLOAD REQUIRED:"
    echo ""
    echo "  1. Visit: https://irsa.ipac.caltech.edu/Missions/planck.html"
    echo "  2. Navigate to: Release 3 → Ancillary Data → Cosmological Parameters"
    echo "  3. Download the following files:"
    for file in "${missing_files[@]}"; do
        echo "     - ${file}"
    done
    echo "  4. Save them to: ${OUTPUT_DIR}"
    echo ""
    echo "Alternative: Direct download links (if available):"
    for file in "${missing_files[@]}"; do
        echo "  ${BASE_URL}/${file}"
    done
    echo ""
    exit 1
fi

# List downloaded files with sizes
echo ""
echo "========================================"
echo "Downloaded Files"
echo "========================================"
echo ""
ls -lh "${OUTPUT_DIR}" | grep -v "^total" | grep -v "^d" | grep -v ".gitkeep" || true
echo ""

# Next steps
echo "========================================"
echo "Next Steps"
echo "========================================"
echo ""
echo "1. Compute SHA-256 hashes for provenance:"
echo ""
echo "   # from repo root (recommended)"
echo "   mkdir -p data/planck_pr3/manifests"
echo "   python tools/data_provenance/hash_dataset.py \\\"
echo "     data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \\\"
echo "     data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt \\\"
echo "     > data/planck_pr3/manifests/planck_pr3_tt_manifest.json"
echo ""
echo "2. Validate data integrity:"
echo ""
echo "   python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/planck_pr3_tt_manifest.json"
echo ""
echo "3. Run CMB comb test:"
echo ""
echo "   cd forensic_fingerprint/cmb_comb"
echo "   python cmb_comb.py \\"
echo "       --dataset planck_pr3 \\"
echo "       --input_obs ../../data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \\"
echo "       --input_model ../../data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt \\"
echo "       --ell_min 30 --ell_max 1500"
echo ""
echo "4. See forensic_fingerprint/RUNBOOK_REAL_DATA.md for complete instructions"
echo ""
echo "========================================"

