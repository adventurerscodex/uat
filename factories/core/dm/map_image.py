"""Map Image Factory"""

import factory

from factories.fixtures import random_wordlist


class MapImage:
    """Map Image model."""

    def __init__(
        self,
        name,
        image_link,
        description,
    ):
        """Initialize Map Image instance."""
        self.name = name
        self.image_link = image_link
        self.description = description


class MapImageFactory(factory.Factory):
    """Definition of Map Image factory."""

    class Meta:
        """Bind model to factory."""

        model = MapImage

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='ImageLink_', max_length=40)
    )

    image_link = factory.Faker(
        'image_url'
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
