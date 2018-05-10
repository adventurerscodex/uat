"""Coins factory."""

import factory

from factories.fixtures import Fixtures, random_wordlist


class Coins:
    """Definition of coins model."""

    def __init__(
        self,
        platinum,
        gold,
        electrum,
        silver,
        copper,

    ):
        """Initialize coins instance."""
        self.platinum = platinum
        self.gold = gold
        self.electrum = electrum
        self.silver = silver
        self.copper = copper


class CoinsFactory(factory.Factory):
    """Definition of coins factory."""

    class Meta:
        """Bind model to factory."""

        model = Coins

    platinum = factory.Faker('random_int', min=0, max=1000000)

    gold = factory.Faker('random_int', min=0, max=1000000)

    electrum = factory.Faker('random_int', min=0, max=1000000)

    silver = factory.Faker('random_int', min=0, max=1000000)

    copper = factory.Faker('random_int', min=0, max=1000000)
