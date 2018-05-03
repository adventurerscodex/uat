"""DM screen component."""

from component_objects import Element, Component


class Screen(Component):
    """Definition of dm screen componenet."""

    conditions_heading_id = 'screenConditionsHeading'
    travel_pace_heading_id = 'screenTravelPaceHeading'
    cover_heading_id = 'screenCoverHeading'
    light_heading_id = 'screenLightHeading'
    difficulty_classes_heading_id = 'screenDifficultyClassesHeading'
    exhaustion_heading_id = 'screenExhaustionHeading'

    conditions_heading = Element(id_=conditions_heading_id)
    travel_pace_heading = Element(id_=travel_pace_heading_id)
    cover_heading = Element(id_=cover_heading_id)
    light_heading = Element(id_=light_heading_id)
    difficulty_classes_heading = Element(id_=difficulty_classes_heading_id)
    exhaustion_heading = Element(id_=exhaustion_heading_id)
