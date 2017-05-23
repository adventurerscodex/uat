"""UAT test suite for Adventurer's Codex core player tools."""

from utils import click_link, click_button, click_radio
from utils import set_input_value


def test_player_wizard(browser):
    """Test player wizard using required values."""
    print('A user should be able to navigate through the player wizard.')

    # AC homepage
    click_link('Start Playing', browser)

    # Get started with the wizard
    click_button('Get Started', browser)

    # Select type player
    click_radio('characterPlayerType', browser)

    # Navigate to the next step
    click_button('Next', browser)

    # Input required fields
    set_input_value('Character Name', 'Test Char', browser)
    set_input_value('Player Name', 'Automated Testing Bot.', browser)

    # Navigate to the next
    click_button('Next', browser)

    # Fill in values for attributes
    set_input_value('Strength', '18', browser)
    set_input_value('Dexterity', '18', browser)
    set_input_value('Constitution', '18', browser)
    set_input_value('Intelligence', '18', browser)
    set_input_value('Wisdom', '18', browser)
    set_input_value('Charisma', '18', browser)

    # Finish the wizard
    click_button('Finish', browser)
