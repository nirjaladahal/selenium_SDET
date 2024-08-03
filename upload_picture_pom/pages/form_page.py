
from selenium.webdriver.common.by import By

from upload_picture_pom.base.base_page import BasePage


class FormPage(BasePage):
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='lastName']")
    UPLOAD_PICTURE_BUTTON = (By.CSS_SELECTOR, "input[id='uploadPicture']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.set_text(*self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name):
        self.set_text(*self.LAST_NAME_FIELD, last_name)

    def upload_picture(self, file_path):
        self.upload_file(*self.UPLOAD_PICTURE_BUTTON, file_path)
