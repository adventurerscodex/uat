"""Weapon components."""

from component_objects import Element, Component


class WeaponAddModal(Component):
    """Definition of weapon add modal component."""

    modal_div_id = 'addWeapon'
    name_id = 'weaponAddNameInput'
    damage_id = 'weaponAddDamageInput'
    magical_modifier_id = 'weaponAddMagicalModifierInput'
    to_hit_modifier_id = 'weaponAddToHitModifierInput'
    type_id = 'weaponAddTypeInput'
    handedness_id = 'weaponAddHandednessInput'
    proficiency_id = 'weaponAddProficiencyInput'
    price_id = 'weaponAddPriceInput'
    currency_denomination_id = 'weaponAddCurrencyDenominationInput'
    weight_id = 'weaponAddWeightInput'
    range_id = 'weaponAddRangeInput'
    damage_type_id = 'weaponAddDamageTypeInput'
    property_id = 'weaponAddPropertyInput'
    quantity_id = 'weaponAddQuantityInput'
    description_id = 'weaponAddDescriptionTextarea'
    add_id = 'weaponAddAddButton'
    cancel_id = 'weaponAddCancelButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    damage = Element(id_=damage_id)
    magical_modifier = Element(id_=magical_modifier_id)
    to_hit_modifier = Element(id_=to_hit_modifier_id)
    type_ = Element(id_=type_id)
    handedness = Element(id_=handedness_id)
    proficiency = Element(id_=proficiency_id)
    price = Element(id_=price_id)
    currency_denomination = Element(id_=currency_denomination_id)
    weight = Element(id_=weight_id)
    range_ = Element(id_=range_id)
    damage_type = Element(id_=damage_type_id)
    property_ = Element(id_=property_id)
    quantity = Element(id_=quantity_id)
    description = Element(id_=description_id)
    add = Element(id_=add_id)
    cancel = Element(id_=cancel_id)


