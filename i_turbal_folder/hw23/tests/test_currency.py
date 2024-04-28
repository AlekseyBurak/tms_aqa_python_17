import time

import pytest

from i_turbal_folder.hw23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestCurrency:

    def test_currency_info(self, main_page):
        time.sleep(5)
        main_page.check_dollar_rate_visible()