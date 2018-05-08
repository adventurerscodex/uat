"""Background factory."""

import factory.fuzzy

from factories.fixtures import Fixtures


class Background:
    """Definition of background model."""

    def __init__(
        self,
        name,
        ideal,
        flaw,
        bond,
        personality_trait,
    ):
        """Initialize background instance."""
        self.name = name,
        self.ideal = ideal
        self.flaw = flaw,
        self.bond = bond,
        self.personality_trait = personality_trait,


class BackgroundFactory(factory.Factory):
    """Definition of armor factory."""

    class Meta:
        """Bind model to factory."""

        model = Background

    name = factory.fuzzy.FuzzyChoice(
        Fixtures['profile']['backgroundOptions']
    )
    ideal = factory.fuzzy.FuzzyText(length=150, prefix='ideal_')
    flaw = factory.fuzzy.FuzzyText(length=150, prefix='flaw_')
    bond = factory.fuzzy.FuzzyText(length=150, prefix='bond_')
    personality_trait = factory.fuzzy.FuzzyText(length=150, prefix='personality_trait_')
