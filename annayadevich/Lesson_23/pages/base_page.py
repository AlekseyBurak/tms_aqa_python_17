from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def init(self, driver):
        self.driver = driver

    def click(self, locator: Tuple[str, str], timeout: int = 5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def text(self, locator: Tuple[str, str], timeout: int = 5) -> str:
        """
        RETURN TEXT
        :param locator:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def scroll_to(self):
        pass

    def input(self):
        pass

    def get_title(self):
        pass

    def select(self):
        pass