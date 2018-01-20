"""Profile component."""

from modules.element import Element, Component


class Profile(Component):
    """Definition of profile componenet."""

    alignment = Element(id_='profileAlignmentInput')
    name = Element(id_='profilePlayerNameInput')
    background = Element(id_='profileBackgroundInput')
    deity = Element(id_='profileDeityInput')
    race = Element(id_='profileRaceInput')
    class_ = Element(id_='profileClassInput')
    gender = Element(id_='profileGenderInput')
    age = Element(id_='profileAgeInput')
