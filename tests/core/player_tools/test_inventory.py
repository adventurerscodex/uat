"""UAT test file for Adventurer's Codex player tools inventory module."""
import time

from selenium.webdriver.support import expected_conditions as EC # noqa

from components.core.character import inventory
from components.core.character.tabs import Tabs
from utils import utils as ut

def test_add_inventory(player_wizard, browser): # noqa
    """As a player, I can add an item to my inventory."""
    print('As a player, I can add an item to my inventory.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    inventory_add.name = 'Add Name'
    inventory_add.weight = 100
    inventory_add.quantity = 2
    inventory_add.cost = 100
    inventory_add.currency_denomination = 'GP'
    inventory_add.description = 'Add Description'

    assert inventory_add.name.get_attribute('value') == 'Add Name'
    assert inventory_add.weight.get_attribute('value') == '100'
    assert inventory_add.quantity.get_attribute('value') == '2'
    assert inventory_add.cost.get_attribute('value') == '100'
    assert inventory_add.currency_denomination.get_attribute('value') == 'GP'
    assert inventory_add.description.get_attribute('value') == 'Add Description'

    inventory_add.add.click()

    row = ut.get_table_row(inventory_table, 'table', 1)
    assert row.item == 'Add Name'
    assert row.quantity == '2'
    assert row.weight == '100 lbs.'
    assert row.cost == '100 GP'
    assert row.description == 'Add Description'


def test_delete_inventory(player_wizard, browser): # noqa
    """As a player, I can delete an item in my inventory."""
    print('As a player, I can delete an item to my inventory.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    rows = ut.get_table_rows(inventory_table, 'table', values=False)
    time.sleep(.3)
    rows[0][5].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(inventory_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new item'


def test_edit_inventory(player_wizard, browser): # noqa
    """As a player, I can edit an item in my inventory."""
    print('As a player, I can edit an item in my inventory.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_edit = inventory.InventoryEditModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    inventory_tabs = inventory.InventoryModalTabs(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    rows = ut.get_table_rows(inventory_table, 'table', values=False)
    time.sleep(.3)
    rows[0][0].click()
    time.sleep(.3)
    inventory_tabs.edit.click()
    time.sleep(.3)

    inventory_edit.name = 'Edit Name'
    inventory_edit.weight = 100
    inventory_edit.quantity = 2
    inventory_edit.cost = 100
    inventory_edit.currency_denomination = 'GP'
    inventory_edit.description = 'Edit Description'

    assert inventory_edit.name.get_attribute('value') == 'Edit Name'
    assert inventory_edit.weight.get_attribute('value') == '100'
    assert inventory_edit.quantity.get_attribute('value') == '2'
    assert inventory_edit.cost.get_attribute('value') == '100'
    assert inventory_edit.currency_denomination.get_attribute('value') == 'GP'
    assert inventory_edit.description.get_attribute('value') == 'Edit Description'

    inventory_edit.done.click()
    time.sleep(.3)
    row = ut.get_table_row(inventory_table, 'table', 1)
    assert row.item == 'Edit Name'
    assert row.quantity == '2'
    assert row.weight == '100 lbs.'
    assert row.cost == '100 GP'
    assert row.description == 'Edit Description'

def test_preview_inventory(player_wizard, browser): # noqa
    """As a player, I can select a row in the inventory table and view the item in the preview tab."""
    print('As a player, I can select a row in the inventory table and view the item in the preview tab')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    inventory_preview = inventory.InventoryPreviewModal(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    time.sleep(.3)
    row = ut.get_table_row(inventory_table, 'table', values=False)
    time.sleep(.3)
    row[0].click()
    time.sleep(.5)

    assert inventory_preview.name.text == 'Abacus'
    assert inventory_preview.weight.text == '2 lbs.'
    assert inventory_preview.quantity.text == '1'
    assert inventory_preview.cost.text == '2 GP'
    assert inventory_preview.description.text == 'Add a description via the edit tab.'

def test_add_inventory_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in inventory table to open the inventory add modal."""
    print('As a player, I can click the first row in inventory table to open the inventory add modal.')

    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    rows = ut.get_table_rows(inventory_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()

def test_autocomplete_inventory(player_wizard, browser): # noqa
    """As a player, if I start typing in the autocomplete inputs, I can select suggested items in the dropdown."""
    print('As a player, if I start typing in the autocomplete inputs, I can select suggested items in the dropdown.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)

    assert inventory_add.name.get_attribute('value') == 'Abacus'


def test_inventory_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from inventory name field, OGL data auto-completes and the remaining fields pre-populate."""
    print('As a player, if I select from inventory name field, OGL data auto-completes and the remaining fields pre-populate.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    row = ut.get_table_row(inventory_table, 'table', 1)

    assert row.item.strip() == 'Abacus'
    assert row.weight == '2 lbs.'
    assert row.quantity == '1'
    assert row.cost == '2 GP'
    assert row.description == ''

def test_inventory_persists(player_wizard, browser): # noqa
    """As a player, all fields for inventory persist after page refresh."""
    print('As a player, all fields for inventory persist after page refresh.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_edit = inventory.InventoryEditModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    inventory_tabs = inventory.InventoryModalTabs(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    browser.refresh()

    row = ut.get_table_row(inventory_table, 'table', 1)

    assert row.item.strip() == 'Abacus'
    assert row.weight == '2 lbs.'
    assert row.quantity == '1'
    assert row.cost == '2 GP'
    assert row.description == ''

    row = ut.get_table_row(inventory_table, 'table', values=False)
    time.sleep(.3)
    row[0].click()
    time.sleep(.3)
    inventory_tabs.edit.click()

    assert inventory_edit.name.get_attribute('value') == 'Abacus'
    assert inventory_edit.weight.get_attribute('value') == '2'
    assert inventory_edit.quantity.get_attribute('value') == '1'
    assert inventory_edit.cost.get_attribute('value') == '2'
    assert inventory_edit.currency_denomination.get_attribute('value') == 'GP'
    assert inventory_edit.description.get_attribute('value') == ''

def test_inventory_total_weight(player_wizard, browser): # noqa
    """As a player, in the inventory table, total weight is calculated correctly."""
    print('As a player, in the armor table, total weight is calculated correctly')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    time.sleep(.3)

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    assert inventory_table.total_weight.text == '4 (lbs)'


def test_inventory_sorting(player_wizard, browser): # noqa
    """As a player, I can sort the inventory table by clicking on the sortable columns."""
    print('As a player, I can sort the inventory table by clicking on the sortable columns')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser)
    inventory_add.add.click()

    time.sleep(.3)
    inventory_table.add.click()
    ut.select_from_autocomplete(inventory_add, 'name', '', browser, arrow_down_count=2)
    inventory_add.add.click()

    time.sleep(.3)
    inventory_table.item_header.click()
    time.sleep(.3)
    rows = ut.get_table_row(inventory_table, 'table', values=False)
    assert rows[0].text.strip() == 'Acid (vial)'

    time.sleep(.3)
    inventory_table.quantity_header.click()
    time.sleep(.3)
    rows = ut.get_table_row(inventory_table, 'table', values=False)
    assert rows[1].text.strip() == '1'

    time.sleep(.3)
    inventory_table.weight_header.click()
    time.sleep(.3)
    rows = ut.get_table_row(inventory_table, 'table', values=False)
    assert rows[2].text.strip() == '1 lbs.'
