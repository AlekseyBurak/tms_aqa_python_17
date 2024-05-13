from typing import Tuple

from novik_folder.homework23.locators.locators import IN_SEARCH_FIELD, IFRAME, LI_SEARCH_RESULT, LI_OVERFLOW, BN_ADD, \
    BN_NAV_TO, TXT_ITEM_IN_CART
from novik_folder.homework23.pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def search_field(self):
        return self.driver.find_element(*IN_SEARCH_FIELD)

    def input_into_search_field(self, text: str):
        self.search_field.send_keys(text)

    def find_button_add_click(self):
        return self.driver.find_element(*BN_ADD).click()

    def navigate_button_and_click(self):
        return self.driver.find_element(*BN_NAV_TO).click()


    def chose_from_iframe_by_index(self):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        self.wait_for(LI_SEARCH_RESULT)
        self.click(LI_SEARCH_RESULT)
        self.driver.switch_to.default_content()


    def wait_for_overflow(self):
        self.wait_for(LI_OVERFLOW)

    def wait_for_items_in_cart(self):
        self.wait_for(TXT_ITEM_IN_CART)

    def find_item_cart_text(self):
        return self.driver.find_element(*TXT_ITEM_IN_CART).text

    def find_element_text(self):
        return self.text(TXT_ITEM_IN_CART)





