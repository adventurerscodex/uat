"""Skills components."""

from modules.element import Element, Component


class SkillsAddModal(Component):
    """Definition of skills add modal component."""

    name = Element(id_='skillsAddNameInput')
    none = Element(id_='skillsAddNoneButton')
    half = Element(id_='skillsAddHalfButton')
    proficient = Element(id_='skillsAddProfcientButton')
    expertise = Element(id_='skillsAddExpertiseButton')
    str_ = Element(id_='skillsAddStrButton')
    dex = Element(id_='skillsAddDexButton')
    con = Element(id_='skillsAddConButton')
    int_ = Element(id_='skillsAddIntButton')
    wis = Element(id_='skillsAddWisButton')
    cha = Element(id_='skillsAddChaButton')
    add = Element(id_='skillsAddAddButton')


class SkillsEditModal(Component):
    """Definition of skills edit modal component."""

    modifer = Element(id_='skillsEditNameInput')
    none = Element(id_='skillsEditNoneButton')
    half = Element(xpath='//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div/div[2]/form/div[2]/div/div/label[2]')
    proficient = Element(xpath='//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div/div[2]/form/div[2]/div/div/label[3]')
    expertise = Element(xpath='//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div/div[2]/form/div[2]/div/div/label[4]')
    done = Element(xpath='//*[@id="skills"]/div[3]/div[1]/skills/div[2]/div/div/div[3]/button')


class SkillsTable(Component):
    """Definition of skillss edit modal componenet."""

    sort_by_skill = Element(id_='skillsTableSkillSortSpan')
    sort_by_proficiency = Element(id_='skillsTableProficiencySortSpan')
    table = Element(xpath='//*[@id="skills"]/div[3]/div[1]/skills/div[1]/div/table')
