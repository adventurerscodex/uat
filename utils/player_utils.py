"""Selenium testing utils for player tools."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def switch_tab(tab, browser):
    """
    Swith to designated tab in the players tools.

    :tab: player tab to switch to
    :browser: selenium webdriver object
    """
    xpath = '//a[@href="#{}"]'
    xpath = xpath.format(tab.lower())
    link = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    link.click()
