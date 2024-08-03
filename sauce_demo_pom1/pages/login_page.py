from selenium.webdriver.common.by import By
from sauce_demo_pom1.base.bases import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver= driver


    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")


    def enter_username(self, username):
        self.set_text(*self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.set_text(*self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)
