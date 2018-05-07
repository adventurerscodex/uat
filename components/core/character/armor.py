"""Armor components."""

from component_objects import Element, Component


class ArmorAddModal(Component):
    """Definition of armor add modal component."""

    modal_div_id = 'addArmor'
    name_id = 'armorAddNameInput'
    type_id = 'armorAddTypeInput'
    magical_modifier_id = 'armorAddMagicalModifierInput'
    price_id = 'armorAddPriceInput'
    currency_denomination_id = 'armorAddCurrencyDenominationInput'
    weight_id = 'armorAddWeightInput'
    armor_class_id = 'armorAddArmorClassInput'
    stealth_id = 'armorAddStealthInput'
    don_id = 'armorAddDonButton'
    doff_id = 'armorAddDoffButton'
    description_id = 'armorAddDescriptionTextarea'
    add_id = 'armorAddAddButton'
    cancel_id = 'armorAddCancelButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    type_ = Element(id_=type_id)
    magical_modifier = Element(id_=magical_modifier_id)
    price = Element(id_=price_id)
    currency_denomination = Element(id_=currency_denomination_id)
    weight = Element(id_=weight_id)
    armor_class = Element(id_=armor_class_id)
    stealth = Element(id_=stealth_id)
    don = Element(id_=don_id)
    doff = Element(id_=doff_id)
    description = Element(id_=description_id)
    add = Element(id_=add_id)
    cancel = Element(id_=cancel_id)


class ArmorEditModal(Component):
    """Definition of armor edit modal component."""

    name_id = 'armorEditNameInput'
    type_id = 'armorEditTypeInput'
    magical_modifier_id = 'armorEditMagicalModifierInput'
    price_id = 'armorEditPriceInput'
    currency_denomination_id = 'armorEditCurrencyDenominationInput'
    weight_id = 'armorEditWeightInput'
    armor_class_id = 'armorEditArmorClassInput'
    stealth_id = 'armorEditStealthInput'
    don_id = 'armorEditDonButton'
    doff_id = 'armorEditDoffButton'
    description_id = 'armorEditDescriptionTextarea'
    done_id = 'armorEditDoneButton'

    name = Element(id_=name_id)
    type_ = Element(id_=type_id)
    magical_modifier = Element(id_=magical_modifier_id)
    price = Element(id_=price_id)
    currency_denomination = Element(id_=currency_denomination_id)
    weight = Element(id_=weight_id)
    armor_class = Element(id_=armor_class_id)
    stealth = Element(id_=stealth_id)
    don = Element(id_=don_id)
    doff = Element(id_=doff_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class ArmorPreviewModal(Component):
    """Definition of armor preview modal component."""

    name_id = 'armorPreviewNameLabel'
    summary_id = 'armorPreviewSummaryLabel'
    weight_id = 'armorPreviewWeightLabel'
    stealth_id = 'armorPreviewStealthLabel'
    description_id = 'ArmorPreviewDescriptionTextarea'
    done_id = 'armorPreviewDoneButton'

    name = Element(id_=name_id)
    summary = Element(id_=summary_id)
    weight = Element(id_=weight_id)
    stealth = Element(id_=stealth_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class ArmorModalTabs(Component):
    """Definition of armor modal tabs component."""

    preview_id = 'armorModalPreviewTab'
    edit_id = 'armorModalEditTab'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class ArmorTable(Component):
    """Definition of armors edit modal componenet."""

    add_id = 'armorAddIcon'
    table_id = 'armorTable'
    equipped_header_id = 'armorTableEquippedHeader'
    equipped_header_sorting_arrow_xpath = '//*[@id="armorTableEquippedHeader"]/span[2]'
    armor_header_id = 'armorTableArmorHeader'
    armor_header_sorting_arrow_xpath = '//*[@id="armorTableArmorHeader"]/span'
    type_header_id = 'armorTableTypeHeader'
    type_header_sorting_arrow_xpath = '//*[@id="armorTableTypeHeader"]/span'
    ac_header_id = 'armorTableAcHeader'
    ac_header_sorting_arrow_xpath = '//*[@id="armorTableAcHeader"]/span'
    total_weight_id = 'armorTableTotalWeightSpan'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
    equipped_header = Element(id_=equipped_header_id)
    equipped_header_sorting_arrow = Element(xpath=equipped_header_sorting_arrow_xpath)
    armor_header = Element(id_=armor_header_id)
    armor_header_sorting_arrow = Element(xpath=armor_header_sorting_arrow_xpath)
    type_header = Element(id_=type_header_id)
    type_header_sorting_arrow = Element(xpath=type_header_sorting_arrow_xpath)
    ac_header = Element(id_=ac_header_id)
    ac_header_sorting_arrow = Element(xpath=ac_header_sorting_arrow_xpath)
    total_weight = Element(id_=total_weight_id)
