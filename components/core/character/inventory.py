"""Inventory components."""

from modules.element import Element, Component


class InventoryAddModal(Component):
    """Definition of inventory add modal component."""

    name = Element(id_='inventoryAddNameInput')
    weight = Element(id_='inventoryAddWeightInput')
    quantity = Element(id_='inventoryAddQuantityInput')
    cost = Element(id_='inventoryAddCostInput')
    currency_denomination = Element(id_='inventoryAddCurrencyDenominationInput')
    description = Element(id_='inventoryAddDescriptionTextarea')
    add = Element(id_='inventoryAddAddButton')
    cancel = Element(id_='inventoryAddCancelButton')


class InventoryEditModal(Component):
    """Definition of inventory edit modal component."""

    name = Element(id_='inventoryEditNameInput')
    weight = Element(id_='inventoryEditWeightInput')
    quantity = Element(id_='inventoryEditQuantityInput')
    cost = Element(id_='inventoryEditCostInput')
    currency_denomination = Element(id_='inventoryEditCurrencyDenominationInput')
    description = Element(id_='inventoryEditDescriptionTextarea')
    done = Element(id_='inventoryEditDoneButton')


class InventoryPreviewModal(Component):
    """Definition of inventory preview modal component."""

    name = Element(id_='inventoryPreviewNameLabel')
    weight = Element(id_='inventoryPreviewWeightLabel')
    quantity = Element(id_='inventoryPreviewQuantityInput')
    cost = Element(id_='inventoryPreviewCostInput')
    description = Element(id_='InventoryPreviewDescriptionTextarea')
    done = Element(id_='inventoryDoneButton')


class InventoryModalTabs(Component):
    """Definition of inventory modal tabs component."""

    preview = Element(id_='inventoryModalPreviewTab')
    edit = Element(id_='inventoryModalEditTab')


class InventoryTable(Component):
    """Definition of inventorys edit modal componenet."""

    add = Element(id_='inventoryAddIcon')
    table = Element(id_='inventoryTable')
