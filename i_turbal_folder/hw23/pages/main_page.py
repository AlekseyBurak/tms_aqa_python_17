import allure

from i_turbal_folder.hw23.pages.base_page import BasePage
from i_turbal_folder.hw23.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, LI_SEARCH_RESULT, IFRAME, \
    BN_CATALOG


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
        with allure.step("Enter value to the search field"):
            self.search_field.send_keys(text)

    def chose_from_iframe_by_index(self):
        with allure.step("Open first find item"):
            iframe = self.wait_for(IFRAME, 10)
            self.driver.switch_to.frame(iframe)
            self.wait_for(LI_SEARCH_RESULT, 10)
            self.click(LI_SEARCH_RESULT)
            self.driver.switch_to.default_content()

    def click_button_catalog(self):
        with allure.step("Click the Каталог button"):
            self.click(BN_CATALOG)
