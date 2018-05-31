"""Appearance component."""

from component_objects import Component, Element


class Appearance(Component):
    """Definition of appearance componenet."""

    height_id = 'appearanceHeightInput'
    weight_id = 'appearanceWeightInput'
    hair_color_id = 'appearanceHairColorInput'
    eye_color_id = 'appearanceEyeColorInput'
    skin_color_id = 'appearanceSkinColorInput'

    height = Element(id_=height_id)
    weight = Element(id_=weight_id)
    hair_color = Element(id_=hair_color_id)
    eye_color = Element(id_=eye_color_id)
    skin_color = Element(id_=skin_color_id)
