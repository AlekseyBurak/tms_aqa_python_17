from selevich_tatsiana.HW_23.locators.cart_page_locators import TXT_CART_PRICE, BN_SUBMIT, IN_ITEM_COUNT
from selevich_tatsiana.HW_23.pages.base_page import BasePage
import allure


class CartPage(BasePage):
    def check_cart_price(self, expected_price: str):
        with allure.step("Check cart price"):
            cart_price = self.text(TXT_CART_PRICE).split()[0]

            assert expected_price == cart_price, f"Prices are not equal, {expected_price=} != {cart_price=}"

    def check_cart_items_amount(self, expected_amount: int):
        with allure.step("Check cart items amount"):
            cart_amount = int(self.find(IN_ITEM_COUNT).get_attribute('value'))

            assert expected_amount == cart_amount, f"Amounts are not equal, {expected_amount} != {cart_amount}"

    def check_cart_title(self):
        with allure.step("Check cart title"):
            page_title = self.driver.title

            assert page_title == "Корзина заказов onliner.by", f"Navigation wrong. {page_title=} != 'Корзина заказов onliner.by'"

    def check_submit_is_clickable(self):
        with allure.step("Check submit button is clickable"):
            self.wait_for_element_to_be_clickable(BN_SUBMIT)
