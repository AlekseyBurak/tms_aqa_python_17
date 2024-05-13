import pytest
import time

from pykhtsenko.Lesson23.Homework_23.Pages_homework.main_homework_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestAddItemToCart:

    def test_critical_path(self, main_page):

        # Перейти в каталог
        main_page.find_and_click_catalog()

        # Ввести в поиск "стиральная машина Bosch"
        main_page.input_text_into_search_field(text='стиральная машина Bosch')

        # Проскролить и выбрать 5-ый элемент
        main_page.select_search_element()

        # Добавить выбранный элемент в корзину
        main_page.add_item_to_cart()

        # Перейти в карзину
        main_page.open_cart()

        # Проверить что мы в корзине (провреить тайтл)
        main_page.assert_cart_title(text='Корзина')

        # Сравнить цену товара с суммой заказа
        main_page.assert_price_items_with_order_amount()

        # Проверить что кнопка "Оформить заказ" кликабельна
        main_page.element_is_clickable()