"""Monster factory."""

import factory

from factories.fixtures import random_wordlist


class Monster:
    """Definition of monster model."""

    def __init__(
        self,
        name,
        size,
        type_,
        alignment,
        armor_class,
        hit_points,
        speed,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
        saving_throws,
        skills,
        damage_immunities,
        damage_vulnerabilities,
        damage_resistances,
        condition_immunities,
        senses,
        languages,
        challenge,
        experience,
        description,
    ):
        """Initialize monster instance."""
        self.name = name
        self.size = size
        self.type_ = type_
        self.alignment = alignment
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.saving_throws = saving_throws
        self.skills = skills
        self.damage_immunities = damage_immunities
        self.damage_vulnerabilities = damage_vulnerabilities
        self.damage_resistances = damage_resistances
        self.condition_immunities = condition_immunities
        self.senses = senses
        self.languages = languages
        self.challenge = challenge
        self.experience = experience
        self.description = description


class MonsterFactory(factory.Factory):
    """Definition of monster factory."""

    class Meta:
        """Bind model to factory."""

        model = Monster

    name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Name_', max_length=40)
    )

    size = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Size_', max_length=40)
    )

    type_ = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Type_', max_length=40)
    )

    alignment = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Alignment_', max_length=40)
    )

    hit_points = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='HitPoints_', max_length=40)
    )

    speed = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Speed_', max_length=40)
    )

    strength = factory.Faker('random_int', min=0, max=100)

    dexterity = factory.Faker('random_int', min=0, max=100)

    constitution = factory.Faker('random_int', min=0, max=100)

    intelligence = factory.Faker('random_int', min=0, max=100)

    wisdom = factory.Faker('random_int', min=0, max=100)

    charisma = factory.Faker('random_int', min=0, max=100)

    saving_throws = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='SavingThrows_', max_length=40)
    )

    skills = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Skills_', max_length=40)
    )

    damage_immunities = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='DamageImmunities_', max_length=40)
    )

    damage_vulnerabilities = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='DamageVulnerabilities_', max_length=40)
    )

    damage_resistances = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='DamageResistances_', max_length=40)
    )

    condition_immunities = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='ConditionImmunities_', max_length=40)
    )

    senses = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Senses_', max_length=40)
    )

    languages = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Languages_', max_length=40)
    )

    challenge = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Challenge_', max_length=40)
    )

    experience = factory.Faker(
        'word',
        ext_word_list=random_wordlist(prefix='Experience_', max_length=40)
    )

    description = factory.Faker(
        'text',
        max_nb_chars=150
    )
