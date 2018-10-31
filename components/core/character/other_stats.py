"""Other Stats components."""

from component_objects import Component, Element


class OtherStats(Component):
    """Definition of OtherStats component."""

    edit_btn_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[1]/div/span' # noqa
    save_btn_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[1]/button[1]' # noqa

    # View labels and popovers

    ac_label_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[2]/div[2]/div' # noqa
    ac_popover_icon_xpath = '//*[@id="otherStatsAcPopoverIconSpan"]'
    ac_popover_content_xpath = '//*[contains(@id, "popover")]/div[2]'

    initiative_label_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[3]/div[1]/div' # noqa
    initiative_popover_icon_xpath = '//*[@id="otherStatsInitiativePopoverIconSpan"]' # noqa
    initiative_popover_content_xpath = '//*[contains(@id, "popover")]/div[2]'

    proficiency_bonus_label_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[2]/div[1]/div' # noqa
    proficiency_popover_icon_xpath = '//*[@id="otherStatsProficiencyPopoverIconSpan"]' # noqa
    proficiency_popover_content_xpath = '//*[contains(@id, "popover")]/div[2]'

    speed_label_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[3]/div[2]/div' # noqa
    level_label_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[4]/div[1]/div' # noqa
    experience_label_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[4]/div[2]/div' # noqa

    # Edit inputs

    proficiency_bonus_input_xpath = '//*[@id="otherStatsProficiencyBonusModifierInput"]' # noqa
    ac_modifier_input_xpath = '//*[@id="otherStatsAcModifierInput"]'
    initiative_modifier_input_xpath = '//*[@id="otherStatsInitiativeModiferInput"]' # noqa
    speed_input_xpath = '//*[@id="otherStatsSpeedInput"]'
    level_input_xpath = '//*[@id="otherStatsLevelInput"]'
    experience_input_xpath = '//*[@id="otherStatsExperienceInput"]'
    inspiration_input_xpath = '//*[@id="stats"]/div[4]/div[2]/div/div/div/div/other-stats/preview-edit/div[2]/form/div/div[4]/div/div/span' # noqa

    edit_btn = Element(xpath=edit_btn_xpath)
    save_btn = Element(xpath=save_btn_xpath)

    # View labels and popovers

    ac_label = Element(xpath=ac_label_xpath)
    ac_popover_icon = Element(xpath=ac_popover_icon_xpath)
    ac_popover_content = Element(xpath=ac_popover_content_xpath)

    initiative_label = Element(xpath=initiative_label_xpath)
    initiative_popover_icon = Element(xpath=initiative_popover_icon_xpath)
    initiative_popover_content = Element(xpath=initiative_popover_content_xpath)

    proficiency_bonus_label = Element(xpath=proficiency_bonus_label_xpath)
    proficiency_popover_icon = Element(xpath=proficiency_popover_icon_xpath)
    proficiency_popover_content = Element(xpath=proficiency_popover_content_xpath)

    speed_label = Element(xpath=speed_label_xpath)
    level_label = Element(xpath=level_label_xpath)
    experience_label = Element(xpath=experience_label_xpath)

    # Edit inputs

    proficiency_bonus_input = Element(xpath=proficiency_bonus_input_xpath)
    ac_modifier_input = Element(xpath=ac_modifier_input_xpath)
    initiative_modifier_input = Element(xpath=initiative_modifier_input_xpath)
    speed_input = Element(xpath=speed_input_xpath)
    level_input = Element(xpath=level_input_xpath)
    experience_input = Element(xpath=experience_input_xpath)
    inspiration_input = Element(xpath=inspiration_input_xpath)
