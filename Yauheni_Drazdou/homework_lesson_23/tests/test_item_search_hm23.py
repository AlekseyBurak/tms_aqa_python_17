import time

import pytest

from Yauheni_Drazdou.homework_lesson_23.pages.main_page import MainPage
from Yauheni_Drazdou.homework_lesson_23.pages.item_page import ItemPage
from Yauheni_Drazdou.homework_lesson_23.pages.cart_page import CartPage


def test_Nokia_3310(driver):

    main_page = MainPage(driver)
    main_page.search_input("Nokia 3310")
    main_page.choose_from_iframe_by_index()

    item_page = ItemPage(driver)
    item_page.get_product_price()
    print(item_page.get_product_price())
    item_page.add_to_cart()
    time.sleep(3)
    item_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_location() == "Корзина"
    cart_page.item_amount()
    print(cart_page.item_amount())
    assert cart_page.item_amount() == "за 1 товар"
    assert cart_page.check_out().is_enabled()
    cart_page.item_price()
    print(cart_page.item_price())






