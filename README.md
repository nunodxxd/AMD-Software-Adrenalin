# AMD Software: Adrenalin for Windows 10/11

Driver Updates for AMD Radeon™ Series Graphics and Ryzen™ Chipsets.  
This repository is not official, but it provides the official drivers extracted directly from the [AMD Drivers and Support](https://www.amd.com/en/support) website.

## Fully Automated Repo

This repository is fully automated — it checks for new stable and optional (beta) driver releases daily and publishes them to [GitHub Releases](https://github.com/nunodxxd/AMD-Software-Adrenalin/releases) with release notes and SHA256 checksums.  
Unfortunately, it is based on web scraping and could break if AMD's frontend changes; I'll try to support it until there's a better alternative.

## Local Usage

```bash
pip install -r requirements.txt

# Check for new versions without downloading
python amd_driver_scraper.py --type stable --check-only
python amd_driver_scraper.py --type optional --check-only

# Download detected drivers and generate changelog
python amd_driver_scraper.py --type stable --download
python amd_driver_scraper.py --type optional --download

# Run unit tests
python -m unittest discover -s tests -v
```

## Official Documentation

Official download: [Get Drivers with AMD Auto-Detect and Install Tool](https://www.amd.com/en/support).

## :warning: Warning

This software doesn't belong to me, I just make it available through GitHub as a personal project.  
[AMD EULA](https://www.amd.com/en/legal/eula/amd-software-eula.html)  
All rights reserved to Advanced Micro Devices, Inc.
