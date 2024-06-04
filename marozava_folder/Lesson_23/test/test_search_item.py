import pytest

from marozava_folder.Lesson_23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestPlayStation:

    def test_play_station(self, main_page: MainPage):
        main_page.input_into_search_field("Playstation 5")
        main_page.chose_from_iframe_by_index()