import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pom_browserstack.src.pages.homepage import Homepage
from pom_browserstack.src.pages.sing_up_page import SignInPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_browserstack(driver):
    driver.get("https://bstackdemo.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()

    homepage.get_username()
    # driver.quit()
