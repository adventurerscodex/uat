"""DM Encounter List component."""

from component_objects import Component, Element


class EncounterList(Component):
    """Definition of Encounter List component."""

    add_plus_icon_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[1]/div/div/div/div/div' # noqa
    add_encounter_detail_placeholder_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/div' # noqa
    added_list_encounter_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[1]/div/div/nested-list/div/a/span[1]' # noqa

    add_plus_icon = Element(xpath=add_plus_icon_xpath)
    add_encounter_detail_placeholder = Element(xpath=add_encounter_detail_placeholder_xpath)
    added_list_encounter = Element(xpath=added_list_encounter_xpath)
