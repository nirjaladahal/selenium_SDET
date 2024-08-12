from selenium.webdriver.common.by import By

from pom_saucedemo_AddToCart.pages.bases import BasePage


class ProductPage(BasePage):

    locators = {
        "product_titles": (By.CLASS_NAME, "inventory_item_name"),
        "add_to_cart_buttons": (By.CLASS_NAME, "btn_inventory"),
        "shopping_cart": (By.CLASS_NAME, "shopping_cart_link")
    }

    def add_to_cart(self, product_name):
        product_titles = self.driver.find_elements(*self.locators["product_titles"])
        add_to_cart_buttons = self.driver.find_elements(*self.locators["add_to_cart_buttons"])
        for title, button in zip(product_titles, add_to_cart_buttons):
            if title.text == product_name:
                self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
                break

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
