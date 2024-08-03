from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
                "sign_in": ("ID", "signin"),
                "user_name": ("CSS", ".username")
    }

    def click_sign_in(self):
        sign_in_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "signin")))
        sign_in_element.click()

    def get_username(self):
        username_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".username")))
        retrieved_username = username_element.text
        # assert retrieved_username == "demouser"
