from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

#wait some time here
driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("username").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()


