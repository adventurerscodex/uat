"""Health components."""

from component_objects import Element, Elements, Component


class HitPointHitDice(Component):
    """Definition of HitPointsHitDice component."""

    max_hit_points_xpath = ('//*[@id="stats"]/div[1]/div[2]/stats/div/div/div'
                            '/div/table/tbody/tr/td[2]/span')
    hit_points_bar_label_xpath = '//*[@id="hitpointsCounter"]'
    hit_points_bar_regular_hp_xpath = '//*[@id="regularHitPoints"]'
    damage_up_xpath = ('//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div/'
                       'table/tbody/tr/td[3]/plus-minus/div[1]/div/button[1]')
    damage_down_xpath = ('//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div'
                         '/table/tbody/tr/td[3]/plus-minus/div[1]/div/'
                         'button[2]')
    reset_xpath = ('//*[@id="stats"]/div[1]/div[2]/stats/div/div/div/div/table'
                   '/tbody/tr/td[4]/a')
    hitdice1_xpath = '//*[@id="0"]'
    hitdice2_xpath = '//*[@id="1"]'
    hitdice3_xpath = '//*[@id="2"]'
    toast_title_xpath = '//*[@id="toast-container"]/div/div[2]'
    toast_message_xpath = '//*[@id="toast-container"]/div/div[3]'
    death_successes_empty_xpath = 'ds-success-empty'
    death_failures_empty_xpath = 'ds-failure-empty'
    hit_dice_list_xpath = ('//*[@id="stats"]/div[1]/div[2]/stats/div/div/div'
                           '/div/div[2]/div')
    open_edit_modal_xpath = ('//*[@id="stats"]/div[1]/div[2]/stats/div/div/div'
                             '/div/table/tbody/tr/td[1]')

    max_hit_points = Element(xpath=max_hit_points_xpath)
    hit_points_bar_label = Element(xpath=hit_points_bar_label_xpath)
    hit_points_bar_regular_hp = Element(xpath=hit_points_bar_regular_hp_xpath)
    damage_up = Element(xpath=damage_up_xpath)
    damage_down = Element(xpath=damage_down_xpath)
    reset = Element(xpath=reset_xpath)
    hitdice1 = Element(xpath=hitdice1_xpath)
    hitdice2 = Element(xpath=hitdice2_xpath)
    hitdice3 = Element(xpath=hitdice3_xpath)
    toast_title = Element(xpath=toast_title_xpath)
    toast_message = Element(xpath=toast_message_xpath)
    death_successes_empty = Elements(class_name=death_successes_empty_xpath)
    death_failures_empty = Elements(class_name=death_failures_empty_xpath)
    hit_dice_list = Element(xpath=hit_dice_list_xpath)
    open_edit_modal = Element(xpath=open_edit_modal_xpath)


class HitPointEditModal(Component):
    """Definition of HitPointsHitDice component."""

    max_hit_points_xpath = ('//*[@id="viewHealth"]/div/div/div[2]/form/div[1]'
                            '/div/input')
    damage_xpath = '//*[@id="viewHealth"]/div/div/div[2]/form/div[2]/div/input'
    temp_hit_points_xpath = ('//*[@id="viewHealth"]/div/div/div[2]/form/div[3]'
                             '/div/input')
    hit_dice_type_xpath = ('//*[@id="viewHealth"]/div/div/div[2]/form/div[4]/'
                           'div/input')
    done_xpath = '//*[@id="viewHealth"]/div/div/div[2]/form/div[5]/button'

    max_hit_points = Element(xpath=max_hit_points_xpath)
    damage = Element(xpath=damage_xpath)
    temp_hit_points = Element(xpath=temp_hit_points_xpath)
    hit_dice_type = Element(xpath=hit_dice_type_xpath)
    done = Element(xpath=done_xpath)
