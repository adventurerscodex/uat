"""Profile component."""

from component_objects import Element, Component


class SpellSlotsTable(Component):
    """Definition of Spell Slots Table component."""

    table_id = 'spellSlotsTable'
    add_id = 'spellSlotsAddIcon'

    table = Element(id_=table_id)
    add = Element(id_=add_id)


class SpellSlotsEditModal(Component):
    """Definition of Spell Slots Edit component."""

    level_id = 'spellSlotsEditModalLevelInput'
    max_id = 'spellSlotsEditModalMaxInput'
    short_rest_id = 'spellSlotsEditModalShortRestButton'
    long_rest_id = 'spellSlotsEditModalLongRestButton'
    done_id = 'spellSlotsEditModalDoneButton'

    level = Element(id_=level_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    done = Element(id_=done_id)


class SpellSlotsAddModal(Component):
    """Definition of Spells add modal component."""

    level_id = 'spellSlotsAddModalLevelInput'
    max_id = 'spellSlotsAddModalMaxInput'
    short_rest_id = 'spellSlotsAddModalShortRestButton'
    long_rest_id = 'spellSlotsAddModalLongRestButton'
    cancel_id = 'spellSlotsAddModalCancelButton'
    add_id = 'spellSlotsAddModalAddButton'

    level = Element(id_=level_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    cancel = Element(id_=cancel_id)
    add = Element(id_=add_id)


class SpellStatsTable(Component):
    """Definition of Spell Stats Table component."""

    spell_stats_table_id = 'spellStatsTable'

    spell_stats_table = Element(id_=spell_stats_table_id)


class SpellStatsEditModal(Component):
    """Definition of Spell Stats Edit component."""

    spell_attack_bonus_id = 'spellStatsEditSpellAttackBonusInput'
    spell_save_dc_id = 'spellStatsEditSpellSaveDcInput'
    spell_casting_ability_id = 'spellStatsEditSpellCastingAbilityInput'
    spells_known_id = 'spellStatsEditSpellsKnownInput'
    cantrip_known_id = 'spellStatsEditCantripKnownInput'
    max_prepared_id = 'spellStatsEditMaxPreparedInput'
    invocations_known_id = 'spellStatsEditInvocationsKnownInput'

    spell_attack_bonus = Element(id_=spell_attack_bonus_id)
    spell_save_dc = Element(id_=spell_save_dc_id)
    spell_casting_ability = Element(id_=spell_casting_ability_id)
    spells_known = Element(id_=spells_known_id)
    cantrip_known = Element(id_=cantrip_known_id)
    max_prepared = Element(id_=max_prepared_id)
    invocations_known = Element(id_=invocations_known_id)


class SpellsAddModal(Component):
    """Definition of Spells add modal component."""

    modal_div_id = 'addSpell'
    name_id = 'spellsAddNameInput'
    prepared_id = 'spellsAddPreparedCheckbox'
    always_prepared_id = 'spellsAddAlwaysPreparedCheckbox'
    ritual_id = 'spellsAddRitualCheckbox'
    level_id = 'spellsAddLevelInput'
    school_id = 'spellsAddSchoolInput'
    type_id = 'spellsAddTypeInput'
    save_attr_id = 'spellsAddSaveAttrInput'
    damage_id = 'spellsAddDamageInput'
    cast_time_id = 'spellsAddCastTimeInput'
    range_id = 'spellsAddRangeInput'
    components_id = 'spellsAddComponentsInput'
    material_components_id = 'spellsAddMaterialComponentsInput'
    duration_id = 'spellsAddDurationInput'
    description_id = 'spellsAddDescriptionTextarea'
    add_id = 'spellsAddAddButton'
    cancel_id = 'spellsAddCancelButton'

    name = Element(id_=name_id)
    prepared = Element(id_=prepared_id)
    always_prepared = Element(id_=always_prepared_id)
    ritual = Element(id_=ritual_id)
    level = Element(id_=level_id)
    school = Element(id_=school_id)
    type_ = Element(id_=type_id)
    save_attr = Element(id_=save_attr_id)
    damage = Element(id_=damage_id)
    cast_time = Element(id_=cast_time_id)
    range_ = Element(id_=range_id)
    components = Element(id_=components_id)
    material_components = Element(id_=material_components_id)
    duration = Element(id_=duration_id)
    description = Element(id_=description_id)
    add = Element(id_=add_id)
    cancel = Element(id_=cancel_id)


class SpellsEditModal(Component):
    """Definition of spells edit modal component."""

    modal_div_id = 'viewSpell'
    name_id = 'spellsEditNameInput'
    prepared_id = 'spellsEditPreparedCheckbox'
    always_prepared_id = 'spellsEditAlwaysPreparedCheckbox'
    ritual_id = 'spellsEditRitualCheckbox'
    level_id = 'spellsEditLevelInput'
    school_id = 'spellsEditSchoolInput'
    type_id = 'spellsEditTypeInput'
    save_attr_id = 'spellsEditSaveAttrInput'
    damage_id = 'spellsEditDamageInput'
    cast_time_id = 'spellsEditCastTimeInput'
    range_id = 'spellsEditRangeInput'
    components_id = 'spellsEditComponentsInput'
    material_components_id = 'spellsEditMaterialComponentsInput'
    duration_id = 'spellsEditDurationInput'
    description_id = 'spellsEditDescriptionTextarea'
    done_id = 'spellsPreviewDoneButton'

    name = Element(id_=name_id)
    prepared = Element(id_=prepared_id)
    always_prepared = Element(id_=always_prepared_id)
    ritual = Element(id_=ritual_id)
    level = Element(id_=level_id)
    school = Element(id_=school_id)
    type_ = Element(id_=type_id)
    save_attr = Element(id_=save_attr_id)
    damage = Element(id_=damage_id)
    cast_time = Element(id_=cast_time_id)
    range_ = Element(id_=range_id)
    components = Element(id_=components_id)
    material_components = Element(id_=material_components_id)
    duration = Element(id_=duration_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class SpellsPreviewModal(Component):
    """Definition of spells preview modal component."""

    name_id = 'spellsPreviewNameLabel'
    spell_summary_label_id = 'spellsPreviewSpellSummaryLabelLabel'
    type_id = 'spellsPreviewTypeLabel'
    damage_id = 'spellsPreviewDamageLabel'
    cast_time_id = 'spellsPreviewCastTimeLabel'
    range_id = 'spellsPreviewRangeLabel'
    components_id = 'spellsPreviewCompenentsLabel'
    duration_id = 'spellsPreviewDurationLabel'
    description_id = 'spellsPreviewDescriptionLabel'
    done_id = 'spellsPreviewDoneButton'

    name = Element(id_=name_id)
    spell_summary_label = Element(id_=spell_summary_label_id)
    type_ = Element(id_=type_id)
    damage = Element(id_=damage_id)
    cast_time = Element(id_=cast_time_id)
    range_ = Element(id_=range_id)
    components = Element(id_=components_id)
    duration = Element(id_=duration_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class SpellsModalTabs(Component):
    """Definition of spells modal tabs component."""

    preview_id = 'spellsModalPreviewTab'
    edit_id = 'spellsModalEditTab'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class SpellsTable(Component):
    """Definition of spells edit modal componet."""

    prepared_header_id = 'spellsTablePreparedHeader'
    spell_header_id = 'spellsTableSpellHeader'
    level_header_id = 'spellsTableLevelHeader'
    type_header_id = 'spellsTableTypeHeader'
    damage_header_id = 'spellsTableDamageHeader'
    casting_time_header_id = 'spellsTableCastingHeader'
    range_header_id = 'spellsTableRangeHeader'
    add_id = 'spellsAddIcon'
    table_id = 'spellsTable'

    prepared_header = Element(id_=prepared_header_id)
    spell_header = Element(id_=spell_header_id)
    level_header = Element(id_=level_header_id)
    type_header = Element(id_=type_header_id)
    damage_header = Element(id_=damage_header_id)
    casting_time_header = Element(id_=casting_time_header_id)
    range_header = Element(id_=range_header_id)
    add = Element(id_=add_id)
    table = Element(id_=table_id)
