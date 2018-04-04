"""UAT test file for Adventurer's Codex player tools profile module."""
from selenium.webdriver.common.keys import Keys

from components.core.character.appearance import Appearance
from components.core.character.background import Background
from components.core.character.profile import Profile
from components.core.character.tabs import Tabs
from utils import utils as ut


def test_profile_persists(player_wizard, browser):
    """Profile inputs should persist data."""
    print('As a player, profile inputs persist data.')
    profile = Profile(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    profile.name = 'Gandalf'
    profile.name.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.name.get_attribute('value').strip() == 'Gandalf'

    profile.background = 'Sage'
    profile.background.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.background.get_attribute('value').strip() == 'Sage'

    profile.alignment = 'Chaotic Good'
    profile.alignment.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.alignment.get_attribute('value').strip() == 'Chaotic Good'

    profile.deity = 'Moridin'
    profile.deity.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.deity.get_attribute('value').strip() == 'Moridin'

    profile.race = 'Gnome'
    profile.race.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.race.get_attribute('value').strip() == 'Gnome'

    profile.class_ = 'Fighter'
    profile.class_.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.class_.get_attribute('value').strip() == 'Fighter'

    profile.gender = 'Male'
    profile.gender.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.gender.get_attribute('value').strip() == 'Male'

    profile.age = '12'
    profile.age.send_keys(Keys.TAB)
    browser.refresh()

    assert profile.age.get_attribute('value').strip() == '12'


def test_background_persists(player_wizard, browser):
    """Profile background should persist data."""
    print('As a player, background textareas persist data.')
    background = Background(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    background.traits = 'Traits...'
    background.traits.send_keys(Keys.TAB)
    browser.refresh()

    assert background.traits.get_attribute('value').strip() == 'Traits...'

    background.ideals = 'Ideals...'
    background.ideals.send_keys(Keys.TAB)
    browser.refresh()

    assert background.ideals.get_attribute('value').strip() == 'Ideals...'

    background.bonds = 'Bonds...'
    background.bonds.send_keys(Keys.TAB)
    browser.refresh()

    assert background.bonds.get_attribute('value').strip() == 'Bonds...'

    background.flaws = 'Flaws...'
    background.flaws.send_keys(Keys.TAB)
    browser.refresh()

    assert background.flaws.get_attribute('value').strip() == 'Flaws...'


def test_appearance_persists(player_wizard, browser):
    """Profile appearance should persist data."""
    print('As a player, appearance textareas persist data.')
    appearance = Appearance(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    appearance.height = '5ft'
    appearance.height.send_keys(Keys.TAB)
    browser.refresh()

    assert appearance.height.get_attribute('value').strip() == '5ft'

    appearance.weight = '165'
    appearance.weight.send_keys(Keys.TAB)
    browser.refresh()

    assert appearance.weight.get_attribute('value').strip() == '165'

    appearance.hair_color = 'Brown'
    appearance.hair_color.send_keys(Keys.TAB)
    browser.refresh()

    assert appearance.hair_color.get_attribute('value').strip() == 'Brown'

    appearance.eye_color = 'Brown'
    appearance.eye_color.send_keys(Keys.TAB)
    browser.refresh()

    assert appearance.eye_color.get_attribute('value').strip() == 'Brown'

    appearance.skin_color = 'Fair'
    appearance.skin_color.send_keys(Keys.TAB)
    browser.refresh()

    assert appearance.skin_color.get_attribute('value').strip() == 'Fair'

def test_alignment_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the alignment field, OGL data auto-completes."""
    print('As a player, if I start typing in the alignment field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(
        profile,
        'alignment',
        browser,
        has_search_term=False
    )

    assert profile.alignment.get_attribute('value').strip() == 'Lawful good'

    profile.alignment.clear()

    ut.select_from_autocomplete(
        profile,
        'alignment',
        browser,
        has_search_term=True,
        search_term='c'
    )

    assert profile.alignment.get_attribute('value').strip() == 'Chaotic good'

def test_race_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the race field, OGL data auto-completes."""
    print('As a player, if I start typing in the race field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(
        profile,
        'race',
        browser,
        has_search_term=False
    )

    assert profile.race.get_attribute('value').strip() == 'Dwarf'

    profile.race.clear()

    ut.select_from_autocomplete(
        profile,
        'race',
        browser,
        has_search_term=True,
        search_term='c'
    )

    assert profile.race.get_attribute('value').strip() == 'Rock Gnome'

def test_class_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the class field, OGL data auto-completes."""
    print('As a player, if I start typing in the class field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(
        profile,
        'class_',
        browser,
        has_search_term=False
    )

    assert profile.class_.get_attribute('value').strip() == 'Barbarian'

    profile.class_.clear()

    ut.select_from_autocomplete(
        profile,
        'class_',
        browser,
        has_search_term=True,
        search_term='c'
    )

    assert profile.class_.get_attribute('value').strip() == 'Cleric'

def test_background_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the background field, OGL data auto-completes."""
    print('As a player, if I start typing in the background field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(
        profile,
        'background',
        browser,
        has_search_term=False
    )

    assert profile.background.get_attribute('value').strip() == 'Acolyte'

    profile.background.clear()

    ut.select_from_autocomplete(
        profile,
        'background',
        browser,
        has_search_term=True,
        search_term='f'
    )

    assert profile.background.get_attribute('value').strip() == 'Folk Hero'
