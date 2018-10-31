"""AbilityScores components."""

from component_objects import Component, Element


class AbilityScoresEditModal(Component):
    """Definition of abilityScores add modal component."""

    modal_div_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]'
    title_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]/div/div/div[1]/h4'
    strength_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]/div/div/div[2]/form/div[1]/div/input' # noqa
    dexterity_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]/div/div/div[2]/form/div[2]/div/input' # noqa
    constitution_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]/div/div/div[2]/form/div[3]/div/input' # noqa
    intelligence_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]/div/div/div[2]/form/div[4]/div/input' # noqa
    wisdom_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]/div/div/div[2]/form/div[5]/div/input' # noqa
    charisma_xpath = '//*[@id="stats"]/div[3]/div/ability-scores/div[2]/div/div/div[2]/form/div[6]/div/input' # noqa
    done_xpath = '//*[@id="abilityScoresEditDoneButton"]'

    modal_div = Element(xpath=modal_div_xpath)
    title = Element(xpath=title_xpath)
    strength = Element(xpath=strength_xpath)
    dexterity = Element(xpath=dexterity_xpath)
    constitution = Element(xpath=constitution_xpath)
    intelligence = Element(xpath=intelligence_xpath)
    wisdom = Element(xpath=wisdom_xpath)
    charisma = Element(xpath=charisma_xpath)
    done = Element(xpath=done_xpath)


class AbilityScoresTable(Component):
    """Definition of abilityScoress edit modal componenet."""

    table_id = 'abilityScoresTable'
    strength_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[1]/span'
    strength_modifier_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[1]/sup/span'
    dexterity_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[2]/span'
    dexterity_modifier_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[2]/sup/span'
    constitution_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[3]/span'
    constitution_modifier_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[3]/sup/span'
    intelligence_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[4]/span'
    intelligence_modifier_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[4]/sup/span'
    wisdom_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[5]/span'
    wisdom_modifier_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[5]/sup/span'
    charisma_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[6]/span'
    charisma_modifier_id = '//*[@id="abilityScoresTable"]/tbody/tr/td[6]/sup/span'

    table = Element(id_=table_id)
    strength = Element(xpath=strength_id)
    strength_modifier = Element(xpath=strength_modifier_id)
    dexterity = Element(xpath=dexterity_id)
    dexterity_modifier = Element(xpath=dexterity_modifier_id)
    constitution = Element(xpath=constitution_id)
    constitution_modifier = Element(xpath=constitution_modifier_id)
    intelligence = Element(xpath=intelligence_id)
    intelligence_modifier = Element(xpath=intelligence_modifier_id)
    wisdom = Element(xpath=wisdom_id)
    wisdom_modifier = Element(xpath=wisdom_modifier_id)
    charisma = Element(xpath=charisma_id)
    charisma_modifier = Element(xpath=charisma_modifier_id)
