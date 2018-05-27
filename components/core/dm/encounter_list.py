"""DM Encounter List component."""

from component_objects import Element, Component


class EncounterList(Component):
    """Definition of Encounter List component."""

    add_plus_icon_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[1]/div/div/div/div/div' # noqa
    add_encounter_detail_placeholder_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/div' # noqa

    add_plus_icon = Element(xpath_=add_plus_icon_xpath)
    add_encounter_detail_placeholder = Element(xpath_=add_encounter_detail_placeholder_xpath)
