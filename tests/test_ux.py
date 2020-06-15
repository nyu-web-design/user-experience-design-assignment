"""
Tests for the presence of the user experience design assignment page and the required content.

Selenium webdriver for Chrome (a.k.a. the file named chromedriver) must be installed in either:
- in the same directory as chrome.exe on Windows (e.g. C:\Program Files\Google\Chrome\Application)
- in a directory that is included in the PATH on Mac OS X (e.g. /usr/local/bin)
"""

import pytest
import json
from selenium import webdriver

class Tests:

  @pytest.fixture(scope="class")
  def settings(self):
    settings = json.load(open('./settings.json', 'r'))
    yield settings

  @pytest.fixture(scope="class")
  def driver(self, settings):
    """
    Pop open a web browser and make it available to the tests.
    """
    print(settings["site_url"])

    # set up the fixture
    driver = webdriver.Chrome()
    driver.get(settings["site_url"] + "/user_experience_design.html") # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_h1(self, driver, settings):
    """
    Check the h1 tag for the correct text
    """
    elem = driver.find_element_by_tag_name("h1")
    assert "User Experience".lower() in elem.text.lower()

  def test_sections(self, driver, settings):
    """
    Check the three required sections exist
    """
    prototype_section = driver.find_element_by_css_selector("section.prototype")
    wireframes_section = driver.find_element_by_css_selector("section.wireframes")
    site_map_section = driver.find_element_by_css_selector("section.site_map")
    assert prototype_section
    assert wireframes_section
    assert site_map_section

  def test_wireframes_exist(self, driver, settings):
    """
    Check that there are at least a few wireframe images
    """
    elems = driver.find_elements_by_css_selector("section.wireframes img")
    assert len(elems) >= 4

  def test_site_map_exists(self, driver, settings):
    """
    Check that there is a site map image
    """
    elems = driver.find_elements_by_css_selector("section.site_map img")
    assert len(elems) >= 1

  def test_prototype_link_exists(self, driver, settings):
    """
    Check that there is a link to a clickable prototype
    """
    elems = driver.find_elements_by_css_selector("section.prototype a")
    assert len(elems) >= 1

  def test_prototype_url_exists(self, driver, settings):
    """
    Check that there is a link to a clickable prototype
    """
    driver.get(settings["clickable_prototype_url"])
    elem = driver.find_element_by_css_selector("img")
    assert elem
