"""UAT test file for Adventurer's Codex player tools stats module."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character.ability_scores import AbilityScoresEditModal, AbilityScoresTable
from components.core.character.health import HitPointHitDice
from components.core.character.other_stats import OtherStats
from components.core.character.profile_picture import ProfilePicture
from components.core.character.saving_throw import SavingThrowEditModal, SavingThrowTable
from conftest import DEFAULT_WAIT_TIME
from expected_conditions.general import modal_finished_closing
from expected_conditions.general import table_cell_updated
from utils import general as ut

def test_data_persists(player_wizard, browser): # noqa
    """As a player, all changes I make to hit points, hit dice, ability scores,
       savings throws, and other stats persist after I refresh the browser."""

    print(('As a player, all changes I make to hit points, hit dice, ability '
           'scores, savings throws, and other stats persist after I refresh '
           ' the browser.'))

    ability_scores_edit = AbilityScoresEditModal(browser)
    ability_scores_table = AbilityScoresTable(browser)
    hp_hd = HitPointHitDice(browser)
    other_stats = OtherStats(browser)
    saving_throw = SavingThrowTable(browser)
    saving_throw_edit = SavingThrowEditModal(browser)

    ability_scores_table.table.click()
    ability_scores_edit.strength = 15
    ability_scores_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        modal_finished_closing()
    )

    hp_hd.damage_up.click()

    hp_hd.hitdice1.click()

    row = ut.get_table_row(saving_throw, 'table', values=False)
    # open edit modal
    row[0].click()
    saving_throw_edit.modifier = 1
    saving_throw_edit.proficiency.click()
    saving_throw_edit.done.click()

    other_stats.ac_modifier = 1
    other_stats.ac_modifier.send_keys(Keys.TAB)

    other_stats.initiative_modifier = 1
    other_stats.initiative_modifier.send_keys(Keys.TAB)

    other_stats.proficiency_bonus_modifier = 1
    other_stats.proficiency_bonus_modifier.send_keys(Keys.TAB)

    other_stats.speed = 40
    other_stats.speed.send_keys(Keys.TAB)

    other_stats.level = 3
    other_stats.level.send_keys(Keys.TAB)

    other_stats.experience = 2000
    other_stats.experience.send_keys(Keys.TAB)

    browser.refresh()

    row = ut.get_table_row(saving_throw, 'table', values=False)
    proficieny = row[0].find_elements(By.TAG_NAME, 'span')

    charisma = ut.get_table_row(saving_throw, 'table')

    assert ability_scores_table.strength.text.strip() == '15'
    assert hp_hd.hit_points_bar_label.text.strip() == 'HP: 9'
    assert hp_hd.hitdice1.get_attribute('class').strip() == 'dice-empty'
    assert charisma.blank2.strip() == '+ 8'
    assert proficieny[0].get_attribute('class').strip() == 'fa fa-check'
    assert other_stats.initiative.text.strip() == '5'
    assert other_stats.proficiency_bonus.text.strip() == '3'
    assert other_stats.speed.get_attribute('value').strip() == '40'
    assert other_stats.level.get_attribute('value').strip() == '3'
    assert other_stats.experience.get_attribute('value').strip() == '2000'

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

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.ID, ability_scores_table.strength.get_attribute('id')),
            '15'
        )
    )

    assert ability_scores_table.strength.text.strip() == '15'
    assert ability_scores_table.dexterity.text.strip() == '16'
    assert ability_scores_table.constitution.text.strip() == '17'
    assert ability_scores_table.intelligence.text.strip() == '16'
    assert ability_scores_table.wisdom.text.strip() == '15'
    assert ability_scores_table.charisma.text.strip() == '14'


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

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.ID, ability_scores_table.strength.get_attribute('id')),
            '15'
        )
    )

    assert ability_scores_table.strength_modifier.text.strip() == '+ 2'
    assert ability_scores_table.dexterity_modifier.text.strip() == '+ 3'
    assert ability_scores_table.constitution_modifier.text.strip() == '+ 3'
    assert ability_scores_table.intelligence_modifier.text.strip() == '+ 3'
    assert ability_scores_table.wisdom_modifier.text.strip() == '+ 2'
    assert ability_scores_table.charisma_modifier.text.strip() == '+ 2'


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

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.text_to_be_present_in_element(
            (By.ID, ability_scores_table.strength.get_attribute('id')),
            '15'
        )
    )

    browser.refresh()

    assert ability_scores_table.strength.text.strip() == '15'
    assert ability_scores_table.dexterity.text.strip() == '16'
    assert ability_scores_table.constitution.text.strip() == '17'
    assert ability_scores_table.intelligence.text.strip() == '16'
    assert ability_scores_table.wisdom.text.strip() == '15'
    assert ability_scores_table.charisma.text.strip() == '14'

def test_hp_stepper(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my hit points via the stepper
       widget."""
    print(('As a player, I can increase or decrease my hit points via the '
           'stepper widget.'))

    hp_hd = HitPointHitDice(browser)

    hp_hd.damage_up.click()

    assert hp_hd.hit_points_bar_label.text.strip() == 'HP: 9'

    hp_hd.damage_down.click()

    assert hp_hd.hit_points_bar_label.text.strip() == 'HP: 10'

