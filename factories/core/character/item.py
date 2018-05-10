"""Item factory."""

import factory

from factories.fixtures import Fixtures, random_wordlist


class Item:
    """Definition of item model."""

    def __init__(
        self,
        name,
        description,
        quantity,
        weight,
        cost,
        currency_denomination,
    ):
        """Initialize item instance."""
        self.name = name,
        self.description = description,
        self.quantity = quantity,
        self.weight = weight,
        self.cost = cost,
        self.currency_denomination = currency_denomination,


class ItemFactory(factory.Factory):
    """Definition of item factory."""

    class Meta:
        """Bind model to factory."""

        model = Item

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Item_')
    )

    quantity = factory.Faker('random_int', min=1, max=10000)

    weight = factory.Faker('random_int', min=0, max=10000)

    cost = factory.Faker('random_int', min=0, max=10000)

    currency_denomination = factory.Faker(
        'random_element',
        elements=Fixtures['general']['currencyDenominationList']
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
