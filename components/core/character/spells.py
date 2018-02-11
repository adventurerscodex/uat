"""Profile component."""

from modules.element import Component, Element


class SpellSlotsTable(Component):
    """Definition of Spell Slots Table component."""
    table = Element(id_='spellSlotsTable')
    add = Element(id_='spellSlotsAddIcon')


class SpellSlotsEditModal(Component):
    """Definition of Spell Slots Edit component."""
    level = Element(id_='spellSlotsEditModalLevelInput')
    max_ = Element(id_='spellSlotsEditModalMaxInput')
    short_rest = Element(id_='spellSlotsEditModalShortRestButton')
    long_rest = Element(id_='spellSlotsEditModalLongRestButton')
    done = Element(id_='spellSlotsEditModalDoneButton')


class SpellSlotsAddModal(Component):
    """Definition of Spells add modal component."""
    level = Element(id_='spellSlotsAddModalLevelInput')
    max_ = Element(id_='spellSlotsAddModalMaxInput')
    short_rest = Element(id_='spellSlotsAddModalShortRestButton')
    long_rest = Element(id_='spellSlotsAddModalLongRestButton')
    cancel = Element(id_='spellSlotsAddModalCancelButton')
    add = Element(id_='spellSlotsAddModalAddButton')


class SpellStatsTable(Component):
    """Definition of Spell Stats Table component."""

    spell_stats_table = Element(id_='spellStatsTable')


class SpellStatsEditModal(Component):
    """Definition of Spell Stats Edit component."""

    spell_attack_bonus = Element(id_='spellStatsEditSpellAttackBonusInput')
    spell_save_dc = Element(id_='spellStatsEditSpellSaveDcInput')
    spell_casting_ability = Element(id_='spellStatsEditSpellCastingAbilityInput')
    spells_known = Element(id_='spellStatsEditSpellsKnownInput')
    cantrip_known = Element(id_='spellStatsEditCantripKnownInput')
    max_prepared = Element(id_='spellStatsEditMaxPreparedInput')
    invocations_known = Element(id_='spellStatsEditInvocationsKnownInput')


class SpellsAddModal(Component):
    """Definition of Spells add modal component."""

    name = Element(id_='spellsAddNameInput')
    prepared = Element(id_='spellsAddPreparedCheckbox')
    always_prepared = Element(id_='spellsAddAlwaysPreparedCheckbox')
    ritual = Element(id_='spellsAddRitualCheckbox')
    level = Element(id_='spellsAddLevelInput')
    school = Element(id_='spellsAddSchoolInput')
    type_ = Element(id_='spellsAddTypeInput')
    save_attr = Element(id_='spellsAddSaveAttrInput')
    damage = Element(id_='spellsAddDamageInput')
    cast_time = Element(id_='spellsAddCastTimeInput')
    range_ = Element(id_='spellsAddRangeInput')
    components = Element(id_='spellsAddComponentsInput')
    material_components = Element(id_='spellsAddMaterialComponentsInput')
    duration = Element(id_='spellsAddDurationInput')
    description = Element(id_='spellsAddDescriptionTextarea')
    add = Element(id_='spellsAddAddButton')
    cancel = Element(id_='spellsAddCancelButton')


class SpellsEditModal(Component):
    """Definition of spells edit modal component."""

    name = Element(id_='spellsEditNameInput')
    prepared = Element(id_='spellsEditPreparedCheckbox')
    always_prepared = Element(id_='spellsEditAlwaysPreparedCheckbox')
    ritual = Element(id_='spellsEditRitualCheckbox')
    level = Element(id_='spellsEditLevelInput')
    school = Element(id_='spellsEditSchoolInput')
    type_ = Element(id_='spellsEditTypeInput')
    save_attr = Element(id_='spellsAddSaveAttrInput')
    damage = Element(id_='spellsEditDamageInput')
    cast_time = Element(id_='spellsEditCastTimeInput')
    range_ = Element(id_='spellsEditRangeInput')
    components = Element(id_='spellsEditComponentsInput')
    material_components = Element(id_='spellsEditMaterialComponentsInput')
    duration = Element(id_='spellsEditDurationInput')
    description = Element(id_='spellsEditDescriptionTextarea')


class SpellsPreviewModal(Component):
    """Definition of spells preview modal component."""

    name = Element(id_='spellsPreviewNameLabel')
    spell_summary_label = Element(id_='spellsPreviewSpellSummaryLabelLabel')
    type_ = Element(id_='spellsPreviewTypeLabel')
    damage = Element(id_='spellsPreviewDamageLabel')
    cast_time = Element(id_='spellsPreviewCastTimeLabel')
    range_ = Element(id_='spellsPreviewRangeLabel')
    components = Element(id_='spellsPreviewComponentsLabel')
    duration = Element(id_='spellsPreviewDurationLabel')
    description = Element(id_='spellsPreviewDescriptionLabel')
    done = Element(id_='spellsPreviewDoneButton')


class SpellsModalTabs(Component):
    """Definition of spells modal tabs component."""

    preview = Element(id_='spellsModalPreviewTab')
    edit = Element(id_='spellsModalEditTab')


class SpellsTable(Component):
    """Definition of spells edit modal componet."""

    prepared_header = Element(id_='spellsTablePreparedHeader')
    spell_header = Element(id_='spellsTableSpellHeader')
    level_header = Element(id_='spellsTableLevelHeader')
    type_header = Element(id_='spellsTableTypeHeader')
    damage_header = Element(id_='spellsTableDamageHeader')
    casting_time_header = Element(id_='spellsTableCastingHeader')
    range_header = Element(id_='spellsTableRangeHeader')
    add = Element(id_='spellsAddIcon')
    table = Element(id_='spellsTable')
