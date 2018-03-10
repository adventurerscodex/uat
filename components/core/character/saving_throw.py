"""Saving Throw components."""

from modules.element import Element, Component


class SavingThrowEditModal(Component):
    """Definition of Saving Throw edit modal component."""

    name = Element(id_='savingThrowEditNameInput')
    modifier = Element(id_='savingThrowEditModifierButton')
    proficiency = Element(id_='savingThrowEditProficiencyCheckbox')
    done = Element(id_='savingThrowEditDoneButton')


class SavingThrowTable(Component):
    """Definition of savingsThrow edit modal componenet."""

    sort_by_saving_throw = Element(id_='savingThrowTableSortSavingThrowSpan')
    table = Element(id_='savingThrowTable')
    edit_charisma = Element(xpath='//*[@id="savingThrowTable"]/tbody/tr[1]/td[1]')
