"""UAT test file for Adventurer's Codex dm tools overview module."""
from selenium.webdriver.common.keys import Keys

from components.core.dm.overview import DMOverview


def test_campaign_info(dm_wizard, browser):
    """Campaign info is editable and persists."""
    print('Campaign info is editable and persists.')

    dm_overview = DMOverview(browser)

    dm_overview.setting = 'The Lost World'
    dm_overview.setting.send_keys(Keys.TAB)
    browser.refresh()

    assert dm_overview.setting.get_attribute('value').strip() == 'The Lost World'

    dm_overview.dm_name = 'Automated Testing Bot'
    dm_overview.dm_name.send_keys(Keys.TAB)
    browser.refresh()

    assert dm_overview.dm_name.get_attribute('value').strip() == 'Automated Testing Bot'
