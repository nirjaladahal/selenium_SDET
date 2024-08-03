from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://demo-opencart.com/")

# Task 1: Print the number of elements that have the class name "product-thumb"
product_thumbs = driver.find_elements(By.CLASS_NAME, "product-thumb")
print(f"Number of elements with class name 'product-thumb': {len(product_thumbs)}")

# Task 2: Print the names of menu items having class "nav-item"
nav_items = driver.find_elements(By.CLASS_NAME, "nav-item")
print("Menu items with class 'nav-item':")
for item in nav_items:
    print(item.text)

# Task 3: Click on 'Tablets' and assert that the page loaded is tablets
tablets_link = driver.find_element(By.LINK_TEXT, "Tablets")
tablets_link.click()

# Wait for the Tablets page to load
WebDriverWait(driver, 10).until(EC.title_contains("Tablets"))

# Check URL
current_url = driver.current_url
assert "route=product/category&path=57" in current_url, f"URL mismatch: {current_url}"

# Check title
current_title = driver.title
assert "Tablets" in current_title, f"Title mismatch: {current_title}"

# Check left navigation
left_nav = driver.find_element(By.ID, "column-left")
assert left_nav.is_displayed(), "Left navigation is not displayed"

# Check page heading
page_heading = driver.find_element(By.CSS_SELECTOR, "#content h2")
assert "Tablets" in page_heading.text, f"Page heading mismatch: {page_heading.text}"

print("All assertions passed. The Tablets page loaded successfully.")






