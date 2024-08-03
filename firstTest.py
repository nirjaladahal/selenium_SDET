from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://selenium.dev/")
browser.maximize_window()
title = browser.title
print(title)
assert "Selenium" in title

# browser.find_element()