"""DM overview component."""

from modules.element import Element, Component


class DMOverview(Component):
    """Definition of dm overview component."""

    setting = Element(id_='dmOverviewSettingInput')
    dm_name = Element(id_='dmOverviewDMNameInput')
