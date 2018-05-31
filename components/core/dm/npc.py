"""NPC component."""

from component_objects import Element, Component


class NPCAddModal(Component):
    """Definition of NPC Add component."""

    name_xpath = '//*[@id="addNPC"]/div/div/div[2]/form/div[1]/div/input'
    race_xpath = '//*[@id="addNPC"]/div/div/div[2]/form/div[2]/div/input'
    description_xpath = '//*[@id="addNPC"]/div/div/div[2]/form/div[3]/div/textarea'
    add_xpath = '//*[@id="addNPC"]/div/div/div[2]/form/div[4]/button'

    name = Element(xpath=name_xpath)
    race = Element(xpath=race_xpath)
    description = Element(xpath=description_xpath)
    add = Element(xpath=add_xpath)


class NPCModalTabs(Component):
    """Definition of NPC Tab component."""

    preview_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[1]/a'
    edit_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[2]/a'

    preview = Element(xpath=preview_xpath)
    edit = Element(xpath=edit_xpath)


class NPCPreviewModal(Component):
    """Definition of NPC Preview component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[1]/span'
    race_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[1]/small'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div/div'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[3]/button'

    name = Element(xpath=name_xpath)
    race = Element(xpath=race_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)


class NPCEditModal(Component):
    """Definition of NPC Edit component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[1]/div/input'
    race_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[2]/div/input'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[3]/div/textarea'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[4]/button'

    name = Element(xpath=name_xpath)
    race = Element(xpath=race_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)