def test_hp_reset(player_wizard, browser): # noqa
    """As a player, I can reset my hp by clicking on the reset icon."""
    print('As a player, I can reset my hp by clicking on the reset icon.')

    hp_hd = HitPointHitDice(browser)

    hp_hd.damage_up.click()

    assert hp_hd.hit_points_bar_label.text.strip() == 'HP: 9'

    hp_hd.reset.click()

    assert hp_hd.hit_points_bar_label.text.strip() == 'HP: 10'

def test_hit_dice_clickable(player_wizard, browser): # noqa
    """As a player, hit dice are clickable and images change when clicked."""

    print(('As a player, hit dice are clickable and images change when '
           'clicked.'))

    hp_hd = HitPointHitDice(browser)

    assert hp_hd.hitdice1.get_attribute('class').strip() == 'dice-full'

    hp_hd.hitdice1.click()

    assert hp_hd.hitdice1.get_attribute('class').strip() == 'dice-empty'

def test_hit_dice_persists(player_wizard, browser): # noqa
    """As a player, if I click on a hit die, the changes persist after I
       refresh the browser."""

    print(('As a player, if I click on a hit die, the changes persist after I '
           'refresh the browser.'))

    hp_hd = HitPointHitDice(browser)
    hp_hd.hitdice1.click()

    assert hp_hd.hitdice1.get_attribute('class').strip() == 'dice-empty'

    browser.refresh()

    assert hp_hd.hitdice1.get_attribute('class').strip() == 'dice-empty'

def test_hit_dice_level(player_wizard, browser): # noqa
    """As a player, if I change the value in the level field, the number of
       hit dice match the level number."""

    print(('As a player, if I change the value in the level field, the number '
           'of hit dice match the level number.'))

    hp_hd = HitPointHitDice(browser)
    other_stats = OtherStats(browser)

    other_stats.level = 3
    other_stats.level.send_keys(Keys.TAB)

    hit_dice_count = len(hp_hd.hit_dice_list.find_elements_by_tag_name('span'))

    assert hit_dice_count == 3

def test_death_saves_clickable(player_wizard, browser): # noqa
    """As a player, death save successes and failures are clickable and images
       change when clicked."""

    print(('As a player, death save successes and failures are clickable and '
           'images change when clicked.'))

    hp_hd = HitPointHitDice(browser)

    # reduce character to 0 hit points
    for _ in range(10):
        hp_hd.damage_up.click()

    success = hp_hd.death_successes_empty[0]
    success.click()

    failure = hp_hd.death_failures_empty[0]
    failure.click()

    assert success.get_attribute('class').strip() == 'ds-success-full'
    assert failure.get_attribute('class').strip() == 'ds-failure-full'

def test_death_saves_persist(player_wizard, browser): # noqa
    """As a player, death save changes persist after I refresh the browser."""

    print(('As a player, death save changes persist after I refresh the '
           'browser.'))

    hp_hd = HitPointHitDice(browser)

    # reduce character to 0 hit points
    for _ in range(10):
        hp_hd.damage_up.click()

    success = hp_hd.death_successes_empty[0]
    success.click()

    failure = hp_hd.death_failures_empty[0]
    failure.click()

    browser.refresh()

    assert len(hp_hd.death_successes_empty) == 2
    assert len(hp_hd.death_failures_empty) == 2

