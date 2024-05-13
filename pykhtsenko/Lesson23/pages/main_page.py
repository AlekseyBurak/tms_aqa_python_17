from selenium.webdriver.common.by import By

from pykhtsenko.Lesson23.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, IFRAME, \
    LI_SEARCH_RESULT_FOR_INDEX, BN_CATALOG
from pykhtsenko.Lesson23.pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def currency_button(self):
        return self.driver.find_element(*CURR_INFO)

    @property
    def search_field(self):
        return self.driver.find_element(*IN_SEARCH_FIELD)

    @property
    def search_result(self):
        return self.driver.find_element(*LI_SEARCH_RESULT_FOR_INDEX)

    def get_current_currency_rate(self):
        return self.text(CURR_INFO)

    def go_to_currency_section(self):
        self.click(CURR_INFO)

    def input_into_search_field(self, text: str):
        self.search_field.send_keys(text)
        self.driver.find_element(*IN_SEARCH_FIELD).send_keys(text)

    def chose_from_iframe_by_index(self, index: int):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        locator = By.XPATH, f'(//li[contains(@class, "search__result")])[{index}]'
        self.wait_for(locator)
        self.click(locator)
        self.driver.switch_to.default_content()

    def check_dollar_rate_visible(self):
        rate = self.get_current_currency_rate()
        assert "$" in rate, f"Description, this test failed because of\n{rate=}"

    def click_bn_catalog(self):
        self.click(BN_CATALOG)