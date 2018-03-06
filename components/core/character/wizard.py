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

    points_left = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[3]/div/div/span')
    strength_up = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[4]/div[1]/div/div[2]/plus-minus/div[1]/div/button[1]')
    strength_down = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[4]/div[1]/div/div[2]/plus-minus/div[1]/div/button[2]')
    dexterity_up = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[4]/div[2]/div/div[2]/plus-minus/div[1]/div/button[1]')
    dexterity_down = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[4]/div[2]/div/div[2]/plus-minus/div[1]/div/button[2]')
    constitution_up = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[5]/div[1]/div/div[2]/plus-minus/div[1]/div/button[1]')
    constitution_down = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[5]/div[1]/div/div[2]/plus-minus/div[1]/div/button[2]')
    intelligence_up = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[5]/div[2]/div/div[2]/plus-minus/div[1]/div/button[1]')
    intelligence_down = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[5]/div[2]/div/div[2]/plus-minus/div[1]/div/button[2]')
    wisdom_up = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[6]/div[1]/div/div[2]/plus-minus/div[1]/div/button[1]')
    wisdom_down = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[6]/div[1]/div/div[2]/plus-minus/div[1]/div/button[2]')
    charisma_up = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[6]/div[2]/div/div[2]/plus-minus/div[1]/div/button[1]')
    charisma_down = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[6]/div[2]/div/div[2]/plus-minus/div[1]/div/button[2]')


class AbilityScoresGeneral(Component):
    """Definition of ability scoreswizard home componenet."""

    manual = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[1]/div/div/label[1]')
    point_buy = Element(xpath='//*[@id="content"]/wizard/div/div/div/wizard-ability-score-step/div/div/div[2]/div[1]/div[1]/div/div/label[2]')
