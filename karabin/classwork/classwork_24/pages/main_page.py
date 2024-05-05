from karabin.classwork.classwork_24.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, IFRAME, LI_SEARCH_RESULT


from karabin.classwork.classwork_24.locators.main_page_locators import (CURR_INFO, IN_SEARCH_FIELD, IFRAME, BN_CATALOG)
from karabin.classwork.classwork_24.pages.base_page import BasePage


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
        assert "$" in rate, f"Description, this test failed because of\n{rate=}"

    def click_bn_catalog(self):
        self.click(BN_CATALOG)
