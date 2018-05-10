"""Magic Item factory."""

import factory

from factories.fixtures import Fixtures, random_wordlist


class MagicItem:
    """Definition of magic item model."""

    def __init__(
        self,
        name,
        type_,
        rarity,
        requires_attunement,
        attuned,
        max_charges,
        used_charges,
        weight,
        description,
    ):
        """Initialize magic item instance."""
        self.name = name
        self.type_ = type_
        self.rarity = rarity
        self.requires_attunement = requires_attunement
        self.attuned = attuned
        self.max_charges = max_charges
        self.used_charges = used_charges
        self.weight = weight
        self.description = description


class MagicItemFactory(factory.Factory):
    """Definition of magic item factory."""

    class Meta:
        """Bind model to factory."""

        model = MagicItem

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='MagicItem_')
    )

    type_ = factory.Faker(
        'random_element',
        elements=Fixtures['magicItem']['magicItemTypeOptions']
    )
    rarity = factory.Faker(
        'random_element',
        elements=Fixtures['magicItem']['magicItemRarityOptions']
    )

    requires_attunement = factory.Faker('boolean', chance_of_getting_true=50)

    attuned = factory.Faker('boolean', chance_of_getting_true=50)

    max_charges = factory.Faker('random_int', min=0, max=1000000)

    used_charges = factory.Faker('random_int', min=0, max=1000000)

    weight = factory.Faker('random_int', min=0, max=10000)

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
