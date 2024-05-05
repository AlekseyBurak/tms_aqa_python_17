import allure

from selevich_tatsiana.HW_23.locators.item_page_locators import BN_GO_TO_CART, BN_ADD_TO_BUCKET, A_ITEM_PRICE
from selevich_tatsiana.HW_23.pages.base_page import BasePage


class ItemPage(BasePage):
    @allure.feature("Bucket")
    @allure.id("1")
    @allure.epic("J-1")
    @allure.story("JQ-1")
    @property
    def item_price(self):
        with allure.step("Find item price"):
            return self.find(A_ITEM_PRICE).text.split()[0]

    @allure.feature("Bucket")
    @allure.title("Add to cart")
    @allure.id("2")
    @allure.epic("J-1")
    @allure.story("JQ-1")
    def add_to_cart(self):
        with allure.step("Add item to cart"):
            self.click(BN_ADD_TO_BUCKET)

    @allure.feature("Bucket")
    @allure.title("Go to cart")
    @allure.id("3")
    @allure.epic("J-1")
    @allure.story("JQ-1")
    def go_to_cart(self):
        with allure.step("Go to cart"):
            self.click(BN_GO_TO_CART)
