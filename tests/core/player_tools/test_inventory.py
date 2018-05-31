"""UAT test file for Adventurer's Codex player tools inventory module."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character import coins, inventory, magic_items
from components.core.character.tabs import Tabs
from expected_conditions.general import modal_finished_closing
from expected_conditions.general import sorting_arrow_down, sorting_arrow_up
from utils import general as ut

def test_add_inventory(player_wizard, browser): # noqa
    """As a player, I can add an item to my inventory."""
    print('As a player, I can add an item to my inventory.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_table.add_id)
        )
    )

    inventory_table.add.click()
    inventory_add.name = 'Add Name'
    inventory_add.weight = 100
    inventory_add.quantity = 2
    inventory_add.cost = 100
    inventory_add.currency_denomination = 'GP'
    inventory_add.description = 'Add Description'

    assert inventory_add.name.get_attribute('value').strip() == 'Add Name'
    assert inventory_add.weight.get_attribute('value').strip() == '100'
    assert inventory_add.quantity.get_attribute('value').strip() == '2'
    assert inventory_add.cost.get_attribute('value').strip() == '100'
    assert inventory_add.currency_denomination.get_attribute('value').strip() == 'GP'
    assert inventory_add.description.get_attribute('value').strip() == 'Add Description'

    inventory_add.add.click()

    row = ut.get_table_row(inventory_table, 'table', 1)

    assert row.item.strip() == 'Add Name'
    assert row.quantity.strip() == '2'
    assert row.weight.strip() == '100 lbs.'
    assert row.cost.strip() == '100 GP'
    assert row.description.strip() == 'Add Description'


def test_delete_inventory(player_wizard, browser): # noqa
    """As a player, I can delete an item in my inventory."""
    print('As a player, I can delete an item to my inventory.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    rows = ut.get_table_rows(inventory_table, 'table', values=False)
    rows[0][5].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(inventory_table, 'table', values=False)

    assert rows[0][0].text.strip() == 'Add a new item'


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
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    rows = ut.get_table_rows(inventory_table, 'table', values=False)
    rows[0][0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_tabs.edit_id)
        )
    )

    inventory_tabs.edit.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, inventory_edit.name_id)
        )
    )

    inventory_edit.name = 'Edit Name'
    inventory_edit.weight = 100
    inventory_edit.quantity = 2
    inventory_edit.cost = 100
    inventory_edit.currency_denomination = 'GP'
    inventory_edit.description = 'Edit Description'

    assert inventory_edit.name.get_attribute('value').strip() == 'Edit Name'
    assert inventory_edit.weight.get_attribute('value').strip() == '100'
    assert inventory_edit.quantity.get_attribute('value').strip() == '2'
    assert inventory_edit.cost.get_attribute('value').strip() == '100'
    assert inventory_edit.currency_denomination.get_attribute('value').strip() == 'GP'
    assert inventory_edit.description.get_attribute('value').strip() == 'Edit Description'

    inventory_edit.done.click()
    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )
    row = ut.get_table_row(inventory_table, 'table', 1)

    assert row.item.strip() == 'Edit Name'
    assert row.quantity.strip() == '2'
    assert row.weight.strip() == '100 lbs.'
    assert row.cost.strip() == '100 GP'
    assert row.description.strip() == 'Edit Description'

def test_preview_inventory(player_wizard, browser): # noqa
    """As a player, I can select a row in the inventory table and view the
       item in the preview tab."""
    print(('As a player, I can select a row in the inventory table and view '
           'the item in the preview tab'))

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    inventory_preview = inventory.InventoryPreviewModal(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_table.add_id)
        )
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    row = ut.get_table_row(inventory_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_preview.done_id)
        )
    )

    assert inventory_preview.name.text.strip() == 'Abacus'
    assert inventory_preview.weight.text.strip() == '2 lbs.'
    assert inventory_preview.quantity.text.strip() == '1'
    assert inventory_preview.cost.text.strip() == '2 GP'
    assert inventory_preview.description.text.strip() == 'Add a description via the edit tab.'

def test_add_inventory_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in inventory table to open the
       inventory add modal."""
    print(('As a player, I can click the first row in inventory table to open '
           'the inventory add modal.'))

    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    rows = ut.get_table_rows(inventory_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()

def test_autocomplete_inventory(player_wizard, browser): # noqa
    """As a player, if I start typing in the autocomplete inputs, I can select
       suggested items in the dropdown."""
    print(('As a player, if I start typing in the autocomplete inputs, I can '
          'select suggested items in the dropdown.'))

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_table.add_id)
        )
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )

    assert inventory_add.name.get_attribute('value').strip() == 'Abacus'


