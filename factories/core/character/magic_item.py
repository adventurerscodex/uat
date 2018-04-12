"""Magic Item factory."""

import factory.fuzzy

from factories.fixtures import Fixtures


class MagicItem:
    """Definition of magic item model."""

    def __init__(
        self,
        name,
        type_,
        rarity,
        requires_attunement,
        attuned,
        max_charges,
        used_charges,
        weight,
        description,
    ):
        """Initialize magic item instance."""
        self.name = name,
        self.type_ = type_,
        self.rarity = rarity,
        self.requires_attunement = requires_attunement,
        self.attuned = attuned,
        self.max_charges = max_charges,
        self.used_charges = used_charges,
        self.weight = weight,
        self.description = description


class MagicItemFactory(factory.Factory):
    """Definition of magic item factory."""

    class Meta:
        """Bind model to factory."""

        model = MagicItem

    name = factory.fuzzy.FuzzyText(length=40, prefix='MagicItem_')
    type_ = factory.fuzzy.FuzzyChoice(
        Fixtures['magicItem']['magicItemTypeOptions']
    )
    rarity = factory.fuzzy.FuzzyChoice(
        Fixtures['magicItem']['magicItemRarityOptions']
    )
    requires_attunement = factory.fuzzy.FuzzyChoice([True, False])
    attuned = factory.fuzzy.FuzzyChoice([True, False])
    max_charges = factory.fuzzy.FuzzyInteger(0, 1000000)
    used_charges = factory.fuzzy.FuzzyInteger(0, 1000000)
    weight = factory.fuzzy.FuzzyInteger(0, 10000)
    description = factory.fuzzy.FuzzyText(length=150, prefix='description_')
