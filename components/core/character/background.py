"""Background component."""

from modules import Element, Component


class Background(Component):
    """Definition of background componenet."""

    traits_id = 'backgroundTraitsTextarea'
    ideals_id = 'backgroundIdealsTextarea'
    bonds_id = 'backgroundBondsTextarea'
    flaws_id = 'backgroundFlawsTextarea'

    traits = Element(id_=traits_id)
    ideals = Element(id_=ideals_id)
    bonds = Element(id_=bonds_id)
    flaws = Element(id_=flaws_id)
