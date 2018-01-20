"""UAT test file for Adventurer's Codex dm tabs."""

from components.dm.tabs import DMTabs


def test_navigate_tabs(dm_wizard, browser): # noqa
    """As a dm, I should be able to navigate through the dm tabs."""
    print('As a dm, I should be able to navigate through the dm tabs.')

    tabs = DMTabs(browser)

    tabs.overview.click()
    assert tabs.overview_label.text == 'Overview'

    tabs.encounters.click()
    assert tabs.encounters_label.text == 'Encounters'

    tabs.screen.click()
    assert tabs.screen_label.text == 'Screen'

    tabs.notes.click()
    assert tabs.notes_label.text == 'Notes'

    # TODO: add chat and chat after login fixture and party connection
    # testing is ready