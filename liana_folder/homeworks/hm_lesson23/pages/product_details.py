from liana_folder.lesson23.pages.base_page import BasePage
from liana_folder.homeworks.hm_lesson23.locators.locators import HEADER, BT_ADD_TO_CART, SIDEBAR, BN_GO_TO_CART, \
    BN_ACCEPT, BN_GO_TO_CHECKOUT


class ProductDetails(BasePage):

    @property
    def get_title(self):
        return self.driver.find_element(*HEADER)

    @property
    def get_accept_button(self):
        return self.driver.find_element(*BN_ACCEPT)

    @property
    def get_add_to_cart_button(self):
        return self.driver.find_element(*BT_ADD_TO_CART)

    @property
    def get_go_to_cart_button(self):
        self.wait_for(BN_GO_TO_CART)
        return self.driver.find_element(*BN_GO_TO_CART)

    @property
    def get_go_to_checkout_button(self):
        self.wait_for(BN_GO_TO_CHECKOUT)
        return self.driver.find_element(*BN_GO_TO_CHECKOUT)

    def click_accept_button(self):
        return self.get_accept_button.click()

    def add_product_to_cart(self):
        return self.get_add_to_cart_button.click()

    def go_to_cart(self):
        return self.get_go_to_cart_button.click()

    def go_to_checkout(self):
        return self.get_go_to_checkout_button.click()





