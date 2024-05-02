import pytest
import time

from liana_folder.homeworks.hm_lesson23.pages.main_page import MainPage
from liana_folder.homeworks.hm_lesson23.pages.product_details import ProductDetails
from liana_folder.homeworks.hm_lesson23.pages.checkout_page import CheckoutDetails


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def product_details_page(driver):
    yield ProductDetails(driver)

@pytest.fixture(autouse=True)
def checkout_details_page(driver):
    yield CheckoutDetails(driver)


class TestPlaystation:

    def test_product_path_to_purchase_playstation(self, main_page, product_details_page, checkout_details_page):
        main_page.input_search_field("PlayStation 5")
        main_page.choose_from_iframe()
        product_details_page.click_accept_button()
        product_details_page.add_product_to_cart()
        product_details_page.go_to_cart()
        title = checkout_details_page.get_title.text
        assert title == "Оформление заказа", "Header is absent"




