import time

from Yauheni_Drazdou.homework_lesson_23.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


FAST_SEARCH_FIELD_LOCATOR = By.XPATH, '//input[@class="fast-search__input"]'
ITEM_SEARCH_FIELD_LOCATOR = By.XPATH, '//input[@class="search__input"]'
IFRAME = By.XPATH, '//iframe[@class="modal-iframe"]'
LI_SEARCH_RESULT = By.XPATH, '//li[@class="search__result"]'

class MainPage(BasePage):

    @property
    def search_field(self):
        return self.driver.find_element(*FAST_SEARCH_FIELD_LOCATOR)

    @allure.title('Input search')
    @allure.severity('Major')
    def search_input(self, item: str):
        with allure.step("Searching for the item"):
            self.search_field.send_keys(item)

    @property
    def research(self):
        return self.driver.find_element(*ITEM_SEARCH_FIELD_LOCATOR)

    def research_input(self, item: str):
        self.research.send_keys(item)

    @allure.title('Choosing product from list')
    @allure.severity('Major')
    def choose_from_iframe_by_index(self):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        self.wait_for(LI_SEARCH_RESULT)
        self.click(LI_SEARCH_RESULT)
        self.driver.switch_to.default_content()

    def choose_from_list(self):
        self.driver.find_element(*LI_SEARCH_RESULT)