def test_inventory_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from inventory name field, OGL data
       auto-completes and the remaining fields pre-populate."""
    print(('As a player, if I select from inventory name field, OGL data '
           'auto-completes and the remaining fields pre-populate.'))

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_table.add_id)
        )
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    row = ut.get_table_row(inventory_table, 'table', 1)

    assert row.item.strip() == 'Abacus'
    assert row.weight.strip() == '2 lbs.'
    assert row.quantity.strip() == '1'
    assert row.cost.strip() == '2 GP'
    assert row.description.strip() == ''

def test_inventory_persists(player_wizard, browser): # noqa
    """As a player, all fields for inventory persist after page refresh."""
    print('As a player, all fields for inventory persist after page refresh.')

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_edit = inventory.InventoryEditModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    inventory_tabs = inventory.InventoryModalTabs(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_table.add_id)
        )
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    browser.refresh()

    row = ut.get_table_row(inventory_table, 'table', 1)

    assert row.item.strip() == 'Abacus'
    assert row.weight.strip() == '2 lbs.'
    assert row.quantity.strip() == '1'
    assert row.cost.strip() == '2 GP'
    assert row.description.strip() == ''

    row = ut.get_table_row(inventory_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_tabs.edit_id)
        )
    )

    inventory_tabs.edit.click()

    assert inventory_edit.name.get_attribute('value').strip() == 'Abacus'
    assert inventory_edit.weight.get_attribute('value').strip() == '2'
    assert inventory_edit.quantity.get_attribute('value').strip() == '1'
    assert inventory_edit.cost.get_attribute('value').strip() == '2'
    assert inventory_edit.currency_denomination.get_attribute('value').strip() == 'GP'
    assert inventory_edit.description.get_attribute('value').strip() == ''

def test_inventory_total_weight(player_wizard, browser): # noqa
    """As a player, in the inventory table, total weight is calculated
       correctly."""
    print(('As a player, in the armor table, total weight is calculated '
           'correctly'))

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_table.add_id)
        )
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    assert inventory_table.total_weight.text.strip() == '4 (lbs)'


def test_inventory_sorting(player_wizard, browser): # noqa
    """As a player, I can sort the inventory table by clicking on the
       sortable columns."""
    print(('As a player, I can sort the inventory table by clicking on the '
           'sortable columns'))

    inventory_add = inventory.InventoryAddModal(browser)
    inventory_table = inventory.InventoryTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, inventory_table.add_id)
        )
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        has_search_term=False
    )
    inventory_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    inventory_table.add.click()
    ut.select_from_autocomplete(
        inventory_add,
        'name',
        browser,
        arrow_down_count=2
    )
    inventory_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    inventory_table.item_header.click()

    WebDriverWait(browser, 5).until(
        sorting_arrow_down(
            inventory_table.item_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(inventory_table, 'table', values=False)

    assert rows[0].text.strip() == 'Acid (vial)'

    inventory_table.quantity_header.click()

    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            inventory_table.quantity_header_sorting_arrow,
        )
    )

    rows = ut.get_table_row(inventory_table, 'table', values=False)

    assert rows[1].text.strip() == '1'

    inventory_table.weight_header.click()

    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            inventory_table.weight_header_sorting_arrow,
        )
    )

    rows = ut.get_table_row(inventory_table, 'table', values=False)

    assert rows[2].text.strip() == '1 lbs.'


def test_add_coins(player_wizard, browser): # noqa
    """As a player, I can add coins."""
    print('As a player, I can add coins')

    coins_table = coins.Coins(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    coins_table.platinum = 2
    coins_table.gold = 4
    coins_table.electrum = 6
    coins_table.silver = 8
    coins_table.copper = 10

    assert coins_table.platinum.get_attribute('value').strip() == '2'
    assert coins_table.gold.get_attribute('value').strip() == '4'
    assert coins_table.electrum.get_attribute('value').strip() == '6'
    assert coins_table.silver.get_attribute('value').strip() == '8'
    assert coins_table.copper.get_attribute('value').strip() == '10'


def test_delete_coins(player_wizard, browser): # noqa
    """As a player, I can delete coins."""
    print('As a player, I can delete coins')

    coins_table = coins.Coins(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    coins_table.platinum = 2
    coins_table.gold = 4
    coins_table.electrum = 6
    coins_table.silver = 8
    coins_table.copper = 10

    assert coins_table.platinum.get_attribute('value').strip() == '2'
    assert coins_table.gold.get_attribute('value').strip() == '4'
    assert coins_table.electrum.get_attribute('value').strip() == '6'
    assert coins_table.silver.get_attribute('value').strip() == '8'
    assert coins_table.copper.get_attribute('value').strip() == '10'

    coins_table.platinum = 0
    coins_table.gold = 0
    coins_table.electrum = 0
    coins_table.silver = 0
    coins_table.copper = 0

    assert coins_table.platinum.get_attribute('value').strip() == '0'
    assert coins_table.gold.get_attribute('value').strip() == '0'
    assert coins_table.electrum.get_attribute('value').strip() == '0'
    assert coins_table.silver.get_attribute('value').strip() == '0'
    assert coins_table.copper.get_attribute('value').strip() == '0'


def test_edit_coins(player_wizard, browser): # noqa
    """As a player, I can edit coins."""
    print('As a player, I can delete coins')

    coins_table = coins.Coins(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    coins_table.platinum = 2
    coins_table.gold = 4
    coins_table.electrum = 6
    coins_table.silver = 8
    coins_table.copper = 10

    assert coins_table.platinum.get_attribute('value').strip() == '2'
    assert coins_table.gold.get_attribute('value').strip() == '4'
    assert coins_table.electrum.get_attribute('value').strip() == '6'
    assert coins_table.silver.get_attribute('value').strip() == '8'
    assert coins_table.copper.get_attribute('value').strip() == '10'

    coins_table.platinum = 4
    coins_table.gold = 6
    coins_table.electrum = 8
    coins_table.silver = 10
    coins_table.copper = 12

    assert coins_table.platinum.get_attribute('value').strip() == '4'
    assert coins_table.gold.get_attribute('value').strip() == '6'
    assert coins_table.electrum.get_attribute('value').strip() == '8'
    assert coins_table.silver.get_attribute('value').strip() == '10'
    assert coins_table.copper.get_attribute('value').strip() == '12'


def test_worth_in_gold_coins(player_wizard, browser): # noqa
    """As a player, I can view total gold for coins."""
    print('As a player, I can view total gold for coins')

    coins_table = coins.Coins(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    coins_table.platinum = 1
    coins_table.gold = 1
    coins_table.electrum = 2
    coins_table.silver = 10
    coins_table.copper = '100'
    coins_table.copper.send_keys(Keys.TAB)

    assert coins_table.worth_in_gold.text.strip() == '14'


def test_coins_total_weight(player_wizard, browser): # noqa
    """As a player, I can view total weight for coins."""
    print('As a player, I can view total weight for coins')

    coins_table = coins.Coins(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    coins_table.platinum = 50
    coins_table.gold = 50
    coins_table.electrum = 50
    coins_table.silver = 50
    coins_table.copper = '49'
    coins_table.copper.send_keys(Keys.TAB)

    assert coins_table.total_weight.text.strip() == '4 (lbs)'

def test_coins_persists(player_wizard, browser): # noqa
    """As a player, all fields for coins persist after page refresh."""
    print('As a player, all fields for coins persist after page refresh.')

    coins_table = coins.Coins(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    coins_table.platinum = 50
    coins_table.gold = 50
    coins_table.electrum = 50
    coins_table.silver = 50
    coins_table.copper = '50'
    coins_table.copper.send_keys(Keys.TAB)

    browser.refresh()

    assert coins_table.platinum.get_attribute('value').strip() == '50'
    assert coins_table.gold.get_attribute('value').strip() == '50'
    assert coins_table.electrum.get_attribute('value').strip() == '50'
    assert coins_table.silver.get_attribute('value').strip() == '50'
    assert coins_table.copper.get_attribute('value').strip() == '50'


def test_add_magic_items(player_wizard, browser): # noqa
    """As a player, I can add an item to my magic_items."""
    print('As a player, I can add an item to my magic_items.')

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    magic_items_table.add.click()
    magic_items_add.item = 'Add Name'
    magic_items_add.type_ = 'Add Armor'
    magic_items_add.rarity = 'Add Rare'
    magic_items_add.max_charges = 3
    magic_items_add.charges = 3
    magic_items_add.weight = 100
    magic_items_add.requires_attunement.click()
    magic_items_add.attuned.click()
    magic_items_add.description = 'Add Description'

    assert magic_items_add.item.get_attribute('value').strip() == 'Add Name'
    assert magic_items_add.type_.get_attribute('value').strip() == 'Add Armor'
    assert magic_items_add.rarity.get_attribute('value').strip() == 'Add Rare'
    assert magic_items_add.max_charges.get_attribute('value').strip() == '3'
    assert magic_items_add.charges.get_attribute('value').strip() == '3'
    assert magic_items_add.weight.get_attribute('value').strip() == '100'
    assert magic_items_add.requires_attunement.is_selected()
    assert magic_items_add.attuned.is_selected()
    assert magic_items_add.description.get_attribute('value').strip() == 'Add Description'

    magic_items_add.add.click()

    row = ut.get_table_row(magic_items_table, 'table', 1)

    assert row.magic_item.strip() == 'Add Name'
    assert row.charges.strip() == '3'
    assert row.weight.strip() == '100 lbs.'
    assert row.description.strip() == 'Add Description'

    row = ut.get_table_row(magic_items_table, 'table', 1, values=False)

    assert row[2].find_element_by_tag_name('input').is_selected()

def test_delete_magic_items(player_wizard, browser): # noqa
    """As a player, I can delete an item in my magic_items."""
    print('As a player, I can delete an item to my magic_items.')

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False
    )
    magic_items_add.add.click()

    rows = ut.get_table_rows(magic_items_table, 'table', values=False)

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    rows[0][5].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(magic_items_table, 'table', values=False)

    assert rows[0][0].text.strip() == 'Add a new magic item'

def test_edit_magic_items(player_wizard, browser): # noqa
    """As a player, I can edit an item in my magic_items."""
    print('As a player, I can edit an item in my magic_items.')

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_edit = magic_items.MagicItemsEditModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    magic_items_tabs = magic_items.MagicItemsModalTabs(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False
    )
    magic_items_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    rows = ut.get_table_rows(magic_items_table, 'table', values=False)
    rows[0][0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, magic_items_tabs.edit_id)
        )
    )

    magic_items_tabs.edit.click()

    magic_items_edit.item = 'Edit Name'
    magic_items_edit.type_ = 'Edit Armor'
    magic_items_edit.rarity = 'Edit Rare'
    magic_items_edit.max_charges = 3
    magic_items_edit.charges = 3
    magic_items_edit.weight = 100
    magic_items_edit.requires_attunement.click()
    magic_items_edit.attuned.click()
    magic_items_edit.description = 'Edit Description'

    assert magic_items_edit.item.get_attribute('value').strip() == 'Edit Name'
    assert magic_items_edit.type_.get_attribute('value').strip() == 'Edit Armor'
    assert magic_items_edit.rarity.get_attribute('value').strip() == 'Edit Rare'
    assert magic_items_edit.max_charges.get_attribute('value').strip() == '3'
    assert magic_items_edit.charges.get_attribute('value').strip() == '3'
    assert magic_items_edit.weight.get_attribute('value').strip() == '100'
    assert magic_items_edit.requires_attunement.is_selected()
    assert magic_items_edit.attuned.is_selected()
    assert magic_items_edit.description.get_attribute('value').strip() == 'Edit Description'

    magic_items_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    row = ut.get_table_row(magic_items_table, 'table', 1)

    assert row.magic_item.strip() == 'Edit Name'
    assert row.charges.strip() == '3'
    assert row.weight.strip() == '100 lbs.'
    assert row.description.strip() == 'Edit Description'

    row = ut.get_table_row(magic_items_table, 'table', 1, values=False)

    assert row[2].find_element_by_tag_name('input').is_selected()


def test_preview_magic_items(player_wizard, browser): # noqa
    """As a player, I can select a row in the magic_items table and view the
       item in the preview tab."""
    print(('As a player, I can select a row in the magic_items table and view '
           ' the item in the preview tab'))

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    magic_items_preview = magic_items.MagicItemsPreviewModal(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False
    )
    magic_items_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    row = ut.get_table_row(magic_items_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, magic_items_preview.item_id), 'Adamantine Armor'
        )
    )

    preview_type_ = magic_items_preview.type_.text.split()
    magic_items_type = ' '.join([string.strip() for string in preview_type_])
    magic_items_max_charges = ' '.join(
        [
            string.strip()
            for string in magic_items_preview.max_charges.text.split()
        ]
    )
    magic_items_weight = ' '.join(
        [
            string.strip()
            for string in magic_items_preview.weight.text.split()
        ]
    )

    assert magic_items_preview.item.text.strip() == 'Adamantine Armor'
    assert magic_items_preview.rarity.text.strip() == 'Uncommon'
    assert magic_items_type == 'Type: Armor (medium or heavy but not hide)'
    assert magic_items_max_charges == 'Max Charges: 0'
    assert magic_items_weight == 'Weight: 0 lbs.'
    assert 'reinforced with adamantine' in magic_items_preview.description.text.strip()


def test_add_magic_items_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in magic_items table to open the
       magic_items add modal."""
    print(('As a player, I can click the first row in magic_items table to '
           'open the magic_items add modal.'))

    magic_items_table = magic_items.MagicItemsTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    rows = ut.get_table_rows(magic_items_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()


def test_autocomplete_magic_items(player_wizard, browser): # noqa
    """As a player, if I start typing in the autocomplete inputs, I can select
       suggested items in the dropdown."""
    print(('As a player, if I start typing in the autocomplete inputs, I can '
           'select suggested items in the dropdown.'))

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, magic_items_table.add_id)
        )
    )

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False
    )
    ut.select_from_autocomplete(
        magic_items_add,
        'type_',
        browser,
        has_search_term=False
    )
    ut.select_from_autocomplete(
        magic_items_add,
        'rarity',
        browser,
        has_search_term=False
    )

    assert magic_items_add.item.get_attribute('value').strip() == 'Adamantine Armor'
    assert magic_items_add.type_.get_attribute('value').strip() == 'Armor'
    assert magic_items_add.rarity.get_attribute('value').strip() == 'Common'


