"""DM Encounter Add Edit component."""

from component_objects import Component, Element


class EncounterAddEditModal(Component):
    """Definition of Encounter Add Edit component."""

    encounter_name_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/div[1]/div[1]/div/input' # noqa
    location_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/div[1]/div[2]/div/input' # noqa
    environment_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[1]/div[1]/div[2]/input' # noqa
    maps_and_images_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[2]/div[1]/div[2]/input' # noqa
    points_of_interest_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[3]/div[1]/div[2]/input' # noqa
    non_player_characters_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[4]/div[1]/div[2]/input' # noqa
    monsters_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[5]/div[1]/div[2]/input' # noqa
    read_aloud_text_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[6]/div[1]/div[2]/input' # noqa
    treasure_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[7]/div[1]/div[2]/input' # noqa
    notes_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/encounter-section-visibility[8]/div[1]/div[2]/input' # noqa
    done_xpath = '//*[@id="encounter-tab"]/encounter/encounter-add-edit-modal/div/div/div/div[2]/form/div[3]/div/div/button' # noqa

    encounter_name = Element(xpath=encounter_name_xpath)
    location = Element(xpath=location_xpath)
    environment = Element(xpath=environment_xpath)
    maps_and_images = Element(xpath=maps_and_images_xpath)
    points_of_interest = Element(xpath=points_of_interest_xpath)
    non_player_characters = Element(xpath=non_player_characters_xpath)
    monsters = Element(xpath=monsters_xpath)
    read_aloud_text = Element(xpath=read_aloud_text_xpath)
    treasure = Element(xpath=treasure_xpath)
    notes = Element(xpath=notes_xpath)
    done = Element(xpath=done_xpath)
