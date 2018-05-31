"""Saving Throw components."""

from component_objects import Component, Element


class SavingThrowEditModal(Component):
    """Definition of Saving Throw edit modal component."""

    modal_div_id = 'viewSavingThrow'
    name_id = 'savingThrowEditNameInput'
    modifier_id = 'savingThrowEditModifierButton'
    proficiency_id = 'savingThrowEditProficiencyCheckbox'
    done_id = 'savingThrowEditDoneButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    modifier = Element(id_=modifier_id)
    proficiency = Element(id_=proficiency_id)
    done = Element(id_=done_id)


class SavingThrowTable(Component):
    """Definition of savingsThrow edit modal componenet."""

    sort_by_saving_throw_id = 'savingThrowTableSortSavingThrowSpan'
    table_id = 'savingThrowTable'
    edit_charisma_xpath = '//*[@id="savingThrowTable"]/tbody/tr[1]/td[1]'

    sort_by_saving_throw = Element(id_=sort_by_saving_throw_id)
    table = Element(id_=table_id)
    edit_charisma = Element(xpath=edit_charisma_xpath)