def test_character_stable_alert(player_wizard, browser): # noqa
    """If 3 death save success are clicked, an alert indicating the player is
       stable is presented."""

    print(('If 3 death save success are clicked, an alert indicating the '
           'player is stable is presented.'))

    hp_hd = HitPointHitDice(browser)

    # reduce character to 0 hit points
    for _ in range(10):
        hp_hd.damage_up.click()

    successes = hp_hd.death_successes_empty
    successes[0].click()
    successes[1].click()
    successes[2].click()

    assert hp_hd.toast_title.text.strip() == 'You are now stable.'
    assert hp_hd.toast_message.text.strip() == 'You have been spared...for now.'

def test_character_dead_alert(player_wizard, browser): # noqa
    """If 3 death save success are clicked, an alert indicating the player is
       dead is presented."""

    print(('If 3 death save success are clicked, an alert indicating the '
           'player is dead is presented.'))

    hp_hd = HitPointHitDice(browser)

    # reduce character to 0 hit points
    for _ in range(10):
        hp_hd.damage_up.click()

    failures = hp_hd.death_failures_empty
    failures[0].click()
    failures[1].click()
    failures[2].click()

    assert hp_hd.toast_title.text.strip() == 'You have died.'
    assert hp_hd.toast_message.text.strip() == 'Failing all 3 death saves will do that...'

def test_initiative_calculation(player_wizard, browser): # noqa
    """As a player, initiative is correctly calculated."""
    print('As a player, initiative is correctly calculated.')

    other_stats = OtherStats(browser)

    assert other_stats.initiative.text.strip() == '4'

