"""Environment Factory"""

import factory

from factories.fixtures import random_wordlist


class Environment:
    """Environment model."""

    def __init__(
        self,
        image_link,
        weather,
        terrain,
        description
    ):
        """Initialize Environment instance."""
        self.image_link = image_link
        self.weather = weather
        self.terrain = terrain
        self.description = description


class EnvironmentFactory(factory.Factory):
    """Definition of Environment factory."""

    class Meta:
        """Bind model to factory."""

        model = Environment

    image_link = factory.Faker(
        'image_url'
    )

    weather = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Weather_')
    )

    terrain = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Terrain_')
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
