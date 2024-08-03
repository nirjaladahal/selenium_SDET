import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")

actions = ActionChains(driver)

hover_element = driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
time.sleep(5)
actions.move_to_element(hover_element).perform()
driver.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(5)