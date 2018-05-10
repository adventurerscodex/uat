"""Background factory."""

import factory

from factories.fixtures import Fixtures


class Background:
    """Definition of background model."""

    def __init__(
        self,
        name,
        ideal,
        flaw,
        bond,
        personality_trait,
    ):
        """Initialize background instance."""
        self.name = name
        self.ideal = ideal
        self.flaw = flaw
        self.bond = bond
        self.personality_trait = personality_trait


class BackgroundFactory(factory.Factory):
    """Definition of background factory."""

    class Meta:
        """Bind model to factory."""

        model = Background

    name = factory.Faker(
        'random_element',
        elements=Fixtures['profile']['backgroundOptions']
    )

    ideal = factory.Faker(
        'text',
        max_nb_chars=150
    )

    flaw = factory.Faker(
        'text',
        max_nb_chars=150
    )

    bond = factory.Faker(
        'text',
        max_nb_chars=150
    )

    personality_trait = factory.Faker(
        'text',
        max_nb_chars=150
    )
