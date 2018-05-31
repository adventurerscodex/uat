"""DM Read Aloud Text component."""

from component_objects import Component, Element


class ReadAloudTextAddModal(Component):
    """Definition of Read Aloud Text Add component."""

    name_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/player-text-section/table/thead/tr/th[1]' # noqa
    description_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/player-text-section/table/thead/tr/th[2]' # noqa
    add_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/player-text-section/table/thead/tr/th[4]/a/i' # noqa

    name = Element(xpath=name_xpath)
    description = Element(xpath=description_xpath)
    add = Element(xpath=add_xpath)


class ReadAloudTextModalTabs(Component):
    """Definition of Read Aloud Text Tab component."""

    preview_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[1]/a/b'
    edit_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[2]/a/b'

    preview = Element(xpath=preview_xpath)
    edit = Element(xpath=edit_xpath)


class ReadAloudTextPreviewModal(Component):
    """Definition of Read Aloud Text Preview component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[1]/div/div'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div/div/p'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[3]/button'

    name = Element(xpath=name_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)


class ReadAloudTextEditModal(Component):
    """Definition of Read Aloud Text Edit component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[1]/div[2]/textarea' # noqa
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[2]/button'

    name = Element(xpath=name_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)
