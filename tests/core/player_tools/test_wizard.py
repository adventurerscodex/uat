"""UAT test file for Adventurer's Codex core player tools wizard."""
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC # noqa

from components.core.general.new_character_campaign import NewCharacterCampaign
from components.core.character import wizard


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
