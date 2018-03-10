"""Tracked components."""

from modules.element import Element, Component


class TrackedTable(Component):
    """Definition of tracked component."""

    table = Element(xpath='//*[@id="trackablesTable"]')
    tracked1_name = Element(xpath='//*[@id="trackablesTable"]/tbody/tr/td[1]/span[3]')
    tracked1_max = Element(xpath='//*[@id="trackablesTable"]/tbody/tr/td[2]/span')
    tracked1_used = Element(xpath='//*[@id="trackablesTable"]/tbody/tr/td[4]/plus-minus/div[1]/div/span')
    tracked1_used_up = Element(xpath='//*[@id="trackablesTable"]/tbody/tr/td[4]/plus-minus/div[1]/div/button[1]')
    tracked1_used_down = Element(xpath='//*[@id="trackablesTable"]/tbody/tr/td[4]/plus-minus/div[1]/div/button[2]')
    tracked1_refresh = Element(xpath='//*[@id="trackablesTable"]/tbody/tr/td[5]/a')
