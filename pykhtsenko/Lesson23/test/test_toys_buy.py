import time

import pytest


from pykhtsenko.Lesson23.pages.cart_page import CartPage
from pykhtsenko.Lesson23.pages.item_page import ItemPage
from pykhtsenko.Lesson23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


class ToysLego:

    def test_buy_toys_lego(self, main_page, item_page, cart_page):
        time.sleep(5)
        main_page.input_into_search_field("Конструктор Lego")
        main_page.chose_from_iframe_by_index(1)
        item_price = item_page.get_first_price()
        item_page.add_to_cart()
        item_page.go_to_cart()
        cart_page.check_cart_title()
        cart_page.check_cart_price(expected_price=item_price)
        cart_page.check_cart_items_amount(num_items=1)
        cart_page.check_submit_possible_is_clickable()