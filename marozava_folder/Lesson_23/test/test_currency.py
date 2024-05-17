import pytest

from marozava_folder.Lesson_23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestCurrency:

    def test_currency_info(self, driver):
        main_page.check_dollar_rate_visible()


