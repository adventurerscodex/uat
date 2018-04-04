"""Test dm screen."""

from components.core.dm.screen import Screen
from components.core.dm.tabs import DMTabs


def test_screen(dm_wizard, browser): # noqa
    """As a dm, I can view the dm screen sections."""
    print('As a dm, I can view the dm screen sections.')
    screen = Screen(browser)

    tabs = DMTabs(browser)
    tabs.screen.click()

    assert 'Cover' in screen.cover_heading.text.strip()
    assert 'Travel' in screen.travel_pace_heading.text.strip()
    assert 'Conditions' in screen.conditions_heading.text.strip()
    assert 'Light' in screen.light_heading.text.strip()
    assert 'Difficulty' in screen.difficulty_classes_heading.text.strip()
    assert 'Exhaustion' in screen.exhaustion_heading.text.strip()
