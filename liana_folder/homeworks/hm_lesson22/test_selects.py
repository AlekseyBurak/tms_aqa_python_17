import select

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from liana_folder.homeworks.hm_lesson22.locators import URL_SINGLE_SELECT, URL_MULT_SELECT, SL_SINGLE_SELECT, BN_SUBMIT


def select_dropdown_option(driver, element, option):
    dropdown = driver.find_element(*element)
    select = Select(dropdown)
    select.select_by_visible_text(option)


def submit(driver):
    driver.find_element(*BN_SUBMIT).click()


class TestSingleSelect:

    @pytest.mark.parametrize("option, result", [
        pytest.param('Python', 'Python'),
        pytest.param('Ruby', 'Ruby'),
        pytest.param('JavaScript', 'JavaScript'),
        pytest.param('Java', 'Java'),
        pytest.param('C#', 'C#')
    ])
    def test_single_select(self, driver, option, result):
        driver.get(URL_SINGLE_SELECT)
        select_dropdown_option(driver, SL_SINGLE_SELECT, option)
        submit(driver)
        result_text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert result_text.text == result


class TestMultSelect:

    def test_mult_select(self, driver):
        pass
