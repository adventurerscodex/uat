"""DM Point of Interest component."""

from component_objects import Component, Element


class PointOfInterestAddModal(Component):
    """Definition of Point of Interest Add component."""

    name_xpath = '//*[@id="addPointOfInterest"]/div/div/div[2]/form/div[1]/div/input' # noqa
    description_xpath = '//*[@id="addPointOfInterest"]/div/div/div[2]/form/div[2]/div/textarea' # noqa
    add_plus_icon_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/point-of-interest-section/table/thead/tr/th[3]/a/i' # noqa
    add_new_point_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/point-of-interest-section/table/tbody/tr/td' # noqa
    remove_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/point-of-interest-section/table/tbody/tr/td[4]/a/i' # noqa
    add_xpath = '//*[@id="addPointOfInterest"]/div/div/div[2]/form/div[3]/button' # noqa

    name = Element(xpath=name_xpath)
    description = Element(xpath=description_xpath)
    add_plus_icon = Element(xpath=add_plus_icon_xpath)
    add_new_point = Element(xpath=add_new_point_xpath)
    remove = Element(xpath=remove_xpath)
    add = Element(xpath=add_xpath)


class PointOfInterestModalTabs(Component):
    """Definition of Point of Interest Tab component."""

    preview_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[1]/a/b'
    edit_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/ul/li[2]/a'

    preview = Element(xpath=preview_xpath)
    edit = Element(xpath=edit_xpath)


class PointOfInterestPreviewModal(Component):
    """Definition of Point of Interest Preview component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[1]/span'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[2]/div/div'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[1]/div[3]/button'

    name = Element(xpath=name_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)


class PointOfInterestEditModal(Component):
    """Definition of Point of Interest Edit component."""

    name_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[1]/div/input'
    description_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[2]/div/textarea'
    done_xpath = '//*[@id="viewWeapon"]/div/div/div[2]/div/div[2]/form/div[3]/button'

    name = Element(xpath=name_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)


class PointOfInterestTable(Component):
    """Definition of Point Of Interest Table component."""

    name_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/point-of-interest-section/table/tbody/tr/td[1]' # noqa
    description_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/point-of-interest-section/table/tbody/tr/td[3]' # noqa
    first_row_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/point-of-interest-section/table/tbody' # noqa
    trash_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/point-of-interest-section/table/tbody/tr/td[4]/a/i' # noqa

    name = Element(xpath=name_xpath)
    description = Element(xpath=description_xpath)
    first_row = Element(xpath=first_row_xpath)
    trash = Element(xpath=trash_xpath)
