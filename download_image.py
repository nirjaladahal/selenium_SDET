import time
import requests
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://pixabay.com/")
time.sleep(5)

img = driver.find_element(By.XPATH, "//div[@class='column--ly2DC']//div[1]//div[1]//a[1]//img[1]")
src = img.get_attribute('src')
print(src)
url = src

response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response