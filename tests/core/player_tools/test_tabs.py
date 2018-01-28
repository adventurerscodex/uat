"""UAT test file for Adventurer's Codex player tabs."""

from components.core.character.tabs import Tabs


def test_navigate_tabs(player_wizard, browser): # noqa
    """As a player, I should be able to navigate through the player tabs."""
    print('As a player, I should be able to navigate through the player tabs.')

    tabs = Tabs(browser)

    tabs.stats.click()
    assert tabs.stats_label.text == 'Stats'

    tabs.skills.click()
    assert tabs.skills_label.text == 'Skills'

    tabs.spells.click()
    assert tabs.spells_label.text == 'Spells'

    tabs.equipment.click()
    assert tabs.equipment_label.text == 'Equipment'

    tabs.inventory.click()
    assert tabs.inventory_label.text == 'Inventory'

    tabs.notes.click()
    assert tabs.notes_label.text == 'Notes'

    tabs.profile.click()
    assert tabs.profile_label.text == 'Profile'

    # TODO: add chat and exhibit after login fixture and party connection
    # testing is ready
