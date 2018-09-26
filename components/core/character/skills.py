"""Skills components."""

from component_objects import Component, Element


class SkillsAddModal(Component):
    """Definition of skills add modal component."""

    modal_div_id = 'addSkill'
    name_id = 'skillsAddNameInput'
    none_id = 'skillsAddNoneButton'
    half_id = 'skillsAddHalfButton'
    proficient_id = 'skillsAddProfcientButton'
    expertise_id = 'skillsAddExpertiseButton'
    str_id = 'skillsAddStrButton'
    dex_id = 'skillsAddDexButton'
    con_id = 'skillsAddConButton'
    int_id = 'skillsAddIntButton'
    wis_id = 'skillsAddWisButton'
    cha_id = 'skillsAddChaButton'
    add_id = 'skillsAddAddButton'

    modal_div = Element(id_=modal_div_id)
    name = Element(id_=name_id)
    none = Element(id_=none_id)
    half = Element(id_=half_id)
    proficient = Element(id_=proficient_id)
    expertise = Element(id_=expertise_id)
    str_ = Element(id_=str_id)
    dex = Element(id_=dex_id)
    con = Element(id_=con_id)
    int_ = Element(id_=int_id)
    wis = Element(id_=wis_id)
    cha = Element(id_=cha_id)
    add = Element(id_=add_id)


class SkillsEditModal(Component):
    """Definition of skills edit modal component."""

    modal_div_xpath = '//*[@id="skills"]/div[3]/div[1]/skills/div[2]'
    modifer_id = 'skillsEditNameInput'
    none_id = 'skillsEditNoneButton'
    half_xpath = ('//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div/div'
                  '[2]/form/div[2]/div/div/label[2]')
    proficient_xpath = ('//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div'
                        '/div[2]/form/div[2]/div/div/label[3]')
    expertise_xpath = ('//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div/'
                       'div[2]/form/div[2]/div/div/label[4]')
    done_xpath = ('//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div/div[2]/form/div[3]/button')

    modal_div = Element(xpath=modal_div_xpath)
    modifer = Element(id_=modifer_id)
    none = Element(id_=none_id)
    half = Element(xpath=half_xpath)
    proficient = Element(xpath=proficient_xpath)
    expertise = Element(xpath=expertise_xpath)
    done = Element(xpath=done_xpath)


class SkillsTable(Component):
    """Definition of skillss edit modal componenet."""

    sort_by_skill_id = 'skillsTableSkillSortSpan'
    sort_by_proficiency_id = 'skillsTableProficiencySortSpan'
    table_xpath = '//*[@id="skills"]/div[3]/div[1]/skills/div[1]/div/table'

    sort_by_skill = Element(id_=sort_by_skill_id)
    sort_by_proficiency = Element(id_=sort_by_proficiency_id)
    table = Element(xpath=table_xpath)
