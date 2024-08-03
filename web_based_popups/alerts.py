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

# Trigger the alert using JavaScript
driver.execute_script("alert('This is an alert');")

time.sleep(2)
# Switch to the alert
alert = driver.switch_to.alert

# Print the alert text
print(alert.text)

# Accept the alert
alert.accept()

# Pause to see the result (optional)
time.sleep(2)

