"""DM overview component."""

from component_objects import Element, Component


class DMOverview(Component):
    """Definition of dm overview component."""

    setting_id = 'dmOverviewSettingInput'
    dm_name_id = 'dmOverviewDMNameInput'

    setting = Element(id_=setting_id)
    dm_name = Element(id_=dm_name_id)
