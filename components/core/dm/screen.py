"""DM screen component."""

from modules.element import Element, Component


class Screen(Component):
    """Definition of dm screen componenet."""

    conditions_heading = Element(id_='screenConditionsHeading')
    travel_pace_heading = Element(id_='screenTravelPaceHeading')
    cover_heading = Element(id_='screenCoverHeading')
    light_heading = Element(id_='screenLightHeading')
    difficulty_classes_heading = Element(id_='screenDifficultyClassesHeading')
    exhaustion_heading = Element(id_='screenExhaustionHeading')
