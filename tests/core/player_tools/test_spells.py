"""UAT test file for Adventurer's Codex player tools spells module."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character import spells
from components.core.character.tabs import Tabs
from expected_conditions.general import modal_finished_closing
from utils import general as ut

def test_add_spells(player_wizard, browser): # noqa
    """As a player, I can add a spells."""
    print('As a player, I can add a spells.')

    spells_add = spells.SpellsAddModal(browser)
    spells_table = spells.SpellsTable(browser)
    tabs = Tabs(browser)
    tabs.spells.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, spells_table.add_id)
        )
    )

    spells_table.add.click()
    spells_add.name = 'Acid Arrow'
    spells_add.name.send_keys(Keys.TAB)

    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, 'ui-menu-item-wrapper')
        )
    )

    spells_add.prepared.click()
    spells_add.level = '5'
    spells_add.school = 'Add School'
    spells_add.type_ = 'Savings Throw'
    spells_add.type_.send_keys(Keys.TAB)
    spells_add.damage = '1d4'
    spells_add.cast_time = '1 action'
    spells_add.range_ = '5 feet'
    spells_add.components = 'S'
    spells_add.material_components = 'Add Material'
    spells_add.duration = '12 Minutes'
    spells_add.description = ' Add Description'

    assert spells_add.name.get_attribute('value').strip() == 'Acid Arrow'
    assert spells_add.prepared.is_selected()
    assert spells_add.level.get_attribute('value').strip() == '5'
    assert spells_add.school.get_attribute('value').strip() == 'Add School'
    assert spells_add.type_.get_attribute('value').strip() == 'Savings Throw'
    assert spells_add.damage.get_attribute('value').strip() == '1d4'
    assert spells_add.cast_time.get_attribute('value').strip() == '1 action'
    assert spells_add.range_.get_attribute('value').strip() == '5 feet'
    assert spells_add.components.get_attribute('value').strip() == 'S'
    assert spells_add.material_components.get_attribute('value').strip() == 'Add Material'
    assert spells_add.duration.get_attribute('value').strip() == '12 Minutes'

    spells_add.add.click()

    row = ut.get_table_row(spells_table, 'table', 1)

    assert row.spell.strip() == 'Acid Arrow'
    assert row.level.strip() == '5'
    assert row.type.strip() == 'Savings Throw'
    assert row.damage.strip() == '1d4'
    assert row.casting_time.strip() == '1 action'
    assert row.range.strip() == '5 feet'

    row = ut.get_table_row(spells_table, 'table', 1, values=False)

def test_delete_spells(player_wizard, browser): # noqa
    """As a player, I can delete a spells."""
    print('As a player, I can delete a spells.')

    spells_add = spells.SpellsAddModal(browser)
    spells_table = spells.SpellsTable(browser)
    tabs = Tabs(browser)
    tabs.spells.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, spells_table.add_id)
        )
    )

    spells_table.add.click()
    ut.select_from_autocomplete(
        spells_add,
        'name',
        browser,
        has_search_term=False
    )
    spells_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    rows = ut.get_table_rows(spells_table, 'table', values=False)
    rows[0][7].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(spells_table, 'table', values=False)

    assert rows[0][0].text.strip() == 'Add a new spell'

def test_edit_spells(player_wizard, browser): # noqa
    """As a player, I can edit a spells."""
    print('As a player, I can edit a spells.')

    spells_add = spells.SpellsAddModal(browser)
    spells_edit = spells.SpellsEditModal(browser)
    spells_table = spells.SpellsTable(browser)
    spells_tabs = spells.SpellsModalTabs(browser)
    tabs = Tabs(browser)
    tabs.spells.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, spells_table.add_id)
        )
    )

    spells_table.add.click()

    ut.select_from_autocomplete(
        spells_add,
        'name',
        browser,
        has_search_term=False
    )
    spells_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    rows = ut.get_table_rows(spells_table, 'table', values=False)
    rows[0][1].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, spells_tabs.edit_id)
        )
    )

    spells_tabs.edit.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, spells_edit.name_id)
        )
    )

    spells_edit.name = 'Add Name'
    spells_edit.prepared.click()
    spells_edit.level = '5'
    spells_edit.school = 'Add School'
    spells_edit.type_ = 'Savings Throw'
    spells_edit.save_attr = 'Con'
    spells_edit.damage = '1d4'
    spells_edit.cast_time = '1 action'
    spells_edit.range_ = '5 feet'
    spells_edit.components = 'S'
    spells_edit.material_components = 'Add Material'
    spells_edit.duration = '12 Minutes'
    spells_edit.description = ' Add Description'

    assert spells_edit.name.get_attribute('value') == 'Add Name'
    assert spells_edit.prepared.is_selected()
    assert spells_edit.level.get_attribute('value') == '5'
    assert spells_edit.school.get_attribute('value') == 'Add School'
    assert spells_edit.type_.get_attribute('value') == 'Savings Throw'
    assert spells_edit.save_attr.get_attribute('value') == 'Con'
    assert spells_edit.damage.get_attribute('value') == '1d4'
    assert spells_edit.cast_time.get_attribute('value') == '1 action'
    assert spells_edit.range_.get_attribute('value') == '5 feet'
    assert spells_edit.components.get_attribute('value') == 'S'
    assert spells_edit.material_components.get_attribute('value') == 'Add Material'
    assert spells_edit.duration.get_attribute('value') == '12 Minutes'
    assert spells_edit.description.get_attribute('value') == ' Add Description'

    spells_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    row = ut.get_table_row(spells_table, 'table', 1)

    assert row.spell == 'Add Name'
    assert row.level == '5'
    assert row.type == 'Savings Throw'
    assert row.damage == '1d4'
    assert row.casting_time == '1 action'
    assert row.range == '5 feet'

    row = ut.get_table_row(spells_table, 'table', 1, values=False)

    assert row[0].find_element_by_tag_name('input').is_selected()

def test_preview_spells(player_wizard, browser): # noqa
    """As a player, I can select a row in the spells table and view the item in the preview tab."""
    print(('As a player, I can select a row in the spells table and view the item in the '
           'preview tab'))

    spells_add = spells.SpellsAddModal(browser)
    spells_table = spells.SpellsTable(browser)
    spells_preview = spells.SpellsPreviewModal(browser)
    tabs = Tabs(browser)
    tabs.spells.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, spells_table.add_id)
        )
    )

    spells_table.add.click()
    ut.select_from_autocomplete(
        spells_add,
        'name',
        browser,
        has_search_term=False
    )
    spells_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    row = ut.get_table_row(spells_table, 'table', values=False)
    row[1].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, spells_preview.done_id)
        )
    )

    assert spells_preview.name.text.strip() == 'Acid Arrow'
    assert spells_preview.spell_summary_label.text.strip() == 'Evocation, Level 2'
    assert spells_preview.type_.text.strip() == 'Ranged Spell Attack'
    assert spells_preview.damage.text.strip() == '4d4'
    assert spells_preview.cast_time.text.strip() == '1 action'
    assert spells_preview.range_.text.strip() == '90 feet'
    assert spells_preview.components.text.strip() == 'V, S, M'
    assert spells_preview.duration.text.strip() == 'Instantaneous'

def test_add_spells_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in spells table to open the spells add modal."""
    print('As a player, I can click the first row in spells table to open the spells add modal.')

    spells_table = spells.SpellsTable(browser)
    tabs = Tabs(browser)
    tabs.spells.click()

    rows = ut.get_table_rows(spells_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()
