"""Wizard component."""

from modules.element import Element, Component


class WhoAreYou(Component):
    """Definition of wizard home component."""

    character_name = Element(id_='whoAreYouCharacterNameInput')
    character_name_required = Element(id_='whoAreYouCharacterNameInputRequired')
    player_name = Element(id_='whoAreYouPlayerNameInput')
    player_name_required = Element(id_='whoAreYouPlayerNameInputRequired')
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
    strength_required = Element(id_='manualStrengthInputRequired')
    dexterity = Element(id_='manualDexterityInput')
    dexterity_required = Element(id_='manualDexterityInputRequired')
    constitution = Element(id_='manualConstitutionInput')
    constitution_required = Element(id_='manualConstitutionInputRequired')
    intelligence = Element(id_='manualIntelligenceInput')
    intelligence_required = Element(id_='manualIntelligenceInputRequired')
    wisdom = Element(id_='manualWisdomInput')
    wisdom_required = Element(id_='manualWisdomInputRequired')
    charisma = Element(id_='manualCharismaInput')
    charisma_required = Element(id_='manualCharismaInputRequired')


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
