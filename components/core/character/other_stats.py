"""Other Stats components."""

from modules.element import Element, Component


class OtherStats(Component):
    """Definition of OtherStats component."""

    ac = Element(id_='otherStatsAcSpan')
    ac_modifier = Element(id_='otherStatsAcModifierInput')
    ac_popover_icon = Element(id_='otherStatsAcPopoverIconSpan')
    ac_popover_content = Element(xpath='//*[contains(@id, "popover")]/div[2]')
    initiative = Element(id_='otherStatsInitiativeSpan')
    initiative_modifier = Element(id_='otherStatsInitiativeModiferInput')
    initiative_popover_icon = Element(id_='otherStatsInitiativePopoverIconSpan')
    initiative_popover_content = Element(xpath='//*[contains(@id, "popover")]/div[2]')
    proficiency_bonus = Element(id_='otherStatsProficiencySpan')
    proficiency_bonus_modifier = Element(id_='otherStatsProficiencyBonusModifierInput')
    proficiency_popover_icon = Element(id_='otherStatsProficiencyPopoverIconSpan')
    proficiency_popover_content = Element(xpath='//*[contains(@id, "popover")]/div[2]')
    level = Element(id_='otherStatsLevelInput')
    inspiration = Element(id_='otherStatsInspirationInput')
    speed = Element(id_='otherStatsSpeedInput')
    experience = Element(id_='otherStatsExperienceInput')
