"""Feature components."""

from modules.element import Element, Component


class FeatureAddModal(Component):
    """Definition of feature add modal component."""

    name = Element(id_='featureAddNameInput')
    class_ = Element(id_='featureAddClassInput')
    level = Element(id_='featureAddLevelInput')
    description = Element(id_='featureAddDescriptionTextarea')
    tracked = Element(id_='featureAddTrackedCheckbox')
    max_ = Element(id_='featureAddMaxInput')
    short_rest = Element(id_='featureAddShortRestInput')
    long_rest = Element(id_='featureAddLongRestInput')
    add = Element(id_='featureAddAddButton')


class FeatureEditModal(Component):
    """Definition of feature edit modal component."""

    name = Element(id_='featureEditNameInput')
    class_ = Element(id_='featureEditClassInput')
    level = Element(id_='featureEditLevelInput')
    description = Element(id_='featureEditDescriptionTextarea')
    tracked = Element(id_='featureEditTrackedCheckbox')
    max_ = Element(id_='featureEditMaxInput')
    short_rest = Element(id_='featureEditShortRestInput')
    long_rest = Element(id_='featureEditLongRestInput')
    done = Element(id_='featureEditDoneButton')


class FeatureModalTabs(Component):
    """Definition of feature modal tabs component."""

    preview = Element(id_='featureModalPreview')
    edit = Element(id_='featureModalEdit')


class FeaturesTable(Component):
    """Definition of features edit modal componenet."""

    add = Element(id_='featureAddIcon')
    table = Element(id_='featureTable')
