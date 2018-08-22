"""UAT test file for Adventurer's Codex player tools calculations."""
from conftest import DEFAULT_WAIT_TIME
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character.ability_scores import AbilityScoresEditModal
from components.core.character.ability_scores import AbilityScoresTable
from components.core.character.hud import HUD
from components.core.character.other_stats import OtherStats
from components.core.character.saving_throw import SavingThrowTable
from components.core.character.skills import SkillsTable
from components.core.character.tabs import Tabs
from components.core.character.weapon import WeaponAddModal, WeaponTable
from expected_conditions.general import table_cell_updated
from utils import general as ut

def test_strength_increase(player_wizard, browser): # noqa
    """When strength is increased or decreased, relevant skills, savings
       throws, to hit, and encumbrance reflect the change."""

    print(('When strength is increased or decreased, relevant skills, savings '
           'throws, to hit, and encumbrance reflect the change.'))

    saving_throw = SavingThrowTable(browser)
    skills = SkillsTable(browser)
    ability_scores_table = AbilityScoresTable(browser)
    ability_scores_edit = AbilityScoresEditModal(browser)
    hud = HUD(browser)
    weapon_table = WeaponTable(browser)
    weapon_add = WeaponAddModal(browser)
    tabs = Tabs(browser)

    ability_scores_table.table.click()
    ability_scores_edit.strength = 14
    ability_scores_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_cell_updated(
            saving_throw,
            'blank2',
            '+ 2',
            'table',
            5
        )
    )

    strength = ut.get_table_row(saving_throw, 'table', row_number=5)

    tabs.skills.click()

    athletics = ut.get_table_row(skills, 'table', row_number=4)

    tabs.equipment.click()

    weapon_table.add.click()
    # select battleaxe
    ut.select_from_autocomplete(
        weapon_add,
        'name',
        browser,
        has_search_term=False
    )
    weapon_add.add.click()

    to_hit = ut.get_table_row(weapon_table, 'table').to_hit

    status = hud.status_line.find_elements_by_tag_name('span')
    encumbrance_color = status[1].get_attribute('class')

    assert strength.blank2.strip() == '+ 2'
    assert to_hit.strip() == '+ 4'
    assert athletics.blank2.strip() == '+ 2 (Str)'
    assert 'text-info' in encumbrance_color


def test_dexterity_increase(player_wizard, browser): # noqa
    """When dexterity is increased or decreased, relevant skills, savings
       throws, initiative, and to hit (finesse weapons) reflect the change."""

    print(('When dexterity is increased or decreased, relevant skills, '
           'savings throws, initiative, and to hit (finesse weapons) reflect '
           'the change.'))

    saving_throw = SavingThrowTable(browser)
    skills = SkillsTable(browser)
    ability_scores_table = AbilityScoresTable(browser)
    ability_scores_edit = AbilityScoresEditModal(browser)
    weapon_table = WeaponTable(browser)
    weapon_add = WeaponAddModal(browser)
    stats = OtherStats(browser)
    tabs = Tabs(browser)

    ability_scores_table.table.click()
    # str needs to be less than dex as we are testing finesse weapon
    # i.e. the higher of str and dex is used
    ability_scores_edit.strength = 10
    ability_scores_edit.dexterity = 14
    ability_scores_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_cell_updated(
            saving_throw,
            'blank2',
            '+ 2',
            'table',
            3
        )
    )

    dexterity = ut.get_table_row(saving_throw, 'table', row_number=3)
    initiative = stats.initiative.text

    tabs.skills.click()

    acrobatics = ut.get_table_row(skills, 'table', row_number=1)
    sleight_of_hand = ut.get_table_row(skills, 'table', row_number=16)
    stealth = ut.get_table_row(skills, 'table', row_number=17)

    tabs.equipment.click()

    weapon_table.add.click()
    # select a dagger
    ut.select_from_autocomplete(
        weapon_add,
        'name',
        browser,
        has_search_term=False,
        arrow_down_count=7
    )
    weapon_add.add.click()

    to_hit = ut.get_table_row(weapon_table, 'table').to_hit

    assert dexterity.blank2.strip() == '+ 2'
    assert initiative.strip() == '2'
    assert to_hit.strip() == '+ 4'
    assert acrobatics.blank2.strip() == '+ 2 (Dex)'
    assert sleight_of_hand.blank2.strip() == '+ 2 (Dex)'
    assert stealth.blank2.strip() == '+ 2 (Dex)'

def test_constitution_increase(player_wizard, browser): # noqa
    """When constitution is increased or decreased, relevant skills reflect
       the change."""

    print(('When constitution is increased or decreased, relevant skills '
           'reflect the change.'))

    saving_throw = SavingThrowTable(browser)
    ability_scores_table = AbilityScoresTable(browser)
    ability_scores_edit = AbilityScoresEditModal(browser)

    ability_scores_table.table.click()
    ability_scores_edit.constitution = 14
    ability_scores_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_cell_updated(
            saving_throw,
            'blank2',
            '+ 2',
            'table',
            2
        )
    )

    constitution = ut.get_table_row(saving_throw, 'table', row_number=2)

    assert constitution.blank2.strip() == '+ 2'

