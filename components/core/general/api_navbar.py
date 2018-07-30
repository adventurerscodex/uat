"""Navbar components."""

from component_objects import Component, Element


class Loginapi(Component):
    """Definition of Login component."""

    login_link_xpath = '//*[@id="content"]/nav/div/div/login/ul/li[1]/a'

    login_link = Element(xpath=login_link_xpath)


class Username(Component):
    """Definition of Username component."""

    username_id = 'id_username'

    username = Element(id_=username_id)


class Password(Component):
    """Definition of password component."""

    password_id = 'id_password'

    password = Element(id_=password_id)


class Submit(Component):
    """Definition of log-in component."""

    submit_id = 'submit-id-submit'

    submit = Element(id_=submit_id)
