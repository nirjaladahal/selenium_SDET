import pytest
from selenium.webdriver.common.by import By

from pom_saucedemo_AddToCart.pages.login_page import LoginPage
from pom_saucedemo_AddToCart.pages.product_page import ProductPage


def test_add_to_cart(test_setUp):
    driver = test_setUp
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)

    # Login
    login_page.login("standard_user", "secret_sauce")

    # Add a product to the cart
    product_name = "Sauce Labs Backpack"
    product_page.add_to_cart(product_name)

    # Verify the product is added to the cart
    product_page.go_to_cart()
    cart_items = [item.text for item in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert product_name in cart_items, f"{product_name} not found in the cart"
