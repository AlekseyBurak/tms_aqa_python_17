from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):  # мы всегда будем работать с браузером
        self.driver: WebDriver = driver

    def click(self, locator: Tuple[str, str], timeout: int = 5):  # Tuple хоть и элемент класса By, но ждет две стринги
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element  # не всегда нужно возвращать, но пусть будет

    def text(self, locator: Tuple[str, str], timeout: int = 5) -> str:
        """
        RETURN text of element
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def wait_for(self, locator: Tuple[str, str], timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
