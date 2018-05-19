"""Spell factory."""

import factory

from factories.fixtures import Fixtures, random_wordlist


class Spell:
    """Definition of spell model."""

    def __init__(
        self,
        name,
        type_,
        damage,
        damage_type,
        school,
        level,
        description,
        material_components,
        is_ritual,
        prepared,
        always_prepared,
        casting_time,
        components,
        duration,
        range_,
    ):
        """Initialize spell instance."""
        self.name = name
        self.type_ = type_
        self.damage = damage
        self.damage_type = damage_type
        self.school = school
        self.level = level
        self.description = description
        self.material_components = material_components
        self.is_ritual = is_ritual
        self.prepared = prepared
        self.always_prepared = always_prepared
        self.casting_time = casting_time
        self.components = components
        self.duration = duration
        self.range_ = range_


class SpellFactory(factory.Factory):
    """Definition of spell factory."""

    class Meta:
        """Bind model to factory."""

        model = Spell

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Spell_'))

    type_ = factory.Faker(
        'random_element',
        elements=Fixtures['spell']['spellTypeOptions']
    )

    damage = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Damage_')
    )

    damage_type = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='DamageType_')
    )

    school = factory.Faker(
        'random_element',
        elements=Fixtures['spell']['spellSchoolOptions']
    )

    level = factory.Faker('random_int', min=0, max=10)

    material_components = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='MaterialComponents_')
    )

    is_ritual = factory.Faker('boolean', chance_of_getting_true=50)

    prepared = factory.Faker('boolean', chance_of_getting_true=50)

    always_prepared = factory.Faker('boolean', chance_of_getting_true=50)

    casting_time = factory.Faker(
        'random_element',
        elements=Fixtures['spell']['spellCastingTimeOptions']
    )

    components = factory.Faker(
        'random_element',
        elements=Fixtures['spell']['spellComponentsOptions']
    )

    duration = factory.Faker(
        'random_element',
        elements=Fixtures['spell']['spellDurationOptions']
    )

    range_ = factory.Faker(
        'random_element',
        elements=Fixtures['spell']['spellRangeOptions']
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
