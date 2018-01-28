"""Wizard component."""

from modules.element import Element, Component


class WhoAreYou(Component):
    """Definition of wizard home component."""

    character_name = Element(id_='whoAreYouCharacterName')
    player_name = Element(id_='whoAreYouPlayerNameInput')
    alignment = Element(id_='whoAreYouAlignmentInput')
    deity = Element(id_='whoAreYouDeityInput')
    race = Element(id_='whoAreYouRaceInput')
    class_ = Element(id_='whoAreYouClassInput')
    gender = Element(id_='whoAreYouGenderInput')
    age = Element(id_='whoAreYouAgeInput')
    background = Element(id_='whoAreYouBackgroundInput')
    backpack = Element(id_='whoAreYouBackpackSelect')
    level = Element(id_='whoAreYouLevelInput')
    experience = Element(id_='whoAreYouExperienceInput')


class AbilityScoresManual(Component):
    """Definition of ability scoreswizard home componenet."""

    strength = Element(id_='manualStrengthInput')
    dexterity = Element(id_='manualDexterityInput')
    constitution = Element(id_='manualConstitutionInput')
    intelligence = Element(id_='manualIntelligenceInput')
    wisdom = Element(id_='manualWisdomInput')
    charisma = Element(id_='manualCharismaInput')


class AbilityScoresPointBuy(Component):
    """Definition of ability scoreswizard home componenet."""

    points_left = Element(id_='pointBuyPointsLeftSpan')
    strength_up = Element(id_='pointBuyStrengthUpButton')
    strength_down = Element(id_='pointBuyStrengthDownButton')
    dexterity_up = Element(id_='pointBuyDexterityUpButton')
    dexterity_down = Element(id_='pointBuyDexterityDownButton')
    constitution_up = Element(id_='pointBuyConstitutionUpButton')
    constitution_down = Element(id_='pointBuyConstitutionDownButton')
    intelligence_up = Element(id_='pointBuyIntelligenceUpButton')
    intelligence_down = Element(id_='pointBuyIntelligenceDownButton')
    wisdom_up = Element(id_='pointBuyWisdomUpButton')
    wisdom_down = Element(id_='pointBuyWisdomDownButton')
    charisma_up = Element(id_='pointBuyCharismaUpButton')
    charisma_down = Element(id_='pointBuyCharismaDownButton')


class AbilityScoresGeneral(Component):
    """Definition of ability scoreswizard home componenet."""

    manual = Element(id_='abilityScoresManuallButton')
    point_buy = Element(id_='abilityScoresManualPointBuyButton')
    back = Element(id_='abilityScoresBackButton')
    finish = Element(id_='abilityScoresFinishButton')
