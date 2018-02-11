"""UAT test file for Adventurer's Codex player tools spells module."""
from components.core.character.spells import SpellStatsEdit



def test_navigate_spells(player_wizard, browser): # noqa
    """As a player, spell stats can be added, deleted, and edited"""
    print('As a player, spell stats can be added, deleted, and edited')

    spells = SpellStatsEdit(browser)

    spells.spell_Stats_Table.click()

    spells.spell_attack_bonus.click()
    assert tabs.stats_label.text == '1'
