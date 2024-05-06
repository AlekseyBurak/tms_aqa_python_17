import time

import pytest

from annayadevich.Lesson_23.Classwork_23.pages.catalog_page import CatalogPage
from annayadevich.Lesson_23.Classwork_23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


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
