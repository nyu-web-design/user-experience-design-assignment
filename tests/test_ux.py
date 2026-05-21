"""
Tests for the user_experience_design.html page.

Requires Selenium 4.6+ (uses Selenium Manager to auto-manage chromedriver)
and a recent installation of Google Chrome.
"""

import json
import pytest
from urllib.request import urlopen, Request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def _build_url(site_url, page=""):
  base = site_url.rstrip("/")
  if not page:
    return base + "/"
  return base + "/" + page.lstrip("/")


class Tests:

  @pytest.fixture(scope="class")
  def settings(self):
    with open('./settings.json', 'r') as f:
      yield json.load(f)

  @pytest.fixture(scope="class")
  def driver(self, settings):
    options = Options()
    options.add_argument("--window-size=1400,1000")
    driver = webdriver.Chrome(options=options)
    driver.get(_build_url(settings["site_url"], "user_experience_design.html"))
    yield driver
    driver.quit()

  def test_h1(self, driver):
    """The h1 must mention 'User Experience'."""
    elem = driver.find_element(By.TAG_NAME, "h1")
    assert "user experience" in elem.text.lower(), (
      "Page <h1> must include the text 'User Experience'."
    )

  def test_sections(self, driver):
    """The three required <section> elements must exist with the right classes."""
    driver.find_element(By.CSS_SELECTOR, "section.prototype")
    driver.find_element(By.CSS_SELECTOR, "section.wireframes")
    driver.find_element(By.CSS_SELECTOR, "section.site_map")

  def test_each_section_has_h2(self, driver):
    """Each required <section> must contain an <h2> heading."""
    for cls, label in (
      ("prototype", "Clickable Prototype"),
      ("wireframes", "Wireframes"),
      ("site_map", "Site Map"),
    ):
      headings = driver.find_elements(By.CSS_SELECTOR, "section.{} h2".format(cls))
      assert headings, "<section class='{}'> has no <h2> heading.".format(cls)
      texts = [h.text.strip().lower() for h in headings]
      assert any(label.lower() in t for t in texts), (
        "Expected an <h2> heading containing '{}' inside <section class='{}'>; "
        "found: {}".format(label, cls, texts)
      )

  def test_wireframes_exist(self, driver):
    """
    There must be at least 5 wireframe <img> elements (one per page of the
    imaginary site, per the README's '5 pages' minimum).
    """
    elems = driver.find_elements(By.CSS_SELECTOR, "section.wireframes img")
    assert len(elems) >= 5, (
      "Expected at least 5 wireframe images in <section class='wireframes'>; "
      "found {}.".format(len(elems))
    )

  def test_wireframes_have_alt(self, driver):
    """Wireframe images must have non-empty alt attributes."""
    elems = driver.find_elements(By.CSS_SELECTOR, "section.wireframes img")
    for img in elems:
      alt = img.get_attribute("alt")
      assert alt is not None and alt.strip() != "", (
        "A wireframe <img> is missing an alt attribute: {}".format(
          img.get_attribute("src")
        )
      )

  def test_site_map_exists(self, driver):
    """The site map section must include at least one <img>."""
    elems = driver.find_elements(By.CSS_SELECTOR, "section.site_map img")
    assert len(elems) >= 1, "No <img> in <section class='site_map'>."

  def test_prototype_link_exists(self, driver):
    """The prototype section must include a link to a clickable prototype."""
    elems = driver.find_elements(By.CSS_SELECTOR, "section.prototype a[href]")
    assert len(elems) >= 1, (
      "No <a> link to a clickable prototype in <section class='prototype'>."
    )

  def test_prototype_link_is_absolute(self, driver):
    """The prototype link must be an absolute URL (not a local file)."""
    elems = driver.find_elements(By.CSS_SELECTOR, "section.prototype a[href]")
    hrefs = [e.get_attribute("href") or "" for e in elems]
    assert any(
      h.startswith("http://") or h.startswith("https://") for h in hrefs
    ), (
      "Expected at least one absolute URL in <section class='prototype'> "
      "links; found: {}".format(hrefs)
    )

  def test_prototype_url_loads(self, settings):
    """
    The clickable_prototype_url in settings.json must respond with HTTP
    200. We don't assert on the page contents because most prototype
    services render entirely client-side.
    """
    url = settings.get("clickable_prototype_url", "")
    assert url.startswith("http://") or url.startswith("https://"), (
      "settings.json clickable_prototype_url is not a real URL: {}".format(url)
    )
    try:
      req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
      with urlopen(req, timeout=15) as resp:
        # 200 OK, or one of the common redirect codes that urlopen will follow.
        assert resp.status == 200, (
          "Expected clickable_prototype_url to return 200, got {}.".format(resp.status)
        )
    except Exception as e:
      raise AssertionError(
        "Could not load clickable_prototype_url {} : {}".format(url, e)
      )
