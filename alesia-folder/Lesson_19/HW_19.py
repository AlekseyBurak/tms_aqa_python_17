import pytest
import unittest

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
@pytest.fixture(autouse=True)
def calc_init():
    print("\nStart test")
    calc = Calc()
    yield calc
    print("\nThe end")
class TestPytestCalc:
    def test_pytest_add(self, calc_init):
        result = calc_init.calc(3, 4, "+")
        assert result == 7
        assert isinstance(result, int)
        assert result in (6, 7, 8)
    def test_pytest_diff(self, calc_init):
        result = calc_init.calc(4, 3, "-")
        assert result == 1
        assert isinstance(result, int)
        assert result not in (2, 3, 4)
    def test_pytest_mult(self, calc_init):
        result = calc_init.calc(3, 4, "*")
        assert result == 12
        assert isinstance(result, int)
    def test_pytest_div(self, calc_init):
        result = calc_init.calc(12, 4, "/")
        assert result == 3
        assert isinstance(result, float)
