import allure

from Yauheni_Drazdou.homework_lesson_23.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


BN_CHECK_OUT = By.XPATH, "//*[contains(text(),'Перейти к оформлению')]"


LI_ITEM_PRICE = By.XPATH, "(//*[contains(@class, 'cart-form__description')])[9]" #item price
TX_BASKET = By.XPATH, "(//*[contains(text(),'Корзина')])[2]"


FD_AMOUNT = By.XPATH, "//span[contains(text(), 'товар')]"
class CartPage(BasePage):

    @allure.title("Check out button clicability test")
    def check_out(self):
        check_out_button = self.driver.find_element(*BN_CHECK_OUT)
        return check_out_button

    @allure.title("Checking item's amount")
    def item_amount(self):
        amount = self.driver.find_element(*FD_AMOUNT)
        return amount.text

    @allure.title("Checking if item's price in a cart matches the price from  the list")
    def item_price(self):
        price_item = self.driver.find_element(*LI_ITEM_PRICE)
        return price_item.text

    def get_location(self):
        location = self.driver.find_element(*TX_BASKET)
        return location.text

    def check_out_button(self):
        button = self.driver.find_element(*BN_CHECK_OUT)
        return button
