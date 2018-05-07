"""Appearance factory."""

import factory.fuzzy


class Appearance:
    """Definition of appearance model."""

    def __init__(
        self,
        weight,
        height,
        hair_color,
        eye_color,
        skin_color,
    ):
        """Initialize appearance instance."""
        self.weight = weight,
        self.height = height,
        self.hair_color = hair_color,
        self.eye_color = eye_color,
        self.skin_color = skin_color,


class AppearanceFactory(factory.Factory):
    """Definition of appearance factory."""

    class Meta:
        """Bind model to factory."""

        model = Appearance

    weight = factory.fuzzy.FuzzyInteger(0, 10000)
    height = factory.fuzzy.FuzzyText(length=40, prefix='Height_')
    hair_color = factory.fuzzy.FuzzyText(length=40, prefix='Hair_Color_')
    eye_color = factory.fuzzy.FuzzyText(length=40, prefix='Eye_Color_')
    skin_color = factory.fuzzy.FuzzyText(length=40, prefix='Skin_Color_')
