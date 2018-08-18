"""UAT test file for Adventurer's Codex footer."""
from conftest import DEFAULT_WAIT_TIME
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.general.footer import Footer
from expected_conditions.general import url_in_new_tab_matches

def test_facebook_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to facebook."""
    print('As a player, navbar footer links to facebook.')

    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.facebook_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.facebook.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://www.facebook.com/adventurerscodex')
    )

    assert browser.current_url.strip() == 'https://www.facebook.com/adventurerscodex'

def test_twitter_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to twitter."""
    print('As a player, navbar footer links to twitter.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.twitter_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.twitter.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://twitter.com/adventurercodex')
    )

    assert browser.current_url.strip() == 'https://twitter.com/adventurercodex'

def test_reddit_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to reddit."""
    print('As a player, navbar footer links to reddit.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.reddit_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.reddit.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://www.reddit.com/r/adventurerscodex/')
    )

    assert browser.current_url.strip() == 'https://www.reddit.com/r/adventurerscodex/'

def test_google_plus_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to google +."""
    print('As a player, navbar footer links to google +.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.google_plus_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.google_plus.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://plus.google.com/105624626079092258118')
    )

    assert browser.current_url.strip() == 'https://plus.google.com/105624626079092258118'

def test_github_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to github."""
    print('As a player, navbar footer links to github.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.github_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.github.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://github.com/adventurerscodex')
    )

    assert browser.current_url.strip() == 'https://github.com/adventurerscodex'

def test_rss_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to rss."""
    print('As a player, navbar footer links to rss.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.rss_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.rss.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    # safari does not have an rss reader
    if browser.name != 'safari':

        WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
            url_in_new_tab_matches('https://adventurerscodex.com/feed.xml')
        )

        assert browser.current_url.strip() == 'https://adventurerscodex.com/feed.xml'

def test_tiny_letter_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to tiny letter."""
    print('As a player, navbar footer links to tiny letter.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.tiny_letter_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.tiny_letter.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://tinyletter.com/adventurerscodex')
    )

    assert browser.current_url.strip() == 'https://tinyletter.com/adventurerscodex'

def test_blog_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to tiny letter."""
    print('As a player, navbar footer links to tiny letter.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.blog_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.blog.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://adventurerscodex.com/')
    )

    assert browser.current_url.strip() == 'https://adventurerscodex.com/'

def test_contact_us_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to contact us."""
    print('As a player, navbar footer links to contact us.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.contact_us_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.contact_us.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://adventurerscodex.com/support.html')
    )

    assert browser.current_url.strip() == 'https://adventurerscodex.com/support.html'

def test_patreon_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to patreon."""
    print('As a player, navbar footer links to patreon.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.patreon_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.patreon.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('https://www.patreon.com/bePatron?u=5313385')
    )

    assert browser.current_url.strip() == 'https://www.patreon.com/bePatron?u=5313385'

def test_ogl_link(player_wizard, browser): # noqa
    """As a player, navbar footer links to ogl."""
    print('As a player, navbar footer links to ogl.')
    footer = Footer(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.ID, footer.ogl_id)
        )
    )

    app_window = browser.window_handles[0]

    footer.ogl.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle.title() != app_window.title():
            browser.switch_to_window(handle)
            continue

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        url_in_new_tab_matches('http://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf')
    )

    ogl = 'http://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf'

    assert browser.current_url.strip() == ogl
