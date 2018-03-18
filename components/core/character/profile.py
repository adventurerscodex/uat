"""Profile component."""

from modules.element import Element, Component


class Profile(Component):
    """Definition of profile componenet."""

    alignment_id = 'profileAlignmentInput'
    name_id = 'profilePlayerNameInput'
    background_id = 'profileBackgroundInput'
    deity_id = 'profileDeityInput'
    race_id = 'profileRaceInput'
    class_id = 'profileClassInput'
    gender_id = 'profileGenderInput'
    age_id = 'profileAgeInput'

    alignment = Element(id_=alignment_id)
    name = Element(id_=name_id)
    background = Element(id_=background_id)
    deity = Element(id_=deity_id)
    race = Element(id_=race_id)
    class_ = Element(id_=class_id)
    gender = Element(id_=gender_id)
    age = Element(id_=age_id)
