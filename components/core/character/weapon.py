"""Weapon components."""

from modules.element import Element, Component


class WeaponAddModal(Component):
    """Definition of weapon add modal component."""

    name = Element(id_='weaponAddNameInput')
    damage = Element(id_='weaponAddDamageInput')
    magical_modifier = Element(id_='weaponAddMagicalModifierInput')
    to_hit_modifier = Element(id_='weaponAddToHitModifierInput')
    type_ = Element(id_='weaponAddTypeInput')
    handedness = Element(id_='weaponAddHandednessInput')
    proficiency = Element(id_='weaponAddProficiencyInput')
    price = Element(id_='weaponAddPriceInput')
    currency_denomination = Element(id_='weaponAddCurrencyDenominationInput')
    weight = Element(id_='weaponAddWeightInput')
    range_ = Element(id_='weaponAddRangeInput')
    damage_type = Element(id_='weaponAddDamageTypeInput')
    property_ = Element(id_='weaponAddPropertyInput')
    quantity = Element(id_='weaponAddQuantityInput')
    description = Element(id_='weaponAddDescriptionTextarea')
    add = Element(id_='weaponAddAddButton')
    cancel = Element(id_='weaponAddCancelButton')


class WeaponEditModal(Component):
    """Definition of weapon edit modal component."""

    name = Element(id_='weaponEditNameInput')
    damage = Element(id_='weaponEditDamageInput')
    magical_modifier = Element(id_='weaponEditMagicalModifierInput')
    to_hit_modifier = Element(id_='weaponEditToHitModifierInput')
    type_ = Element(id_='weaponEditTypeInput')
    handedness = Element(id_='weaponEditHandednessInput')
    proficiency = Element(id_='weaponEditProficiencyInput')
    price = Element(id_='weaponEditPriceInput')
    currency_denomination = Element(id_='weaponEditCurrencyDenominationInput')
    weight = Element(id_='weaponEditWeightInput')
    range_ = Element(id_='weaponEditRangeInput')
    damage_type = Element(id_='weaponEditDamageTypeInput')
    property_ = Element(id_='weaponEditPropertyInput')
    quantity = Element(id_='weaponEditQuantityInput')
    description = Element(id_='weaponEditDescriptionTextarea')
    done = Element(id_='weaponEditDoneButton')


class WeaponPreviewModal(Component):
    """Definition of weapon priview modal component."""

    name = Element(id_='weaponPreviewNameLabel')
    magical_modifier = Element(id_='weaponPreviewMagicalModifierLabel')
    damage = Element(id_='weaponPreviewDamageLabel')
    to_hit_modifier = Element(id_='weaponPreviewToHitModifierLabel')
    range_ = Element(id_='weaponPreviewRangeLabel')
    type_ = Element(id_='weaponPreviewTypeLabel')
    proficiency = Element(id_='weaponPreviewProficiencyLabel')
    handedness = Element(id_='weaponPreviewHandednessLabel')
    weight = Element(id_='weaponPreviewWeightLabel')
    range_ = Element(id_='weaponPreviewRangeLabel')
    damage_type = Element(id_='weaponPreviewDamageTypeLabel')
    property_ = Element(id_='weaponPreviewPropertyLabel')
    description = Element(id_='weaponPreviewDescriptionTextarea')
    done = Element(id_='weaponPreviewCancelButton')


class WeaponModalTabs(Component):
    """Definition of weapon modal tabs component."""

    preview = Element(id_='weaponModalPreviewTab')
    edit = Element(id_='weaponModalEditTab')


class WeaponTable(Component):
    """Definition of weapons edit modal componenet."""

    add = Element(id_='weaponAddIcon')
    table = Element(id_='weaponTable')
    weapon_header = Element(id_='weaponTableWeaponHeader')
    to_hit_header = Element(id_='weaponTableToHitHeader')
    damage_header = Element(id_='weaponTableDamageHeader')
    damage_type_header = Element(id_='weaponTableDamageTypeHeader')
    range_header = Element(id_='weaponTableRangeHeader')
    property_header = Element(id_='weaponTablePropertyHeader')
    quantity_header = Element(id_='weaponTableQuantityHeader')
    total_weight = Element(id_='weaponTableTotalWeightSpan')
