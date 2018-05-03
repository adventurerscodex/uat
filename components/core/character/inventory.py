"""Inventory components."""

from component_objects import Element, Component


class InventoryAddModal(Component):
    """Definition of inventory add modal component."""

    modal_div_id = 'addItem'
    name_id = 'inventoryAddNameInput'
    weight_id = 'inventoryAddWeightInput'
    quantity_id = 'inventoryAddQuantityInput'
    cost_id = 'inventoryAddCostInput'
    currency_denomination_id = 'inventoryAddCurrencyDenominationInput'
    description_id = 'inventoryAddDescriptionTextarea'
    add_id = 'inventoryAddAddButton'
    cancel_id = 'inventoryAddCancelButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    weight = Element(id_=weight_id)
    quantity = Element(id_=quantity_id)
    cost = Element(id_=cost_id)
    currency_denomination = Element(id_=currency_denomination_id)
    description = Element(id_=description_id)
    add = Element(id_=add_id)
    cancel = Element(id_=cancel_id)


class InventoryEditModal(Component):
    """Definition of inventory edit modal component."""

    modal_div_id = 'viewItem'
    name_id = 'inventoryEditNameInput'
    weight_id = 'inventoryEditWeightInput'
    quantity_id = 'inventoryEditQuantityInput'
    cost_id = 'inventoryEditCostInput'
    currency_denomination_id = 'inventoryEditCurrencyDenominationInput'
    description_id = 'inventoryEditDescriptionTextarea'
    done_id = 'inventoryEditDoneButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    weight = Element(id_=weight_id)
    quantity = Element(id_=quantity_id)
    cost = Element(id_=cost_id)
    currency_denomination = Element(id_=currency_denomination_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class InventoryPreviewModal(Component):
    """Definition of inventory preview modal component."""

    name_id = 'inventoryPreviewNameLabel'
    weight_id = 'inventoryPreviewWeightLabel'
    quantity_id = 'inventoryPreviewQuantityInput'
    cost_id = 'inventoryPreviewCostInput'
    description_id = 'InventoryPreviewDescriptionTextarea'
    done_id = 'inventoryDoneButton'

    name = Element(id_=name_id)
    weight = Element(id_=weight_id)
    quantity = Element(id_=quantity_id)
    cost = Element(id_=cost_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class InventoryModalTabs(Component):
    """Definition of inventory modal tabs component."""

    preview_id = 'inventoryModalPreviewTab'
    edit_id = 'inventoryModalEditTab'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class InventoryTable(Component):
    """Definition of inventorys edit modal componenet."""

    add_id = 'inventoryAddIcon'
    table_id = 'inventoryTable'
    item_header_id = 'inventoryTableItemHeader'
    item_header_sorting_arrow_xpath = '//*[@id="inventoryTableItemHeader"]/span'
    quantity_header_id = 'inventoryTableQuantityHeader'
    quantity_header_sorting_arrow_xpath = '//*[@id="inventoryTableQuantityHeader"]/span'
    weight_header_id = 'inventoryTableWeightHeader'
    wegith_header_sorting_arrow_xpath = '//*[@id="inventoryTableWeightHeader"]/span'
    cost_header_id = 'inventoryTableCostHeader'
    cost_header_sorting_arrow_xpath = '//*[@id="inventoryTableCostHeader"]/span'
    total_weight_id = 'inventoryTableTotalWeightSpan'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
    item_header = Element(id_=item_header_id)
    item_header_sorting_arrow = Element(xpath=item_header_sorting_arrow_xpath)
    quantity_header = Element(id_=quantity_header_id)
    quantity_header_sorting_arrow = Element(xpath=quantity_header_sorting_arrow_xpath)
    weight_header = Element(id_=weight_header_id)
    weight_header_sorting_arrow = Element(xpath=wegith_header_sorting_arrow_xpath)
    cost_header = Element(id_=cost_header_id)
    cost_header_sorting_arrow = Element(xpath=cost_header_sorting_arrow_xpath)
    total_weight = Element(id_=total_weight_id)
