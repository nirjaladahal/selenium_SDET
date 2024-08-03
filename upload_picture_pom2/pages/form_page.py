from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class FormPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "first_name_field": ('CSS', "input[id='firstName']"),
        "last_name_field": ('CSS', "input[id='lastName']"),
        "upload_picture_button": ('CSS', "input[id='uploadPicture']")
    }

    def enter_first_name(self, first_name):
        self.first_name_field.set_text(first_name)

    def enter_last_name(self, last_name):
        self.last_name_field.set_text(last_name)

    def upload_picture(self, file_path):
        self.upload_picture_button.set_text(file_path)
