import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test100.pages.unsplash_page import UnsplashPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_download_picture(driver):
    driver.get("https://unsplash.com/")

    unsplash_page = UnsplashPage(driver)
    unsplash_page.search("Nepal")

    # Wait for images to load before attempting to download
    try:
        unsplash_page.wait.until(lambda d: unsplash_page.find_element(*unsplash_page.SPECIFIC_IMAGE_DOWNLOAD_BUTTON))
    except Exception as e:
        print(f"Failed to find the specific image download button: {e}")
        return

    # Click the download button of the specified image
    try:
        unsplash_page.click_specific_image_download_button()
    except Exception as e:
        print(f"Failed to click the specific image download button: {e}")