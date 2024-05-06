import time

import pytest

from liana_folder.lesson23.pages.catalog_page import CatalogPage

from liana_folder.lesson23.pages.main_page1 import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


class TestChains:

    def test_action_chain(self, main_page, catalog_page):
        time.sleep(5)
        main_page.click_bn_catalog()
        catalog_page.click_bn_onliner_prime()
        catalog_page.go_to_page_cosmetic()
        main_page.click_first_select()
        main_page.click_yo()
        main_page.click_yo()
        time.sleep(5)
