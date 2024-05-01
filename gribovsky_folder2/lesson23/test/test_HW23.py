import pytest

from gribovsky_folder2.lesson23.pages.cart_page import CartPage
from gribovsky_folder2.lesson23.pages.main_page import MainPage
from gribovsky_folder2.lesson23.pages.product_page import ProductPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def product_page(driver):
    yield ProductPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


class TestBlender:

    def test_blender(self, main_page, product_page, cart_page):
        main_page.input_into_search_field("Xiaomi Blender")
        main_page.chose_from_iframe_by_index()
        primary_price = product_page.return_primary_price()
        product_page.add_to_cart()
        product_page.go_to_cart()
        cart_page.check_url_title()
        cart_page.check_cart_price(primary_price)
        cart_page.check_product_amount(amount=1)
        cart_page.check_submit_order_clickable()


