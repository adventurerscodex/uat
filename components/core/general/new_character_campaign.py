"""New character/campaign component."""

from modules.element import Element, Component


class NewCharacterCampaign(Component):
    """Definition of new character/campaign componenet."""

    import_existing = Element(id_='newCharCampaignImportExistingButton')
    get_started = Element(id_='newCharCampaignGetStartedButton')
    dm = Element(id_='newCharCampaignDMButton')
    player = Element(id_='newCharCampaignPlayerButton')
    back = Element(id_='newCharCampaignBackButton')
    next_ = Element(id_='newCharCampaignNextButton')
    finish = Element(id_='newCharCampaignFinishButton')
