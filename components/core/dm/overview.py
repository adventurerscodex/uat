"""DM overview component."""

from component_objects import Component, Element


class DMOverview(Component):
    """Definition of dm overview component."""

    edit_btn_xpath = '//*[@id="overview-tab"]/campaign-overview/div/div[2]/div[2]/div/preview-edit/div[1]/div/span' # noqa
    save_btn_xpath = '//*[@id="overview-tab"]/campaign-overview/div/div[2]/div[2]/div/preview-edit/div[1]/button[1]' # noqa
    setting_label_xpath = '//*[@id="overview-tab"]/campaign-overview/div/div[2]/div[2]/div/preview-edit/div[2]/div[2]/div' # noqa
    setting_input_xpath = '//*[@id="dmOverviewSettingInput"]'
    dm_name_label_xpath = '//*[@id="overview-tab"]/campaign-overview/div/div[2]/div[2]/div/preview-edit/div[2]/div[1]/div' # noqa
    dm_name_input_xpath = '//*[@id="dmOverviewDMNameInput"]'

    setting_label = Element(xpath=setting_label_xpath)
    setting_input = Element(xpath=setting_input_xpath)
    dm_name_label = Element(xpath=dm_name_label_xpath)
    dm_name_input = Element(xpath=dm_name_input_xpath)
    edit_btn = Element(xpath=edit_btn_xpath)
    save_btn = Element(xpath=save_btn_xpath)
