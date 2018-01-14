"""UAT test file for Adventurer's Codex player tools profile module."""

from utils import utils as ut


def test_player_profile(player_wizard, browser):
    """As a player, all fields are editable and persist after refreshing the browser."""
    print('As a player, all fields are editable and persist after refreshing the browser.')

    ut.switch_tabs('profile', browser)
    ut.clear_input_value('Player Name', browser)
    ut.set_input_value_assert_persists('Player Name', 'Testing Bot', browser)
    ut.set_input_value_assert_persists('Background', 'Sage', browser)
    ut.set_input_value_assert_persists('Alignment', 'Chaotic Good', browser)
    ut.set_input_value_assert_persists('Deity', 'Moridin', browser)
    ut.set_input_value_assert_persists('Race', 'Elf', browser)
    ut.set_input_value_assert_persists('Class', 'Fighter', browser)
    ut.set_input_value_assert_persists('Gender', 'Male', browser)
    ut.set_input_value_assert_persists('Age', '22', browser)
    ut.set_input_value_assert_persists('Height', '5ft', browser)
    ut.set_input_value_assert_persists('Weight', '122', browser)
    ut.set_input_value_assert_persists('Hair Color', 'Brown', browser)
    ut.set_input_value_assert_persists('Eye Color', 'Brown', browser)
    ut.set_input_value_assert_persists('Skin Color', 'Fair', browser)

    ut.set_textarea_assert_persists('Personality Traits:', 'Jerk', browser)
    ut.set_textarea_assert_persists('Ideals:', 'Visionary', browser)
    ut.set_textarea_assert_persists('Bonds:', 'Nope', browser)
    ut.set_textarea_assert_persists('Flaws:', 'Not funny', browser)
