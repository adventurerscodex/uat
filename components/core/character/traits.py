"""Trait components."""

from modules.element import Element, Component


class TraitAddModal(Component):
    """Definition of trait add modal component."""

    modal_div_id = 'addTrait'
    name_id = 'traitAddNameInput'
    race_id = 'traitAddRaceInput'
    description_id = 'traitAddDescriptionTextarea'
    tracked_id = 'traitAddTrackedCheckbox'
    max_id = 'traitAddMaxInput'
    short_rest_id = 'traitAddShortRestInput'
    long_rest_id = 'traitAddLongRestInput'
    add_id = 'traitAddAddButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    race = Element(id_=race_id)
    description = Element(id_=description_id)
    tracked = Element(id_=tracked_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    add = Element(id_=add_id)


class TraitEditModal(Component):
    """Definition of trait edit modal component."""

    modal_div_id = 'viewWeapon'
    name_id = 'traitEditNameInput'
    race_id = 'traitEditRaceInput'
    description_id = 'traitEditDescriptionTextarea'
    tracked_id = 'traitEditTrackedCheckbox'
    max_id = 'traitEditMaxInput'
    short_rest_id = 'traitEditShortRestInput'
    long_rest_id = 'traitEditLongRestInput'
    done_id = 'traitEditDoneButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    race = Element(id_=race_id)
    description = Element(id_=description_id)
    tracked = Element(id_=tracked_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    done = Element(id_=done_id)


class TraitModalTabs(Component):
    """Definition of trait modal tabs component."""

    preview_id = 'traitModalPreview'
    edit_id = 'traitModalEdit'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class TraitsTable(Component):
    """Definition of traits edit modal componenet."""

    add_id = 'traitAddIcon'
    table_id = 'traitTable'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
