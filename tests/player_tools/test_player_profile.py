"""UAT test file for Adventurer's Codex player tools profile module."""

from components.character.appearance import Appearance
from components.character.background import Background
from components.character.profile import Profile
from components.character.tabs import Tabs


def test_profile_persists(player_wizard, browser):
    """Profile inputs should persist data."""
    print('As a player, profile inputs persist data.')
    profile = Profile(browser)

    tabs = Tabs(browser)
    tabs.profile.click()

    profile.name.clear()

    profile.name = 'Gandalf\t'
    browser.refresh()
    assert profile.name.get_attribute('value') == 'Gandalf'

    profile.deity = 'Moridin\t'
    browser.refresh()
    assert profile.deity.get_attribute('value') == 'Moridin'

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
