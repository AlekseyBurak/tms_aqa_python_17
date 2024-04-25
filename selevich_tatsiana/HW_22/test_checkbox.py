import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from urls import SINGLE_CHECKBOX_URL, MULTIPLE_CHECKBOX_URL


def click_checkbox(driver, xpath):
    checkbox = driver.find_element(By.XPATH, xpath)
    checkbox.click()


def click_button(driver):
    button = driver.find_element(By.XPATH, '//input[@id = "submit-id-submit"]')
    button.submit()


@pytest.mark.url(SINGLE_CHECKBOX_URL)
class TestCaseSingleCheckbox:
    def test_marked_checkbox(self, driver):
        click_checkbox(driver, '//input[@id = "id_checkbox_0"]')
        click_button(driver)

        title = driver.find_element(By.XPATH, '//div[@id="result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'Selected checkboxes:' and text.text == 'select me or not'

    def test_unmarked_checkbox(self, driver):
        click_button(driver)

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, '//div[@id="result"]/p[1]')


@pytest.mark.url(MULTIPLE_CHECKBOX_URL)
class TestCaseMultipleCheckbox:
    @pytest.mark.parametrize("checkbox_xpath, result", [
        pytest.param('//input[@id="id_checkboxes_0"]', 'one'),
        pytest.param('//input[@id="id_checkboxes_1"]', 'two'),
        pytest.param('//input[@id="id_checkboxes_2"]', 'three')
    ])
    def test_one_marked_checkbox(self, driver, checkbox_xpath, result):
        click_checkbox(driver, checkbox_xpath)
        click_button(driver)

        title = driver.find_element(By.XPATH, '//div[@id = "result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'Selected checkboxes:' and text.text == result

    @pytest.mark.parametrize("checkbox_xpath1, checkbox_xpath2, result", [
        pytest.param('//input[@id="id_checkboxes_0"]', '//input[@id="id_checkboxes_1"]', 'one, two'),
        pytest.param('//input[@id="id_checkboxes_1"]', '//input[@id="id_checkboxes_2"]', 'two, three'),
        pytest.param('//input[@id="id_checkboxes_0"]', '//input[@id="id_checkboxes_2"]', 'one, three')
    ])
    def test_two_marked_checkbox(self, driver, checkbox_xpath1, checkbox_xpath2, result):
        click_checkbox(driver, checkbox_xpath1)
        click_checkbox(driver, checkbox_xpath2)
        click_button(driver)

        title = driver.find_element(By.XPATH, '//div[@id = "result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'Selected checkboxes:' and text.text == result

    def test_three_marked_checkbox(self, driver):
        click_checkbox(driver, '//input[@id="id_checkboxes_0"]')
        click_checkbox(driver, '//input[@id="id_checkboxes_1"]')
        click_checkbox(driver, '//input[@id="id_checkboxes_2"]')
        click_button(driver)

        title = driver.find_element(By.XPATH, '//div[@id = "result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'Selected checkboxes:' and text.text == 'one, two, three'

    def test_unmarked_checkbox(self, driver):
        click_button(driver)

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, '//div[@id="result"]/p[1]')
