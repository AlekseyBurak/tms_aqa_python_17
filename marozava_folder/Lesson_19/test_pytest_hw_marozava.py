import pytest


class Calc:

    def operations(self, a: int, b: int, operation: str):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Error"


@pytest.mark.smoke
def test_smoke():
    assert True


@pytest.fixture(scope="class", autouse=True)
def start_test_run():
    print("\nStart class test")
    yield
    print("\nEnd class test")


@pytest.fixture(scope="module", autouse=True)
def modul_scope():
    print("\nModule setup")
    yield
    print("\nModule teardown")


@pytest.fixture(autouse=True)
def calc_init():
    print("\nStart\n")
    calc = Calc()
    yield calc
    print("\nEnd\n")


class TestPytestCalc:
    def test_pytest_calc_1(self, calc_init):
        calc = calc_init
        result = calc.operations(4, 3, "+")
        assert result == 7

    def test_pytest_calc_2(self, calc_init):
        calc = calc_init
        result = calc.operations(4, 3, "-")
        assert result == 1

    def test_pytest_calc_3(self, calc_init):
        calc = calc_init
        result = calc.operations(4, 3, "*")
        assert result == 12

    def test_pytest_calc_4(self, calc_init):
        calc = calc_init
        result = calc.operations(9, 3, "/")
        assert result == 3

    def test_pytest_calc_5(self, calc_init):
        calc = calc_init
        result = calc.operations(9, 3, "/")
        assert isinstance(result, float)

    @pytest.mark.critical_pass
    def test_division_1(self, calculator_init):
        with pytest.raises(ZeroDivisionError):
            assert calculator_init.calc(8, 0, "/")

    @pytest.mark.critical_pass
    def test_float(self, calculator_init):
        with pytest.raises(TypeError):
            assert calculator_init.calc(8, 1.0, "/")
