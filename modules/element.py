"""Class defintition of Elements."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
    """Class definition of a selenium DOM element."""

    def __init__(self, **kwargs):
        """Populate values."""
        key, value = next(iter(kwargs.items()))
        self.locating_key = LOCATOR_MAP[key]
        self.locating_value = value

    def __get__(self, obj, objtype):
        """Descriptor for retrieving element."""
        element = WebDriverWait(obj.browser, 30).until(
            EC.presence_of_element_located(
                (self.locating_key, self.locating_value)
            )
        )

        return element

    def __set__(self, obj, value):
        """Descriptor for setting a value."""
        element = self.__get__(obj, obj.__class__)
        element.send_keys()

        return element.send_keys(value)
