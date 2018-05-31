"""Feature components."""

from component_objects import Component, Element


class FeatureAddModal(Component):
    """Definition of feature add modal component."""

    modal_div_id = 'addFeature'
    name_id = 'featureAddNameInput'
    class_id = 'featureAddClassInput'
    level_id = 'featureAddLevelInput'
    description_id = 'featureAddDescriptionTextarea'
    tracked_id = 'featureAddTrackedCheckbox'
    max_id = 'featureAddMaxInput'
    short_rest_id = 'featureAddShortRestInput'
    long_rest_id = 'featureAddLongRestInput'
    add_id = 'featureAddAddButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    class_ = Element(id_=class_id)
    level = Element(id_=level_id)
    description = Element(id_=description_id)
    tracked = Element(id_=tracked_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    add = Element(id_=add_id)


class FeatureEditModal(Component):
    """Definition of feature edit modal component."""

    modal_div_id = 'viewWeapon'
    name_id = 'featureEditNameInput'
    class_id = 'featureEditClassInput'
    level_id = 'featureEditLevelInput'
    description_id = 'featureEditDescriptionTextarea'
    tracked_id = 'featureEditTrackedCheckbox'
    max_id = 'featureEditMaxInput'
    short_rest_id = 'featureEditShortRestInput'
    long_rest_id = 'featureEditLongRestInput'
    done_id = 'featureEditDoneButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    class_ = Element(id_=class_id)
    level = Element(id_=level_id)
    description = Element(id_=description_id)
    tracked = Element(id_=tracked_id)
    max_ = Element(id_=max_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
    done = Element(id_=done_id)


class FeatureModalTabs(Component):
    """Definition of feature modal tabs component."""

    preview_id = 'featureModalPreview'
    edit_id = 'featureModalEdit'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class FeaturesTable(Component):
    """Definition of features edit modal componenet."""

    add_id = 'featureAddIcon'
    table_id = 'featureTable'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
