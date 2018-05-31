"""Feat components."""

from component_objects import Component, Element


class FeatAddModal(Component):
    """Definition of feat add modal component."""

    modal_div_id = 'addFeat'
    name_id = 'featAddNameInput'
    description_id = 'featAddDescriptionTextarea'
    tracked_id = 'featAddTrackedCheckbox'
    max_id = 'featAddMaxInput'
    short_rest_id = 'featAddShortRestInput'
    long_rest_id = 'featAddLongRestInput'
    add_id = 'featAddAddButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    description = Element(id_=description_id)
    tracked = Element(id_=tracked_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    add = Element(id_=add_id)


class FeatEditModal(Component):
    """Definition of feat edit modal component."""

    modal_div_id = 'viewWeapon'
    name_id = 'featEditNameInput'
    description_id = 'featEditDescriptionTextarea'
    tracked_id = 'featEditTrackedCheckbox'
    max_id = 'featEditMaxInput'
    short_rest_id = 'featEditShortRestInput'
    long_rest_id = 'featEditLongRestInput'
    done_id = 'featEditDoneButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    description = Element(id_=description_id)
    tracked = Element(id_=tracked_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    done = Element(id_=done_id)


class FeatModalTabs(Component):
    """Definition of feat modal tabs component."""

    preview_id = 'featModalPreview'
    edit_id = 'featModalEdit'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class FeatsTable(Component):
    """Definition of feats edit modal componenet."""

    add_id = 'featAddIcon'
    table_id = 'featTable'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
