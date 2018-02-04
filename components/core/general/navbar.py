"""Navbar components."""

from modules.element import Element, Component


class Login(Component):
    """Definition of Login component."""

    login_link = Element(id_='loginLink')


class Signup(Component):
    """Definition of Sign Up component."""

    signup_link = Element(id_='signupLink')


class NewImport(Component):
    """Definition of New Import component."""

    new_import_link = Element(id_='navbarImportLink')


class CharactersAndGames(Component):
    """Definition of Characters and Games component."""

    characters_and_games = Element(id_='navbarCharactersGamesLink')


class ManageParty(Component):
    """Definition of Manage Party component."""

    manage_party_link = Element(id_='navbarManagePartyLink')


class Export(Component):
    """Definition of Export component."""

    export_link = Element(id_='navbarExportLink')


class Logo(Component):
    """Definition of Logo component."""

    home_link = Element(id_='navbarLogoLink')
