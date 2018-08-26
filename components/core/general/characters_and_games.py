"""Characters and games components."""

from component_objects import Component, Element


class CharactersAndGamesModal(Component):
    """Definition of Login component."""

    first_line_delete_btn_xpath = '//*[@id="charactersModal"]/div/div/div[2]/div/div/a[1]/div/div[3]/label/i' # noqa
    first_line_confirm_delete_btn_xpath = '//*[@id="charactersModal"]/div/div/div[2]/div/div/div[1]/div/div/button[1]' # noqa

    first_line_delete_btn = Element(xpath=first_line_delete_btn_xpath)
    first_line_confirm_delete_btn = Element(xpath=first_line_confirm_delete_btn_xpath)
