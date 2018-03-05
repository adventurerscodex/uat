"""AbilityScores components."""

from modules.element import Element, Component


class AbilityScoresEditModal(Component):
    """Definition of abilityScores add modal component."""

    strength = Element(id_='abilityScoresEditStrengthInput')
    dexterity = Element(id_='abilityScoresEditDexterityInput')
    constitution = Element(id_='abilityScoresEditConstitutionInput')
    intelligence = Element(id_='abilityScoresEditIntelligenceInput')
    wisdom = Element(id_='abilityScoresEditWisdomInput')
    charisma = Element(id_='abilityScoresEditCharismaTextarea')
    done = Element(id_='abilityScoresEditDoneButton')


class AbilityScoresTable(Component):
    """Definition of abilityScoress edit modal componenet."""

    table = Element(id_='abilityScoresTable')
    strength = Element(id_='abilityScoresTableStrengthSpan')
    strength_modifier = Element(id_='abilityScoresTableStrengthModifierSpan')
    dexterity = Element(id_='abilityScoresTableDexteritySpan')
    dexterity_modifier = Element(id_='abilityScoresTableDexterityModifierSpan')
    constitution = Element(id_='abilityScoresTableConstitutionSpan')
    constitution_modifier = Element(id_='abilityScoresTableConstitutionModifierSpan')
    intelligence = Element(id_='abilityScoresTableIntelligIntelligenceSpan')
    intelligence_modifier = Element(id_='abilityScoresTableIntelligIntelligenceModifierSpan')
    wisdom = Element(id_='abilityScoresTableWisdomSpan')
    wisdom_modifier = Element(id_='abilityScoresTableWisdomModifierSpan')
    charisma = Element(id_='abilityScoresTableCharismaSpan')
    charisma_modifier = Element(id_='abilityScoresTableCharismaModifierSpan')
