from annayadevich.Lesson_23.locators.currency_locators import CURR_INFO
from annayadevich.Lesson_23.pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def currency_button(self):
        return self.driver.find_element(CURR_INFO)

    def get_current_currency_rate(self):
        return self.text(CURR_INFO)

    def go_to_currency_section(self):
        self.click(CURR_INFO)
        # self.currency_button.click()
