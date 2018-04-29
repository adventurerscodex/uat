"""Tracked components."""

from modules import Element, Component


class TrackedTable(Component):
    """Definition of tracked component."""

    table_xpath = '//*[@id="trackablesTable"]'
    tracked1_name_xpath = '//*[@id="trackablesTable"]/tbody/tr/td[1]/span[3]'
    tracked1_max_xpath = '//*[@id="trackablesTable"]/tbody/tr/td[2]/span'
    tracked1_used_xpath = '//*[@id="trackablesTable"]/tbody/tr/td[4]/plus-minus/div[1]/div/span'
    tracked1_used_up_xpath = ('//*[@id="trackablesTable"]/tbody/tr/td[4]/plus-minus/div[1]/div/'
                              'button[1]')
    tracked1_used_down_xpath = ('//*[@id="trackablesTable"]/tbody/tr/td[4]/plus-minus/div[1]/div/'
                                'button[2]')
    tracked1_refresh_xpath = '//*[@id="trackablesTable"]/tbody/tr/td[5]/a'

    table = Element(xpath=table_xpath)
    tracked1_name = Element(xpath=tracked1_name_xpath)
    tracked1_max = Element(xpath=tracked1_max_xpath)
    tracked1_used = Element(xpath=tracked1_used_xpath)
    tracked1_used_up = Element(xpath=tracked1_used_up_xpath)
    tracked1_used_down = Element(xpath=tracked1_used_down_xpath)
    tracked1_refresh = Element(xpath=tracked1_refresh_xpath)
