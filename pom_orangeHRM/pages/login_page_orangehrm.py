from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

from pom_orangeHRM.utils.utils import Utils


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "username_field": ('NAME', 'username'),
        "password_field": ('NAME', 'password'),
        "login_button": ('CSS', "button[type='submit']")
    }

    # utility_page= Utils()

    def enter_username(self, username):
        self.username_field.set_text(username)

    def enter_password(self, password):
        self.password_field.set_text(password)

    def click_login(self):
        self.login_button.click()
    #
    # def enter_username(self, username):
    #     Utils.enter_text(self.driver,*self.username_field, username )
    #
    # def enter_password(self, password):
    #     Utils.enter_text( password)
    #
    # def click_login(self):
    #     Utils.click_element()

