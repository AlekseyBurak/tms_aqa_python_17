from i_turbal_folder.hw23.locators.item_and_order_pages_locators import PRICE, BT_BUY_NOW, TOT_PRICE
from i_turbal_folder.hw23.pages.base_page import BasePage




class ItemPage(BasePage):
    @property
    def search_first_price(self):
        return self.driver.find_element(*PRICE)

    def get_first_price(self):
        return self.text(PRICE)


    def click_buy_now(self):
        self.click(BT_BUY_NOW)

    def total_price(self):
        return self.text(TOT_PRICE)