"""Tabs component."""

from component_objects import Element, Component


class DMTabs(Component):
    """Definition of dm tabs componenet."""

    overview_id = 'tabOverviewLink'
    overview_label_id = 'tabOverviewSpan'

    encounters_id = 'tabEncountersLink'
    encounters_label_id = 'tabEncountersSpan'

    screen_id = 'tabScreenLink'
    screen_label_id = 'tabScreenSpan'

    notes_id = 'tabNotesLink'
    notes_label_id = 'tabNotesSpan'

    party_id = 'tabPartyLink'
    party_label_id = 'tabPartySpan'

    chat_id = 'tabChatLink'
    chat_label_id = 'tabChatSpan'

    overview = Element(id_=overview_id)
    overview_label = Element(id_=overview_label_id)

    encounters = Element(id_=encounters_id)
    encounters_label = Element(id_=encounters_label_id)

    screen = Element(id_=screen_id)
    screen_label = Element(id_=screen_label_id)

    notes = Element(id_=notes_id)
    notes_label = Element(id_=notes_label_id)

    party = Element(id_=party_id)
    party_label = Element(id_=party_label_id)

    chat = Element(id_=chat_id)
    chat_label = Element(id_=chat_label_id)
