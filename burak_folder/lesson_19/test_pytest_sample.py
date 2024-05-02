import time

import pytest
import allure

my_very_important_module = 4

@pytest.fixture(autouse=True)
def demo():
    print(1)
    yield
    print(2)


class TestPytestMarks:

    @allure.title("LOOOoooooooooooooNG")
    @allure.description("12345")
    @allure.feature("LOOONg")
    @pytest.mark.smoke
    def test_smoke1(self):
        with allure.step("Step one"):
            time.sleep(1)
        with allure.step("Step two"):
            time.sleep(0.5)
        with allure.step("Assertion"):
            assert 1 == 1

    @allure.title("not long")
    @allure.description("12346")
    @allure.feature("not long")
    @pytest.mark.smoke
    def test_smoke2(self):
        time.sleep(1)

        assert True

    @pytest.mark.smoke
    def test_smoke3(self):
        time.sleep(1)

        assert True

    @pytest.mark.smoke
    @pytest.mark.mobile
    def test_android1(self):
        assert True

    @pytest.mark.mobile
    def test_android2(self):
        time.sleep(1)

        assert True

    def test_ios1(self):
        assert True

    def test_ios2(self):
        assert True

    @pytest.mark.e2e
    def test_e2e(self):
        assert True
