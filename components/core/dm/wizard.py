"""Wizard component."""

from component_objects import Element, Component


class TellUsAStory(Component):
    """Definition of dm wizard component."""

    campaign_name_id = 'tellUsAStoryCampaignNameInput'
    player_name_id = 'tellUsAStoryPlayerNameInput'

    campaign_name = Element(id_=campaign_name_id)
    player_name = Element(id_=player_name_id)
