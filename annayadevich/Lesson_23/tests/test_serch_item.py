import pytest

from annayadevich.Lesson_23.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestPlayStation:

    def test_play_station(self, main_page):
        main_page.input_into_search_field("PlayStation 5")
        main_page.chose_from_iframe_by_index()


        #pytest burak_folder/lesson_23/test/test_hw.py --reruns 3 --reruns-delay 1 - для реранов тестов 