"""Background component."""

from component_objects import Component, Element


class BackgroundEdit(Component):
    """Definition of background edit component."""

    traits_xpath = '//*[@id="backgroundTraitsTextarea"]'
    ideals_xpath = '//*[@id="backgroundIdealsTextarea"]'
    bonds_xpath = '//*[@id="backgroundBondsTextarea"]'
    flaws_xpath = '//*[@id="backgroundFlawsTextarea"]'
    name_xpath = '//*[@id="profileBackgroundInput"]'

    edit_btn_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[1]/div[2]/span' # noqa
    save_btn_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[1]/button[1]' # noqa
    cancel_btn_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[1]/button[2]' # noqa

    name = Element(xpath=name_xpath)
    edit_btn = Element(xpath=edit_btn_xpath)
    save_btn = Element(xpath=save_btn_xpath)
    cancel_btn = Element(xpath=cancel_btn_xpath)
    traits = Element(xpath=traits_xpath)
    ideals = Element(xpath=ideals_xpath)
    bonds = Element(xpath=bonds_xpath)
    flaws = Element(xpath=flaws_xpath)


class BackgroundView(Component):
    """Definition of background view component."""

    traits_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[2]/div[1]/div' # noqa
    ideals_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[2]/div[2]/div' # noqa
    bonds_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[2]/div[3]/div' # noqa
    flaws_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[2]/div[4]/div' # noqa
    name_xpath = '//*[@id="profile"]/div[2]/div/background/div/div/preview-edit/div[1]/div[1]/h3' # noqa

    name = Element(xpath=name_xpath)
    traits = Element(xpath=traits_xpath)
    ideals = Element(xpath=ideals_xpath)
    bonds = Element(xpath=bonds_xpath)
    flaws = Element(xpath=flaws_xpath)
