import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


def log_info(message):
    """Log informational message with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO] {timestamp} - {message}")


def log_warning(message):
    """Log warning message with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[WARNING] {timestamp} - {message}")


def log_error(message):
    """Log error message with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ERROR] {timestamp} - {message}")


def log_debug(message):
    """Log debug message with timestamp"""
    if os.environ.get("DEBUG", "false").lower() == "true":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[DEBUG] {timestamp} - {message}")


def set_github_output(name, value):
    """Set GitHub Actions output variable with better logging"""
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"{name}={value}\n")
        log_info(f"Setting GitHub output: {name}={value}")
    else:
        # Fallback for local testing or older GitHub Actions
        print(f"::set-output name={name}::{value}")
        log_info(f"Setting output using legacy method: {name}={value}")


def load_config():
    """Load configuration from JSON file"""
    config_path = Path("configs/config.json")
    log_info(f"Loading configuration from {config_path}")
    
    if not config_path.exists():
        log_info("Config file not found.")
    
    # Load existing config
    log_debug("Reading existing configuration file")
    with open(config_path, "r") as f:
        config = json.load(f)
    
    log_info("Configuration loaded successfully")
    log_debug(f"Current stable driver link: {config['driver_links']['stable']}")
    log_debug(f"Current optional driver link: {config['driver_links']['optional']}")
    
    return config


def save_config(config):
    """Save configuration to JSON file"""
    config_path = "configs/config.json"
    log_info(f"Saving configuration to {config_path}")
    
    # Ensure configs directory exists
    os.makedirs("configs", exist_ok=True)
    
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    
    log_info("Configuration saved successfully")


def get_page_content(url, headers, max_retries=3):
    """Get HTML content from URL with retry mechanism"""
    log_info(f"Fetching content from URL: {url}")
    
    for attempt in range(max_retries):
        try:
            log_debug(f"HTTP request attempt {attempt + 1} of {max_retries}")
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            log_info(f"Successfully retrieved content: {len(response.content)} bytes, status code: {response.status_code}")
            return response.content
        except requests.exceptions.RequestException as e:
            log_warning(f"Request failed (attempt {attempt + 1}): {str(e)}")
            if attempt + 1 < max_retries:
                wait_time = 2 ** attempt  # Exponential backoff
                log_info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                log_error(f"Failed to retrieve content after {max_retries} attempts")
                raise


def scrape_stable_driver(config):
    """Scrape AMD stable driver download link"""
    log_info("Scraping stable driver download link")
    headers = config["headers"]
    url = config["urls"]["stable_driver"]
    
    try:
        html = get_page_content(url, headers)
        
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.select('article.container-fluid > div > div:nth-child(5) > div > a')
        
        if not elements:
            log_warning("No download link elements found for stable driver")
            return None
        
        link = elements[0]['href']
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
        
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.find_all("article", class_="container-fluid")
        
        log_debug(f"Found {len(articles)} article elements")
        
        download_link = None
        for i, article in enumerate(articles):
            log_debug(f"Checking article {i+1}")
            optional_text = article.find("p", string=lambda text: text and "Optional" in text)
            if optional_text:
                log_debug(f"Found 'Optional' text in article {i+1}: {optional_text.text.strip()}")
                link_tag = article.find("a", href=True)
                if link_tag:
                    download_link = link_tag["href"]
                    log_info(f"Found optional driver link: {download_link}")
                    break
                else:
                    log_debug(f"No link found in article {i+1} with 'Optional' text")
        
        if not download_link:
            log_warning("No download link found for optional driver")
            return None
            
        return download_link
    except Exception as e:
        log_error(f"Error scraping optional driver link: {str(e)}")
        return None


def scrape_full_driver(config, version):
    """Scrape AMD full driver download link"""
    log_info(f"Scraping full driver link for version {version}")
    headers = config["headers"]
    url = config["urls"]["release_notes_template"].format(version)
    
    try:
        html = get_page_content(url, headers)
        
        soup = BeautifulSoup(html, 'html.parser')
        a_links = soup.select('a[href*="/drivers/"]')
        
        log_debug(f"Found {len(a_links)} driver links")
        
        if not a_links:
            log_warning(f"No full driver links found for version {version}")
            return None
        
        link = a_links[0].get('href')
        log_info(f"Found full driver link: {link}")
        return link
    except Exception as e:
        log_error(f"Error scraping full driver link: {str(e)}")
        return None


def scrape_full_combined_driver(config, version):
    """Scrape AMD full combined driver download link"""
    log_info(f"Scraping full combined driver link for version {version}")
    headers = config["headers"]
    url = config["urls"]["release_notes_template"].format(version)
    
    try:
        html = get_page_content(url, headers)
        
        soup = BeautifulSoup(html, 'html.parser')
        a_links = soup.select('a[href*="/drivers/"]')
        
        log_debug(f"Found {len(a_links)} driver links")
        
        if len(a_links) < 2:
            log_warning(f"Less than 2 driver links found for version {version}, can't identify combined driver")
            return None
        
        link = a_links[1].get('href')
        log_info(f"Found full combined driver link: {link}")
        return link
    except Exception as e:
        log_error(f"Error scraping full combined driver link: {str(e)}")
        return None


def extract_version_from_link(link):
    """Extract version string from download link"""
    log_debug(f"Extracting version from link: {link}")
    import re
    version_match = re.search(r'(\d+\.\d+\.\d+)', link)
    if version_match:
        version = version_match.group(1)
        log_info(f"Extracted version: {version}")
        return version
    
    log_warning(f"Could not extract version from link: {link}")
    return None


def download_driver(link, headers, output_dir="driver"):
    """Download driver from link with progress reporting"""
    filename = link.split('/')[-1]
    log_info(f"Starting download of driver: {filename}")
    
    if not os.path.exists(output_dir):
        log_info(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)
    
    filepath = os.path.join(output_dir, filename)
    log_info(f"Download destination: {filepath}")
    
    try:
        response = requests.get(link, headers=headers, stream=True, timeout=600)  # 10-minute timeout
        response.raise_for_status()
        
        file_size = int(response.headers.get('content-length', 0))
        log_info(f"File size: {file_size / (1024 * 1024):.2f} MB")
        
        downloaded = 0
        start_time = time.time()
        last_report_time = start_time
        report_interval = 5  # seconds
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    # Report progress at intervals
                    current_time = time.time()
                    if current_time - last_report_time > report_interval:
                        elapsed = current_time - start_time
                        speed = downloaded / (1024 * 1024 * elapsed) if elapsed > 0 else 0
                        progress = (downloaded / file_size) * 100 if file_size > 0 else 0
                        log_info(f"Download progress: {progress:.1f}% ({downloaded / (1024 * 1024):.2f} MB / {file_size / (1024 * 1024):.2f} MB), Speed: {speed:.2f} MB/s")
                        last_report_time = current_time
        
        download_time = time.time() - start_time
        log_info(f"Download completed in {download_time:.2f} seconds ({downloaded / (1024 * 1024 * download_time):.2f} MB/s average)")
        
        return filepath
    except Exception as e:
        log_error(f"Error downloading driver {filename}: {str(e)}")
        if os.path.exists(filepath):
            log_info(f"Removing partial download: {filepath}")
            os.remove(filepath)
        raise


def format_version_for_files(version):
    """Format version string for use in filenames (e.g., 25.3.1 to 25-3-1)"""
    formatted = version.replace('.', '-')
    log_debug(f"Formatted version {version} to {formatted} for filenames")
    return formatted


def generate_changelog(config, version, driver_files=None):
    """Generate changelog from release notes page"""
    log_info(f"Generating changelog for version {version}")
    version_formatted = format_version_for_files(version)
    headers = config["headers"]
    url = config["urls"]["release_notes_template"].format(version_formatted)
    
    try:
        log_info(f"Fetching release notes from {url}")
        html = get_page_content(url, headers)
        
        soup = BeautifulSoup(html, 'html.parser')
        
        selected_html = soup.select('div.center-container > div > div.cmp-container__content > div > div > div')
        if not selected_html:
            log_warning("Could not find release notes content in the page")
            return "Changelog not found"
        
        selected_html = selected_html[0].decode_contents()
        log_debug(f"Found release notes HTML content ({len(selected_html)} characters)")
        
        # Add SHA256 checksums if driver files are provided
        if driver_files:
            log_info(f"Calculating SHA256 checksums for {len(driver_files)} files")
            selected_html += '<h2>SHA256 checksum:</h2> <ul>'
            
            for file in driver_files:
                path_to_file = file
                hasher = hashlib.sha256()
                try:
                    log_debug(f"Calculating SHA256 for {path_to_file}")
                    with open(path_to_file, 'rb') as f:
                        for chunk in iter(lambda: f.read(4096), b""):
                            hasher.update(chunk)
                    hash_value = hasher.hexdigest()
                    
                    filename = os.path.basename(path_to_file)
                    selected_html += f'<li>{filename}: {hash_value}</li>'
                    log_debug(f"SHA256 for {filename}: {hash_value}")
                except Exception as e:
                    log_error(f"Error calculating SHA256 for {path_to_file}: {str(e)}")
            
            selected_html += '</ul>'
        
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
    old_link = config["driver_links"]["stable"]
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
    old_link = config["driver_links"]["optional"]
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
    
    # Get full driver link
    log_info("Checking for full driver link")
    full_link = scrape_full_driver(config, version_formatted)
    if full_link:
        log_info(f"Found full driver link: {full_link}")
        config["driver_links"]["stable_full"] = full_link
    else:
        log_warning("Full driver link not found")
    
    # Get full combined driver link
    log_info("Checking for full combined driver link")
    full_combined_link = scrape_full_combined_driver(config, version_formatted)
    if full_combined_link:
        log_info(f"Found full combined driver link: {full_combined_link}")
        config["driver_links"]["stable_full_combined"] = full_combined_link
    else:
        log_warning("Full combined driver link not found")
    
    save_config(config)
    
    # Download drivers
    driver_files = []
    
    # Download minimal setup
    if config["driver_links"]["stable"]:
        log_info("Downloading minimal setup driver")
        try:
            minimal_file = download_driver(config["driver_links"]["stable"], config["headers"])
            driver_files.append(minimal_file)
            log_info(f"Successfully downloaded minimal setup driver: {minimal_file}")
        except Exception as e:
            log_error(f"Failed to download minimal setup driver: {str(e)}")
    
    # Download full setup
    if config["driver_links"]["stable_full"]:
        log_info("Downloading full setup driver")
        try:
            full_file = download_driver(config["driver_links"]["stable_full"], config["headers"])
            driver_files.append(full_file)
            log_info(f"Successfully downloaded full setup driver: {full_file}")
        except Exception as e:
            log_error(f"Failed to download full setup driver: {str(e)}")
    
    # Download full combined setup
    if config["driver_links"]["stable_full_combined"]:
        log_info("Downloading full combined setup driver")
        try:
            full_combined_file = download_driver(config["driver_links"]["stable_full_combined"], config["headers"])
            driver_files.append(full_combined_file)
            log_info(f"Successfully downloaded full combined setup driver: {full_combined_file}")
        except Exception as e:
            log_error(f"Failed to download full combined setup driver: {str(e)}")
    
    log_info(f"Downloaded {len(driver_files)} driver files in total")
    return driver_files


def download_optional_drivers(config):
    """Download optional drivers"""
    log_info("Downloading optional drivers")
    driver_files = []
    
    if config["driver_links"]["optional"]:
        log_info(f"Downloading optional driver from {config['driver_links']['optional']}")
        try:
            optional_file = download_driver(config["driver_links"]["optional"], config["headers"])
            driver_files.append(optional_file)
            log_info(f"Successfully downloaded optional driver: {optional_file}")
        except Exception as e:
            log_error(f"Failed to download optional driver: {str(e)}")
    else:
        log_warning("No optional driver link found in configuration")
    
    log_info(f"Downloaded {len(driver_files)} optional driver files in total")
    return driver_files


def create_changelog(config, version, driver_files=None):
    """Create and save changelog for a version"""
    log_info(f"Creating changelog for version {version}")
    
    # Generate changelog
    changelog = generate_changelog(config, version, driver_files)
    
    # Determine filename based on driver type
    if "beta" in version:
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


def main():
    log_info("=== AMD Driver Scraper ===")
    log_info(f"Script started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    parser = argparse.ArgumentParser(description="AMD Driver Scraper")
    parser.add_argument("--type", choices=["stable", "optional"], required=True, help="Driver type to scrape")
    parser.add_argument("--check-only", action="store_true", help="Only check for new versions without downloading")
    parser.add_argument("--download", action="store_true", help="Download drivers for version previously detected")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()
    
    # Set debug mode based on argument or environment variable
    if args.debug:
        os.environ["DEBUG"] = "true"
        log_info("Debug mode enabled via command line argument")
    elif os.environ.get("DEBUG", "").lower() == "true":
        log_info("Debug mode enabled via environment variable")
    
    log_info(f"Operating mode: type={args.type}, check_only={args.check_only}, download={args.download}")
    
    config = load_config()
    
    if args.type == "stable":
        log_info("=== Processing STABLE driver ===")
        
        if args.check_only:
            log_info("Check-only mode: Looking for new stable version")
            # Only check for new version
            version, is_new = check_stable_driver(config)
            if is_new and version:
                log_info(f"✅ New stable driver found: {version}")
                # Output for GitHub Actions
                set_github_output("version", version)
                set_github_output("tag", version)
            else:
                log_info("❌ No new stable driver found")
                
        elif args.download:
            log_info("Download mode: Fetching previously detected stable driver")
            # Download stage - assumes version was already detected
            version = extract_version_from_link(config["driver_links"]["stable"])
            if version:
                log_info(f"Downloading stable driver version: {version}")
                driver_files = download_stable_drivers(config, version)
                
                if driver_files:
                    changelog_path = create_changelog(config, version, driver_files)
                    
                    # Output for GitHub Actions
                    set_github_output("changelog", changelog_path)
                    
                    # List downloaded files
                    log_info("=== Downloaded files ===")
                    for file in driver_files:
                        file_size = os.path.getsize(file) / (1024 * 1024)
                        log_info(f"File: {file} ({file_size:.2f} MB)")
                    log_info("=====================")
                else:
                    log_error("No driver files were downloaded successfully")
            else:
                log_error("Error: No stable version detected to download")
                sys.exit(1)
                
    elif args.type == "optional":
        log_info("=== Processing OPTIONAL driver ===")
        
        if args.check_only:
            log_info("Check-only mode: Looking for new optional version")
            # Only check for new version
            version, is_new = check_optional_driver(config)
            if is_new and version:
                log_info(f"✅ New optional driver found: {version}")
                # Output for GitHub Actions
                set_github_output("version", version)
                set_github_output("beta_tag", f"{version}-beta")
            else:
                log_info("❌ No new optional driver found")
                
        elif args.download:
            log_info("Download mode: Fetching previously detected optional driver")
            # Download stage - assumes version was already detected
            version = extract_version_from_link(config["driver_links"]["optional"])
            if version:
                log_info(f"Downloading optional driver version: {version}")
                driver_files = download_optional_drivers(config)
                
                if driver_files:
                    changelog_path = create_changelog(config, version, driver_files)
                    
                    # Output for GitHub Actions
                    set_github_output("changelog", changelog_path)
                    
                    # List downloaded files
                    log_info("=== Downloaded files ===")
                    for file in driver_files:
                        file_size = os.path.getsize(file) / (1024 * 1024)
                        log_info(f"File: {file} ({file_size:.2f} MB)")
                    log_info("=====================")
                else:
                    log_error("No driver files were downloaded successfully")
            else:
                log_error("Error: No optional version detected to download")
                sys.exit(1)
    
    log_info(f"Script completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_error(f"Unhandled exception: {str(e)}")
        import traceback
        log_error(traceback.format_exc())
        sys.exit(1)