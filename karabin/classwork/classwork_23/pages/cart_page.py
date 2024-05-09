import pytest

from karabin.classwork.classwork_23.locators.cart_page_locators import TXT_TITLE, TXT_AMOUNT_OF_ITEMS, \
    TXT_EXPECTED_PRICE
from karabin.classwork.classwork_23.pages.base_page import BasePage


class CartPage(BasePage):
    def check_title(self):
        cart = self.text(TXT_TITLE)
        assert "Корзина" in cart

    # def amount_of_items(self, amount: int):
    #     amount_of = self.driver.find_element(TXT_AMOUNT_OF_ITEMS)
    #     expected_number_of_amount = f"{amount} товар"
    #     assert expected_number_of_amount in amount_of, f"Amounts are not equal, {expected_number_of_amount} != {amount_of}"

    def check_cart(self, expected_price: str):
        item_price = self.text(TXT_EXPECTED_PRICE)
        assert expected_price in item_price, f"Prices are not equal, {expected_price=} != {item_price=}"
