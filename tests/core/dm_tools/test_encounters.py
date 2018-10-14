"""UAT test file for Adventurer's Codex dm tools encounters module."""
import time

from conftest import DEFAULT_WAIT_TIME
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.dm.map_or_image import MapOrImageAddModal
from components.core.dm.map_or_image import MapOrImageEditModal
from components.core.dm.map_or_image import MapOrImageModalTabs
from components.core.dm.map_or_image import MapOrImageTable
from components.core.dm.points_of_interest import PointOfInterestAddModal
from components.core.dm.points_of_interest import PointOfInterestEditModal
from components.core.dm.points_of_interest import PointOfInterestModalTabs
from components.core.dm.points_of_interest import PointOfInterestTable
from components.core.dm.read_aloud_text import ReadAloudTextAddModal
from components.core.dm.read_aloud_text import ReadAloudTextEditModal
from components.core.dm.read_aloud_text import ReadAloudTextModalTabs
from components.core.dm.read_aloud_text import ReadAloudTextTable
from expected_conditions.general import modal_finished_closing, table_has_data, table_is_empty
from factories.core.dm.map_image import MapOrImageFactory
from factories.core.dm.pointofinterest import PointOfInterestFactory
from factories.core.dm.read_aloud_text import ReadAloudTextFactory


def test_add_read_aloud_text(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can add read aloud text to an encounter and the data persists."""
    print('As a dm, I can add read aloud text to an encounter and the data persists')

    read_aloud_text = ReadAloudTextAddModal(browser)
    read_aloud_table = ReadAloudTextTable(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_text.add_plus_icon_xpath)
        )
    )

    read_aloud_text.add_plus_icon.click()
    stub = ReadAloudTextFactory.stub()

    read_aloud_text.name = stub.name
    read_aloud_text.description = stub.description
    read_aloud_text.add.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_has_data(read_aloud_table)
    )

    before_refresh_name = read_aloud_table.name.text.strip()
    before_refresh_description = read_aloud_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
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

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_text.add_plus_icon_xpath)
        )
    )

    read_aloud_text.add_plus_icon.click()
    stub = ReadAloudTextFactory.stub()

    read_aloud_text.name = stub.name
    read_aloud_text.description = stub.description
    read_aloud_text.add.click()

    read_aloud_edit = ReadAloudTextEditModal(browser)
    read_aloud_tabs = ReadAloudTextModalTabs(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )
    time.sleep(1)

    read_aloud_table.name.click()
    edit = browser.find_elements_by_xpath(read_aloud_tabs.edit_xpath)[1]
    time.sleep(2)

    edit.click()
    edit.click()

    read_aloud_edit.name = stub.name
    read_aloud_edit.description = stub.description
    read_aloud_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )

    before_refresh_name = read_aloud_table.name.text.strip()
    before_refresh_description = read_aloud_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, read_aloud_table.name_xpath)
        )
    )

    after_refresh_name = read_aloud_table.name.text.strip()
    after_refresh_description = read_aloud_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description

    read_aloud_text.remove.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_is_empty(read_aloud_table)
    )

    assert read_aloud_text.add_new_point.text.strip() == 'Add new text for your players.'


def test_add_point_of_interest(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can add read aloud text to an encounter and the data persists."""
    print('As a dm, I can add read aloud text to an encounter and the data persists')

    point_of_interest_modal = PointOfInterestAddModal(browser)
    point_of_interest_table = PointOfInterestTable(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_modal.add_plus_icon_xpath)
        )
    )

    point_of_interest_modal.add_plus_icon.click()
    stub = PointOfInterestFactory.stub()

    point_of_interest_modal.name = stub.name
    point_of_interest_modal.description = stub.description
    point_of_interest_modal.add.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_has_data(point_of_interest_table)
    )

    before_refresh_name = point_of_interest_table.name.text.strip()
    before_refresh_description = point_of_interest_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
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

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_modal.add_plus_icon_xpath)
        )
    )

    point_of_interest_modal.add_plus_icon.click()
    stub = PointOfInterestFactory.stub()

    point_of_interest_modal.name = stub.name
    point_of_interest_modal.description = stub.description
    point_of_interest_modal.add.click()

    point_of_interest_edit = PointOfInterestEditModal(browser)
    point_of_interest_tabs = PointOfInterestModalTabs(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )
    time.sleep(1)
    point_of_interest_table.name.click()
    edit = browser.find_element_by_xpath(point_of_interest_tabs.edit_xpath)
    time.sleep(1)
    edit.click()

    point_of_interest_edit.name = stub.name
    point_of_interest_edit.description = stub.description
    point_of_interest_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )

    before_refresh_name = point_of_interest_table.name.text.strip()
    before_refresh_description = point_of_interest_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, point_of_interest_table.name_xpath)
        )
    )

    after_refresh_name = point_of_interest_table.name.text.strip()
    after_refresh_description = point_of_interest_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description

    point_of_interest_modal.remove.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_is_empty(point_of_interest_table)
    )

    assert point_of_interest_modal.add_new_point.text.strip() == 'Add a new Point of Interest'


