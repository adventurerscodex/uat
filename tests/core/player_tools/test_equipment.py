"""UAT test file for Adventurer's Codex player tools equipment module."""
import time

from selenium.webdriver.support import expected_conditions as EC # noqa

from components.core.character import armor
from components.core.character.tabs import Tabs
from utils import utils as ut

def test_add_armor(player_wizard, browser): # noqa
    """As a player, I can add an armor."""
    print('As a player, I can add an armor.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    armor_add.name = 'Add Name'
    armor_add.type_ = 'Add Type'
    armor_add.magical_modifier.clear()
    armor_add.magical_modifier = 1
    armor_add.price = 200
    armor_add.currency_denomination = 'GP'
    armor_add.weight = 100
    armor_add.armor_class = 15
    armor_add.stealth = 'Disadvantage\t'
    armor_add.don.click()
    armor_add.description = 'Add Description'

    assert armor_add.name.get_attribute('value') == 'Add Name'
    assert armor_add.type_.get_attribute('value') == 'Add Type'
    assert armor_add.magical_modifier.get_attribute('value') == '1'
    assert armor_add.price.get_attribute('value') == '200'
    assert armor_add.currency_denomination.get_attribute('value') == 'GP'
    assert armor_add.weight.get_attribute('value') == '100'
    assert armor_add.armor_class.get_attribute('value') == '15'
    assert armor_add.stealth.get_attribute('value') == 'Disadvantage'
    assert 'active' in armor_add.don.get_attribute('class')
    assert armor_add.description.get_attribute('value') == 'Add Description'
    armor_add.add.click()

    row = ut.get_table_row(armor_table, 'table', 1)
    assert row.armor == 'Add Name  + 1'
    assert row.armor_class == '15'
    assert row.type == 'Add Type'

def test_delete_armor(player_wizard, browser): # noqa
    """As a player, I can delete an armor."""
    print('As a player, I can delete an armor.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    rows = ut.get_table_rows(armor_table, 'table', values=False)
    time.sleep(.3)
    rows[0][4].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(armor_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new armor'

def test_edit_armor(player_wizard, browser): # noqa
    """As a player, I can edit an armor."""
    print('As a player, I can edit an armor.')

    armor_add = armor.ArmorAddModal(browser)
    armor_edit = armor.ArmorEditModal(browser)
    armor_table = armor.ArmorTable(browser)
    armor_tabs = armor.ArmorModalTabs(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    rows = ut.get_table_rows(armor_table, 'table', values=False)
    time.sleep(.3)
    rows[0][0].click()
    time.sleep(.3)
    armor_tabs.edit.click()

    armor_edit.name.clear()
    armor_edit.type_.clear()
    armor_edit.magical_modifier.clear()
    armor_edit.price.clear()
    armor_edit.currency_denomination.clear()
    armor_edit.weight.clear()
    armor_edit.armor_class.clear()
    armor_edit.stealth.clear()
    armor_edit.description.clear()

    armor_edit.name = 'Edit Name'
    armor_edit.type_ = 'Edit Type'
    armor_edit.magical_modifier = 2
    armor_edit.price = 300
    armor_edit.currency_denomination = 'EP'
    armor_edit.weight = 200
    armor_edit.armor_class = 16
    armor_edit.stealth = 'Advantage\t'
    armor_edit.doff.click()
    armor_edit.description = 'Edit Description'

    assert armor_edit.name.get_attribute('value') == 'Edit Name'
    assert armor_edit.type_.get_attribute('value') == 'Edit Type'
    assert armor_edit.magical_modifier.get_attribute('value') == '2'
    assert armor_edit.price.get_attribute('value') == '300'
    assert armor_edit.currency_denomination.get_attribute('value') == 'EP'
    assert armor_edit.weight.get_attribute('value') == '200'
    assert armor_edit.armor_class.get_attribute('value') == '16'
    assert armor_edit.stealth.get_attribute('value') == 'Advantage'
    assert 'active' in armor_add.doff.get_attribute('class')
    assert armor_edit.description.get_attribute('value') == 'Edit Description'
    armor_edit.done.click()
    time.sleep(.3)
    row = ut.get_table_row(armor_table, 'table', 1)
    assert row.armor == 'Edit Name  + 2'
    assert row.armor_class == '16'
    assert row.type == 'Edit Type'

def test_add_armor_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in armor table to open the armor add modal."""
    print('As a player, I can click the first row in armor table to open the armor add modal.')

    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    rows = ut.get_table_rows(armor_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()

def test_autocomplete_armor(player_wizard, browser): # noqa
    """As a player, if I start typing in the name, type and stealth field, I can select suggested items in the dropdown."""
    print('As a player, if I start typing in the name, type and stealth field, I can select suggested items in the dropdown.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    ut.select_from_autocomplete(armor_add, 'type_', '', browser)
    ut.select_from_autocomplete(armor_add, 'stealth', '', browser)

    assert armor_add.name.get_attribute('value') == 'Breastplate'
    assert armor_add.type_.get_attribute('value') == 'Light'
    assert armor_add.stealth.get_attribute('value') == 'Advantage'

def test_armor_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from armor name field, OGL data auto-completes and the remaining fields pre-populate."""
    print('As a player, if I select from armor name field, OGL data auto-completes and the remaining fields pre-populate.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    row = ut.get_table_row(armor_table, 'table', 1)

    assert row.armor.strip() == 'Breastplate'
    assert row.armor_class == '14'
    assert row.type == 'Medium'

def test_magical_modifier(player_wizard, browser): # noqa
    """As a player, if armor is magical, a badge indicating the modifier is present."""
    print('As a player, if armor is magical, a badge indicating the modifier is present.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    armor_add.name = 'Add Name'
    armor_add.magical_modifier.clear()
    armor_add.magical_modifier = 3

    armor_add.add.click()
    time.sleep(.5)

    row = ut.get_table_row(armor_table, 'table', 1)
    assert row.armor == 'Add Name  + 3'

def test_armor_persists(player_wizard, browser): # noqa
    """As a player, all fields for armor persist after page refresh."""
    print('As a player, all fields for armor persist after page refresh.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    browser.refresh()

    row = ut.get_table_row(armor_table, 'table', 1)

    assert row.armor.strip() == 'Breastplate'
    assert row.armor_class == '14'
    assert row.type == 'Medium'

def test_armor_donned(player_wizard, browser): # noqa
    """As a player, the checkbox appears when armor is donned."""
    print('As a player, the checkbox appears when armor is donned.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    armor_table.add.click()
    armor_add.name = 'Add Name'
    armor_add.don.click()

    armor_add.add.click()
    time.sleep(.3)

    row = ut.get_table_row(armor_table, 'table', 1, values=False)
    assert 'fa fa-check' in row[0].find_element_by_tag_name('span').get_attribute('class')
