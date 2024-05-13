import time

from karabin.classwork.classwork_23.locators.item_page_locators import BN_offers, SORT_OFFERS, SORTING_OFFERS, BN_add_to_cart, \
    BN_go_to_cart, TXT_price
from karabin.classwork.classwork_23.pages.main_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class ItemPage(BasePage):

    def offers_of_item(self):
        self.click(BN_offers)

    def sort_offers(self):
        self.click(SORT_OFFERS)

    def sort_by_price(self, ):
        Select(self.driver.find_element(*SORTING_OFFERS)).select_by_visible_text("по возрастанию цены")
        time.sleep(5)

    def add_to_cart(self):
        self.click(BN_add_to_cart)

    def go_to_cart(self):
        self.click(BN_go_to_cart)

    def remember_price(self):
        cost_of_item = self.text(TXT_price)
        return cost_of_item
