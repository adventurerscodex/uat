"""Selenium testing utils common to player, dm, and collab tools."""

from collections import namedtuple
import time
from keyword import iskeyword

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # noqa


def select_from_autocomplete(element_,
                             attribute,
                             browser,
                             arrow_down_count=1,
                             search_term=None,
                             has_search_term=True):
    """Select an item form jquery autocomplete."""
    element = getattr(element_, attribute)

    if search_term:
        element.send_keys(search_term)
    # TODO: remove sleep
    # Investigate this: https://stackoverflow.com/questions/32893984/
    # detecting-when-a-jquery-ui-autocomplete-pops-open-with-selenium
    # TODO: this function is only working when the search_term is ''
    time.sleep(.3)
    for i in range(arrow_down_count):
        element.send_keys(Keys.DOWN)
    element.send_keys(Keys.RETURN)


def _named_tuple_from_headers(headers):
    """Return a named tuple class derived from headers."""
    tuple_headers = []
    blank_count = 1
    for raw_header in headers:
        header = ''
        header_stripped = raw_header.text.strip()
        if header_stripped:
            header_list = header_stripped.split()
            header_list = [word.lower() for word in header_list]
            header = '_'.join(header_list)
            if iskeyword(header):
                header = '{}_'.format(header)
        else:
            header = 'blank{}'.format(blank_count)
            blank_count += 1

        tuple_headers.append(header)

    return namedtuple('Row', tuple_headers)


def get_table_row(element_,
                  attribute,
                  row_number=1,
                  values=True):
    """Return row by row number.

    If values, return named tuple, else return
    raw selenium object.
    """
    table = getattr(element_, attribute)
    headers = table.find_elements(By.TAG_NAME, 'th')

    rows = table.find_elements(By.TAG_NAME, 'tr')
    row = rows[row_number].find_elements(By.TAG_NAME, 'td')

    if values:
        values = [r.text for r in row]
        Row = _named_tuple_from_headers(headers) # noqa

        return Row(*values)

    return row


def get_table_rows(element_,
                   attribute,
                   values=True):
    """Return table rows.

    If values, return named tuple, else return
    raw selenium objects.
    """
    table = getattr(element_, attribute)
    headers = table.find_elements(By.TAG_NAME, 'th')

    rows = table.find_elements(By.TAG_NAME, 'tr')

    # remove headers
    rows.pop(0)

    if values:
        Row = _named_tuple_from_headers(headers) # noqa
        output = []
        for tr in rows:
            row = tr.find_elements(By.TAG_NAME, 'td')
            values = [r.text for r in row]
            output.append(Row(*values))

        return output

    output = []

    for tr in rows:
        row = tr.find_elements(By.TAG_NAME, 'td')
        output.append(row)

    return output
