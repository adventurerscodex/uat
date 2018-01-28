"""Background component."""

from modules.element import Element, Component


class Background(Component):
    """Definition of background componenet."""

    traits = Element(id_='backgroundTraitsTextarea')
    ideals = Element(id_='backgroundIdealsTextarea')
    bonds = Element(id_='backgroundBondsTextarea')
    flaws = Element(id_='backgroundFlawsTextarea')
