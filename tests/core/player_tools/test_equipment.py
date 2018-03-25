"""UAT test file for Adventurer's Codex player tools equipment module."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character import armor, weapon
from components.core.character.tabs import Tabs
from expected_conditions.conditions import modal_finished_closing
from expected_conditions.conditions import sorting_arrow_up, sorting_arrow_down
from expected_conditions.conditions import table_cell_updated
from factories.core.character.armor import ArmorFactory
from utils import utils as ut


def test_add_weapon(player_wizard, browser): # noqa
    """As a player, I can add a weapon."""
    print('As a player, I can add a weapon.')

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    weapon_add.name = 'Add Name'
    weapon_add.damage = 'Add Damage'
    weapon_add.magical_modifier = 1
    weapon_add.to_hit_modifier = 2
    weapon_add.type_ = 'Ranged'
    weapon_add.handedness = 'Add Handedness'
    weapon_add.proficiency = 'Add Proficiency'
    weapon_add.price = 200
    weapon_add.currency_denomination = 'GP'
    weapon_add.weight = 100
    weapon_add.range_ = '20/40'
    weapon_add.damage_type = 'Add Damage Type'
    weapon_add.property_ = 'Add Property'
    weapon_add.quantity = 2
    weapon_add.description = 'Add Description'

    assert weapon_add.name.get_attribute('value') == 'Add Name'
    assert weapon_add.damage.get_attribute('value') == 'Add Damage'
    assert weapon_add.magical_modifier.get_attribute('value') == '1'
    assert weapon_add.to_hit_modifier.get_attribute('value') == '2'
    assert weapon_add.handedness.get_attribute('value') == 'Add Handedness'
    assert weapon_add.proficiency.get_attribute('value') == 'Add Proficiency'
    assert weapon_add.price.get_attribute('value') == '200'
    assert weapon_add.currency_denomination.get_attribute('value') == 'GP'
    assert weapon_add.weight.get_attribute('value') == '100'
    assert weapon_add.range_.get_attribute('value') == '20/40'
    assert weapon_add.damage_type.get_attribute('value') == 'Add Damage Type'
    assert weapon_add.property_.get_attribute('value') == 'Add Property'
    assert weapon_add.quantity.get_attribute('value') == '2'
    assert weapon_add.description.get_attribute('value') == 'Add Description'

    weapon_add.add.click()

    row = ut.get_table_row(weapon_table, 'table', 1)

    assert row.weapon == 'Add Name  + 1'
    assert row.to_hit == '+ 9'
    assert row.damage == 'Add Damage'
    assert row.damage_type == 'Add Damage Type'
    assert row.range == '20/40 ft.'
    assert row.property == 'Add Property'
    assert row.quantity == '2'

def test_delete_weapon(player_wizard, browser): # noqa
    """As a player, I can delete a weapon."""
    print('As a player, I can delete a weapon.')

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    rows = ut.get_table_rows(weapon_table, 'table', values=False)
    rows[0][7].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(weapon_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new weapon'


def test_edit_weapon(player_wizard, browser): # noqa
    """As a player, I can edit a weapon."""
    print('As a player, I can edit a weapon.')

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_edit = weapon.WeaponEditModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    weapon_tabs = weapon.WeaponModalTabs(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    rows = ut.get_table_rows(weapon_table, 'table', values=False)
    rows[0][0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_tabs.edit_id)
        )
    )

    weapon_tabs.edit.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, weapon_edit.name_id)
        )
    )

    weapon_edit.name = 'Edit Name'
    weapon_edit.damage = '1d10'
    weapon_edit.magical_modifier = 2
    weapon_edit.to_hit_modifier = 2
    weapon_edit.type_ = 'Melee'
    weapon_edit.handedness = 'One-Handed'
    weapon_edit.proficiency = 'Simple'
    weapon_edit.price = 200
    weapon_edit.currency_denomination = 'GP'
    weapon_edit.weight = 200
    weapon_edit.range_ = 5
    weapon_edit.damage_type = 'Slashing'
    weapon_edit.property_ = 'Versatile'
    weapon_edit.quantity = 2
    weapon_edit.description = 'Edit Description'

    assert weapon_edit.name.get_attribute('value') == 'Edit Name'
    assert weapon_edit.damage.get_attribute('value') == '1d10'
    assert weapon_edit.magical_modifier.get_attribute('value') == '2'
    assert weapon_edit.to_hit_modifier.get_attribute('value') == '2'
    assert weapon_edit.type_.get_attribute('value') == 'Melee'
    assert weapon_edit.handedness.get_attribute('value') == 'One-Handed'
    assert weapon_edit.proficiency.get_attribute('value') == 'Simple'
    assert weapon_edit.price.get_attribute('value') == '200'
    assert weapon_edit.currency_denomination.get_attribute('value') == 'GP'
    assert weapon_edit.weight.get_attribute('value') == '200'
    assert weapon_edit.range_.get_attribute('value') == '5'
    assert weapon_edit.damage_type.get_attribute('value') == 'Slashing'
    assert weapon_edit.property_.get_attribute('value') == 'Versatile'
    assert weapon_edit.quantity.get_attribute('value') == '2'
    assert weapon_edit.description.get_attribute('value') == 'Edit Description'

    weapon_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_edit.modal_div_id)
    )

    row = ut.get_table_row(weapon_table, 'table', 1)

    assert row.weapon == 'Edit Name  + 2'
    assert row.to_hit == '+ 10'
    assert row.damage == '1d10'
    assert row.damage_type == 'Slashing'
    assert row.range == '5 ft.'
    assert row.property == 'Versatile'
    assert row.quantity == '2'

def test_preview_weapon(player_wizard, browser): # noqa
    """As a player, I can select a row in the weapon table and view the item
       in the preview tab."""
    print(('As a player, I can select a row in the weapon '
           'table and view the item in the preview tab'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    weapon_preview = weapon.WeaponPreviewModal(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    row = ut.get_table_row(weapon_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, weapon_preview.done_xpath)
        )
    )

    assert weapon_preview.name.text == 'Battleaxe'
    assert weapon_preview.magical_modifier.text == ''
    assert weapon_preview.damage.text == '1d8 or 1d10'
    assert weapon_preview.to_hit_modifier.text == '0'
    assert weapon_preview.range_.text == '5 ft.'
    assert weapon_preview.type_.text == 'Melee'
    assert weapon_preview.proficiency.text == 'Martial'
    assert weapon_preview.handedness.text == 'One or Two Handed'
    assert weapon_preview.weight.text == '4 lbs.'
    assert weapon_preview.range_.text == '5 ft.'
    assert weapon_preview.damage_type.text == 'Slashing'
    assert weapon_preview.property_.text == 'Versatile'
    assert '' in weapon_preview.description.text

def test_add_weapon_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in weapon table to open
       the weapon add modal."""
    print(('As a player, I can click the first row in weapon table to open '
           'the weapon add modal.'))

    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    rows = ut.get_table_rows(weapon_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()

def test_autocomplete_weapon(player_wizard, browser): # noqa
    """As a player, if I start typing in the autocomplete inputs, I can select
       suggested items in the dropdown."""
    print(('As a player, if I start typing in the autocomplete inputs, I can '
           ' select suggested items in the dropdown.'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    ut.select_from_autocomplete(weapon_add, 'type_', '', browser)
    ut.select_from_autocomplete(weapon_add, 'handedness', '', browser)
    ut.select_from_autocomplete(weapon_add, 'proficiency', '', browser)
    ut.select_from_autocomplete(weapon_add, 'damage_type', '', browser)
    ut.select_from_autocomplete(weapon_add, 'property_', '', browser)

    assert weapon_add.name.get_attribute('value') == 'Battleaxe'
    assert weapon_add.type_.get_attribute('value') == 'Melee'
    assert weapon_add.handedness.get_attribute('value') == 'One or Two Handed'
    assert weapon_add.proficiency.get_attribute('value') == 'Martial'
    assert weapon_add.damage_type.get_attribute('value') == 'Acid'
    assert weapon_add.property_.get_attribute('value') == 'Ammunition'


def test_weapon_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from weapon name field, OGL data auto-completes
       and the remaining fields pre-populate."""
    print(('As a player, if I select from weapon name field, OGL data '
           'auto-completes and the remaining fields pre-populate.'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    row = ut.get_table_row(weapon_table, 'table', 1)

    assert row.weapon.strip() == 'Battleaxe'
    assert row.to_hit == '+ 6'
    assert row.damage == '1d8 or 1d10'
    assert row.damage_type == 'Slashing'
    assert row.range == '5 ft.'
    assert row.property == 'Versatile'
    assert row.quantity == '1'


def test_weapon_magical_modifier(player_wizard, browser): # noqa
    """As a player, if weapon is magical, a badge indicating the modifier
       is present."""
    print(('As a player, if weapon is magical, a badge indicating the '
           'modifier is present.'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    weapon_table.add.click()
    weapon_add.name = 'Add Name'
    weapon_add.magical_modifier = 3

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    row = ut.get_table_row(weapon_table, 'table', 1)

    assert row.weapon == 'Add Name  + 3'


def test_weapon_persists(player_wizard, browser): # noqa
    """As a player, all fields for weapon persist after page refresh."""
    print('As a player, all fields for weapon persist after page refresh.')

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_edit = weapon.WeaponEditModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    weapon_tabs = weapon.WeaponModalTabs(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    browser.refresh()

    row = ut.get_table_row(weapon_table, 'table', 1)

    assert row.weapon.strip() == 'Battleaxe'
    assert row.to_hit == '+ 6'
    assert row.damage == '1d8 or 1d10'
    assert row.damage_type == 'Slashing'
    assert row.range == '5 ft.'
    assert row.property == 'Versatile'
    assert row.quantity == '1'

    row = ut.get_table_row(weapon_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_tabs.edit_id)
        )
    )

    weapon_tabs.edit.click()

    assert weapon_edit.name.get_attribute('value') == 'Battleaxe'
    assert weapon_edit.damage.get_attribute('value') == '1d8 or 1d10'
    assert weapon_edit.magical_modifier.get_attribute('value') == '0'
    assert weapon_edit.to_hit_modifier.get_attribute('value') == '0'
    assert weapon_edit.type_.get_attribute('value') == 'Melee'
    assert weapon_edit.handedness.get_attribute('value') == 'One or Two Handed'
    assert weapon_edit.proficiency.get_attribute('value') == 'Martial'
    assert weapon_edit.price.get_attribute('value') == '10'
    assert weapon_edit.currency_denomination.get_attribute('value') == 'GP'
    assert weapon_edit.weight.get_attribute('value') == '4'
    assert weapon_edit.range_.get_attribute('value') == ''
    assert weapon_edit.damage_type.get_attribute('value') == 'Slashing'
    assert weapon_edit.property_.get_attribute('value') == 'Versatile'
    assert weapon_edit.quantity.get_attribute('value') == '1'
    assert weapon_edit.description.get_attribute('value') == ''


def test_weapon_total_weight(player_wizard, browser): # noqa
    """As a player, in the weapon table, total weight is calculated
       correctly."""
    print(('As a player, in the armor table, total weight is calculated '
           'correctly'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    assert weapon_table.total_weight.text == '8 (lbs)'


def test_melee_ft(player_wizard, browser): # noqa
    """As a player, if I add a melee weapon, the range of 5 ft. is assigned
       after I close the modal."""
    print(('As a player, if I add a melee weapon, the range of 5 ft. is '
           'assigned after I close the modal'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()

    weapon_add.name = 'Test name'
    weapon_add.type_ = 'Melee'

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_add.add_id)
        )
    )

    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    row = ut.get_table_row(weapon_table, 'table', values=False)

    assert row[4].text == '5 ft.'


def test_ranged_ft(player_wizard, browser): # noqa
    """As a player, if I add a ranged weapon, ft. is appended to the range
       after I close the modal."""
    print(('As a player, if I add a ranged weapon, ft. is appended to the '
           'range after I close the modal'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    weapon_add.name = 'Test name'
    weapon_add.type_ = 'Ranged'
    weapon_add.range_ = '25'

    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    row = ut.get_table_row(weapon_table, 'table', values=False)

    assert row[4].text == '25 ft.'


def test_reach_ft(player_wizard, browser): # noqa
    """As a player, if I add a weapon with property reach, 5 ft. is added
       after I close the modal."""
    print(('As a player, if I add a weapon with property reach, 5 ft. is '
           'added after I close the modal'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    weapon_add.name = 'Test name'
    weapon_add.type_ = 'Melee'
    weapon_add.property_ = 'Reach'
    weapon_add.range_ = '5'
    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    row = ut.get_table_row(weapon_table, 'table', values=False)

    assert row[4].text == '10 ft.'


def test_weapon_sorting(player_wizard, browser): # noqa
    """As a player, I can sort the weapon table by clicking on the
       sortable columns."""
    print(('As a player, I can sort the weapon table by clicking on the '
           ' sortable columns'))

    weapon_add = weapon.WeaponAddModal(browser)
    weapon_table = weapon.WeaponTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, weapon_table.add_id)
        )
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser)
    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    weapon_table.add.click()
    ut.select_from_autocomplete(weapon_add, 'name', '', browser, arrow_down_count=2)
    weapon_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(weapon_add.modal_div_id)
    )

    weapon_table.weapon_header.click()

    WebDriverWait(browser, 5).until(
        sorting_arrow_down(
            weapon_table.weapon_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[0].text.strip() == 'Blowgun'

    weapon_table.to_hit_header.click()
    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            weapon_table.to_hit_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[1].text.strip() == '+ 6'

    weapon_table.damage_header.click()
    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            weapon_table.damage_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[2].text.strip() == '1'

    weapon_table.damage_type_header.click()
    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            weapon_table.damage_type_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[3].text.strip() == 'Piercing'

    weapon_table.damage_type_header.click()
    WebDriverWait(browser, 5).until(
        sorting_arrow_down(
            weapon_table.damage_type_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[3].text.strip() == 'Slashing'

    weapon_table.range_header.click()
    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            weapon_table.range_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[4].text.strip() == '5 ft.'

    weapon_table.property_header.click()
    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            weapon_table.property_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[5].text.strip() == 'Ranged, Ammunition, and Loading'

    weapon_table.quantity_header.click()
    WebDriverWait(browser, 5).until(
        sorting_arrow_up(
            weapon_table.quantity_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(weapon_table, 'table', values=False)

    assert rows[6].text.strip() == '1'


def test_add_armor(player_wizard, browser): # noqa
    """As a player, I can add an armor."""
    print('As a player, I can add an armor.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    stub = ArmorFactory.stub()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    armor_add.name = stub.name
    armor_add.type_ = stub.type_
    armor_add.magical_modifier = stub.magical_modifier
    armor_add.price = stub.price
    armor_add.currency_denomination = stub.currency_denomination
    armor_add.weight = stub.weight
    armor_add.armor_class = stub.armor_class
    armor_add.stealth = stub.stealth
    armor_add.stealth.send_keys(Keys.TAB)
    armor_add.don.click()
    armor_add.description = stub.description

    assert armor_add.name.get_attribute('value') == stub.name
    assert armor_add.type_.get_attribute('value') == stub.type_
    assert int(armor_add.magical_modifier.get_attribute('value')) == stub.magical_modifier
    assert int(armor_add.price.get_attribute('value')) == stub.price
    assert armor_add.currency_denomination.get_attribute('value') == stub.currency_denomination
    assert int(armor_add.weight.get_attribute('value')) == stub.weight
    assert int(armor_add.armor_class.get_attribute('value')) == stub.armor_class
    assert armor_add.stealth.get_attribute('value') == stub.stealth
    assert 'active' in armor_add.don.get_attribute('class')
    assert armor_add.description.get_attribute('value') == stub.description

    armor_add.add.click()

    row = ut.get_table_row(armor_table, 'table', 1)

    assert row.armor == '{}  + {}'.format(
        stub.name, stub.magical_modifier
    )
    assert int(row.armor_class) == stub.armor_class
    assert row.type == stub.type_

def test_delete_armor(player_wizard, browser): # noqa
    """As a player, I can delete an armor."""
    print('As a player, I can delete an armor.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    rows = ut.get_table_rows(armor_table, 'table', values=False)

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

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

    stub = ArmorFactory.stub()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    rows = ut.get_table_rows(armor_table, 'table', values=False)

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    rows[0][0].click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_tabs.edit_id)
        )
    )
    armor_tabs.edit.click()

    armor_edit.name = stub.name
    armor_edit.type_ = stub.type_
    armor_edit.magical_modifier = stub.magical_modifier
    armor_edit.price = stub.price
    armor_edit.currency_denomination = stub.currency_denomination
    armor_edit.weight = stub.weight
    armor_edit.armor_class = stub.armor_class
    armor_edit.stealth = stub.stealth
    armor_edit.stealth.send_keys(Keys.TAB)
    armor_edit.doff.click()
    armor_edit.description = stub.description

    assert armor_edit.name.get_attribute('value') == stub.name
    assert armor_edit.type_.get_attribute('value') == stub.type_
    assert int(armor_edit.magical_modifier.get_attribute('value')) == stub.magical_modifier
    assert int(armor_edit.price.get_attribute('value')) == stub.price
    assert armor_edit.currency_denomination.get_attribute('value') == stub.currency_denomination
    assert int(armor_edit.weight.get_attribute('value')) == stub.weight
    assert int(armor_edit.armor_class.get_attribute('value')) == stub.armor_class
    assert armor_edit.stealth.get_attribute('value') == stub.stealth
    assert 'active' in armor_add.doff.get_attribute('class')
    assert armor_edit.description.get_attribute('value') == stub.description

    armor_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    WebDriverWait(browser, 10).until(
        table_cell_updated(
            armor_table,
            'armor',
            '{}  + {}'.format(stub.name, stub.magical_modifier),
            'table',
            1
        )
    )

    row = ut.get_table_row(armor_table, 'table', 1)

    assert row.armor == '{}  + {}'.format(stub.name, stub.magical_modifier)
    assert int(row.armor_class) == stub.armor_class
    assert row.type == stub.type_


def test_preview_armor(player_wizard, browser): # noqa
    """As a player, I can select a row in the armor table and view the item
       in the preview tab."""
    print(('As a player, I can select a row in the armor table and view '
           'the item in the preview tab'))

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    armor_preview = armor.ArmorPreviewModal(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    row = ut.get_table_row(armor_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, armor_preview.name_id), 'Breastplate'
        )
    )

    assert armor_preview.name.text == 'Breastplate'
    assert armor_preview.summary.text == 'AC 14'
    assert armor_preview.weight.text == 'Weight: 20 lbs.'
    assert armor_preview.stealth.text == 'Stealth: Normal'
    assert 'metal chest piece' in armor_preview.description.text

def test_add_armor_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in armor table to open the
       armor add modal."""
    print(('As a player, I can click the first row in armor table to open '
           'the armor add modal.'))

    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    rows = ut.get_table_rows(armor_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()

def test_autocomplete_armor(player_wizard, browser): # noqa
    """As a player, if I start typing in the name, type and stealth field, I
       can select suggested items in the dropdown."""
    print(('As a player, if I start typing in the name, type and stealth '
           'field, I can select suggested items in the dropdown.'))

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    ut.select_from_autocomplete(armor_add, 'type_', '', browser)
    ut.select_from_autocomplete(armor_add, 'stealth', '', browser)

    assert armor_add.name.get_attribute('value') == 'Breastplate'
    assert armor_add.type_.get_attribute('value') == 'Light'
    assert armor_add.stealth.get_attribute('value') == 'Advantage'

def test_armor_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from armor name field, OGL data auto-completes
       and the remaining fields pre-populate."""
    print(('As a player, if I select from armor name field, OGL data '
           'auto-completes and the remaining fields pre-populate.'))

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )
    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    row = ut.get_table_row(armor_table, 'table', 1)

    assert row.armor.strip() == 'Breastplate'
    assert row.armor_class == '14'
    assert row.type == 'Medium'

def test_magical_modifier(player_wizard, browser): # noqa
    """As a player, if armor is magical, a badge indicating the modifier
       is present."""
    print(('As a player, if armor is magical, a badge indicating the '
           'modifier is present.'))

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    stub = ArmorFactory.stub()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    armor_add.name = stub.name
    armor_add.magical_modifier = stub.magical_modifier

    armor_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    row = ut.get_table_row(armor_table, 'table', 1)

    assert row.armor == '{}  + {}'.format(stub.name, stub.magical_modifier)

def test_armor_persists(player_wizard, browser): # noqa
    """As a player, all fields for armor persist after page refresh."""
    print('As a player, all fields for armor persist after page refresh.')

    armor_add = armor.ArmorAddModal(browser)
    armor_edit = armor.ArmorEditModal(browser)
    armor_table = armor.ArmorTable(browser)
    armor_tabs = armor.ArmorModalTabs(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    browser.refresh()

    row = ut.get_table_row(armor_table, 'table', 1)

    assert row.armor.strip() == 'Breastplate'
    assert row.armor_class == '14'
    assert row.type == 'Medium'

    row = ut.get_table_row(armor_table, 'table', values=False)
    row[0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_tabs.edit_id)
        )
    )

    armor_tabs.edit.click()

    assert armor_edit.name.get_attribute('value') == 'Breastplate'
    assert armor_edit.armor_class.get_attribute('value') == '14'
    assert armor_edit.type_.get_attribute('value') == 'Medium'
    assert armor_edit.magical_modifier.get_attribute('value') == '0'
    assert armor_edit.price.get_attribute('value') == '400'
    assert armor_edit.currency_denomination.get_attribute('value') == 'GP'
    assert armor_edit.weight.get_attribute('value') == '20'
    assert armor_edit.armor_class.get_attribute('value') == '14'
    assert armor_edit.stealth.get_attribute('value') == 'Normal'
    assert 'armor consists of' in armor_edit.description.get_attribute('value')


def test_armor_donned(player_wizard, browser): # noqa
    """As a player, the checkbox appears when armor is donned."""
    print('As a player, the checkbox appears when armor is donned.')

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    stub = ArmorFactory.stub()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    armor_add.name = stub.name
    armor_add.don.click()

    armor_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    row = ut.get_table_row(armor_table, 'table', 1, values=False)

    assert 'fa fa-check' in row[0].find_element_by_tag_name('span').get_attribute('class')

def test_armor_total_weight(player_wizard, browser): # noqa
    """As a player, in the armor table, total weight is calculated
       correctly."""
    print(('As a player, in the armor table, total weight is calculated '
           'correctly'))

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, armor_table.total_weight_id),
            '40 (lbs)'
        )
    )

    assert armor_table.total_weight.text == '40 (lbs)'


def test_armor_sorting(player_wizard, browser): # noqa
    """As a player, I can sort the armor table by clicking on the sortable
       columns."""
    print(('As a player, I can sort the armor table by clicking on the '
           'sortable columns'))

    armor_add = armor.ArmorAddModal(browser)
    armor_table = armor.ArmorTable(browser)
    tabs = Tabs(browser)
    tabs.equipment.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, armor_table.add_id)
        )
    )

    armor_table.add.click()
    ut.select_from_autocomplete(armor_add, 'name', '', browser)
    armor_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    armor_table.add.click()
    ut.select_from_autocomplete(
        armor_add, 'name', '', browser, arrow_down_count=2
    )
    armor_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(armor_add.modal_div_id)
    )

    armor_table.armor_header.click()
    WebDriverWait(browser, 10).until(
        sorting_arrow_down(
            armor_table.armor_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(armor_table, 'table', values=False)

    assert rows[1].text.strip() == 'Chain mail'

    armor_table.type_header.click()
    WebDriverWait(browser, 10).until(
        sorting_arrow_up(
            armor_table.type_header_sorting_arrow,
        )
    )
    rows = ut.get_table_row(armor_table, 'table', values=False)

    assert rows[2].text.strip() == 'Heavy'
