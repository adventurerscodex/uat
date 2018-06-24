from component_objects import Component, Element


class MapOrImageAddModal(Component):
    """Definition of Map or Image Add component."""

    name_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/maps-and-images-section/table/thead/tr/th[1]' # noqa
    link_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/maps-and-images-section/table/thead/tr/th[3]' # noqa
    description_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/maps-and-images-section/table/thead/tr/th[2]' # noqa
    add_xpath = '//*[@id="encounter-tab"]/encounter/div/div/div[2]/div[2]/encounter-detail/div/div[2]/maps-and-images-section/table/thead/tr/th[5]/a/i' # noqa

    name = Element(xpath=name_xpath)
    link = Element(xpath=link_xpath)
    description = Element(xpath=description_xpath)
    add = Element(xpath=add_xpath)


class MapOrImageModalTabs(Component):
    """Definition of Map or Image Tab component."""

    preview_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/ul/li[1]/a/b'
    edit_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/ul/li[2]/a/b'

    preview = Element(xpath=preview_xpath)
    edit = Element(xpath=edit_xpath)


class MapOrImagePreviewModal(Component):
    """Definition of Map or Image Preview component."""

    name_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[1]/div[1]/div[1]/span' # noqa
    link_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[1]/div[1]/div[2]/div/small/em' # noqa
    description_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[1]/div[1]/div[3]/div/div' # noqa
    done_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[2]/button'

    name = Element(xpath=name_xpath)
    link = Element(xpath=link_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)


class MapOrImageEditModal(Component):
    """Definition of Map or Image Edit component."""

    name_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[1]/div[2]/form/div[1]/div/input' # noqa
    link_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/input' # noqa
    description_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[1]/div[2]/form/div[3]/div/textarea' # noqa
    done_xpath = '//*[@id="viewMapOrImage"]/div/div/div[2]/div[2]/button'

    name = Element(xpath=name_xpath)
    link = Element(xpath=link_xpath)
    description = Element(xpath=description_xpath)
    done = Element(xpath=done_xpath)
