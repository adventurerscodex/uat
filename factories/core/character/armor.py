"""Armor factory."""

import factory.fuzzy

from factories.fixtures import Fixtures


class Armor:
    """Definition of armor model."""

    def __init__(
        self,
        name,
        type_,
        magical_modifier,
        price,
        currency_denomination,
        weight,
        armor_class,
        stealth,
        description,
    ):
        """Initialize armor instance."""
        self.name = name,
        self.type_ = type_
        self.magical_modifier = magical_modifier,
        self.price = price,
        self.currency_denomination = currency_denomination,
        self.weight = weight,
        self.armor_class = armor_class,
        self.stealth = stealth,
        self.description = description


class ArmorFactory(factory.Factory):
    """Definition of armor factory."""

    class Meta:
        """Bind model to factory."""

        model = Armor

    name = factory.fuzzy.FuzzyText(length=40, prefix='Armor_')
    type_ = factory.fuzzy.FuzzyChoice(
        Fixtures['armor']['armorTypeOptions']
    )
    magical_modifier = factory.fuzzy.FuzzyInteger(1, 10)
    price = factory.fuzzy.FuzzyInteger(0, 1000000)
    currency_denomination = factory.fuzzy.FuzzyChoice(
        Fixtures['general']['currencyDenominationList']
    )
    weight = factory.fuzzy.FuzzyInteger(0, 10000)
    armor_class = factory.fuzzy.FuzzyInteger(10, 30)
    stealth = factory.fuzzy.FuzzyChoice(
        Fixtures['armor']['armorStealthOptions']
    )
    description = factory.fuzzy.FuzzyText(length=150)
