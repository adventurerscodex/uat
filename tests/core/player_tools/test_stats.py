"""UAT test file for Adventurer's Codex player tools stats module."""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character.ability_scores import AbilityScoresEditModal, AbilityScoresTable
from components.core.character.health import HitPointHitDice, HitPointEditModal
from components.core.character.other_stats import OtherStats
from components.core.character.saving_throw import SavingThrowEditModal, SavingThrowTable
from components.core.character.tabs import Tabs
from expected_conditions.conditions import url_in_new_tab_matches


def test_edit_ability_scores(player_wizard, browser): # noqa
    """As a player, I can edit my ability scores."""
    print('As a player, I can edit my ability scores.')
    ability_scores_edit = AbilityScoresEditModal(browser)
    ability_scores_table = AbilityScoresTable(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    ability_scores_table.table.click()
    ability_scores_edit.strength = 15
    ability_scores_edit.dexterity = 16
    ability_scores_edit.constitution = 17
    ability_scores_edit.intelligence = 16
    ability_scores_edit.wisdom = 15
    ability_scores_edit.charisma = 14

    ability_scores_edit.done.click()

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, ability_scores_table.strength.get_attribute('id')),
            '15'
        )
    )

    assert ability_scores_table.strength.text == '15'
    assert ability_scores_table.dexterity.text == '16'
    assert ability_scores_table.constitution.text == '17'
    assert ability_scores_table.intelligence.text == '16'
    assert ability_scores_table.wisdom.text == '15'
    assert ability_scores_table.charisma.text == '14'


def test_ability_scores_modifiers(player_wizard, browser): # noqa
    """As a player, I can view my ability score modifiers."""
    print('As a player, I can view my ability score modifiers.')
    ability_scores_edit = AbilityScoresEditModal(browser)
    ability_scores_table = AbilityScoresTable(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    ability_scores_table.table.click()
    ability_scores_edit.strength = 15
    ability_scores_edit.dexterity = 16
    ability_scores_edit.constitution = 17
    ability_scores_edit.intelligence = 16
    ability_scores_edit.wisdom = 15
    ability_scores_edit.charisma = 14

    ability_scores_edit.done.click()

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, ability_scores_table.strength.get_attribute('id')),
            '15'
        )
    )

    assert ability_scores_table.strength_modifier.text == '+ 2'
    assert ability_scores_table.dexterity_modifier.text == '+ 3'
    assert ability_scores_table.constitution_modifier.text == '+ 3'
    assert ability_scores_table.intelligence_modifier.text == '+ 3'
    assert ability_scores_table.wisdom_modifier.text == '+ 2'
    assert ability_scores_table.charisma_modifier.text == '+ 2'


def test_ability_scores_persist(player_wizard, browser): # noqa
    """As a player, ability scores persist after page refresh."""
    print('As a player, ability scores persist after page refresh.')
    ability_scores_edit = AbilityScoresEditModal(browser)
    ability_scores_table = AbilityScoresTable(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    ability_scores_table.table.click()
    ability_scores_edit.strength = 15
    ability_scores_edit.dexterity = 16
    ability_scores_edit.constitution = 17
    ability_scores_edit.intelligence = 16
    ability_scores_edit.wisdom = 15
    ability_scores_edit.charisma = 14

    ability_scores_edit.done.click()

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, ability_scores_table.strength.get_attribute('id')),
            '15'
        )
    )

    browser.refresh()

    assert ability_scores_table.strength.text == '15'
    assert ability_scores_table.dexterity.text == '16'
    assert ability_scores_table.constitution.text == '17'
    assert ability_scores_table.intelligence.text == '16'
    assert ability_scores_table.wisdom.text == '15'
    assert ability_scores_table.charisma.text == '14'

def test_hp_stepper(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my hit points via the stepper widget."""
    print('As a player, I can increase or decrease my hit points via the stepper widget.')
    hp_hd = HitPointHitDice(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    hp_hd.damage_up.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 9'

    hp_hd.damage_down.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 10'

def test_hp_reset(player_wizard, browser): # noqa
    """As a player, I can reset my hp by clicking on the reset icon."""
    print('As a player, I can reset my hp by clicking on the reset icon.')
    hp_hd = HitPointHitDice(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    hp_hd.damage_up.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 9'

    hp_hd.reset.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 10'

def test_initiative_calculation(player_wizard, browser): # noqa
    """As a player, initiative is correctly calculated."""
    print('As a player, initiative is correctly calculated.')
    other_stats = OtherStats(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    assert other_stats.initiative.text == '4'

def test_initiative_modifier(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my calculated initiative via a modifier field and this is reflected in the label."""
    print('As a player, I can increase or decrease my calculated initiative via a modifier field and this is reflected in the label.')
    other_stats = OtherStats(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    other_stats.initiative_modifier = 1
    other_stats.initiative_modifier.send_keys(Keys.TAB)

    assert other_stats.initiative.text == '5'

    other_stats.initiative_modifier = -1

    assert other_stats.initiative.text == '4'

def test_initiative_popover(player_wizard, browser): # noqa
    """As a player, I can can click on a popover showing the calculation for Initiative."""
    print('As a player, I can can click on a popover showing the calculation for Initiative.')
    other_stats = OtherStats(browser)

    tabs = Tabs(browser)
    tabs.stats.click()

    other_stats.initiative_popover_icon.click()

    assert other_stats.initiative_popover_content.text == 'Initiative = Dexterity Modifier + Modifier\nInitiative = 4 + 0'
