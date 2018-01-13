"""Test fixtures for selenium UAT for adventurer's codex."""

import pytest

from selenium import webdriver


def pytest_addoption(parser):
    """Command line parameters."""
    parser.addoption('--web_driver', action='store', default='chrome')
    parser.addoption(
        '--url',
        action='store',
        default='https://nightly.adventurerscodex.com'
    )


@pytest.fixture
def web_driver(request):
    """Return command line argument."""
    return request.config.getoption('--web_driver')


@pytest.fixture
def url(request):
    """Return command line argument."""
    return request.config.getoption('--url')


@pytest.fixture(scope='function')
def browser(request, web_driver, url):
    """Return selenium webdriver chrome instance."""
    driver = None
    if web_driver.lower() == 'chrome':
        driver = webdriver.Chrome()

    elif web_driver.lower() == 'firefox':
        driver = webdriver.Firefox()

    driver.get(url)

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)

    return driver
