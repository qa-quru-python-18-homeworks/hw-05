import pytest
from selene import browser


@pytest.fixture(scope="session")
def maximize_browser():
    browser.driver.maximize_window()
    yield
    browser.quit()
