"""UAT test file for Adventurer's Codex core dm tools."""

from components.core.general.new_character_campaign import NewCharacterCampaign
from components.core.character import wizard
from components.core.dm.wizard import TellUsAStory
from utils import utils as ut


def test_dm_wizard(browser):
    """Test dm wizard using required values."""
    print('As a dm, I should be able to navigate through the dm wizard.')

    wizard_main = NewCharacterCampaign(browser)
    tell_us_a_story = TellUsAStory(browser)

    wizard_main.get_started.click()
    wizard_main.dm.click()
    wizard_main.next_.click()

    tell_us_a_story.campaign_name = 'Test Campaign'
    tell_us_a_story.player_name = 'Automated Testing Bot.'

    wizard_main.finish.click()
