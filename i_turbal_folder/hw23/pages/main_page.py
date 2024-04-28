from i_turbal_folder.hw23.pages.base_page import BasePage
from i_turbal_folder.hw23.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, LI_SEARCH_RESULT, IFRAME


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

    def input_into_search_field(self, text: str):
        self.search_field.send_keys(text)

    def chose_from_iframe_by_index(self):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        self.wait_for(LI_SEARCH_RESULT)
        self.click(LI_SEARCH_RESULT)
        self.driver.switch_to.default_content()
