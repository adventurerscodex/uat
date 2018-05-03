"""Feat factory."""

import factory.fuzzy


class Feat:
    """Definition of feat model."""

    def __init__(
        self,
        name,
        description,
    ):
        """Initialize feat instance."""
        self.name = name,
        self.description = description


class FeatFactory(factory.Factory):
    """Definition of feat factory."""

    class Meta:
        """Bind model to factory."""

        model = Feat

    name = factory.fuzzy.FuzzyText(length=125, prefix='Feat_')
    description = factory.fuzzy.FuzzyText(length=150, prefix='Description_')
