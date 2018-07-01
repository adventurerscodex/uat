"""UAT test file for Adventurer's Codex dm tools encounters module."""
from components.core.dm.encounter_list import EncounterList
from components.core.dm.tabs import DMTabs
from components.core.dm.encounter_add_edit_modal import EncounterAddEditModal


def test_full_encounter(dm_wizard, browser):
    """This test will create a full encounter list"""
    print('This test will create a full encounter list')

    tabs = DMTabs(browser)

    tabs.encounters.click()

    assert tabs.encounters_label.text.strip() == 'Encounters'

    encounter_list = EncounterList(browser)

    encounter_list.add_plus_icon.click()

    encounter_add_edit_modal = EncounterAddEditModal(browser)

    encounter_add_edit_modal.encounter_name = 'Encounters'
    encounter_add_edit_modal.location = 'Location'
    encounter_add_edit_modal.environment.click()
    encounter_add_edit_modal.maps_and_images.click()
    encounter_add_edit_modal.points_of_interest.click()
    encounter_add_edit_modal.non_player_characters.click()
    encounter_add_edit_modal.monsters.click()
    encounter_add_edit_modal.treasure.click()
    encounter_add_edit_modal.done.click()

    assert encounter_list.added_list_encounter.text.strip() == 'Encounters'