def test_magic_items_persists(player_wizard, browser): # noqa
    """As a player, all fields for magic_items persist after page refresh."""
    print('As a player, all fields for magic_items persist after page refresh.')

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_edit = magic_items.MagicItemsEditModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    magic_items_tabs = magic_items.MagicItemsModalTabs(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False
    )
    magic_items_add.add.click()

    browser.refresh()

    row = ut.get_table_row(magic_items_table, 'table', 1)

    assert row.magic_item.strip() == 'Adamantine Armor'
    assert row.charges.strip() == 'N/A'
    assert row.weight.strip() == '0 lbs.'
    assert 'with adamantine' in row.description.strip()

    row = ut.get_table_row(magic_items_table, 'table', 1, values=False)

    assert row[2].find_element_by_tag_name('input').is_displayed() is False

    row = ut.get_table_row(magic_items_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, magic_items_tabs.edit_id)
        )
    )

    magic_items_tabs.edit.click()

    assert magic_items_edit.item.get_attribute('value').strip() == 'Adamantine Armor'

    armor_type = 'Armor (medium or heavy but not hide)'
    assert magic_items_edit.type_.get_attribute('value').strip() == armor_type
    assert magic_items_edit.rarity.get_attribute('value').strip() == 'Uncommon'
    assert magic_items_edit.max_charges.get_attribute('value').strip() == '0'
    assert magic_items_edit.weight.get_attribute('value').strip() == '0'
    assert magic_items_edit.requires_attunement.is_selected() is False

    description = magic_items_edit.description.get_attribute('value').strip()
    assert 'reinforced with adamantine' in description


