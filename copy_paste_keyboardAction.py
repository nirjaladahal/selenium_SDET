from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navigate to a web page with input fields
driver.get('https://www.w3schools.com/html/html_forms.asp')

# Find the first input field (assume it's for the First Name)
first_name_field = driver.find_element(By.ID,  'fname')
first_name_field.clear()
first_name_field.send_keys('Nirjala Dahal')

actions = ActionChains(driver)

# Select all text in the first input field (Ctrl + A)
actions.click(first_name_field).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

# Copy the selected text (Ctrl + C)
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# Find the second input field
last_name_field = driver.find_element(By.ID, 'lname')
last_name_field.clear()

# Click the second input field to focus
actions.click(last_name_field).perform()

# Paste the copied text into the second input field (Ctrl + V)
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(5)

