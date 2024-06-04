from marozava_folder.Lesson_23.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, IFRAME, \
    LI_SEARCH_RESULT, CONSENT_BUTTON, LI_BASKET, INITIAL_PRICE, GO_TO_BASKET, BASKET_PRICE, BU_CHECKOUT
from marozava_folder.Lesson_23.pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def currency_button(self):
        return self.driver.find_element(*CURR_INFO)

    @property
    def search_field(self):
        return self.driver.find_element(*IN_SEARCH_FIELD)

    @property
    def search_result(self):
        return self.driver.find_element(*LI_SEARCH_RESULT)

    def get_current_currency_rate(self):
        return self.text(CURR_INFO)

    def go_to_currency_section(self):
        self.click(CURR_INFO)

    def input_into_search_field(self, text: str):
        self.search_field.send_keys(text)

    def chose_from_iframe_by_index(self):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        self.wait_for(LI_SEARCH_RESULT)
        self.click(LI_SEARCH_RESULT)
        self.driver.switch_to.default_content()

    def check_dollar_rate_visible(self):
        rate = self.get_current_currency_rate()
        assert "$" in rate, "Description"

    def consent_button_click(self):
        self.click(CONSENT_BUTTON)

    def add_to_basket_click(self):
        self.click(LI_BASKET)

    def get_initial_price(self):
        price_element = self.driver.find_element(*INITIAL_PRICE)
        return price_element.text

    def go_to_basket(self):
        self.click(GO_TO_BASKET)

    def get_basket_price(self):
        basket_price = self.driver.find_element(*BASKET_PRICE)
        return basket_price.text

    def checkout_click(self):
        self.click(BU_CHECKOUT)






