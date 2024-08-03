import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from upload_picture_pom2.pages.form_page import FormPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_upload_picture(driver):
    driver.get("https://demoqa.com/automation-practice-form")

    form_page = FormPage(driver)

    form_page.enter_first_name("Baibhav")
    form_page.enter_last_name("Dahal")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    form_page.upload_picture(r"E:\Desktop\images\ambika.jpg")
    # Add assertions here if necessary
