"""
Tests for the basic content of an index.html file of a web site with a particular set of content.

Selenium webdriver for Chrome (a.k.a. the file named chromedriver) must be installed in either:
- in the same directory as chrome.exe on Windows (e.g. C:\Program Files\Google\Chrome\Application)
- in a directory that is included in the PATH on Mac OS X (e.g. /usr/local/bin)
"""

import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    driver.get(settings["site_url"]) # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_link_href_exists(self, driver):
    """
    Check url of links to assignment page.
    """
    target_urls = ['user_experience_design.html']
    for url in target_urls:
      # check for hrefs with either single or double quotes
      elem_option1 = driver.find_element_by_xpath('//a[@href="' + url + '"]')
      elem_option2 = driver.find_element_by_xpath("//a[@href='" + url + "']")
      assert elem_option1 or elem_option2 # check that it exists

  def test_link_text_exists(self, driver):
    """
    Check text of links to all assignment pages.
    """
    target_terms = ['User Experience']
    for term in target_terms:
      assert driver.find_element_by_partial_link_text(term) or driver.find_element_by_partial_link_text(term.lower())