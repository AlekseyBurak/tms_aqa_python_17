import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import NEW_TAB_LINK_URL, NEW_TAB_BUTTON_URL, NEW_PAGE_URL


def switch_window(driver, original_window):
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


@pytest.mark.url(NEW_TAB_LINK_URL)
class TestCaseNewTabLink:
    def test_click_link(self, driver):
        link = driver.find_element(By.XPATH, '//a[@id="new-page-link"]')

        original_window = driver.current_window_handle
        link.click()
        switch_window(driver, original_window)

        assert driver.current_url == NEW_PAGE_URL


@pytest.mark.url(NEW_TAB_BUTTON_URL)
class TestCaseNewTabButton:
    def test_click_button(self, driver):
        button = driver.find_element(By.XPATH, '//a[@id="new-page-button"]')

        original_window = driver.current_window_handle
        button.click()
        switch_window(driver, original_window)

        assert driver.current_url == NEW_PAGE_URL
