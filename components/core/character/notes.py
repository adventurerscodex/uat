"""Notes components."""

from modules.element import Element, Component


class NotesList(Component):
    """Definition of notes list component."""

    add_xpath = '//*[@id="notes"]/div/div/notes/div/div[1]/div/div[1]/div/div/span'
    note1_delete_xpath = '//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[1]/div/span'
    note1_select_xpath = '//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[1]'
    note2_delete_xpath = '//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[2]/div/span'
    note2_select_xpath = '//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[2]'

    add = Element(xpath=add_xpath)
    note1_delete = Element(xpath=note1_delete_xpath)
    note1_select = Element(xpath=note1_select_xpath)
    note2_delete = Element(xpath=note2_delete_xpath)
    note2_select = Element(xpath=note2_select_xpath)


class NotesDetail(Component):
    """Definition of notes detail component."""

    preview_tab_xpath = ('//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/'
                         'markdown-edit-preview/ul/li[1]')
    preview_textarea_xpath = ('//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/'
                              'markdown-edit-preview/div/div[1]/div/div/div')
    no_notes_text_xpath = '//*[@id="notes"]/div/div/notes/div/div[2]/div/p'
    add_xpath = '//*[@id="notes"]/div/div/notes/div/div[2]/div'
    edit_tab_xpath = ('//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/'
                      'markdown-edit-preview/ul/li[2]')
    edit_textarea_xpath = ('//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/'
                           'markdown-edit-preview/div/div[2]/div/textarea')
    markdown_cheatcheat_xpath = ('//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/'
                                 'markdown-edit-preview/div/small/a')

    preview_tab = Element(xpath=preview_tab_xpath)
    preview_textarea = Element(xpath=preview_textarea_xpath)
    no_notes_text = Element(xpath=no_notes_text_xpath)
    add = Element(xpath=add_xpath)
    edit_tab = Element(xpath=edit_tab_xpath)
    edit_textarea = Element(xpath=edit_textarea_xpath)
    markdown_cheatcheat = Element(xpath=markdown_cheatcheat_xpath)
