"""Tabs component."""

from modules.element import Element, Component


class DMTabs(Component):
    """Definition of dm tabs componenet."""

    overview = Element(id_='tabOverviewLink')
    overview_label = Element(id_='tabOverviewSpan')

    encounters = Element(id_='tabEncountersLink')
    encounters_label = Element(id_='tabEncountersSpan')

    screen = Element(id_='tabScreenLink')
    screen_label = Element(id_='tabScreenSpan')

    notes = Element(id_='tabNotesLink')
    notes_label = Element(id_='tabNotesSpan')

    party = Element(id_='tabPartyLink')
    party_label = Element(id_='tabPartySpan')

    chat = Element(id_='tabChatLink')
    chat_label = Element(id_='tabChatSpan')
