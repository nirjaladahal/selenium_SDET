from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://trytestingthis.netlify.app/")

# driver.save_screenshot(r"E:\User\Pictures\screenshot\homepage.png")

driver.get_screenshot_as_file(r"E:\User\Pictures\screenshot\feature1.png")
