"""HUD component."""

from modules.element import Element, Component


class HUD(Component):
    """Definition of a HUD component."""

    character_name = Element(id_='characterNameLabel')
