import selenium
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from liana_folder.homeworks.hm_lesson22.locators import URL_SINGLE_CHECKBOX, CH_SINGLE_CHECKBOX, \
    BN_SUBMIT, URL_MULT_CHECKBOXES, CH_ONE_CHECKBOX, CH_TWO_CHECKBOX, CH_THREE_CHECKBOX


def click_checkbox(element):
    element.click()


def click_submit_button(driver):
    driver.find_element(*BN_SUBMIT).click()


class TestSingleCheckbox:

    def test_select_single_checkbox(self, driver):
        driver.get(URL_SINGLE_CHECKBOX)
        single_checkbox = driver.find_element(*CH_SINGLE_CHECKBOX)
        click_checkbox(single_checkbox)
        state_single_checkbox = single_checkbox.get_attribute("data-gtm-form-interact-field-id")
        assert state_single_checkbox == "0", "Attribute 'data-gtm-form-interact-field-id' not found"

    def test_submit_selected_single_checkbox(self, driver):
        driver.get(URL_SINGLE_CHECKBOX)
        single_checkbox = driver.find_element(*CH_SINGLE_CHECKBOX)
        click_checkbox(single_checkbox)
        click_submit_button(driver)
        result = driver.find_element(By.XPATH, '//div[@id="result"]')
        assert result.is_displayed(), "Result div is not displayed"

    def test_default_value_single_checkbox(self, driver):
        driver.get(URL_SINGLE_CHECKBOX)
        single_checkbox = driver.find_element(*CH_SINGLE_CHECKBOX)
        assert not single_checkbox.get_attribute("data-gtm-form-interact-field-id")

    def test_submit_unselected_single_checkbox(self, driver):
        driver.get(URL_SINGLE_CHECKBOX)
        click_submit_button(driver)
        assert not driver.find_elements(By.XPATH, '//div[@id="result"]')


class TestCheckboxes:

    @pytest.mark.parametrize("checkbox_locator", [CH_ONE_CHECKBOX, CH_TWO_CHECKBOX, CH_THREE_CHECKBOX])
    def test_click_checkbox(self, driver, checkbox_locator):
        driver.get(URL_MULT_CHECKBOXES)
        checkbox = driver.find_element(*checkbox_locator)
        click_checkbox(checkbox)
        state_checkbox = checkbox.get_attribute("data-gtm-form-interact-field-id")
        assert state_checkbox == "0", "Attribute 'data-gtm-form-interact-field-id' not found"

    @pytest.mark.parametrize("checkbox_locator, result ", [
        pytest.param(CH_ONE_CHECKBOX, "one"),
        pytest.param(CH_TWO_CHECKBOX, "two"),
        pytest.param(CH_THREE_CHECKBOX, "three")]
                            )
    def test_submit_selected_checkbox(self, driver, checkbox_locator, result):
        driver.get(URL_MULT_CHECKBOXES)
        checkbox = driver.find_element(*checkbox_locator)
        click_checkbox(checkbox)
        click_submit_button(driver)
        result_text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert result_text.text == result


    # need to think about
    # @pytest.mark.parametrize("checkbox_locator1", [CH_ONE_CHECKBOX, CH_TWO_CHECKBOX, CH_THREE_CHECKBOX])
    # @pytest.mark.parametrize("checkbox_locator2", [CH_ONE_CHECKBOX, CH_TWO_CHECKBOX, CH_THREE_CHECKBOX])
    # def test_submit_selected_checkbox1(self, driver, checkbox_locator1, checkbox_locator2):
    #     driver.get(URL_MULT_CHECKBOXES)
    #     checkbox1 = driver.find_element(*checkbox_locator1)
    #     click_checkbox(checkbox1)
    #     checkbox2 = driver.find_element(*checkbox_locator2)
    #     click_checkbox(checkbox2)
    #     click_submit_button(driver)
    #     result = driver.find_element(By.XPATH, '//div[@class="result"]/p[2]')
    #
    #     expected_result = ""
    #     if checkbox_locator1 == CH_ONE_CHECKBOX:
    #         expected_result += "one"
    #     elif checkbox_locator1 == CH_TWO_CHECKBOX:
    #         expected_result += "two"
    #     elif checkbox_locator1 == CH_THREE_CHECKBOX:
    #         expected_result += "three"
    #
    #     if checkbox_locator2 == CH_ONE_CHECKBOX:
    #         expected_result += "one"
    #     elif checkbox_locator2 == CH_TWO_CHECKBOX:
    #         expected_result += "two"
    #     elif checkbox_locator2 == CH_THREE_CHECKBOX:
    #         expected_result += "three"
    #
    #     assert result.text == expected_result

    @pytest.mark.parametrize("checkbox_locator", [CH_ONE_CHECKBOX, CH_TWO_CHECKBOX, CH_THREE_CHECKBOX])
    def test_default_valur_checkbox(self, driver, checkbox_locator):
        driver.get(URL_MULT_CHECKBOXES)
        checkbox = driver.find_element(*checkbox_locator)
        assert not checkbox.get_attribute("data-gtm-form-interact-field-id")

    def test_submit_unselected_single_checkbox(self, driver):
        driver.get(URL_MULT_CHECKBOXES)
        click_submit_button(driver)
        assert not driver.find_elements(By.XPATH, '//div[@id="result"]')

