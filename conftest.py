"""Test fixtures for selenium UAT for adventurer's codex."""

import pytest

from selenium import webdriver

from utils import utils as ut


def pytest_addoption(parser):
    """Command line parameters."""
    parser.addoption('--web_driver', action='store', default='chrome')
    parser.addoption(
        '--url',
        action='store',
        default='https://nightly.adventurerscodex.com'
    )


@pytest.fixture
def web_driver(request):
    """Return command line argument."""
    return request.config.getoption('--web_driver')


@pytest.fixture
def url(request):
    """Return command line argument."""
    return request.config.getoption('--url')


@pytest.fixture(scope='function')
def browser(request, web_driver, url):
    """Return selenium webdriver chrome instance."""
    driver = None
    if web_driver.lower() == 'chrome':
        driver = webdriver.Chrome()

    elif web_driver.lower() == 'firefox':
        driver = webdriver.Firefox()

    driver.get(url)

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)

    return driver


@pytest.fixture(scope='function')
def dm_wizard(browser):
    """Navigate through the dm wizard."""
    # Get started with the wizard
    ut.click_button('Get Started', browser)

    # Select type player
    ut.click_radio('dmPlayerType', browser)

    # Navigate to the next step
    ut.click_button('Next', browser)

    # Input required fields
    ut.set_input_value('Campaign Name', 'Test Campaign', browser)
    ut.set_input_value('Player Name', 'Automated Testing Bot.', browser)

    # Finish the wizard
    ut.click_button('Finish', browser)


@pytest.fixture(scope='function')
def player_wizard(browser):
    """Navigate through the player wizard."""
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
