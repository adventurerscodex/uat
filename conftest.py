"""Test fixtures for selenium UAT for adventurer's codex."""

import logging
import pytest
import sys
from time import gmtime, strftime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.general.new_character_campaign import NewCharacterCampaign
from components.core.character import wizard
from components.core.dm.wizard import TellUsAStory


LOGGER.setLevel(logging.WARNING)


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

    elif web_driver.lower() == 'safari':
        driver = webdriver.Safari()

    driver.get(url)
    driver.maximize_window()

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)

    return driver


def pytest_csv_register_columns(columns):
    """Add custom columns to csv reporting."""
    browser = None
    for arg in sys.argv:
        if '--web_driver' in arg:
            arg_string = arg.split('=')
            try:
                browser = arg_string[1]
            except IndexError:
                pass

    columns['browser'] = browser
    columns['created_at'] = strftime('%Y-%m-%d %H:%M:%S', gmtime())


@pytest.fixture(scope='function')
def dm_wizard(browser):
    """Navigate through the dm wizard."""
    wizard_main = NewCharacterCampaign(browser)
    tell_us_a_story = TellUsAStory(browser)

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.get_started_id)
        )
    )

    wizard_main.get_started.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.dm_id)
        )
    )

    wizard_main.dm.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.next_id)
        )
    )

    wizard_main.next_.click()

    tell_us_a_story.campaign_name = 'Test Campaign'
    tell_us_a_story.player_name = 'Automated Testing Bot.'

    wizard_main.finish.click()


@pytest.fixture(scope='function')
def player_wizard(browser):
    """Navigate through the player wizard."""
    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)
    ability_scores = wizard.AbilityScoresManual(browser)

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.get_started_id)
        )
    )

    wizard_main.get_started.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.player_id)
        )
    )

    wizard_main.player.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.next_id)
        )
    )

    wizard_main.next_.click()

    who_are_you.character_name = 'Test Char'
    who_are_you.player_name = 'Automated Testing Bot.'

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.next_id)
        )
    )

    wizard_main.next_.click()

    ability_scores.strength = '18'
    ability_scores.dexterity = '18'
    ability_scores.constitution = '18'
    ability_scores.intelligence = '18'
    ability_scores.wisdom = '18'
    ability_scores.charisma = '18'

    wizard_main.finish.click()
