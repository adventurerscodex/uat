"""UAT test file for Adventurer's Codex player tools profile module."""
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

    profile.name = 'Gandalf\t'
    browser.refresh()

    assert profile.name.get_attribute('value') == 'Gandalf'

    profile.background = 'Sage\t'
    browser.refresh()

    assert profile.background.get_attribute('value') == 'Sage'

    profile.alignment = 'Chaotic Good\t'
    browser.refresh()

    assert profile.alignment.get_attribute('value') == 'Chaotic Good'

    profile.deity = 'Moridin\t'
    browser.refresh()

    assert profile.deity.get_attribute('value') == 'Moridin'

    profile.race = 'Gnome\t'
    browser.refresh()

    assert profile.race.get_attribute('value') == 'Gnome'

    profile.class_ = 'Fighter\t'
    browser.refresh()

    assert profile.class_.get_attribute('value') == 'Fighter'

    profile.gender = 'Male\t'
    browser.refresh()

    assert profile.gender.get_attribute('value') == 'Male'

    profile.age = '12\t'
    browser.refresh()

    assert profile.age.get_attribute('value') == '12'


def test_background_persists(player_wizard, browser):
    """Profile background should persist data."""
    print('As a player, background textareas persist data.')
    background = Background(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    background.traits = 'Traits...\t'
    browser.refresh()

    assert background.traits.get_attribute('value') == 'Traits...'

    background.ideals = 'Ideals...\t'
    browser.refresh()

    assert background.ideals.get_attribute('value') == 'Ideals...'

    background.bonds = 'Bonds...\t'
    browser.refresh()

    assert background.bonds.get_attribute('value') == 'Bonds...'

    background.flaws = 'Flaws...\t'
    browser.refresh()

    assert background.flaws.get_attribute('value') == 'Flaws...'


def test_appearance_persists(player_wizard, browser):
    """Profile appearance should persist data."""
    print('As a player, appearance textareas persist data.')
    appearance = Appearance(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    appearance.height = '5ft\t'
    browser.refresh()

    assert appearance.height.get_attribute('value') == '5ft'

    appearance.weight = '165\t'
    browser.refresh()

    assert appearance.weight.get_attribute('value') == '165'

    appearance.hair_color = 'Brown\t'
    browser.refresh()

    assert appearance.hair_color.get_attribute('value') == 'Brown'

    appearance.eye_color = 'Brown\t'
    browser.refresh()

    assert appearance.eye_color.get_attribute('value') == 'Brown'

    appearance.skin_color = 'Fair\t'
    browser.refresh()

    assert appearance.skin_color.get_attribute('value') == 'Fair'

def test_alignment_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the alignment field, OGL data auto-completes."""
    print('As a player, if I start typing in the alignment field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(profile, 'alignment', '', browser)

    assert profile.alignment.get_attribute('value') == 'Lawful good'

    profile.alignment.clear()

    ut.select_from_autocomplete(profile, 'alignment', 'c', browser)

    assert profile.alignment.get_attribute('value') == 'Chaotic good'

def test_race_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the race field, OGL data auto-completes."""
    print('As a player, if I start typing in the race field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(profile, 'race', '', browser)

    assert profile.race.get_attribute('value') == 'Dwarf'

    profile.race.clear()

    ut.select_from_autocomplete(profile, 'race', 'c', browser)

    assert profile.race.get_attribute('value') == 'Rock Gnome'

def test_class_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the class field, OGL data auto-completes."""
    print('As a player, if I start typing in the class field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(profile, 'class_', '', browser)

    assert profile.class_.get_attribute('value') == 'Barbarian'

    profile.class_.clear()

    ut.select_from_autocomplete(profile, 'class_', 'c', browser)

    assert profile.class_.get_attribute('value') == 'Cleric'

def test_background_autocomplete(player_wizard, browser): # noqa
    """As a player, if I start typing in the background field, OGL data auto-completes."""
    print('As a player, if I start typing in the background field, OGL data auto-completes.')

    profile = Profile(browser)
    tabs = Tabs(browser)
    tabs.profile.click()

    ut.select_from_autocomplete(profile, 'background', '', browser)

    assert profile.background.get_attribute('value') == 'Acolyte'

    profile.background.clear()

    ut.select_from_autocomplete(profile, 'background', 'f', browser)

    assert profile.background.get_attribute('value') == 'Folk Hero'
