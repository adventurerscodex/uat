"""Appearance factory."""

import factory

from factories.fixtures import random_wordlist


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
        self.weight = weight
        self.height = height
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.skin_color = skin_color


class AppearanceFactory(factory.Factory):
    """Definition of appearance factory."""

    class Meta:
        """Bind model to factory."""

        model = Appearance

    weight = factory.Faker('random_int', min=0, max=10000)

    height = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Height_', max_length=40)
    )

    hair_color = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='HairColor_', max_length=40)
    )
    eye_color = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='EyeColor_', max_length=40)
    )
    skin_color = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='SkinColor_', max_length=40)
    )
