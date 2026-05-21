"""
Tests for the basic content of the index.html file of a personal web site.

Requires Selenium 4.6+ (uses Selenium Manager to auto-manage chromedriver)
and a recent installation of Google Chrome.
"""

import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


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
    driver.get(_build_url(settings["site_url"]))
    yield driver
    driver.quit()

  def test_link_href_exists(self, driver):
    """The home page must link to user_experience_design.html."""
    try:
      elem = driver.find_element(
        By.CSS_SELECTOR,
        "a[href='user_experience_design.html'], "
        "a[href$='/user_experience_design.html']",
      )
    except NoSuchElementException:
      elem = None
    assert elem, "No link to 'user_experience_design.html' was found on the home page."

  def test_link_text_exists(self, driver):
    """At least one link must mention 'User Experience'."""
    elems_text = ''.join(
      x.text.lower() for x in driver.find_elements(By.CSS_SELECTOR, "a")
    )
    assert 'user experience' in elems_text, (
      "No link text mentions 'User Experience'."
    )
