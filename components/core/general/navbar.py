"""Navbar components."""

from component_objects import Component, Element


class Login(Component):
    """Definition of Login component."""

    login_link_id = 'loginLink'

    login_link = Element(id_=login_link_id)


class Signup(Component):
    """Definition of Sign Up component."""

    signup_link_id = 'signupLink'

    signup_link = Element(id_=signup_link_id)


class NewImport(Component):
    """Definition of New Import component."""

    new_import_link_id = 'navbarImportLink'

    new_import_link = Element(id_=new_import_link_id)


class CharactersAndGames(Component):
    """Definition of Characters and Games component."""

    characters_and_games_xpath = '//*[@id="navbar"]/ul/li[2]/a'

    characters_and_games = Element(xpath=characters_and_games_xpath)


class ManageParty(Component):
    """Definition of Manage Party component."""

    manage_party_link_id = 'navbarManagePartyLink'

    manage_party_link = Element(id_=manage_party_link_id)


class Export(Component):
    """Definition of Export component."""

    export_link_id = 'navbarExportLink'

    export_link = Element(id_=export_link_id)


class Logo(Component):
    """Definition of Logo component."""

    home_link_id = 'navbarLogoLink'

    home_link = Element(id_=home_link_id)
