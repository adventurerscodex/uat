"""UAT test file for Adventurer's Codex dm tools overview module."""

from utils import utils as ut


def test_campaign_info(dm_wizard, browser):
    """Campaign info is editable and persists."""
    print('Campaign info is editable and persists.')

    ut.set_input_value_assert_persists('Setting', 'The Lost World', browser)
    ut.clear_input_value('DM Name', browser)
    ut.set_input_value_assert_persists(
        'DM Name', 'Automated Testing Bot', browser
    )
