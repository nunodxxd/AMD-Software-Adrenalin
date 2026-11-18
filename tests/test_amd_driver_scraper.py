import hashlib
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import amd_driver_scraper as scraper


SAMPLE_SUPPORT_HTML = b"""
<html>
<body>
  <article class="container-fluid">
    <div>
      <div>1</div><div>2</div><div>3</div><div>4</div>
      <div><a href="https://drivers.amd.com/drivers/installer/26.20/beta/amd-software-adrenalin-edition-26.11.1-minimalsetup-261111_web.exe">Download</a></div>
    </div>
  </article>
  <article class="container-fluid">
    <p>Adrenalin 26.11.1 (Optional)</p>
    <a href="https://drivers.amd.com/drivers/amd-software-adrenalin-edition-26.11.1-win11-b.exe">Download Optional</a>
  </article>
  <article class="container-fluid">
    <p>Adrenalin 26.10.1 WHQL (Recommended)</p>
    <a href="https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-26.10.1-win11-b.exe">Download WHQL</a>
  </article>
</body>
</html>
"""

SAMPLE_RELEASE_NOTES_SINGLE_HTML = b"""
<html>
<body>
  <div class="center-container">
    <div>
      <div class="cmp-container__content">
        <div>
          <div>
            <div>
              <h2>Highlights</h2>
              <p>See <a href="/en/resources/support-articles/faqs/RSX2-INSTALL.html">Install Guide</a>.</p>
              <p>Download: <a href="https://drivers.amd.com/drivers/amd-software-adrenalin-edition-26.11.1-win11-c.exe">Driver</a></p>
              <p>Workaround: <a href="https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-26.9.1-win11-c.exe">Old Driver</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

SAMPLE_RELEASE_NOTES_COMBINED_HTML = b"""
<html>
<body>
  <div class="center-container">
    <div>
      <div class="cmp-container__content">
        <div>
          <div>
            <div>
              <a href="https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-25.5.1-win10-win11-may8-rdna.exe">RDNA</a>
              <a href="https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-25.5.1-win10-win11-may8-vega-polaris.exe">Combined</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""


def make_test_config():
    return {
        "headers": {"User-Agent": "TestAgent/1.0"},
        "urls": {
            "stable_driver": "https://www.amd.com/en/support/rx-7900-xt.html",
            "optional_driver": "https://www.amd.com/en/support/rx-7900-xt.html",
            "release_notes_template": "https://www.amd.com/en/resources/RN-RAD-WIN-{}.html",
        },
        "driver_links": {
            "stable": "https://drivers.amd.com/drivers/installer/26.20/beta/amd-software-adrenalin-edition-26.10.2-minimalsetup-261029_web.exe",
            "stable_full": "https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-26.10.2-win11-c.exe",
            "stable_full_combined": "https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-25.5.1-win10-win11-may8-vega-polaris.exe",
            "optional": "https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-26.10.2-win11-b.exe",
        },
    }


