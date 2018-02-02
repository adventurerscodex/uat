"""Other Stats components."""

from modules.element import Element, Component


class OtherStats(Component):
    """Definition of OtherStats component."""

    ac = Element(id_='otherStatsAcInput')
    ac_modifier = Element(id_='otherStatsAcSpan')
    ac_popover_icon = Element(id_='otherStatsAcPopoverIconSpan')
    ac_popover_content = Element(id='otherStatsAcPopoverContentDiv')
    initiative = Element(id_='otherStatsInitiativeInput')
    initiative_modifier = Element(id_='otherStatsInitiativeSpan')
    initiative_popover_icon = Element(id_='otherStatsInitiativePopoverIconSpan')
    initiative_popover_content = Element(id='otherStatsInitiativePopoverContentDiv')
    proficiency_bonus = Element(id_='otherStatsProficiencyInput')
    proficiency_bonus_modifier = Element(id_='otherStatsProficiencyBonusModifierSpan')
    proficiency_popover_icon = Element(id_='otherStatsProficiencyPopoverIconSpan')
    proficiency_popover_content = Element(id='otherStatsProficiencyPopoverContentDiv')
    level = Element(id_='otherStatsLevelInput')
    inspiration = Element(id_='otherStatsInspirationInput')
    speed = Element(id_='otherStatsSpeedInput')
    experience = Element(id_='otherStatsExperienceInput')
