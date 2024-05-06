import pytest
import allure

from ..pages.main_page import MainPage
from ..pages.product_details import ProductDetails
from ..pages.checkout_page import CheckoutDetails
from ..pages.cart_page import CartPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def product_details_page(driver):
    yield ProductDetails(driver)

@pytest.fixture(autouse=True)
def checkout_details_page(driver):
    yield CheckoutDetails(driver)

@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


class TestPlaystation:

    @allure.id("1")
    @allure.title("E2E")
    @allure.description("Scenario 1: Buy Playstation 5")
    @allure.feature("[JIRA-1]Feature Playstation")
    def test_product_path_to_purchase_playstation(self, main_page, product_details_page, checkout_details_page,
                                                  cart_page):
        main_page.input_search_field("PlayStation 5")
        main_page.choose_from_iframe()
        product_details_page.click_accept_button()
        product_details_page.add_product_to_cart()
        product_details_page.go_to_cart()
        product_details_page.go_to_checkout()
        title = checkout_details_page.get_title
        assert title == "Оформление заказа", f"Expected header text: 'Оформление заказа', Actual: {title}"

    @allure.id("2")
    @allure.title("Check the name of the cart page")
    @allure.description("Scenario 1: Buy Playstation 5")
    @allure.feature("[JIRA-1]Feature Playstation")
    def test_cart_page_title(self, main_page, product_details_page, cart_page):
        main_page.input_search_field("PlayStation 5")
        main_page.choose_from_iframe()
        product_details_page.click_accept_button()
        product_details_page.add_product_to_cart()
        product_details_page.go_to_cart()
        title = cart_page.get_title
        assert title == "Корзина", f"Expected header text: 'Корзина', Actual: {title}"
    @allure.id("3")
    @allure.title("Check the name of the product details page")
    @allure.description("Scenario 1: Buy Playstation 5")
    @allure.feature("[JIRA-1]Feature Playstation")
    def test_product_page_title(self, main_page, product_details_page, cart_page):
        main_page.input_search_field("PlayStation 5")
        main_page.choose_from_iframe()
        product_details_page.click_accept_button()
        title = product_details_page.get_title_product
        assert title == "Игровая приставка Sony PlayStation 5 CFI-1000", \
            f"Expected header text: 'Игровая приставка Sony PlayStation 5 CFI-1000', Actual: {title}"




