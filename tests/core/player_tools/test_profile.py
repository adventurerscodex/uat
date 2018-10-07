"""UAT test file for Adventurer's Codex player tools profile module."""
from conftest import DEFAULT_WAIT_TIME
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character.appearance import AppearanceEdit, AppearanceView
from components.core.character.background import BackgroundEdit, BackgroundView
from components.core.character.profile import ProfileEdit, ProfileView
from components.core.character.tabs import Tabs
from utils import general as ut


def test_profile_and_appearance_persists(player_wizard, browser):
    """Profile inputs should persist data."""
    print('As a player, profile inputs persist data.')
    profile_edit = ProfileEdit(browser)
    profile_view = ProfileView(browser)

    appearance_edit = AppearanceEdit(browser)
    appearance_view = AppearanceView(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, profile_view.alignment_xpath),
            'No Alignment'
        )
    )

    profile_edit.edit_btn.click()

    profile_edit.alignment = 'Chaotic Good'

    assert profile_edit.alignment.get_attribute('value').strip() == 'Chaotic Good'

    profile_edit.deity = 'Moridin'

    assert profile_edit.deity.get_attribute('value').strip() == 'Moridin'

    profile_edit.race = 'Gnome'

    assert profile_edit.race.get_attribute('value').strip() == 'Gnome'

    profile_edit.class_ = 'Fighter'

    assert profile_edit.class_.get_attribute('value').strip() == 'Fighter'

    profile_edit.gender = 'Male'

    assert profile_edit.gender.get_attribute('value').strip() == 'Male'

    profile_edit.age = '12'

    assert profile_edit.age.get_attribute('value').strip() == '12'

    appearance_edit.weight = '165'

    assert appearance_edit.weight.get_attribute('value').strip() == '165'

    appearance_edit.hair_color = 'Brown'

    assert appearance_edit.hair_color.get_attribute('value').strip() == 'Brown'

    appearance_edit.eye_color = 'Brown'

    assert appearance_edit.eye_color.get_attribute('value').strip() == 'Brown'

    appearance_edit.skin_color = 'Fair'

    assert appearance_edit.skin_color.get_attribute('value').strip() == 'Fair'

    profile_edit.save_btn.click()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, profile_view.alignment_xpath),
            'Chaotic Good'
        )
    )

    assert profile_view.alignment.text.strip() == 'Chaotic Good'
    assert profile_view.deity.text.strip() == 'Moridin'
    assert profile_view.race.text.strip() == 'Gnome'
    assert profile_view.class_.text.strip() == 'Fighter'
    assert profile_view.gender.text.strip() == 'Male'
    assert profile_view.age.text.strip() == '12'
    assert appearance_view.weight.text.strip() == '165'
    assert appearance_view.hair_color.text.strip() == 'Brown'
    assert appearance_view.eye_color.text.strip() == 'Brown'
    assert appearance_view.skin_color.text.strip() == 'Fair'


def test_background_persists(player_wizard, browser):
    """Profile background should persist data."""
    print('As a player, background textareas persist data.')
    background_edit = BackgroundEdit(browser)
    background_view = BackgroundView(browser)
    profile_view = ProfileView(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, profile_view.alignment_xpath),
            'No Alignment'
        )
    )

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, background_view.traits_xpath),
            'No Personality Trait'
        )
    )

    background_edit.edit_btn.click()

    background_edit.name = 'Sage...'
    background_edit.traits = 'Traits...'
    background_edit.ideals = 'Ideals...'
    background_edit.bonds = 'Bonds...'
    background_edit.flaws = 'Flaws...'

    background_edit.save_btn.click()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, background_view.traits_xpath),
            'Traits...'
        )
    )

    assert background_view.name.text.strip() == 'Sage...'
    assert background_view.traits.text.strip() == 'Traits...'
    assert background_view.ideals.text.strip() == 'Ideals...'
    assert background_view.bonds.text.strip() == 'Bonds...'
    assert background_view.flaws.text.strip() == 'Flaws...'


def test_alignment_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the alignment field, OGL data auto-completes."""
    print('As a player, if I start typing in the alignment field, OGL data auto-completes.')

    profile_edit = ProfileEdit(browser)
    profile_view = ProfileView(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, profile_view.alignment_xpath),
            'No Alignment'
        )
    )

    profile_edit.edit_btn.click()

    ut.select_from_autocomplete(
        profile_edit,
        'alignment',
        browser,
        has_search_term=False
    )

    assert profile_edit.alignment.get_attribute('value').strip() == 'Lawful good'

    profile_edit.alignment.clear()

    ut.select_from_autocomplete(
        profile_edit,
        'alignment',
        browser,
        has_search_term=True,
        search_term='c'
    )

    assert profile_edit.alignment.get_attribute('value').strip() == 'Chaotic good'

def test_race_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the race field, OGL data auto-completes."""
    print('As a player, if I start typing in the race field, OGL data auto-completes.')

    profile_edit = ProfileEdit(browser)
    profile_view = ProfileView(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, profile_view.alignment_xpath),
            'No Alignment'
        )
    )

    profile_edit.edit_btn.click()

    ut.select_from_autocomplete(
        profile_edit,
        'race',
        browser,
        has_search_term=False
    )

    assert profile_edit.race.get_attribute('value').strip() == 'Dwarf'

    profile_edit.race.clear()

    ut.select_from_autocomplete(
        profile_edit,
        'race',
        browser,
        has_search_term=True,
        search_term='c'
    )

    assert profile_edit.race.get_attribute('value').strip() == 'Rock Gnome'

def test_class_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the class field, OGL data auto-completes."""
    print('As a player, if I start typing in the class field, OGL data auto-completes.')

    profile_edit = ProfileEdit(browser)
    profile_view = ProfileView(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, profile_view.alignment_xpath),
            'No Alignment'
        )
    )

    profile_edit.edit_btn.click()

    ut.select_from_autocomplete(
        profile_edit,
        'class_',
        browser,
        has_search_term=False
    )

    assert profile_edit.class_.get_attribute('value').strip() == 'Barbarian'

    profile_edit.class_.clear()

    ut.select_from_autocomplete(
        profile_edit,
        'class_',
        browser,
        has_search_term=True,
        search_term='c'
    )

    assert profile_edit.class_.get_attribute('value').strip() == 'Cleric'

def test_background_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the background field, OGL data auto-completes."""
    print('As a player, if I start typing in the background field, OGL data auto-completes.')

    background_edit = BackgroundEdit(browser)
    profile_view = ProfileView(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, profile_view.alignment_xpath),
            'No Alignment'
        )
    )

    background_edit.edit_btn.click()

    ut.select_from_autocomplete(
        background_edit,
        'name',
        browser,
        has_search_term=False
    )

    assert background_edit.name.get_attribute('value').strip() == 'Acolyte'

    background_edit.name.clear()

    ut.select_from_autocomplete(
        background_edit,
        'name',
        browser,
        has_search_term=True,
        search_term='f'
    )

    assert background_edit.name.get_attribute('value').strip() == 'Folk Hero'
