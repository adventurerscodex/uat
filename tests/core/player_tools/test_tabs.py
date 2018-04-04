"""UAT test file for Adventurer's Codex player tabs."""

from components.core.character.tabs import Tabs


def test_navigate_tabs(player_wizard, browser): # noqa
    """As a player, I should be able to navigate through the player tabs."""
    print('As a player, I should be able to navigate through the player tabs.')

    tabs = Tabs(browser)

    tabs.stats.click()
    assert tabs.stats_label.text.strip() == 'Stats'

    tabs.skills.click()
    assert tabs.skills_label.text.strip() == 'Skills'

    tabs.spells.click()
    assert tabs.spells_label.text.strip() == 'Spells'

    tabs.equipment.click()
    assert tabs.equipment_label.text.strip() == 'Equipment'

    tabs.inventory.click()
    assert tabs.inventory_label.text.strip() == 'Inventory'

    tabs.notes.click()
    assert tabs.notes_label.text.strip() == 'Notes'

    tabs.profile.click()
    assert tabs.profile_label.text.strip() == 'Profile'

    # TODO: add chat and exhibit after login fixture and party connection
    # testing is ready
