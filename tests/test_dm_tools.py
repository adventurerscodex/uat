"""UAT test suite for Adventurer's Codex core dm tools.."""

from utils import click_link, click_button, click_radio
from utils import set_input_value


def test_dm_wizard(browser):
    """Test dm wizard using required values."""
    print('A dm should be able to navigate through the dm wizard.')

    # AC homepage
    click_link('Start Playing', browser)

    # Get started with the wizard
    click_button('Get Started', browser)

    # Select type player
    click_radio('dmPlayerType', browser)

    # Navigate to the next step
    click_button('Next', browser)

    # Input required fields
    set_input_value('Campaign Name', 'Test Campaign', browser)
    set_input_value('Player Name', 'Automated Testing Bot.', browser)

    # Finish the wizard
    click_button('Finish', browser)