def test_initiative_modifier(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my calculated initiative via a
       modifier field and this is reflected in the label."""
    print(('As a player, I can increase or decrease my calculated initiative '
           'via a modifier field and this is reflected in the label.'))

    other_stats = OtherStats(browser)

    other_stats.initiative_modifier = 1
    other_stats.initiative_modifier.send_keys(Keys.TAB)

    assert other_stats.initiative.text.strip() == '5'

    other_stats.initiative_modifier = -1
    other_stats.initiative_modifier.send_keys(Keys.TAB)

    assert other_stats.initiative.text.strip() == '3'

def test_initiative_popover(player_wizard, browser): # noqa
    """As a player, I can can click on a popover showing the calculation
       for Initiative."""
    print(('As a player, I can can click on a popover showing the calculation '
           'for Initiative.'))

    other_stats = OtherStats(browser)

    other_stats.initiative_popover_icon.click()

    # safari has no newline, so it must be stripped
    popover = other_stats.initiative_popover_content.text.strip()
    popover = popover.replace('\n', '')

    assert popover == 'Initiative = Dexterity Modifier + ModifierInitiative = 4 + 0'

def test_proficieny_bonus_calculation(player_wizard, browser): # noqa
    """As a player, proficieny bonus is correctly calculated."""
    print('As a player, proficieny bonus is correctly calculated.')

    other_stats = OtherStats(browser)

    other_stats.level = 5
    other_stats.level.send_keys(Keys.TAB)

    assert other_stats.proficiency_bonus.text.strip() == '3'

def test_proficiency_modifier(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my calculated proficiency via
       a modifier field and this is reflected in the label."""
    print(('As a player, I can increase or decrease my calculated proficiency '
           'via a modifier field and this is reflected in the label.'))

    other_stats = OtherStats(browser)

    other_stats.level = 5
    other_stats.level.send_keys(Keys.TAB)

    other_stats.proficiency_bonus_modifier = 1
    other_stats.proficiency_bonus_modifier.send_keys(Keys.TAB)

    assert other_stats.proficiency_bonus.text.strip() == '4'

def test_proficiency_popover(player_wizard, browser): # noqa
    """As a player, I can can click on a popover showing the calculation for
       Proficiency Bonus."""
    print(('As a player, I can can click on a popover showing the calculation '
           'for Proficiency Bonus.'))

    other_stats = OtherStats(browser)

    other_stats.proficiency_popover_icon.click()

    # safari has no newline, so it must be stripped
    popover = other_stats.proficiency_popover_content.text.strip()
    popover = popover.replace('\n', '')

    assert popover == 'Proficiency = (Level / 4) + 1 + ModifierProficiency = 1 + 1 + 0'

def test_inpiration_blue_circle(player_wizard, browser): # noqa
    """As a player, if I am inspired, there should be a blue circle around my
       profice pic."""
    print(('As a player, if I am inspired, there should be a blue circle '
           'around my profice pic.'))

    other_stats = OtherStats(browser)
    profile_pic = ProfilePicture(browser)

    other_stats.inspiration = 1
    other_stats.inspiration.send_keys(Keys.TAB)

    assert 'image-border-inspired' in profile_pic.profile_pic_border.get_attribute('class').strip()

def test_health_bar_changes_color(player_wizard, browser): # noqa
    """As a player, I can see the hit points bar change colors at certain
       intervals as hit points decrease."""
    print(('As a player, I can see the hit points bar change colors at '
           'certain intervals as hit points decrease.'))

    health = HitPointHitDice(browser)

    hp_bar_class = health.hit_points_bar_regular_hp.get_attribute('class').strip()
    assert 'progress-bar-danger' not in hp_bar_class

    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()
    health.damage_up.click()

    assert 'progress-bar-danger' in health.hit_points_bar_regular_hp.get_attribute('class').strip()

def test_ac_modifier(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my calculated armor class via
       a modifier field and this is reflected in the label."""
    print(('As a player, I can increase or decrease my calculated armor class '
           'via a modifier field and this is reflected in the label.'))

    other_stats = OtherStats(browser)

    other_stats.ac_modifier = 1
    other_stats.ac_modifier.send_keys(Keys.TAB)

    assert other_stats.ac.text.strip() == '15'

def test_ac_popover(player_wizard, browser): # noqa
    """As a player, I can can click on a popover showing the calculation for
       Armor Class."""
    print(('As a player, I can can click on a popover showing the calculation '
           'for Armor Class.'))

    other_stats = OtherStats(browser)

    other_stats.ac_popover_icon.click()

    # safari has no newline, so it must be stripped
    popover = other_stats.proficiency_popover_content.text.strip()
    popover = popover.replace('\n', '')

    assert popover == ('Armor Class = Base AC + Dexterity Modifier + Magical Modifier(s) + '
                       'Shield + ModifierArmor Class = 10 + 4 + 0 + 0 + 0')

def test_saving_throw_proficiency(player_wizard, browser): # noqa
    """As a player, I can select to become proficient in a savings throw, and
       this can be viewed in the table via in icon."""
    print(('As a player, I can select to become proficient in a savings throw, '
           'and this can be viewed in the table via in icon.'))

    saving_throw = SavingThrowTable(browser)
    saving_throw_edit = SavingThrowEditModal(browser)

    row = ut.get_table_row(saving_throw, 'table', values=False)
    # open edit modal
    row[0].click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, saving_throw_edit.proficiency.get_attribute('id'))
        )
    )

    saving_throw_edit.proficiency.click()
    saving_throw_edit.done.click()

    # add custom wait to test for class in nested element
    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        modal_finished_closing()
    )

    row = ut.get_table_row(saving_throw, 'table', values=False)
    span = row[0].find_elements(By.TAG_NAME, 'span')

    assert span[0].get_attribute('class').strip() == 'fa fa-check'

def test_saving_throw_modifier(player_wizard, browser): # noqa
    """As a player, I can increase or decrease my savings throws via a modifier
       field"""
    print(('As a player, I can increase or decrease my savings throws via a '
           'modifier field.'))

    saving_throw = SavingThrowTable(browser)
    saving_throw_edit = SavingThrowEditModal(browser)

    row = ut.get_table_row(saving_throw, 'table', values=False)
    # open edit modal
    row[0].click()

    saving_throw_edit.modifier = 1
    saving_throw_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_cell_updated(
            saving_throw,
            'blank2',
            '+ 5',
            'table',
            1
        )
    )

    row = ut.get_table_row(saving_throw, 'table')

    assert row.blank2.strip() == '+ 5'
