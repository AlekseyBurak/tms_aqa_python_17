import time

import pytest

from i_turbal_folder.hw23.pages.item_and_order_pages import ItemPage
from i_turbal_folder.hw23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)

@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


class TestE2E:

    def test_add_to_card_item(self, main_page, item_page):
        main_page.input_into_search_field("PlayStation 5")
        main_page.chose_from_iframe_by_index()
        first_price_on_item_page = item_page.get_first_price()
        item_page.click_buy_now()
        total_price =item_page.total_price()
        assert total_price == first_price_on_item_page