def test_intelligence_increase(player_wizard, browser): # noqa
    """When intelligence is increased or decreased, relevant skills reflect
       the change."""

    print(('When intelligence is increased or decreased, relevant skills '
           'reflect the change.'))

    saving_throw = SavingThrowTable(browser)
    skills = SkillsTable(browser)
    ability_scores_table = AbilityScoresTable(browser)
    ability_scores_edit = AbilityScoresEditModal(browser)
    tabs = Tabs(browser)

    ability_scores_table.table.click()
    ability_scores_edit.intelligence = 14
    ability_scores_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_cell_updated(
            saving_throw,
            'blank2',
            '+ 2',
            'table',
            4
        )
    )

    intelligence = ut.get_table_row(saving_throw, 'table', row_number=4)

    tabs.skills.click()

    arcana = ut.get_table_row(skills, 'table', row_number=3)
    history = ut.get_table_row(skills, 'table', row_number=6)
    investigation = ut.get_table_row(skills, 'table', row_number=9)
    nature = ut.get_table_row(skills, 'table', row_number=11)
    religion = ut.get_table_row(skills, 'table', row_number=15)

    assert intelligence.blank2.strip() == '+ 2'
    assert arcana.blank2.strip() == '+ 2 (Int)'
    assert history.blank2.strip() == '+ 2 (Int)'
    assert investigation.blank2.strip() == '+ 2 (Int)'
    assert nature.blank2.strip() == '+ 2 (Int)'
    assert religion.blank2.strip() == '+ 2 (Int)'

def test_wisdom_increase(player_wizard, browser): # noqa
    """When wisdom is increased or decreased, relevant skills and savings
       throws reflect the change."""

    print(('When wisdom is increased or decreased, relevant skills and '
           'savings throws reflect the change.'))

    saving_throw = SavingThrowTable(browser)
    skills = SkillsTable(browser)
    ability_scores_table = AbilityScoresTable(browser)
    ability_scores_edit = AbilityScoresEditModal(browser)
    tabs = Tabs(browser)

    ability_scores_table.table.click()
    ability_scores_edit.wisdom = 14
    ability_scores_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_cell_updated(
            saving_throw,
            'blank2',
            '+ 2',
            'table',
            6
        )
    )

    wisdom = ut.get_table_row(saving_throw, 'table', row_number=6)

    tabs.skills.click()

    animal_handling = ut.get_table_row(skills, 'table', row_number=2)
    insight = ut.get_table_row(skills, 'table', row_number=7)
    medicine = ut.get_table_row(skills, 'table', row_number=10)
    perception = ut.get_table_row(skills, 'table', row_number=12)
    survival = ut.get_table_row(skills, 'table', row_number=18)

    assert wisdom.blank2.strip() == '+ 2'
    assert animal_handling.blank2.strip() == '+ 2 (Wis)'
    assert insight.blank2.strip() == '+ 2 (Wis)'
    assert medicine.blank2.strip() == '+ 2 (Wis)'
    assert perception.blank2.strip() == '+ 2 (Wis)'
    assert survival.blank2.strip() == '+ 2 (Wis)'

def test_charisma_increase(player_wizard, browser): # noqa
    """When charisma is increased or decreased, relevant skills and savings
       throws reflect the change."""

    print(('When charisma is increased or decreased, relevant skills and '
           'savings throws reflect the change.'))

    saving_throw = SavingThrowTable(browser)
    skills = SkillsTable(browser)
    ability_scores_table = AbilityScoresTable(browser)
    ability_scores_edit = AbilityScoresEditModal(browser)
    tabs = Tabs(browser)

    ability_scores_table.table.click()
    ability_scores_edit.charisma = 14
    ability_scores_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_cell_updated(
            saving_throw,
            'blank2',
            '+ 2',
            'table',
            1
        )
    )

    charisma = ut.get_table_row(saving_throw, 'table', row_number=1)

    tabs.skills.click()

    deception = ut.get_table_row(skills, 'table', row_number=5)
    intimidation = ut.get_table_row(skills, 'table', row_number=8)
    performance = ut.get_table_row(skills, 'table', row_number=13)
    persuasion = ut.get_table_row(skills, 'table', row_number=14)

    assert charisma.blank2.strip() == '+ 2'
    assert deception.blank2.strip() == '+ 2 (Cha)'
    assert intimidation.blank2.strip() == '+ 2 (Cha)'
    assert performance.blank2.strip() == '+ 2 (Cha)'
    assert persuasion.blank2.strip() == '+ 2 (Cha)'
