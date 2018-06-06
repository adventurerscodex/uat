"""Monster component."""

from component_objects import Component, Element


class MonsterAddModal(Component):
    """Definition of Monster Add component."""

    name_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[1]/div/input'
    size_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[2]/div/input'
    type_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[3]/div/input'
    alignment_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[4]/div/input'
    armor_class_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[5]/div/input'
    hit_points_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[6]/div/input'
    speed_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[7]/div/input'
    strength_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/table/tbody/tr/td[1]/input'
    dexterity_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/table/tbody/tr/td[2]/input'
    constitution_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/table/tbody/tr/td[3]/input'
    intelligence_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/table/tbody/tr/td[4]/input'
    wisdom_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/table/tbody/tr/td[5]/input'
    charisma_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/table/tbody/tr/td[6]/input'
    saving_throws_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[8]/div/input'
    skills_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[9]/div/input'
    damage_immunities_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[10]/div/input'
    damage_vulnerabilities_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[11]/div/input'
    damage_resistances_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[12]/div/input'
    condition_immunities_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[13]/div/input'
    senses_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[14]/div/input'
    languages_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[15]/div/input'
    challenge_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[16]/div/input'
    experience_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[17]/div/input'
    description_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[18]/div/textarea'
    cancel_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[19]/button[1]'
    add_xpath = '//*[@id="addMonster"]/div/div/div[2]/form/div[19]/button[2]'

    name = Element(xpath=name_xpath)
    size = Element(xpath=size_xpath)
    type_ = Element(xpath=type_xpath)
    alignment = Element(xpath=alignment_xpath)
    armor_class = Element(xpath=armor_class_xpath)
    hit_points = Element(xpath=hit_points_xpath)
    speed = Element(xpath=speed_xpath)
    strength = Element(xpath=strength_xpath)
    dexterity = Element(xpath=dexterity_xpath)
    constitution = Element(xpath=constitution_xpath)
    intelligence = Element(xpath=intelligence_xpath)
    wisdom = Element(xpath=wisdom_xpath)
    charisma = Element(xpath=charisma_xpath)
    saving_throws = Element(xpath=saving_throws_xpath)
    skills = Element(xpath=skills_xpath)
    damage_immunities = Element(xpath=damage_immunities_xpath)
    damage_vulnerabilities = Element(xpath=damage_vulnerabilities_xpath)
    damage_resistances = Element(xpath=damage_resistances_xpath)
    condition_immunities = Element(xpath=condition_immunities_xpath)
    senses = Element(xpath=senses_xpath)
    languages = Element(xpath=languages_xpath)
    challenge = Element(xpath=challenge_xpath)
    experience = Element(xpath=experience_xpath)
    description = Element(xpath=description_xpath)
    cancel = Element(xpath=cancel_xpath)
    add = Element(xpath=add_xpath)


class MonsterModalTabs(Component):
    """Definition of Monster Tab component."""

    preview_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[1]/a/b'
    edit_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[2]/a/b'

    preview = Element(xpath=preview_xpath)
    edit = Element(xpath=edit_xpath)


