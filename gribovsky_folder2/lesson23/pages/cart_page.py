from gribovsky_folder2.lesson23.locators.cart_page_locator import TXT_PRODUCT_CART_PRICE, TXT_PRODUCT_CART_AMOUNT, \
    BN_SUBMIT_ORDER
from gribovsky_folder2.lesson23.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class CartPage(BasePage):
    def check_url_title(self):
        title = self.driver.title
        url = self.driver.current_url
        assert "Корзина заказов onliner.by" in title, f"This test failed because of \n{title=}"
        assert "https://cart.onliner.by" in url, f"This test failed because of \n{url=}"
        print(title, url, end="\n")

    def check_cart_price(self, primary_price: str):
        cart_price = self.text(TXT_PRODUCT_CART_PRICE)
        assert primary_price in cart_price, f"This test failed because of {cart_price=}!={primary_price=}"

    def check_product_amount(self, amount: int):
        product_cart_amount = self.text(TXT_PRODUCT_CART_PRICE)
        expected_amount = f"{amount} товар"
        assert product_cart_amount in product_cart_amount, f"More than 1 item was added in the cart"

    def check_submit_order_clickable(self):
        self.wait_for_element_to_be_clickable(BN_SUBMIT_ORDER)
