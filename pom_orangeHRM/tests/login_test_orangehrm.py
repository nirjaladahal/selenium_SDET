import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pom_orangeHRM.pages.login_page_orangehrm import LoginPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(driver)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    # assert "dashboard" in driver.current_url
