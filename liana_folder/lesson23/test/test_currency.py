import pytest

from liana_folder.lesson23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestCurrency:

    def test_currency_info(self, main_page):
        main_page.check_dollar_visible()



