"""HUD component."""

from modules.element import Element, Component


class HUD(Component):
    """Definition of a HUD component."""

    character_name_id = 'characterNameLabel'
    status_line_xpath = '//*[@id="characters"]/div/div/div/div[2]/div[1]/div/player-status-line'

    character_name = Element(id_=character_name_id)
    status_line = Element(xpath=status_line_xpath)
