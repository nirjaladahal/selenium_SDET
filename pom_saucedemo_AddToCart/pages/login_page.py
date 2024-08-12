from selenium.webdriver.common.by import By

from pom_saucedemo_AddToCart.pages.bases import BasePage


class LoginPage(BasePage):
    locators = {
        "username": (By.ID, "user-name"),
        "password": (By.ID, "password"),
        "login_button": (By.ID, "login-button")
    }

    def login(self, username, password):
        self.set_text(self.locators["username"], username)
        self.set_text(self.locators["password"], password)
        self.click(self.locators["login_button"])
