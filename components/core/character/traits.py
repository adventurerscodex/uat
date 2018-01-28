"""Trait components."""

from modules.element import Element, Component


class TraitAddModal(Component):
    """Definition of trait add modal component."""

    name = Element(id_='traitAddNameInput')
    race = Element(id_='traitAddRaceInput')
    description = Element(id_='traitAddDescriptionTextarea')
    tracked = Element(id_='traitAddTrackedCheckbox')
    max_ = Element(id_='traitAddMaxInput')
    short_rest = Element(id_='traitAddShortRestInput')
    long_rest = Element(id_='traitAddLongRestInput')
    add = Element(id_='traitAddAddButton')


class TraitEditModal(Component):
    """Definition of trait edit modal component."""

    name = Element(id_='traitEditNameInput')
    race = Element(id_='traitEditRaceInput')
    description = Element(id_='traitEditDescriptionTextarea')
    tracked = Element(id_='traitEditTrackedCheckbox')
    max_ = Element(id_='traitEditMaxInput')
    short_rest = Element(id_='traitEditShortRestInput')
    long_rest = Element(id_='traitEditLongRestInput')
    done = Element(id_='traitEditDoneButton')


class TraitModalTabs(Component):
    """Definition of trait modal tabs component."""

    preview = Element(id_='traitModalPreview')
    edit = Element(id_='traitModalEdit')


class TraitsTable(Component):
    """Definition of traits edit modal componenet."""

    add = Element(id_='traitAddIcon')
    table = Element(id_='traitTable')
