from marozava_folder.Lesson_23.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, IFRAME, \
    LI_SEARCH_RESULT
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
        return self.driver.find_elements(*LI_SEARCH_RESULT)

    def get_current_currency_rate(self):
        return self.text(CURR_INFO)

    def go_to_currency_section(self):
        self.click(CURR_INFO)

    def input_into_search_field(self, text: str):
        self.search_field.send_keys(text)

    def chose_from_iframe_by_index(self, index: int):
        self.driver.switch_to.frame(self.driver.find_element(*IFRAME))
        self.search_result[index - 1].click()
        self.driver.switch_to.default_content()

    def check_dollar_rate_visible(self):
        rate = self.get_current_currency_rate()
        assert "$" in rate, "Description"