class TestAMDDriverScraper(unittest.TestCase):
    def setUp(self):
        scraper.clear_cache()

    def test_version_extraction_and_matching(self):
        link = "https://drivers.amd.com/drivers/installer/26.20/beta/amd-software-adrenalin-edition-26.11.1-minimalsetup-261111_web.exe"
        self.assertEqual(scraper.extract_version_from_link(link), "26.11.1")
        self.assertIsNone(scraper.extract_version_from_link("https://drivers.amd.com/drivers/autodetect.exe"))
        self.assertEqual(scraper.format_version_for_files("26.11.1"), "26-11-1")
        self.assertTrue(scraper.link_matches_version(link, "26.11.1"))
        self.assertTrue(scraper.link_matches_version(link, "26-11-1"))
        self.assertFalse(scraper.link_matches_version(link, "25.5.1"))

    @patch("amd_driver_scraper.get_page_content", return_value=SAMPLE_SUPPORT_HTML)
    def test_scrape_stable_and_optional_drivers(self, _mock_get):
        config = make_test_config()
        stable_link = scraper.scrape_stable_driver(config)
        optional_link = scraper.scrape_optional_driver(config)

        self.assertEqual(
            stable_link,
            "https://drivers.amd.com/drivers/installer/26.20/beta/amd-software-adrenalin-edition-26.11.1-minimalsetup-261111_web.exe",
        )
        self.assertEqual(
            optional_link,
            "https://drivers.amd.com/drivers/amd-software-adrenalin-edition-26.11.1-win11-b.exe",
        )

    @patch("amd_driver_scraper.get_page_content", return_value=SAMPLE_RELEASE_NOTES_SINGLE_HTML)
    def test_scrape_full_driver_ignores_mismatched_version_links(self, _mock_get):
        config = make_test_config()
        # Even though the page has 2 driver links (26.11.1 and a 26.9.1 workaround link),
        # only 26.11.1 matches the target version, so combined driver should be None!
        full_link = scraper.scrape_full_driver(config, "26-11-1")
        combined_link = scraper.scrape_full_combined_driver(config, "26-11-1")

        self.assertEqual(
            full_link,
            "https://drivers.amd.com/drivers/amd-software-adrenalin-edition-26.11.1-win11-c.exe",
        )
        self.assertIsNone(combined_link)

    @patch("amd_driver_scraper.get_page_content", return_value=SAMPLE_RELEASE_NOTES_COMBINED_HTML)
    def test_scrape_full_combined_driver_when_present(self, _mock_get):
        config = make_test_config()
        full_link = scraper.scrape_full_driver(config, "25-5-1")
        combined_link = scraper.scrape_full_combined_driver(config, "25-5-1")

        self.assertEqual(
            full_link,
            "https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-25.5.1-win10-win11-may8-rdna.exe",
        )
        self.assertEqual(
            combined_link,
            "https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-25.5.1-win10-win11-may8-vega-polaris.exe",
        )

    @patch("amd_driver_scraper.save_config")
    @patch("amd_driver_scraper.download_driver")
    @patch("amd_driver_scraper.get_page_content", return_value=SAMPLE_RELEASE_NOTES_SINGLE_HTML)
    def test_download_stable_drivers_clears_stale_combined_link(
        self, _mock_page, mock_download, _mock_save
    ):
        config = make_test_config()
        config["driver_links"]["stable"] = (
            "https://drivers.amd.com/drivers/installer/26.20/beta/amd-software-adrenalin-edition-26.11.1-minimalsetup-261111_web.exe"
        )
        mock_download.side_effect = lambda link, _headers: f"driver/{os.path.basename(link)}"

        files = scraper.download_stable_drivers(config, "26.11.1")

        # Stale 25.5.1 combined link must be cleared and NOT downloaded
        self.assertEqual(config["driver_links"]["stable_full_combined"], "")
        self.assertEqual(len(files), 2)
        self.assertEqual(mock_download.call_count, 2)

    def test_page_cache_prevents_duplicate_http_requests(self):
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RELEASE_NOTES_SINGLE_HTML
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()

        mock_session = MagicMock()
        mock_session.get.return_value = mock_response

        config = make_test_config()
        with patch("amd_driver_scraper.get_session", return_value=mock_session):
            scraper.scrape_full_driver(config, "26-11-1")
            scraper.scrape_full_combined_driver(config, "26-11-1")
            scraper.generate_changelog(config, "26.11.1")

        # All 3 calls hit the same release notes URL, so session.get should only be called once
        self.assertEqual(mock_session.get.call_count, 1)

    @patch("amd_driver_scraper.get_page_content", return_value=SAMPLE_RELEASE_NOTES_SINGLE_HTML)
    def test_generate_changelog_absolutizes_links_and_computes_sha256(self, _mock_get):
        config = make_test_config()
        with tempfile.TemporaryDirectory() as tmpdir:
            dummy_driver = Path(tmpdir) / "amd-software-adrenalin-edition-26.11.1-win11-c.exe"
            payload = b"dummy installer binary content"
            dummy_driver.write_bytes(payload)
            expected_sha = hashlib.sha256(payload).hexdigest()

            markdown = scraper.generate_changelog(
                config, "26.11.1", driver_files=[str(dummy_driver)]
            )

        self.assertIn(
            "https://www.amd.com/en/resources/support-articles/faqs/RSX2-INSTALL.html",
            markdown,
        )
        self.assertIn(
            f"amd-software-adrenalin-edition-26.11.1-win11-c.exe: {expected_sha}",
            markdown,
        )


if __name__ == "__main__":
    unittest.main()
