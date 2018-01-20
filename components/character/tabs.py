"""Tabs component."""

from modules.element import Element, Component


class Tabs(Component):
    """Definition of player tabs componenet."""

    stats = Element(id_='tabStatsLink')
    skills = Element(id_='tabSkillsLink')
    spells = Element(id_='tabSpellsLink')
    equipment = Element(id_='tabEquipmentLink')
    inventory = Element(id_='tabInventoryLink')
    notes = Element(id_='tabNotesLink')
    profile = Element(id_='tabProfileLink')
    chat = Element(id_='tabChatLink')
    exhibit = Element(id_='tabExhibitLink')
