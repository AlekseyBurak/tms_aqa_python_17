from gribovsky_folder2.lesson23.locators.product_page_locator import BN_ADD_TO_CART, BN_GO_TO_CART, TXT_PRIMARY_PRICE
from gribovsky_folder2.lesson23.pages.base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        self.click(BN_ADD_TO_CART)

    def go_to_cart(self):
        self.click(BN_GO_TO_CART)

    def return_primary_price(self):
        primary_price = self.text(TXT_PRIMARY_PRICE)
        return primary_price
