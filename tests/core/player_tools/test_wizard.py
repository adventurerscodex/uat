"""UAT test file for Adventurer's Codex core player tools wizard."""
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC # noqa

from components.core.general.new_character_campaign import NewCharacterCampaign
from components.core.character import wizard
from utils import utils as ut


def test_player_wizard(browser):
    """A user should be able to navigate through the player wizard."""
    print('As a player, I should be able to navigate through the player wizard.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)
    ability_scores = wizard.AbilityScoresManual(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    who_are_you.character_name = 'Test Char'
    who_are_you.player_name = 'Automated Testing Bot.'

    wizard_main.next_.click()

    ability_scores.strength = '18'
    ability_scores.dexterity = '18'
    ability_scores.constitution = '18'
    ability_scores.intelligence = '18'
    ability_scores.wisdom = '18'
    ability_scores.charisma = '18'

    wizard_main.finish.click()


def test_attributes_required(browser):
    """A user should be required to add attribute values."""
    print('As a player, I should be required to add attribute values.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)
    ability_scores = wizard.AbilityScoresManual(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    who_are_you.character_name = 'Test Char'
    who_are_you.player_name = 'Automated Testing Bot.'

    wizard_main.next_.click()

    assert ability_scores.strength_required.is_displayed()
    assert ability_scores.dexterity_required.is_displayed()
    assert ability_scores.constitution_required.is_displayed()
    assert ability_scores.intelligence_required.is_displayed()
    assert ability_scores.wisdom_required.is_displayed()
    assert ability_scores.charisma_required.is_displayed()

    with pytest.raises(NoSuchElementException) as excinfo:
        browser.find_element_by_id('newCharCampaignFinishButton')


def test_name_required(browser):
    """A user should be required to enter a char and player name."""
    print('As a player, I should be required to enter a char and player name.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    assert who_are_you.character_name_required.is_displayed()
    assert who_are_you.player_name_required.is_displayed()

    with pytest.raises(NoSuchElementException) as excinfo:
        browser.find_element_by_id('newCharCampaignNextButton')


def test_alignment_auto_complete(browser): # noqa
    """ As a player, when I start typing in the alignment field, OGL data auto-completes."""
    print('As a player, when I start typing in the alignment field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(who_are_you, 'alignment', '', browser)

    assert who_are_you.alignment.get_attribute('value') == 'Lawful good'


def test_race_auto_complete(browser): # noqa
    """As a player, when I start typing in the race field, OGL data auto-completes."""
    print('As a player, when I start typing in the race field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(who_are_you, 'race', '', browser)

    assert who_are_you.race.get_attribute('value') == 'Dwarf'


def test_class_auto_complete(browser): # noqa
    """As a player, when I start typing in the class field, OGL data auto-completes."""
    print('As a player, when I start typing in the class field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(who_are_you, 'class_', '', browser)

    assert who_are_you.class_.get_attribute('value') == 'Barbarian'


def test_background_auto_complete(browser): # noqa
    """As a player, when I start typing in the background field, OGL data auto-completes."""
    print('As a player, when I start typing in the background field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(who_are_you, 'background', '', browser)

    assert who_are_you.background.get_attribute('value') == 'Acolyte'


def test_add_ability_scores(browser): # noqa
    """As a player, I can add values to all my ability scores."""
    print('As a player, I can add values to all my ability scores.')

    wizard_main = NewCharacterCampaign(browser)
    ability_scores = wizard.AbilityScoresManual(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    who_are_you.character_name = 'Test Char'
    who_are_you.player_name = 'Automated Testing Bot.'
    wizard_main.next_.click()

    ability_scores.strength = '18'
    ability_scores.dexterity = '18'
    ability_scores.constitution = '18'
    ability_scores.intelligence = '18'
    ability_scores.wisdom = '18'
    ability_scores.charisma = '18'

    assert ability_scores.strength.get_attribute('value') == '18'
    assert ability_scores.dexterity.get_attribute('value') == '18'
    assert ability_scores.constitution.get_attribute('value') == '18'
    assert ability_scores.intelligence.get_attribute('value') == '18'
    assert ability_scores.wisdom.get_attribute('value') == '18'
    assert ability_scores.charisma.get_attribute('value') == '18'
