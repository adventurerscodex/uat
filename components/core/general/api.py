"""Navbar components."""

from component_objects import Component, Element


class Navbar(Component):
    """Definition of Login component."""

    login_link_xpath = '//*[@id="content"]/nav/div/div/login/ul/li[1]/a'

    login_link = Element(xpath=login_link_xpath)


class LoginForm(Component):

    username_id = 'id_username'
    password_id = 'id_password'
    submit_id = 'submit-id-submit'

    username = Element(id_=username_id)
    password = Element(id_=password_id)
    submit = Element(id_=submit_id)
