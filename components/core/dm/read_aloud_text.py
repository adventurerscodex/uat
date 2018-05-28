"""DM Read Aloud Text component."""

from component_objects import Element, Component


class ReadAloudTextAddModal(Component):
    """Definition of Point of Interest Add component."""

    name_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/player-text-section/table/thead/tr/th[1]' # noqa
    description_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/player-text-section/table/thead/tr/th[2]' # noqa
    add_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/player-text-section/table/thead/tr/th[4]/a/i' # noqa

    name = Element(xpath_=name_xpath)
    description = Element(xpath_=description_xpath)
    add = Element(xpath_=add_xpath)


class ReadAloudTextModalTabs(Component):
    """Definition of Point of Interest Tab component."""

    preview_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[1]/a/b'
    edit_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[2]/a/b'

    preview = Element(xpath_=preview_xpath)
    edit = Element(xpath_=edit_xpath)


class ReadAloudTextPreviewModal(Component):
    """Definition of Point of Interest Preview component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[1]/div/div'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div/div/p'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[3]/button'

    name = Element(xpath_=name_xpath)
    description = Element(xpath_=description_xpath)
    done = Element(xpath_=done_xpath)


class ReadAloudTextEditModal(Component):
    """Definition of Point of Interest Edit component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[1]/div[2]/textarea' # noqa
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[2]/button'

    name = Element(xpath_=name_xpath)
    description = Element(xpath_=description_xpath)
    done = Element(xpath_=done_xpath)
