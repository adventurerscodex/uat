import factory.fuzzy

from factories.fixtures import Fixtures


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

    name = factory.fuzzy.FuzzyText(length=40, prefix='Item_')
    description = factory.fuzzy.FuzzyText(length=150, prefix='description_')
    quantity = factory.fuzzy.FuzzyInteger(1, 10000)
    weight = factory.fuzzy.FuzzyInteger(0, 10000)
    cost = factory.fuzzy.FuzzyInteger(0, 10000)
    currency_denomination = factory.fuzzy.FuzzyChoice(
        Fixtures['general']['currencyDenominationList']
    )
