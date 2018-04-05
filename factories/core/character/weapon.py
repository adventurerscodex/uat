"""Weapon factory."""

import factory.fuzzy

from factories.fixtures import Fixtures


class Weapon:
    """Definition of weapon model."""

    def __init__(
        self,
        name,
        damage,
        magical_modifier,
        to_hit_modifier,
        type_,
        handedness,
        proficiency,
        price,
        currency_denomination,
        weight,
        range_,
        damage_type,
        property_,
        quantity,
        description,
    ):
        """Initialize weapon instance."""
        self.name = name,
        self.damage = damage,
        self.magical_modifier = magical_modifier,
        self.to_hit_modifier = to_hit_modifier,
        self.type_ = type_,
        self.handedness = handedness,
        self.proficiency = proficiency,
        self.price = price,
        self.currency_denomination = currency_denomination,
        self.weight = weight,
        self.range_ = range_,
        self.damage_type = damage_type,
        self.property_ = property_,
        self.quantity = quantity,
        self.description = description


class WeaponFactory(factory.Factory):
    """Definition of weapon factory."""

    class Meta:
        """Bind model to factory."""

        model = Weapon

    name = factory.fuzzy.FuzzyText(length=40, prefix='Weapon_')
    damage = factory.fuzzy.FuzzyText(length=40, prefix='damage_')
    magical_modifier = factory.fuzzy.FuzzyInteger(0, 10)
    to_hit_modifier = factory.fuzzy.FuzzyInteger(0, 10)
    type_ = factory.fuzzy.FuzzyChoice(
        Fixtures['weapon']['weaponTypeOptions']
    )
    handedness = factory.fuzzy.FuzzyChoice(
        Fixtures['weapon']['weaponHandednessOptions']
    )
    proficiency = factory.fuzzy.FuzzyChoice(
        Fixtures['weapon']['weaponProficiencyOptions']
    )
    price = factory.fuzzy.FuzzyInteger(0, 1000000)
    currency_denomination = factory.fuzzy.FuzzyChoice(
        Fixtures['general']['currencyDenominationList']
    )
    weight = factory.fuzzy.FuzzyInteger(0, 10000)
    range_ = factory.fuzzy.FuzzyText(length=40, prefix='range_')
    damage_type = factory.fuzzy.FuzzyText(length=40, prefix='damage_type_')
    property_ = factory.fuzzy.FuzzyChoice(
        Fixtures['weapon']['weaponPropertyOptions']
    )
    quantity = factory.fuzzy.FuzzyInteger(0, 1000)
    description = factory.fuzzy.FuzzyText(length=150, prefix='description_')
