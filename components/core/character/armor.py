"""Armor components."""

from modules.element import Element, Component


class ArmorAddModal(Component):
    """Definition of armor add modal component."""

    name = Element(id_='armorAddNameInput')
    type_ = Element(id_='armorAddTypeInput')
    magical_modifier = Element(id_='armorAddMagicalModifierInput')
    price = Element(id_='armorAddPriceInput')
    currency_denomination = Element(id_='armorAddCurrencyDenominationInput')
    weight = Element(id_='armorAddWeightInput')
    armor_class = Element(id_='armorAddArmorClassInput')
    stealth = Element(id_='armorAddStealthInput')
    don = Element(id_='armorAddDonButton')
    doff = Element(id_='armorAddDoffButton')
    description = Element(id_='armorAddDescriptionTextarea')
    add = Element(id_='armorAddAddButton')
    cancel = Element(id_='armorAddCancelButton')


class ArmorEditModal(Component):
    """Definition of armor edit modal component."""

    name = Element(id_='armorEditNameInput')
    type_ = Element(id_='armorEditTypeInput')
    magical_modifier = Element(id_='armorEditMagicalModifierInput')
    price = Element(id_='armorEditPriceInput')
    currency_denomination = Element(id_='armorEditCurrencyDenominationInput')
    weight = Element(id_='armorEditWeightInput')
    armor_class = Element(id_='armorEditArmorClassInput')
    stealth = Element(id_='armorEditStealthInput')
    don = Element(id_='armorEditDonButton')
    doff = Element(id_='armorEditDoffButton')
    description = Element(id_='ArmorEditDescriptionTextarea')
    add = Element(id_='armorEditAddButton')
    cancel = Element(id_='armorEditCancelButton')


class ArmorPreviewModal(Component):
    """Definition of armor preview modal component."""

    name = Element(id_='armorPreviewNameLabel')
    type_ = Element(id_='armorPreviewTypeLabel')
    weight = Element(id_='armorPreviewWeightLabel')
    stealth = Element(id_='armorPreviewStealthLabel')
    description = Element(id_='ArmorPreviewDescriptionTextarea')
    done = Element(id_='armorPreviewDoneButton')


class ArmorModalTabs(Component):
    """Definition of armor modal tabs component."""

    preview = Element(id_='armorModalPreviewTab')
    edit = Element(id_='armorModalEditTab')


class ArmorTable(Component):
    """Definition of armors edit modal componenet."""

    add = Element(id_='armorAddIcon')
    table = Element(id_='armorTable')
