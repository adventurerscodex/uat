"""Class defintition of Elements."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # noqa


LOCATOR_MAP = {'css': By.CSS_SELECTOR,
               'id_': By.ID,
               'name': By.NAME,
               'xpath': By.XPATH,
               'link_text': By.LINK_TEXT,
               'partial_link_text': By.PARTIAL_LINK_TEXT,
               'tag_name': By.TAG_NAME,
               'class_name': By.CLASS_NAME,
               }


class Component:
    """Class defenition of a component."""

    def __init__(self, browser):
        """Init the browser instance."""
        self.browser = browser


class Element:
    """Class definition of a selenium element object."""

    def __init__(self, **kwargs):
        """Populate values."""
        key, value = next(iter(kwargs.items()))
        self.locating_key = LOCATOR_MAP[key]
        self.locating_value = value

    def __get__(self, obj, objtype):
        """Descriptor for retrieving element."""
        element = WebDriverWait(obj.browser, 10).until(
            EC.visibility_of_element_located(
                (self.locating_key, self.locating_value)
            )
        )

        return element

    def __set__(self, obj, value):
        """Descriptor for setting a value."""
        element = WebDriverWait(obj.browser, 10).until(
            EC.visibility_of_element_located(
                (self.locating_key, self.locating_value)
            )
        )

        # element.send_keys()
        # TODO: this is a workaround for firefox
        try:
            element.clear()
        except:
            pass

        element.send_keys(value)


class Elements:
    """Class definition of multiple selenium element objects."""

    def __init__(self, **kwargs):
        """Populate values."""
        key, value = next(iter(kwargs.items()))
        self.locating_key = LOCATOR_MAP[key]
        self.locating_value = value

    def __get__(self, obj, objtype):
        """Descriptor for retrieving element."""
        elements = WebDriverWait(obj.browser, 5).until(
            EC.presence_of_all_elements_located(
                (self.locating_key, self.locating_value)
            )
        )

        return elements

    def __set__(self, obj, value):
        """Descriptor for setting a value."""
        raise('Setting values not supported for this object.')
