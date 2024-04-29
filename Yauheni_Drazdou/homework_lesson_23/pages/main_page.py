import time

from Yauheni_Drazdou.homework_lesson_23.pages.base_page import BasePage
from selenium.webdriver.common.by import By


FAST_SEARCH_FIELD_LOCATOR = By.XPATH, '//input[@class="fast-search__input"]'
ITEM_SEARCH_FIELD_LOCATOR = By.XPATH, '//input[@class="search__input"]'
IFRAME = By.XPATH, '//iframe[@class="modal-iframe"]'
LI_SEARCH_RESULT = By.XPATH, '//li[@class="search__result"]'

class MainPage(BasePage):

    @property
    def search_field(self):
        return self.driver.find_element(*FAST_SEARCH_FIELD_LOCATOR)

    def search_input(self, item: str):
        self.search_field.send_keys(item)


    def choose_from_iframe_by_index(self):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        self.wait_for(LI_SEARCH_RESULT)
        self.click(LI_SEARCH_RESULT)
        self.driver.switch_to.default_content()

    def choose_from_list(self):
        self.driver.find_element(*LI_SEARCH_RESULT)

