from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.google.com')

# Locate the element where you want to perform the keyboard action
search_box = driver.find_element(By.NAME, 'q')

actions = ActionChains(driver)

# Perform keyboard actions
actions.click(search_box)  # Click on the element to focus
actions.send_keys('Shah Rukh Khan')
actions.send_keys(Keys.RETURN)  # Press Enter key
actions.perform()  # Perform the action
