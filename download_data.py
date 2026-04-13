"""
Downloads EPA Toxics Release Inventory (TRI) Basic Plus data files for 2020-2024.
Run this script once before starting the activity.

Usage:
    python download_data.py
"""

import os
import zipfile
import requests
from bs4 import BeautifulSoup

TRI_PAGE = "https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-plus-data-files-calendar-years-1987-present"
YEARS = [2020, 2021, 2022, 2023, 2024]


def get_download_links(page_url):
    """Scrape the TRI data page to find zip file download links for each year."""
    response = requests.get(page_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    links = {}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        for year in YEARS:
            if f"us_{year}" in href.lower() and href.endswith(".zip"):
                full_url = href if href.startswith("http") else "https://www.epa.gov" + href
                links[year] = full_url
    return links


def download_and_extract(year, url):
    """Download a zip file and extract it into a us_YEAR/ folder."""
    zip_path = f"us_{year}.zip"
    out_dir = f"us_{year}"

    if os.path.exists(out_dir):
        print(f"  {year}: folder already exists, skipping")
        return

    print(f"  {year}: downloading from {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"  {year}: extracting...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(out_dir)

    os.remove(zip_path)
    print(f"  {year}: done — files in {out_dir}/")


if __name__ == "__main__":
    print("Finding download links on EPA website...")
    links = get_download_links(TRI_PAGE)

    if not links:
        print("Could not find download links. The EPA may have updated their page.")
        print(f"Visit {TRI_PAGE} and download the 'Basic Plus' zip files manually.")
    else:
        print(f"Found links for years: {sorted(links.keys())}\n")
        for year in YEARS:
            if year in links:
                download_and_extract(year, links[year])
            else:
                print(f"  {year}: no link found — check the EPA page manually")

    print("\nDone. Load the data with:")
    print('  df = pd.read_csv("us_2024/US_1a_2024.txt", sep="\\t", low_memory=False)')
