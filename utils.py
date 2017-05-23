"""Utils for selenium testing at AC."""

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def set_input_value(label, value, browser):
    """
    Set a value for an input element.
    This assumes a label with text is a sibling to the input.

    :label: label of the span
    :value: value of the input
    :browser: selenium webdriver object
    """
    xpath = "//span[contains(text(), '{}')]/following-sibling::input"
    xpath = xpath.format(label)
    element = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(value)


def click_button(label, browser):
    """
    Click a button via button text.

    :label: label of the button
    :browser: selenium webdriver object
    """
    xpath = "//button[contains(text(), '{}')]".format(label)
    button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()


def click_link(label, browser):
    """
    Click a link by text.

    :label: label of the link
    :browser: selenium webdriver object
    """
    xpath = "//a[contains(text(), '{}')]".format(label)
    button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()


def click_radio(value, browser):
    """
    Select a radio in the style of AC radios.

    TODO: not sure why we have to select twice, but it's the only
    way I could get it to work.  Improvement needed.

    :value: value of the radio value
    :browser: selenium webdriver object
    """
    time.sleep(1)
    browser.execute_script("$('input:radio[value={}]').click();".format(
        value)
    )
    time.sleep(1)
    browser.execute_script("$('input:radio[value={}]').click();".format(
        value)
    )
