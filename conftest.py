"""Test fixtures for selenium UAT for adventurer's codex."""

import logging
import sys
from time import gmtime, strftime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character import wizard
from components.core.dm.encounter_add_edit_modal import EncounterAddEditModal
from components.core.dm.encounter_list import EncounterList
from components.core.dm.tabs import DMTabs
from components.core.dm.wizard import TellUsAStory
from components.core.general.new_character_campaign import NewCharacterCampaign
from components.core.general.api_navbar import Loginapi
from components.core.general.api_navbar import Username
from components.core.general.api_navbar import Password
from components.core.general.api_navbar import Submit

from factories.core.dm.encounter import EncounterAddEditModalFactory


LOGGER.setLevel(logging.WARNING)

DEFAULT_WAIT_TIME = 15


def login_user(browser, login, usr, pwd):
    """User logs in"""
    print('As a User, I am able to login')
    login = Loginapi(browser)
    login.login_link.click()

    user = Username(browser)
    user.username = usr

    password = Password(browser)
    password.password = pwd

    submit = Submit(browser)
    submit.submit.click()


def pytest_addoption(parser):
    """Command line parameters."""
    parser.addoption('--web_driver', action='store', default='chrome')
    parser.addoption('--login', action='store', default=False)
    parser.addoption('--usr', action='store', default=None)
    parser.addoption('--pwd', action='store', default=None)
    parser.addoption('--opera_binary_path', action='store')
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
def opera_binary_path(request):
    """Return command line argument."""
    return request.config.getoption('--opera_binary_path')


@pytest.fixture
def url(request):
    """Return command line argument."""
    return request.config.getoption('--url')


@pytest.fixture(scope='function')
def browser(request, web_driver, opera_binary_path, url):
    """Return selenium webdriver chrome instance."""
    driver = None
    if web_driver.lower() == 'chrome':
        driver = webdriver.Chrome()

    elif web_driver.lower() == 'firefox':
        driver = webdriver.Firefox()

    elif web_driver.lower() == 'safari':
        driver = webdriver.Safari()

    elif web_driver.lower() == 'opera':
        if not opera_binary_path:
            raise Exception('Opera binary path required: --opera_binary_path')

        options = webdriver.ChromeOptions()
        options.binary_location = opera_binary_path

        driver = webdriver.Opera(options=options)

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


@pytest.fixture
def login(request):
    """Return command line argument."""
    return request.config.getoption('--login')


@pytest.fixture
def usr(request):
    """Return command line argument."""
    return request.config.getoption('--usr')


@pytest.fixture
def pwd(request):
    """Return command line argument."""
    return request.config.getoption('--pwd')


@pytest.fixture(scope='function')
def dm_wizard(browser, login, usr, pwd):
    """Navigate through the dm wizard."""

    if login:
        login_user(browser, login, usr, pwd)

    wizard_main = NewCharacterCampaign(browser)
    tell_us_a_story = TellUsAStory(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.get_started_id)
        )
    )

    wizard_main.get_started.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.dm_id)
        )
    )

    wizard_main.dm.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.next_id)
        )
    )

    wizard_main.next_.click()

    tell_us_a_story.campaign_name = 'Test Campaign'
    tell_us_a_story.player_name = 'Automated Testing Bot.'

    wizard_main.finish.click()


@pytest.fixture(scope='function')
def encounter_all_sections(browser):
    """Will create an encounter with all sections."""
    tabs = DMTabs(browser)

    tabs.encounters.click()

    encounter_list = EncounterList(browser)

    encounter_list.add_plus_icon.click()

    encounter_add_edit_modal = EncounterAddEditModal(browser)

    stub = EncounterAddEditModalFactory.stub()

    encounter_add_edit_modal.encounter_name = stub.encounter_name
    encounter_add_edit_modal.location = stub.location
    encounter_add_edit_modal.environment.click()
    encounter_add_edit_modal.maps_and_images.click()
    encounter_add_edit_modal.points_of_interest.click()
    encounter_add_edit_modal.non_player_characters.click()
    encounter_add_edit_modal.monsters.click()
    encounter_add_edit_modal.treasure.click()
    encounter_add_edit_modal.done.click()


@pytest.fixture(scope='function')
def player_wizard(browser, login, usr, pwd):
    """Navigate through the player wizard."""

    if login:
        login_user(browser, login, usr, pwd)

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)
    ability_scores = wizard.AbilityScoresManual(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.get_started_id)
        )
    )

    wizard_main.get_started.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.player_id)
        )
    )

    wizard_main.player.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.next_id)
        )
    )

    wizard_main.next_.click()

    who_are_you.character_name = 'Test Char'
    who_are_you.player_name = 'Automated Testing Bot.'

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
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
