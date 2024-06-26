import allure
from selenium.webdriver.common.by import By
from selevich_tatsiana.HW_23.locators.main_page_locators import IN_SEARCH_FIELD, IFRAME
from selevich_tatsiana.HW_23.pages.base_page import BasePage


class MainPage(BasePage):
    @property
    def search_field(self):
        return self.find(IN_SEARCH_FIELD)

    def input_into_search_field(self, text: str):
        with allure.step("Enter a text to search field"):
            self.search_field.send_keys(text)

    def chose_from_iframe_by_index(self, index: int = 1):
        with allure.step("Choose item from iFrame by index"):
            iframe = self.wait_for(IFRAME)
            self.driver.switch_to.frame(iframe)
            locator = By.XPATH, f'(//div[@class="result__item result__item_product"])[{index}]'
            self.wait_for(locator)
            self.click(locator)
            self.driver.switch_to.default_content()
