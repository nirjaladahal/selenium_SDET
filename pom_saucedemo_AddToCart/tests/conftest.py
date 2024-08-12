import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def test_setUp():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver  # keyword to implement the teardown

