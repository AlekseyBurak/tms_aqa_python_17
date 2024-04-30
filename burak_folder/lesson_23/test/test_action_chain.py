import time

import pytest

from burak_folder.lesson_23.pages.cart_page import CartPage
from burak_folder.lesson_23.pages.catalog_page import CatalogPage
from burak_folder.lesson_23.pages.item_page import ItemPage
from burak_folder.lesson_23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


class TestAction:

    def test_action(self, main_page, catalog_page, item_page):
        time.sleep(2)
        main_page.click_bn_catalog()
        catalog_page.click_onliner_prime()
        catalog_page.go_to_pet_cosmetics()
        item_page.click_first_select()
        item_page.click_yo()
        item_page.check_yo_clicked()
        time.sleep(10)