def test_add_map_or_image(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can add a map or image to an encounter and the data persists."""
    print('As a dm, I can add a map or image to an encounter and the data persists') # noqa
    map_or_image_modal = MapOrImageAddModal(browser)
    map_or_image_table = MapOrImageTable(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, map_or_image_modal.add_plus_icon_xpath)
        )
    )

    map_or_image_modal.add_plus_icon.click()
    stub = MapOrImageFactory.stub()

    map_or_image_modal.name = stub.name
    map_or_image_modal.link = stub.image_link
    map_or_image_modal.description = stub.description
    map_or_image_modal.add.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, map_or_image_table.name_xpath)
        )
    )

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_has_data(map_or_image_table)
    )

    before_refresh_name = map_or_image_table.name.text.strip()
    before_refresh_description = map_or_image_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, map_or_image_table.name_xpath)
        )
    )

    after_refresh_name = map_or_image_table.name.text.strip()
    after_refresh_description = map_or_image_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description


def test_edit_map_or_image(dm_wizard, encounter_all_sections, browser):
    """As a dm, I can edit and delete a map or image to an encounter and the data persists."""
    print('As a dm, I can edit and delete a map or image to an encounter and the data persists') # noqa
    map_or_image_modal = MapOrImageAddModal(browser)
    map_or_image_table = MapOrImageTable(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, map_or_image_modal.add_plus_icon_xpath)
        )
    )

    map_or_image_modal.add_plus_icon.click()
    stub = MapOrImageFactory.stub()

    map_or_image_modal.name = stub.name
    map_or_image_modal.link = stub.image_link
    map_or_image_modal.description = stub.description
    map_or_image_modal.add.click()

    map_or_image_edit = MapOrImageEditModal(browser)
    map_or_image_tabs = MapOrImageModalTabs(browser)

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(modal_finished_closing())

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, map_or_image_table.name_xpath)
        )
    )

    time.sleep(1)
    map_or_image_table.name.click()
    edit = browser.find_elements_by_xpath(map_or_image_tabs.edit_xpath)[1]
    time.sleep(1)
    edit.click()
    edit.click()

    map_or_image_edit.name = stub.name
    map_or_image_edit.link = stub.image_link
    map_or_image_edit.description = stub.description
    map_or_image_edit.done.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, map_or_image_table.name_xpath)
        )
    )

    before_refresh_name = map_or_image_table.name.text.strip()
    before_refresh_description = map_or_image_table.description.text.strip()

    browser.refresh()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, map_or_image_table.name_xpath)
        )
    )

    after_refresh_name = map_or_image_table.name.text.strip()
    after_refresh_description = map_or_image_table.description.text.strip()

    assert before_refresh_name == after_refresh_name
    assert before_refresh_description == after_refresh_description

    map_or_image_modal.remove.click()

    WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
        table_is_empty(map_or_image_table)
    )

    assert map_or_image_modal.add_new_point.text.strip() == 'Add a new Map or Image.'
