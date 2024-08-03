from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com/")

# Wait until the Flights tab is clickable
flights_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Flights']")))
flights_tab.click()
time.sleep(5)

# Locate and interact with the input field
input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".uitk-fake-input.uitk-form-field-trigger")))
input_field.click()
input_field.send_keys("NYC")
print("Text 'NYC' should be typed into the input field.")

going_to = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button[aria-label='Going to']"))).click()
going_to.send_keys("KTM")
