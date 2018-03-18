"""Tabs component."""

from modules.element import Element, Component


class Tabs(Component):
    """Definition of player tabs componenet."""

    stats_id = 'tabStatsLink'
    stats_label_id = 'tabStatsSpan'

    skills_id = 'tabSkillsLink'
    skills_label_id = 'tabSkillsSpan'

    spells_id = 'tabSpellsLink'
    spells_label_id = 'tabSpellsSpan'

    equipment_id = 'tabEquipmentLink'
    equipment_label_id = 'tabEquipmentSpan'

    inventory_id = 'tabInventoryLink'
    inventory_label_id = 'tabInventorySpan'

    notes_id = 'tabNotesLink'
    notes_label_id = 'tabNotesSpan'

    profile_id = 'tabProfileLink'
    profile_label_id = 'tabProfileSpan'

    chat_id = 'tabChatLink'
    chat_label_id = 'tabChatSpan'

    exhibit_id = 'tabExhibitLink'
    exhibit_label_id = 'tabExhibitSpan'

    stats = Element(id_=stats_id)
    stats_label = Element(id_=stats_label_id)

    skills = Element(id_=skills_id)
    skills_label = Element(id_=skills_label_id)

    spells = Element(id_=spells_id)
    spells_label = Element(id_=spells_label_id)

    equipment = Element(id_=equipment_id)
    equipment_label = Element(id_=equipment_label_id)

    inventory = Element(id_=inventory_id)
    inventory_label = Element(id_=inventory_label_id)

    notes = Element(id_=notes_id)
    notes_label = Element(id_=notes_label_id)

    profile = Element(id_=profile_id)
    profile_label = Element(id_=profile_label_id)

    chat = Element(id_=chat_id)
    chat_label = Element(id_=chat_label_id)

    exhibit = Element(id_=exhibit_id)
    exhibit_label = Element(id_=exhibit_label_id)
