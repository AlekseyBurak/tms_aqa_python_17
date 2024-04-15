import py_compile

import pytest


class Calc:
    def calc(self, a: int, b: int, operation: str):
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


@pytest.fixture(scope="module", autouse=True)
def module_test_run():
    print("\nStart test run")
    yield
    print("\nEnd test run")


@pytest.fixture(scope="class", autouse=True)
def start_test_run():
    print("\nStart class test")
    yield
    print("\nEnd class test")


@pytest.fixture(autouse=True)
def calc_init():
    print("\nStart test case")
    calc = Calc()
    yield calc
    print("\nEnd test case")


@pytest.mark.regression
def test_regress():
    print("This test case is in regression scope")


class TestCalcAdd:

    @pytest.mark.regression
    def test_positive_add(self, calc_init):
        result = calc_init.calc(3, 5, "+")
        assert result == 8

    def test_negative_add(self, calc_init):
        result = calc_init.calc(-3, -8, "+")
        assert result == -11


class TestCalcSubt:

    @pytest.mark.regression
    def test_positive_subt(self, calc_init):
        result = calc_init.calc(3, 5, "-")
        assert result == -2

    def test_negative_subt(self, calc_init):
        result = calc_init.calc(-3, -8, "-")
        assert result == 5


class TestCalcMult:

    @pytest.mark.regression
    def test_positive_mult(self, calc_init):
        result = calc_init.calc(3, 5, "*")
        assert result == 15

    def test_negative_mult(self, calc_init):
        result = calc_init.calc(-3, -8, "*")
        assert result == 24


class TestCalcDiv:

    @pytest.mark.regression
    def test_positive_div(self, calc_init):
        result = calc_init.calc(3, 5, "/")
        assert result == 0.6

    @pytest.mark.regression
    def test_positive_divzero(self, calc_init):
        with pytest.raises(ZeroDivisionError):
            result = calc_init.calc(3, 0, "/")

    def test_negative_div(self, calc_init):
        result = calc_init.calc(-3, -8, "/")
        assert result == 0.375