class WeaponEditModal(Component):
    """Definition of weapon edit modal component."""

    modal_div_id = 'editWeapon'
    name_id = 'weaponEditNameInput'
    damage_id = 'weaponEditDamageInput'
    magical_modifier_id = 'weaponEditMagicalModifierInput'
    to_hit_modifier_id = 'weaponEditToHitModifierInput'
    type_id = 'weaponEditTypeInput'
    handedness_id = 'weaponEditHandednessInput'
    proficiency_id = 'weaponEditProficiencyInput'
    price_id = 'weaponEditPriceInput'
    currency_denomination_id = 'weaponEditCurrencyDenominationInput'
    weight_id = 'weaponEditWeightInput'
    range_id = 'weaponEditRangeInput'
    damage_type_id = 'weaponEditDamageTypeInput'
    property_id = 'weaponEditPropertyInput'
    quantity_id = 'weaponEditQuantityInput'
    description_id = 'weaponEditDescriptionTextarea'
    done_id = 'weaponEditDoneButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    damage = Element(id_=damage_id)
    magical_modifier = Element(id_=magical_modifier_id)
    to_hit_modifier = Element(id_=to_hit_modifier_id)
    type_ = Element(id_=type_id)
    handedness = Element(id_=handedness_id)
    proficiency = Element(id_=proficiency_id)
    price = Element(id_=price_id)
    currency_denomination = Element(id_=currency_denomination_id)
    weight = Element(id_=weight_id)
    range_ = Element(id_=range_id)
    damage_type = Element(id_=damage_type_id)
    property_ = Element(id_=property_id)
    quantity = Element(id_=quantity_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class WeaponPreviewModal(Component):
    """Definition of weapon priview modal component."""

    name_id = 'weaponPreviewNameLabel'
    magical_modifier_id = 'weaponPreviewMagicalModifierLabel'
    damage_id = 'weaponPreviewDamageLabel'
    to_hit_modifier_id = 'weaponPreviewToHitModifierLabel'
    range_id = 'weaponPreviewRangeLabel'
    type_id = 'weaponPreviewTypeLabel'
    proficiency_id = 'weaponPreviewProficiencyLabel'
    handedness_id = 'weaponPreviewHandednessLabel'
    weight_id = 'weaponPreviewWeightLabel'
    range_id = 'weaponPreviewRangeLabel'
    damage_type_id = 'weaponPreviewDamageTypeLabel'
    property_id = 'weaponPreviewPropertyLabel'
    description_id = 'weaponPreviewDescriptionTextarea'
    done_xpath = '//*[@id="weaponsModalPreview"]/div[4]/button'

    name = Element(id_=name_id)
    magical_modifier = Element(id_=magical_modifier_id)
    damage = Element(id_=damage_id)
    to_hit_modifier = Element(id_=to_hit_modifier_id)
    range_ = Element(id_=range_id)
    type_ = Element(id_=type_id)
    proficiency = Element(id_=proficiency_id)
    handedness = Element(id_=handedness_id)
    weight = Element(id_=weight_id)
    range_ = Element(id_=range_id)
    damage_type = Element(id_=damage_type_id)
    property_ = Element(id_=property_id)
    description = Element(id_=description_id)
    done = Element(xpath=done_xpath)


class WeaponModalTabs(Component):
    """Definition of weapon modal tabs component."""

    preview_id = 'weaponModalPreviewTab'
    edit_id = 'weaponModalEditTab'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class WeaponTable(Component):
    """Definition of weapons edit modal componenet."""

    add_id = 'weaponAddIcon'
    table_id = 'weaponTable'
    weapon_header_id = 'weaponTableWeaponHeader'
    weapon_header_sorting_arrow_xpath = '//*[@id="weaponTableWeaponHeader"]/span'
    to_hit_header_id = 'weaponTableToHitHeader'
    to_hit_header_sorting_arrow_xpath = '//*[@id="weaponTableToHitHeader"]/span'
    damage_header_id = 'weaponTableDamageHeader'
    damage_header_sorting_arrow_xpath = '//*[@id="weaponTableDamageHeader"]/span'
    damage_type_header_id = 'weaponTableDamageTypeHeader'
    damage_type_header_sorting_arrow_xpath = '//*[@id="weaponTableDamageTypeHeader"]/span'
    range_header_id = 'weaponTableRangeHeader'
    range_header_sorting_arrow_xpath = '//*[@id="weaponTableRangeHeader"]/span'
    property_header_id = 'weaponTablePropertyHeader'
    property_header_sorting_arrow_xpath = '//*[@id="weaponTablePropertyHeader"]/span'
    quantity_header_id = 'weaponTableQuantityHeader'
    quantity_header_sorting_arrow_xpath = '//*[@id="weaponTableQuantityHeader"]/span'
    total_weight_id = 'weaponTableTotalWeightSpan'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
    weapon_header = Element(id_=weapon_header_id)
    weapon_header_sorting_arrow = Element(xpath=weapon_header_sorting_arrow_xpath)
    to_hit_header = Element(id_=to_hit_header_id)
    to_hit_header_sorting_arrow = Element(xpath=to_hit_header_sorting_arrow_xpath)
    damage_header = Element(id_=damage_header_id)
    damage_header_sorting_arrow = Element(xpath=damage_header_sorting_arrow_xpath)
    damage_type_header = Element(id_=damage_type_header_id)
    damage_type_header_sorting_arrow = Element(xpath=damage_type_header_sorting_arrow_xpath)
    range_header = Element(id_=range_header_id)
    range_header_sorting_arrow = Element(xpath=range_header_sorting_arrow_xpath)
    property_header = Element(id_=property_header_id)
    property_header_sorting_arrow = Element(xpath=property_header_sorting_arrow_xpath)
    quantity_header = Element(id_=quantity_header_id)
    quantity_header_sorting_arrow = Element(xpath=quantity_header_sorting_arrow_xpath)
    total_weight = Element(id_=total_weight_id)
