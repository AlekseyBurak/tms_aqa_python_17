from liana_folder.lesson23.pages.base_page import BasePage
from liana_folder.lesson23.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, IFRAME, SEARCH_RESULT


class MainPage(BasePage):

    @property
    def currency_button(self):
        return self.driver.find_element(*CURR_INFO)

    @property
    def search_field(self):
        return self.driver.find_element(*IN_SEARCH_FIELD)

    @property
    def search_result(self):
        return self.driver.find_element(*SEARCH_RESULT)

    def input_search_field(self, text: str):
        self.search_field.send_keys(text)

    def choose_from_iframe(self):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        self.wait_for(SEARCH_RESULT)
        self.click(SEARCH_RESULT)
        self.driver.switch_to.default_content()

    def get_currency_currency_rate(self):
        return self.text(CURR_INFO)

    def go_to_currency_section(self):
        self.click(CURR_INFO)
        # self.currency_button.click()

    def check_dollar_visible(self):
        rate = self.get_currency_currency_rate()
        assert "$" in rate, "Description"
