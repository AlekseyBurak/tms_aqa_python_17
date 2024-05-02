import pytest
import allure


class Calc:
    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"

@pytest.fixture(scope="class", autouse=True)
def class_scope():
    print("\nClass setup")
    yield
    print("\nClass teardown")


class TestPytestCalc:

    @allure.title("test_title_1")
    @allure.id("12345")
    @allure.feature("Feature 123")
    @allure.description("RQ1")
    def test_pytest_calc_1(self):
        calc = Calc()
        result = calc.concatinate(4, 2)
        assert result == 6
        assert isinstance(result, int)

