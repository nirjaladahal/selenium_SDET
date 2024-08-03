import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

# parametarization with pytest
@pytest.mark.parametrize("username, password", [
    ("test", "test"),
    ("user2", "pass2"),
    ("user3", "pass3"),
])

def test_login(driver, username, password):
    driver.get("https://trytestingthis.netlify.app/")
    username_field = driver.find_element(By.ID, "uname")
    password_field = driver.find_element(By.ID, "pwd")
    submit_button = driver.find_element(By.XPATH, "//input[@value='Login']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    assert "Successful" in driver.page_source