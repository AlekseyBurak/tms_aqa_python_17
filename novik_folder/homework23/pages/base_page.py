from typing import Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
    def find_and_click(self, locator: Tuple[str, str]):
        element_on_page = WebDriver.find_element(self.driver, locator)
        element_on_page.click()
        return element_on_page

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

    def wait_for(self, locator: Tuple[str, str], timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

