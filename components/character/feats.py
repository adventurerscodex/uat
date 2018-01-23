"""feat components."""

from modules.element import Element, Component


class FeatAddModal(Component):
    """Definition of feat add modal component."""

    name = Element(id_='featAddNameInput')
    description = Element(id_='featAddDescriptionTextarea')
    tracked = Element(id_='featAddTrackedCheckbox')
    max_ = Element(id_='featAddMaxInput')
    short_rest = Element(id_='featAddShortRestInput')
    long_rest = Element(id_='featAddLongRestInput')
    add = Element(id_='featAddAddButton')


class FeatEditModal(Component):
    """Definition of feat edit modal component."""

    name = Element(id_='featEditNameInput')
    description = Element(id_='featEditDescriptionTextarea')
    tracked = Element(id_='featEditTrackedCheckbox')
    max_ = Element(id_='featEditMaxInput')
    short_rest = Element(id_='featEditShortRestInput')
    long_rest = Element(id_='featEditLongRestInput')
    done = Element(id_='featEditDoneButton')


class FeatModalTabs(Component):
    """Definition of feat modal tabs component."""

    preview = Element(id_='featModalPreview')
    edit = Element(id_='featModalEdit')


class FeatsTable(Component):
    """Definition of feats edit modal componenet."""

    add = Element(id_='featAddIcon')
    table = Element(id_='featTable')
