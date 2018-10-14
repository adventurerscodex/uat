"""UAT test file for Adventurer's Codex dm tools overview module."""
from selenium.webdriver.common.keys import Keys

from components.core.dm.overview import DMOverview


def test_campaign_info(dm_wizard, browser):
    """Campaign info is editable and persists."""
    print('Campaign info is editable and persists.')

    dm_overview = DMOverview(browser)

    dm_overview.edit_btn.click()
    dm_overview.setting_input = 'The Lost World'
    dm_overview.setting_input.send_keys(Keys.TAB)
    dm_overview.save_btn.click()
    browser.refresh()

    assert dm_overview.setting_label.text.strip() == 'The Lost World'

    dm_overview.edit_btn.click()
    dm_overview.dm_name_input = 'Automated Testing Bot'
    dm_overview.dm_name_input.send_keys(Keys.TAB)
    dm_overview.save_btn.click()
    browser.refresh()

    assert dm_overview.dm_name_label.text.strip() == 'Automated Testing Bot'
