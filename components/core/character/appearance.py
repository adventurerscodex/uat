"""Appearance component."""

from component_objects import Component, Element


class AppearanceEdit(Component):
    """Definition of appearance edit componenet."""

    # height_xpath = ''
    weight_xpath = '//*[@id="appearanceWeightInput"]'
    hair_color_xpath = '//*[@id="appearanceHairColorInput"]'
    eye_color_xpath = '//*[@id="appearanceEyeColorInput"]'
    skin_color_xpath = '//*[@id="appearanceSkinColorInput"]'

    # height = Element(xpath=height_xpath)
    weight = Element(xpath=weight_xpath)
    hair_color = Element(xpath=hair_color_xpath)
    eye_color = Element(xpath=eye_color_xpath)
    skin_color = Element(xpath=skin_color_xpath)


class AppearanceView(Component):
    """Definition of appearance view componenet."""

    # height_xpath = ''
    weight_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[5]/div[1]/div' # noqa
    hair_color_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[5]/div[2]/div' # noqa
    eye_color_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[6]/div[1]/div' # noqa
    skin_color_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[6]/div[2]/div' # noqa

    # height = Element(xpath=height_xpath)
    weight = Element(xpath=weight_xpath)
    hair_color = Element(xpath=hair_color_xpath)
    eye_color = Element(xpath=eye_color_xpath)
    skin_color = Element(xpath=skin_color_xpath)
