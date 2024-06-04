import pytest


from marozava_folder.Lesson_23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestBasket:

    def test_add_to_basket(self, main_page: MainPage):
        main_page.input_into_search_field("Dyson Purifier Cool")
        main_page.chose_from_iframe_by_index()
        main_page.consent_button_click()
        main_page.add_to_basket_click()

    def test_price(self, main_page: MainPage):
        main_page.input_into_search_field("Dyson Purifier Cool")
        main_page.chose_from_iframe_by_index()
        main_page.consent_button_click()
        initial_price = main_page.get_initial_price()
        main_page.add_to_basket_click()
        main_page.go_to_basket()
        main_page.driver.implicitly_wait(10)
        basket_price = main_page.get_basket_price()
        assert f"{initial_price} р." == basket_price
        main_page.checkout_click()










