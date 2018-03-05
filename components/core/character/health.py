"""Health components."""

from modules.element import Element, Component


class HitPointHitDice(Component):
    """Definition of HitPointsHitDice component."""

    max_hit_points = Element(xpath='//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div/table/tbody/tr/td[2]/span')
    hit_points_bar_label = Element(xpath='//*[@id="hitpointsCounter"]')
    damage_up = Element(xpath='//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div/table/tbody/tr/td[3]/plus-minus/div[1]/div/button[1]')
    damage_down = Element(xpath='//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div/table/tbody/tr/td[3]/plus-minus/div[1]/div/button[2]')
    reset = Element(xpath='//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div/table/tbody/tr/td[4]/a')
    hitdice1 = Element(xpath='//*[@id="0"]')
    hitdice2 = Element(xpath='//*[@id="1"]')
    hitdice3 = Element(xpath='//*[@id="2"]')
    open_edit_modal = Element(xpath='//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div/table/tbody/tr/td[1]')


class HitPointEditModal(Component):
    """Definition of HitPointsHitDice component."""

    max_hit_points = Element(xpath='//*[@id="viewHealth"]/div/div/div[2]/form/div[1]/div/input')
    damage = Element(xpath='//*[@id="viewHealth"]/div/div/div[2]/form/div[2]/div/input')
    temp_hit_points = Element(xpath='//*[@id="viewHealth"]/div/div/div[2]/form/div[3]/div/input')
    hit_dice_type = Element(xpath='//*[@id="viewHealth"]/div/div/div[2]/form/div[4]/div/input')
    done = Element(xpath='//*[@id="viewHealth"]/div/div/div[2]/form/div[5]/button')
