"""Profile component."""

from component_objects import Component, Element


class ProfileEdit(Component):
    """Definition of profile edit componenet."""

    alignment_xpath = '//*[@id="profileAlignmentInput"]'
    deity_xpath = '//*[@id="profileDeityInput"]'
    race_xpath = '//*[@id="profileRaceInput"]'
    class_xpath = '//*[@id="profileClassInput"]'
    gender_xpath = '//*[@id="profileGenderInput"]'
    age_xpath = '//*[@id="profileAgeInput"]'
    edit_btn_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[1]/div/span' # noqa
    save_btn_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[1]/button[1]' # noqa
    cancel_btn_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[1]/button[2]' # noqa

    edit_btn = Element(xpath=edit_btn_xpath)
    save_btn = Element(xpath=save_btn_xpath)
    cancel_btn = Element(xpath=cancel_btn_xpath)
    alignment = Element(xpath=alignment_xpath)
    deity = Element(xpath=deity_xpath)
    race = Element(xpath=race_xpath)
    class_ = Element(xpath=class_xpath)
    gender = Element(xpath=gender_xpath)
    age = Element(xpath=age_xpath)


class ProfileView(Component):
    """Definition of profile view componenet."""

    alignment_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[2]/div[1]/div' # noqa
    deity_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[2]/div[2]/div'
    race_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[3]/div[1]/div'
    class_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[3]/div[2]/div'
    gender_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[4]/div[1]/div'
    age_xpath = '//*[@id="profile"]/div[1]/div[2]/profile/div/div/preview-edit/div[4]/div[2]/div'

    alignment = Element(xpath=alignment_xpath)
    deity = Element(xpath=deity_xpath)
    race = Element(xpath=race_xpath)
    class_ = Element(xpath=class_xpath)
    gender = Element(xpath=gender_xpath)
    age = Element(xpath=age_xpath)
