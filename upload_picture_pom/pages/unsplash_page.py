from selenium.webdriver.common.by import By
from upload_picture_pom.base.base_page import BasePage
import base64
import re

class UnsplashPage(BasePage):
    SEARCH_INPUT = (By.NAME, 'searchKeyword')
    FIRST_IMAGE = (By.CSS_SELECTOR, 'figure div a img')

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, keyword):
        self.set_text(*self.SEARCH_INPUT, keyword)
        self.find_element(*self.SEARCH_INPUT).send_keys("\n")

    def download_first_image(self):
        first_image = self.find_element(*self.FIRST_IMAGE)
        image_src = first_image.get_attribute('src')
        return image_src
