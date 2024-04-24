import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_checkbox import click_button
from urls import SINGLE_SELECT_URL, MULTIPLE_SELECT_URL


def select_option(driver, option_text, dropdown_xpath):
    drop_down = driver.find_element(By.XPATH, dropdown_xpath)
    select = Select(drop_down)
    select.select_by_visible_text(option_text)


@pytest.mark.url(SINGLE_SELECT_URL)
class TestCaseSingleSelection:
    @pytest.mark.parametrize("value, result", [
        pytest.param('Python', 'Python'),
        pytest.param('Ruby', 'Ruby'),
        pytest.param('JavaScript', 'JavaScript'),
        pytest.param('Java', 'Java'),
        pytest.param('C#', 'C#')
    ])
    def test_single_selection(self, driver, value, result):
        select_option(driver, value, '//select[@id="id_choose_language"]')

        click_button(driver)

        title = driver.find_element(By.XPATH, '//div[@id = "result"]/p[1]')
        text = driver.find_element(By.XPATH, '//p[@id="result-text"]')

        assert title.text == 'You selected' and text.text == result

    def test_empty_selection(self, driver):
        click_button(driver)
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, '//div[@id="result"]/p[1]')


@pytest.mark.url(MULTIPLE_SELECT_URL)
class TestCaseMultipleSelection:
    @pytest.mark.parametrize("place, transport, day", [
        pytest.param('Sea', 'Bus', 'Tomorrow'),
        pytest.param('Mountains', 'Car', 'Today'),
        pytest.param('Old town', 'Train', 'Tomorrow'),
        pytest.param('Ocean', 'Train', 'Today'),
        pytest.param('Restaurant', 'Air', 'Next week')
    ])
    def test_multiple_selection(self, driver, place, transport, day):
        select_option(driver, place, '//select[@id="id_choose_the_place_you_want_to_go"]')
        select_option(driver, transport, '//select[@id="id_choose_how_you_want_to_get_there"]')
        select_option(driver, day, '//select[@id="id_choose_when_you_want_to_go"]')

        click_button(driver)

        title = driver.find_element(By.XPATH, '//div[@id = "result"]/p[1]')
        text = driver.find_element(By.XPATH, '//p[@id="result-text"]')

        assert title.text == 'You selected' and text.text == f'to go by {transport.lower()} to the {place.lower()} {day.lower()}'

    def test_empty_selection(self, driver):
        click_button(driver)
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, '//div[@id="result"]/p[1]')

    @pytest.mark.parametrize("place, transport, day", [
        pytest.param('', 'Bus', 'Tomorrow'),
        pytest.param('Mountains', '', 'Next week'),
        pytest.param('Old town', 'Train', ''),
        pytest.param('', '', 'Tomorrow'),
        pytest.param('Restaurant', '', ''),
        pytest.param('', 'Air', '')
    ])
    def test_missed_option(self, driver, place, transport, day):
        select_option(driver, place, '//select[@id="id_choose_the_place_you_want_to_go"]')
        select_option(driver, transport, '//select[@id="id_choose_how_you_want_to_get_there"]')
        select_option(driver, day, '//select[@id="id_choose_when_you_want_to_go"]')

        click_button(driver)

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, '//div[@id="result"]/p[1]')
