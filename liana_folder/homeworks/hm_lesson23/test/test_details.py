import pytest

from liana_folder.homeworks.hm_lesson23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestPlaystation:

    def test_playstation(self, main_page):
        main_page.input_search_field("PlayStation 5")
        main_page.choose_from_iframe()



