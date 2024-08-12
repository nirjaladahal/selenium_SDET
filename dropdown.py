import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)
time.sleep(2)

#select the value by visible text
# select.select_by_visible_text("Option 2")
#select the value by index
# select.select_by_index(1)
#select the options by using value
select.select_by_value("2")
