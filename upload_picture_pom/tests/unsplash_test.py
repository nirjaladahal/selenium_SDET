import os
import base64
import re
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from upload_picture_pom.pages.unsplash_page import UnsplashPage

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

    image_src = unsplash_page.download_first_image()

    # Check if the image source is a base64 string
    if image_src.startswith('data:image'):
        # Extract the base64 data part
        base64_str = re.search(r'base64,(.*)', image_src).group(1)
        image_data = base64.b64decode(base64_str)
        image_path = os.path.join(os.path.expanduser("~"), "Downloads", "beautiful nepal.jpg")

        with open(image_path, 'wb') as file:
            file.write(image_data)

        assert os.path.exists(image_path), "File not downloaded"
        print(f"Image downloaded to {image_path}")
    else:
        print("The image source is not a base64-encoded string.")
