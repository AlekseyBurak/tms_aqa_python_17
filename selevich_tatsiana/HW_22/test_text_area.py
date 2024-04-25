import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from test_checkbox import click_button
from urls import SINGLE_TEXT_AREA_URL, MULTIPLE_TEXT_AREA_URL


@pytest.mark.url(SINGLE_TEXT_AREA_URL)
class TestCaseSingleTextArea:
    def test_single_text_area(self, driver):
        driver.find_element(By.XPATH, '//textarea[@id="id_text_area"]').send_keys('Hey')
        click_button(driver)

        title = driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'You entered' and text.text == 'Hey'

    def test_empty_single_text_area(self, driver):
        driver.find_element(By.XPATH, '//textarea[@id="id_text_area"]')
        click_button(driver)

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')


@pytest.mark.url(MULTIPLE_TEXT_AREA_URL)
class TestCaseMultipleTextArea:
    @pytest.mark.parametrize("first_chapter, second_chapter, third_chapter, result", [
        pytest.param('Hey', 'Test', '123', f'{'Hey'}\n{'Test'}\n{'123'}'),
        pytest.param('Hey', 'Test', '', f'{'Hey'}\n{'Test'}'),
        pytest.param('Hey', '', '123', f'{'Hey'}\n{'123'}'),
        pytest.param('Hey', '', '', f'{'Hey'}')
    ])
    def test_valid_multiple_text_area(self, driver, first_chapter, second_chapter, third_chapter,
                                      result):
        driver.find_element(By.XPATH, '//textarea[@id="id_first_chapter"]').send_keys(first_chapter)
        driver.find_element(By.XPATH, '//textarea[@id="id_second_chapter"]').send_keys(second_chapter)
        driver.find_element(By.XPATH, '//textarea[@id="id_third_chapter"]').send_keys(third_chapter)
        click_button(driver)

        title = driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'You entered' and text.text == result

    @pytest.mark.parametrize("first_chapter, second_chapter, third_chapter", [
        pytest.param('', '', ''),
        pytest.param('', 'Test', ''),
        pytest.param('', '', '123'),
        pytest.param('', 'Test', '123')
    ])
    def test_invalid_multiple_text_area(self, driver, first_chapter, second_chapter, third_chapter):
        driver.find_element(By.XPATH, '//textarea[@id="id_first_chapter"]').send_keys(first_chapter)
        driver.find_element(By.XPATH, '//textarea[@id="id_second_chapter"]').send_keys(second_chapter)
        driver.find_element(By.XPATH, '//textarea[@id="id_third_chapter"]').send_keys(third_chapter)
        click_button(driver)

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')
