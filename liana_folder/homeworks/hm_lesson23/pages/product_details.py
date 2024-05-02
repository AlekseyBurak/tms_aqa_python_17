from liana_folder.lesson23.pages.base_page import BasePage
from liana_folder.homeworks.hm_lesson23.locators.locators import HEADER, BT_ADD_TO_CART, SIDEBAR, BN_GO_TO_CART


class ProductDetails(BasePage):

    @property
    def get_title(self):
        return self.driver.find_element(*HEADER)

    # @property
    # def search_result(self):
    #     return self.driver.find_element(*SEARCH_RESULT)

    # def input_search_field(self, text: str):
    #     self.search_field.send_keys(text)

    def add_product_to_cart(self):
        self.driver.find_element(*BT_ADD_TO_CART).click()

    def go_to_cart(self):
        self.driver.find_element(*BN_GO_TO_CART).click()






