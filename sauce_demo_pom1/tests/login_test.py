import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sauce_demo_pom1.pages.login_page import LoginPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_invalid_username(driver):
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.enter_username("invalid_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message()

def test_invalid_password(driver):
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message()

def test_empty_username(driver):
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.enter_username("")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "Epic sadface: Username is required" in login_page.get_error_message()

def test_empty_password(driver):
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("")
    login_page.click_login()

    assert "Epic sadface: Password is required" in login_page.get_error_message()
