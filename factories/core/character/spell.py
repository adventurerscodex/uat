"""Spell factory."""

import factory.fuzzy

from factories.fixtures import Fixtures


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
        self.name = name,
        self.type_ = type_,
        self.damage = damage,
        self.damage_type = damage_type,
        self.school = school,
        self.level = level,
        self.description = description,
        self.material_components = material_components,
        self.is_ritual = is_ritual,
        self.prepared = prepared,
        self.always_prepared = always_prepared,
        self.casting_time = casting_time,
        self.components = components,
        self.duration = duration,
        self.range_ = range_


class SpellFactory(factory.Factory):
    """Definition of spell factory."""

    class Meta:
        """Bind model to factory."""

        model = Spell

    name = factory.fuzzy.FuzzyText(length=40, prefix='Spell_')
    type_ = factory.fuzzy.FuzzyChoice(
        Fixtures['spell']['spellTypeOptions']
    )
    damage = factory.fuzzy.FuzzyText(length=40, prefix='damage_')
    damage_type = factory.fuzzy.FuzzyText(length=40, prefix='damage_type_')
    school = factory.fuzzy.FuzzyChoice(
        Fixtures['spell']['spellSchoolOptions']
    )
    level = factory.fuzzy.FuzzyInteger(0, 10)
    description = factory.fuzzy.FuzzyText(length=150, prefix='description_')
    material_components = factory.fuzzy.FuzzyText(
        length=40, prefix='material_components_'
    )
    is_ritual = factory.fuzzy.FuzzyChoice([True, False])
    prepared = factory.fuzzy.FuzzyChoice([True, False])
    always_prepared = factory.fuzzy.FuzzyChoice([True, False])
    casting_time = factory.fuzzy.FuzzyChoice(
        Fixtures['spell']['spellCastingTimeOptions']
    )
    components = factory.fuzzy.FuzzyChoice(
        Fixtures['spell']['spellComponentsOptions']
    )
    duration = factory.fuzzy.FuzzyChoice(
        Fixtures['spell']['spellDurationOptions']
    )
    range_ = factory.fuzzy.FuzzyChoice(
        Fixtures['spell']['spellRangeOptions']
    )
