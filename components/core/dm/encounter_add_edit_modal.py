"""DM Encounter Add Edit component."""

from component_objects import Element, Component


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

    encounter_name = Element(xpath_=encounter_name_xpath)
    location = Element(xpath_=location_xpath)
    environment = Element(xpath_=environment_xpath)
    maps_and_images = Element(xpath_=maps_and_images_xpath)
    points_of_interest = Element(xpath_=points_of_interest_xpath)
    non_player_characters = Element(xpath_=non_player_characters_xpath)
    monsters = Element(xpath_=monsters_xpath)
    read_aloud_text = Element(xpath_=read_aloud_text_xpath)
    treasure = Element(xpath_=treasure_xpath)
    notes = Element(xpath_=notes_xpath)
