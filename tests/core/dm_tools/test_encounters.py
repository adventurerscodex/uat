"""UAT test file for Adventurer's Codex dm tools encounters module."""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.dm.points_of_interest import PointOfInterestAddModal
from components.core.dm.points_of_interest import PointOfInterestEditModal
from components.core.dm.points_of_interest import PointOfInterestModalTabs
from components.core.dm.points_of_interest import PointOfInterestTable
from components.core.dm.read_aloud_text import ReadAloudTextAddModal
from components.core.dm.read_aloud_text import ReadAloudTextEditModal
from components.core.dm.read_aloud_text import ReadAloudTextModalTabs
from components.core.dm.read_aloud_text import ReadAloudTextTable
from factories.core.dm.pointofinterest import PointOfInterestFactory
from factories.core.dm.read_aloud_text import ReadAloudTextFactory


def test_add_read_aloud_text(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can add read aloud text to an encounter and the data persists."""
    print('As a dm, I can add read aloud text to an encounter and the data persists')

    read_aloud_text = ReadAloudTextAddModal(browser)
    read_aloud_table = ReadAloudTextTable(browser)

    read_aloud_text.add_plus_icon.click()
    stub = ReadAloudTextFactory.stub()

    read_aloud_text.name = stub.name
    read_aloud_text.description = stub.description
    read_aloud_text.add.click()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )

    before_refresh_name = read_aloud_table.name.text.strip()
    before_refresh_description = read_aloud_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )

    after_refresh_name = read_aloud_table.name.text.strip()
    after_refresh_description = read_aloud_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description


def test_edit_read_aloud_text(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can add, edit and delete a read aloud text in an encounter and the data persists.""" # noqa
    print('As a dm I can edit and delete a read aloud text in an encounter and the data persists ') # noqa

    read_aloud_text = ReadAloudTextAddModal(browser)
    read_aloud_table = ReadAloudTextTable(browser)

    read_aloud_text.add_plus_icon.click()
    stub = ReadAloudTextFactory.stub()

    read_aloud_text.name = stub.name
    read_aloud_text.description = stub.description
    read_aloud_text.add.click()

    read_aloud_edit = ReadAloudTextEditModal(browser)
    read_aloud_tabs = ReadAloudTextModalTabs(browser)

    read_aloud_table.name.click()
    edit = browser.find_elements_by_xpath(read_aloud_tabs.edit_xpath)[1]
    time.sleep(1)
    edit.click()

    read_aloud_edit.name = stub.name
    read_aloud_edit.description = stub.description
    read_aloud_edit.done.click()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )

    before_refresh_name = read_aloud_table.name.text.strip()
    before_refresh_description = read_aloud_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )

    after_refresh_name = read_aloud_table.name.text.strip()
    after_refresh_description = read_aloud_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description

    read_aloud_text.remove.click()

    assert read_aloud_text.add_new_point.text.strip() == 'Add new text for your players.'


def test_add_point_of_interest(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can add read aloud text to an encounter and the data persists."""
    print('As a dm, I can add read aloud text to an encounter and the data persists')

    point_of_interest_modal = PointOfInterestAddModal(browser)
    point_of_interest_table = PointOfInterestTable(browser)

    point_of_interest_modal.add_plus_icon.click()
    stub = PointOfInterestFactory.stub()

    point_of_interest_modal.name = stub.name
    point_of_interest_modal.description = stub.description
    point_of_interest_modal.add.click()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )

    before_refresh_name = point_of_interest_table.name.text.strip()
    before_refresh_description = point_of_interest_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )

    after_refresh_name = point_of_interest_table.name.text.strip()
    after_refresh_description = point_of_interest_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description


def test_edit_point_of_interest(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can edit and delete a Point of interest to an encounter and the data persists."""
    print('As a dm, I can edit and delete a Point of interest to an encounter and the data persists') # noqa

    point_of_interest_modal = PointOfInterestAddModal(browser)
    point_of_interest_table = PointOfInterestTable(browser)

    point_of_interest_modal.add_plus_icon.click()
    stub = PointOfInterestFactory.stub()

    point_of_interest_modal.name = stub.name
    point_of_interest_modal.description = stub.description
    point_of_interest_modal.add.click()

    point_of_interest_edit = PointOfInterestEditModal(browser)
    point_of_interest_tabs = PointOfInterestModalTabs(browser)

    point_of_interest_table.name.click()
    edit = browser.find_element_by_xpath(point_of_interest_tabs.edit_xpath)
    time.sleep(1)
    edit.click()

    point_of_interest_edit.name = stub.name
    point_of_interest_edit.description = stub.description
    point_of_interest_edit.done.click()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )

    before_refresh_name = point_of_interest_table.name.text.strip()
    before_refresh_description = point_of_interest_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )

    after_refresh_name = point_of_interest_table.name.text.strip()
    after_refresh_description = point_of_interest_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description

    point_of_interest_modal.remove.click()

    assert point_of_interest_modal.add_new_point.text.strip() == 'Add a new Point of Interest'
