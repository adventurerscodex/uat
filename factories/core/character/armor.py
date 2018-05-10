"""Armor factory."""

import factory

from factories.fixtures import Fixtures, random_wordlist


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

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Armor_', max_length=40)
    )

    type_ = factory.Faker(
        'random_element', elements=Fixtures['armor']['armorTypeOptions']
    )

    magical_modifier = factory.Faker('random_int', min=1, max=10)

    price = factory.Faker('random_int', min=0, max=1000000)

    currency_denomination = factory.Faker(
        'random_element',
        elements=Fixtures['general']['currencyDenominationList']
    )

    weight = factory.Faker('random_int', min=0, max=10000)

    armor_class = factory.Faker('random_int', min=10, max=30)

    stealth = factory.Faker(
        'random_element',
        elements=Fixtures['armor']['armorStealthOptions']
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
