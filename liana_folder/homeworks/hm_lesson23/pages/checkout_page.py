from .base_page import BasePage
from ..locators.locators import HEADER_CHECKOUT


class CheckoutDetails(BasePage):

    @property
    def get_title(self):
        self.wait_for(HEADER_CHECKOUT)
        title = self.driver.find_element(*HEADER_CHECKOUT)
        return title.text






