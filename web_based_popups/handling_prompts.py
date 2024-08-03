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

# Trigger the prompt using JavaScript (for demo purposes)
driver.execute_script("prompt('Enter your name:');")

# Switch to the prompt
prompt = driver.switch_to.alert
print(prompt.text)

time.sleep(3)
# Enter text into the prompt
prompt.send_keys('hi Nirjala')

prompt.accept()
time.sleep(5)

