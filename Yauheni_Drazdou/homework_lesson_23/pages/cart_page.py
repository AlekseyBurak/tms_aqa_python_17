from Yauheni_Drazdou.homework_lesson_23.pages.base_page import BasePage
from selenium.webdriver.common.by import By

BN_CHECK_OUT = By.XPATH, "//*[contains(text(),'Перейти к оформлению')]"


LI_ITEM_PRICE = By.XPATH, "(//*[contains(@class, 'cart-form__description')])[9]"
TX_BASKET = By.XPATH, "(//*[contains(text(),'Корзина')])[2]"


FD_AMOUNT = By.XPATH, "(//*[contains(@class, 'cart-form__description cart-form__description_base-alter')])[3]"
class CartPage(BasePage):

    def check_out(self):
        check_out_button = self.driver.find_element(*BN_CHECK_OUT)
        return check_out_button

    def item_amount(self):
        amount = self.driver.find_element(*FD_AMOUNT)
        return amount.text

    def item_price(self):
        price_item = self.driver.find_element(*LI_ITEM_PRICE)
        return price_item.text

    def get_location(self):
        location = self.driver.find_element(*TX_BASKET)
        return location.text

    def check_out_button(self):
        button = self.driver.find_element(*BN_CHECK_OUT)
        return button
