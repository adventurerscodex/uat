"""Point Of Interest Factory"""

import factory

from factories.fixtures import random_wordlist


class ReadAloudText:
    """Definition of Read aloud text model."""

    def __init__(
        self,
        name,
        description,
    ):
        """Initialize Read aloud text instance."""
        self.name = name
        self.description = description


class ReadAloudTextFactory(factory.Factory):
    """Definition of Read aloud text factory."""

    class Meta:
        """Bind model to factory."""

        model = ReadAloudText

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='ReadAloudText_', max_length=40)
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
