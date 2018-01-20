"""UAT test file for Adventurer's Codex dm tools overview module."""

from components.dm.overview import DMOverview


def test_campaign_info(dm_wizard, browser):
    """Campaign info is editable and persists."""
    print('Campaign info is editable and persists.')

    dm_overview = DMOverview(browser)
    dm_overview.dm_name.clear()

    dm_overview.setting = 'The Lost World\t'
    browser.refresh()
    assert dm_overview.setting.get_attribute('value') == 'The Lost World'

    dm_overview.dm_name = 'Automated Testing Bot\t'
    browser.refresh()
    assert dm_overview.dm_name.get_attribute('value') == 'Automated Testing Bot'