def test_magic_items_total_weight(player_wizard, browser): # noqa
    """As a player, in the magic_items table, total weight is calculated
       correctly."""
    print(('As a player, in the armor table, total weight is calculated '
           'correctly'))

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False,
        search_term='b'
    )
    magic_items_add.weight = 5
    magic_items_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False,
        search_term='b'
    )
    magic_items_add.weight = 10
    magic_items_add.add.click()

    assert magic_items_table.total_weight.text.strip() == '15 (lbs)'

def test_magic_items_sorting(player_wizard, browser): # noqa
    """As a player, I can sort the magic_items table by clicking on the
       sortable columns."""
    print(('As a player, I can sort the magic_items table by clicking on the '
           'sortable columns'))

    magic_items_add = magic_items.MagicItemsAddModal(browser)
    magic_items_table = magic_items.MagicItemsTable(browser)
    tabs = Tabs(browser)
    tabs.inventory.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, magic_items_table.add_id)
        )
    )

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False
    )
    magic_items_add.weight = 100
    magic_items_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    magic_items_table.add.click()
    ut.select_from_autocomplete(
        magic_items_add,
        'item',
        browser,
        has_search_term=False,
        arrow_down_count=2
    )
    magic_items_add.max_charges = 2
    magic_items_add.charges = 1
    magic_items_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing()
    )

    magic_items_table.magic_item_header.click()
    WebDriverWait(browser, 10).until(
        sorting_arrow_down(
            magic_items_table.magic_item_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(magic_items_table, 'table', values=False)

    assert rows[0].text.strip() == 'Amulet of Health'

    magic_items_table.charges_header.click()
    WebDriverWait(browser, 10).until(
        sorting_arrow_up(
            magic_items_table.charges_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(magic_items_table, 'table', values=False)

    assert rows[1].text.strip() == 'N/A'

    magic_items_table.weight_header.click()
    WebDriverWait(browser, 10).until(
        sorting_arrow_up(
            magic_items_table.weight_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(magic_items_table, 'table', values=False)

    assert rows[3].text.strip() == '0 lbs.'

    magic_items_table.weight_header.click()
    WebDriverWait(browser, 10).until(
        sorting_arrow_down(
            magic_items_table.weight_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(magic_items_table, 'table', values=False)

    assert rows[3].text.strip() == '100 lbs.'
