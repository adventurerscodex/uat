"""UAT test file for Adventurer's Codex core player tools wizard."""
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from components.core.general.new_character_campaign import NewCharacterCampaign
from components.core.character import inventory
from components.core.character import wizard
from components.core.character.tabs import Tabs
from components.core.character.profile import Profile
from components.core.character.other_stats import OtherStats
from expected_conditions.conditions import table_has_data
from utils import general as ut


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

    with pytest.raises(NoSuchElementException):
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

    with pytest.raises(NoSuchElementException):
        browser.find_element_by_id('newCharCampaignNextButton')


def test_alignment_auto_complete(browser): # noqa
    """ As a player, when I start typing in the alignment field, OGL data auto-completes."""
    print('As a player, when I start typing in the alignment field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(
        who_are_you,
        'alignment',
        browser,
        has_search_term=False
    )

    assert who_are_you.alignment.get_attribute('value').strip() == 'Lawful good'


def test_race_auto_complete(browser): # noqa
    """As a player, when I start typing in the race field, OGL data auto-completes."""
    print('As a player, when I start typing in the race field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(
        who_are_you,
        'race',
        browser,
        has_search_term=False
    )

    assert who_are_you.race.get_attribute('value').strip() == 'Dwarf'


def test_class_auto_complete(browser): # noqa
    """As a player, when I start typing in the class field, OGL data auto-completes."""
    print('As a player, when I start typing in the class field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(
        who_are_you,
        'class_',
        browser,
        has_search_term=False
    )

    assert who_are_you.class_.get_attribute('value').strip() == 'Barbarian'


def test_background_auto_complete(browser): # noqa
    """As a player, when I start typing in the background field, OGL data auto-completes."""
    print('As a player, when I start typing in the background field, OGL data auto-completes.')

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    ut.select_from_autocomplete(
        who_are_you,
        'background',
        browser,
        has_search_term=False
    )

    assert who_are_you.background.get_attribute('value').strip() == 'Acolyte'


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

    assert ability_scores.strength.get_attribute('value').strip() == '18'
    assert ability_scores.dexterity.get_attribute('value').strip() == '18'
    assert ability_scores.constitution.get_attribute('value').strip() == '18'
    assert ability_scores.intelligence.get_attribute('value').strip() == '18'
    assert ability_scores.wisdom.get_attribute('value').strip() == '18'
    assert ability_scores.charisma.get_attribute('value').strip() == '18'

def test_wizard_profile_stats(browser): # noqa
    """As a player, after creating a character via the character creation wizard, I can view all
       the data entered in the stats and profile modules."""
    print(('As a player, after creating a character via the character creation wizard, I can '
           'view all the data entered in the stats and profile modules.'))
    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)
    ability_scores = wizard.AbilityScoresManual(browser)
    tabs = Tabs(browser)
    profile = Profile(browser)
    stats = OtherStats(browser)

    wizard_main.get_started.click()
    wizard_main.player.click()
    wizard_main.next_.click()

    who_are_you.character_name = 'Test Char'
    who_are_you.player_name = 'Automated Testing Bot.'
    ut.select_from_autocomplete(
        who_are_you,
        'alignment',
        browser,
        has_search_term=False
    )
    who_are_you.deity = 'Test Deity'
    ut.select_from_autocomplete(
        who_are_you,
        'race',
        browser,
        has_search_term=False
    )
    ut.select_from_autocomplete(
        who_are_you,
        'class_',
        browser,
        has_search_term=False
    )
    who_are_you.gender = 'Test Male'
    who_are_you.age = 21
    ut.select_from_autocomplete(
        who_are_you,
        'background',
        browser,
        has_search_term=False
    )
    who_are_you.level = 3
    who_are_you.experience = 1000

    wizard_main.next_.click()

    ability_scores.strength = '18'
    ability_scores.dexterity = '18'
    ability_scores.constitution = '18'
    ability_scores.intelligence = '18'
    ability_scores.wisdom = '18'
    ability_scores.charisma = '18'

    wizard_main.finish.click()

    tabs.profile.click()

    assert profile.name.get_attribute('value').strip() == 'Automated Testing Bot.'
    assert profile.background.get_attribute('value').strip() == 'Acolyte'
    assert profile.alignment.get_attribute('value').strip() == 'Lawful good'
    assert profile.deity.get_attribute('value').strip() == 'Test Deity'
    assert profile.race.get_attribute('value').strip() == 'Dwarf'
    assert profile.class_.get_attribute('value').strip() == 'Barbarian'
    assert profile.gender.get_attribute('value').strip() == 'Test Male'
    assert profile.age.get_attribute('value').strip() == '21'

    tabs.stats.click()

    assert stats.level.get_attribute('value') == '3'
    assert stats.experience.get_attribute('value') == '1000'

def test_wizard_backpack_prepop(browser): # noqa
    """As a player, after selecting a backpack, all items are pre-populated in the inventory
       module."""
    print(('As a player, after selecting a backpack, all items are pre-populated in the '
           'inventory module.'))

    wizard_main = NewCharacterCampaign(browser)
    who_are_you = wizard.WhoAreYou(browser)
    ability_scores = wizard.AbilityScoresManual(browser)
    tabs = Tabs(browser)
    inventory_table = inventory.InventoryTable(browser)

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.get_started_id)
        )
    )

    wizard_main.get_started.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.player_id)
        )
    )

    wizard_main.player.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.next_id)
        )
    )

    wizard_main.next_.click()

    who_are_you.character_name = 'Test Char'
    who_are_you.player_name = 'Automated Testing Bot.'

    backpack = Select(browser.find_element_by_id(who_are_you.backpack_id))
    backpack.select_by_index(1)

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, wizard_main.next_id)
        )
    )

    wizard_main.next_.click()

    ability_scores.strength = '18'
    ability_scores.dexterity = '18'
    ability_scores.constitution = '18'
    ability_scores.intelligence = '18'
    ability_scores.wisdom = '18'
    ability_scores.charisma = '18'

    wizard_main.finish.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, tabs.inventory_id)
        )
    )

    tabs.inventory.click()

    # Safari has known issue where selects not working
    # https://forums.developer.apple.com/message/184592#184592
    # Javascript example not working either
    if browser.name != 'safari':
        WebDriverWait(browser, 15).until(
            table_has_data(
                inventory_table,
            )
        )

        rows = ut.get_table_rows(inventory_table, 'table')

        assert rows[0].item.strip() == 'Backpack'
        assert rows[0].quantity.strip() == '1'
        assert rows[0].weight.strip() == '5 lbs.'
        assert rows[0].cost.strip() == '2 GP'
        assert rows[0].description.strip() == ''

        assert rows[1].item.strip() == 'Ball bearings (bag of 1000)'
        assert rows[2].item.strip() == 'Bell'
        assert rows[3].item.strip() == 'Candle'
        assert rows[4].item.strip() == 'Crowbar'
        assert rows[5].item.strip() == 'Hammer'
        assert rows[6].item.strip() == 'Lantern hooded'
        assert rows[7].item.strip() == 'Oil (flask)'
        assert rows[8].item.strip() == 'Piton'
        assert rows[9].item.strip() == 'Rations (1 day)'
        assert rows[10].item.strip() == 'Rope hempen (50 feet)'
        assert rows[11].item.strip() == 'String (10 feet)'
        assert rows[12].item.strip() == 'Tinderbox'

        assert rows[13].item.strip() == 'Waterskin'
        assert rows[13].quantity.strip() == '1'
        assert rows[13].weight.strip() == '5 lbs.'
        assert rows[13].cost.strip() == '2 SP'
        assert rows[13].description.strip() == '(full)'
