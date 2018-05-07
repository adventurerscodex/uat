"""Other Stats components."""

from component_objects import Element, Component


class OtherStats(Component):
    """Definition of OtherStats component."""

    ac_id = 'otherStatsAcSpan'
    ac_modifier_id = 'otherStatsAcModifierInput'
    ac_popover_icon_id = 'otherStatsAcPopoverIconSpan'
    ac_popover_content_xpath = '//*[contains(@id, "popover")]/div[2]'
    initiative_id = 'otherStatsInitiativeSpan'
    initiative_modifier_id = 'otherStatsInitiativeModiferInput'
    initiative_popover_icon_id = 'otherStatsInitiativePopoverIconSpan'
    initiative_popover_content_xpath = '//*[contains(@id, "popover")]/div[2]'
    proficiency_bonus_id = 'otherStatsProficiencySpan'
    proficiency_bonus_modifier_id = 'otherStatsProficiencyBonusModifierInput'
    proficiency_popover_icon_id = 'otherStatsProficiencyPopoverIconSpan'
    proficiency_popover_content_xpath = '//*[contains(@id, "popover")]/div[2]'
    level_id = 'otherStatsLevelInput'
    inspiration_id = 'otherStatsInspirationInput'
    speed_id = 'otherStatsSpeedInput'
    experience_id = 'otherStatsExperienceInput'

    ac = Element(id_=ac_id)
    ac_modifier = Element(id_=ac_modifier_id)
    ac_popover_icon = Element(id_=ac_popover_icon_id)
    ac_popover_content = Element(xpath=ac_popover_content_xpath)
    initiative = Element(id_=initiative_id)
    initiative_modifier = Element(id_=initiative_modifier_id)
    initiative_popover_icon = Element(id_=initiative_popover_icon_id)
    initiative_popover_content = Element(xpath=initiative_popover_content_xpath)
    proficiency_bonus = Element(id_=proficiency_bonus_id)
    proficiency_bonus_modifier = Element(id_=proficiency_bonus_modifier_id)
    proficiency_popover_icon = Element(id_=proficiency_popover_icon_id)
    proficiency_popover_content = Element(xpath=proficiency_popover_content_xpath)
    level = Element(id_=level_id)
    inspiration = Element(id_=inspiration_id)
    speed = Element(id_=speed_id)
    experience = Element(id_=experience_id)
