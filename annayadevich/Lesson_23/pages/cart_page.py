from annayadevich.Lesson_23.locators.cart_locators import TXT_CART_PRICE, BN_SUBMIT
from annayadevich.Lesson_23.pages.base_page import BasePage


class CartPage(BasePage):

    def check_cart_price(self, expected_price: str):
        cart_price = self.text(TXT_CART_PRICE)
        assert expected_price in cart_price, f"Prices are not equal, {expected_price=} != {cart_price=}"

    def check_cart_items_amount(self, num_items: int):
        cart_amount = self.text(TXT_CART_PRICE)
        expected_amount = f"{num_items} товар"
        assert expected_amount in cart_amount, f"Amounts are not equal, {expected_amount=} != {cart_amount=}"

    def check_cart_title(self):
        page_title = self.driver.title
        assert page_title == "Корзина заказов onliner.by", (f"Navigation wrong. {page_title=} "
                                                            f"!= 'Корзина заказов onliner.by'")

    def check_submit_possible_is_clickable(self):
        self.wait_for_element_to_be_clickable(BN_SUBMIT)