"""AbilityScores components."""

from modules import Element, Component


class AbilityScoresEditModal(Component):
    """Definition of abilityScores add modal component."""

    modal_div_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]'
    strength_id = 'abilityScoresEditStrengthInput'
    dexterity_id = 'abilityScoresEditDexterityInput'
    constitution_id = 'abilityScoresEditConstitutionInput'
    intelligence_id = 'abilityScoresEditIntelligenceInput'
    wisdom_id = 'abilityScoresEditWisdomInput'
    charisma_id = 'abilityScoresEditCharismaTextarea'
    done_id = 'abilityScoresEditDoneButton'

    modal_div = Element(xpath=modal_div_xpath)
    strength = Element(id_=strength_id)
    dexterity = Element(id_=dexterity_id)
    constitution = Element(id_=constitution_id)
    intelligence = Element(id_=intelligence_id)
    wisdom = Element(id_=wisdom_id)
    charisma = Element(id_=charisma_id)
    done = Element(id_=done_id)


class AbilityScoresTable(Component):
    """Definition of abilityScoress edit modal componenet."""

    table_id = 'abilityScoresTable'
    strength_id = 'abilityScoresTableStrengthSpan'
    strength_modifier_id = 'abilityScoresTableStrengthModifierSpan'
    dexterity_id = 'abilityScoresTableDexteritySpan'
    dexterity_modifier_id = 'abilityScoresTableDexterityModifierSpan'
    constitution_id = 'abilityScoresTableConstitutionSpan'
    constitution_modifier_id = 'abilityScoresTableConstitutionModifierSpan'
    intelligence_id = 'abilityScoresTableIntelligIntelligenceSpan'
    intelligence_modifier_id = 'abilityScoresTableIntelligIntelligenceModifierSpan'
    wisdom_id = 'abilityScoresTableWisdomSpan'
    wisdom_modifier_id = 'abilityScoresTableWisdomModifierSpan'
    charisma_id = 'abilityScoresTableCharismaSpan'
    charisma_modifier_id = 'abilityScoresTableCharismaModifierSpan'

    table = Element(id_=table_id)
    strength = Element(id_=strength_id)
    strength_modifier = Element(id_=strength_modifier_id)
    dexterity = Element(id_=dexterity_id)
    dexterity_modifier = Element(id_=dexterity_modifier_id)
    constitution = Element(id_=constitution_id)
    constitution_modifier = Element(id_=constitution_modifier_id)
    intelligence = Element(id_=intelligence_id)
    intelligence_modifier = Element(id_=intelligence_modifier_id)
    wisdom = Element(id_=wisdom_id)
    wisdom_modifier = Element(id_=wisdom_modifier_id)
    charisma = Element(id_=charisma_id)
    charisma_modifier = Element(id_=charisma_modifier_id)
