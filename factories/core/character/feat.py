"""Feat factory."""

import factory

from factories.fixtures import random_wordlist


class Feat:
    """Definition of feat model."""

    def __init__(
        self,
        name,
        description,
    ):
        """Initialize feat instance."""
        self.name = name,
        self.description = description


class FeatFactory(factory.Factory):
    """Definition of feat factory."""

    class Meta:
        """Bind model to factory."""

        model = Feat

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=125, prefix='Feat_')
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
