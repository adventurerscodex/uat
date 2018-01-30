"""Proficiency components."""

from modules.element import Element, Component


class ProficiencyAddModal(Component):
    """Definition of proficiency add modal component."""

    name = Element(id_='proficiencyAddNameInput')
    type_ = Element(id_='proficiencyAddTypeInput')
    description = Element(id_='proficiencyAddDescriptionTextarea')
    add = Element(id_='proficiencyAddAddButton')


class ProficiencyEditModal(Component):
    """Definition of proficiency edit modal component."""

    name = Element(id_='proficiencyEditNameInput')
    type_ = Element(id_='proficiencyEditTypeInput')
    description = Element(id_='proficiencyEditDescriptionTextarea')
    done = Element(id_='proficiencyEditDoneButton')


class ProficiencyModalTabs(Component):
    """Definition of proficiency modal tabs component."""

    preview = Element(id_='proficiencyModalPreview')
    edit = Element(id_='proficiencyModalEdit')


class ProficiencyTable(Component):
    """Definition of proficiencys edit modal componenet."""

    add = Element(id_='proficiencyAddIcon')
    table = Element(id_='proficiencyTable')
