"""Actions components."""

from modules.element import Element, Component


class Actions(Component):
    """Definition of actions component."""

    actions = Element(id_='actionsActionsButton')
    short_rest = Element(id_='actionsShortRestButton')
    long_rest = Element(id_='actionsLongRestButton')
