from typing import Tuple

import allure

from Yauheni_Drazdou.homework_lesson_23.pages.base_page import BasePage
from selenium.webdriver.common.by import By

BN_ADD_TO_CART = By.PARTIAL_LINK_TEXT, 'В корзину'
BN_GO_TO_CART = By.XPATH, "//*[contains(text(), 'Перейти в корзину')]"

TX_PRICE = By.XPATH, "//div[@class='product-aside__offers']//span"
TX_TITLE = By.XPATH, "//*[@class='catalog-masthead__title js-nav-header']"

class ItemPage(BasePage):

    @allure.title("Adding product to the cart")
    @allure.severity("Major")
    def add_to_cart(self):
        add_to = self.driver.find_element(*BN_ADD_TO_CART)
        add_to.click()
        return add_to

    @allure.title("Going to the cart")
    def go_to_cart(self):
        go_to_cart = self.driver.find_element(*BN_GO_TO_CART)
        go_to_cart.click()
        return go_to_cart

    @allure.title("Getting product price")
    def get_product_price(self):
        product_price_element = self.driver.find_element(*TX_PRICE)
        return product_price_element.text

    def get_product_title(self):
        product_title = self.driver.find_element(*TX_TITLE)
        return product_title.text

    def close_tab(self):
        return self.driver.close()

