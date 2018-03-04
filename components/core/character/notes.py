"""Notes components."""

from modules.element import Element, Component


class NotesList(Component):
    """Definition of notes list component."""

    add = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[1]/div/div[1]/div/div/span')
    note1_delete = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[1]/div/span')
    note1_select = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[1]')
    note2_delete = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[2]/div/span')
    note2_select = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[1]/div/div[2]/a[2]')


class NotesDetail(Component):
    """Definition of notes detail component."""

    preview_tab = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/markdown-edit-preview/ul/li[1]')
    preview_textarea = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/markdown-edit-preview/div/div[1]/div/div/div')
    no_notes_text = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[2]/div/p')
    add = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[2]/div')
    edit_tab = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/markdown-edit-preview/ul/li[2]')
    edit_textarea = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/markdown-edit-preview/div/div[2]/div/textarea')
    markdown_cheatcheat = Element(xpath='//*[@id="notes"]/div/div/notes/div/div[2]/div/div/div/div/markdown-edit-preview/div/small/a')
