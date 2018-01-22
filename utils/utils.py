"""Selenium testing utils common to player, dm, and collab tools."""

from collections import namedtuple
import time
from keyword import iskeyword

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # noqa


def select_from_autocomplete(element_,
                             attribute,
                             search_term,
                             browser,
                             arrow_down_count=1):
    """Select an item form jquery autocomplete."""
    element = getattr(element_, attribute)
    element.send_keys(search_term)
    # TODO: remove sleep
    # Investigate this: https://stackoverflow.com/questions/32893984/
    # detecting-when-a-jquery-ui-autocomplete-pops-open-with-selenium
    time.sleep(.3)
    for i in range(arrow_down_count):
        element.send_keys(Keys.DOWN)
    element.send_keys(Keys.TAB)


def named_tuple_from_headers(headers):
    """Return a named tuple class derived from headers."""
    tuple_headers = []
    blank_count = 1
    for raw_header in headers:
        header = ''
        if raw_header.text:
            header_list = raw_header.text.split()
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
        Row = named_tuple_from_headers(headers) # noqa

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

    if values:
        Row = named_tuple_from_headers(headers) # noqa
        output = []
        for tr in rows:
            row = tr.find_elements(By.TAG_NAME, 'td')
            values = [r.text for r in row]
            output.append(Row(*values))

        return output

    output = []
    # remove headers
    rows.pop(0)
    for tr in rows:
        row = tr.find_elements(By.TAG_NAME, 'td')
        output.append(row)

    return output


def set_input_value(label, value, browser):
    """
    Set a value for an input element.

    This assumes a label with text is a sibling to the input.

    :label: label of the span
    :value: value of the input
    :browser: selenium webdriver object
    """
    xpath = "//span[contains(text(), '{}')]/following-sibling::input"
    xpath = xpath.format(label)
    element = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(value)


def clear_input_value(label, browser):
    """
    Clear a value for an input element.

    This assumes a label with text is a sibling to the input.

    :label: label of the span
    :value: value of the input
    :browser: selenium webdriver object
    """
    xpath = "//span[contains(text(), '{}')]/following-sibling::input"
    xpath = xpath.format(label)
    element = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    element.clear()


def click_button(label, browser):
    """
    Click a button via button text.

    :label: label of the button
    :browser: selenium webdriver object
    """
    xpath = "//button[contains(text(), '{}')]".format(label)
    button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()


def click_link(label, browser):
    """
    Click a link by text.

    :label: label of the link
    :browser: selenium webdriver object
    """
    xpath = "//a[contains(text(), '{}')]".format(label)
    button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()


def click_radio(value, browser):
    """
    Select a radio in the style of AC radios.

    TODO: not sure why we have to select twice, but it's the only
    way I could get it to work.  Improvement needed.

    :value: value of the radio value
    :browser: selenium webdriver object
    """
    time.sleep(1)
    browser.execute_script("$('input:radio[value={}]').click();".format(
        value)
    )
    time.sleep(1)
    browser.execute_script("$('input:radio[value={}]').click();".format(
        value)
    )
