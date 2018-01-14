"""UAT test file for Adventurer's Codex core player tools wizard."""
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import utils as ut


def test_player_wizard(browser):
    """A user should be able to navigate through the player wizard."""
    print('A user should be able to navigate through the player wizard.')

    # Get started with the wizard
    ut.click_button('Get Started', browser)

    # Select type player
    ut.click_radio('characterPlayerType', browser)

    # Navigate to the next step
    ut.click_button('Next', browser)

    # Input required fields
    ut.set_input_value('Character Name', 'Test Char', browser)
    ut.set_input_value('Player Name', 'Automated Testing Bot.', browser)
    # from pdb import set_trace; set_trace()
    # Navigate to the next
    ut.click_button('Next', browser)

    # Fill in values for attributes
    ut.set_input_value('Strength', '18', browser)
    ut.set_input_value('Dexterity', '18', browser)
    ut.set_input_value('Constitution', '18', browser)
    ut.set_input_value('Intelligence', '18', browser)
    ut.set_input_value('Wisdom', '18', browser)
    ut.set_input_value('Charisma', '18', browser)

    # Finish the wizard
    ut.click_button('Finish', browser)


def test_attributes_required(browser):
    """A user should be required to add attribute values."""
    print('A user should be required to add attribute values.')

    # Get started with the wizard
    ut.click_button('Get Started', browser)

    # Select type player
    ut.click_radio('characterPlayerType', browser)

    # Navigate to the next step
    ut.click_button('Next', browser)

    # Input required fields
    ut.set_input_value('Character Name', 'Test Char', browser)
    ut.set_input_value('Player Name', 'Automated Testing Bot.', browser)

    # Navigate to the next
    ut.click_button('Next', browser)

    xpath = "//div[@class='col-md-2 col-padded']//span[contains(text(), 'Required')]"
    errors = WebDriverWait(browser, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))

    # There should be one required text for each attribute
    assert len(errors) == 6

    # With required fields, the finish button should not be visible
    with pytest.raises(NoSuchElementException) as excinfo:
        xpath = "//button[contains(text(), 'Finish')]"
        browser.find_element_by_xpath(xpath)

    assert 'no such element' in str(excinfo)


def test_name_required(browser):
    """A user should be required to enter a char and player name."""
    print('A user should be required to enter a char and player name.')

    # Get started with the wizard
    ut.click_button('Get Started', browser)

    # Select type player
    ut.click_radio('characterPlayerType', browser)

    # Navigate to the next step
    ut.click_button('Next', browser)

    xpath = "//div[@class='col-md-2 col-padded']//span[contains(text(), 'Required')]"
    errors = WebDriverWait(browser, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))

    # There should be one required text for each attribute
    assert len(errors) == 2

    # With required fields, the finish button should not be visible
    with pytest.raises(NoSuchElementException) as excinfo:
        xpath = "//button[contains(text(), 'Next')]"
        browser.find_element_by_xpath(xpath)

    assert 'no such element' in str(excinfo)
