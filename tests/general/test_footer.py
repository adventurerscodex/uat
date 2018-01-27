"""UAT test file for Adventurer's Codex footer."""
from selenium.webdriver.support import expected_conditions as EC # noqa

from components.general.footer import Footer


def test_facebook_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to facebook."""
    print('As a player, navbar footer links to facebook.')
    footer = Footer(browser)

    footer.facebook.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://www.facebook.com/adventurerscodex'

def test_twitter_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to twitter."""
    print('As a player, navbar footer links to twitter.')
    footer = Footer(browser)

    footer.twitter.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://twitter.com/adventurercodex'

def test_reddit_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to reddit."""
    print('As a player, navbar footer links to reddit.')
    footer = Footer(browser)

    footer.reddit.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://www.reddit.com/r/adventurerscodex/'

def test_google_plus_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to google +."""
    print('As a player, navbar footer links to google +.')
    footer = Footer(browser)

    footer.google_plus.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://plus.google.com/105624626079092258118'

def test_github_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to github."""
    print('As a player, navbar footer links to github.')
    footer = Footer(browser)

    footer.github.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://github.com/adventurerscodex'

def test_rss_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to rss."""
    print('As a player, navbar footer links to rss.')
    footer = Footer(browser)

    footer.rss.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://adventurerscodex.com/feed.xml'

def test_tiny_letter_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to tiny letter."""
    print('As a player, navbar footer links to tiny letter.')
    footer = Footer(browser)

    footer.tiny_letter.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://tinyletter.com/adventurerscodex'

def test_blog_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to tiny letter."""
    print('As a player, navbar footer links to tiny letter.')
    footer = Footer(browser)

    footer.blog.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://adventurerscodex.com/'

def test_contact_us_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to contact us."""
    print('As a player, navbar footer links to contact us.')
    footer = Footer(browser)

    footer.contact_us.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://adventurerscodex.com/support.html'

def test_patreon_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to patreon."""
    print('As a player, navbar footer links to patreon.')
    footer = Footer(browser)

    footer.patreon.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://www.patreon.com/bePatron?u=5313385'

def test_ogl_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to ogl."""
    print('As a player, navbar footer links to ogl.')
    footer = Footer(browser)

    footer.ogl.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'http://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf'
