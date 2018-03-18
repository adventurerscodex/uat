"""New character/campaign component."""

from modules.element import Element, Component


class NewCharacterCampaign(Component):
    """Definition of new character/campaign componenet."""

    import_existing_id = 'newCharCampaignImportExistingButton'
    get_started_id = 'newCharCampaignGetStartedButton'
    dm_id = 'newCharCampaignDMButton'
    player_id = 'newCharCampaignPlayerButton'
    back_id = 'newCharCampaignBackButton'
    next_id = 'newCharCampaignNextButton'
    finish_id = 'newCharCampaignFinishButton'

    import_existing = Element(id_=import_existing_id)
    get_started = Element(id_=get_started_id)
    dm = Element(id_=dm_id)
    player = Element(id_=player_id)
    back = Element(id_=back_id)
    next_ = Element(id_=next_id)
    finish = Element(id_=finish_id)
