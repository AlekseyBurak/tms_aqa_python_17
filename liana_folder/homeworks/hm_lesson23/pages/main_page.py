from liana_folder.lesson23.pages.base_page import BasePage
from liana_folder.homeworks.hm_lesson23.locators.locators import IN_SEARCH_FIELD, IFRAME, SEARCH_RESULT


class MainPage(BasePage):

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



