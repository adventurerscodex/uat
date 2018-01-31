"""MagicItems components."""

from modules.element import Element, Component


class MagicItemsAddModal(Component):
    """Definition of magicItems add modal component."""

    item = Element(id_='magicItemsAddItemInput')
    type_ = Element(id_='magicItemsAddTypeInput')
    rarity = Element(id_='magicItemsAddRarityInput')
    max_charges = Element(id_='magicItemsAddMaxChargesInput')
    weight = Element(id_='magicItemsAddWeightInput')
    requires_attunement = Element(id_='magicItemsAddRequiresAttunementCheckbox')
    attuned = Element(id_='magicItemsAddAttunedCheckbox')
    description = Element(id_='magicItemsAddDescriptionTextarea')
    add = Element(id_='magicItemsAddAddButton')
    cancel = Element(id_='magicItemsAddCancelButton')


class MagicItemsEditModal(Component):
    """Definition of magicItems edit modal component."""

    item = Element(id_='magicItemsEditItemInput')
    type_ = Element(id_='magicItemsEditTypeInput')
    rarity = Element(id_='magicItemsEditRarityInput')
    max_charges = Element(id_='magicItemsEditMaxChargesInput')
    weight = Element(id_='magicItemsEditWeightInput')
    requires_attunement = Element(id_='magicItemsEditRequiresAttunementCheckbox')
    attuned = Element(id_='magicItemsEditAttunedCheckbox')
    description = Element(id_='magicItemsEditDescriptionTextarea')
    add = Element(id_='magicItemsEditAddButton')
    cancel = Element(id_='magicItemsEditCancelButton')


class MagicItemsPreviewModal(Component):
    """Definition of magicItems preview modal component."""

    item = Element(id_='magicItemsPreviewItemInput')
    type_ = Element(id_='magicItemsPreviewTypeInput')
    max_charges = Element(id_='magicItemsPreviewMaxChargesInput')
    weight = Element(id_='magicItemsPreviewWeightInput')
    description = Element(id_='magicItemsPreviewDescriptionTextarea')
    done = Element(id_='magicItemsPreviewDoneButton')


class MagicItemsModalTabs(Component):
    """Definition of magicItems modal tabs component."""

    preview = Element(id_='magicItemsModalPreviewTab')
    edit = Element(id_='magicItemsModalEditTab')


class MagicItemsTable(Component):
    """Definition of magicItemss edit modal componenet."""

    add = Element(id_='magicItemsAddIcon')
    table = Element(id_='magicItemsTable')
