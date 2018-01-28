"""Appearance component."""

from modules.element import Element, Component


class Appearance(Component):
    """Definition of appearance componenet."""

    height = Element(id_='appearanceHeightInput')
    weight = Element(id_='appearanceWeightInput')
    hair_color = Element(id_='appearanceHairColorInput')
    eye_color = Element(id_='appearanceEyeColorInput')
    skin_color = Element(id_='appearanceSkinColorInput')
