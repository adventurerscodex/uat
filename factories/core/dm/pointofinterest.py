"""Point Of Interest Factory."""

import factory

from factories.fixtures import random_wordlist


class PointOfInterest:
    """Definition of Point Of Interest model."""

    def __init__(
        self,
        name,
        description,
    ):
        """Initialize Point Of Interest instance."""
        self.name = name
        self.description = description


class PointOfInterestFactory(factory.Factory):
    """Definition of Point Of Interest factory."""

    class Meta:
        """Bind model to factory."""

        model = PointOfInterest

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='PointOfInterest_', max_length=40)
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
