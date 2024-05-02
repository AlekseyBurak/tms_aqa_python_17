import pytest
from selenium.webdriver.common.by import By

from liana_folder.homeworks.hm_lesson22.locators import URL_SINGLE_TEXT_AREA, TA_SINGLE_TEXT_AREA, BN_SUBMIT


def click_submit_button(driver):
    driver.find_element(*BN_SUBMIT).click()


class TestTextArea:

    # specialno with fail
    @pytest.mark.parametrize("value", [
        pytest.param("Text"),
        pytest.param("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
        pytest.param(1),
        pytest.param(1.23),
        pytest.param("@#$%^&*()_+_)(*&^%$<>?/.,"),
        pytest.param(2147483649),
        pytest.param(""),
        pytest.param(" "),
                             ])
    def test_text_area(self, driver, value):
        driver.get(URL_SINGLE_TEXT_AREA)
        text_area = driver.find_element(*TA_SINGLE_TEXT_AREA)
        text_area.send_keys(value)
        click_submit_button(driver)
        result_text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert result_text.text == value
