"""UAT test file for Adventurer's Codex core dm tools."""

from utils import utils as ut


def test_dm_wizard(browser):
    """Test dm wizard using required values."""
    print('A dm should be able to navigate through the dm wizard.')

    # Get started with the wizard
    ut.click_button('Get Started', browser)

    # Select type player
    ut.click_radio('dmPlayerType', browser)

    # Navigate to the next step
    ut.click_button('Next', browser)

    # Input required fields
    ut.set_input_value('Campaign Name', 'Test Campaign', browser)
    ut.set_input_value('Player Name', 'Automated Testing Bot.', browser)

    # Finish the wizard
    ut.click_button('Finish', browser)
