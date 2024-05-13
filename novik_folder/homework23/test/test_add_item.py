import time

import pytest
from selenium.webdriver.common.by import By

from novik_folder.homework23.locators.locators import BN_ADD, BN_NAV_TO, LI_OVERFLOW, TXT_ITEM_IN_CART
from novik_folder.homework23.pages import base_page, main_page
from novik_folder.homework23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestPlayStation:

    def test_iphone_15(self, main_page, driver):
        main_page.input_into_search_field("Смартфон Apple iPhone 15 Pro Max 256GB (белый титан)")
        main_page.chose_from_iframe_by_index()
        time.sleep(3)
        main_page.find_button_add_click()
        main_page.wait_for_overflow()
        main_page.navigate_button_and_click()
        main_page.wait_for_items_in_cart()
        assert main_page.find_item_cart_text() == "Смартфон Apple iPhone 15 Pro Max 256GB (белый титан)"







