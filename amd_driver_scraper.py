import argparse
import hashlib
import json
import os
import re
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

AMD_BASE_URL = "https://www.amd.com"
CONFIG_PATH = Path("configs/config.json")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024  # 1 MB chunks for faster streaming downloads
VERSION_PATTERN = re.compile(r"(\d+\.\d+\.\d+)")

_SESSION = None
_PAGE_CACHE = {}
_FILE_HASHES = {}


def log_info(message):
    """Log informational message with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO] {timestamp} - {message}", flush=True)


def log_warning(message):
    """Log warning message with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[WARNING] {timestamp} - {message}", flush=True)


def log_error(message):
    """Log error message with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ERROR] {timestamp} - {message}", flush=True)


def log_debug(message):
    """Log debug message with timestamp"""
    if os.environ.get("DEBUG", "false").lower() == "true":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[DEBUG] {timestamp} - {message}", flush=True)


def get_session():
    """Return a shared requests.Session instance for connection pooling"""
    global _SESSION
    if _SESSION is None:
        _SESSION = requests.Session()
    return _SESSION


def clear_cache():
    """Clear in-memory HTML and file hash caches"""
    _PAGE_CACHE.clear()
    _FILE_HASHES.clear()


def set_github_output(name, value):
    """Set GitHub Actions output variable with better logging"""
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"{name}={value}\n")
        log_info(f"Setting GitHub output: {name}={value}")
    else:
        log_info(f"Local output: {name}={value}")


def load_config(config_path=CONFIG_PATH):
    """Load configuration from JSON file"""
    config_path = Path(config_path)
    log_info(f"Loading configuration from {config_path}")

    if not config_path.exists():
        log_error(f"Config file not found: {config_path}")
        raise FileNotFoundError(f"Config file not found: {config_path}")

    log_debug("Reading existing configuration file")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    driver_links = config.setdefault("driver_links", {})
    for key in ("stable", "stable_full", "stable_full_combined", "optional"):
        driver_links.setdefault(key, "")

    log_info("Configuration loaded successfully")
    log_debug(f"Current stable driver link: {driver_links['stable']}")
    log_debug(f"Current optional driver link: {driver_links['optional']}")

    return config


def save_config(config, config_path=CONFIG_PATH):
    """Save configuration to JSON file"""
    config_path = Path(config_path)
    log_info(f"Saving configuration to {config_path}")

    # Ensure configs directory exists
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
        f.write("\n")

    log_info("Configuration saved successfully")


def get_page_content(url, headers, max_retries=3, use_cache=True):
    """Get HTML content from URL with retry mechanism and in-memory caching"""
    if use_cache and url in _PAGE_CACHE:
        log_debug(f"Using cached content for URL: {url}")
        return _PAGE_CACHE[url]

    log_info(f"Fetching content from URL: {url}")
    session = get_session()

    for attempt in range(max_retries):
        try:
            log_debug(f"HTTP request attempt {attempt + 1} of {max_retries}")
            response = session.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            content = response.content
            log_info(
                f"Successfully retrieved content: {len(content)} bytes, status code: {response.status_code}"
            )
            if use_cache:
                _PAGE_CACHE[url] = content
            return content
        except requests.exceptions.RequestException as e:
            log_warning(f"Request failed (attempt {attempt + 1}): {str(e)}")
            if attempt + 1 < max_retries:
                wait_time = 2 ** attempt  # Exponential backoff
                log_info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                log_error(f"Failed to retrieve content after {max_retries} attempts")
                raise


def extract_version_from_link(link):
    """Extract version string from download link"""
    if not link:
        return None
    log_debug(f"Extracting version from link: {link}")
    version_match = VERSION_PATTERN.search(link)
    if version_match:
        version = version_match.group(1)
        log_info(f"Extracted version: {version}")
        return version

    log_warning(f"Could not extract version from link: {link}")
    return None


def format_version_for_files(version):
    """Format version string for use in filenames (e.g., 25.3.1 to 25-3-1)"""
    formatted = version.replace(".", "-")
    log_debug(f"Formatted version {version} to {formatted} for filenames")
    return formatted


def normalize_version(version):
    """Normalize version string to dot-separated format (e.g., 25-3-1 -> 25.3.1)"""
    if not version:
        return ""
    return version.replace("-", ".")


def link_matches_version(link, target_version):
    """Check whether a driver download link matches the expected version"""
    if not link:
        return False
    expected = normalize_version(target_version)
    if not expected:
        return True
    link_version = extract_version_from_link(link)
    # If the URL embeds a semantic version, require it to match the target version
    if link_version:
        return link_version == expected
    return True


def scrape_stable_driver(config):
    """Scrape AMD stable driver download link"""
    log_info("Scraping stable driver download link")
    headers = config["headers"]
    url = config["urls"]["stable_driver"]

    try:
        html = get_page_content(url, headers)

        soup = BeautifulSoup(html, "html.parser")
        elements = soup.select("article.container-fluid > div > div:nth-child(5) > div > a")

        if not elements:
            # Fallback selector if div nesting changes slightly inside the first article
            first_article = soup.find("article", class_="container-fluid")
            if first_article:
                elements = first_article.select('a[href*="/drivers/"]')

        if not elements:
            log_warning("No download link elements found for stable driver")
            return None

        link = elements[0].get("href")
        if not link:
            log_warning("Stable driver element found without href attribute")
            return None

        log_info(f"Found stable driver link: {link}")
        return link
    except Exception as e:
        log_error(f"Error scraping stable driver link: {str(e)}")
        return None


def scrape_optional_driver(config):
    """Scrape AMD optional driver download link"""
    log_info("Scraping optional driver download link")
    headers = config["headers"]
    url = config["urls"]["optional_driver"]

    try:
        html = get_page_content(url, headers)

        soup = BeautifulSoup(html, "html.parser")
        articles = soup.find_all("article", class_="container-fluid")

        log_debug(f"Found {len(articles)} article elements")

        download_link = None
        for i, article in enumerate(articles):
            log_debug(f"Checking article {i + 1}")
            optional_text = article.find(
                "p", string=lambda text: text and "Optional" in text
            )
            if optional_text:
                log_debug(
                    f"Found 'Optional' text in article {i + 1}: {optional_text.text.strip()}"
                )
                link_tag = article.find("a", href=True)
                if link_tag:
                    download_link = link_tag["href"]
                    log_info(f"Found optional driver link: {download_link}")
                    break
                else:
                    log_debug(f"No link found in article {i + 1} with 'Optional' text")

        if not download_link:
            log_warning("No download link found for optional driver")
            return None

        return download_link
    except Exception as e:
        log_error(f"Error scraping optional driver link: {str(e)}")
        return None


def _extract_release_notes_driver_links(html, version):
    """Extract unique driver download links from release notes HTML matching the target version"""
    soup = BeautifulSoup(html, "html.parser")
    a_links = soup.select('a[href*="/drivers/"]')
    log_debug(f"Found {len(a_links)} raw driver link elements")

    matched_links = []
    seen = set()
    for tag in a_links:
        href = (tag.get("href") or "").strip()
        if not href or href in seen:
            continue
        if not link_matches_version(href, version):
            log_debug(
                f"Skipping driver link {href} because it does not match target version {version}"
            )
            continue
        seen.add(href)
        matched_links.append(href)

    log_debug(f"Found {len(matched_links)} matching driver links for version {version}")
    return matched_links


def scrape_full_driver(config, version):
    """Scrape AMD full driver download link"""
    log_info(f"Scraping full driver link for version {version}")
    headers = config["headers"]
    url = config["urls"]["release_notes_template"].format(format_version_for_files(version))

    try:
        html = get_page_content(url, headers)
        links = _extract_release_notes_driver_links(html, version)

        if not links:
            log_warning(f"No full driver links found for version {version}")
            return None

        link = links[0]
        log_info(f"Found full driver link: {link}")
        return link
    except Exception as e:
        log_error(f"Error scraping full driver link: {str(e)}")
        return None


def scrape_full_combined_driver(config, version):
    """Scrape AMD full combined driver download link"""
    log_info(f"Scraping full combined driver link for version {version}")
    headers = config["headers"]
    url = config["urls"]["release_notes_template"].format(format_version_for_files(version))

    try:
        html = get_page_content(url, headers)
        links = _extract_release_notes_driver_links(html, version)

        if len(links) < 2:
            log_warning(
                f"Less than 2 driver links found for version {version}, can't identify combined driver"
            )
            return None

        link = links[1]
        log_info(f"Found full combined driver link: {link}")
        return link
    except Exception as e:
        log_error(f"Error scraping full combined driver link: {str(e)}")
        return None


def calculate_sha256(filepath):
    """Calculate SHA256 checksum of a file, using cached digest if computed during download"""
    abs_path = os.path.abspath(filepath)
    if abs_path in _FILE_HASHES:
        log_debug(f"Using cached SHA256 for {filepath}")
        return _FILE_HASHES[abs_path]

    log_debug(f"Calculating SHA256 for {filepath}")
    with open(filepath, "rb") as f:
        if hasattr(hashlib, "file_digest"):
            digest = hashlib.file_digest(f, "sha256").hexdigest()
        else:
            hasher = hashlib.sha256()
            for chunk in iter(lambda: f.read(DOWNLOAD_CHUNK_SIZE), b""):
                hasher.update(chunk)
            digest = hasher.hexdigest()

    _FILE_HASHES[abs_path] = digest
    return digest


def download_driver(link, headers, output_dir="driver"):
    """Download driver from link with progress reporting and streaming SHA256 calculation"""
    parsed_path = urlparse(link).path
    filename = os.path.basename(parsed_path) or link.split("/")[-1]
    log_info(f"Starting download of driver: {filename}")

    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    log_info(f"Download destination: {filepath}")

    session = get_session()
    try:
        with session.get(link, headers=headers, stream=True, timeout=600) as response:
            response.raise_for_status()

            file_size = int(response.headers.get("content-length", 0))
            log_info(f"File size: {file_size / (1024 * 1024):.2f} MB")

            downloaded = 0
            start_time = time.time()
            last_report_time = start_time
            report_interval = 5  # seconds
            hasher = hashlib.sha256()

            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
                        hasher.update(chunk)
                        downloaded += len(chunk)

                        # Report progress at intervals
                        current_time = time.time()
                        if current_time - last_report_time > report_interval:
                            elapsed = max(current_time - start_time, 1e-6)
                            speed = downloaded / (1024 * 1024 * elapsed)
                            progress = (
                                (downloaded / file_size) * 100 if file_size > 0 else 0
                            )
                            log_info(
                                f"Download progress: {progress:.1f}% "
                                f"({downloaded / (1024 * 1024):.2f} MB / {file_size / (1024 * 1024):.2f} MB), "
                                f"Speed: {speed:.2f} MB/s"
                            )
                            last_report_time = current_time

            download_time = max(time.time() - start_time, 1e-6)
            avg_speed = downloaded / (1024 * 1024 * download_time)
            log_info(
                f"Download completed in {download_time:.2f} seconds ({avg_speed:.2f} MB/s average)"
            )

            _FILE_HASHES[os.path.abspath(filepath)] = hasher.hexdigest()
            return filepath
    except Exception as e:
        log_error(f"Error downloading driver {filename}: {str(e)}")
        if os.path.exists(filepath):
            log_info(f"Removing partial download: {filepath}")
            os.remove(filepath)
        raise


def _absolutize_relative_links(container, base_url=AMD_BASE_URL):
    """Convert root-relative href/src attributes inside a BeautifulSoup tag to absolute AMD URLs"""
    for tag in container.find_all(["a", "img"]):
        attr = "href" if tag.name == "a" else "src"
        val = tag.get(attr)
        if val and val.startswith("/"):
            tag[attr] = urljoin(base_url, val)


def generate_changelog(config, version, driver_files=None):
    """Generate changelog from release notes page"""
    log_info(f"Generating changelog for version {version}")
    version_formatted = format_version_for_files(version)
    headers = config["headers"]
    url = config["urls"]["release_notes_template"].format(version_formatted)

    try:
        log_info(f"Fetching release notes from {url}")
        html = get_page_content(url, headers)

        soup = BeautifulSoup(html, "html.parser")

        selected_elements = soup.select(
            "div.center-container > div > div.cmp-container__content > div > div > div"
        )
        if not selected_elements:
            log_warning("Could not find release notes content in the page")
            return "Changelog not found"

        container = selected_elements[0]
        _absolutize_relative_links(container, AMD_BASE_URL)
        selected_html = container.decode_contents()
        log_debug(f"Found release notes HTML content ({len(selected_html)} characters)")

        # Add SHA256 checksums if driver files are provided
        if driver_files:
            log_info(f"Calculating SHA256 checksums for {len(driver_files)} files")
            selected_html += "<h2>SHA256 checksum:</h2> <ul>"

            for path_to_file in driver_files:
                try:
                    hash_value = calculate_sha256(path_to_file)
                    filename = os.path.basename(path_to_file)
                    selected_html += f"<li>{filename}: {hash_value}</li>"
                    log_debug(f"SHA256 for {filename}: {hash_value}")
                except Exception as e:
                    log_error(f"Error calculating SHA256 for {path_to_file}: {str(e)}")

            selected_html += "</ul>"

        # Convert HTML to Markdown
        log_info("Converting HTML to Markdown")
        markdown_content = markdownify(selected_html, heading_style="ATX")
        log_debug(f"Generated Markdown content ({len(markdown_content)} characters)")

        return markdown_content
    except Exception as e:
        log_error(f"Error generating changelog: {str(e)}")
        return f"Error generating changelog: {str(e)}"


def check_stable_driver(config):
    """Check for new stable driver version"""
    log_info("Checking for new stable driver version")
    old_link = config["driver_links"].get("stable", "")
    log_debug(f"Current stable driver link: {old_link}")

    new_link = scrape_stable_driver(config)

    if not new_link:
        log_error("Failed to fetch stable driver link")
        return None, False

    if new_link != old_link:
        log_info(f"New stable driver link detected: {new_link}")
        version = extract_version_from_link(new_link)

        if version:
            log_info(f"New stable driver version: {version}")
            config["driver_links"]["stable"] = new_link
            save_config(config)
            return version, True
        else:
            log_warning(f"Could not extract version from new link: {new_link}")
            return None, False
    else:
        log_info("No new stable driver link detected")
        return None, False


def check_optional_driver(config):
    """Check for new optional driver version"""
    log_info("Checking for new optional driver version")
    old_link = config["driver_links"].get("optional", "")
    log_debug(f"Current optional driver link: {old_link}")

    new_link = scrape_optional_driver(config)

    if not new_link or new_link == "Download link not found":
        log_warning("No new optional version found or link not found")
        return None, False

    if new_link != old_link:
        log_info(f"New optional driver link detected: {new_link}")
        version = extract_version_from_link(new_link)

        if version:
            log_info(f"New optional driver version: {version}")
            config["driver_links"]["optional"] = new_link
            save_config(config)
            return version, True
        else:
            log_warning(f"Could not extract version from new link: {new_link}")
            return None, False
    else:
        log_info("No new optional driver link detected")
        return None, False


def download_stable_drivers(config, version):
    """Download stable drivers and prepare for release"""
    log_info(f"Downloading stable drivers for version {version}")
    version_formatted = format_version_for_files(version)

    # Get full driver link (clear stale link if not found)
    log_info("Checking for full driver link")
    full_link = scrape_full_driver(config, version_formatted)
    if full_link:
        log_info(f"Found full driver link: {full_link}")
        config["driver_links"]["stable_full"] = full_link
    else:
        log_warning("Full driver link not found; clearing stale stable_full link")
        config["driver_links"]["stable_full"] = ""

    # Get full combined driver link (clear stale link if not found)
    log_info("Checking for full combined driver link")
    full_combined_link = scrape_full_combined_driver(config, version_formatted)
    if full_combined_link:
        log_info(f"Found full combined driver link: {full_combined_link}")
        config["driver_links"]["stable_full_combined"] = full_combined_link
    else:
        log_warning(
            "Full combined driver link not found; clearing stale stable_full_combined link"
        )
        config["driver_links"]["stable_full_combined"] = ""

    save_config(config)

    # Download drivers after verifying each link matches the target version
    driver_files = []
    candidates = [
        ("minimal setup", "stable"),
        ("full setup", "stable_full"),
        ("full combined setup", "stable_full_combined"),
    ]

    for label, key in candidates:
        link = config["driver_links"].get(key, "")
        if not link:
            continue

        if not link_matches_version(link, version):
            log_warning(
                f"Skipping {label} driver ({link}) because its version does not match {version}"
            )
            continue

        log_info(f"Downloading {label} driver")
        try:
            downloaded_file = download_driver(link, config["headers"])
            driver_files.append(downloaded_file)
            log_info(f"Successfully downloaded {label} driver: {downloaded_file}")
        except Exception as e:
            log_error(f"Failed to download {label} driver: {str(e)}")

    log_info(f"Downloaded {len(driver_files)} driver files in total")
    return driver_files


def download_optional_drivers(config):
    """Download optional drivers"""
    log_info("Downloading optional drivers")
    driver_files = []

    optional_link = config["driver_links"].get("optional", "")
    if optional_link:
        log_info(f"Downloading optional driver from {optional_link}")
        try:
            optional_file = download_driver(optional_link, config["headers"])
            driver_files.append(optional_file)
            log_info(f"Successfully downloaded optional driver: {optional_file}")
        except Exception as e:
            log_error(f"Failed to download optional driver: {str(e)}")
    else:
        log_warning("No optional driver link found in configuration")

    log_info(f"Downloaded {len(driver_files)} optional driver files in total")
    return driver_files


def create_changelog(config, version, driver_files=None, is_optional=False):
    """Create and save changelog for a version"""
    log_info(f"Creating changelog for version {version}")

    # Generate changelog
    changelog = generate_changelog(config, version, driver_files)

    # Determine filename based on driver type
    if is_optional or "beta" in version:
        changelog_path = "configs/generated_changelog_optional.md"
    else:
        changelog_path = "configs/generated_changelog.md"

    log_info(f"Saving changelog to {changelog_path}")

    # Ensure configs directory exists
    os.makedirs("configs", exist_ok=True)

    # Save changelog
    with open(changelog_path, "w", encoding="utf-8") as f:
        f.write(changelog)

    log_info(f"Changelog saved successfully ({len(changelog)} characters)")
    return changelog_path


def _log_downloaded_files(driver_files):
    """Log summary of downloaded driver files and their sizes"""
    log_info("=== Downloaded files ===")
    for file in driver_files:
        file_size = os.path.getsize(file) / (1024 * 1024)
        log_info(f"File: {file} ({file_size:.2f} MB)")
    log_info("=====================")


def main():
    log_info("=== AMD Driver Scraper ===")
    log_info(f"Script started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    parser = argparse.ArgumentParser(description="AMD Driver Scraper")
    parser.add_argument(
        "--type",
        choices=["stable", "optional"],
        required=True,
        help="Driver type to scrape",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Only check for new versions without downloading",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="Download drivers for version previously detected",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    # Set debug mode based on argument or environment variable
    if args.debug:
        os.environ["DEBUG"] = "true"
        log_info("Debug mode enabled via command line argument")
    elif os.environ.get("DEBUG", "").lower() == "true":
        log_info("Debug mode enabled via environment variable")

    log_info(
        f"Operating mode: type={args.type}, check_only={args.check_only}, download={args.download}"
    )

    config = load_config()

    if args.type == "stable":
        log_info("=== Processing STABLE driver ===")

        if args.check_only:
            log_info("Check-only mode: Looking for new stable version")
            version, is_new = check_stable_driver(config)
            if is_new and version:
                log_info(f"✅ New stable driver found: {version}")
                set_github_output("version", version)
                set_github_output("tag", version)
            else:
                log_info("❌ No new stable driver found")

        elif args.download:
            log_info("Download mode: Fetching previously detected stable driver")
            version = extract_version_from_link(config["driver_links"].get("stable", ""))
            if not version:
                log_error("Error: No stable version detected to download")
                sys.exit(1)

            log_info(f"Downloading stable driver version: {version}")
            driver_files = download_stable_drivers(config, version)

            if not driver_files:
                log_error("No driver files were downloaded successfully")
                sys.exit(1)

            changelog_path = create_changelog(
                config, version, driver_files, is_optional=False
            )
            set_github_output("changelog", changelog_path)
            _log_downloaded_files(driver_files)

    elif args.type == "optional":
        log_info("=== Processing OPTIONAL driver ===")

        if args.check_only:
            log_info("Check-only mode: Looking for new optional version")
            version, is_new = check_optional_driver(config)
            if is_new and version:
                log_info(f"✅ New optional driver found: {version}")
                set_github_output("version", version)
                set_github_output("beta_tag", f"{version}-beta")
            else:
                log_info("❌ No new optional driver found")

        elif args.download:
            log_info("Download mode: Fetching previously detected optional driver")
            version = extract_version_from_link(
                config["driver_links"].get("optional", "")
            )
            if not version:
                log_error("Error: No optional version detected to download")
                sys.exit(1)

            log_info(f"Downloading optional driver version: {version}")
            driver_files = download_optional_drivers(config)

            if not driver_files:
                log_error("No driver files were downloaded successfully")
                sys.exit(1)

            changelog_path = create_changelog(
                config, version, driver_files, is_optional=True
            )
            set_github_output("changelog", changelog_path)
            _log_downloaded_files(driver_files)

    log_info(f"Script completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_error(f"Unhandled exception: {str(e)}")
        log_error(traceback.format_exc())
        sys.exit(1)