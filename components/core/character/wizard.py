"""Wizard component."""

from modules import Element, Component


class WhoAreYou(Component):
    """Definition of wizard home component."""

    character_name_id = 'whoAreYouCharacterNameInput'
    character_name_required_id = 'whoAreYouCharacterNameInputRequired'
    player_name_id = 'whoAreYouPlayerNameInput'
    player_name_required_id = 'whoAreYouPlayerNameInputRequired'
    alignment_id = 'whoAreYouAlignmentInput'
    deity_id = 'whoAreYouDeityInput'
    race_id = 'whoAreYouRaceInput'
    class_id = 'whoAreYouClassInput'
    gender_id = 'whoAreYouGenderInput'
    age_id = 'whoAreYouAgeInput'
    background_id = 'whoAreYouBackgroundInput'
    backpack_id = 'whoAreYouBackpackSelect'
    level_id = 'whoAreYouLevelInput'
    experience_id = 'whoAreYouExperienceInput'

    character_name = Element(id_=character_name_id)
    character_name_required = Element(id_=character_name_required_id)
    player_name = Element(id_=player_name_id)
    player_name_required = Element(id_=player_name_required_id)
    alignment = Element(id_=alignment_id)
    deity = Element(id_=deity_id)
    race = Element(id_=race_id)
    class_ = Element(id_=class_id)
    gender = Element(id_=gender_id)
    age = Element(id_=age_id)
    background = Element(id_=background_id)
    backpack = Element(id_=backpack_id)
    level = Element(id_=level_id)
    experience = Element(id_=experience_id)


class AbilityScoresManual(Component):
    """Definition of ability scoreswizard home componenet."""

    strength_id = 'manualStrengthInput'
    strength_required_id = 'manualStrengthInputRequired'
    dexterity_id = 'manualDexterityInput'
    dexterity_required_id = 'manualDexterityInputRequired'
    constitution_id = 'manualConstitutionInput'
    constitution_required_id = 'manualConstitutionInputRequired'
    intelligence_id = 'manualIntelligenceInput'
    intelligence_required_id = 'manualIntelligenceInputRequired'
    wisdom_id = 'manualWisdomInput'
    wisdom_required_id = 'manualWisdomInputRequired'
    charisma_id = 'manualCharismaInput'
    charisma_required_id = 'manualCharismaInputRequired'

    strength = Element(id_=strength_id)
    strength_required = Element(id_=strength_required_id)
    dexterity = Element(id_=dexterity_id)
    dexterity_required = Element(id_=dexterity_required_id)
    constitution = Element(id_=constitution_id)
    constitution_required = Element(id_=constitution_required_id)
    intelligence = Element(id_=intelligence_id)
    intelligence_required = Element(id_=intelligence_required_id)
    wisdom = Element(id_=wisdom_id)
    wisdom_required = Element(id_=wisdom_required_id)
    charisma = Element(id_=charisma_id)
    charisma_required = Element(id_=charisma_required_id)


class AbilityScoresPointBuy(Component):
    """Definition of ability scoreswizard home componenet."""

    points_left_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-ability'
                         '-score-step/div/div/div[2]/div[1]/div[3]/div/div/'
                         'span')
    strength_up_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-ability'
                         '-score-step/div/div/div[2]/div[1]/div[4]/div[1]/div/'
                         'div[2]/plus-minus/div[1]/div/button[1]')
    strength_down_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-'
                           'ability-score-step/div/div/div[2]/div[1]/div[4]/'
                           'div[1]/div/div[2]/plus-minus/div[1]/div/button[2]')
    dexterity_up_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-'
                          'ability-score-step/div/div/div[2]/div[1]/div[4]/div'
                          '[2]/div/div[2]/plus-minus/div[1]/div/button[1]')
    dexterity_down_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-'
                            'ability-score-step/div/div/div[2]/div[1]/div[4]/'
                            'div[2]/div/div[2]/plus-minus/div[1]/div/button'
                            '[2]')
    constitution_up_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-'
                             'ability-score-step/div/div/div[2]/div[1]/div[5]/'
                             'div[1]/div/div[2]/plus-minus/div[1]/div/button'
                             '[1]')
    constitution_down_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-'
                               'ability-score-step/div/div/div[2]/div[1]/div'
                               '[5]/div[1]/div/div[2]/plus-minus/div[1]/div/'
                               'button[2]')
    intelligence_up_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-'
                             'ability-score-step/div/div/div[2]/div[1]/div[5]/'
                             'div[2]/div/div[2]/plus-minus/div[1]/div/button'
                             '[1]')
    intelligence_down_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard'
                               '-ability-score-step/div/div/div[2]/div[1]/div'
                               '[5]/div[2]/div/div[2]/plus-minus/div[1]/div/'
                               'button[2]')
    wisdom_up_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-ability'
                       '-score-step/div/div/div[2]/div[1]/div[6]/div[1]/div/'
                       'div[2]/plus-minus/div[1]/div/button[1]')
    wisdom_down_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-ability'
                         '-score-step/div/div/div[2]/div[1]/div[6]/div[1]/div/'
                         'div[2]/plus-minus/div[1]/div/button[2]')
    charisma_up_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-ability'
                         '-score-step/div/div/div[2]/div[1]/div[6]/div[2]/div/'
                         'div[2]/plus-minus/div[1]/div/button[1]')
    charisma_down_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-'
                           'ability-score-step/div/div/div[2]/div[1]/div[6]/'
                           'div[2]/div/div[2]/plus-minus/div[1]/div/button[2]')

    points_left = Element(xpath=points_left_xpath)
    strength_up = Element(xpath=strength_up_xpath)
    strength_down = Element(xpath=strength_down_xpath)
    dexterity_up = Element(xpath=dexterity_up_xpath)
    dexterity_down = Element(xpath=dexterity_down_xpath)
    constitution_up = Element(xpath=constitution_up_xpath)
    constitution_down = Element(xpath=constitution_down_xpath)
    intelligence_up = Element(xpath=intelligence_up_xpath)
    intelligence_down = Element(xpath=intelligence_down_xpath)
    wisdom_up = Element(xpath=wisdom_up_xpath)
    wisdom_down = Element(xpath=wisdom_down_xpath)
    charisma_up = Element(xpath=charisma_up_xpath)
    charisma_down = Element(xpath=charisma_down_xpath)


class AbilityScoresGeneral(Component):
    """Definition of ability scoreswizard home componenet."""

    manual_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-ability-'
                    'score-step/div/div/div[2]/div[1]/div[1]/div/div/label[1]')
    point_buy_xpath = ('//*[@id="content"]/wizard/div/div/div/wizard-ability'
                       '-score-step/div/div/div[2]/div[1]/div[1]/div/div/label'
                       '[2]')

    manual = Element(xpath=manual_xpath)
    point_buy = Element(xpath=point_buy_xpath)
