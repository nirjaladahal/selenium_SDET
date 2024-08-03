from selenium.webdriver.common.by import By
from test100.base.bases import BasePage


class UnsplashPage(BasePage):
    SEARCH_INPUT = (By.NAME, 'searchKeyword')
    SPECIFIC_IMAGE_DOWNLOAD_BUTTON = (By.XPATH, "//figure[21]//div[1]//div[1]//div[4]//div[2]//a[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, keyword):
        self.set_text(*self.SEARCH_INPUT, keyword)
        self.find_element(*self.SEARCH_INPUT).send_keys("\n")

    def click_specific_image_download_button(self):
        try:
            download_button = self.find_element(*self.SPECIFIC_IMAGE_DOWNLOAD_BUTTON)
            download_button.click()
        except Exception as e:
            print(f"Failed to click the specific image download button: {e}")