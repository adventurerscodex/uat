"""Actions components."""

from component_objects import Component, Element


class Actions(Component):
    """Definition of actions component."""

    actions_id = 'actionsActionsButton'
    short_rest_id = 'actionsShortRestButton'
    long_rest_id = 'actionsLongRestButton'

    actions = Element(id_=actions_id)
    short_rest = Element(id_=short_rest_id)
    long_rest = Element(id_=long_rest_id)
