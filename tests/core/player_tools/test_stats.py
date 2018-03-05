"""UAT test file for Adventurer's Codex player tools stats module."""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character.ability_scores import AbilityScoresEditModal, AbilityScoresTable
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
