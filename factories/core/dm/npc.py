"""NPC factory."""

import factory

from factories.fixtures import random_wordlist


class NPC:
    """Definition of npc model."""

    def __init__(
        self,
        name,
        race,
        description,
    ):
        """Initialize npc instance."""
        self.name = name
        self.race = race
        self.description = description


class NPCFactory(factory.Factory):
    """Definition of npc factory."""

    class Meta:
        """Bind model to factory."""

        model = NPC

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Name_'))

    race = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Race_'))

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
