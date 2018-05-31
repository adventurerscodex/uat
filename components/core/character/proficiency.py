"""Proficiency components."""

from component_objects import Component, Element


class ProficiencyAddModal(Component):
    """Definition of proficiency add modal component."""

    modal_div_id = 'addProficiency'
    name_id = 'proficiencyAddNameInput'
    type_id = 'proficiencyAddTypeInput'
    description_id = 'proficiencyAddDescriptionTextarea'
    add_id = 'proficiencyAddAddButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    type_ = Element(id_=type_id)
    description = Element(id_=description_id)
    add = Element(id_=add_id)


class ProficiencyEditModal(Component):
    """Definition of proficiency edit modal component."""

    modal_div_id = 'viewProficiency'
    name_id = 'proficiencyEditNameInput'
    type_id = 'proficiencyEditTypeInput'
    description_id = 'proficiencyEditDescriptionTextarea'
    done_id = 'proficiencyEditDoneButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    type_ = Element(id_=type_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class ProficiencyModalTabs(Component):
    """Definition of proficiency modal tabs component."""

    preview_id = 'proficiencyModalPreview'
    edit_id = 'proficiencyModalEdit'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class ProficiencyTable(Component):
    """Definition of proficiencys edit modal componenet."""

    add_id = 'proficiencyAddIcon'
    table_id = 'proficiencyTable'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
