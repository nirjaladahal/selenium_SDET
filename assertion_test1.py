import unittest
from selenium import webdriver

class TestGoogleHomePage(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com")
        driver.maximize_window()

        title = driver.title
        self.assertTrue(title == "Google")

        driver.quit()

if __name__ == "__main__":
    unittest.main()

