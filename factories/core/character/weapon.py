"""Weapon factory."""

import factory

from factories.fixtures import Fixtures, random_wordlist


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
        self.name = name
        self.damage = damage
        self.magical_modifier = magical_modifier
        self.to_hit_modifier = to_hit_modifier
        self.type_ = type_
        self.handedness = handedness
        self.proficiency = proficiency
        self.price = price
        self.currency_denomination = currency_denomination
        self.weight = weight
        self.range_ = range_
        self.damage_type = damage_type
        self.property_ = property_
        self.quantity = quantity
        self.description = description


class WeaponFactory(factory.Factory):
    """Definition of weapon factory."""

    class Meta:
        """Bind model to factory."""

        model = Weapon

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Weapon_')
    )

    damage = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Damage_')
    )

    magical_modifier = factory.Faker('random_int', min=0, max=10)

    to_hit_modifier = factory.Faker('random_int', min=0, max=10)

    type_ = factory.Faker(
        'random_element',
        elements=Fixtures['weapon']['weaponTypeOptions']
    )

    handedness = factory.Faker(
        'random_element',
        elements=Fixtures['weapon']['weaponHandednessOptions']
    )

    proficiency = factory.Faker(
        'random_element',
        elements=Fixtures['weapon']['weaponProficiencyOptions']
    )

    price = factory.Faker('random_int', min=0, max=1000000)

    currency_denomination = factory.Faker(
        'random_element',
        elements=Fixtures['general']['currencyDenominationList']
    )

    weight = factory.Faker('random_int', min=0, max=10000)

    range_ = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Range_')
    )

    damage_type = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='DamageType_')
    )

    property_ = factory.Faker(
        'random_element',
        elements=Fixtures['weapon']['weaponPropertyOptions']
    )

    quantity = factory.Faker('random_int', min=0, max=1000)

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