class MonsterPreviewModal(Component):
    """Definition of Monster Preview component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[1]/span'
    size_type_alignment_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[1]/small'
    armor_class_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[1]/span'
    hit_points_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[2]/span'
    speed_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[3]/span'
    strength_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[11]/table/tbody' +
                      '/tr/td[1]/span'
                      )
    dexterity_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[11]/table/' +
                       'tbody/tr/td[2]/span'
                       )
    constitution_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[11]/table/' +
                          'tbody/tr/td[3]/span'
                          )
    intelligence_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[11]/table/' +
                          'tbody/tr/td[4]/span'
                          )
    wisdom_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[11]/table/tbody/' +
                    'tr/td[5]/span'
                    )
    charisma_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[11]/table/' +
                      'tbody/tr/td[6]/span'
                      )
    saving_throws_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[12]/span'
    skills_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[13]/span'
    damage_immunities_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[8]/span'
    damage_vulnerabilities_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/' +
                                    'div[7]/span'
                                    )
    damage_resistances_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[9]/span'
    condition_immunities_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[10]' +
                                  '/span'
                                  )
    senses_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[14]/span'
    languages_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[4]/span'
    challenge_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[5]/span'
    experience_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div[6]/span'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[3]/div/div'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[4]/button'

    name = Element(xpath=name_xpath)
    size_type_alignment = Element(xpath=size_type_alignment_xpath)
    armor_class = Element(xpath=armor_class_xpath)
    hit_points = Element(xpath=hit_points_xpath)
    speed = Element(xpath=speed_xpath)
    strength = Element(xpath=strength_xpath)
    dexterity = Element(xpath=dexterity_xpath)
    constitution = Element(xpath=constitution_xpath)
    intelligence = Element(xpath=intelligence_xpath)
    wisdom = Element(xpath=wisdom_xpath)
    charisma = Element(xpath=charisma_xpath)
    saving_throws = Element(xpath=saving_throws_xpath)
    skills = Element(xpath=skills_xpath)
    damage_immunities = Element(xpath=damage_immunities_xpath)
    damage_vulnerabilities = Element(xpath=damage_vulnerabilities_xpath)
    damage_resistances = Element(xpath=damage_resistances_xpath)
    condition_immunities = Element(xpath=condition_immunities_xpath)
    senses = Element(xpath=senses_xpath)
    languages = Element(xpath=languages_xpath)
    challenge = Element(xpath=challenge_xpath)
    experience = Element(xpath=experience_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)


class MonsterEditModal(Component):
    """Definition of Monster Edit component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[1]/div/input'
    size_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[2]/div/input'
    type_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[3]/div/input'
    alignment_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[4]/div/input'
    armor_class_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[5]/div/input'
    hit_points_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[6]/div/input'
    speed_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[7]/div/input'
    strength_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/table/tbody/tr/td[1]' +
                      '/input'
                      )
    dexterity_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/table/tbody/tr/td[2]' +
                       '/input'
                       )
    constitution_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/table/tbody/tr/' +
                          'td[3]/input'
                          )
    intelligence_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/table/tbody/tr/' +
                          'td[4]/input'
                          )
    wisdom_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/table/tbody/tr/td[5]/input'
    charisma_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/table/tbody/tr/td[6]/' +
                      'input'
                      )
    saving_throws_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[8]/div/input'
    skills_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[9]/div/input'
    damage_immunities_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[10]/div/' +
                               'input'
                               )
    damage_vulnerabilities_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[11]' +
                                    '/div/input'
                                    )
    damage_resistances_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[12]/div' +
                                '/input'
                                )
    condition_immunities_xpath = ('//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[13]/' +
                                  'div/input'
                                  )
    senses_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[14]/div/input'
    languages_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[15]/div/input'
    challenge_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[16]/div/input'
    experience_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[17]/div/input'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[18]/div/textarea'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[19]/button'

    name = Element(xpath=name_xpath)
    size = Element(xpath=size_xpath)
    type_ = Element(xpath=type_xpath)
    alignment = Element(xpath=alignment_xpath)
    armor_class = Element(xpath=armor_class_xpath)
    hit_points = Element(xpath=hit_points_xpath)
    speed = Element(xpath=speed_xpath)
    strength = Element(xpath=strength_xpath)
    dexterity = Element(xpath=dexterity_xpath)
    constitution = Element(xpath=constitution_xpath)
    intelligence = Element(xpath=intelligence_xpath)
    wisdom = Element(xpath=wisdom_xpath)
    charisma = Element(xpath=charisma_xpath)
    saving_throws = Element(xpath=saving_throws_xpath)
    skills = Element(xpath=skills_xpath)
    damage_immunities = Element(xpath=damage_immunities_xpath)
    damage_vulnerabilities = Element(xpath=damage_vulnerabilities_xpath)
    damage_resistances = Element(xpath=damage_resistances_xpath)
    condition_immunities = Element(xpath=condition_immunities_xpath)
    senses = Element(xpath=senses_xpath)
    languages = Element(xpath=languages_xpath)
    challenge = Element(xpath=challenge_xpath)
    experience = Element(xpath=experience_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)
