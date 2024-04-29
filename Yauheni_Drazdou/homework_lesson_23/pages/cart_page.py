from Yauheni_Drazdou.homework_lesson_23.pages.base_page import BasePage
from selenium.webdriver.common.by import By

BN_CHECK_OUT = By.XPATH, "//*[@class='button-style button-style_small cart-form__button button-style_primary']]"


LI_ITEM_PRICE = By.XPATH, "//div[@class='cart-form__description cart-form__description_other cart-form__description_base-alter cart-form__description_condensed-other']"
TX_BASKET = By.XPATH, "//*[@class='cart-form__title cart-form__title_base cart-form__title_nocondensed cart-form__title_condensed-special']"


FD_AMOUNT = By.XPATH, "//span[@class='cart-form__description cart-form__description_other cart-form__description_base cart-form__description_font-weight_normal cart-form__description_nowrap']"

class CartPage(BasePage):

    def check_out(self):
        check_out_button = self.driver.find_element(*BN_CHECK_OUT)
        return check_out_button

    def item_amount(self):
        amount = self.driver.find_element(*FD_AMOUNT)
        return amount.text

    def item_price(self):
        price_item = self.driver.find_element(*LI_ITEM_PRICE)
        price_item.click()
        return price_item

    def get_location(self):
        location = self.driver.find_element(*TX_BASKET)
        return location.text

    def check_out_button(self):
        button = self.driver.find_element(*BN_CHECK_OUT)
        return button
