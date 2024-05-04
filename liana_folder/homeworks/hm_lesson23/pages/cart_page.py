from .base_page import BasePage
from ..locators.locators import HEADER_CART


class CartPage(BasePage):

    @property
    def get_title(self):
        self.wait_for(HEADER_CART)
        title = self.driver.find_element(*HEADER_CART)
        return title.text






