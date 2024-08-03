from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

        self.locators = {
            "username": ("CSS", "#username input"),
            "password": ("CSS", "#password input"),
            "login_btn": ("ID", "login-btn")
        }


    def select_username(self):
        # self.user_name.set_text("demouser")
        username_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username input")))
        username_element.send_keys("demouser\n")

    def select_password(self):
        # self.password.set_text('testingisfun99')
        password_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password input")))
        password_element.send_keys("testingisfun99\n")

    def click_login(self):
        login_btn_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn")))
        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_btn_element)
        # Use JavaScript to click the element
        self.driver.execute_script("arguments[0].click();", login_btn_element)