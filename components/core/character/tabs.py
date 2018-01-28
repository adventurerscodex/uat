"""Tabs component."""

from modules.element import Element, Component


class Tabs(Component):
    """Definition of player tabs componenet."""

    stats = Element(id_='tabStatsLink')
    stats_label = Element(id_='tabStatsSpan')

    skills = Element(id_='tabSkillsLink')
    skills_label = Element(id_='tabSkillsSpan')

    spells = Element(id_='tabSpellsLink')
    spells_label = Element(id_='tabSpellsSpan')

    equipment = Element(id_='tabEquipmentLink')
    equipment_label = Element(id_='tabEquipmentSpan')

    inventory = Element(id_='tabInventoryLink')
    inventory_label = Element(id_='tabInventorySpan')

    notes = Element(id_='tabNotesLink')
    notes_label = Element(id_='tabNotesSpan')

    profile = Element(id_='tabProfileLink')
    profile_label = Element(id_='tabProfileSpan')

    chat = Element(id_='tabChatLink')
    chat_label = Element(id_='tabChatSpan')

    exhibit = Element(id_='tabExhibitLink')
    exhibit_label = Element(id_='tabExhibitSpan')
