"""Wizard component."""

from modules.element import Element, Component


class TellUsAStory(Component):
    """Definition of dm wizard component."""

    campaign_name = Element(id_='tellUsAStoryCampaignNameInput')
    player_name = Element(id_='tellUsAStoryPlayerNameInput')
