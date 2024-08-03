from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(login_url)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,  ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()

