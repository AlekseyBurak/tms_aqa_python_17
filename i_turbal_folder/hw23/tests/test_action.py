import time

import allure
import pytest

from i_turbal_folder.hw23.pages.catalog_page import CatalogPage
from i_turbal_folder.hw23.pages.item_and_order_pages import ItemPage
from i_turbal_folder.hw23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@allure.title('Check filters')
@allure.description("Open items list, select filters, open first item and check resulst")
class TestAddFilters:

    def test_add_filters(self, main_page, catalog_page, item_page):
        main_page.click_button_catalog()
        catalog_page.click_onliner_prime()
        catalog_page.go_to_zoo()
        category_of_animal = catalog_page.get_text_of_cat_category()
        catalog_page.select_category_for_cat()
        catalog_page.open_selector_where()
        category_of_placing = catalog_page.get_text_of_checbox_floor()
        catalog_page.select_checkbox_floor()
        catalog_page.open_first_item()
        animal_on_item_page = item_page.get_for_who_text()
        placing_on_item_page = item_page.get_placing_text()
        assert category_of_animal == animal_on_item_page
        assert category_of_placing == placing_on_item_page
