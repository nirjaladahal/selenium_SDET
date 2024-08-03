from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.selenium.dev/documentation/webdriver/interactions/alerts/')

# Trigger the confirmation dialog using JavaScript
driver.execute_script("confirm('Do you confirm this?');")

# Switch to the confirmation dialog
confirmation = driver.switch_to.alert

# Print the confirmation dialog text
print(confirmation.text)

# Accept the confirmation dialog
confirmation.accept()

# To dismiss the confirmation dialog
# confirmation.dismiss()
time.sleep(2)

