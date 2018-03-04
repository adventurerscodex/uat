"""UAT test notes for Adventurer's Codex player tools notes module."""
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character.notes import NotesList, NotesDetail
from components.core.character.tabs import Tabs
from utils import utils as ut
from expected_conditions.conditions import url_in_new_tab_matches


def test_add_note(player_wizard, browser): # noqa
    """As a player, I can add a note."""
    print('As a player, I can add a note.')
    notes_list = NotesList(browser)
    notes_detail = NotesDetail(browser)

    tabs = Tabs(browser)
    tabs.notes.click()

    notes_list.add.click()
    notes_detail.edit_textarea = 'Test Note 1'

    assert notes_detail.edit_textarea.get_attribute('value') == 'Test Note 1'


def test_delete_note(player_wizard, browser): # noqa
    """As a player, I can delete a note."""
    print('As a player, I can delete a note.')
    notes_list = NotesList(browser)
    notes_detail = NotesDetail(browser)

    tabs = Tabs(browser)
    tabs.notes.click()

    notes_list.add.click()
    notes_detail.edit_textarea = 'Test Note 1'
    notes_list.note1_delete.click()

    assert notes_detail.no_notes_text.text == 'Add a note to begin documenting your adventure'


def test_edit_note(player_wizard, browser): # noqa
    """As a player, I can edit a note."""
    print('As a player, I can edit a note.')
    notes_list = NotesList(browser)
    notes_detail = NotesDetail(browser)

    tabs = Tabs(browser)
    tabs.notes.click()

    notes_list.add.click()
    notes_detail.edit_textarea = 'Test Note 1'
    notes_list.add.click()
    notes_list.note1_select.click()
    notes_detail.edit_tab.click()
    notes_detail.edit_textarea = 'Test Edit Note 1'

    assert notes_detail.edit_textarea.get_attribute('value') == 'Test Edit Note 1'


def test_notes_persist_note(player_wizard, browser): # noqa
    """As a player, notes persist after a browser refresh."""
    print('As a player, notes persist after a browser refresh.')
    notes_list = NotesList(browser)
    notes_detail = NotesDetail(browser)

    tabs = Tabs(browser)
    tabs.notes.click()

    notes_list.add.click()
    notes_detail.edit_textarea = 'Test Note 1'

    browser.refresh()

    assert notes_detail.edit_textarea.get_attribute('value') == 'Test Note 1'


def test_note_preview(player_wizard, browser): # noqa
    """As a player, I can preview a note in the preview tab."""
    print('As a player, I can preview a note in the prevew tab.')
    notes_list = NotesList(browser)
    notes_detail = NotesDetail(browser)

    tabs = Tabs(browser)
    tabs.notes.click()

    notes_list.add.click()
    notes_detail.edit_textarea = '## Test Note 1'
    notes_detail.preview_tab.click()

    notes_detail.preview_textarea.find_element_by_tag_name('h2')

    assert notes_detail.preview_textarea.find_element_by_tag_name('h2').text


def test_markdown_cheatsheet_link(player_wizard, browser): # noqa
    """As a player, I can click on the link to the markdown guide."""
    print('As a player, I can click on the link to the markdown guide.')
    notes_list = NotesList(browser)
    notes_detail = NotesDetail(browser)

    tabs = Tabs(browser)
    tabs.notes.click()

    notes_list.add.click()
    notes_detail.edit_textarea = 'Test Note 1'

    notes_detail.markdown_cheatcheat.click()
    WebDriverWait(browser, 20).until(EC.number_of_windows_to_be(2))
    browser.switch_to.window(browser.window_handles[1])
    WebDriverWait(browser, 20).until(url_in_new_tab_matches('https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet'))
    assert browser.current_url == 'https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet'


def test_add_note_by_detail_div(player_wizard, browser): # noqa
    """As a player, if no notes are visible, I can add a note by clicking on the detail div."""
    print('As a player, if no notes are visible, I can add a note by clicking on the detail div.')
    notes_detail = NotesDetail(browser)

    tabs = Tabs(browser)
    tabs.notes.click()

    notes_detail.add.click()
    notes_detail.edit_textarea = 'Test Note 1'

    assert notes_detail.edit_textarea.get_attribute('value') == 'Test Note 1'
