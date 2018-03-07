"""UAT test file for Adventurer's Codex player tools stats module."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character.ability_scores import AbilityScoresEditModal, AbilityScoresTable
from components.core.character.health import HitPointHitDice, HitPointEditModal
from components.core.character.other_stats import OtherStats
from components.core.character.profile_picture import ProfilePicture
from components.core.character.saving_throw import SavingThrowEditModal, SavingThrowTable


def test_edit_ability_scores(player_wizard, browser): # noqa
    """As a player, I can edit my ability scores."""
    print('As a player, I can edit my ability scores.')
    ability_scores_edit = AbilityScoresEditModal(browser)
    ability_scores_table = AbilityScoresTable(browser)

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

    hp_hd.damage_up.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 9'

    hp_hd.damage_down.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 10'

def test_hp_reset(player_wizard, browser): # noqa
    """As a player, I can reset my hp by clicking on the reset icon."""
    print('As a player, I can reset my hp by clicking on the reset icon.')
    hp_hd = HitPointHitDice(browser)

    hp_hd.damage_up.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 9'

    hp_hd.reset.click()

    assert hp_hd.hit_points_bar_label.text == 'HP: 10'

def test_initiative_calculation(player_wizard, browser): # noqa
    """As a player, initiative is correctly calculated."""
    print('As a player, initiative is correctly calculated.')
    other_stats = OtherStats(browser)

    assert other_stats.initiative.text == '4'

def test_initiative_modifier(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my calculated initiative via a modifier field and this is reflected in the label."""
    print('As a player, I can increase or decrease my calculated initiative via a modifier field and this is reflected in the label.')
    other_stats = OtherStats(browser)

    other_stats.initiative_modifier = 1
    other_stats.initiative_modifier.send_keys(Keys.TAB)

    assert other_stats.initiative.text == '5'

    other_stats.initiative_modifier = -1

    assert other_stats.initiative.text == '4'

def test_initiative_popover(player_wizard, browser): # noqa
    """As a player, I can can click on a popover showing the calculation for Initiative."""
    print('As a player, I can can click on a popover showing the calculation for Initiative.')
    other_stats = OtherStats(browser)

    other_stats.initiative_popover_icon.click()

    assert other_stats.initiative_popover_content.text == 'Initiative = Dexterity Modifier + Modifier\nInitiative = 4 + 0'

def test_proficieny_bonus_calculation(player_wizard, browser): # noqa
    """As a player, proficieny bonus is correctly calculated."""
    print('As a player, proficieny bonus is correctly calculated.')
    other_stats = OtherStats(browser)

    other_stats.level = 5
    other_stats.level.send_keys(Keys.TAB)

    assert other_stats.proficiency_bonus.text == '3'

def test_proficiency_modifier(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my calculated proficiency via a modifier field and this is reflected in the label."""
    print('As a player, I can increase or decrease my calculated proficiency via a modifier field and this is reflected in the label.')
    other_stats = OtherStats(browser)

    other_stats.level = 5
    other_stats.level.send_keys(Keys.TAB)

    other_stats.proficiency_bonus_modifier = 1
    other_stats.proficiency_bonus_modifier.send_keys(Keys.TAB)

    assert other_stats.proficiency_bonus.text == '4'

def test_proficiency_popover(player_wizard, browser): # noqa
    """As a player, I can can click on a popover showing the calculation for Proficiency Bonus."""
    print('As a player, I can can click on a popover showing the calculation for Proficiency Bonus.')
    other_stats = OtherStats(browser)

    other_stats.proficiency_popover_icon.click()

    assert other_stats.proficiency_popover_content.text == 'Proficiency = (Level / 4) + 1 + Modifier\nProficiency = 1 + 1 + 0'

def test_inpiration_blue_circle(player_wizard, browser): # noqa
    """As a player, if I am inspired, there should be a blue circle around my profice pic."""
    print('As a player, if I am inspired, there should be a blue circle around my profice pic.')
    other_stats = OtherStats(browser)
    profile_pic = ProfilePicture(browser)

    other_stats.inspiration = 1
    other_stats.inspiration.send_keys(Keys.TAB)

    assert 'image-border-inspired' in profile_pic.profile_pic_border.get_attribute('class')

def test_health_bar_changes_color(player_wizard, browser): # noqa
    """As a player, I can see the hit points bar change colors at certain intervals as hit points decrease."""
    print('As a player, I can see the hit points bar change colors at certain intervals as hit points decrease.')
    health = HitPointHitDice(browser)

    assert 'progress-bar-danger' not in health.hit_points_bar_regular_hp.get_attribute('class')

    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()

    assert 'progress-bar-danger' in health.hit_points_bar_regular_hp.get_attribute('class')
