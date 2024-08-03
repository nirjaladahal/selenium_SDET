from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:

    @staticmethod
    def enter_text(driver, by_locator,text):
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    @staticmethod
    def click_element(driver, by, locator):
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, locator)))
        element.click()

    @staticmethod
    def get_element_text(driver, by, locator):
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, locator)))
        return element.text